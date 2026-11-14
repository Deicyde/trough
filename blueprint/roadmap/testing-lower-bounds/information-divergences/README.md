# Information divergences

A divergence between measures is a function which maps two measures on any common space $\mathcal X$ to a value in $[-\infty, +\infty]$. For two probability measures $\mu$ and $\nu$, we will want the divergence $D(\mu, \nu)$ to be non-negative and to be zero if $\mu = \nu$ : divergences are meant to be notions of dissimilarity between measures.

We will pay particular attention to how the divergence behaves with respect to transformations of the measures. For a Markov kernel $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ , a fundamental property of all divergences we will consider is the *data-processing inequality*, which states that $D(\kappa \circ \mu, \kappa \circ \nu) \le D(\mu, \nu)$. That is, processing data with a (possibly random) common transformation $\kappa$ can only lose information about the difference between the two measures.

Another important concept is the *conditional divergence* of two kernels $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ given a measure $\mu \in \mathcal M(\mathcal X)$. This is the value $D(\mu \otimes \kappa, \mu \otimes \eta)$.

TODO: two possible concepts of conditional divergence are $D(\mu \otimes \kappa, \mu \otimes \eta)$ and $\mu\left[x \mapsto D(\kappa(x), \eta(x))\right]$. They are equal for $f$-divergences (which gives also convexity of the divergence) but not in general.

- [Statistical divergences](statistical-divergences/README.md)
- [f-divergences](f-divergences/README.md)
- [Kullback-Leibler divergence](kullback-leibler-divergence/README.md)
- [Hellinger alpha-divergences](hellinger-alpha-divergences/README.md)
- [Rényi divergences](renyi-divergences/README.md)
- [Chernoff divergence](chernoff-divergence/README.md)
