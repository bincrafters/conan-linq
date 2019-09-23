#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class LinqConan(ConanFile):
    name = "linq"
    version = "2.0"
    description = "Linq for list comprehension in C++"
    homepage = "https://github.com/pfultz2/Linq"
    topics = ("linq", "list-comprehension", "ranges")
    url = "https://github.com/bincrafters/conan-linq"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "BSL-1.0"
    no_copy_source = True
    requires = "boost/1.68.0@conan/stable"
    _source_subfolder = "source_subfolder"

    def source(self):
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = "Linq-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy("*.h", dst="include", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
