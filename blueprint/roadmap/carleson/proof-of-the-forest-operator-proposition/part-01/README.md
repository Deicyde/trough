---
navigation: transparent
---

# convex scales to overlap implies distance

- [convex scales](convex-scales.md)

For a nonempty collection of tiles $\mathfrak{S} \subset {\mathfrak P}$ we define

$$
\mathcal{J}_0(\mathfrak{S})
$$

to be the collection of all dyadic cubes $J \in \mathcal{D}$ such that $s(J) = -S$ or

$$
{\mathcal{I}}({\mathfrak p}) \not\subset B(c(J), 100D^{s(J) + 1})
$$

for all ${\mathfrak p} \in \mathfrak{S}$. We define $\mathcal{J}(\mathfrak{S})$ to be the collection of inclusion maximal cubes in $\mathcal{J}_0(\mathfrak{S})$.

We further define

$$
\mathcal{L}_0(\mathfrak{S})
$$

to be the collection of dyadic cubes $L \in \mathcal{D}$ such that $s(L) = -S$, or there exists ${\mathfrak p} \in \mathfrak{S}$ with $L \subset {\mathcal{I}}({\mathfrak p})$ and there exists no ${\mathfrak p} \in \mathfrak{S}$ with ${\mathcal{I}}({\mathfrak p}) \subset L$. We define $\mathcal{L}(\mathfrak{S})$ to be the collection of inclusion maximal cubes in $\mathcal{L}_0(\mathfrak{S})$.

- [dyadic partitions](dyadic-partitions.md)

For a finite collection of pairwise disjoint cubes $\mathcal{C}$, define the projection operator

$$
P_{\mathcal{C}}f(x) :=\sum_{J\in\mathcal{C}}\mathbf{1}_J(x) \frac{1}{\mu(J)}\int_J f(y) \, \mathrm{d}\mu(y)\,.
$$

Given a scale $-S \le s\le S$ and a point $x \in \bigcup_{I\in \mathcal{D}, s(I) = s} I$, there exists a unique cube in $\mathcal{D}$ of scale $s$ containing $x$ by [(7)](../../proof-of-metric-space-carleson-overview/README.md). We denote it by $I_s(x)$. Define for ${\vartheta} \in {\Theta}$ the nontangential maximal operator

$$
T_{\mathcal{N}}^{\vartheta} f(x) := \sup_{-S \le s_1 < S} \sup_{x' \in I_{s_1}(x)} \sup_{\substack{s_1 \le s_2 \le S\\ D^{s_2-1} \le R_Q({\vartheta}, x')}} \left| \sum_{s = s_1}^{s_2} \int K_s(x',y) f(y) \, \mathrm{d}\mu(y) \right|\,.\qquad\text{(3)}
$$

Define for each ${\mathfrak u} \in {\mathfrak U}$ the auxiliary operator

$$
S_{1,{\mathfrak u}}f(x)
$$

$$
:=\sum_{I\in\mathcal{D}} \mathbf{1}_{I}(x) \sum_{\substack{J\in \mathcal{J}({\mathfrak T}({\mathfrak u}))\\
J\subset B(c(I), 16 D^{s(I)})\\ s(J) \le s(I)}} \frac{D^{(s(J) - s(I))/a}}{\mu(B(c(I), 16D^{s(I)}))}\int_J |f(y)| \, \mathrm{d}\mu(y)\,.\qquad\text{(4)}
$$

Define also the collection of balls

$$
\mathcal{B} = \{B(c(I), 2^s D^{s(I)+t}) \ : \ I \in \mathcal{D}\,, 0 \le s \le S + 5\,, 0 \le t \le 2S+3\}\,.
$$

The following pointwise estimate for operators associated to sets ${\mathfrak T}({\mathfrak u})$ is the main result of this subsection.

- [pointwise tree estimate](pointwise-tree-estimate.md)
- [first tree pointwise](first-tree-pointwise.md)
- [second tree pointwise](second-tree-pointwise.md)
- [third tree pointwise](third-tree-pointwise.md)

## An auxiliary $L^2$ tree estimate

In this subsection we prove the following estimate on $L^2$ for operators associated to trees.

- [tree projection estimate](tree-projection-estimate.md)

Below, we deduce [tree projection estimate](tree-projection-estimate.md) from [pointwise tree estimate](pointwise-tree-estimate.md) and the following estimates for the operators in [pointwise tree estimate](pointwise-tree-estimate.md).

- [nontangential operator bound](nontangential-operator-bound.md)
- [boundary operator bound](boundary-operator-bound.md)

*Proof of tree projection estimate: shown with [tree projection estimate](tree-projection-estimate.md).*

Now we prove the two auxiliary lemmas. We begin with the nontangential maximal operator $T_{\mathcal{N}}$.

*Proof of nontangential operator bound: shown with [nontangential operator bound](nontangential-operator-bound.md).*

We need the following lemma to prepare the $L^2$-estimate for the auxiliary operators $S_{1, {\mathfrak u}}$.

- [boundary overlap](boundary-overlap.md)

Now we can bound the operators $S_{1, {\mathfrak u}}$.

*Proof of boundary operator bound: shown with [boundary operator bound](boundary-operator-bound.md).*

## The quantitative $L^2$ tree estimate

The main result of this subsection is the following quantitative bound for operators associated to trees, with decay in the densities $\operatorname{\operatorname{dens}}_1$ and $\operatorname{\operatorname{dens}}_2$.

- [densities tree bound](densities-tree-bound.md)

Below, we deduce this lemma from [tree projection estimate](tree-projection-estimate.md) and the following two estimates controlling the size of support of the operator and its adjoint.

- [local dens1 tree bound](local-dens1-tree-bound.md)
- [local dens2 tree bound](local-dens2-tree-bound.md)

*Proof of densities tree bound: shown with [densities tree bound](densities-tree-bound.md).*

Now we prove the two auxiliary estimates.

*Proof of local dens1 tree bound: shown with [local dens1 tree bound](local-dens1-tree-bound.md).*

*Proof of local dens2 tree bound: shown with [local dens2 tree bound](local-dens2-tree-bound.md).*

## Almost orthogonality of separated trees

The main result of this subsection is the almost orthogonality estimate for operators associated to distinct trees in a forest in [correlation separated trees](correlation-separated-trees.md) below. We will deduce it from Lemmas [correlation distant tree parts](correlation-distant-tree-parts.md) and [correlation near tree parts](correlation-near-tree-parts.md), which are proven in Subsections Proof of the Tiles with large separation Lemma and Proof of The Remaining Tiles Lemma, respectively. Before stating it, we introduce some relevant notation.

The adjoint of the operator $T_{{\mathfrak p}}$ defined in [(20)](../../proof-of-metric-space-carleson-overview/discrete-carleson.md) is given by

$$
T_{{\mathfrak p}}^* g(x) = \int_{E({\mathfrak p})} \overline{K_{{\mathrm{s}}({\mathfrak p})}(y,x)} e(-{Q}(y)(x)+ {Q}(y)(y)) g(y) \, \mathrm{d}\mu(y)\,.\qquad\text{(25)}
$$

- [adjoint tile support](adjoint-tile-support.md)
- [adjoint tree estimate](adjoint-tree-estimate.md)

We define

$$
S_{2,{\mathfrak u}}g := \left|\sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}}^*g \right| + M_{\mathcal{B},1}g + |g|\,.
$$

- [adjoint tree control](adjoint-tree-control.md)

Now we are ready to state the main result of this subsection.

- [correlation separated trees](correlation-separated-trees.md)
- [correlation distant tree parts](correlation-distant-tree-parts.md)
- [correlation near tree parts](correlation-near-tree-parts.md)

In the proofs of both lemmas, we will need the following observation.

- [overlap implies distance](overlap-implies-distance.md)
