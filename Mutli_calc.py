#simple calcutlator for mutli-trunk trees in inches from a csv file
#adding the total diameter of the largest trunk to one-half the diameter of each additional trunk
#Methodoloy can be found here: https://www.portland.gov/trees/tree-care-and-resources/how-measure-tree#toc-measuring-multi-stemmed-trees
#Date: 090822
#For educational purposes only

#Importing csv file

#CSV FORMAT:
#ID,X,Y,ELEV,TYPE SPREAD T1xT2xT3x.....

#Importing CSV
import csv
file = open("tree_test.csv")
reader = csv.reader(file)
#Getting the number of lines in the file
lines= len(list(reader))

#creating tree to store multi trunk values
tree = []
i = 0

#Opening CSV
with open("tree_test.csv") as f:
        reader = csv.reader(f)

        #for each row of the csv:
        for row in reader:
                
            #isolating the multi trunk string
            tree = (row[lines-1]).split(' ')
                
            #removing the "x" spacing
            treelist = tree[2].split('x')
                
            #converting text to float
            Prep = [float(i) for i in treelist]
                
            #mutlitrunk calculation formula:
            multi_dia = (((sum(Prep)-max(Prep))/2)+max(Prep))

            #returning the final result:
            print("The multi-trunk diameter is: ",round(multi_dia,2))







