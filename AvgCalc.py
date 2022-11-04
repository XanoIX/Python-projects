i = int(input("How many scores to be used ? : "))
sum = 0
j = i


while j != 0 :
    scores = float(input(f"Score {i} : "))
    sum += scores 
    j = j-1

average = sum / float(i)   
print(average) 
