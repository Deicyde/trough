---
declaration: section
origin: cited
lean: MetaMathlibExt.platonic_solids_classification, MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.E, MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope, MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope.toSet, MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope.dim, MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope.IsFullDim, MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope.IsFace, MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope.faceDim
statement: formalized
---

# Platonic solids and regular polytopes

17 results, 16 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html).

## Classification of the Platonic solids

Let $V, E, F, p, q$ be natural numbers with
$V, E, F > 0$ and $p, q \ge 3$, and let $l > 0$ and $d > 0$ be real numbers. Let
$x_0, \dots, x_{V-1}$ be points of the Euclidean space $\mathbb{R}^3$, let $K$ be their convex
hull and let $\partial K$ be its topological boundary. Let each edge $e < E$ be an ordered pair
$(a_e, b_e)$ of point indices, with segment $[x_{a_e}, x_{b_e}]$, and let each face $f < F$ be a
list $\phi_f(0), \dots, \phi_f(p-1)$ of point indices, read cyclically: positions are taken
modulo $p$, the sides of $f$ are the pairs $(\phi_f(i), \phi_f(i+1))$, and the filled face is
the convex hull of $x_{\phi_f(0)}, \dots, x_{\phi_f(p-1)}$. An edge $e$ lies on side $i$ of $f$
when $(a_e, b_e)$ equals $(\phi_f(i), \phi_f(i+1))$ or $(\phi_f(i+1), \phi_f(i))$. Assume:
$K$ is convex and contains every $x_i$; no $x_i$ lies in the convex hull of the $x_j$ with
$j \ne i$; the differences $x_i - x_j$ span a space of dimension $3$; every edge segment has
length $l$; for every face $f$ and position $i$,
$\operatorname{dist}(x_{\phi_f(i)}, x_{\phi_f(i+1)}) = l$ and
$\operatorname{dist}(x_{\phi_f(i-1)}, x_{\phi_f(i+1)}) = d$; the indices
$\phi_f(0), \dots, \phi_f(p-1)$ of each face are distinct; no vertex $x_{\phi_f(k)}$ of a face
lies in the convex hull of the other vertices of that face; two sides $(i_1, i_1+1)$ and
$(i_2, i_2+1)$ of a face whose four endpoint positions are all different have disjoint
segments; some edge lies on each side of every face, and every edge lies on a side of some face;
every edge lies on a side of exactly two faces; every edge segment and every filled face is
contained in $K$; the differences of the vertices of each face span a space of dimension at
most $2$; for every face $f$ there are a nonzero vector $n$ and a real $c$ with
$\langle n, x \rangle \le c$ for all $x \in K$ and $\langle n, x_{\phi_f(i)} \rangle = c$ for
every position $i$; two edges $e_1, e_2$ with $(a_{e_1}, b_{e_1})$ equal to
$(a_{e_2}, b_{e_2})$ or $(b_{e_2}, a_{e_2})$ are equal; two faces with the same set of indices
are equal; every $x_i$, every edge segment and every filled face is contained in $\partial K$;
every point of $\partial K$ lies in some filled face; every point index occurs in exactly $q$
faces; and $2E = pF$, $2E = qV$ and $V - E + F = 2$. Then $(p, q, V, E, F)$ is one of
$(3, 3, 4, 6, 4)$ (tetrahedron), $(4, 3, 8, 12, 6)$ (cube), $(3, 4, 6, 12, 8)$ (octahedron),
$(5, 3, 20, 30, 12)$ (dodecahedron) or $(3, 5, 12, 30, 20)$ (icosahedron).

Conversely, each of these five tuples $(p, q, V, E, F)$ is realized: there are points, edges,
faces and reals $l, d > 0$ satisfying all the conditions above, except that the points, edge
segments and filled faces are required to lie in $\partial K$ but not separately in $K$.

Euler's relation $V - E + F = 2$ and the incidence counts $2E = pF$, $2E = qV$ are hypotheses,
and the classification is up to the tuple $(p, q, V, E, F)$, not up to congruence. Together they
give $1/p + 1/q > 1/2$, which leaves the five tuples; explicit coordinates realize each one.

## Sources

- https://en.wikipedia.org/wiki/Platonic_solid.

Formalized by `MetaMathlibExt.platonic_solids_classification`, a theorem declared in [MathlibExt/Geometry/Polyhedra/PlatonicSolidsClassification.lean, line 4331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Polyhedra/PlatonicSolidsClassification.lean#L4331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#platonic-solids-classification).

## Ambient Euclidean space of the Platonic classification

For a natural number $n$, the real
Euclidean space $\mathbb{R}^n$: $n$-tuples of reals with the standard inner product and norm.

Formalized by `MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.E`, an abbreviation declared in [WantedExt/Geometry/PlatonicClassificationWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PlatonicClassificationWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#e).

## Convex polytope

A convex polytope in $\mathbb{R}^n$ is given by its vertex set: a finite
nonempty set $V \subseteq \mathbb{R}^n$ that equals the set of extreme points of its convex hull
$\operatorname{conv}(V)$. The polytope itself is the convex set $\operatorname{conv}(V)$.

Formalized by `MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope`, a structure declared in [WantedExt/Geometry/PlatonicClassificationWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PlatonicClassificationWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#convex-polytope).

## Underlying set of a convex polytope

The underlying set of a convex polytope $P$ in
$\mathbb{R}^n$ is the convex hull of its vertex set.

Formalized by `MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope.toSet`, a definition declared in [WantedExt/Geometry/PlatonicClassificationWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PlatonicClassificationWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#to-set).

## Dimension of a convex polytope

The dimension of a convex polytope
$P \subseteq \mathbb{R}^n$ is its affine dimension: the dimension of the real vector space
spanned by the differences $x - y$ of points $x, y \in P$.

Formalized by `MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope.dim`, a definition declared in [WantedExt/Geometry/PlatonicClassificationWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PlatonicClassificationWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#dim).

## Full-dimensional convex polytope

A convex polytope $P \subseteq \mathbb{R}^n$ is
full-dimensional if its dimension equals $n$.

Formalized by `MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope.IsFullDim`, a definition declared in [WantedExt/Geometry/PlatonicClassificationWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PlatonicClassificationWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#is-full-dim).

## Face of a convex polytope

A face of a convex polytope $P \subseteq \mathbb{R}^n$ is a
nonempty set of the form $\{x \in P : \ell(y) \le \ell(x) \text{ for all } y \in P\}$ for some
linear functional $\ell$ on $\mathbb{R}^n$, that is, the set of points where $\ell$ attains its
maximum over $P$. Taking $\ell = 0$ shows that $P$ itself is a face.

Formalized by `MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope.IsFace`, a definition declared in [WantedExt/Geometry/PlatonicClassificationWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PlatonicClassificationWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#is-face).

## Affine dimension of a set

For a subset $F \subseteq \mathbb{R}^n$, its affine dimension is
the dimension of the real vector space spanned by the differences $x - y$ with $x, y \in F$.
The empty set and every single point get dimension $0$.

Formalized by `MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope.faceDim`, a definition declared in [WantedExt/Geometry/PlatonicClassificationWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PlatonicClassificationWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#face-dim).

## Flag of a convex polytope

A flag of a convex polytope $P \subseteq \mathbb{R}^n$ is a
sequence $F_0, F_1, \dots, F_{n-1}$ of faces of $P$ such that each $F_k$ has affine dimension $k$
and $F_i \subsetneq F_j$ whenever $i < j$.

The definition applies to every $P$; it is used for full-dimensional $P$.

Formalized by `MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope.Flag`, a structure declared in [WantedExt/Geometry/PlatonicClassificationWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PlatonicClassificationWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#flag).

## Rigid motions

The rigid motions of $\mathbb{R}^n$ are the affine isometric bijections
$\mathbb{R}^n \to \mathbb{R}^n$.

Formalized by `MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope.Isom`, an abbreviation declared in [WantedExt/Geometry/PlatonicClassificationWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PlatonicClassificationWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#isom).

## Symmetry of a convex polytope

An affine isometry $\varphi$ of $\mathbb{R}^n$ is a
symmetry of a convex polytope $P \subseteq \mathbb{R}^n$ if $\varphi(P) = P$.

Formalized by `MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope.isSymmetry`, a definition declared in [WantedExt/Geometry/PlatonicClassificationWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PlatonicClassificationWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#is-symmetry).

## Regular convex polytope

A convex polytope $P \subseteq \mathbb{R}^n$ is regular
(Platonic) if it is full-dimensional and for any two flags $(F_0, \dots, F_{n-1})$ and
$(G_0, \dots, G_{n-1})$ of $P$ there is an affine isometry $\varphi$ of $\mathbb{R}^n$ with
$\varphi(P) = P$ and $\varphi(F_k) = G_k$ for every $k < n$.

Formalized by `MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope.IsRegular`, a definition declared in [WantedExt/Geometry/PlatonicClassificationWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PlatonicClassificationWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#is-regular).

## Similar polytopes

Two convex polytopes $P$ and $Q$ in $\mathbb{R}^n$ are **similar** when
there are a real number $a > 0$ and an affine isometry $\varphi$ of $\mathbb{R}^n$ such that the
underlying set of $Q$ is $\{a\,\varphi(x) : x \in P\}$.

Formalized by `MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.ConvexPolytope.Similar`, a definition declared in [WantedExt/Geometry/PlatonicClassificationWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PlatonicClassificationWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#similar).

## Regular polytopes

For $d \in \mathbb{N}$, this is the set of regular (Platonic) convex
polytopes in $\mathbb{R}^d$: the convex polytopes in $\mathbb{R}^d$ that are full-dimensional and
whose symmetry group acts transitively on their flags.

Formalized by `MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.regularPolytopes`, a definition declared in [WantedExt/Geometry/PlatonicClassificationWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PlatonicClassificationWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#regular-polytopes).

## Similarity of regular polytopes

For regular convex polytopes $P$ and $Q$ in
$\mathbb{R}^d$, $P$ is related to $Q$ when they are similar as convex polytopes, that is, when
there are a real number $a > 0$ and an affine isometry $\varphi$ of $\mathbb{R}^d$ such that the
underlying set of $Q$ is $\{a\,\varphi(x) : x \in P\}$.

Formalized by `MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.regularSimilar`, a definition declared in [WantedExt/Geometry/PlatonicClassificationWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PlatonicClassificationWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#regular-similar).

## Number of Platonic polytopes

For $d \in \mathbb{N}$, $p_d \in \mathbb{N} \cup \{\infty\}$
is the number of similarity classes of regular convex polytopes in $\mathbb{R}^d$, with
$p_d = \infty$ when there are infinitely many classes.

Formalized by `MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.platonicCount`, a definition declared in [WantedExt/Geometry/PlatonicClassificationWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PlatonicClassificationWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#platonic-count).

## Classification of the Platonic polytopes

For $d \in \mathbb{N}$ let $p_d \in
\mathbb{N} \cup \{\infty\}$ be the number of regular convex polytopes in $\mathbb{R}^d$ up to
similarity. Then $p_2 = \infty$, $p_3 = 5$, $p_4 = 6$, and $p_d = 3$ for every $d \ge 5$.

## Sources

- Euclid, Elements, Book XIII (~300 BC, p_3 = 5); L. Schläfli, Theorie der vielfachen Kontinuität (1852, posthumous publication; p_4 = 6, p_d = 3 for d ≥ 5). Listed as §42 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `platonic_classification` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.PlatonicClassificationWanted.Geometry.PlatonicClassification.platonic_classification` is written with `theorem_wanted` in [WantedExt/Geometry/PlatonicClassificationWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/PlatonicClassificationWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html#platonic-classification).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Platonic solids and regular polytopes](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/discrete-geometry/part-01/platonic-solids-and-regular-polytopes)
