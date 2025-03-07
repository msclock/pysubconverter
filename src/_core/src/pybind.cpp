#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "_core.hpp"
#include "pysubconverter.hpp"

namespace py = pybind11;

PYBIND11_MODULE(_core, m) {
    m.doc() = R"pbdoc(
      Pybind11 _core plugin
      -----------------------
      .. currentmodule:: _core
    )pbdoc";

    m.def("version", []() { return _core::ProjectVersion(); }, R"pbdoc(
        The _core plugin version.
    )pbdoc");

    m.def("subconverter", _core::pysubconverter, py::arg("arguments"), py::doc(R"pbdoc(convert to subscription format

Args:
    arguments (dict): subscription conversion arguments.
Returns:
    str: converted subscription.)pbdoc"));

    m.def("init_config",
          _core::init_config,
          py::arg("dir"),
          py::doc(R"pbdoc(initialize the configuration directory from subconverter.)pbdoc"));
}
