print("\n----Numeric Calculator----\n")
print("use key only '+','-','*' and '/'")
print("raise to the power '**' and first bracket '()'")
print("avoid letters, spaces or any other special characters rather than numbers\n")
print("Type 'quit' to exit calculator\n")

def do_power(li):
	for i in range (len(li)):
		if li[i]=="**":
			left=li[i-1]
			right=li[i+1]
			ans=left**right
			li[i-1]=ans
			del li[i]
			del li[i]
			return li

def do_multiplydivide(li):
	for i in range (len(li)):
		if li[i]=="*" or li[i]=="/":
			left=li[i-1]
			right=li[i+1]
			
			if li[i]=="*":
				ans=left*right
			elif li[i] =="/":
				ans=left/right
				
			li[i-1]=ans
			del li[i] 
			del li[i] 
			return li
			
					
def do_plusminus(li):
	for i in range (len(li)):
		if li[i]=="+" or li[i]=="-":
			left=li[i-1]
			right=li[i+1]
			
			if li[i]=="+":
				ans=left+right
			elif li[i] =="-":
				ans=left-right
				
			li[i-1]=ans
			del li[i] 
			del li[i] 
			return li


while True:
	expr=input("")
	if expr=="quit":
		print("Calculator closed")
		break
		

	empt=[]
	num=("")
	i=0
	while i< len(expr):
		if expr[i].isdigit() or expr[i]==".":
			num+=expr[i]
		else:
			if num !="":
				empt.append(float(num))
			if expr[i]=="*" and i+1< len(expr) and expr[i+1]=="*":
				empt.append("**")
				i+=1
			else:
				empt.append(expr[i])
			num=""
		i+=1
	if num !="":
		empt.append(float(num))
		
		
	while "(" in empt:	
		for i in range (len(empt)):
			if empt[i]=="(":
				start=i
		for j in range (start, len(empt)):
			if empt[j]==")":
				end=j
				break
		sublist=empt[start+1:end]
		
	
		while "**" in sublist:
			do_power(sublist)				
		while "*" in sublist or "/" in sublist:
			do_multiplydivide(sublist)
		while "+" in sublist or "-" in sublist:
			do_plusminus(sublist)
		
		empt[start:end+1]=[sublist[0]]
	
	while "**" in empt:
		do_power(empt)				
	while "*" in empt or "/" in empt:
		do_multiplydivide(empt)
	while "+" in empt or "-" in empt:
		do_plusminus(empt)
		
	print(empt[0])
	print("[quit] to exit\n")