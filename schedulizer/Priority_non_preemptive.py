class PriorityNonPreemptive:

    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = int(input("Enter Process ID: "))
            arrival_time = int(input("Enter Arrival Time: "))
            burst_time = int(input("Enter Burst Time: "))
            priority = int(input("Enter Priority: "))
            print()
            temporary.extend([process_id, arrival_time, burst_time, priority, 0])
            process_data.append(temporary)
        Priority.schedulingProcess(self, process_data)


    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        process_data.sort(key=lambda x: x[1])
        '''
        Sort processes according to the Arrival Time
        '''
        for i in range(len(process_data)):
            ready_queue = []
            temp = []
            normal_queue = []
            for j in range(len(process_data)):
                if (process_data[j][1] <= s_time) and (process_data[j][4] == 0):
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2], process_data[j][3]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[j][4] == 0:
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2], process_data[j][3]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[3], reverse=True)
                '''
                Sort the processes according to the Priority, considering Higher the Value, Higher the Priority
                '''
                start_time.append(s_time)
                s_time = s_time + ready_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][4] = 1
                process_data[k].append(e_time)
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][4] = 1
                process_data[k].append(e_time)
        t_time = Priority.calculateTurnaroundTime(self, process_data)
        w_time = Priority.calculateWaitingTime(self, process_data)
        Priority.printData(self, process_data, t_time, w_time)


    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]   #turnaround_time = completion_time - arrival_time
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        return average_turnaround_time


    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][2]  #waiting_time = turnaround_time - burst_time
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        return average_waiting_time


    def printData(self, process_data, average_turnaround_time, average_waiting_time):
        process_data.sort(key=lambda x: x[4])   #sort based on completion time        
        seq=[]
        for i in process_data:
            seq.append(i[0])
        process_data.sort(key=lambda x: x[0])   #Sort processes according to the Process ID
        print("Process_ID   Arrival_Time   Burst_time    Priority   Completion_Time   Turnaround_Time   Waiting_Time")
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                if j!=4:
                    print(process_data[i][j], end="	    	")
            print()
        print('Average Turnaround Time:',average_turnaround_time)
        print('Average Waiting Time:',average_waiting_time)
        print('Gantt chart:',seq)
