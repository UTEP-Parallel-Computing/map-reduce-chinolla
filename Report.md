# Cristobal Chinolla

# Problems Encountered:

    The main problem I encountered was creating a function that counted the words in a file for all files. During initial testing, I was using .count(word) and it was working just fine for me.
    I still have to test on a different computer so I had to push what I thought would work then test it. As soon as i would try to run my file in the VM, .count() would no longer work. I spent a lot of time trying to figure out why it wasnt working and even used .read() to read the files

    The other problem I had is that my main dictionary kept getting reset and the results were not accurate. I realized this was becuase I had each thread in pymp.Parallel reseting it. So I had to move it outside.

# Time Spent:

    I spent a lot less time on this lab than I did on last lab. Mainly because I felt like the objective was a lot easier to understand.

    Probably around 5 hours 

# Performance Measurements: 
    A single thread took around 2.60 seconds

    When completed with anything above 2 threads, the time to complete was around 1.01 - 1.08 seconds

# Analysis:

    I figured that the difference between time completions using different amounts of threads would not be that different since each thread has to wait when using the lock and acquire

# CPU Info

    Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz
          4      36     216

