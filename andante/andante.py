n = int(input());
a = list(map(int, input().split()));
 
count = 0;
 
for i in range(n):
    for j in range(i+1, n):
        diff = abs(a[i] - a[j]);
        count += a.count(diff);
 
print(count);