import sys
import time
AUTHOR = "Ondrej Zapletal"


def gen_stamp():
    return ("# -*- coding: utf-8 -*-\n" +
            "# Author: %s\n" % (AUTHOR) +
            "# Date: %s\n" % (time.strftime("%d/%m/%Y")) +
            "# Description:\n\n")


def gen_main():
    return (gen_fun("main") + "\n" + sp(4) + gen_doc('TODO: main function description.') + "\n" +
        'if __name__ == "__main__":\n' + sp(4) + 'main()')


def gen_fun(name, params=""):
    return "def %s(%s):\n" % (name, params)

def gen_met(name, params=None):
    if params:
        return "def %s(self, %s):\n" % (name, params)
    else:
        return "def %s(self):\n" % (name)

def gen_doc(text='TODO: Docstring'):
    return '""" %s """\n' % text

def gen_class(name, inherit=None):
    if inherit:
        return "class %s(%s):\n" % (name, inherit)
    else:
        return "class %s(object):\n" % (name)

def gen_impr(name):
    return 'import %s\n' % name

def gen_from(name, what='*'):
    return 'from %s import %s\n\n' % (name, what)

def gen_tests(project):
    return (
        gen_doc('Unit tests for %s application.' % project) +

        gen_impr("unittest") + gen_from(project) +
        gen_class("MainTest", "unittest.TestCae") + sp(4) + gen_doc() + sp(4) +

        '@classmethod\n' + sp(4) + gen_fun("setUp","cls") + sp(8) + gen_doc("Test Set Up") +
        sp(8) + 'pass\n\n' + sp(4) + '@classmethod\n' + sp(4) + gen_fun("tearDown", "cls") +
        sp(8) + gen_doc('Test Clean Up') + sp(8) + 'pass\n\n' + sp(4) + gen_met('test_%s' % project) +
        sp(8) + gen_doc() + sp(8) + 'pass\n')


def gen_project(project_name):
    return (gen_stamp() + '""" %s application. """\n\n\n' % (project_name) +
            gen_main())


def sp(num):
    return num*" "


def main():
    if len(sys.argv) > 1:
        project_name = sys.argv[1]

        with open("%s.py" % project_name, 'w') as script_file:
            script_file.write(gen_project(project_name))
        with open("%s_test.py" % project_name, 'w') as test_file:
            test_file.write(gen_tests(project_name))
    else:
        sys.exit()

if __name__ == "__main__":
    main()
