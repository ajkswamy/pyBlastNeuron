//main function for neuron comparison
//a test function to automatically retrieve similar neurons, without pre-specified number
//by Yinan Wan
//2012-03-14

#ifdef DISABLE_V3D_MSG
	#define DISABLE_V3D_MSG
#endif

#include "basic_surf_objs.h"
#include <unistd.h>
#include "neuron_retrieve.h"
#include "batch_compute.h"
#include <QtGlobal>
#include <vector>
using namespace std;

void printHelp();

extern char *optarg;
extern int optind, opterr;

int main(int argc, char *argv[])
{
	if  (argc <=1)
	{
		printHelp();
		return 0;
	}

	//read arguments
	char *dfile_database = NULL;
	char *dfile_query = NULL;
	char *dfile_result = NULL;
	int norm_code = 2;//normalization method. 1: rank; 2: whitening
	int retrieved_num = 2;
	double thres = 0.1;

	int c;
	static char optstring[] = "hi:o:";
	opterr = 0;
	while ((c = getopt(argc, argv, optstring))!=-1)
	{
		switch (c)
		{
			case 'h':
				printHelp();
				return 0;
				break;
			case 'i':
				if (strcmp(optarg,"(null)")==0 || optarg[0]=='-')
				{
					fprintf(stderr, "Found illegal or NULL parameter for the option -i.\n");
					return 1;
				}
				dfile_database = optarg;
				break;
			case 'o':
				if (strcmp(optarg,"(null)")==0 || optarg[0]=='-')
				{
					fprintf(stderr, "Found illegal or NULL parameter for the option -o.\n");
					return 1;
				}
				dfile_result = optarg;
				break;
			case '?':
				fprintf(stderr,"Unknown option '-%c' or incomplete argument lists.\n",optopt);
				return 1;
				break;
		}
	}

	//read database file
	QStringList nameList;
	V3DLONG neuronNum;
	QString qs_database(dfile_database);
	vector<NeuronTree> nt_list;

	qs_database = qs_database.simplified();
	if (qs_database.endsWith(".ano") || qs_database.endsWith(".ANO"))
	{
		printf("(0). reading a linker file.\n");
		P_ObjectFileType linker_object;
		if (!loadAnoFile(QString(dfile_database),linker_object))
		{
			fprintf(stderr,"Error in reading the linker file.\n");
			return 1;
		}
		nameList = linker_object.swc_file_list;
		neuronNum = nameList.size();
		for (V3DLONG i=0;i<neuronNum;i++)
		{
			NeuronTree tmp = readSWC_file(nameList.at(i));
			nt_list.push_back(tmp);
		}
	}
	else if (qs_database.endsWith(".swc") || qs_database.endsWith(".SWC"))
	{
		printf("(0). reading a list of swc file names.\n");
		nameList = qs_database.split(" ");
		neuronNum = nameList.size();
		for (V3DLONG i=0;i<neuronNum;i++)
		{
			NeuronTree tmp = readSWC_file(nameList.at(i));
			nt_list.push_back(tmp);
		}
	}
	else {
		fprintf(stderr, "the reference file/list you specified is not supported.\n");
		return 1;
	}

	QString outfile(dfile_result);
	if (!dfile_result)
	{
		outfile = qs_database + "features.nfb";
	}

	QList<double*> morph_list, gmi_list;
	if (!batch_compute(nt_list, morph_list, 1))
	{
		fprintf(stderr,"Error in batch_compute!\n");
		return 1;
	}
	if (!batch_compute(nt_list, gmi_list, 2))
	{
		fprintf(stderr,"Error in batch_compute!\n");
		return 1;
	}
	//output a neuron featurebase (.nfb) file
	FILE * fp;
	fp = fopen(qPrintable(outfile), "w");
	for (V3DLONG i=0;i<neuronNum;i++)
	{
		fprintf(fp, qPrintable("SWCFILE=" + nameList.at(i)));
		fprintf(fp, "\n");
		for (int j=0;j<21;j++)
			fprintf(fp,"%.4f\t", morph_list[i][j]);
		fprintf(fp,"\n");
		for (int j=0;j<14;j++)
			fprintf(fp,"%.4f\t", gmi_list[i][j]);
		fprintf(fp,"\n");
	}
	fclose(fp);


	for (V3DLONG i=0;i<neuronNum;i++)
	{
		if (morph_list[i]) {delete []morph_list[i]; morph_list[i]=NULL;}
		if (gmi_list[i]) {delete []gmi_list[i]; gmi_list[i]=NULL;}
	}

	return 0;
}

void printHelp()
{
	printf("\nBatch Compute: compute and record the neuron features (morph & gmi). by Yinan Wan.\n\n");
	printf("Usage:\n");
	printf("\t -i <database_file(s)>         input linker file (.ano) or file name list(\"a.swc b.swc\")\n");
	printf("\t -o <output_file>              name of the output file, which will be neuron featurebase (.nfb) file.\n");
	printf("\t                               default result will be generated under the same directory of the query file and has a name of 'databaseName_features.nfb'.\n");
	printf("\t -h                            print this message.\n\n");
	printf("Example: ./batch_compute -i mydatabase.ano -o features.nfb\n\n");
}
