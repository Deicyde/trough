---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Integration.Partition, MathlibExt.Analysis.Integration.TaggedPartition, MathlibExt.Analysis.Integration.Partition.mesh, MathlibExt.Analysis.Integration.Partition.pointSet, MathlibExt.Analysis.Integration.Partition.IsRefinement, MathlibExt.Analysis.Integration.riemannSum, MathlibExt.Analysis.Integration.Partition.a_le_b, MathlibExt.Analysis.Integration.Partition.n_pos_of_lt
statement: formalized
proof: formalized
---

# Riemann integral

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html).

## Partition of an interval

For real numbers $a$ and $b$, a partition of the closed interval
$[a, b]$ consists of a natural number $n$, the number of subintervals, together with $n + 1$
points forming a strictly increasing sequence $a = x_0 < x_1 < \dots < x_n = b$.

Formalized by `MathlibExt.Analysis.Integration.Partition`, a structure declared in [MathlibExt/Analysis/Integration/RiemannPartition.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannPartition.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#partition).

## Tagged partition

A tagged partition of $[a, b]$ is a partition
$a = x_0 < x_1 < \cdots < x_n = b$ of $[a, b]$ together with a choice of a tag
$\xi_k \in [x_{k-1}, x_k]$ in each subinterval, for $k = 1, \dots, n$.

Formalized by `MathlibExt.Analysis.Integration.TaggedPartition`, a structure declared in [MathlibExt/Analysis/Integration/RiemannPartition.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannPartition.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#tagged-partition).

## Mesh of a partition

The mesh (also called the norm) of a partition
$a = x_0 < x_1 < \dots < x_n = b$ of $[a, b]$ is the maximum subinterval length
$\max_{1 \le k \le n} (x_k - x_{k-1})$ when $n \ge 1$, and $0$ when $n = 0$.

Formalized by `MathlibExt.Analysis.Integration.Partition.mesh`, a definition declared in [MathlibExt/Analysis/Integration/RiemannPartition.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannPartition.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#mesh).

## Points of a partition

The point set of a partition $a = x_0 < x_1 < \dots < x_n = b$ of
$[a, b]$ is the set of its points $x_0, x_1, \dots, x_n$.

Formalized by `MathlibExt.Analysis.Integration.Partition.pointSet`, a definition declared in [MathlibExt/Analysis/Integration/RiemannPartition.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannPartition.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#point-set).

## Refinement of a partition

For partitions $P$ and $Q$ of $[a, b]$, $Q$ is a refinement of
$P$ when every point of $P$ is a point of $Q$, that is, when the point set of $P$ is contained in
the point set of $Q$.

Formalized by `MathlibExt.Analysis.Integration.Partition.IsRefinement`, a definition declared in [MathlibExt/Analysis/Integration/RiemannPartition.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannPartition.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#is-refinement).

## Riemann sum

Let $f : \mathbb{R} \to \mathbb{R}$ and let $T$ be a tagged partition of
$[a, b]$, with points $a = x_0 < x_1 < \cdots < x_n = b$ and tags $\xi_k \in [x_{k-1}, x_k]$
for $k = 1, \dots, n$. The Riemann sum of $f$ with respect to $T$ is
$S_f(x, \xi) = \sum_{k=1}^{n} f(\xi_k)\,(x_k - x_{k-1})$ (an empty sum, equal to $0$, when
$n = 0$).

Formalized by `MathlibExt.Analysis.Integration.riemannSum`, a definition declared in [MathlibExt/Analysis/Integration/RiemannPartition.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannPartition.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#riemann-sum).

## Endpoints of a partition are ordered

If $a, b \in \mathbb{R}$ and the interval $[a, b]$
has a partition, then $a \le b$.

Formalized by `MathlibExt.Analysis.Integration.Partition.a_le_b`, a lemma declared in [MathlibExt/Analysis/Integration/RiemannPartition.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannPartition.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#a-le-b).

## A partition of a nondegenerate interval has a subinterval

If $a < b$, then every
partition $a = x_0 < x_1 < \dots < x_n = b$ of $[a, b]$ has at least one subinterval, that is,
$n \ge 1$.

Formalized by `MathlibExt.Analysis.Integration.Partition.n_pos_of_lt`, a lemma declared in [MathlibExt/Analysis/Integration/RiemannPartition.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannPartition.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#n-pos-of-lt).

## The mesh is positive on a nondegenerate interval

If $a < b$, then every partition of
$[a, b]$ has strictly positive mesh.

Formalized by `MathlibExt.Analysis.Integration.Partition.mesh_pos_of_lt`, a lemma declared in [MathlibExt/Analysis/Integration/RiemannPartition.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannPartition.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#mesh-pos-of-lt).

## Riemann sum over a trivial partition

For every function $f : \mathbb{R} \to \mathbb{R}$
and every tagged partition of $[a, b]$ with no subintervals, the Riemann sum of $f$ is $0$, since
it is an empty sum.

Formalized by `MathlibExt.Analysis.Integration.riemannSum_eq_zero_of_n_eq_zero`, a lemma declared in [MathlibExt/Analysis/Integration/RiemannPartition.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannPartition.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#riemann-sum-eq-zero-of-n-eq-zero).

## Subintervals of a partition have nonnegative length

If
$a = x_0 < x_1 < \cdots < x_n = b$ is a partition of $[a, b]$, then $x_{i+1} - x_i \ge 0$ for
every $i$ with $0 \le i < n$.

Formalized by `MathlibExt.Analysis.Integration.Partition.succ_sub_castSucc_nonneg`, a lemma declared in [MathlibExt/Analysis/Integration/RiemannPartition.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannPartition.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#succ-sub-cast-succ-nonneg).

## Subinterval lengths are at most the mesh

Let $a = x_0 < x_1 < \dots < x_n = b$ be a
partition of $[a, b]$. Then for every $i$ with $0 \le i < n$, the subinterval length
$x_{i+1} - x_i$ is at most the mesh of the partition.

Formalized by `MathlibExt.Analysis.Integration.Partition.le_mesh`, a lemma declared in [MathlibExt/Analysis/Integration/RiemannPartition.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannPartition.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#le-mesh).

## Subinterval lengths of a partition telescope

If $a = x_0 < x_1 < \cdots < x_n = b$ is
a partition of $[a, b]$, then the lengths of its subintervals sum to the length of the interval:
$\sum_{i=0}^{n-1} (x_{i+1} - x_i) = b - a$.

Formalized by `MathlibExt.Analysis.Integration.Partition.sum_sub_eq`, a lemma declared in [MathlibExt/Analysis/Integration/RiemannPartition.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannPartition.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#sum-sub-eq).

## Tags of a tagged partition lie in the interval

Every tag $\xi_k$ of a tagged partition
of $[a, b]$ lies in $[a, b]$.

Formalized by `MathlibExt.Analysis.Integration.TaggedPartition.tag_mem_Icc`, a lemma declared in [MathlibExt/Analysis/Integration/RiemannPartition.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannPartition.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#tag-mem-icc).

## Riemann sum of a constant function

For every real constant $c$ and every tagged partition
of $[a, b]$, the Riemann sum of the constant function $x \mapsto c$ equals $c(b - a)$.

Formalized by `MathlibExt.Analysis.Integration.riemannSum_const`, a lemma declared in [MathlibExt/Analysis/Integration/RiemannPartition.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannPartition.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#riemann-sum-const).

## Telescoping over the fibers of an assignment

Let $y_0, \dots, y_N$ be real numbers,
let $\varphi : \{0, \dots, m\} \to \{0, \dots, N\}$ be strictly increasing, and let
$\sigma : \{0, \dots, N-1\} \to \{0, \dots, m-1\}$ satisfy
$\varphi(\sigma(j)) \le j < \varphi(\sigma(j) + 1)$ for every $j < N$. Then for every $k < m$,

$$\sum_{j < N,\ \sigma(j) = k} (y_{j+1} - y_j) = y_{\varphi(k+1)} - y_{\varphi(k)}.$$

Formalized by `MathlibExt.Analysis.Integration.telescope_sum_of_embedding`, a lemma declared in [MathlibExt/Analysis/Integration/RiemannSumRefinement.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannSumRefinement.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#telescope-sum-of-embedding).

## Tagged-refinement data

Let $T$ and $T'$ be tagged partitions of $[a, b]$ with points
$a = x_0 < \dots < x_n = b$ and $a = x'_0 < \dots < x'_{n'} = b$ respectively. Tagged-refinement
data from $T$ to $T'$ consist of a map $\sigma$ assigning to each index $j < n'$ an index
$\sigma(j) < n$ such that $x_{\sigma(j)} \le x'_j$ and $x'_{j+1} \le x_{\sigma(j)+1}$ for every
$j < n'$ (so the $j$-th subinterval of $T'$ lies in the $\sigma(j)$-th subinterval of $T$), and
such that for every $k < n$ the lengths assigned to $k$ add up to its length:
$\sum_{j < n',\ \sigma(j) = k} (x'_{j+1} - x'_j) = x_{k+1} - x_k$. The tags of $T$ and $T'$
play no role.

Such data exist whenever every point of $T$ is a point of $T'$.

Formalized by `MathlibExt.Analysis.Integration.TaggedPartition.IsTaggedRefinement`, a structure declared in [MathlibExt/Analysis/Integration/RiemannSumRefinement.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannSumRefinement.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#is-tagged-refinement).

## Refinements carry tagged-refinement data

Let $T$ and $T'$ be tagged partitions of
$[a, b]$ such that every point of $T$ is a point of $T'$. Then tagged-refinement data from $T$
to $T'$ exist: an assignment of each subinterval of $T'$ to a subinterval of $T$ that contains
it, such that for each subinterval of $T$ the lengths of the subintervals of $T'$ assigned to it
add up to its length.

Formalized by `MathlibExt.Analysis.Integration.TaggedPartition.nonempty_isTaggedRefinement_of_isRefinement`, a theorem declared in [MathlibExt/Analysis/Integration/RiemannSumRefinement.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannSumRefinement.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#nonempty-is-tagged-refinement-of-is-refi).

## Riemann sum regrouped over a refinement

Let $f : \mathbb{R} \to \mathbb{R}$, let $T$ be
a tagged partition of $[a, b]$ with points $x_0 < \dots < x_n$ and tags
$\xi_0, \dots, \xi_{n-1}$, and let $T'$ be a tagged partition of $[a, b]$ with points
$x'_0 < \dots < x'_{n'}$, together with tagged-refinement data from $T$ to $T'$ assigning to
each $j < n'$ an index $\sigma(j) < n$. Then the Riemann sum $S_f(T)$ of $f$ over $T$ satisfies

$$S_f(T) = \sum_{j=0}^{n'-1} f(\xi_{\sigma(j)}) \, (x'_{j+1} - x'_j).$$

Formalized by `MathlibExt.Analysis.Integration.riemannSum_eq_fiber`, a lemma declared in [MathlibExt/Analysis/Integration/RiemannSumRefinement.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannSumRefinement.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#riemann-sum-eq-fiber).

## Riemann sums under refinement, given refinement data

Let $f : \mathbb{R} \to \mathbb{R}$,
let $T$ and $T'$ be tagged partitions of $[a, b]$ together with tagged-refinement data from $T$
to $T'$, and let $\omega \in \mathbb{R}$ satisfy $|f(x) - f(y)| \le \omega$ for all
$x, y \in [a, b]$ with $|x - y| \le \|T\|$, where $\|T\|$ is the mesh of $T$. Writing $S_f(T)$
for the Riemann sum of $f$ over $T$, we have $|S_f(T) - S_f(T')| \le \omega (b - a)$.

Formalized by `MathlibExt.Analysis.Integration.riemannSum_sub_le_of_isTaggedRefinement`, a theorem declared in [MathlibExt/Analysis/Integration/RiemannSumRefinement.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannSumRefinement.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#riemann-sum-sub-le-of-is-tagged-refineme).

## Riemann sums under refinement

Let $f : \mathbb{R} \to \mathbb{R}$, let $T$ and $T'$ be
tagged partitions of $[a, b]$ such that every point of $T$ is a point of $T'$, and let
$\omega \in \mathbb{R}$ satisfy $|f(x) - f(y)| \le \omega$ for all $x, y \in [a, b]$ with
$|x - y| \le \|T\|$, where $\|T\|$ is the mesh of $T$. Writing $S_f(T)$ for the Riemann sum of
$f$ over $T$, we have $|S_f(T) - S_f(T')| \le \omega (b - a)$.

This is Theorem II of the Riemann integral section in oscillation form: an explicit bound
$\omega$ replaces the modulus of continuity, so $f$ need not be continuous.

Formalized by `MathlibExt.Analysis.Integration.riemannSum_sub_le_of_isRefinement`, a theorem declared in [MathlibExt/Analysis/Integration/RiemannSumRefinement.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannSumRefinement.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#riemann-sum-sub-le-of-is-refinement).

## Riemann sums of two partitions with a common refinement

Let $f : \mathbb{R} \to \mathbb{R}$
and let $T_1$, $T_2$ be tagged partitions of $[a, b]$ with meshes $\|T_1\|$ and $\|T_2\|$.
Suppose $\omega_1, \omega_2 \in \mathbb{R}$ satisfy, for $i = 1, 2$, $|f(x) - f(y)| \le \omega_i$
for all $x, y \in [a, b]$ with $|x - y| \le \|T_i\|$. Let $T''$ be a tagged partition of
$[a, b]$ together with tagged-refinement data from $T_1$ to $T''$ and from $T_2$ to $T''$.
Writing $S_f(T)$ for the Riemann sum of $f$ over $T$, we have
$|S_f(T_1) - S_f(T_2)| \le (\omega_1 + \omega_2)(b - a)$.

This is Theorem III of the Riemann integral section in oscillation form: explicit bounds
$\omega_i$ replace the modulus of continuity, so $f$ need not be continuous.

Formalized by `MathlibExt.Analysis.Integration.riemannSum_sub_le_of_commonRefinement`, a theorem declared in [MathlibExt/Analysis/Integration/RiemannSumRefinement.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannSumRefinement.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#riemann-sum-sub-le-of-common-refinement).

## Common refinement of two tagged partitions

Let $a, b$ be real numbers. For any two
tagged partitions $T_1$ and $T_2$ of $[a, b]$, there is a tagged partition $T''$ of $[a, b]$
that is a tagged refinement of both $T_1$ and $T_2$.

The proof takes for $T''$ the partition whose points are the union of the points of $T_1$
and $T_2$, with each tag at the left endpoint of its subinterval.

Formalized by `MathlibExt.Analysis.Integration.TaggedPartition.exists_commonRefinement`, a theorem declared in [MathlibExt/Analysis/Integration/RiemannCommonRefinement.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Integration/RiemannCommonRefinement.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html#exists-common-refinement).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Riemann integral](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/riemann-integral/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/real-functions/integration/riemann-integral)
