# neuron retrieval
# by Yinan Wan
# 20120313

TEMPLATE = app
CONFIG += qt warn_off
CONFIG -= app_bundle
CONFIG += debug

V3DMAINPATH = ../../../v3d_external/v3d_main
INCLUDEPATH += $$V3DMAINPATH/basic_c_fun
INCLUDEPATH += $$V3DMAINPATH/common_lib/include

HEADERS += $$V3DMAINPATH/basic_c_fun/v3d_message.h
HEADERS += $$V3DMAINPATH/basic_c_fun/basic_surf_objs.h

SOURCES += $$V3DMAINPATH/basic_c_fun/v3d_message.cpp
SOURCES += $$V3DMAINPATH/basic_c_fun/basic_surf_objs.cpp
SOURCES += main_retrieve.cpp
SOURCES += neuron_retrieve.cpp
SOURCES += compute_morph.cpp
SOURCES += compute_gmi.cpp
SOURCES += prune_short_branch.cpp
