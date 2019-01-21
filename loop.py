# Rough comparison of speed to count numbers, Python vs Bash


# Python
i = 0
while(True):
    i += 1
    print(i)


# Bash - two different ways
# i=0; for (( ; ; )); do  ((i=i+1));  echo $i; done
# i=0; for (( ; ; )); do  let i=i+1;  echo $i; done
