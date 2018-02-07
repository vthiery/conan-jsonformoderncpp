from conans import ConanFile, tools
import os


class JsonForModernCppConan(ConanFile):
    name = "jsonformoderncpp"
    version = "3.1.0"
    description = "JSON for Modern C++ parser and generator from https://github.com/nlohmann/json"
    license = "MIT"
    url = "https://github.com/vthiery/conan-jsonformoderncpp"
    repo_url = "https://github.com/nlohmann/json"
    author = "Vincent Thiery (vjmthiery@gmail.com)"

    def source(self):
        tools.download("%s/blob/v%s/LICENSE.MIT" % (self.repo_url, self.version), "LICENSE.MIT")

        expected_hash = "2b7234fca394d1e27b7e017117ed80b7518fafbb4f4c13a7c069624f6f924673"
        tools.get("%s/releases/download/v%s/include.zip" % (self.repo_url, self.version), sha256=expected_hash)

    def package(self):
        self.copy("*.hpp")
        self.copy("LICENSE.MIT")

