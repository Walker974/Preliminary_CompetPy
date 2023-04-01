n = int(input(""));
a = list(map(int, input("").split()));
 
counter = 0;
 
dictionary = {};
for u in a:
    if u in dictionary:
        dictionary[u] += 1;
    else:
        dictionary[u] = 1;
 
 
for i in range(n):
    for j in range(i+1, n):
        diff = abs(a[i] - a[j]);
        if diff in dictionary and i < j:
            counter += dictionary[diff];
 
print(counter);