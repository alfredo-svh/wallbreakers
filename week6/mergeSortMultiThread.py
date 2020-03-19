import threading
import random

def merge(lst, l,r):
	i=0
	while len(l)>0 or len(r)>0:
		if len(r)==0:
			lst[i] = l[0]
			del l[0]
			i+=1
		elif len(l)==0:
			lst[i] = r[0]
			del r[0]
			i+=1
		elif l[0] <= r[0]:
			lst[i] = l[0]
			del l[0]
			i+=1
		else:
			lst[i] = r[0]
			del r[0]
			i+=1


def mergeSort(lst):
	if len(lst)>1:
		m = len(lst)//2
		l = lst[:m]
		r = lst[m:]
		mergeSort(l)
		mergeSort(r)
		merge(lst, l,r)


totalThreads = 4
lst = []
for i in range(100000):
	lst.append(random.randint(0, 100000))
n = len(lst)//totalThreads
sblsts = []
threads = []

#split lst into \totalThreads\ sublists
for i in range(totalThreads):
	if i==totalThreads-1:
		sblsts.append(lst[i*n:])
	else:
		sblsts.append(lst[i*n : i*n+n])

#call mergeSort for every sublist
for i in range(totalThreads):
	threads.append(threading.Thread(target=mergeSort, args=(sblsts[i],)))
	threads[i].start()

#join threads
for i in range(totalThreads):
	threads[i].join()

#call merge \totalThreads\-1 times to get the final sorted lst
lst = []
tmp = [0 for _ in range(len(sblsts[0]))]
for i in range(totalThreads-1):
	tmp += sblsts[i+1]
	merge(tmp, sblsts[i], sblsts[i+1])
	sblsts[i+1] = tmp.copy()

lst = sblsts[-1]

print(lst)