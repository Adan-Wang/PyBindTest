#include<iostream>
#include "pybind11/pybind11.h"

//Remember to add pybind11 and python directories into include path, and add python39/libs/ into library path (VS is in project properties)


namespace py = pybind11;

int main() {
	std::cout << "Hello World" << std::endl;

	return 0;
}

int add(int i, int j) {
	return i * j;
}

PYBIND11_MODULE(cppAdd, m) {
	m.doc() = "Pybind11 test plugin";
	m.def("add", &add, "A function that multiplies two numbers in C++");
}