import csv as csv
import heapq as hp
def addNewEdgeToClusterSet(clusters,edge):
	distance = edge[0];
	n1 = edge[1][0]
	n2 = edge[1][1]
	fuse =[]
	notFuse =[]

	for cluster in clusters:
		if doesEdgeBelongToCluster(cluster,edge):
			fuse.append(cluster);
		else:
			notFuse.append(cluster);

	if len(fuse)>0:
		clusters = notFuse;
		if len(fuse)>1:
			f = {}
			for i in range(len(fuse)):
				f.update(fuse[i])
		else:
			f = fuse[0]
		f = addNodeToGraph(f,distance,n1,n2)
		clusters.append(f);
	else:
		C = {};
		C = addNodeToGraph(C,distance,n1,n2);
		clusters.append(C);
	return clusters

def doesEdgeBelongToCluster(cluster,edge):
	distance = edge[0];
	n1 = edge[1][0]
	n2 = edge[1][1]
	if(cluster.get(n1)==None and cluster.get(n2)==None):
		return False;
	else:
		return True;

def addNodeToGraph(G,distance,n1,n2):
	if G.get(n1)==None:
		G[n1] = [];
	G[n1].append((n2,distance))

	if G.get(n2) == None:
		G[n2] = [];
	G[n2].append((n1,distance))
	return G

def hamming_distance(s1, s2):
	if s1 == s2:
		return 0
	sum = 0
	for ch1, ch2 in zip(s1, s2):
		if ch1 != ch2:
			sum = sum +1
			if sum >3:
				return sum
	return sum

f  = open('algo2clustering_big.txt', "rb")
reader = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE)
G = {};
clusters =[];
h =[];
nodes = [];
for row in reader:
	n1 = row[0]
	n1.strip()
	nodes.append(n1)
l = len(nodes)

for i in range(l):
	n1 = nodes[i]

	for j in range(i+1,l):
		n2 = nodes[j]
		distance = hamming_distance(n1,n2)
		if distance <=3:
			print n1,n2,distance
			G = addNodeToGraph(G,distance,n1,n2);
			hp.heappush(h,(distance,[n1,n2]))
size = len(G)
print G
standAloneNodes = len(nodes)-len(G)

print "stand Alone nodes"
print standAloneNodes

print " Created heap and graph";

actualNumberOfClusters = len(G);


distance = 0
maxDistance =3
while (len(clusters)==0 or distance <=maxDistance) and len(h)>0:
	startClusters = len(clusters)+len(G)
	edge = hp.heappop(h);
	clusters = addNewEdgeToClusterSet(clusters,edge)
	distance = edge[0];
	n1 = edge[1][0];
	n2 = edge[1][1];

	if (G.get(n1)!=None):
		del G[n1]
	if (G.get(n2)!=None):
		del G[n2]
	endClusters = len(clusters)+len(G)
	if distance == maxDistance and startClusters >endClusters:
		finalClusters = startClusters
		break
	elif len(h)==0:
		finalClusters = endClusters
		
print finalClusters
print standAloneNodes
print standAloneNodes+finalClusters
exit()
