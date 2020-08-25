from sklearn.preprocessing import Normalizer
from mywork import *
from sklearn.pipeline import make_pipeline
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

normalizer=Normalizer()
new=normalizer.fit_transform(movements)


# china_new=normalizer.fit_transform(china_movements)


# fig, axs=plt.subplots(3,5)
# axs=axs.ravel()
# for i in range(15):
#     axs[i].plot(us_movements[i][:])
#     plt.title(us_companies[i])
#     plt.show()

kmeans=KMeans(n_clusters=2, max_iter=1000)
pipeline=make_pipeline(normalizer, kmeans)
pipeline.fit(movements)
labels=pipeline.predict(movements)
df=pd.DataFrame({'labels':labels, "companies":companies})

reduced_data=PCA(n_components=2).fit_transform(new)
kmeans2=KMeans(n_clusters=2)
kmeans2.fit(reduced_data)
labels=kmeans2.predict(reduced_data)
df2=pd.DataFrame({'labels':labels, "companies":companies})
print(df2.sort_values('labels'))



h = 0.01

# plot the decision boundary
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:,0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:,1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain abels for each point in the mesh using our trained model
Z = kmeans2.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
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


# plot the centroid of each cluster as a white X
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1],
 marker='x', s=169, linewidth=3,
 color='w', zorder=10)

plt.title('K-Means Clustering on Stock Market Movements (PCA-Reduced Data)')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.show()