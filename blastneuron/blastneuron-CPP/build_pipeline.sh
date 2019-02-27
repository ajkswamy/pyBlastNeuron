cd neuron_retrieve
qmake batch_compute.pro
make -j4
qmake neuron_retrieve.pro
make -j4
cd ../tree_matching
make
cd ../pointcloud_match
qmake main_pointcloud_match.pro
make -j4
cd ../prune_short_branch
qmake prune_short_branch.pro
make -j4
cd ..
