from sklearn.preprocessing import Normalizer
from mywork import *
from sklearn.pipeline import make_pipeline
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from tomark import Tomark 

def plot_us():
    us_mv_dict={}
    for i in range(15):
        us_mv_dict[us_companies[i]]=np.mean(us_movements[i])
        plt.plot(us_data[:900].index,us_movements[i])
        plt.title(us_companies[i])
        #plt.savefig(f"Images/movements/{us_companies[i]}.png")
    return us_mv_dict
def plot_china():
    c_mv_dict={}
    for i in range(15):
        c_mv_dict[china_companies[i]]=np.mean(china_movements[i])
        plt.plot(china_data[:900].index,china_movements[i])
        plt.title(china_companies[i])
        #plt.savefig(f"Images/movements/{china_companies[i]}.png")
    return c_mv_dict
def plot_movements():
    mv_dict={}
    for i in range(30):
        mv_dict[companies[i]]=np.mean(movements[i])
        plt.plot(us_data[:900].index, movements[i])
        plt.title(companies[i])
        #plt.savefig(f"Images/movements/{companies[i]}.png")
    return mv_dict

#implement Kmeans
def km(movements, clusters=2):
    normalizer=Normalizer()
    kmeans=KMeans(n_clusters=clusters, max_iter=1000)
    pipeline=make_pipeline(normalizer, kmeans)
    pipeline.fit(movements)
    labels=pipeline.predict(movements)
    df=pd.DataFrame({'labels':labels, "companies":companies})
    return (df.sort_values('labels'))

#implement PCA
def pca(movements, clusters=2):
    normalizer=Normalizer()
    new=normalizer.fit_transform(movements)
    reduced_data=PCA(n_components=2).fit_transform(new)
    kmeans=KMeans(n_clusters=2)
    kmeans.fit(reduced_data)
    labels=kmeans.predict(reduced_data)
    df=pd.DataFrame({'labels':labels, "companies":companies})
    
    #determine size of meshplot
    h = 0.01

    # plot the decision boundary
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:,0].max() + 1
    y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:,1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Obtain labels for each point 
    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

    # Placing in plot
    Z = Z.reshape(xx.shape)

    # define colorplot
    cmap = plt.cm.Paired

    # plot figure
    plt.clf()
    plt.figure(figsize=(10,10))
    plt.imshow(Z, interpolation='nearest',
    extent = (xx.min(), xx.max(), yy.min(), yy.max()),
    cmap = cmap,
    aspect = 'auto', origin='lower')
    plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=5)


    # plot the centroids for each cluster
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1],
    marker='x', s=169, linewidth=3,
    color='w', zorder=10)

    plt.title('K-Means Clustering on Stock Market Movements (PCA-Reduced Data)')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.show()



df1=pd.DataFrame.from_dict(plot_movements(), orient='index')
print(df1.to_markdown())