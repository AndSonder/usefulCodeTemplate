""" 2021-1-12 coronaPolvo
this py file is used to produce readme file
I need a codes list for my cpp codes. I use this python file to achieve this
"""

import os
import re

basic_readme_file = """
# usefulCodeTemplate

- coronaPolvo的实用代码模版仓库


> 发现在平时编写代码的时候有很多重复的代码可以利用，所以我使用这个仓库来保存这些代码

"""


# get the file list of projects
def get_file_list():
    file_list = []
    for item in os.listdir('./'):
        if '.' not in item:
            file_list.append('./' + item + '/README.md')
    file_list.reverse()
    return file_list


# read project's readme file and
def get_name_and_produce(file_path):
    f = open(file_path, 'r')
    file = f.read()
    name = re.findall(r'name\{(.*)\}', file, re.M | re.I)
    introduce = re.findall(r'introduce\{(.*)\}', file, re.M | re.I)
    name = name[0] if len(name) > 0 else None
    introduce = introduce[0] if len(introduce) > 0 else None
    return name, introduce


# main function of producing readme file
def produce_readme_file(file_list):
    """
    add code list to basic readme file
    :return: None
    """
    basic = "- [ ] [{}]({})\n{}\n"
    for item in file_list:
        name, introduce = get_name_and_produce(item)
        block = basic.format(name, item, introduce)
        global basic_readme_file
        basic_readme_file += block


def run():
    file_list = get_file_list()
    produce_readme_file(file_list)
    with open('README.md', 'w') as f:
        f.write(basic_readme_file)


run()
