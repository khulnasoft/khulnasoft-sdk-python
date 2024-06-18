#!/usr/bin/env python
# coding=utf-8
#
# Copyright © 2011-2024 KhulnaSoft, Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from os import path
import logging

from khulnasoftlib.searchcommands import environment
from khulnasoftlib import searchcommands

package_directory = path.dirname(path.realpath(__file__))
project_root = path.dirname(path.dirname(package_directory))


def rebase_environment(name):
    environment.app_root = path.join(package_directory, 'apps', name)
    logging.Logger.manager.loggerDict.clear()
    del logging.root.handlers[:]

    environment.khulnasoftlib_logger, environment.logging_configuration = environment.configure_logging('khulnasoftlib')
    searchcommands.logging_configuration = environment.logging_configuration
    searchcommands.khulnasoftlib_logger = environment.khulnasoftlib_logger
    searchcommands.app_root = environment.app_root
