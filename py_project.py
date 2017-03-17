import sys
import time

AUTHOR = "Ondrej Zapletal"


def gen_func_prot(name, params="", ind=0):
    """ Function returns properly indeted code """
    func_text = ""

    func_text += indentation(ind) + "def %s(%s):\n" % (name, params)

    return func_text


def gen_method_prot(name, ind=1, params=None, mod=None):
    method_text = ""
    param_text = "self"

    if mod == 'c':
        method_text += indentation(ind) + '@classmethod\n'
        param_text = "cls"

    if params:
        param_text += ", %s:\n" % (params)

    method_text += indentation(ind) + "def %s(%s):\n" % (name, param_text)
    return method_text


def gen_doc(text='TODO: Docstring', ind=0, single=True):
    doc_text = ""
    doc_text += indentation(ind) + '"""%s"""\n' % text

    if not single:
        doc_text += '\n'

    return doc_text


def gen_stamp():
    return ("#!/usr/bin/env python3\n" +
            "# -*- coding: utf-8 -*-\n" +
            "# Author: %s\n" % (AUTHOR) +
            "# Date: %s\n\n" % (time.strftime("%d/%m/%Y")))


def gen_class(name, inherit=None):
    if inherit:
        return "class %s(%s):\n\n" % (name, inherit)
    else:
        return "class %s(object):\n\n" % (name)


def gen_import(name):
    return 'import %s\n' % name


def gen_import_from(name, what='*'):
    return 'from %s import %s\n\n' % (name, what)


def gen_tests(project):
    return (gen_stamp() +
            gen_doc('Unit tests for %s application.' % project) +
            gen_import("unittest") +
            gen_import_from(project) +
            gen_class("MainTest", "unittest.TestCase") +
            gen_doc(ind=1, single=False) +
            gen_method_prot("setUp", mod='c') +
            gen_doc("Test Set Up", ind=2) +
            gen_plc_holder(ind=2) +
            gen_method_prot("tearDown", mod='c') +
            gen_doc('Test Clean Up', ind=2) +
            gen_plc_holder(ind=2) +
            gen_method_prot('test_%s' % project) +
            gen_doc(ind=2) +
            gen_plc_holder(ind=2))


def gen_plc_holder(ind):
    return indentation(ind) + 'pass\n\n'


def gen_main():
    return (gen_func_prot("main") +
            gen_doc('TODO: main function description.', ind=1) +
            gen_plc_holder(ind=1) +
            'if __name__ == "__main__":\n' +
            sp(4) + 'main()')


def gen_project(project_name):
    return (gen_stamp() +
            gen_doc("TODO: Script docstring.", single=False) +
            gen_main())


def sp(num):
    return num*" "


def indentation(num):
    return num*sp(4)


def main():
    if len(sys.argv) > 1:
        project_name = sys.argv[1]

        with open("%s.py" % project_name, 'w') as script_file:
            script_file.write(gen_project(project_name))
        with open("%s_test.py" % project_name, 'w') as test_file:
            test_file.write(gen_tests(project_name)[:-1])
    else:
        sys.exit()


if __name__ == "__main__":
    main()
