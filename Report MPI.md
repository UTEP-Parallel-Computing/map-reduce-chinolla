# Cristobal Chinolla

# How to Run:

    mpirun -n <# process> python3 mapreduce_MPI.py

# Problems Encountered:

    The main problem I encountered was testing. Because I am working on two different machines (one to write the code and the other to test in the VM (cuz i have m1 mac)) I could not test as frequently as I would have liked. I encountered a lot of errors with testing, I had errors with the print statements, then with importing the MPI library. 



# Time Spent:

    because this lab built off the last lab, it did not take as long as I thought it would. The examples provided were really helpful. Total time spend ~ 4 hours


# Performance Measurements: 
    A single thread took around 2.60 seconds

    When completed with anything above 2 threads, the time to complete was around 1.01 - 1.08 seconds

# Analysis:

    I figured that the difference between time completions using different amounts of threads would not be that different since each thread has to wait when using the lock and acquire

# CPU Info

    Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz
          4      36     216

