from schedulizer import SJFNonPreemptive

def test_sjf_non_preemptive_normal_execution():
    print("Test 05: SJF Non-Preemptive - Normal Execution")
    predefined_processes = [(1, 5, 10), (2, 8, 5), (3, 12, 8)]
    sjf = SJFNonPreemptive()
    sjf.schedulingProcess(predefined_processes)

def test_sjf_non_preemptive_empty_input():
    print("Test 05: SJF Non-Preemptive - Empty Input")
    sjf = SJFNonPreemptive()
    sjf.processData(0)

def test_sjf_non_preemptive_single_process():
    print("Test 05: SJF Non-Preemptive - Single Process")
    sjf = SJFNonPreemptive()
    sjf.processData(1)

def test_sjf_non_preemptive_negative_values():
    print("Test 05: SJF Non-Preemptive - Negative Values")
    predefined_processes_with_negative_values = [(1, -2, 5), (2, 3, -7), (3, -1, -4)]
    sjf = SJFNonPreemptive()
    sjf.schedulingProcess(predefined_processes_with_negative_values)

def test_sjf_non_preemptive_large_number_of_processes():
    print("Test 05: SJF Non-Preemptive - Large Number of Processes")
    large_number_of_processes = [(i, i * 2, i * 3) for i in range(1, 1001)]
    sjf = SJFNonPreemptive()
    sjf.schedulingProcess(large_number_of_processes)

if __name__ == "__main__":
    test_sjf_non_preemptive_normal_execution()
    test_sjf_non_preemptive_empty_input()
    test_sjf_non_preemptive_single_process()
    test_sjf_non_preemptive_negative_values()
    test_sjf_non_preemptive_large_number_of_processes()
