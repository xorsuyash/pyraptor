from sklearn import GaussianMixture
import umap 
import numpy as np  

class TreeNode:
    def __init__(self, value):
        self.value = value  
        self.children = []

def fit_gmm_and_cluster(data, n_components_range):
    best_gmm, best_bic = None, np.inf
    for n_components in n_components_range:
        gmm = GaussianMixture(n_components=n_components, random_state=0).fit(data)
        bic = gmm.bic(data)
        if bic < best_bic:
            best_bic, best_gmm = bic, gmm
    labels = best_gmm.predict(data)
    return labels, best_gmm

def recursive_cluster_summarize(node, vectors, depth=0, max_depth=5):
    if depth == max_depth:
        return
    
   
    umap = umap(n_neighbors=15, min_dist=0.1, n_components=50)
    reduced_vectors = umap.fit_transform(vectors)
    
    
    labels, gmm = fit_gmm_and_cluster(reduced_vectors, range(2, 10))
    
    for cluster_id in np.unique(labels):
        cluster_vectors = vectors[labels == cluster_id]
        summary_vector = np.mean(cluster_vectors, axis=0)
        child_node = TreeNode(summary_vector)
        node.children.append(child_node)
        
        # Recursive call
        recursive_cluster_summarize(child_node, cluster_vectors, depth+1, max_depth)