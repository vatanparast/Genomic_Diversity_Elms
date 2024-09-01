# This script reads the CSV data and creates a SNP density plot.
# Install and load CMplot package 
# https://github.com/YinLiLin/CMplot

install.packages("CMplot")

library(CMplot)

# Read the input data
data <- read.csv('glabra-only_LD-pruned.bim.csv', header = TRUE, sep = ",")

# Plot SNP density
CMplot(data, plot.type="d", bin.size=1e6, chr.den.col=c("darkgreen", "yellow", "red"),
       file="pdf", file.name="SNP_Density_glabra.pdf", dpi=300, main="SNP Density , U. glabra", file.output=TRUE,verbose=TRUE,width=9,height=3,legend.cex=0.6)


