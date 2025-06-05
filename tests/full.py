from FCFS import FCFS
from Priority_non_preemptive import PriorityNonPreemptive
from Priority_preemptive import PriorityPreemptive
from Round_robin import RoundRobin
from SJF_non_preemptive import SJFNonPreemptive
from SJF_preemptive import SJFPreemptive



def test_scheduling_algorithms():
    # Test FCFS
    print("="*40 + " FCFS Scheduling " + "="*40)
    fcfs = FCFS()
    fcfs.processData(3)  # Replace '3' with the desired number of processes

    # Test Priority (Non-Preemptive)
    print("="*40 + " Priority (Non-Preemptive) Scheduling " + "="*40)
    priority_non_preemptive = PriorityNonPreemptive()
    priority_non_preemptive.processData(3)  # Replace '3' with the desired number of processes

    # Test Priority (Preemptive)
    print("="*40 + " Priority (Preemptive) Scheduling " + "="*40)
    priority_preemptive = PriorityPreemptive()
    priority_preemptive.processData(3)  # Replace '3' with the desired number of processes

    # Test Round Robin
    print("="*40 + " Round Robin Scheduling " + "="*40)
    round_robin = RoundRobin()
    round_robin.processData(3)  # Replace '3' with the desired number of processes

    # Test SJF (Non-Preemptive)
    print("="*40 + " SJF (Non-Preemptive) Scheduling " + "="*40)
    sjf_non_preemptive = SJFNonPreemptive()
    sjf_non_preemptive.processData(3)  # Replace '3' with the desired number of processes

    # Test SJF (Preemptive)
    print("="*40 + " SJF (Preemptive) Scheduling " + "="*40)
    sjf_preemptive = SJFPreemptive()
    sjf_preemptive.processData(3)  # Replace '3' with the desired number of processes

if __name__ == "__main__":
    test_scheduling_algorithms()
