def knapsack_job_scheduling(jobs, machine_capacities):
    num_jobs = len(jobs)
    num_machines = len(machine_capacities)

    # Sort jobs by deadline (earliest first)
    jobs.sort(key=lambda x: x['deadline'])

    # Initialize DP table
    dp = [[0] * (num_machines + 1) for _ in range(num_jobs + 1)]

    # Fill DP table
    for j in range(1, num_jobs + 1):
        current_job = jobs[j - 1]
        profit = current_job['profit']
        processing_time = current_job['processing_time']
        deadline = current_job['deadline']

        for m in range(1, num_machines + 1):
            if processing_time <= machine_capacities[m - 1]:
                dp[j][m] = max(dp[j - 1][m], dp[j - 1][m - 1] + profit)
            else:
                dp[j][m] = dp[j - 1][m]

    # Backtrack to find the selected jobs
    selected_jobs = []
    max_profit = dp[num_jobs][num_machines]
    j = num_jobs
    m = num_machines
    while j > 0 and m > 0:
        if dp[j][m] != dp[j - 1][m]:
            selected_jobs.append(jobs[j - 1])
            m -= 1
        j -= 1

    selected_jobs.reverse()  # Reverse to maintain order of selection

    return selected_jobs, max_profit

# Example usage:
if __name__ == "__main__":
    jobs = [
        {'id': 1, 'processing_time': 2, 'deadline': 3, 'profit': 100},
        {'id': 2, 'processing_time': 1, 'deadline': 1, 'profit': 50},
        {'id': 3, 'processing_time': 3, 'deadline': 4, 'profit': 50},
        {'id': 4, 'processing_time': 2, 'deadline': 2, 'profit': 200}
    ]
   
    machine_capacities = [3, 3, 3]
    selected_jobs, max_profit = knapsack_job_scheduling(jobs, machine_capacities)

    # Print the selected jobs and maximum profit
    print("Selected Jobs:")
    for job in selected_jobs:
        print(f"Job {job['id']} with processing time {job['processing_time']} and deadline {job['deadline']}")
    
    print(f"Maximum Profit: {max_profit}")