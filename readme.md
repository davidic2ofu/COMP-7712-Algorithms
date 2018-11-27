David Rosenberg
U00063482
COMP 7712

Programming Assignment 3

NOTE: This dynamic programming solution runs in O( X Y n ) time, which
is the upper bound of time it takes to populate the value array.  It
works basically like a 2-d n-knapsack problem.


CLOTH CUTTING PROBLEM...

6.14. Cutting cloth. You are given a rectangular piece of cloth with 
dimensions X × Y , where X and Y are positive integers, and a list of 
n products that can be made using the cloth. For each product i ∈ [1, 
n] you know that a rectangle of cloth of dimensions ai × bi is needed 
and that the final selling price of the product is ci. Assume the ai, 
bi, and ci are all positive integers. You have a machine that can cut 
any rectangular piece of cloth into two pieces either horizontally or 
vertically. Design an algorithm that determines the best return on 
the X × Y piece of cloth, that is, a strategy for cutting the cloth 
so that the products made from the resulting pieces give the maximum 
sum of selling prices. You are free to make as many copies of a given 
product as you wish, or none if desired.

Assume the input is given as follows. The first line will be X and Y 
separated by a space symbol. Then, comes n on the next line, and the 
remaining n lines will be ai, bi, ci separated by spaces. The output 
must contain the best return you can get. 
