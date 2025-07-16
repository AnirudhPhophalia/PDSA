# A manufacturing plant has N independent working lines. Each job requires different amount of time to be completed and due time. Optimize the scheduling of jobs for every line so that every job is will be completed within due time or minimum lateness possible.

# Write a function minimizeLateness(N, jobs) to return the sequence of job ids to be scheduled in list of list. jobs is the tuple of (job_id, time_required, due_time), where job_id, time_required and due_time are the unique number assigned to job, relative time required to complete the job and absolute time before which the job should have completed respectively.

def minimizeLateness(N, jobs):
    sortedL = sorted(jobs, key=lambda x: (x[2], x[1], x[0]))
    optimum = [[] for i in range(N)]
    usedtime = {i: 0 for i in range(N)}
    i = 0
    while i < len(sortedL):
        freeline = min(usedtime, key=lambda x: usedtime[x])
        optimum[freeline].append(sortedL[i][0])
        usedtime[freeline] += sortedL[i][1]
        i += 1
    return optimum

# suffix (invisible)
def lateness(optimum, jobs):
    jobdict = {job[0]: [job[0], job[1], job[2]] for job in jobs}
    time = 0
    late = 0
    for optID in optimum:
        time += jobs[optID][1]
        overtime = time - jobdict[optID][2]
        late += overtime if overtime >= 0 else 0
    return late

N = int(input())
m = int(input())
jobs = []
while True:
    line = input().strip()
    if line == '': 
        break
    t = line.split(' ')
    jobs.append((int(t[0]), int(t[1]), int(t[2])))

optimum = minimizeLateness(N, jobs)
extratime = 0
for i in range(N):
    extratime += lateness(optimum[i], jobs)
if extratime <= m:
    print('Passed')
else:
    print('Improve your algorithm')
