# Proof of Metric Space Carleson, overview

This section organizes the proof of [metric space Carleson](../introduction/metric-space-carleson.md) into sections [Proof of Metric Space Carleson](../proof-of-metric-space-carleson/README.md), [Proof of Finitary Carleson](../proof-of-finitary-carleson/README.md), [Proof of discrete Carleson](../proof-of-discrete-carleson/README.md), [Proof of the Antichain Operator Proposition](../proof-of-the-antichain-operator-proposition/README.md), [Proof of the Forest Operator Proposition](../proof-of-the-forest-operator-proposition/README.md), [Proof of the Hölder cancellative condition](../proof-of-the-holder-cancellative-condition/README.md), and [Proof of Vitali covering and Hardy–Littlewood](../proof-of-vitali-covering-and-hardy-littlewood/README.md). These sections are mutually independent except for referring to the statements formulated in the present section. [Proof of Metric Space Carleson](../proof-of-metric-space-carleson/README.md) proves the main [metric space Carleson](../introduction/metric-space-carleson.md), while sections [Proof of Finitary Carleson](../proof-of-finitary-carleson/README.md), [Proof of discrete Carleson](../proof-of-discrete-carleson/README.md), [Proof of the Antichain Operator Proposition](../proof-of-the-antichain-operator-proposition/README.md), [Proof of the Forest Operator Proposition](../proof-of-the-forest-operator-proposition/README.md), [Proof of the Hölder cancellative condition](../proof-of-the-holder-cancellative-condition/README.md), and [Proof of Vitali covering and Hardy–Littlewood](../proof-of-vitali-covering-and-hardy-littlewood/README.md) each prove one proposition that is stated in the present section. The present section also introduces all definitions used across these sections.

Auxiliary lemmas proves some auxiliary lemmas that are used in more than one of the sections 3-9.

Let $a, q$ be given as in [metric space Carleson](../introduction/metric-space-carleson.md).

Define

$$
D:= 2^{100 a^2}\, ,\qquad\text{(1)}
$$

$$
\kappa:= 2^{-10a}\,,\qquad\text{(2)}
$$

and

$$
Z := 2^{12a}\,.\qquad\text{(3)}
$$

Let $\psi:{\mathbb{R}} \to {\mathbb{R}}$ be the unique compactly supported, piece-wise linear, continuous function with corners precisely at $\frac 1{4D}$, $\frac 1{2D}$, $\frac 14$ and $\frac 12$ which satisfies

$$
\sum_{s\in \mathbb{Z}} \psi(D^{-s}x)=1\qquad\text{(4)}
$$

for all $x>0$. This function vanishes outside $[\frac1{4D},\frac 12]$, is constant one on $[\frac1{2D},\frac 14]$, and is Lipschitz with constant $4D$.

Let a doubling metric measure space $(X,\rho,\mu, a)$ be given. Let a cancellative compatible collection ${\Theta}$ of functions on $X$ be given. Let $o\in X$ be a point such that ${\vartheta}(o)=0$ for all ${\vartheta}\in {\Theta}$.

Let a Borel measurable function ${Q}:X\to {\Theta}$ with finite range be given. Let a one-sided Calderón–Zygmund kernel $K$ on $X$ be given so that for every ${\vartheta}\in {\Theta}$ the operator $T_{{Q}}^{{\vartheta}}$ defined in [(20)](../introduction/README.md) satisfies [(22)](../introduction/linearised-metric-carleson.md).

For $s\in\mathbb{Z}$, we define

$$
K_s(x,y):=K(x,y)\psi(D^{-s}\rho(x,y))\,,\qquad\text{(5)}
$$

so that for each $x, y \in X$ with $x\neq y$ we have

$$
K(x,y)=\sum_{s\in\mathbb{Z}}K_s(x,y).
$$

In [Proof of Metric Space Carleson](../proof-of-metric-space-carleson/README.md), we prove [metric space Carleson](../introduction/metric-space-carleson.md) and [linearised metric Carleson](../introduction/linearised-metric-carleson.md) from the finitary version, [finitary Carleson](finitary-carleson.md) below. Recall that a function from a measure space to a finite set is measurable if the pre-image of each of the elements in the range is measurable.

- [finitary Carleson](finitary-carleson.md)

Let measurable functions ${\sigma_1}\leq \sigma_2\colon X\to \mathbb{Z}$ with finite range be given. Let bounded Borel sets $F,G$ in $X$ be given. Let $S$ be the smallest integer such that the ranges of $\sigma_1$ and $\sigma_2$ are contained in $[-S,S]$ and $F$ and $G$ are contained in the ball $B(o, \frac{1}{4}D^S)$.

In [Proof of Finitary Carleson](../proof-of-finitary-carleson/README.md), we prove [finitary Carleson](finitary-carleson.md) using a bound for a dyadic model formulated in [discrete Carleson](discrete-carleson.md) below.

A grid structure $(\mathcal{D}, c, s)$ on $X$ consists of a finite collection $\mathcal{D}$ of pairs $(I, k)$ of Borel sets in $X$ and integers $k \in [-S, S]$, the projection $s\colon \mathcal{D}\to [-S, S], (I, k) \mapsto k$ to the second component which is assumed to be surjective and called scale function, and a function $c:\mathcal{D}\to X$ called center function such that the five properties (7), (8), (9), (10), and (11) hold. We call the elements of $\mathcal{D}$ dyadic cubes. By abuse of notation, we will usually write just $I$ for the cube $(I,k)$, and we will write $I \subset J$ to mean that for two cubes $(I,k), (J, l) \in \mathcal{D}$ we have $I \subset J$ and $k \le l$.

For each dyadic cube $I$ and each $-S\le k\lt s(I)$ we have

$$
I\subset \bigcup_{J\in \mathcal {D}: s(J)=k}J\, .\qquad\text{(7)}
$$

Any two non-disjoint dyadic cubes $I,J$ with $s(I)\le s(J)$ satisfy

$$
I\subset J.\qquad\text{(8)}
$$

There exists a $I_0 \in \mathcal{D}$ with $s(I_0) = S$ and $c(I_0) = o$

and for all cubes $J \in \mathcal{D}$, we have

$$
J \subset I_0\,.\qquad\text{(9)}
$$

For any dyadic cube $I$,

$$
c(I)\in B(c(I), \frac{1}{4} D^{s(I)}) \subset I \subset B(c(I), 4 D^{s(I)})\,.\qquad\text{(10)}
$$

For any dyadic cube $I$ and any $t$ with $tD^{s(I)} \ge D^{-S}$,

$$
\mu(\{x \in I \ : \ \rho(x, X \setminus I) \leq t D^{s(I)}\}) \le 2 t^\kappa \mu(I)\,.\qquad\text{(11)}
$$

A tile structure $({\mathfrak P},{\mathcal{I}},{\Omega},{\mathcal{Q}},{\mathrm{c}},{\mathrm{s}})$ for a given grid structure $(\mathcal{D}, c, s)$ is a finite set ${\mathfrak P}$ of elements called tiles with five maps

$$
\begin{aligned}
{\mathcal{I}}&\colon {\mathfrak P}\to {\mathcal{D}}\\
{\Omega}&\colon {\mathfrak P}\to \mathcal{P}({\Theta}) \\
{\mathcal{Q}} &\colon {\mathfrak P}\to {Q}(X)\\
{\mathrm{c}} &\colon {\mathfrak P}\to X\\
{\mathrm{s}} &\colon {\mathfrak P}\to \mathbb{Z}
\end{aligned}
$$

with ${\mathcal{I}}$ surjective and $\mathcal{P}({\Theta})$ denoting the power set of ${\Theta}$ such that the five properties (13), (14), (15), (17), and (18) hold. For each dyadic cube $I$, the restriction of the map $\Omega$ to the set

$$
{\mathfrak P}(I)=\{{\mathfrak p}: {\mathcal{I}}({\mathfrak p}) =I\}\qquad\text{(12)}
$$

is injective and we have the disjoint covering property (we use the union symbol with dot on top to denote a disjoint union)

$$
{Q}(X)\subset \dot{\bigcup}_{{\mathfrak p}\in {\mathfrak P}(I)}{\Omega}({\mathfrak p}).\qquad\text{(13)}
$$

For any tiles ${\mathfrak p},{\mathfrak q}$ with ${\mathcal{I}}({\mathfrak p})\subset {\mathcal{I}}({\mathfrak q})$ and ${\Omega}({\mathfrak p}) \cap {\Omega}({\mathfrak q}) \neq \emptyset$ we have

$$
{\Omega}({\mathfrak q})\subset {\Omega}({\mathfrak p}) .\qquad\text{(14)}
$$

For each tile ${\mathfrak p}$,

$$
{\mathcal{Q}}({\mathfrak p})\in B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), 0.2) \subset {\Omega}({\mathfrak p}) \subset B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}),1)\,,\qquad\text{(15)}
$$

where

$$
B_{{\mathfrak p}} ({\vartheta}, R) := \{{\theta} \in {\Theta} \, : \, d_{{\mathfrak p}}({\vartheta}, {\theta}) < R\,\} ,
$$

and

$$
d_{{\mathfrak p}} := d_{B({\mathrm{c}}({\mathfrak p}),\frac 14 D^{{\mathrm{s}}({\mathfrak p})})}\, .\qquad\text{(16)}
$$

We have for each tile ${\mathfrak p}$

$$
{\mathrm{c}}({\mathfrak p})=c({\mathcal{I}}({\mathfrak p})),\qquad\text{(17)}
$$

$$
{\mathrm{s}}({\mathfrak p})=s({\mathcal{I}}({\mathfrak p})).\qquad\text{(18)}
$$

- [discrete Carleson](discrete-carleson.md)

The proof of [discrete Carleson](discrete-carleson.md) is done in [Proof of discrete Carleson](../proof-of-discrete-carleson/README.md) by a reduction to two further propositions that we state below.

Fix a grid structure $(\mathcal{D}, c, s)$ and a tile structure $({\mathfrak P},{\mathcal{I}},{\Omega},{\mathcal{Q}},{\mathrm{c}},{\mathrm{s}})$ for this grid structure.

We define the relation

$$
{\mathfrak p}\le {\mathfrak p}'\qquad\text{(22)}
$$

on ${\mathfrak P}\times {\mathfrak P}$ meaning ${\mathcal{I}}({\mathfrak p})\subset {\mathcal{I}}({\mathfrak p}')$ and $\Omega({\mathfrak p}')\subset \Omega({\mathfrak p})$. We further define for $\lambda,\lambda' >0$ the relation

$$
\lambda {\mathfrak p} \lesssim \lambda' {\mathfrak p}'\qquad\text{(23)}
$$

on ${\mathfrak P}\times {\mathfrak P}$ meaning ${\mathcal{I}}({\mathfrak p})\subset {\mathcal{I}}({\mathfrak p}')$ and

$$
B_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'),\lambda') \subset B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}),\lambda)\, .
$$

Define for a tile ${\mathfrak p}$ and $\lambda>0$

$$
E_1({\mathfrak p}):=\{x\in {\mathcal{I}}({\mathfrak p})\cap G: {Q}(x)\in {\Omega}({\mathfrak p})\}\, ,\qquad\text{(24)}
$$

$$
E_2(\lambda, {\mathfrak p}):=\{x\in {\mathcal{I}}({\mathfrak p})\cap G: {Q}(x)\in B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), \lambda)\}\, .\qquad\text{(25)}
$$

Given a subset ${\mathfrak P}'$ of ${\mathfrak P}$, we define ${\mathfrak P}({\mathfrak P}')$ to be the set of all ${\mathfrak p} \in {\mathfrak P}$ such that there exist ${\mathfrak p}' \in {\mathfrak P}'$ with ${\mathcal{I}}({\mathfrak p})\subset {\mathcal{I}}({\mathfrak p}')$. Define the densities

$$
{\operatorname{\operatorname{dens}}}_1({\mathfrak P}') := \sup_{{\mathfrak p}'\in {\mathfrak P}'}\sup_{\lambda \geq 2} \lambda^{-a} \sup_{{\mathfrak p} \in {\mathfrak P}({\mathfrak P}'), \lambda {\mathfrak p}' \lesssim \lambda {\mathfrak p}}
\frac{\mu({E}_2(\lambda, {\mathfrak p}))}{\mu({\mathcal{I}}({\mathfrak p}))}\, ,\qquad\text{(26)}
$$

$$
{\operatorname{\operatorname{dens}}}_2({\mathfrak P}') := \sup_{{\mathfrak p}'\in {\mathfrak P}'}
\sup_{r\ge 4D^{{\mathrm{s}}({\mathfrak p})}}
\frac{\mu(F\cap B({\mathrm{c}}({\mathfrak p}),r))}{\mu(B({\mathrm{c}}({\mathfrak p}),r))}\, .\qquad\text{(27)}
$$

An antichain is a subset $\mathfrak{A}$ of ${\mathfrak P}$ such that for any distinct ${\mathfrak p},{\mathfrak q}\in \mathfrak{A}$ we do not have ${\mathfrak p}\le {\mathfrak q}$.

The following proposition is proved in [Proof of the Antichain Operator Proposition](../proof-of-the-antichain-operator-proposition/README.md).

- [antichain operator](antichain-operator.md)

Let $n\ge 0$. An $n$-forest is a pair $({\mathfrak U}, \mathfrak{T})$ where ${\mathfrak U}$ is a subset of ${\mathfrak P}$ and $\mathfrak{T}$ is a map assigning to each ${\mathfrak u}\in {\mathfrak U}$ a nonempty set ${\mathfrak T} ({\mathfrak u})\subset {\mathfrak P}$ called tree such that the following properties (30), (31), (32), (33), (34), and (35) hold.

For each ${\mathfrak u}\in {\mathfrak U}$ and each ${\mathfrak p}\in {\mathfrak T}({\mathfrak u})$ we have ${\mathcal{I}}({\mathfrak p}) \ne {\mathcal{I}}({\mathfrak u})$ and

$$
4{\mathfrak p}\lesssim {\mathfrak u}.\qquad\text{(30)}
$$

For each ${\mathfrak u} \in {\mathfrak U}$ and each ${\mathfrak p},{\mathfrak p}''\in {\mathfrak T}({\mathfrak u})$ and ${\mathfrak p}'\in {\mathfrak P}$ we have

$$
{\mathfrak p}, {\mathfrak p}'' \in \mathfrak{T}({\mathfrak u}), {\mathfrak p} \leq {\mathfrak p}' \leq {\mathfrak p}'' \implies {\mathfrak p}' \in \mathfrak{T}({\mathfrak u}).\qquad\text{(31)}
$$

We have

$$
\|\sum_{{\mathfrak u}\in {\mathfrak U}} \mathbf{1}_{{\mathcal{I}}({\mathfrak u})}\|_\infty \leq 2^n\,.\qquad\text{(32)}
$$

We have for every ${\mathfrak u}\in {\mathfrak U}$

$$
\operatorname{\operatorname{dens}}_1({\mathfrak T}({\mathfrak u}))\le 2^{4a + 1-n}\, .\qquad\text{(33)}
$$

We have for ${\mathfrak u}, {\mathfrak u}'\in {\mathfrak U}$ with ${\mathfrak u}\neq {\mathfrak u}'$ and ${\mathfrak p}\in {\mathfrak T}({\mathfrak u}')$ with ${\mathcal{I}}({\mathfrak p})\subset {\mathcal{I}}({\mathfrak u})$ that

$$
d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak u}))>2^{Z(n+1)}\, .\qquad\text{(34)}
$$

We have for every ${\mathfrak u}\in {\mathfrak U}$ and ${\mathfrak p}\in {\mathfrak T}({\mathfrak u})$ that

$$
B({\mathrm{c}}({\mathfrak p}), 8D^{{\mathrm{s}}({\mathfrak p})})\subset {\mathcal{I}}({\mathfrak u}).\qquad\text{(35)}
$$

The following proposition is proved in [Proof of the Forest Operator Proposition](../proof-of-the-forest-operator-proposition/README.md).

- [forest operator](forest-operator.md)

[metric space Carleson](../introduction/metric-space-carleson.md) is formulated at the level of generality for general kernels satisfying the mere Hölder regularity condition [(15)](../introduction/README.md). On the other hand, the cancellative condition [(12)](../introduction/README.md) is a testing condition against more regular, namely Lipschitz functions. To bridge the gap, we follow (zk-polynomial) to observe a variant of [(12)](../introduction/README.md) that we formulate in the following proposition proved in [Proof of the Hölder cancellative condition](../proof-of-the-holder-cancellative-condition/README.md).

Define

$$
\tau:=\frac 1a\, .
$$

Define for any open ball $B$ of radius $R$ in $X$ the $L^\infty$-normalized $\tau$-Hölder norm by

$$
\|\varphi\|_{C^\tau(B)} = \sup_{x \in B} |\varphi(x)| + R^\tau \sup_{x,y \in B, x \neq y} \frac{|\varphi(x) - \varphi(y)|}{\rho(x,y)^\tau}\,.\qquad\text{(38)}
$$

- [Holder van der Corput](holder-van-der-corput.md)

We further formulate a classical Vitali covering result and maximal function estimate that we need throughout several sections. This following proposition will typically be applied to the absolute value of a complex valued function and be proved in [Proof of Vitali covering and Hardy–Littlewood](../proof-of-vitali-covering-and-hardy-littlewood/README.md). By a ball $B$ we mean a set $B(x,r)$ with $x\in X$ and $r>0$ as defined in [(6)](../introduction/README.md). For a finite collection $\mathcal{B}$ of balls in $X$ and $1\le p< \infty$ define the measurable function $M_{\mathcal{B},p}u$ on $X$ by

$$
M_{\mathcal{B},p}u(x):=\left(\sup_{B\in \mathcal{B}} \frac{\mathbf{1}_{B}(x)}{\mu(B)}\int _{B} |u(y)|^p\, d\mu(y)\right)^\frac 1p\, .\qquad\text{(48)}
$$

Define further $M_{\mathcal{B}}:=M_{\mathcal{B},1}$.

- [Hardy–Littlewood](hardy-littlewood.md)

This completes the overview of the proof of [metric space Carleson](../introduction/metric-space-carleson.md).

## Auxiliary lemmas

We close this section by recording some auxiliary lemmas about the objects defined in Proof of Metric Space Carleson, overview, which will be used in multiple sections to follow.

First, we record an estimate for the metrical entropy numbers of balls in the space ${\Theta}$ equipped with any of the metrics $d_B$, following from the doubling property [(11)](../introduction/README.md).

- [ball metric entropy](ball-metric-entropy.md)

The next lemma concerns monotonicity of the metrics $d_{B(c(I), \frac 14 D^{s(I)})}$ with respect to inclusion of cubes $I$ in a grid.

- [monotone cube metrics](monotone-cube-metrics.md)

We also record the following basic estimates for the kernels $K_s$.

- [kernel summand](kernel-summand.md)
