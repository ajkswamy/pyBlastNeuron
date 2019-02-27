//main function for neuron comparison
//by Yinan Wan
//2012-03-13

#ifdef DISABLE_V3D_MSG
	#define DISABLE_V3D_MSG
#endif

#include "basic_surf_objs.h"
#include <unistd.h>
#include "neuron_retrieve.h"
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
	int cand = 0; //retrieved candidate number
	int feature_code = 1;//feature ext. strategy. 1: morphological; 2: moment
	int norm_code = 1;//normalization method. 1: rank; 2: whitening

	int c;
	static char optstring[] = "hd:q:o:n:f:m:";
	opterr = 0;
	while ((c = getopt(argc, argv, optstring))!=-1)
	{
		switch (c)
		{
			case 'h':
				printHelp();
				return 0;
				break;
			case 'd':
				if (strcmp(optarg,"(null)")==0 || optarg[0]=='-')
				{
					fprintf(stderr, "Found illegal or NULL parameter for the option -d.\n");
					return 1;
				}
				dfile_database = optarg;
				break;
			case 'q':
				if (strcmp(optarg,"(null)")==0 || optarg[0]=='-')
				{
					fprintf(stderr, "Found illegal or NULL parameter for the option -q.\n");
					return 1;
				}
				dfile_query = optarg;
				break;
			case 'o':
				if (strcmp(optarg,"(null)")==0 || optarg[0]=='-')
				{
					fprintf(stderr, "Found illegal or NULL parameter for the option -o.\n");
					return 1;
				}
				dfile_result = optarg;
				break;
			case 'n':
				if (strcmp(optarg,"(null)")==0 || optarg[0]=='-')
				{
					fprintf(stderr, "Found illegal or NULL parameter for the option -n.\n");
					return 1;
				}
				cand = atoi(optarg);
				if (cand<=0)
				{
					fprintf(stderr, "Illegal candidate number. It must>0.\n");
				}
				break;
			case 'f':
				if (strcmp(optarg,"(null)")==0 || optarg[0]=='-')
				{
					fprintf(stderr, "Found illegal or NULL parameter for the option -f.\n");
					return 1;
				}
				feature_code = atoi(optarg);
				if (feature_code<0)
				{
					fprintf(stderr, "Illegal feature method code. It must>=0.\n");
				}
				break;
			case 'm':
				if (strcmp(optarg,"(null)")==0 || optarg[0]=='-')
				{
					fprintf(stderr, "Found illegal or NULL parameter for the option -m.\n");
					return 1;
				}
				norm_code = atoi(optarg);
				if (norm_code<0)
				{
					fprintf(stderr, "Illegal normalization method code. It must>=0.\n");
				}
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

	//read query file
	QString qs_query(dfile_query);
	NeuronTree query = readSWC_file(qs_query);

	//read output file
	QString outfileName(dfile_result);
	if (dfile_result==NULL)
		outfileName = qs_query+QString("_retrieved.ano");

	vector<V3DLONG> retrieved_id;
	if (!neuron_retrieve(nt_list, query, retrieved_id, cand, feature_code, norm_code))
	{
		fprintf(stderr,"Error in neuron_retrieval.\n");
		return 1;
	}
	if (!print_result(retrieved_id, qPrintable(outfileName), nameList, qPrintable(qs_database), qPrintable(qs_query)))
	{
		fprintf(stderr, "Error in print_result.\n");
		return 1;
	}

	return 0;
}

void printHelp()
{
	printf("\nNeuron Comparison: given a query neuron, retrieve certain number of candidates from a database. by Yinan Wan.\n\n");
	printf("Usage:\n");
	printf("\t -d <database_file(s)>         input linker file (.ano) or file name list(\"a.swc b.swc\")\n");
	printf("\t -q <query_file>               query neuron file (.swc)\n");
	printf("\t -n <candidate_number>         number of candidates you want to retrive.\n");
	printf("\t -o <output_file>              name of the output file, which will be a swc linker file.\n");
	printf("\t                               default result will be generated under the same directory of the query file and has a name of 'queryFileName_retrieved.ano'.\n");
	printf("\t -f <feature_method>           the method to extract feature vector.\n");
	printf("\t                               f=1: global morphological feature [default]; f=1: geometric moment invariant.\n");
	printf("\t -m <normalization_method>     normalization method\n");
	printf("\t                               m=1: ranking [default]; m=2: whitening.\n");
	printf("\t -h                            print this message.\n\n");
	printf("Example: ./neuron_retrieve -d mylinker.ano -q query.swc -n 10 -o result.txt -f 1 -m 1\n\n");
}
