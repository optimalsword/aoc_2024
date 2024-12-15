import sys

sys.setrecursionlimit(3000)



def lst_distance(lst1, lst2):
    
    def helper(lst1, lst2, acc):
        if len(lst1) == 1 and len(lst2) == 1:
            return acc + abs(lst1[0] - lst2[0])
        
        return helper(lst1[1:], lst2[1:], acc + abs(lst1[0] - lst2[0]))
    
    return helper(lst1, lst2, 0)
        



if __name__ == '__main__':
    _lst1 = []
    _lst2 = []
    
    with open('day1.txt', 'r') as file:
        _lists = file.read()
        _lists = _lists.split('\n')
        for index in range(len(_lists)):
            cur_nums = _lists[index]
            _lst1.append(int(cur_nums.split('   ')[0]))
            _lst2.append(int(cur_nums.split('   ')[1]))
            
            
    _lst1.sort()
    _lst2.sort()
    print(lst_distance(_lst1, _lst2))