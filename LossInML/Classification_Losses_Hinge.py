#Classification Losses
#Hinge Loss or Multi Class SVM Loss
"""
In simple terms, the score of correct category should be greater 
than sum of scores of all incorrect categories by some safety 
margin (usually one). And hence hinge loss is used for 
maximum-margin classification, most notably for 
support vector machines. Although not differentiable, 
it’s a convex function which makes it easy to work with 
usual convex optimizers used in machine learning domain.

Data -
			1 				2 				3
Dog		  -0.39			  -4.61			   1.03		
Cat   	   1.49			   3.28			  -2.37
Horse	   4.21            1.46           -2.27

Note -  First We Get Loss of Dog, Cat and then Horse
"""
#Dog

max(0, (1.49) - (-0.39) + 1) + max(0, (4.21) - (-0.39) + 1)
max(0, 2.88) + max(0, 5.6)
2.88 + 5.6
8.48 # (High loss as very wrong prediction)

#Cat

max(0, (-4.61) - (3.28)+ 1) + max(0, (1.46) - (3.28)+ 1)
max(0, -6.89) + max(0, -0.82)
0 + 0
0 #(Zero loss as correct prediction)

#Horse

max(0, (1.03) - (-2.27)+ 1) + max(0, (-2.37) - (-2.27)+ 1)
max(0, 4.3) + max(0, 0.9)
4.3 + 0.9
5.2 #High loss as very wrong prediction)


