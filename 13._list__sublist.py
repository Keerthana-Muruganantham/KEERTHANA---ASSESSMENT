def sub_List(list, k, ans):
    if len(list) == k:
        if list not in ans:
            ans.append(list)
        return ans
    if len(list) < k or k == 0:
        return [[]]
    for i in range(4,0,-1):
        a = list.copy()
        a.remove(i)
        sub_List(a, k, ans)
    print (ans)
sub_List([1,2,3,4], 3,[])
