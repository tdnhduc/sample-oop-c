cmake_minimum_required(VERSION 2.8.9)
project(shape)

set(CMAKE_CXX_STANDARD 14)

include_directories(include)
  
file(GLOB SOURCES "src/*.cpp")
 
add_executable(shape ${SOURCES})



