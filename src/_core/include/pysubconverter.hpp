#pragma once

#include "subconverter/handler/interfaces.h"

namespace _core {

std::string pysubconverter(const std::map<std::string, std::string>& arguments);

void init_config(const std::string& configDir);

} // namespace _core
