# Proof of Finitary Carleson

To prove Proposition [finitary Carleson](../proof-of-metric-space-carleson-overview/finitary-carleson.md), we already fixed in [Proof of Metric Space Carleson, overview](../proof-of-metric-space-carleson-overview/README.md) measurable functions ${\sigma_1},\sigma_2, {Q}$ and Borel sets $F,G$. We have also defined $S$ to be the smallest integer such that the ranges of $\sigma_1$ and $\sigma_2$ are contained in $[-S,S]$ and $F$ and $G$ are contained in the ball $B(o, \frac 14 D^S)$.

The proof of the next lemma is done in Proof of Grid Existence Lemma, following the construction of dyadic cubes in (christ1990b, § 3).

- [grid existence](grid-existence.md)

The next lemma, which we prove in Proof of Tile Structure Lemma, should be compared with the construction in (zk-polynomial, Lemma 2.12).

- [tile structure](tile-structure.md)

Choose a grid structure $(\mathcal{D}, c,s)$ with [grid existence](grid-existence.md) and a tile structure for this grid structure $({\mathfrak P},{\mathcal{I}},{\Omega},{\mathcal{Q}},{\mathrm{c}},{\mathrm{s}})$ with [tile structure](tile-structure.md). Applying [discrete Carleson](../proof-of-metric-space-carleson-overview/discrete-carleson.md), we obtain a Borel set $G'$ in $X$ with $2\mu(G')\leq \mu(G)$ such that for all Borel functions $f:X\to {\mathbb{C}}$ with $|f|\le \mathbf{1}_F$ we have [(21)](../proof-of-metric-space-carleson-overview/discrete-carleson.md).

- [tile sum operator](tile-sum-operator.md)

We use this to prove [finitary Carleson](../proof-of-metric-space-carleson-overview/finitary-carleson.md).

*Proof of finitary Carleson: shown with [finitary Carleson](../proof-of-metric-space-carleson-overview/finitary-carleson.md).*

## Proof of Grid Existence Lemma

We begin with the construction of the centers of the dyadic cubes.

- [counting balls](counting-balls.md)

For each $-S\le k\le S$, let $Y_k$ be a set of maximal cardinality in $X$ such that $Y=Y_k$ satisfies the properties [(4)](counting-balls.md) and [(5)](counting-balls.md) and such that $o \in Y_k$. By the upper bound of [counting balls](counting-balls.md), such a set exists.

For each $-S\le k\le S$, choose an enumeration of the points in the finite set $Y_k$ and thus a total order $<$ on $Y_{k}$.

- [cover big ball](cover-big-ball.md)

Define the set

$$
\mathcal{C}:= \{(y,k): -S\le k\le S, y\in Y_k\}\,
$$

We totally order the set $\mathcal{C}$ lexicographically by setting $(y,k)<(y',k')$ if $k< k'$ or both $k=k'$ and $y\lt y'$. In what follows, we define recursively in the sense of this order a function

$$
(I_1,I_2,I_3): \mathcal{C}\to \mathcal{P}(X)\times \mathcal{P}(X)\times \mathcal{P}(X)\, .
$$

Assume the sets ${I}_j(y',k')$ have already been defined for $j=1,2,3$ if $k'\lt k$ and if $k=k'$ and $y'\lt y$.

If $k=-S$, define for $j\in \{1,2\}$ the set ${I}_j(y,k)$ to be $B(y,jD^{-S})$. If $-S\lt k$, define for $j\in \{1,2\}$ and $y\in Y_k$ the set ${I}_j(y,k)$ to be

$$
\bigcup\{I_3(y',k-1):
y'\in Y_{k-1}\cap B(y,jD^k)\}.\qquad\text{(8)}
$$

Define for $-S\leq k\leq S$ and $y\in Y_k$

$$
I_3(y,k):={I_1}(y,k)\cup \left[{I_2}(y,k)\setminus \left[X_k\cup \bigcup\{I_3(y',k):y'\in Y_{k}, y'\lt y\})\right]\right]\qquad\text{(9)}
$$

with

$$
X_{k}:=\bigcup\{I_1(y', k):y'\in Y_{k}\}.
$$

- [basic grid structure](basic-grid-structure.md)
- [cover by cubes](cover-by-cubes.md)
- [dyadic property](dyadic-property.md)

For $-S\le k'\le k\le S$ and $y'\in Y_{k'}$, $y\in Y_k$ write $(y',k'|y,k)$ if $I_3(y',k')\subset I_3(y,k)$ and

$$
\inf_{x\in X\setminus I_3(y,k)}\rho(y',x)<6D^{k'}\, .\qquad\text{(16)}
$$

- [transitive boundary](transitive-boundary.md)
- [small boundary](small-boundary.md)
- [smaller boundary](smaller-boundary.md)
- [boundary measure](boundary-measure.md)

Let $\tilde{\mathcal{D}}$ be the set of all $I_3(y,k)$ with $k\in [-S,S]$ and $y\in Y_k$. Define

$$
s(I_3(y,k)):=k
$$

$$
c(I_3(y,k)):=y\,.
$$

We define $\mathcal{D}$ to be the set of all $I \in \tilde{\mathcal{D}}$ such that $I \subset I_3(o, S)$.

*Proof of grid existence: shown with [grid existence](grid-existence.md).*

## Proof of Tile Structure Lemma

Choose a grid structure $(\mathcal{D}, c, s)$ with [grid existence](grid-existence.md) Let $I \in \mathcal{D}$. Suppose that

$$
\mathcal{Z} \subset {Q}(X)\qquad\text{(27)}
$$

is such that for any ${\vartheta}, {\theta} \in \mathcal{Z}$ with ${\vartheta}\ne {\theta}$ we have

$$
B_{I^\circ}({\vartheta}, 0.3) \cap B_{I^\circ}({\theta}, 0.3) \cap {Q}(X) = \emptyset\,.\qquad\text{(28)}
$$

Since ${Q}(X)$ is finite, there exists a set $\mathcal{Z}$ satisfying both (27) and (28) of maximal cardinality among all such sets. We pick for each $I \in \mathcal{D}$ such a set $\mathcal{Z}(I)$.

- [frequency ball cover](frequency-ball-cover.md)

We define

$$
{\mathfrak P} = \{(I, z) \ : \ I \in \mathcal{D}, z \in \mathcal{Z}(I)\}\,,
$$

$$
{\mathcal{I}}((I, z)) = I\qquad \text{and} \qquad {\mathcal{Q}}((I, z)) = z.
$$

We further set

$$
{\mathrm{s}}({\mathfrak p}) = s({\mathcal{I}}({\mathfrak p})),\qquad \qquad {\mathrm{c}}({\mathfrak p}) = c({\mathcal{I}}({\mathfrak p})).
$$

Then [(17)](../proof-of-metric-space-carleson-overview/README.md), [(18)](../proof-of-metric-space-carleson-overview/README.md) hold by definition.

It remains to construct the map $\Omega$, and verify properties [(13)](../proof-of-metric-space-carleson-overview/README.md), [(14)](../proof-of-metric-space-carleson-overview/README.md) and [(15)](../proof-of-metric-space-carleson-overview/README.md). We first construct an auxiliary map $\Omega_1$. For each $I \in \mathcal{D}$, we pick an enumeration of the finite set $\mathcal{Z}(I)$

$$
\mathcal{Z}(I) = \{z_1, \dotsc, z_M\}\,.
$$

We define $\Omega_1:{\mathfrak P} \mapsto \mathcal{P}({\Theta})$ as below. Set

$$
\Omega_1((I, z_1)) = B_{I^\circ}(z_1, 0.7) \setminus \bigcup_{z \in \mathcal{Z}(I)\setminus \{z_1\}} B_{I^\circ}(z, 0.3)
$$

and then define iteratively

$$
\Omega_1((I, z_k)) = B_{I^\circ}(z_k, 0.7) \setminus \bigcup_{z \in \mathcal{Z}(I) \setminus \{z_k\}} B_{I^\circ}(z, 0.3) \setminus \bigcup_{i=1}^{k-1} \Omega_1((I, z_i))\,.\qquad\text{(30)}
$$

- [disjoint frequency cubes](disjoint-frequency-cubes.md)
- [frequency cube cover](frequency-cube-cover.md)

Now we are ready to define the function $\Omega$. We define for all ${\mathfrak p} \in {\mathfrak P}(I_0)$

$$
{\Omega}({\mathfrak p}) = \Omega_1({\mathfrak p})\,.\qquad\text{(33)}
$$

For all other cubes $I \in \mathcal{D}$, $I \ne I_0$, there exists, by [(8)](../proof-of-metric-space-carleson-overview/README.md) and [(9)](../proof-of-metric-space-carleson-overview/README.md), $J \in \mathcal{D}$ with $I \subset J$ and $I \ne J$. On such $I$ we define $\Omega$ by recursion. We can pick an inclusion minimal $J \in \mathcal{D}$ among the finitely many cubes such that $I \subset J$ and $I \ne J$. This $J$ is unique: Suppose that $J'$ is another inclusion minimal cube with $I \subset J'$ and $I \ne J'$. Without loss of generality, we have that $s(J) \le s(J')$. By [(8)](../proof-of-metric-space-carleson-overview/README.md), it follows that $J \subset J'$. Since $J'$ is minimal with respect to inclusion, it follows that $J = J'$. Then we define

$$
{\Omega}({\mathfrak p}) = \bigcup_{z \in \mathcal{Z}(J) \cap \Omega_1({\mathfrak p})} \Omega((J, z)) \cup B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}),0.2)\,.\qquad\text{(34)}
$$

We now verify that $({\mathfrak P},{\mathcal{I}},{\Omega},{\mathcal{Q}},{\mathrm{c}},{\mathrm{s}})$ forms a tile structure.

*Proof of tile structure: shown with [tile structure](tile-structure.md).*
