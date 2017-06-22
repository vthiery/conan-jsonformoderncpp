from conans import ConanFile, tools
from conans.tools import download

class JsonForModernCppConan(ConanFile):
    name = "jsonformoderncpp"
    version = "2.1.1"
    description = "JSON for Modern C++ parser and generator from https://github.com/nlohmann/json"
    license = "MIT"
    url = "https://github.com/vthiery/conan-jsonformoderncpp"
    author = "Vincent Thiery (vjmthiery@gmail.com)"
    settings = "compiler"

    def configure(self):
        if self.settings.compiler == "gcc" and not str(self.settings.compiler.version) in ["4.9", "5.3", "5.4", "6.1", "6.2", "6.3"]:
            raise Exception("Old gcc < 4.9 versions are not supported")
        if self.settings.compiler == "Visual Studio" and not str(self.settings.compiler.version) in ["14", "15"]:
            raise Exception("Old Visual Studio < 14 versions are not supported")
        if self.settings.compiler == "clang" and not str(self.settings.compiler.version) in ["3.4", "3.5", "3.6", "3.7", "3.8", "3.9", "4.0"]:
            raise Exception("Old clang < 3.4 versions are not supported")
        if self.settings.compiler == "apple-clang" and not str(self.settings.compiler.version) in ["6.4", "7.0", "7.3", "8.0", "8.1", "8.2", "8.3"]:
            raise Exception("Old apple-clang < 6.4 versions are not supported")

    def source(self):
        download("https://github.com/nlohmann/json/releases/download/v%s/json.hpp" % self.version, "json.hpp")

    def build(self):
        # as there is no LICENSE file, lets extract and generate it.
        # It is useful for package consumers, so they can collect all license from all dependencies
        tmp = tools.load("json.hpp")
        license_contents = tmp[2:tmp.find("*/", 1)]
        tools.save("LICENSE", license_contents)

    def package(self):
        self.copy("*.hpp", dst="include")
        self.copy("LICENSE")

    def package_info(self):
        self.cpp_info.libdirs = []
        self.cpp_info.bindirs = []
