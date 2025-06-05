from schedulizer import SJFPreemptive

def test_sjf_preemptive_normal_execution():
    print("Test 06: SJF Preemptive - Normal Execution")
    predefined_processes = [(1, 5, 10), (2, 8, 5), (3, 12, 8)]
    sjf = SJFPreemptive()
    sjf.schedulingProcess(predefined_processes)

def test_sjf_preemptive_empty_input():
    print("Test 06: SJF Preemptive - Empty Input")
    sjf = SJFPreemptive()
    sjf.processData(0)

def test_sjf_preemptive_single_process():
    print("Test 06: SJF Preemptive - Single Process")
    sjf = SJFPreemptive()
    sjf.processData(1)

def test_sjf_preemptive_negative_values():
    print("Test 06: SJF Preemptive - Negative Values")
    predefined_processes_with_negative_values = [(1, -2, 5), (2, 3, -7), (3, -1, -4)]
    sjf = SJFPreemptive()
    sjf.schedulingProcess(predefined_processes_with_negative_values)

def test_sjf_preemptive_large_number_of_processes():
    print("Test 06: SJF Preemptive - Large Number of Processes")
    large_number_of_processes = [(i, i * 2, i * 3) for i in range(1, 1001)]
    sjf = SJFPreemptive()
    sjf.schedulingProcess(large_number_of_processes)

if __name__ == "__main__":
    test_sjf_preemptive_normal_execution()
    test_sjf_preemptive_empty_input()
    test_sjf_preemptive_single_process()
    test_sjf_preemptive_negative_values()
    test_sjf_preemptive_large_number_of_processes()
