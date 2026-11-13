---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.GoldenRatioThompsonEmbedWanted.IsDyadic, MathlibExt.GroupTheory.GoldenRatioThompsonEmbedWanted.IsGoldenInteger, MathlibExt.GroupTheory.GoldenRatioThompsonEmbedWanted.IsPLHomeoWith, MathlibExt.GroupTheory.GoldenRatioThompsonEmbedWanted.thompsonF, MathlibExt.GroupTheory.GoldenRatioThompsonEmbedWanted.clearyFTau, MathlibExt.GroupTheory.GoldenRatioThompsonEmbedWanted.conjecture, MathlibExt.GroupTheory.GoldenRatioThompsonEmbedWanted.conjecture_refuted
statement: formalized
---

# Golden-ratio Thompson group

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/golden-ratio-thompson-group/index.html).

## Dyadic rationals

A real number $x$ is dyadic when $x = a / 2^n$ for some integer $a$ and
some natural number $n$, that is, when $x$ lies in $\mathbb{Z}[1/2]$.

Formalized by `MathlibExt.GroupTheory.GoldenRatioThompsonEmbedWanted.IsDyadic`, a definition declared in [WantedExt/GroupTheory/GoldenRatioThompsonEmbedWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/GoldenRatioThompsonEmbedWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/golden-ratio-thompson-group/index.html#is-dyadic).

## Golden integers

Let $\tau = (1 + \sqrt{5})/2$ be the golden ratio. A real number $x$ is a
golden integer when $x = a + b\tau$ for some integers $a$ and $b$. Since $\tau^2 = \tau + 1$, these
are exactly the elements of $\mathbb{Z}[\tau]$.

Formalized by `MathlibExt.GroupTheory.GoldenRatioThompsonEmbedWanted.IsGoldenInteger`, a definition declared in [WantedExt/GroupTheory/GoldenRatioThompsonEmbedWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/GoldenRatioThompsonEmbedWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/golden-ratio-thompson-group/index.html#is-golden-integer).

## Piecewise-linear maps with prescribed breakpoints and slopes

Let $B$ and $S$ be sets of
real numbers. A permutation $f$ of $\mathbb{R}$ is piecewise linear with breakpoints in $B$ and
slopes in $S$ when $f(x) = x$ for every $x \notin [0, 1]$, and there are a natural number $n$
and points $0 = t_0 < t_1 < \dots < t_{n+1} = 1$, all in $B$, such that for each $i \le n$ there
is $s \in S$ with $f(x) = f(t_i) + s (x - t_i)$ for all $x \in [t_i, t_{i+1}]$.

Adjacent pieces agree at the shared point, so $f$ restricts to a piecewise-linear homeomorphism
of $[0, 1]$ when the slopes are positive.

Formalized by `MathlibExt.GroupTheory.GoldenRatioThompsonEmbedWanted.IsPLHomeoWith`, a definition declared in [WantedExt/GroupTheory/GoldenRatioThompsonEmbedWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/GoldenRatioThompsonEmbedWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/golden-ratio-thompson-group/index.html#is-plhomeo-with).

## Thompson's group F

Thompson's group $F$ is the set of permutations $f$ of $\mathbb{R}$
such that $f(x) = x$ for every $x \notin [0, 1]$, and there are a natural number $n$ and points
$0 = t_0 < t_1 < \dots < t_{n+1} = 1$, each of the form $a / 2^m$ with $a \in \mathbb{Z}$ and
$m \in \mathbb{N}$, such that on each interval $[t_i, t_{i+1}]$ the map $f$ is affine with slope
$2^k$ for some integer $k$, that is, $f(x) = f(t_i) + 2^k (x - t_i)$ for all
$x \in [t_i, t_{i+1}]$.

Formalized by `MathlibExt.GroupTheory.GoldenRatioThompsonEmbedWanted.thompsonF`, a definition declared in [WantedExt/GroupTheory/GoldenRatioThompsonEmbedWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/GoldenRatioThompsonEmbedWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/golden-ratio-thompson-group/index.html#thompson-f).

## Cleary's golden-ratio Thompson group

Let $\tau = (1 + \sqrt{5})/2$ be the golden
ratio. Cleary's group $F_\tau$ is the set of permutations $f$ of $\mathbb{R}$ such that
$f(x) = x$ for every $x \notin [0, 1]$, and there are a natural number $n$ and points
$0 = t_0 < t_1 < \dots < t_{n+1} = 1$, each of the form $a + b\tau$ with $a, b \in \mathbb{Z}$,
such that on each interval $[t_i, t_{i+1}]$ the map $f$ is affine with slope $\tau^k$ for some
integer $k$, that is, $f(x) = f(t_i) + \tau^k (x - t_i)$ for all $x \in [t_i, t_{i+1}]$.

Formalized by `MathlibExt.GroupTheory.GoldenRatioThompsonEmbedWanted.clearyFTau`, a definition declared in [WantedExt/GroupTheory/GoldenRatioThompsonEmbedWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/GoldenRatioThompsonEmbedWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/golden-ratio-thompson-group/index.html#cleary-ftau).

## Golden-ratio Thompson embedding conjecture

The proposition that there is a map
$\varphi$ from permutations of $\mathbb{R}$ to permutations of $\mathbb{R}$ that sends every
element of Cleary's golden-ratio Thompson group $F_\tau$ into Thompson's group $F$, is injective
on $F_\tau$, and satisfies $\varphi(g h) = \varphi(g) \varphi(h)$ for all $g, h \in F_\tau$,
where the product of permutations is composition.

Since $F_\tau$ is a group under composition, this says that $F_\tau$ embeds in $F$ as a group.

## Sources

- record OWR-16167-018.

Formalized by `MathlibExt.GroupTheory.GoldenRatioThompsonEmbedWanted.conjecture`, a definition declared in [WantedExt/GroupTheory/GoldenRatioThompsonEmbedWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/GoldenRatioThompsonEmbedWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/golden-ratio-thompson-group/index.html#conjecture).

## Cleary's golden-ratio group does not embed in Thompson's group F

There is no map $\varphi$
from permutations of $\mathbb{R}$ to permutations of $\mathbb{R}$ that sends every element of
Cleary's golden-ratio Thompson group $F_\tau$ into Thompson's group $F$, is injective on
$F_\tau$, and satisfies $\varphi(g h) = \varphi(g) \varphi(h)$ for all $g, h \in F_\tau$, where
the product of permutations is composition. In other words, the golden-ratio Thompson embedding
conjecture is false: $F_\tau$ does not embed in $F$ as a group.

Hyde and Moore proved this by introducing F-obstructions (Corollary 1.4; Corollary 1 in arXiv v1).

## Sources

- J. Hyde, J. T. Moore, Subgroups of PL+I which do not embed into Thompson's group F, Groups, Geometry, and Dynamics 17 (2023) 533-554, arXiv:2103.14911, https://arxiv.org/abs/2103.14911.

Stated but not proved: `MathlibExt.GroupTheory.GoldenRatioThompsonEmbedWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/GoldenRatioThompsonEmbedWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/GoldenRatioThompsonEmbedWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/golden-ratio-thompson-group/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Golden-ratio Thompson group](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/golden-ratio-thompson-group/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/golden-ratio-thompson-group)
