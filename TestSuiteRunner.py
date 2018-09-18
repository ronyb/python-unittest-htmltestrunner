import unittest
import datetime
import os
import time

from HTMLTestRunner import HTMLTestRunner
from TestsClass0 import TestsClass0
from TestsClass1 import TestsClass1
from TestsClass2 import TestsClass2


if __name__ == "__main__":

    testSuite  = unittest.TestSuite()
    testLoader = unittest.TestLoader()

    testSuite.addTests(testLoader.loadTestsFromTestCase(TestsClass0))
    testSuite.addTests(testLoader.loadTestsFromTestCase(TestsClass1))
    testSuite.addTests(testLoader.loadTestsFromTestCase(TestsClass2))

    # HTML Tests Runner
    reportsFolder = "./html-reports"
    if not os.path.exists(reportsFolder):
        os.makedirs(reportsFolder)
    
    reportTitle = "This is the report title"
    reportDescription = "This is the report description"
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%d%b%y_%H%M%S')
    fileStream = open(reportsFolder + "/report_" + timestamp + ".html", "w")
    
    htmlTestRunner = HTMLTestRunner(stream=fileStream, verbosity=3, title=reportTitle, description=reportDescription)
    htmlTestRunner.run(testSuite)

    '''
    # Text Tests Runner
    textTestRunner = unittest.TextTestRunner(verbosity=3)
    textTestRunner.run(testSuite)
    '''