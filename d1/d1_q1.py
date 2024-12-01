'''
I need to pair smallest number in left with smallest number in right, thne next smallest left, next smallest right.
Take the distances of the two numbers and add them up.

Brute force:
Sort each list.
Calculate the distance of each pair and add it to total distance.
nlogn



'''
inputs_a = []
inputs_b = []
with open("d1_q1_input.txt", "r") as txt_input:
    for line in txt_input:
        split_line = line.strip().split(" ")
        filtered_line = [int(n) for n in split_line if n]
        inputs_a.append(filtered_line[0])
        inputs_b.append(filtered_line[1])

#Case, sizes of inputs might not be the same

inputs_a.sort()
inputs_b.sort()
total_distance = 0
for i in range(len(inputs_a)):
    total_distance += abs(inputs_a[i]-inputs_b[i])

print(total_distance)
