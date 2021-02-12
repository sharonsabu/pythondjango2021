#pgm to find the pair which gives the sum
lst=[1,2,3,4,5,6]
no=int(input("enter a number"))
st=set(lst)
out=set()
for num in st:
    op=no-num
    if (op in st)&(op!=num):
        if op>num:
            out.add((num,op))
        else:
            out.add((op,num))

print(out)