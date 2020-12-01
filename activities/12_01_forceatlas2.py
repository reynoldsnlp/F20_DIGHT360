"""Example of visualizing topic model using ForceAtlas2 algorithm."""

from fa2 import ForceAtlas2  # python3 -m pip install --user fa2
import matplotlib.pyplot as plt  # python3 -m pip install --user matplotlib
import networkx as nx  # python3 -m pip install --user networkx

with open('doc_topics.csv') as t_file:
    e = t_file.readlines()[1:]  # first line is header
edges = []
for line in e:
    doc, topic, _, weight = line.split(',')
    edges.append((doc[8:-5], topic, weight))


g = nx.Graph()
g.add_weighted_edges_from(edges)
print(g.edges())


forceatlas2 = ForceAtlas2(# Behavior alternatives  # noqa: E261
                          outboundAttractionDistribution=True,  # Dissuade hubs
                          linLogMode=False,  # NOT IMPLEMENTED
                          adjustSizes=False,  # Prevent overlap (NOT IMPLEMENTED)
                          edgeWeightInfluence=1.0,

                          # Performance
                          jitterTolerance=1.0,  # Tolerance
                          barnesHutOptimize=True,
                          barnesHutTheta=1.2,
                          multiThreaded=False,  # NOT IMPLEMENTED

                          # Tuning
                          scalingRatio=2.0,
                          strongGravityMode=False,
                          gravity=1.0,

                          # Log
                          verbose=True)

positions = forceatlas2.forceatlas2_networkx_layout(g, pos=None, iterations=2000)
print(positions)
nx.draw_networkx(g, positions, cmap=plt.get_cmap('jet'), node_size=75,
                 with_labels=True, font_size=6,
                 label=f'Topics in 10-2017 General Conference')
plt.show()
