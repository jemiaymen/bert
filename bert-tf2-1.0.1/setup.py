# coding=utf-8
# Copyright 2018 The Google AI Language Team Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Install BERT."""
from setuptools import find_packages
from setuptools import setup

setup(
    name='bert-tf2',
    version='1.0.1',
    description='BERT',
    author='Google Inc.',
    author_email='no-reply@google.com',
    url='https://github.com/jemiaymen/bert',
    license='Apache 2.0',
    packages=find_packages(),
    install_requires=[
        'six',
    ],
    extras_require={
        'tensorflow': ['tensorflow>=2.1.0'],
        'tensorflow_gpu': ['tensorflow-gpu>=2.1.0'],
        'tensorflow-hub': ['tensorflow-hub>=0.8.0'],
    },
)
