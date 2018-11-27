
instructions = '''
David Rosenberg
U00063482
COMP 7712

Programming Assignment 3

NOTE: This dynamic programming solution runs in O( X Y n ) time, which
is the upper bound of time it takes to populate the value array.  It
works basically like a 2-d n-knapsack problem.


CLOTH CUTTING PROBLEM...

6.14. Cutting cloth. You are given a rectangular piece of cloth with 
dimensions X x Y , where X and Y are positive integers, and a list of 
n products that can be made using the cloth. For each product i exists [1, 
n] you know that a rectangle of cloth of dimensions ai x bi is needed 
and that the final selling price of the product is ci. Assume the ai, 
bi, and ci are all positive integers. You have a machine that can cut 
any rectangular piece of cloth into two pieces either horizontally or 
vertically. Design an algorithm that determines the best return on 
the X x Y piece of cloth, that is, a strategy for cutting the cloth 
so that the products made from the resulting pieces give the maximum 
sum of selling prices. You are free to make as many copies of a given 
product as you wish, or none if desired.

Assume the input is given as follows. The first line will be X and Y 
separated by a space symbol. Then, comes n on the next line, and the 
remaining n lines will be ai, bi, ci separated by spaces. The output 
must contain the best return you can get. 
'''

def cloth(X, Y, abc):
	
	def _cloth(n, x, y):
		# check the value array first as not to recalculate values
		if value[n][x][y] is not None: 
			return value[n][x][y]
		
		# cloth is gone or we're out of valuable sizes of cloth
		if n == 0 or x == 0 or y == 0: 
			result = 0

		# turn the piece of cloth around if it will get us a valuable shape to cut from
		elif (x < abc[n][0] and x >= abc[n][1] and y >= abc[n][0]) or (y < abc[n][1] and y >= abc[n][0] and x >= abc[n][1]):
			result = _cloth(n, y, x)

		# if current valuable shape doesn't fit, try the next shape
		elif x < abc[n][0] or y < abc[n][1]:
			result = _cloth(n-1, x, y)

		# otherwise see which of the remaining options is of max value, and choose it 
		else:
			tmp1 = _cloth(n-1, x, y)
			tmp2 = abc[n][2] + _cloth(len(abc), x-abc[n][0], y) + _cloth(len(abc), abc[n][0], y-abc[n][1])
			tmp3 = abc[n][2] + _cloth(len(abc), x, y-abc[n][1]) + _cloth(len(abc), x-abc[n][0], abc[n][1])
			result = max(tmp1, tmp2, tmp3)
		
		# store the result in value array
		value[n][x][y] = result
		return result

	# value array will store the values to make this a dynamic programming solution
	value = [[[None for x in range(X+1)] for y in range(Y+1)] for i in range(len(abc)+1)]
	return _cloth(len(abc), X, Y)


if __name__ == '__main__':
	print(instructions)
	import pdb;pdb.set_trace()
	user_input = input('\nEnter X and Y separated by a space symbol: ')
	X, Y = tuple(int(i) for i in user_input.split())
	n = int(input('\nEnter value for n: '))
	abc = {}
	for i in range(n):
		user_input = input('\nEnter a{i}, b{i}, c{i}, separated by spaces: '.format(i=i+1))
		user_tuple = tuple(int(i) for i in user_input.split())
		abc.update({i+1: user_tuple})
	print('\nBest return: $' + str(cloth(X, Y, abc)) + '\n')
