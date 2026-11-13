---
declaration: section
origin: cited
lean: ConvexCovering.IsConvexBody, ConvexCovering.CoveredByTranslates, ConvexCovering.CoveredByInteriorTranslates, ConvexCovering.UniformInteriorTranslateBound, ConvexCovering.IsCentrallySymmetric, ConvexCovering.UniformSymmetricInteriorTranslateBound, ConvexCovering.CoveredBySmallerPositiveHomothets, ConvexCovering.translateCoveringNumber
statement: formalized
---

# Hadwiger covering and illumination problem

46 results, 34 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html).

## Convex bodies in Euclidean space

A set $K$ in the Euclidean space $\mathbb{R}^n$ is a
convex body when it is compact and convex and its interior in $\mathbb{R}^n$ is nonempty.

Formalized by `ConvexCovering.IsConvexBody`, a definition declared in [MathlibExt/Geometry/Convex/Covering.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Covering.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#is-convex-body).

## Covering by translates

For sets $K$ and $L$ in the Euclidean space $\mathbb{R}^n$ and a
natural number $q$, $K$ is covered by $q$ translates of $L$ when there are vectors
$v_1, \dots, v_q \in \mathbb{R}^n$ with $K \subseteq \bigcup_{i=1}^{q} (v_i + L)$, where
$v + L = \{v + y : y \in L\}$.

Formalized by `ConvexCovering.CoveredByTranslates`, a definition declared in [MathlibExt/Geometry/Convex/Covering.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Covering.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#covered-by-translates).

## Covering by interior translates

A set $K$ in the Euclidean space $\mathbb{R}^n$ is covered
by $q$ interior translates, for a natural number $q$, when there are vectors
$v_1, \dots, v_q \in \mathbb{R}^n$ such that
$K \subseteq \bigcup_{i=1}^{q} (v_i + \operatorname{int} K)$, where $\operatorname{int} K$ is the
interior of $K$ in $\mathbb{R}^n$ and $v + S = \{v + y : y \in S\}$.

Formalized by `ConvexCovering.CoveredByInteriorTranslates`, a definition declared in [MathlibExt/Geometry/Convex/Covering.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Covering.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#covered-by-interior-translates).

## Uniform bound for covering convex bodies by interior translates

For $n, q \in \mathbb{N}$,
the uniform interior translate bound holds when every convex body $K \subseteq \mathbb{R}^n$ (a
compact convex set with nonempty interior) is covered by $q$ translates of its interior
$\operatorname{int} K$, that is, $K \subseteq (v_1 + \operatorname{int} K) \cup \dots \cup
(v_q + \operatorname{int} K)$ for some $v_1, \dots, v_q \in \mathbb{R}^n$.

This is one bound $q$ for all bodies at once, not a minimum over bodies.

Formalized by `ConvexCovering.UniformInteriorTranslateBound`, a definition declared in [MathlibExt/Geometry/Convex/Covering.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Covering.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#uniform-interior-translate-bound).

## Central symmetry about some center

A set $K$ in the Euclidean space $\mathbb{R}^n$ is
centrally symmetric when there is a point $c \in \mathbb{R}^n$ such that for every
$x \in \mathbb{R}^n$, $x \in K$ if and only if $2c - x \in K$.

Formalized by `ConvexCovering.IsCentrallySymmetric`, a definition declared in [MathlibExt/Geometry/Convex/Covering.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Covering.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#is-centrally-symmetric).

## Uniform bound for covering centrally symmetric convex bodies by interior translates

For
$n, q \in \mathbb{N}$, the uniform symmetric interior translate bound holds when every convex body
$K \subseteq \mathbb{R}^n$ (a compact convex set with nonempty interior) that is centrally
symmetric, meaning that there is $c \in \mathbb{R}^n$ such that for all $x \in \mathbb{R}^n$,
$x \in K$ if and only if $2c - x \in K$, is covered by $q$ translates of its interior, that is,
$K \subseteq (v_1 + \operatorname{int} K) \cup \dots \cup (v_q + \operatorname{int} K)$ for some
$v_1, \dots, v_q \in \mathbb{R}^n$.

Formalized by `ConvexCovering.UniformSymmetricInteriorTranslateBound`, a definition declared in [MathlibExt/Geometry/Convex/Covering.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Covering.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#uniform-symmetric-interior-translate-bou).

## Covering by smaller positive homothets

A set $K$ in the Euclidean space $\mathbb{R}^n$ is
covered by $q$ smaller positive homothets, for a natural number $q$, when there are real numbers
$r_1, \dots, r_q$ with $0 < r_i < 1$ for every $i$ and vectors $v_1, \dots, v_q \in \mathbb{R}^n$
such that every point of $K$ lies in $v_i + r_i K = \{v_i + r_i y : y \in K\}$ for some $i$.

The homothets are indexed by $i$, so the same homothet may occur more than once.

Formalized by `ConvexCovering.CoveredBySmallerPositiveHomothets`, a definition declared in [MathlibExt/Geometry/Convex/Covering.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Covering.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#covered-by-smaller-positive-homothets).

## Translate covering number

For sets $K, L \subseteq \mathbb{R}^n$, the translate covering
number of $K$ by $L$ is the least natural number $q$ for which there are vectors
$v_1, \dots, v_q \in \mathbb{R}^n$ with $K \subseteq (v_1 + L) \cup \dots \cup (v_q + L)$, and it
is $\infty$ if no such $q$ exists.

Formalized by `ConvexCovering.translateCoveringNumber`, a definition declared in [MathlibExt/Geometry/Convex/Covering.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Covering.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#translate-covering-number).

## Hadwiger covering number

The Hadwiger covering number of dimension $n$, an element of
$\mathbb{N} \cup \{\infty\}$, is the least natural number $q$ such that every convex body $K$ in
the Euclidean space $\mathbb{R}^n$ is covered by $q$ translates of its interior
$\operatorname{int} K$, and it is $\infty$ if no such $q$ exists.

Formalized by `ConvexCovering.hadwigerCoveringNumber`, a definition declared in [MathlibExt/Geometry/Convex/Covering.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Covering.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#hadwiger-covering-number).

## Symmetric Hadwiger covering number

For $n \in \mathbb{N}$, the symmetric Hadwiger
covering number in dimension $n$ is the least natural number $q$ such that every centrally
symmetric convex body $K \subseteq \mathbb{R}^n$ (a compact convex set with nonempty interior that
is symmetric about some point) is covered by $q$ translates of its interior, and it is $\infty$
if no such $q$ exists.

Formalized by `ConvexCovering.symmetricHadwigerCoveringNumber`, a definition declared in [MathlibExt/Geometry/Convex/Covering.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Covering.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#symmetric-hadwiger-covering-number).

## Pointwise form of covering by translates

For sets $K$ and $L$ in the Euclidean space
$\mathbb{R}^n$ and a natural number $q$, $K$ is covered by $q$ translates of $L$ if and only if
there are vectors $v_1, \dots, v_q \in \mathbb{R}^n$ such that every $x \in K$ lies in
$v_i + L = \{v_i + y : y \in L\}$ for some $i$.

Formalized by `ConvexCovering.coveredByTranslates_iff`, a theorem declared in [MathlibExt/Geometry/Convex/Covering.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Covering.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#covered-by-translates-iff).

## Interior-translate covers unfold to translate covers

For every set $K$ in the Euclidean
space $\mathbb{R}^n$ and every natural number $q$, $K$ has a cover by $q$ interior translates if
and only if $K$ is covered by $q$ translates of the set $L = \operatorname{int} K$, the interior
of $K$ in $\mathbb{R}^n$.

Formalized by `ConvexCovering.coveredByInteriorTranslates_iff`, a theorem declared in [MathlibExt/Geometry/Convex/Covering.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Covering.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#covered-by-interior-translates-iff).

## The translate covering number is the least covering count

Let $K, L \subseteq \mathbb{R}^n$
and let $q \in \mathbb{N}$. If $q$ is the least natural number $r$ such that $K$ is covered by $r$
translates of $L$, then the translate covering number of $K$ by $L$ equals $q$.

Formalized by `ConvexCovering.translateCoveringNumber_eq_of_isLeast`, a theorem declared in [MathlibExt/Geometry/Convex/Covering.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Covering.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#translate-covering-number-eq-of-is-least).

## A least uniform bound is the Hadwiger covering number

If $q$ is the least natural number
such that every convex body $K$ in the Euclidean space $\mathbb{R}^n$ is covered by $q$ translates
of its interior, then the Hadwiger covering number of dimension $n$ equals $q$.

Formalized by `ConvexCovering.hadwigerCoveringNumber_eq_of_isLeast`, a theorem declared in [MathlibExt/Geometry/Convex/Covering.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Covering.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#hadwiger-covering-number-eq-of-is-least).

## A least uniform bound is the symmetric Hadwiger covering number

If $q$ is the least
natural number such that every centrally symmetric convex body $K$ in the Euclidean space
$\mathbb{R}^n$ is covered by $q$ translates of its interior, then the symmetric Hadwiger
covering number of dimension $n$ equals $q$.

Formalized by `ConvexCovering.symmetricHadwigerCoveringNumber_eq_of_isLeast`, a theorem declared in [MathlibExt/Geometry/Convex/Covering.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Covering.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#symmetric-hadwiger-covering-number-eq-of).

## Coordinate cube

For $n \in \mathbb{N}$, the coordinate cube is the set $[-1, 1]^n$ of
points $x$ of the Euclidean space $\mathbb{R}^n$ with $-1 \le x_i \le 1$ for every coordinate
$i$.

Formalized by `ConvexCovering.coordinateCube`, a definition declared in [MathlibExt/Geometry/Convex/CubeCovering.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/CubeCovering.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#coordinate-cube).

## The coordinate cube as an absolute-value box

For every $n$, the coordinate cube in
$\mathbb{R}^n$ equals the set of points $x \in \mathbb{R}^n$ with $|x_i| \le 1$ for every
coordinate $i$.

Formalized by `ConvexCovering.coordinateCube_eq_absSet`, a theorem declared in [MathlibExt/Geometry/Convex/CubeCovering.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/CubeCovering.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#coordinate-cube-eq-abs-set).

## Affine cube

A set $K \subseteq \mathbb{R}^n$ is an affine cube if $K = e([-1, 1]^n)$ for
some affine bijection $e : \mathbb{R}^n \to \mathbb{R}^n$, where $[-1, 1]^n$ is the coordinate cube
$\{x \in \mathbb{R}^n : -1 \le x_i \le 1 \text{ for all } i\}$.

Formalized by `ConvexCovering.IsAffineCube`, a definition declared in [MathlibExt/Geometry/Convex/CubeCovering.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/CubeCovering.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#is-affine-cube).

## Interior of the coordinate cube

A point $x \in \mathbb{R}^n$ lies in the interior of
the coordinate cube $[-1, 1]^n$ if and only if $-1 < x_i < 1$ for every coordinate $i$.

Formalized by `ConvexCovering.coordinateCube_interior_iff`, a theorem declared in [MathlibExt/Geometry/Convex/CubeCovering.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/CubeCovering.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#coordinate-cube-interior-iff).

## The coordinate cube is a convex body

For every $n$, the coordinate cube $[-1, 1]^n$ in
$\mathbb{R}^n$ is a convex body: it is compact and convex, and its interior in $\mathbb{R}^n$ is
nonempty.

Formalized by `ConvexCovering.coordinateCube_isConvexBody`, a theorem declared in [MathlibExt/Geometry/Convex/CubeCovering.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/CubeCovering.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#coordinate-cube-is-convex-body).

## The coordinate cube is centrally symmetric

For every $n$, the coordinate cube
$[-1, 1]^n$ in $\mathbb{R}^n$ is centrally symmetric: there is a point $c \in \mathbb{R}^n$ such
that for every $x \in \mathbb{R}^n$, $x$ lies in the cube if and only if $2c - x$ does.

Formalized by `ConvexCovering.coordinateCube_isCentrallySymmetric`, a theorem declared in [MathlibExt/Geometry/Convex/CubeCovering.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/CubeCovering.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#coordinate-cube-is-centrally-symmetric).

## Covering the cube by translates of its interior needs $2^n$ translates

Let
$C_n = [-1, 1]^n$ be the coordinate cube in $\mathbb{R}^n$. If $C_n$ is contained in the union of
$q$ translates $v_1 + \operatorname{int} C_n, \dots, v_q + \operatorname{int} C_n$ of its interior,
then $2^n \le q$.

Formalized by `ConvexCovering.coordinateCube_coveringCount_ge_two_pow`, a theorem declared in [MathlibExt/Geometry/Convex/CubeCovering.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/CubeCovering.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#coordinate-cube-covering-count-ge-two-po).

## Lower bound $2^n$ for uniform interior-translate covering

Let $n$ and $q$ be natural
numbers. If every convex body $K \subseteq \mathbb{R}^n$ (a compact convex set with nonempty
interior) can be covered by $q$ not necessarily distinct translates of its interior, then
$2^n \le q$.

The coordinate cube $[-1, 1]^n$ already needs $2^n$ translates.

Formalized by `ConvexCovering.uniformInteriorTranslateBound_ge_two_pow`, a theorem declared in [MathlibExt/Geometry/Convex/CubeCovering.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/CubeCovering.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#uniform-interior-translate-bound-ge-two).

## Uniform interior-translate bounds in dimension three are at least eight

If $q$ is a
natural number such that every convex body $K \subseteq \mathbb{R}^3$ is contained in the union of
$q$ translates of its interior $\operatorname{int} K$, then $8 \le q$.

Formalized by `ConvexCovering.cubeLowerBound`, a theorem declared in [MathlibExt/Geometry/Convex/CubeCovering.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/CubeCovering.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#cube-lower-bound).

## Lower bound $2^n$ for centrally symmetric interior-translate covering

Let $n$ and $q$ be
natural numbers. If every centrally symmetric convex body $K \subseteq \mathbb{R}^n$ (a compact
convex set with nonempty interior that is symmetric about some point) can be covered by $q$ not
necessarily distinct translates of its interior, then $2^n \le q$.

The coordinate cube $[-1, 1]^n$ is such a body and already needs $2^n$ translates.

Formalized by `ConvexCovering.symmetricInteriorTranslateBound_ge_two_pow`, a theorem declared in [MathlibExt/Geometry/Convex/CubeCovering.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/CubeCovering.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#symmetric-interior-translate-bound-ge-tw).

## Eight translates of the interior cover the three-dimensional cube

Let
$C_3 = [-1, 1]^3$ be the coordinate cube in $\mathbb{R}^3$. There are vectors
$v_1, \dots, v_8 \in \mathbb{R}^3$ such that $C_3$ is contained in the union of the translates
$v_1 + \operatorname{int} C_3, \dots, v_8 + \operatorname{int} C_3$ of its interior.

Formalized by `ConvexCovering.coordinateCube_three_coveredByInteriorTranslates`, a theorem declared in [MathlibExt/Geometry/Convex/CubeCovering.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/CubeCovering.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#coordinate-cube-three-covered-by-interio).

## Eight is the least number of interior translates covering the three-dimensional cube

Let $C_3 = [-1, 1]^3$ be the coordinate cube in $\mathbb{R}^3$. Then $8$ is the least natural
number $q$ such that $C_3$ is contained in the union of $q$ translates of its interior
$\operatorname{int} C_3$.

Formalized by `ConvexCovering.coordinateCube_three_least_coveringCount`, a theorem declared in [MathlibExt/Geometry/Convex/CubeCovering.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/CubeCovering.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#coordinate-cube-three-least-covering-cou).

## Translate covering number of the three-dimensional cube by its interior

Let
$C_3 = [-1, 1]^3$ be the coordinate cube in $\mathbb{R}^3$. The translate covering number of $C_3$
by its interior $\operatorname{int} C_3$, the least number of translates of $\operatorname{int} C_3$
whose union contains $C_3$, equals $8$.

Formalized by `ConvexCovering.coordinateCube_three_translateCoveringNumber`, a theorem declared in [MathlibExt/Geometry/Convex/CubeCovering.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/CubeCovering.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#coordinate-cube-three-translate-covering).

## Illumination by a direction

Let $K \subseteq \mathbb{R}^n$ be a set and let
$v, x \in \mathbb{R}^n$. The direction $v$ illuminates $x$ with respect to $K$ when $x$ lies on
the boundary of $K$, $\|v\| = 1$, and $x + tv$ lies in the interior of $K$ for some real
$t > 0$.

Formalized by `ConvexCovering.DirectionIlluminates`, a definition declared in [MathlibExt/Geometry/Convex/Illumination.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Illumination.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#direction-illuminates).

## Illumination by $q$ directions

A set $K \subseteq \mathbb{R}^n$ is illuminated by $q$
directions, for a natural number $q$, if there are unit vectors $v_1, \dots, v_q \in \mathbb{R}^n$
(not necessarily distinct) such that for every boundary point $x$ of $K$ there are an index $i$
and a real $t > 0$ with $x + tv_i$ in the interior of $K$.

Formalized by `ConvexCovering.IlluminatedByDirections`, a definition declared in [MathlibExt/Geometry/Convex/Illumination.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Illumination.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#illuminated-by-directions).

## Illumination by an external point

Let $K \subseteq \mathbb{R}^n$ be a set and let
$p, x \in \mathbb{R}^n$. The point $p$ illuminates $x$ with respect to $K$ when $p \notin K$, $x$
lies on the boundary of $K$, and $p + t(x - p)$ lies in the interior of $K$ for some real $t > 1$;
that is, the ray from $p$ through $x$ meets the interior of $K$ at a point beyond $x$.

Formalized by `ConvexCovering.ExternalPointIlluminates`, a definition declared in [MathlibExt/Geometry/Convex/Illumination.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Illumination.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#external-point-illuminates).

## Illumination by $q$ external points

A set $K \subseteq \mathbb{R}^n$ is illuminated by $q$
external points, for a natural number $q$, if there are points
$p_1, \dots, p_q \in \mathbb{R}^n \setminus K$ (not necessarily distinct) such that for every
boundary point $x$ of $K$ there are an index $i$ and a real $t > 1$ with $p_i + t(x - p_i)$ in the
interior of $K$.

Formalized by `ConvexCovering.IlluminatedByExternalPoints`, a definition declared in [MathlibExt/Geometry/Convex/Illumination.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Illumination.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#illuminated-by-external-points).

## Directional illumination number

The directional illumination number of a set
$K \subseteq \mathbb{R}^n$ is the least natural number $q$ such that $K$ is illuminated by $q$
directions, and $\infty$ if there is no such $q$.

Formalized by `ConvexCovering.directionalIlluminationNumber`, a definition declared in [MathlibExt/Geometry/Convex/Illumination.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Illumination.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#directional-illumination-number).

## External-point illumination number

The external-point illumination number of a set
$K \subseteq \mathbb{R}^n$ is the least natural number $q$ such that $K$ is illuminated by $q$
external points, and $\infty$ if there is no such $q$.

Formalized by `ConvexCovering.externalPointIlluminationNumber`, a definition declared in [MathlibExt/Geometry/Convex/Illumination.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Illumination.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#external-point-illumination-number).

## Two equivalent formulations of Hadwiger's covering conjecture

The following statements
are equivalent: for every $n \ge 1$, every convex body $K \subseteq \mathbb{R}^n$ is covered by at
most $2^n$ homothets $v_i + r_i K$ with $v_i \in \mathbb{R}^n$ and $0 < r_i < 1$; and for every
$n \ge 1$, every convex body $K \subseteq \mathbb{R}^n$ is covered by $2^n$ translates of its
interior $\operatorname{int} K$, repetitions allowed.

## Sources

- Bezdek and Khan, arXiv:1602.06040v2, introduction; Arman, Kaire and Prymak, arXiv:2510.25968v3, introduction.

Stated but not proved: `ConvexCovering.homothetInteriorTranslateFormulationsEquivalent` is written with `theorem_wanted` in [WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#homothet-interior-translate-formulations).

## Papadoperakis's bound for Hadwiger's covering problem in dimension 3

Every convex body
$K \subseteq \mathbb{R}^3$ is covered by $16$ translates of its interior $\operatorname{int} K$,
repetitions allowed.

## Sources

- Papadoperakis (1999), reported in Arman, Bondarenko and Prymak, arXiv:2404.00547v1, introduction.

Stated but not proved: `ConvexCovering.papadoperakis1999UpperBound` is written with `theorem_wanted` in [WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#papadoperakis1999-upper-bound).

## Prymak's bound for Hadwiger's covering problem in dimension 3

Every convex body
$K \subseteq \mathbb{R}^3$ is covered by $14$ translates of its interior $\operatorname{int} K$,
repetitions allowed.

## Sources

- Prymak (2023), arXiv:2112.10698; reported in Arman, Bondarenko and Prymak, arXiv:2404.00547v1, introduction.

Stated but not proved: `ConvexCovering.prymak2023UpperBound` is written with `theorem_wanted` in [WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#prymak2023-upper-bound).

## Lassak's theorem for centrally symmetric bodies in dimension 3

The number $8$ is the least
natural number $q$ such that every centrally symmetric convex body $K \subseteq \mathbb{R}^3$ is
covered by $q$ translates of its interior $\operatorname{int} K$, repetitions allowed. Here $K$ is
centrally symmetric when there is a point $c$ with $x \in K$ if and only if $2c - x \in K$.

## Sources

- Lassak (1984), reported in Arman, Bondarenko and Prymak, arXiv:2404.00547v1, introduction.

Stated but not proved: `ConvexCovering.lassak1984SymmetricExactValue` is written with `theorem_wanted` in [WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#lassak1984-symmetric-exact-value).

## Directional and exterior-point illumination are equivalent

Let $n \ge 1$, let
$K \subseteq \mathbb{R}^n$ be a convex body and let $q$ be a natural number. Then some $q$ unit
vectors $v_1, \dots, v_q$ illuminate $K$ if and only if some $q$ points $p_1, \dots, p_q$ outside
$K$ illuminate $K$. Here the vectors illuminate $K$ when every boundary point $x$ of $K$ has an $i$
and a $t > 0$ with $x + t v_i$ in the interior of $K$, and the points illuminate $K$ when every
boundary point $x$ of $K$ has an $i$ and a $t > 1$ with $p_i + t (x - p_i)$ in the interior of $K$.

## Sources

- Bezdek and Khan, arXiv:1602.06040v2, introduction.

Stated but not proved: `ConvexCovering.directionalExternalFormulationsEquivalent` is written with `theorem_wanted` in [WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#directional-external-formulations-equiva).

## Directional illumination is equivalent to covering by smaller homothets

Let $n \ge 1$,
let $K \subseteq \mathbb{R}^n$ be a convex body and let $q$ be a natural number. Then some $q$
unit vectors illuminate $K$ if and only if $K$ is covered by $q$ homothets
$v_1 + r_1 K, \dots, v_q + r_q K$ with $v_i \in \mathbb{R}^n$ and $0 < r_i < 1$, repetitions
allowed.

## Sources

- Bezdek and Khan, arXiv:1602.06040v2, introduction.

Stated but not proved: `ConvexCovering.directionalHomothetFormulationsEquivalent` is written with `theorem_wanted` in [WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#directional-homothet-formulations-equiva).

## Directional illumination is equivalent to covering by interior translates

Let $n \ge 1$,
let $K \subseteq \mathbb{R}^n$ be a convex body and let $q$ be a natural number. Then some $q$ unit
vectors illuminate $K$ if and only if $K$ is covered by $q$ translates
$v_1 + \operatorname{int} K, \dots, v_q + \operatorname{int} K$ of its interior, repetitions
allowed.

## Sources

- Arman, Kaire and Prymak, arXiv:2510.25968v3, introduction.

Stated but not proved: `ConvexCovering.directionalInteriorFormulationsEquivalent` is written with `theorem_wanted` in [WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#directional-interior-formulations-equiva).

## Directional and exterior-point illumination numbers are equal

For every $n \ge 1$ and
every convex body $K \subseteq \mathbb{R}^n$, the directional illumination number of $K$ equals
its exterior-point illumination number. These are the least $q$ such that some $q$ unit vectors,
respectively some $q$ points outside $K$, illuminate $K$, with the value $\infty$ when no finite
family does.

## Sources

- Bezdek and Khan, arXiv:1602.06040v2, introduction; follows from its finite-count equivalence, whose Lean proof is also requested here.

Stated but not proved: `ConvexCovering.directionalExternalIlluminationNumbersEqual` is written with `theorem_wanted` in [WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#directional-external-illumination-number).

## Directional illumination number equals the interior-translate covering number

For every
$n \ge 1$ and every convex body $K \subseteq \mathbb{R}^n$, the directional illumination number of
$K$ equals the least $q$ such that $K$ is covered by $q$ translates of its interior
$\operatorname{int} K$. Both sides take the value $\infty$ when no finite family exists.

## Sources

- Arman, Kaire and Prymak, arXiv:2510.25968v3, introduction; follows from the finite-count equivalence, whose Lean proof is also requested here.

Stated but not proved: `ConvexCovering.directionalInteriorCoveringNumbersEqual` is written with `theorem_wanted` in [WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#directional-interior-covering-numbers-eq).

## Every convex body has a finite illumination number

For every $n \ge 1$ and every convex
body $K \subseteq \mathbb{R}^n$ there is a least natural number $q$ such that some $q$ unit vectors
$v_1, \dots, v_q$ illuminate $K$: every boundary point $x$ of $K$ has an $i$ and a $t > 0$ with
$x + t v_i$ in the interior of $K$.

## Sources

- Arman, Kaire and Prymak, arXiv:2510.25968v3, introduction's illumination-number definition; finite existence is the standard compact-convex-body qualification.

Stated but not proved: `ConvexCovering.illuminationFiniteMinimum` is written with `theorem_wanted` in [WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#illumination-finite-minimum).

## Uniform covering by interior translates and uniform directional illumination

For
integers $n \ge 1$ and $q \ge 0$, every convex body in $\mathbb{R}^n$ (a compact convex set with
nonempty interior) can be covered by $q$ translates of its interior if and only if every convex
body $K$ in $\mathbb{R}^n$ is illuminated by $q$ directions: there are unit vectors
$v_1, \dots, v_q$ such that each boundary point $x$ of $K$ has some $i$ and some $t > 0$ with
$x + t v_i$ in the interior of $K$.

## Sources

- Arman, Kaire and Prymak, arXiv:2510.25968v3, introduction; follows from the finite-count equivalence, whose Lean proof is also requested here.

Stated but not proved: `ConvexCovering.uniformDirectionalIlluminationInterpretation` is written with `theorem_wanted` in [WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#uniform-directional-illumination-interpr).

## Uniform covering of symmetric bodies and uniform illumination by external points

For
integers $n \ge 1$ and $q \ge 0$, every centrally symmetric convex body in $\mathbb{R}^n$ (a
compact convex set with nonempty interior that is symmetric about some point) can be covered by
$q$ translates of its interior if and only if every centrally symmetric convex body $K$ in
$\mathbb{R}^n$ is illuminated by $q$ external points: there are points $p_1, \dots, p_q$ outside
$K$ such that each boundary point $x$ of $K$ has some $i$ and some $t > 1$ with
$p_i + t(x - p_i)$ in the interior of $K$.

## Sources

- Arman, Kaire and Prymak, arXiv:2510.25968v3, introduction, and Bezdek and Khan, arXiv:1602.06040v2, introduction; follows from the two finite-count equivalences.

Stated but not proved: `ConvexCovering.uniformSymmetricExternalIlluminationInterpretation` is written with `theorem_wanted` in [WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/Convex/HadwigerCoveringWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html#uniform-symmetric-external-illumination).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hadwiger covering and illumination problem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/packings-and-coverings/hadwiger-covering-and-illumination-problem)
