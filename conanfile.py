from conans import ConanFile
from conans.tools import download

class JsonForModernCppConan(ConanFile):
    name = "jsonformoderncpp"
    version = "2.1.1"
    description = "JSON for Modern C++ parser and generator from https://github.com/nlohmann/json"
    license = "MIT"
    url = "https://github.com/vthiery/conan-jsonformoderncpp"
    author = "Vincent Thiery (vjmthiery@gmail.com)"

    def source(self):
        download("https://github.com/nlohmann/json/releases/download/v%s/json.hpp" % self.version, "json.hpp")

    def package(self):
        self.copy("*.hpp", dst="include")

    def package_info(self):
        self.cpp_info.libdirs = []
        self.cpp_info.bindirs = []
