# A group of workers have to complete a list of tasks, those tasks have dependencies within the task list. But the workers prefer some interesting task and hates to do some boring task. They always do the most interesting one among the available tasks to be done.

# Write a function coolWorkers(AList, preference) to return the order in which the tasks will be done. AList is the adjacency list with the dependencies and preference is the tasks sorted in preferred order, in which task in index 0 is the most preferred and index -1 (last element) be the least preferred.

def coolWorkers(AList, preference):
    n = len(AList.keys())
    indegree = {}
    toposortlist = []
    for i in AList.keys():
        indegree[i] = 0
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] = indegree[v] + 1

    for i in range(n):
        availableTasks = [k for k in AList if indegree[k] == 0]
        t = [(preference.index(i), i) for i in availableTasks]
        t.sort()
        j = t[0][1]
        toposortlist.append(j)
        indegree[j] = indegree[j] - 1
        for k in AList[j]:
            indegree[k] -= 1
    return toposortlist

AList = eval(input())
preference = eval(input())
print(coolWorkers(AList, preference))