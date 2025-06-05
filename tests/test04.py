from schedulizer import RoundRobin

def test_round_robin_normal_execution():
    print("Test 04: Round Robin - Normal Execution")
    predefined_processes = [(1, 5, 10), (2, 8, 5), (3, 12, 8)]
    rr = RoundRobin()
    rr.schedulingProcess(predefined_processes)

def test_round_robin_empty_input():
    print("Test 04: Round Robin - Empty Input")
    rr = RoundRobin()
    rr.processData(0)

def test_round_robin_single_process():
    print("Test 04: Round Robin - Single Process")
    rr = RoundRobin()
    rr.processData(1)

def test_round_robin_negative_values():
    print("Test 04: Round Robin - Negative Values")
    predefined_processes_with_negative_values = [(1, -2, 5), (2, 3, -7), (3, -1, -4)]
    rr = RoundRobin()
    rr.schedulingProcess(predefined_processes_with_negative_values)

def test_round_robin_large_number_of_processes():
    print("Test 04: Round Robin - Large Number of Processes")
    large_number_of_processes = [(i, i * 2, i * 3) for i in range(1, 1001)]
    rr = RoundRobin()
    rr.schedulingProcess(large_number_of_processes)

if __name__ == "__main__":
    test_round_robin_normal_execution()
    test_round_robin_empty_input()
    test_round_robin_single_process()
    test_round_robin_negative_values()
    test_round_robin_large_number_of_processes()
