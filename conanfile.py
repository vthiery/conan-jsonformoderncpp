from conans import ConanFile, CMake, tools
import os


class JsonForModernCppConan(ConanFile):
    name = "jsonformoderncpp"
    version = "3.2.0"
    settings = "os", "compiler", "arch", "build_type"
    description = "JSON for Modern C++ parser and generator from https://github.com/nlohmann/json"
    license = "MIT"
    url = "https://github.com/vthiery/conan-jsonformoderncpp"
    repo_url = "https://github.com/nlohmann/json"
    author = "Vincent Thiery (vjmthiery@gmail.com)"

    def source(self):
        tools.get("%s/archive/v%s.zip" % (self.repo_url, self.version))

    def build(self):
        cmake = CMake(self)
        cmake.definitions["JSON_BuildTests"] = False
        cmake.definitions["JSON_MultipleHeaders"] = True
        cmake.configure(source_folder="json-%s" % self.version)
        cmake.install()

    def package(self):
        self.copy("LICENSE.MIT", src="json-%s" % self.version)

    def package_id(self):
        self.info.header_only()
