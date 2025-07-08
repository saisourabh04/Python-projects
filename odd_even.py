def read_file(file_name):
    with open(file_name) as file:
        data=file.read()
    return data

def write_file(file_name,data):
    with open(file_name,mode='a') as file:
        file.write(data)

def filter_nums(nums_str):
    nums=nums_str.split(',')
    even_list,odd_list=[],[]
    for num in nums:
        x=int(num)
        if x % 2 ==0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return even_list,odd_list
def main():
    nums_str=read_file(file_name='nums.txt')
    even,odd= filter_nums(nums_str)
    for x in even:
        write_file('even.txt',x+' ')
    for x in odd:
        write_file('odd.txt',x+' ')

main()