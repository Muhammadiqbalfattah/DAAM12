#!/usr/bin/env python
# coding: utf-8

# In[77]:


import networkx as nx
import matplotlib.pyplot as plt


# In[78]:


vertices = range(1,10)
edges =[(7,2),(2,3),(7,4),(4,5),(7,3),(7,5),(1,6),(1,7),(2,8),(2,9),(10,2)]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels=True, node_color='y', node_size=900)


# In[79]:


nx.degree_centrality(G)


# In[80]:


nx.betweenness_centrality(G)


# In[81]:


nx.closeness_centrality(G)


# In[82]:


centrality = nx.eigenvector_centrality(G)


# In[83]:


sorted((v,'{:0.2f}'.format(c)) for v, c in centrality.items())


# In[95]:


#latihan 1
vertices = range(1,9)
edges =[(7,2),(2,3),(3,1),(7,4),(4,2),(4,5),(7,3),(7,5),(5,1),(1,4),(1,6),(6,3),(6,5),(1,7),(8,9),(2,9)
       ]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels=True, node_color='y', node_size=1000)


# In[93]:


centrality = nx.eigenvector_centrality(G)


# In[86]:


sorted((v,'{:0.2f}'.format(c)) for v, c in centrality.items())


# In[96]:


#latihan 2
vertices = range(1,15)
edges =[(1,4),(1,10),(1,2),(2,11),(2,15),(2,12),(2,3),(3,13),(3,5),
        (2,6),(6,14),(6,9),(6,7),(6,8)
        
       ]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels=True, node_color='g', node_size=1000)


# In[88]:


centrality = nx.eigenvector_centrality(G)


# In[89]:


sorted((v,'{:0.2f}'.format(c)) for v, c in centrality.items())


# In[ ]:


G_fb = nx.read.edgelist("C:\Users\User\Downloads\facebook_combined.txt", create_using = nx.Graph(), nodetype=int)


# In[ ]:


print(nx.info(G_fb))


# In[ ]:


pos = nx.spring_layout(G_fb)
betCent = nx.between_centrality(G_fb, normalized=True, endpoints=True)
node_color = [20000.0 * G_fb.degree(v) for v in G_fb]
node_size = [v *10000 for v in betCent.values()]
plt.figure(figsize =(20,20))
nx.draw_networkx(G_fb, pos=pos, with_labels=False,
                node_color = node_color,
                node_size = node_size)
plt.axis ('off')

