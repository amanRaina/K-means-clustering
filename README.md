# K-means-clustering

K-Means Clustering

Implementation of the k-means clustering algorithm to cluster a data set. Used a data set from the UC Irvine Machine Learning Repository at: https://archive.ics.uci.edu/ml/index.html.

Format of data file

The data file that is being clustered is a database related to iris plants. A complete description can be found here:
https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names
Will use the file at https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data as our input file. Each line of the csv file looks something like this: 5.1,3.5,1.4,0.2,Iris-setosa
It consists of four floating point values and a text label for the type of iris plant.
The four floating point attributes correspond to:
1. sepal length in cm 2. sepal width in cm 3. petal length in cm 4. petal width in cm
The string attribute is the iris class, one of the following:
-- Iris Setosa
-- Iris Versicolour -- Iris Virginica

program should do the following:

1. Read the data from the file. Use only the floating point values for the clustering. Don’t discard the class information. We will need it later for assigning names to the clusters and for checking the accuracy of the clusters.
2. Apply the k-means algorithm to find clusters. (There are 3 natural clusters in the case of the iris data.) (See below for more information on k-means.) Use Euclidean distance as your distance measure.
3. Assign each final cluster a name by choosing the most frequently occurring class label of the examples in the cluster.
4. Find the number of data points that were put in clusters in which they didn’t belong (based on having a different class label than the cluster name).
k-means algorithm:

For each point, place it in the cluster whose current centroid it is nearest
After all points are assigned, update the locations of centroids of the k clusters
Repeat for the specified number of iterations.

Output of your program

The program will produce output of the form:
Cluster <clustername1>:
(List of points in that cluster, one per line)
Cluster <clustername2>:
(List of points in that cluster, one per line)
Cluster <clustername3>:
(List of points in that cluster, one per line)
Number of points assigned to wrong cluster: (number of points)

Running the code

python filename.py dataFileName k iter initialPoints where:
dataFileName is a string indicating the name of the data file to be clustered
k is an integer representing the number of clusters (three in the case of the iris data set) iter is the number of iterations for the k-means clustering to run