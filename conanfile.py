from conans import ConanFile, CMake, tools
import os

class JsondtoConan(ConanFile):
    name = "json_dto"
    version = "0.2.9.2"
    license = "BSD-3-Clause"
    author = "Stiffstream info@stiffstream.com"
    url = "https://github.com/Stiffstream/json_dto-conan"
    description = "A small header-only helper for converting data between json representation and c++ structs"
    topics = ("JSON", "DTO", "Serialization")
    generators = "cmake"

    _cmake = None
    
    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def requirements(self):
        self.requires("rapidjson/1.1.0")

    def source(self):
        # https://github.com/Stiffstream/json_dto/archive/v.0.2.8.tar.gz
        source_url = "https://github.com/Stiffstream/json_dto/archive"
        tools.get("{0}/v.{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-v." + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        if self._cmake:
            return self._cmake
        self._cmake = CMake(self)
        cmake.definitions['JSON_DTO_INSTALL'] = True
        cmake.definitions['JSON_DTO_FIND_DEPS'] = False
        cmake.configure(source_folder = self._source_subfolder + "/dev/json_dto")
        
    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        self.copy("license*", src=self.source_subfolder, dst="licenses", ignore_case=True, keep_path=False)

    def package_id(self):
        self.info.header_only()
