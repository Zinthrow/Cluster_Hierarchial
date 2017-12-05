# Cluster_Hierarchial
A bottom-up Agglomerative cluster which is given an input of relative gene expression sets and outputs the average of all values per cluster.  Each cluster is printed out in ascending order with the subclusters printed in a similar ascending format. The Program takes The raw gene files in tab separated values (.tsv); either a single link, complete link, or average link; and the "k" value. 

The clusterun.sh file can be changed to handle a couple different parameters it should look like:

example:
python3 tiny-yeast.tsv S 5
python2 c-elegans.tsv A 2

clusterun.sh can then be executed from the terminal
