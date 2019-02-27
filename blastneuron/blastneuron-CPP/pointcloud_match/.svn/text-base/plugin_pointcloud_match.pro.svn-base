
TEMPLATE      = lib
CONFIG       += plugin warn_off

V3DMAINPATH = ../../../v3d_external/v3d_main
INCLUDEPATH  += $$V3DMAINPATH/basic_c_fun
INCLUDEPATH  += $$V3DMAINPATH/jba/newmat11

LIBS += -L$$V3DMAINPATH/jba/c++ -lv3dnewmat

HEADERS      += $$V3DMAINPATH/basic_c_fun/v3d_message.h
HEADERS      += $$V3DMAINPATH/basic_c_fun/basic_surf_objs.h
HEADERS      += q_pointcloud_match_basic.h
HEADERS      += q_pointcloud_match_initialmatch.h
HEADERS      += q_pointcloud_match_refinematch_manifold.h
HEADERS      += q_pointcloud_match_refinematch_affine.h
HEADERS      += q_pointcloud_match.h
HEADERS      += q_pointcloud_match_dialogs.h
HEADERS      += plugin_pointcloud_match.h

SOURCES      += $$V3DMAINPATH/basic_c_fun/v3d_message.cpp
SOURCES      += $$V3DMAINPATH/basic_c_fun/basic_surf_objs.cpp
#SOURCES      += $$V3DMAINPATH/basic_c_fun/io_ano_file.cpp
SOURCES      += q_pointcloud_match_basic.cpp
SOURCES      += q_pointcloud_match_initialmatch.cpp
SOURCES      += q_pointcloud_match_refinematch_manifold.cpp
SOURCES      += q_pointcloud_match_refinematch_affine.cpp
SOURCES      += q_pointcloud_match.cpp
SOURCES      += q_pointcloud_match_dialogs.cpp
SOURCES      += plugin_pointcloud_match.cpp

TARGET        = $$qtLibraryTarget(plugin_pointcloud_match)


#DESTDIR       = ../../v3d_main/v3d/plugins/unfinished/pointcloud_matcher/ #win32 qmake couldn't handle space in path

