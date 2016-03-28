import sys
from collections import defaultdict
import numpy as np

dict_input_Points={}
display_list=[0]
dic_center_points={}
dict_initial_points={}
dict_input_Points1={}
label1=""
cluster_name=[]

def read(input_file,initial_points,k,noOfIterations):
    data = list()
    data = [l.strip() for l in input_file if l.strip()]
    points = [tuple(map(float, x.split(',')[:-1])) for x in data]
    labels_input = [x.split(',')[-1] for x in data]

    data_initialPoints = [l.strip() for l in initial_points if l.strip()]
    initial_points = [tuple(map(float, x.split(',')[:-1])) for x in data_initialPoints]
    
    label_initial=[x.split(',')[-1] for x in data_initialPoints]

    dict_initial_points=dict(zip(initial_points,label_initial))
    dict_input_Points=dict(zip(points, labels_input))
    dict_input_Points1=dict(zip(labels_input,points))
    
    points1 = dict_input_Points.keys()
    
    clusters = kmeans(points,initial_points,k,noOfIterations,dict_input_Points,dict_initial_points,dict_input_Points1)

def kmeans(points,initial_points,k,noOfIterations,dict_input_Points,dict_initial_points1,dict_input_Points1):
    count=0
    label=""
    centers = dict((c,[c]) for c in initial_points[::-1])
   
    for i in xrange(noOfIterations):
        new_centers = assign(centers,points)
        new_centers = update(new_centers)
        if centers == new_centers:
            break
        else:
            centers = new_centers
    count3=0    
    for k,v in centers.items():  
        count=0    
        display_list1=display(v,dict_input_Points)
        list_temp=[]
        for x in display_list1:
            list_temp.append(x[4])

        dict_temp={}    
        for x in list_temp:
            if(dict_temp.get(x)==None):
                dict_temp[x]=1
            else:
                dict_temp[x]+=1
                
        val1=0
   
        for ran in range(0,len(dict_temp)):
            temp=dict_temp.keys()[ran]
            val=dict_temp.get(temp)
            if(val>=val1):
                val1=val

    
        for ran in range(0,len(dict_temp)):
            temp=dict_temp.keys()[ran]
            if(dict_temp.get(temp)==val1):
                cluster_name=(dict_temp.keys()[ran])

               
        for x in list_temp:
            if(x!=cluster_name):
                count3+=1     

        print("cluster :",cluster_name)

        for x in display_list1:
            print(x)

    print("\n")        
    print("number of points wrongly assigned")  
    print(count3)      
    
def display(v,dict_input_Points):
        display_list=[]
        print("\n")
        for val in v: 
            label=dict_input_Points.get(val)
            val=list(val)
            val.append(label)
            #print(val)
            display_list.append(val)
        return(display_list)

def assign(centers,points):
    best=()
    new_centers = defaultdict(list)
    for p in points:
        list_points=[]
        for c in centers:
            if(p!=c):
                best = min(centers, key=lambda c: distance(p,c))
        new_centers[best] += [p]
    return new_centers
    
def distance(poi, cen):
    a = np.array
    d = a(poi)-a(cen)
    return np.sqrt(np.dot(d, d))

def update(centers):
    new_centers = {}
    for c in centers:
        new_centers[mean(centers[c])] = centers[c]
    return new_centers  

def mean(feats):
    return tuple(np.mean(feats, axis=0)) 

def main():
   input_file = open(sys.argv[1])
   k=int(sys.argv[2])
   noOfIterations=int(sys.argv[3])
   initial_points=open(sys.argv[4])
   read(input_file,initial_points,k,noOfIterations)

if __name__ == '__main__':
    main()    
