s = str(input(""));
t = str(input(""));
 
 
s_chars = set(s);
t_chars = set(t);
 
 
if s_chars.issubset(t_chars) and t_chars.issubset(s_chars):
    print("Yes");
else:
    print("No");