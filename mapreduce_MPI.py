# Cristobal Chinolla
# Lab 2 Map Reduce
import re
from numpy import size
from mpi4py import MPI
import time

listofFiles = ('shakespeare1.txt', 'shakespeare2.txt', 'shakespeare3.txt', 'shakespeare4.txt',
               'shakespeare5.txt', 'shakespeare6.txt', 'shakespeare7.txt', 'shakespeare8.txt')
listofWords = ('hate', 'love', 'death', 'night', 'sleep', 'time', 'henry',
               'hamlet', 'you', 'my', 'blood', 'poison', 'macbeth', 'king', 'heart', 'honest')


# function returns the count (int) of occurences of a word in a file
def countWords(word, filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            count += len(re.findall(word, line))
    return count


def makeLocalDict(file):
    localdict = {}
    for word in listofWords:
        localdict[word] = 0

    text_file = open(file, "r")
    filelines = text_file.readlines()
    text_file.close()

    for line in filelines:
        for word in listofWords:
            localdict[word] += countWords(word, listofFiles[file])

    return localdict


def updateDict(localDict, addedDict):
    for word in addedDict.keys():
        localDict[word] += addedDict[word]
    return localDict


def mapReduce(files):
    finalDict = {}
    for word in listofWords:
        finalDict[word] = 0

    for file in files:
        currentDict = makeLocalDict(file)
        finalDict = updateDict(finalDict, currentDict)

    return finalDict


def parallel(files):

    # get the world communicator
    comm = MPI.COMM_WORLD

    # get our rank (process #)
    rank = comm.Get_rank()

    # get the size of the communicator in # processes
    size = comm.Get_size()
    
    if rank == 0:
        docsPerThread = len(listofFiles) / size
        localList = listofFiles[:int(docsPerThread)]

        for process in range(1, size):
            # start and end of slice we're sending
            startOfSlice = int(docsPerThread * process )
            endOfSlice = int(docsPerThread * (process + 1) )

            sliceToSend = listofFiles[startOfSlice:endOfSlice]
            comm.send(sliceToSend, dest=process, tag=0)

        localDict = mapReduce(localList)

        for process in range(1,size):
                recvd_count,recvd_time = comm.recv(source=process, tag=1)
                print(f'Thread 0 recieved from {process}')
                localDict = updateDict(localDict, recvd_count)
    else:
        localList = comm.recv(source=0, tag=0)
        print(f"Thread {rank} received {localList}.")
        
        # counts file
        localDict = mapReduce(localList)
        
        # send data back to thread 0
        comm.send(localDict, dest=0, tag=1)
    
def main():
    parallel(listofFiles)

main()
