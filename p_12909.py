import sys
s = sys.stdin.readline().strip()

def solution(s):
	cnt = 0
	for i in s:
		if i == '(':
			cnt+=1
		if i == ')':
			cnt-=1
		if cnt == -1:
			break

	if cnt == 0:
		return True
	else:
		return False

print(solution(s))