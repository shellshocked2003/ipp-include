from conans import ConanFile, CMake, tools

class mklDynamic(ConanFile):
    name = "ipp-include"
    version = "2019.4"
    url = "https://github.com/shellshocked2003/ipp-include"
    homepage = "https://anaconda.org/anaconda/ipp-include"
    author = "Michael Gardner <mhgardner@berkeley.edu>"
    license = "Intel Simplified Software License"   
    settings = "os", "compiler", "build_type", "arch"
    description = "Intel Integrated Performance Primitives Header files"
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    build_policy = "missing"

    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self._build_subfolder)
        return cmake    
    
    def build(self):
        if self.settings.os == "Windows":
            url = ("https://anaconda.org/intel/ipp-include/2019.4/download/win-64/ipp-include-2019.4-intel_245.tar.bz2")
        elif self.settings.os == "Macos":
            url = ("https://anaconda.org/intel/ipp-include/2019.4/download/osx-64/ipp-include-2019.4-intel_233.tar.bz2")
        elif self.settings.os == "Linux":
            url = ("https://anaconda.org/intel/ipp-include/2019.4/download/linux-64/ipp-include-2019.4-intel_243.tar.bz2")
        else:
            raise Exception("Binary does not exist for these settings")
        tools.get(url, destination=self._source_subfolder)

    def package(self):
        self.copy("LICENSE.txt", dst="licenses", src=self._source_subfolder + "/info")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
