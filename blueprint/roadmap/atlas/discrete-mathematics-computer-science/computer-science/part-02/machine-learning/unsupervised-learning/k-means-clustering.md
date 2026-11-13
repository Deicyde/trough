---
declaration: section
origin: cited
lean: Cslib.MachineLearning.KMeans.centroid, Cslib.MachineLearning.KMeans.sum_sq_eq, Cslib.MachineLearning.KMeans.Nearest, Cslib.MachineLearning.KMeans.exists_nearest, Cslib.MachineLearning.KMeans.cost, Cslib.MachineLearning.KMeans.cost_eq_sum_clusters, Cslib.MachineLearning.KMeans.centers, Cslib.MachineLearning.KMeans.cost_centers_le
statement: formalized
proof: formalized
---

# k-means clustering

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html).

## Centroid

Let $x_i$ be points in a real inner product space and $s$ a finite set of
indices. The centroid of the points indexed by $s$ is $\frac{1}{|s|} \sum_{i \in s} x_i$; when $s$
is empty it is the zero vector.

Formalized by `Cslib.MachineLearning.KMeans.centroid`, a definition declared in [CSLibExt/MachineLearning/KMeans.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/KMeans.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#centroid).

## Sum of squared distances about the centroid

Let $x_i$ ($i \in \iota$) be points in a
real inner product space $E$, let $s$ be a finite set of indices, and let $\mu$ be the centroid of
the points $x_i$ with $i \in s$. Then for every point $c \in E$,

$$
\sum_{i \in s} \|x_i - c\|^2 = \sum_{i \in s} \|x_i - \mu\|^2 + |s| \, \|\mu - c\|^2.
$$

Consequently the centroid minimizes the sum of squared distances to the points $x_i$, $i \in s$.

Formalized by `Cslib.MachineLearning.KMeans.sum_sq_eq`, a theorem declared in [CSLibExt/MachineLearning/KMeans.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/KMeans.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#sum-sq-eq).

## Nearest-center assignment

Given points $x_i$ ($i \in \iota$) in a normed additive
commutative group $E$ and centers $c_0, \dots, c_{k-1} \in E$, an assignment
$a : \iota \to \{0, \dots, k-1\}$ assigns every point to a nearest center when
$\|x_i - c_{a(i)}\| \le \|x_i - c_j\|$ for every index $i \in \iota$ and every $j < k$.

Formalized by `Cslib.MachineLearning.KMeans.Nearest`, a definition declared in [CSLibExt/MachineLearning/KMeans.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/KMeans.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#nearest).

## Nearest-center assignments exist

For any points $x_i$ in a normed additive commutative
group and any centers $c_0, \dots, c_{k-1}$ with $k \ge 1$, there is an assignment that sends
every point to a nearest center.

Formalized by `Cslib.MachineLearning.KMeans.exists_nearest`, a theorem declared in [CSLibExt/MachineLearning/KMeans.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/KMeans.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#exists-nearest).

## The k-means cost

For points $x_i$ ($i \in \iota$, a finite type) in a normed additive
commutative group, an assignment $a$ of each point $i$ to a cluster $a(i) \in \{0, \dots, k-1\}$
and centers $c_0, \dots, c_{k-1}$, the $k$-means cost is
$\sum_{i \in \iota} \lVert x_i - c_{a(i)} \rVert^2$, the sum of the squared distances from the
points to their assigned centers.

Formalized by `Cslib.MachineLearning.KMeans.cost`, a definition declared in [CSLibExt/MachineLearning/KMeans.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/KMeans.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#cost).

## The cost as a sum over clusters

For points $x_i$ ($i \in \iota$, a finite type) in a
normed additive commutative group, an assignment $a$ of each point $i$ to a cluster
$a(i) \in \{0, \dots, k-1\}$ and centers $c_0, \dots, c_{k-1}$, the $k$-means cost equals
$\sum_{j} \sum_{i : a(i) = j} \lVert x_i - c_j \rVert^2$: for each cluster $j$, add up the squared
distances from the points assigned to $j$ to its center $c_j$.

Formalized by `Cslib.MachineLearning.KMeans.cost_eq_sum_clusters`, a theorem declared in [CSLibExt/MachineLearning/KMeans.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/KMeans.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#cost-eq-sum-clusters).

## The centroid update step

Let $x_i$ ($i \in \iota$, a finite type) be points in a real
inner product space and let $a$ assign each point $i$ to a cluster $a(i) \in \{0, \dots, k-1\}$.
The updated centers send each cluster $j$ to the centroid of the points $x_i$ with $a(i) = j$.
A cluster with no points gets the center $0$, which does not affect the $k$-means cost of $a$.

Formalized by `Cslib.MachineLearning.KMeans.centers`, a definition declared in [CSLibExt/MachineLearning/KMeans.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/KMeans.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#centers).

## The update step never increases the cost

For a fixed assignment, the centroids are the
best centers.

Formalized by `Cslib.MachineLearning.KMeans.cost_centers_le`, a theorem declared in [CSLibExt/MachineLearning/KMeans.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/KMeans.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#cost-centers-le).

## The assignment step never increases the cost

For fixed centers, nearest-center
assignment is optimal.

Formalized by `Cslib.MachineLearning.KMeans.cost_nearest_le`, a theorem declared in [CSLibExt/MachineLearning/KMeans.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/KMeans.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#cost-nearest-le).

## One round of Lloyd's algorithm never increases the cost

Recompute the centers, then
reassign every point to a nearest new center.

Formalized by `Cslib.MachineLearning.KMeans.cost_lloyd_le`, a theorem declared in [CSLibExt/MachineLearning/KMeans.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/KMeans.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#cost-lloyd-le).

## Run of Lloyd's algorithm

Let $x_i$ ($i \in \iota$, a finite index set) be points in a
real inner product space $E$. Sequences of assignments $a_t : \iota \to \{0, \dots, k-1\}$ and of
centers $c_t : \{0, \dots, k-1\} \to E$, indexed by $t \in \mathbb{N}$, form a run of Lloyd's
algorithm when for every $t$: for each $j < k$ the center $c_{t+1}(j)$ is the centroid of the
cluster $\{i : a_t(i) = j\}$ (the zero vector if this cluster is empty), and $a_{t+1}$ assigns
every point to a nearest center of $c_{t+1}$. The initial assignment $a_0$ and centers $c_0$ are
arbitrary.

Formalized by `Cslib.MachineLearning.KMeans.IsRun`, a definition declared in [CSLibExt/MachineLearning/KMeans.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/KMeans.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#is-run).

## The cost never increases along a run of Lloyd's algorithm

**The cost never increases along a run of Lloyd's algorithm.**

Formalized by `Cslib.MachineLearning.KMeans.IsRun.antitone`, a theorem declared in [CSLibExt/MachineLearning/KMeans.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/KMeans.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#antitone).

## Runs of Lloyd's algorithm exist

Let $x_i$ ($i \in \iota$, a finite type) be points in a
real inner product space and let $k \ge 1$. Every starting assignment $a_0$ of the points to
clusters $0, \dots, k-1$ and every choice of starting centers $c_0$ extend to a run of Lloyd's
algorithm: there are assignments $a_t$ and centers $c_t$ for $t \in \mathbb{N}$, equal to $a_0$
and $c_0$ at $t = 0$, that form a run.

Formalized by `Cslib.MachineLearning.KMeans.exists_run`, a theorem declared in [CSLibExt/MachineLearning/KMeans.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/KMeans.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#exists-run).

## Responsibilities with a common variance

Given weights $w_1, \dots, w_K \in \mathbb{R}$,
means $\mu_1, \dots, \mu_K \in \mathbb{R}^d$ and a real $v$, the common-variance responsibility
of component $k$ at a point $x \in \mathbb{R}^d$ is

$$
r_v(x, k) = \frac{w_k \, \mathcal{N}(x \mid \mu_k, vI)}
{\sum_i w_i \, \mathcal{N}(x \mid \mu_i, vI)},
$$

where, for $v > 0$, $\mathcal{N}(x \mid \mu, vI)$ is the isotropic Gaussian density with mean
$\mu$ and covariance $vI$, and for $v \le 0$ it is $1$ if $d = 0$ and $0$ if $d \ge 1$. A quotient
with denominator $0$ is $0$.

Formalized by `Cslib.MachineLearning.LatentVariable.HardEM.softAssign`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/HardEM.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/HardEM.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#soft-assign).

## The Gaussian-mixture responsibilities are the common-variance responsibilities

Let
$\theta$ be valid parameters of an isotropic Gaussian mixture with $K$ components on
$\mathbb{R}^d$, with weights $w_k$, means $\mu_k$ and variances all equal to a real number $v$.
Then for every point $x \in \mathbb{R}^d$ and every component $k$, the responsibility of $k$ at
$x$ under $\theta$ equals the common-variance responsibility $r_v(x, k)$ for the weights $w$ and
means $\mu$.

Formalized by `Cslib.MachineLearning.LatentVariable.HardEM.resp_eq_softAssign`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/HardEM.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/HardEM.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#resp-eq-soft-assign).

## Ratio of isotropic Gaussian densities with a common variance

For all points
$\mu, \nu, x \in \mathbb{R}^d$ and every real $v > 0$, writing $\mathcal{N}(x \mid \mu, vI)$ for
the isotropic Gaussian density with mean $\mu$ and covariance $vI$,

$$
\frac{\mathcal{N}(x \mid \mu, vI)}{\mathcal{N}(x \mid \nu, vI)}
= \exp\left(\frac{\|x - \nu\|^2 - \|x - \mu\|^2}{2v}\right).
$$

Formalized by `Cslib.MachineLearning.LatentVariable.HardEM.isoGaussPDF_div`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/HardEM.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/HardEM.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#iso-gauss-pdf-div).

## Exponential decay as the variance tends to zero

For every real $c < 0$,
$\exp(c / (2v)) \to 0$ as $v \to 0^+$.

Formalized by `Cslib.MachineLearning.LatentVariable.HardEM.tendsto_exp_div_nhdsGT_zero`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/HardEM.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/HardEM.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#tendsto-exp-div-nhds-gt-zero).

## Common-variance responsibilities relative to a fixed component

For weights
$w_1, \dots, w_K \in \mathbb{R}$, means $\mu_1, \dots, \mu_K \in \mathbb{R}^d$, a real $v > 0$,
a point $x \in \mathbb{R}^d$ and components $j$ and $k$, the common-variance responsibility
$r_v(x, k)$ of component $k$ at $x$ for these weights and means satisfies

$$
r_v(x, k) = \frac{w_k \exp\bigl((\|x - \mu_j\|^2 - \|x - \mu_k\|^2) / (2v)\bigr)}
{\sum_i w_i \exp\bigl((\|x - \mu_j\|^2 - \|x - \mu_i\|^2) / (2v)\bigr)}.
$$

Formalized by `Cslib.MachineLearning.LatentVariable.HardEM.softAssign_eq`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/HardEM.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/HardEM.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#soft-assign-eq).

## Responsibilities in the zero-variance limit

Let $w_1, \dots, w_K$ be positive weights,
$\mu_1, \dots, \mu_K \in \mathbb{R}^d$ means and $x \in \mathbb{R}^d$ a point, and suppose that
$\mu_j$ is the unique nearest mean to $x$: $\|x - \mu_j\| < \|x - \mu_k\|$ for every $k \ne j$.
Then for every component $k$, the common-variance responsibility $r_v(x, k)$ of $k$ at $x$ for
these weights and means tends to $1$ if $k = j$ and to $0$ otherwise as $v \to 0^+$.

## Sources

- Bishop, *Pattern Recognition and Machine Learning*, Section 9.3.2.

Formalized by `Cslib.MachineLearning.LatentVariable.HardEM.tendsto_softAssign`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/HardEM.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/HardEM.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#tendsto-soft-assign).

## The k-means assignment step is the zero-variance limit of the E-step

Let
$x_1, \dots, x_N$ be points of $\mathbb{R}^d$, let $\mu_1, \dots, \mu_K \in \mathbb{R}^d$ be means
with positive weights $w_1, \dots, w_K$, and let $a$ assign to each $n$ a component $a(n)$ such
that $\|x_n - \mu_{a(n)}\| < \|x_n - \mu_k\|$ for every $k \ne a(n)$. Then $a$ is a nearest-center
assignment, that is, $\|x_n - \mu_{a(n)}\| \le \|x_n - \mu_k\|$ for all $n$ and $k$, and for all
$n$ and $k$ the common-variance responsibility $r_v(x_n, k)$ of component $k$ at $x_n$ for these
weights and means tends to $1$ if $k = a(n)$ and to $0$ otherwise as $v \to 0^+$.

Formalized by `Cslib.MachineLearning.LatentVariable.HardEM.nearest_and_tendsto_softAssign`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/HardEM.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/HardEM.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#nearest-and-tendsto-soft-assign).

## Common-variance M-step mean

Given weights $w_1, \dots, w_K \in \mathbb{R}$, means
$\mu_1, \dots, \mu_K \in \mathbb{R}^d$, a real $v$ and data $x_1, \dots, x_N \in \mathbb{R}^d$,
the common-variance M-step mean of component $k$ is

$$
\Bigl(\sum_n r_v(x_n, k)\Bigr)^{-1} \sum_n r_v(x_n, k) \, x_n,
$$

where $r_v(x, k)$ is the common-variance responsibility of component $k$ at $x$ for these
weights and means, and $0^{-1} = 0$.

Formalized by `Cslib.MachineLearning.LatentVariable.HardEM.softMean`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/HardEM.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/HardEM.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#soft-mean).

## The Gaussian-mixture M-step mean is the common-variance M-step mean

Let $\theta$ be valid
parameters of an isotropic Gaussian mixture with $K$ components on $\mathbb{R}^d$, with weights
$w_k$, means $\mu_k$ and variances all equal to a real number $v$. Then for data
$x_1, \dots, x_N \in \mathbb{R}^d$ and every component $k$, the M-step mean of component $k$ under
$\theta$ equals the common-variance M-step mean of component $k$ for the weights $w$, means $\mu$,
variance $v$ and data $x_1, \dots, x_N$.

Formalized by `Cslib.MachineLearning.LatentVariable.HardEM.newMean_eq_softMean`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/HardEM.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/HardEM.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#new-mean-eq-soft-mean).

## The M-step in the zero-variance limit

Let $x_1, \dots, x_N \in \mathbb{R}^d$ be data, let
$\mu_1, \dots, \mu_K \in \mathbb{R}^d$ be means with positive weights $w_1, \dots, w_K$, and let
$a$ assign to each $n$ a component $a(n)$ with $\|x_n - \mu_{a(n)}\| < \|x_n - \mu_k\|$ for
every $k \ne a(n)$. Then for every component $k$ such that $a(n) = k$ for some $n$, the
common-variance M-step mean of component $k$ for these weights, means and data tends, as
$v \to 0^+$, to the k-means centroid of cluster $k$ under $a$, the mean of the points $x_n$ with
$a(n) = k$.

Formalized by `Cslib.MachineLearning.LatentVariable.HardEM.tendsto_softMean`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/HardEM.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/HardEM.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html#tendsto-soft-mean).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: k-means clustering](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/machine-learning/unsupervised-learning/k-means-clustering)
