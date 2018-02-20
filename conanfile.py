from conans import ConanFile, tools
import os


class JsonForModernCppConan(ConanFile):
    name = "jsonformoderncpp"
    version = "3.1.1"
    description = "JSON for Modern C++ parser and generator from https://github.com/nlohmann/json"
    license = "MIT"
    url = "https://github.com/vthiery/conan-jsonformoderncpp"
    repo_url = "https://github.com/nlohmann/json"
    author = "Vincent Thiery (vjmthiery@gmail.com)"

    def source(self):
        tools.download("%s/blob/v%s/LICENSE.MIT" % (self.repo_url, self.version), "LICENSE.MIT")

        expected_hash = "fde771d4b9e4f222965c00758a2bdd627d04fb7b59e09b7f3d1965abdc848505"
        tools.get("%s/releases/download/v%s/include.zip" % (self.repo_url, self.version), sha256=expected_hash)

    def package(self):
        self.copy("*.hpp")
        self.copy("LICENSE.MIT")

