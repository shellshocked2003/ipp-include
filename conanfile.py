from conans import ConanFile, CMake, tools
import os

class mklDynamic(ConanFile):
    name = "ipp-include"
    version = "2019.4"
    url = "https://github.com/shellshocked2003/ipp-include"
    homepage = "https://anaconda.org/anaconda/ipp-include"
    author = "Michael Gardner <mhgardner@berkeley.edu>"
    license = "Intel Simplified Software License"
    settings = {"os": None, "compiler": None, "build_type": None, "arch": ["x86_64"]}
    description = "Intel Integrated Performance Primitives Header files"
    no_copy_source = True
    build_policy = "missing"

    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "source_subfolder"

    # def _configure_cmake(self):
    #     cmake = CMake(self)
    #     cmake.configure(build_folder=self._build_subfolder)
    #     return cmake    
    
    def source(self):
        source_url = ""        
        if self.settings.os == "Windows":
            source_url = ("https://anaconda.org/intel/ipp-include/2019.4/download/win-64/ipp-include-2019.4-intel_245.tar.bz2")
        elif self.settings.os == "Macos":
            source_url = ("https://anaconda.org/intel/ipp-include/2019.4/download/osx-64/ipp-include-2019.4-intel_233.tar.bz2")
        elif self.settings.os == "Linux":
            source_url = ("https://anaconda.org/intel/ipp-include/2019.4/download/linux-64/ipp-include-2019.4-intel_243.tar.bz2")
        else:
            raise Exception("Binary does not exist for these settings")
        
        tools.get(source_url, destination=self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "include")
        self.copy("LICENSE.txt", dst="licenses", src=self._source_subfolder + "/info")        
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
