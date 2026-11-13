---
declaration: section
origin: cited
lean: MathlibExt.Topology.FamiliesOfMapsB01Wanted.FamiliesOfMapsB01.Supported, MathlibExt.Topology.FamiliesOfMapsB01Wanted.FamiliesOfMapsB01.AdaptedTo, MathlibExt.Topology.FamiliesOfMapsB01Wanted.FamiliesOfMapsB01.IsPolyhedron, MathlibExt.Topology.FamiliesOfMapsB01Wanted.FamiliesOfMapsB01.Subdivision, MathlibExt.Topology.FamiliesOfMapsB01Wanted.FamiliesOfMapsB01.closedCell, MathlibExt.Topology.FamiliesOfMapsB01Wanted.FamiliesOfMapsB01.IsBoundarySubpolyhedron, MathlibExt.Topology.FamiliesOfMapsB01Wanted.FamiliesOfMapsB01.continuous, MathlibExt.Topology.FamiliesOfMapsB01Wanted.FamiliesOfMapsB01.biLipschitz
statement: formalized
---

# Adapting families of maps to open covers

8 results, 6 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/adapting-families-of-maps-to-open-covers/index.html).

## Families of maps supported on a set

Let $X$ and $T$ be topological spaces and $P$ a set. A
family of maps $f : P \times X \to T$ is supported on a set $S \subseteq X$ when it does not depend
on the parameter outside $S$: $f(p, x) = f(p', x)$ for all $p, p' \in P$ and all $x \notin S$.

Formalized by `MathlibExt.Topology.FamiliesOfMapsB01Wanted.FamiliesOfMapsB01.Supported`, a definition declared in [WantedExt/Topology/FamiliesOfMapsB01Wanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/FamiliesOfMapsB01Wanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/adapting-families-of-maps-to-open-covers/index.html#supported).

## Adapted families of maps

Let $X$ and $T$ be topological spaces, $P$ a set,
$U = (U_\alpha)_{\alpha \in \iota}$ a family of subsets of $X$ and $k$ a natural number. A
family of maps $f : P \times X \to T$ is adapted to $U$ with bound $k$ when there is a finite
set $A$ of at most $k$ indices such that $f$ is supported on $\bigcup_{\alpha \in A} U_\alpha$.

Formalized by `MathlibExt.Topology.FamiliesOfMapsB01Wanted.FamiliesOfMapsB01.AdaptedTo`, a definition declared in [WantedExt/Topology/FamiliesOfMapsB01Wanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/FamiliesOfMapsB01Wanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/adapting-families-of-maps-to-open-covers/index.html#adapted-to).

## Convex linear polyhedra

A subset $P \subseteq \mathbb{R}^k$ is a convex linear polyhedron
when it is the convex hull of a finite set of points (equivalently, a bounded intersection of
finitely many closed half-spaces).

Formalized by `MathlibExt.Topology.FamiliesOfMapsB01Wanted.FamiliesOfMapsB01.IsPolyhedron`, a definition declared in [WantedExt/Topology/FamiliesOfMapsB01Wanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/FamiliesOfMapsB01Wanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/adapting-families-of-maps-to-open-covers/index.html#is-polyhedron).

## Polyhedral subdivisions

A polyhedral subdivision of a set $P \subseteq \mathbb{R}^k$ is a
geometric simplicial complex in $\mathbb{R}^k$ with finitely many faces whose underlying space
equals $P$.

Formalized by `MathlibExt.Topology.FamiliesOfMapsB01Wanted.FamiliesOfMapsB01.Subdivision`, a structure declared in [WantedExt/Topology/FamiliesOfMapsB01Wanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/FamiliesOfMapsB01Wanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/adapting-families-of-maps-to-open-covers/index.html#subdivision).

## Closed cells

Let $P \subseteq \mathbb{R}^k$ and let $D \subseteq \mathbb{R}^k$ be a finite
set (typically the vertex set of a face of a subdivision of $P$). The closed cell of $D$ in $P$ is
the set of points of $P$ that lie in the convex hull of $D$, viewed as a subset of $P$.

Formalized by `MathlibExt.Topology.FamiliesOfMapsB01Wanted.FamiliesOfMapsB01.closedCell`, a definition declared in [WantedExt/Topology/FamiliesOfMapsB01Wanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/FamiliesOfMapsB01Wanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/adapting-families-of-maps-to-open-covers/index.html#closed-cell).

## Boundary subpolyhedra

Let $P \subseteq \mathbb{R}^k$. A subset $Q \subseteq P$ is a
boundary subpolyhedron of $P$ when $Q$ is the convex hull of a finite set of points of
$\mathbb{R}^k$, $Q$ lies in the intrinsic frontier (relative boundary) of $P$, and $Q$ is a face of
$P$: whenever a point of $Q$ lies in the open segment between two points of $P$, both of those
points lie in $Q$.

The face condition matches the paper's "convex linear subpolyhedron of $\partial P$"; without it a
single non-vertex point of the boundary of $P$ would qualify.

Formalized by `MathlibExt.Topology.FamiliesOfMapsB01Wanted.FamiliesOfMapsB01.IsBoundarySubpolyhedron`, a definition declared in [WantedExt/Topology/FamiliesOfMapsB01Wanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/FamiliesOfMapsB01Wanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/adapting-families-of-maps-to-open-covers/index.html#is-boundary-subpolyhedron).

## Morrison–Walker lemma on adapting families of maps to an open cover

Let $X$ be a compact
topological space, $T$ a topological space, $P \subseteq \mathbb{R}^k$ a convex linear polyhedron,
$(U_\alpha)_{\alpha \in \iota}$ a family of open subsets of $X$, and $\rho$ a partition of unity on
$X$ indexed by $\iota$ and subordinate to $U$ (the closed support of $\rho_\alpha$ lies in
$U_\alpha$). Then for every continuous map $f : P \times X \to T$ there is a continuous map
$F : [0, 1] \times P \times X \to T$ such that: (i) $F(0, p, x) = f(p, x)$ for all $p \in P$ and
$x \in X$; (ii) there is a polyhedral subdivision $K$ of $P$ such that, for every facet (maximal
face) $D$ of $K$, the family $(p, x) \mapsto F(1, p, x)$ with $p$ in the closed cell of $D$ is
adapted to $U$ with bound $k$; (iii) for every $S \subseteq X$, if $f$ is supported on $S$, then
$F$, as a family with parameter $(t, p) \in [0, 1] \times P$, is supported on $S$; (iv) for every
boundary subpolyhedron $Q$ of $P$ and every $S' \subseteq X$, if the restriction of $f$ to
$Q \times X$ is supported on $S'$, then the restriction of $F$ to $[0, 1] \times Q \times X$, as a
family with parameter $(t, q) \in [0, 1] \times Q$, is supported on $S'$.

## Sources

- S. Morrison and K. Walker, *The Blob Complex*, arXiv:1009.5025, Appendix B, Lemma B.0.1 (pp. 93–96): https://arxiv.org/pdf/1009.5025. Problem `families_of_maps_b01` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.FamiliesOfMapsB01Wanted.FamiliesOfMapsB01.continuous` is written with `theorem_wanted` in [WantedExt/Topology/FamiliesOfMapsB01Wanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/FamiliesOfMapsB01Wanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/adapting-families-of-maps-to-open-covers/index.html#continuous).

## Morrison–Walker lemma on adapting families of maps, bi-Lipschitz case

Let $X$ be a
compact metric space, $T$ a metric space, $P \subseteq \mathbb{R}^k$ a convex linear polyhedron,
$(U_\alpha)_{\alpha \in \iota}$ a family of open subsets of $X$, and $\rho$ a partition of unity on
$X$ indexed by $\iota$ and subordinate to $U$. Let $f : P \times X \to T$ be continuous and suppose
that for each $p \in P$ the map $x \mapsto f(p, x)$ is a homeomorphism $h_p : X \to T$, and that for
some constant $L \ge 0$ the map $f$ is $L$-Lipschitz on $P \times X$ (for the sup metrics on
$\mathbb{R}^k$ and on $P \times X$) and every inverse $h_p^{-1}$ is $L$-Lipschitz. Then there are a
continuous map $F : [0, 1] \times P \times X \to T$, a constant $L' \ge 0$ and homeomorphisms
$H_{t,p} : X \to T$ for $(t, p) \in [0, 1] \times P$ such that: (i) $F(0, p, x) = f(p, x)$ for all
$p$ and $x$; (ii) $F(t, p, x) = H_{t,p}(x)$ for all $t$, $p$, $x$; (iii) there is a polyhedral
subdivision $K$ of $P$ such that, for every facet (maximal face) $D$ of $K$, the family
$(p, x) \mapsto F(1, p, x)$ with $p$ in the closed cell of $D$ is adapted to $U$ with bound $k$;
(iv) for every $S \subseteq X$, if $f$ is supported on $S$, then $F$, as a family with parameter
$(t, p) \in [0, 1] \times P$, is supported on $S$; (v) for every boundary subpolyhedron $Q$ of $P$
and every $S' \subseteq X$, if the restriction of $f$ to $Q \times X$ is supported on $S'$, then
the restriction of $F$ to $[0, 1] \times Q \times X$, as a family with parameter
$(t, q) \in [0, 1] \times Q$, is supported on $S'$; and (vi) every $H_{t,p}$ and every inverse
$H_{t,p}^{-1}$ is $L'$-Lipschitz.

## Sources

- S. Morrison and K. Walker, *The Blob Complex*, arXiv:1009.5025, Appendix B, Lemma B.0.1 (pp. 93–96): https://arxiv.org/pdf/1009.5025. Problem `families_of_maps_b01` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.FamiliesOfMapsB01Wanted.FamiliesOfMapsB01.biLipschitz` is written with `theorem_wanted` in [WantedExt/Topology/FamiliesOfMapsB01Wanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/FamiliesOfMapsB01Wanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/adapting-families-of-maps-to-open-covers/index.html#bi-lipschitz).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Adapting families of maps to open covers](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/adapting-families-of-maps-to-open-covers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/algebraic-topology/adapting-families-of-maps-to-open-covers)
