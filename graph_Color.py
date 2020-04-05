class node:
    def __init__(self,ad_list,id,visited):
        self.num=id
        self.ad_list=ad_list
        self.visited=visited
        self.color_node='null'

n=int(input("enter the no of nodes"))
colors=[]
nodes=[]
color_used=[]
for i in range(n):
    colors.append(chr(65+i))
    print("enter the node adjacent to ",i)
    x=input().split(',')
    li=[]
    for j in x:
        li.append(int(j))
    nodes.append(node(li,i,0))

for  i in range(n):
    if nodes[i].visited==1:
        pass
    else:
        for color in colors:
            if(nodes[i].visited==0):
                c=0
                for j in nodes[i].ad_list:
                    if(nodes[j].color_node==color):
                        c+=1
                if(c==0):
                    nodes[i].color_node=color
                    color_used.append(color)
                    nodes[i].visited=1
for i in range(n):
    print(nodes[i].num,"color used : ",nodes[i].color_node)
print("no of colors used",len(set(color_used)))

                


    
  







            





