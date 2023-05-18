from glob import glob
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "cppAdd",
        sorted(glob("CppDriver/CppDriver/*.cpp")),
    )
]

setup(name ='test',
    version='1.0'
    ,ext_modules=ext_modules,
    python_requires=">3.7",
    zip_safe=False,
    cmdclass = {"build_ext": build_ext}
    )