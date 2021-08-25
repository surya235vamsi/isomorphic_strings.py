def dd(s,t):
    l=[]
    p=[]
    q=[]
    a=[]
    if len(set(s))!=len(set(t)):
        return False
    for i in range(0,len(s)):
        l.append(s[i])
    for i in l:
        if l.count(i)==2:
            e=i
        else:
            e=l[-1]
    for i in range(0,len(l)):
        if i==0:
            p.append(l[-1])
        else:
            p.append(l[-i-1])
    for i in range(0,len(t)):
        q.append(t[i])
    for j in q:
        if q.count(j)==2:
            w=j
        else:
            w=q[-1]
    for i in range(0,len(q)):
        if i==0:
            a.append(q[-1])
        else:
            a.append(q[-i-1])
    u=int(q.index(w))+int(a.index(w))
    h=int(l.index(e)+int(p.index(e)))
    if u==h:
        return True
    else:
        return False
s="abb"
t="bee"
print(dd(s,t))
