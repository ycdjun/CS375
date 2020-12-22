import random

# Input: None
# Output: 100 random jobs


def generateJobs():
    jobs = []
    for i in range(100):
        if i == 0:
            arrivalTime, length = 0, random.uniform(0.5, 1)
        else:
            arrivalTime, length = random.random(), random.uniform(0.5, 1)
        jobs.append((arrivalTime, length))

    return jobs

#Input: jobs
# Output: Schedule jobs based on shortest job first


def shortestFirst(jobs):
    s = jobs.copy()
    # sort the jobs based on shortest job length
    s.sort(key=lambda x: x[1])
    schedule = []
    schedule.append(s[0])
    wt = list(range(100))
    st = list(range(100))
    wt[0] = schedule[0][0]
    st[0] = schedule[0][1]
    time = wt[0]

    for i in range(1, len(s)):
        current = s[i]
        time += schedule[0][1]
        wt[i] = time - current[0]
        st[i] = wt[i] + current[1]
        schedule.pop()
        schedule.append(current)

    print("Shortest first avg wait time: " + str(sum(wt)/100))
    print("Shortest first max wait time: " + str(max(wt)))
    print("Shortest first avg service time: " + str(sum(st)/100))
    print("Shortest first max service time: " + str(max(st)))


def longestFirst(jobs):
    s = jobs.copy()
    s.sort(key=lambda x: x[1], reverse=True)
    schedule = []
    schedule.append(s[0])
    wt = list(range(100))
    st = list(range(100))
    wt[0] = schedule[0][0]
    st[0] = schedule[0][1]
    time = wt[0]

    for i in range(1, len(s)):
        current = s[i]
        time += schedule[0][1]
        wt[i] = time - current[0]
        st[i] = wt[i] + current[1]
        schedule.pop()
        schedule.append(current)

    print("Longest first avg wait time: " + str(sum(wt)/100))
    print("Longest first max wait time: " + str(max(wt)))
    print("Longest first avg service time: " + str(sum(st)/100))
    print("Longest first max service time: " + str(max(st)))


def FirstCome(jobs):
    s = jobs.copy()
    s.sort(key=lambda x: x[0])
    # print(s)
    schedule = []
    schedule.append(s[0])
    wt = list(range(100))
    st = list(range(100))
    wt[0] = schedule[0][0]
    st[0] = schedule[0][1]
    time = schedule[0][0]

    for i in range(1, len(s)):
        current = s[i]
        time += schedule[0][1]
        wt[i] = time - current[0]
        st[i] = wt[i] + current[1]
        schedule.pop()
        schedule.append(current)

    print("First come first serve avg waiting time: " + str(sum(wt)/100))
    print("First come first serve max waiting time: " + str(max(wt)))
    print("First come first serve avg service time: " + str(sum(st)/100))
    print("First come first serve max service time: " + str(max(st)))


jobs = generateJobs()
shortestFirst(jobs)
longestFirst(jobs)
FirstCome(jobs)
