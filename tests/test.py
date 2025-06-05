import unittest
from tests.test01 import (
    test_normal_execution,
    test_empty_input,
    test_single_process,
    test_negative_values,
    test_large_number_of_processes
    )
from tests.test02 import (
    test_priority_non_preemptive_normal_execution,
    test_priority_non_preemptive_empty_input,
    test_priority_non_preemptive_single_process,
    test_priority_non_preemptive_negative_values,
    test_priority_non_preemptive_large_number_of_processes,
)
from tests.test03 import (
    test_priority_preemptive_normal_execution,
    test_priority_preemptive_empty_input,
    test_priority_preemptive_single_process,
    test_priority_preemptive_negative_values,
    test_priority_preemptive_large_number_of_processes,
)
from tests.test04 import (
    test_round_robin_normal_execution,
    test_round_robin_empty_input,
    test_round_robin_single_process,
    test_round_robin_negative_values,
    test_round_robin_large_number_of_processes,
)
from tests.test05 import (
    test_sjf_non_preemptive_normal_execution,
    test_sjf_non_preemptive_empty_input,
    test_sjf_non_preemptive_single_process,
    test_sjf_non_preemptive_negative_values,
    test_sjf_non_preemptive_large_number_of_processes,
)
from tests.test06 import (
    test_sjf_preemptive_normal_execution,
    test_sjf_preemptive_empty_input,
    test_sjf_preemptive_single_process,
    test_sjf_preemptive_negative_values,
    test_sjf_preemptive_large_number_of_processes,
)

def suite():
    test_suite = unittest.TestSuite()

    # Test 01
    test_suite.addTest(unittest.FunctionTestCase(test_normal_execution))
    test_suite.addTest(unittest.FunctionTestCase(test_empty_input))
    test_suite.addTest(unittest.FunctionTestCase(test_single_process))
    test_suite.addTest(unittest.FunctionTestCase(test_negative_values))
    test_suite.addTest(unittest.FunctionTestCase(test_large_number_of_processes))

    # Test 02
    test_suite.addTest(unittest.FunctionTestCase(test_priority_non_preemptive_normal_execution))
    test_suite.addTest(unittest.FunctionTestCase(test_priority_non_preemptive_empty_input))
    test_suite.addTest(unittest.FunctionTestCase(test_priority_non_preemptive_single_process))
    test_suite.addTest(unittest.FunctionTestCase(test_priority_non_preemptive_negative_values))
    test_suite.addTest(unittest.FunctionTestCase(test_priority_non_preemptive_large_number_of_processes))

    # Test 03
    test_suite.addTest(unittest.FunctionTestCase(test_priority_preemptive_normal_execution))
    test_suite.addTest(unittest.FunctionTestCase(test_priority_preemptive_empty_input))
    test_suite.addTest(unittest.FunctionTestCase(test_priority_preemptive_single_process))
    test_suite.addTest(unittest.FunctionTestCase(test_priority_preemptive_negative_values))
    test_suite.addTest(unittest.FunctionTestCase(test_priority_preemptive_large_number_of_processes))

    # Test 04
    test_suite.addTest(unittest.FunctionTestCase(test_round_robin_normal_execution))
    test_suite.addTest(unittest.FunctionTestCase(test_round_robin_empty_input))
    test_suite.addTest(unittest.FunctionTestCase(test_round_robin_single_process))
    test_suite.addTest(unittest.FunctionTestCase(test_round_robin_negative_values))
    test_suite.addTest(unittest.FunctionTestCase(test_round_robin_large_number_of_processes))

    # Test 05
    test_suite.addTest(unittest.FunctionTestCase(test_sjf_non_preemptive_normal_execution))
    test_suite.addTest(unittest.FunctionTestCase(test_sjf_non_preemptive_empty_input))
    test_suite.addTest(unittest.FunctionTestCase(test_sjf_non_preemptive_single_process))
    test_suite.addTest(unittest.FunctionTestCase(test_sjf_non_preemptive_negative_values))
    test_suite.addTest(unittest.FunctionTestCase(test_sjf_non_preemptive_large_number_of_processes))

    # Test 06
    test_suite.addTest(unittest.FunctionTestCase(test_sjf_preemptive_normal_execution))
    test_suite.addTest(unittest.FunctionTestCase(test_sjf_preemptive_empty_input))
    test_suite.addTest(unittest.FunctionTestCase(test_sjf_preemptive_single_process))
    test_suite.addTest(unittest.FunctionTestCase(test_sjf_preemptive_negative_values))
    test_suite.addTest(unittest.FunctionTestCase(test_sjf_preemptive_large_number_of_processes))

    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
