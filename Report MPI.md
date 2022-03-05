# Cristobal Chinolla

# How to Run:

    mpirun -n <# process> python3 mapreduce_MPI.py

# Problems Encountered:

    The main problem I encountered was testing. Because I am working on two different machines (one to write the code and the
     other to test in the VM (cuz i have m1 mac))
     I could not test as frequently as I would have liked. 
     I encountered a lot of errors with testing, I had errors with the print statements, then with importing the MPI library. 



# Time Spent:

    because this lab built off the last lab, it did not take as long as I thought it would. 
    The examples provided were really helpful. Total time spend ~ 4 hours


# Performance Measurements: 

    16 threads - 63.72s
    ![Screen Shot 2022-03-04 at 9 52 31 PM](https://user-images.githubusercontent.com/98130863/156868495-5b517b98-fecc-4a7c-b90a-4326801e8243.png)

    8 threads - 31.82s
    ![Screen Shot 2022-03-04 at 9 51 29 PM](https://user-images.githubusercontent.com/98130863/156868471-9a5f3da9-f6b1-48b1-b04e-32e6530e81e1.png)

    4 threads - 30.25s
    
    3 threads - 28.64s
    ![Screen Shot 2022-03-04 at 9 53 27 PM](https://user-images.githubusercontent.com/98130863/156868516-de663bcb-314b-47c9-b7e9-37f0a7326ec0.png)

    2 threads - 24.49s
    1 thread -  37.08s

# Analysis:

    My implentation using MPI over OpenMP took significantly longer to finish the same task. I am not sure if it is because of 
    MPI or if my implementation was just inefficient (probably the second one)

    As far as the analysis for MPI, I noticed that if the number of threads was greater than the number of files (8), this actually
     increased the total time to complete. I assume this is because the excess amount of threads have nothing to do and increase the 
     overhead time.

    I also noticed a pattern. When the threads:amount of files reached a specific ratio, (for example 2 threads), where there were
     less threads and each thread had an even amount of files. The run time was lower.
     
    ![Optional Text](Screen Shot 2022-03-04 at 9.43.50 PM.png)
    


# CPU Info

    Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz
          4      36     216

