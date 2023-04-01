Given 3 integers a,b,n you can perform the following operation several (possibly zero) times:

Choose two integers x and y such that x+y=n and a≥x and b≥y then set a:=a−x+y and b:=b−y+x.

What is the maximum value of a you can get?

Input:
 - The first line of the input contains one integer T (1≤T≤10^5). Followed by T testcases.
 - Each testcase consists of one line containing 3 integers separated by spaces a,b,n (0≤a,b≤10^9 and 1≤n≤10^9)

Output:
 - For each testcase, output one line containing the maximum value a can get by performing the operation described in the statement