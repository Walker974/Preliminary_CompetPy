s = str(input(""));
t = str(input(""));
 
s_set = set(s);
t_set = set(t);
 
if (s_set.issubset(t_set) and t_set.issubset(s_set)):
    print("Yes");
else:
    print("No");