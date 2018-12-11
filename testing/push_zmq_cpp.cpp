/*https://github.com/zeromq/cppzmq


Build instructions
Build steps:

Build libzmq via cmake. This does an out of source build and installs the build files

download and unzip the lib, cd to directory
mkdir build
cd build
cmake ..
sudo make -j4 install
Build cppzmq via cmake. This does an out of source build and installs the build files

download and unzip the lib, cd to directory
mkdir build
cd build
cmake ..
sudo make -j4 install
Using this:

A cmake find package scripts is provided for you to easily include this library. Add these lines in your CMakeLists.txt to include the headers and library files of cpp zmq (which will also include libzmq for you).

#find cppzmq wrapper, installed by make of cppzmq
find_package(cppzmq)
target_link_libraries(*Your Project Name* cppzmq)

*/

zmq::context_t ctx (1);
zmq::socket_t s (ctx, ZMQ_PUB);
s.connect ("tcp://127.0.0.1:5555");
len_ = ss.length()+1
zmq::message_t msg (len_);
memset(msg.data(),ss, len_);
s.send_string(msg);