---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.EucPlane, MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.dimMeasure, MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.IsMeasurablePartition, MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.partitionEntropy, MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.iteratedJoin, MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.entropyW, MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.kolmogorovSinaiEntropy, MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.lyapunovUpperAt
statement: formalized
---

# Entropy, dimension and Lyapunov exponents

13 results, 10 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/entropy-dimension-and-lyapunov-exponents/index.html).

## Euclidean plane

The Euclidean plane $\mathbb{R}^2$ with its Euclidean inner product and
norm. The theorems of this module model a compact surface by a compact invariant subset of
this plane.

Formalized by `MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.EucPlane`, an abbreviation declared in [WantedExt/Dynamics/LaiSangYoungWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/LaiSangYoungWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/entropy-dimension-and-lyapunov-exponents/index.html#euc-plane).

## Hausdorff dimension of a measure

For a measure $\mu$ on an extended metric space $M$
equipped with a σ-algebra, the Hausdorff dimension of $\mu$ is the infimum, in $[0, \infty]$, of
the Hausdorff dimensions of the measurable sets $s \subseteq M$ with $\mu(M \setminus s) = 0$.

Formalized by `MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.dimMeasure`, a definition declared in [WantedExt/Dynamics/LaiSangYoungWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/LaiSangYoungWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/entropy-dimension-and-lyapunov-exponents/index.html#dim-measure).

## Measurable partition modulo null sets

Let $\mu$ be a measure on a measurable space $M$.
A finite family $P$ of subsets of $M$ is a measurable partition of $M$ modulo $\mu$-null sets
when every member of $P$ is measurable, the complement of the union of the members of $P$ has
$\mu$-measure $0$, and any two distinct members $A \ne B$ of $P$ satisfy $\mu(A \cap B) = 0$.

Formalized by `MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.IsMeasurablePartition`, a structure declared in [WantedExt/Dynamics/LaiSangYoungWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/LaiSangYoungWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/entropy-dimension-and-lyapunov-exponents/index.html#is-measurable-partition).

## Shannon entropy of a finite family of sets

For a measure $\mu$ on a measurable space $M$
and a finite collection $P$ of subsets of $M$, the entropy of $P$ is
$H_\mu(P) = \sum_{A \in P} -\mu(A) \log \mu(A)$, where $\log$ is the natural logarithm, with the
convention $0 \log 0 = 0$. Here $\mu(A)$ is taken as a real number, so a set of infinite measure
contributes $0$.

It is applied to finite measurable partitions $P$.

Formalized by `MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.partitionEntropy`, a definition declared in [WantedExt/Dynamics/LaiSangYoungWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/LaiSangYoungWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/entropy-dimension-and-lyapunov-exponents/index.html#partition-entropy).

## Iterated join of a partition

For a map $T : M \to M$, a finite family $P$ of subsets of
$M$ and $n \in \mathbb{N}$, the iterated join $\bigvee_{k=0}^{n-1} T^{-k} P$ is the finite family
of all sets $\bigcap_{k=0}^{n-1} T^{-k}(A_k)$ with $A_0, \dots, A_{n-1} \in P$, where $T^{-k}(A)$
is the preimage of $A$ under the $k$-th iterate $T^k$. For $n = 0$ it is $\{M\}$.

Formalized by `MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.iteratedJoin`, a definition declared in [WantedExt/Dynamics/LaiSangYoungWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/LaiSangYoungWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/entropy-dimension-and-lyapunov-exponents/index.html#iterated-join).

## Entropy of a map relative to a partition

Let $\mu$ be a measure on a measurable space
$M$, let $T : M \to M$ be a map and let $P$ be a finite family of subsets of $M$. The entropy of
$T$ relative to $P$ is

$$h_\mu(T, P) = \limsup_{n \to \infty} \frac{1}{n} H_\mu\Big(\bigvee_{k=0}^{n-1} T^{-k} P\Big),$$

where $\bigvee_{k=0}^{n-1} T^{-k} P$ is the iterated join of $P$ under $T$; the Shannon entropy
of a finite family $Q$ of sets is $H_\mu(Q) = \sum_{A \in Q} -\mu(A) \log \mu(A)$, with
$0 \log 0 = 0$ and with $\mu(A)$ replaced by $0$ when $\mu(A) = \infty$; and the limit superior
is taken to be $0$ when it is $+\infty$ or $-\infty$.

Formalized by `MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.entropyW`, a definition declared in [WantedExt/Dynamics/LaiSangYoungWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/LaiSangYoungWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/entropy-dimension-and-lyapunov-exponents/index.html#entropy-w).

## Kolmogorov–Sinai entropy

Let $\mu$ be a measure on a measurable space $M$ and let
$T : M \to M$ be a map. The Kolmogorov–Sinai entropy $h_\mu(T)$ is the supremum of the
entropies $h_\mu(T, P)$ of $T$ relative to $P$ over all finite measurable partitions $P$ of $M$
modulo $\mu$-null sets, taken to be $0$ when these entropies are not bounded above.

Formalized by `MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.kolmogorovSinaiEntropy`, a definition declared in [WantedExt/Dynamics/LaiSangYoungWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/LaiSangYoungWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/entropy-dimension-and-lyapunov-exponents/index.html#kolmogorov-sinai-entropy).

## Upper Lyapunov exponent

For a map $T : \mathbb{R}^2 \to \mathbb{R}^2$ of the Euclidean
plane and a point $x \in \mathbb{R}^2$, the upper Lyapunov exponent of $T$ at $x$ is

$$\overline{\lambda}(T, x) = \limsup_{n \to \infty} \frac{1}{n} \log \|D(T^n)_x\|,$$

where $D(T^n)_x$ is the derivative at $x$ of the $n$-th iterate $T^n$, taken to be $0$ when
$T^n$ is not differentiable at $x$; $\|\cdot\|$ is the operator norm; $\log 0 = 0$; and the
limit superior is taken to be $0$ when it is $+\infty$ or $-\infty$.

Formalized by `MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.lyapunovUpperAt`, a definition declared in [WantedExt/Dynamics/LaiSangYoungWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/LaiSangYoungWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/entropy-dimension-and-lyapunov-exponents/index.html#lyapunov-upper-at).

## Lower Lyapunov exponent

For a map $T : \mathbb{R}^2 \to \mathbb{R}^2$ of the Euclidean
plane and a point $x \in \mathbb{R}^2$, the lower Lyapunov exponent of $T$ at $x$ is

$$\underline{\lambda}(T, x) = -\limsup_{n \to \infty} \frac{1}{n} \log \|(D(T^n)_x)^{-1}\|,$$

where $D(T^n)_x$ is the derivative at $x$ of the $n$-th iterate $T^n$, taken to be $0$ when
$T^n$ is not differentiable at $x$; the inverse $(D(T^n)_x)^{-1}$ is taken to be $0$ when
$D(T^n)_x$ is not invertible; $\|\cdot\|$ is the operator norm; $\log 0 = 0$; and the limit
superior is taken to be $0$ when it is $+\infty$ or $-\infty$.

Formalized by `MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.lyapunovLowerAt`, a definition declared in [WantedExt/Dynamics/LaiSangYoungWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/LaiSangYoungWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/entropy-dimension-and-lyapunov-exponents/index.html#lyapunov-lower-at).

## Harmonic mean of Lyapunov exponents

For real numbers $\lambda_1$ and $\lambda_2$, this
is the harmonic mean $\frac{2 \lambda_1 (-\lambda_2)}{\lambda_1 - \lambda_2}$ of $\lambda_1$ and
$-\lambda_2$, taken to be $0$ when $\lambda_1 = \lambda_2$.

Formalized by `MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.harmonicMeanLyapunov`, a definition declared in [WantedExt/Dynamics/LaiSangYoungWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/LaiSangYoungWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/entropy-dimension-and-lyapunov-exponents/index.html#harmonic-mean-lyapunov).

## Young's entropy–dimension–Lyapunov formula (planar case)

Let $T$ be a $C^2$
diffeomorphism of the Euclidean plane $\mathbb{R}^2$: $T$ has a two-sided inverse $T^{-1}$ and
both $T$ and $T^{-1}$ are $C^2$. Let $K \subseteq \mathbb{R}^2$ be a compact set with
$T(K) = K$, and let $\mu$ be a Borel probability measure on $\mathbb{R}^2$ with
$\mu(\mathbb{R}^2 \setminus K) = 0$ that is $T$-invariant and ergodic for $T$. Let $\lambda_1$
and $\lambda_2$ be the $\mu$-integrals of the upper and the lower Lyapunov exponent of $T$. Then
the Kolmogorov–Sinai entropy of $T$ with respect to $\mu$ is

$$h_\mu(T) = \frac{\dim(\mu) \cdot H}{2},$$

where $\dim(\mu)$ is the Hausdorff dimension of $\mu$ and
$H = \frac{2 \lambda_1 (-\lambda_2)}{\lambda_1 - \lambda_2}$ is the harmonic mean of $\lambda_1$
and $-\lambda_2$, taken to be $0$ when $\lambda_1 = \lambda_2$.

## Sources

- L.-S. Young, *Dimension, entropy and Lyapunov exponents*, Ergodic Theory Dynam. Systems 2 (1982), 109–124. Knill, *Some fundamental theorems in mathematics*, §103. Problem `entropy_dimension_lyapunov` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.entropy_dimension_lyapunov` is written with `theorem_wanted` in [WantedExt/Dynamics/LaiSangYoungWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/LaiSangYoungWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/entropy-dimension-and-lyapunov-exponents/index.html#entropy-dimension-lyapunov).

## Pesin entropy formula (planar case)

Let $T$ be a $C^2$ diffeomorphism of the Euclidean
plane $\mathbb{R}^2$, that is, a $C^2$ map with a $C^2$ two-sided inverse. Let
$K \subseteq \mathbb{R}^2$ be a compact set with $T(K) = K$, and let $\mu$ be an ergodic
$T$-invariant Borel probability measure on $\mathbb{R}^2$ with
$\mu(\mathbb{R}^2 \setminus K) = 0$. Write $h_\mu(T)$ for the Kolmogorov–Sinai entropy of $T$
with respect to $\mu$, and $\lambda_1(x)$ and $\lambda_2(x)$ for the upper and lower Lyapunov
exponents of $T$ at $x$. Suppose that the Hausdorff dimension of $\mu$ equals $2$ and that
$\int \lambda_1 \, d\mu = -\int \lambda_2 \, d\mu$. Then $h_\mu(T) = \int \lambda_1 \, d\mu$.

## Sources

- Ya. B. Pesin, *Characteristic Lyapunov exponents and smooth ergodic theory*, Russian Math. Surveys 32 (1977). Knill, *Some fundamental theorems in mathematics*, §103. Problem `pesin_formula` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.pesin_formula` is written with `theorem_wanted` in [WantedExt/Dynamics/LaiSangYoungWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/LaiSangYoungWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/entropy-dimension-and-lyapunov-exponents/index.html#pesin-formula).

## Margulis–Ruelle inequality (planar case)

Let $T$ be a $C^2$ diffeomorphism of the
Euclidean plane $\mathbb{R}^2$, that is, a $C^2$ map with a $C^2$ two-sided inverse. Let
$K \subseteq \mathbb{R}^2$ be a compact set with $T(K) = K$, and let $\mu$ be an ergodic
$T$-invariant Borel probability measure on $\mathbb{R}^2$ with
$\mu(\mathbb{R}^2 \setminus K) = 0$. Write $h_\mu(T)$ for the Kolmogorov–Sinai entropy of $T$
with respect to $\mu$, and $\lambda_1(x)$ and $\lambda_2(x)$ for the upper and lower Lyapunov
exponents of $T$ at $x$. Then

$$h_\mu(T) \le \max(0, \int \lambda_1 \, d\mu) + \max(0, \int \lambda_2 \, d\mu).$$

## Sources

- D. Ruelle, *An inequality for the entropy of differentiable maps*, Bol. Soc. Brasil. Mat. 9 (1978); G. A. Margulis (1968, unpublished). Knill, *Some fundamental theorems in mathematics*, §103. Problem `margulis_ruelle` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.LaiSangYoungWanted.Dynamics.margulis_ruelle` is written with `theorem_wanted` in [WantedExt/Dynamics/LaiSangYoungWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/LaiSangYoungWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/entropy-dimension-and-lyapunov-exponents/index.html#margulis-ruelle).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Entropy, dimension and Lyapunov exponents](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/entropy-dimension-and-lyapunov-exponents/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/smooth-dynamics/entropy-dimension-and-lyapunov-exponents)
