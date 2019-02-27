Before you run the comparison pipeline, make sure you have your neuron database stored in database.ano file

Please follow the instructions to set up the neuron comparison pipeline

1. run "build_pipeline.sh" script to get executable applications
2. go to global_cmp folder, run
	./batch_compute -i <database.ano> -o <featurebase.nfb>
	This will give you a featurebase .nfb file. Once you got the featurebase, you can start the pipeline from the featurebase rather than neurons

To run retrieve and comparison, assume you have your query query.swc file. run:
	./blastneuron_main.sh <featurebase.nfb> <query.swc> <candidate_num> <output_folder>
	Example: ./blastneuron_main.sh featurebase.nfb query.swc 5 outdata

The result will be stored in the output_folder.

Enjoy running BlastNeuron :)
