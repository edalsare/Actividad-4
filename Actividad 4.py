import pandas as pd

df = pd.read_excel("/content/accidente-de-trafico-en-bogota-entre-2007-y-2017-geopoint.xlsx")
df.head(3)

cond1 = df['ANO_OCURRENCIA']==2017
cond2 = df['DIA_OCURRENCIA']=='LUNES'
cond3 = df['MES_OCURRENCIA']=='ENERO'

newDF = df[cond1 & cond2 & cond3]
newDF.info()

newDF = newDF["Geo Point"].str.split(',', expand=True)
newDF.columns = ['y', 'x']
newDF.info()

newDF['x'] = newDF['x'].astype(float)
newDF['y'] = newDF['y'].astype(float)
newDF.info()

import matplotlib.pyplot as plt

#Creamos una grafica de sipercion
plt.scatter(newDF['x'], newDF['y'])
plt.show()

from sklearn.cluster import KMeans
kmeans =KMeans(n_clusters=10).fit(newDF)
centroid = kmeans.cluster_centers_
print(centroid)

plt.scatter(newDF['x'], newDF['y'], c=kmeans.labels_.astype(float), s=30, alpha=0.5)
plt.scatter(centroid[:,1], centroid[:,0], c='red', s=50, alpha=1)
plt.show()