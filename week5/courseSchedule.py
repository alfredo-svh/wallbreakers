class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        queue = []
        
        #fill graph
        for course in prerequisites:
            if course[0] not in graph:
                graph[course[0]] = [course[1]]
            else:
                graph[course[0]].append(course[1])
        
        
        #bfs
        for course in graph.items():
            #add prerequisites to queue
            for p in course[1]:
                queue.append(p)

            visited = set()

            # for each prereq, we check its prereqs.
            # if the course is a prereq for one of its prereqs
            # (aka, we found a cycle in the graph),
            # we return false
            while len(queue) > 0:
                pre = queue.pop()
                visited.add(pre)

                if pre == course[0]:
                    return False

                if pre in graph:
                    for c in graph[pre]:
                        if c not in visited:
                            queue.append(c)
        
        
        return True