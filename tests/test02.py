from schedulizer import PriorityNonPreemptive

def test_priority_non_preemptive_normal_execution():
    print("Test 02: Priority Non-Preemptive - Normal Execution")
    predefined_processes = [(1, 5, 10, 3), (2, 8, 5, 1), (3, 12, 8, 2)]
    priority = PriorityNonPreemptive()
    priority.schedulingProcess(predefined_processes)

def test_priority_non_preemptive_empty_input():
    print("Test 02: Priority Non-Preemptive - Empty Input")
    priority = PriorityNonPreemptive()
    priority.processData(0)

def test_priority_non_preemptive_single_process():
    print("Test 02: Priority Non-Preemptive - Single Process")
    priority = PriorityNonPreemptive()
    priority.processData(1)

def test_priority_non_preemptive_negative_values():
    print("Test 02: Priority Non-Preemptive - Negative Values")
    predefined_processes_with_negative_values = [(1, -2, 5, 3), (2, 3, -7, 1), (3, -1, -4, 2)]
    priority = PriorityNonPreemptive()
    priority.schedulingProcess(predefined_processes_with_negative_values)

def test_priority_non_preemptive_large_number_of_processes():
    print("Test 02: Priority Non-Preemptive - Large Number of Processes")
    large_number_of_processes = [(i, i * 2, i * 3, i % 5) for i in range(1, 1001)]
    priority = PriorityNonPreemptive()
    priority.schedulingProcess(large_number_of_processes)

if __name__ == "__main__":
    test_priority_non_preemptive_normal_execution()
    test_priority_non_preemptive_empty_input()
    test_priority_non_preemptive_single_process()
    test_priority_non_preemptive_negative_values()
    test_priority_non_preemptive_large_number_of_processes()
