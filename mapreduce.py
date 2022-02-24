# Cristobal Chinolla
# Lab 2 Map Reduce
import re
import pymp
import time

listofFiles = ('shakespeare1.txt', 'shakespeare2.txt', 'shakespeare3.txt', 'shakespeare4.txt', 'shakespeare5.txt', 'shakespeare6.txt', 'shakespeare7.txt' ,'shakespeare8.txt')
listofWords = ('hate', 'love', 'death', 'night', 'sleep', 'time', 'henry', 'hamlet', 'you', 'my', 'blood', 'poison', 'macbeth', 'king', 'heart', 'honest')


# function returns the count (int) of occurences of a word in a file
def countWords(word, filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            count += len(re.findall(word, line))
    return count 



def mapreduce(thread):
    start_time = time.time()
    maindict = pymp.shared.dict()
    
    # the main dictionary that the function will return, sets all values to zero for all words
    for word in listofWords:
            maindict[word] = 0

    with pymp.Parallel(thread) as p:
        lock = p.lock
        # sets the local dictionary used by threads, all values to 0
        threaddict = dict()
        for word in listofWords:
            threaddict[word] = 0
        # updates the local dictionary with word count occurences for each word and each file
        for file in p.range(len(listofFiles)):
            for word in listofWords:
                threaddict[word] += countWords(word, listofFiles[file])
        # updating the main dictionary, locking before edits and releasing after finished
        for word in listofWords:
            lock.acquire()
            maindict[word] += threaddict[word]
            lock.release()

    end_time = time.time()
    print("Thread ", thread," Duration: ",end_time - start_time, "seconds")
    return(maindict)  



for i in range(1, 9):
    print(mapreduce(i))
    print('thread_num:', i)

