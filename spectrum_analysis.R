library(igraph)
# Load graph
g <- read.graph(file="<filename>.net", format="pajek")
# Make it undirected
g <- as.undirected(g, mode = "collapse")
# Convert it into an adjacency matrix
m <- get.adjacency(g, type="both")
# Compute eigenvalues and eigenvectors
e <- as.data.frame(eigen(m, symmetric = TRUE, only.values = FALSE, EISPACK = FALSE))
# Plot
ggplot(e, aes(x=values)) + geom_density(alpha=.3)
