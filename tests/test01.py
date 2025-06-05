from schedulizer import FCFS

def test_normal_execution():
    print("Test 01: Normal Execution")
    predefined_processes = [(1, 5, 10), (2, 8, 5), (3, 12, 8)]
    fcfs = FCFS()
    fcfs.schedulingProcess(predefined_processes)

def test_empty_input():
    print("Test 02: Empty Input")
    fcfs = FCFS()
    fcfs.processData(0)

def test_single_process():
    print("Test 03: Single Process")
    fcfs = FCFS()
    fcfs.processData(1)

def test_negative_values():
    print("Test 04: Negative Values")
    predefined_processes_with_negative_values = [(1, -2, 5), (2, 3, -7), (3, -1, -4)]
    fcfs = FCFS()
    fcfs.schedulingProcess(predefined_processes_with_negative_values)

def test_large_number_of_processes():
    print("Test 05: Large Number of Processes")
    large_number_of_processes = [(i, i * 2, i * 3) for i in range(1, 1001)]
    fcfs = FCFS()
    fcfs.schedulingProcess(large_number_of_processes)

if __name__ == "__main__":
    test_normal_execution()
    test_empty_input()
    test_single_process()
    test_negative_values()
    test_large_number_of_processes()

