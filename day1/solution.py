# input = './example.txt'
input = './input1.txt'

# with open(input, 'r') as inp_file:
#     rows = [[int(id) for id in line.strip().split("   ")] for line in inp_file]
#     first_list, second_list = sorted([row[0] for row in rows]), sorted([row[1] for row in rows])
#     diffs = [abs(first_list[i] - second_list[i]) for i in range(len(first_list))]
#     print(first_list)
#     print(second_list)
#     print(sum(diffs))

with open(input, 'r') as inp_file:
    rows = [[int(id) for id in line.strip().split("   ")] for line in inp_file]
    first_list, second_list = sorted([row[0] for row in rows]), sorted([row[1] for row in rows])
    scores = [second_list.count(id) * id for id in first_list]
    print(sum(scores))
