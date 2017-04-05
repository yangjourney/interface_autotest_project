#!/usr/bin/python
# -*- coding: utf-8 -*-
import testlink

manual = 1  # 手动
automation = 2  # 自动

# 连接test link
url = "http://192.168.118.103/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
key = "9758909a6fd284d04bdeadea1f532353"  # 我这个key是错误的key
tlc = testlink.TestlinkAPIClient(url, key)


def get_information_test_project():
    print("Number of Projects      in TestLink: %s " % tlc.countProjects())
    print("Number of Platforms  (in TestPlans): %s " % tlc.countPlatforms())
    print("Number of Builds                   : %s " % tlc.countBuilds())
    print("Number of TestPlans                : %s " % tlc.countTestPlans())
    print("Number of TestSuites               : %s " % tlc.countTestSuites())
    print("Number of TestCases (in TestSuites): %s " % tlc.countTestCasesTS())
    print("Number of TestCases (in TestPlans) : %s " % tlc.countTestCasesTP())
    tlc.listProjects()

def get_test_suite():
    projects = tlc.getProjects()
    top_suites = tlc.getFirstLevelTestSuitesForTestProject(projects[0]["id"])
    for suite in top_suites:
        print (suite["id"], suite["name"])

def create_test_suite(project_id, test_suite_name, test_suite_describe, father_id):
    if father_id == "":
        tlc.createTestSuite(project_id, test_suite_name, test_suite_describe)
    else:
        tlc.createTestSuite(project_id, test_suite_name, test_suite_describe, parentid=father_id)

def create_test_case(father_id, data):
    tlc.initStep(data[0][2], data[0][3], automation)
    for i in range(1, len(data)):
        tlc.appendStep(data[i][2], data[i][3], automation)
    tlc.createTestCase(data[0][0], father_id, "1", "timen.xu", "", preconditions=data[0][1])

def get_test_case(test_case_id):
    test_case = tlc.getTestCase(None, testcaseexternalid=test_case_id)
    for i in test_case:
        print ("序列", "执行步骤", "预期结果")
        for m in i.get("steps"):
            print (m.get("step_number"), m.get("actions"), m.get("expected_results"))

def report_test_result(test_plan_id, test_case_id, test_result):
    tlc.reportTCResult(None, test_plan_id, None, test_result, "", guess=True,
                       testcaseexternalid=test_case_id, platformname="0")







