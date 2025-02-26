#include "pysubconverter.hpp"

#include <filesystem>
#include <string>

#include "subconverter/handler/settings.h"
#include "subconverter/utils/system.h"

namespace fs = std::filesystem;

namespace _core {
void cd(const std::string &dir) {
    try {
        fs::current_path(fs::canonical(dir));
    }
    catch (const fs::filesystem_error &e) {
        throw std::runtime_error(e.what());
    }
}

void init_config(const std::string &configDir) {
    cd(configDir);
    if (!fileExist(global.prefPath)) {
        if (fileExist("pref.toml"))
            global.prefPath = "pref.toml";
        else if (fileExist("pref.yml"))
            global.prefPath = "pref.yml";
        else if (!fileExist("pref.ini")) {
            if (fileExist("pref.example.toml")) {
                fileCopy("pref.example.toml", "pref.toml");
                global.prefPath = "pref.toml";
            }
            else if (fileExist("pref.example.yml")) {
                fileCopy("pref.example.yml", "pref.yml");
                global.prefPath = "pref.yml";
            }
            else if (fileExist("pref.example.ini"))
                fileCopy("pref.example.ini", "pref.ini");
        }
    }
    readConf();
    if (!global.updateRulesetOnRequest)
        refreshRulesets(global.customRulesets, global.rulesetsContent);

    std::string env_api_mode = getEnv("API_MODE");
    std::string env_managed_prefix = getEnv("MANAGED_PREFIX");
    std::string env_token = getEnv("API_TOKEN");
    global.APIMode = tribool().parse(toLower(env_api_mode)).get(global.APIMode);
    if (!env_managed_prefix.empty())
        global.managedConfigPrefix = env_managed_prefix;
    if (!env_token.empty())
        global.accessToken = env_token;
}

std::string pysubconverter(const std::map<std::string, std::string> &arguments) {
    Request request;
    for (auto &item : arguments) {
        request.argument.emplace(item.first, item.second);
    }
    Response response;
    return subconverter(request, response);
}
} // namespace _core
