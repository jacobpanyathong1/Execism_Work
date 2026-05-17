cmake_minimum_required(VERSION 3.0.0)
project(MyCMakeproject VERSION 0.1.0 LANGUAGES C CXX)

INCLUDE (CTest)
enable_testing()

add_executable(MyCmakeproject mycppcode.cpp)

