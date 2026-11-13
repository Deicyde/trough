---
declaration: section
origin: cited
lean: MathlibExt.Topology.ClassificationOfSurfacesWanted.Complex.ClosedUnitDisc, MathlibExt.Topology.ClassificationOfSurfacesWanted.Complex.ClosedUnitDisc.bdyPtOfReal, MathlibExt.Topology.ClassificationOfSurfacesWanted.Topology.ClassificationOfSurfaces.OrientableRel, MathlibExt.Topology.ClassificationOfSurfacesWanted.Topology.ClassificationOfSurfaces.NonOrientableRel, MathlibExt.Topology.ClassificationOfSurfacesWanted.Topology.ClassificationOfSurfaces.classification_of_surfaces
statement: formalized
---

# Classification of surfaces

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/classification-of-surfaces/index.html).

## The closed unit disc

## Closed unit disc in the complex plane

The closed unit disc in the complex plane.

Formalized by `MathlibExt.Topology.ClassificationOfSurfacesWanted.Complex.ClosedUnitDisc`, an abbreviation declared in [WantedExt/Topology/ClassificationOfSurfacesWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ClassificationOfSurfacesWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/classification-of-surfaces/index.html#closed-unit-disc).

## Boundary point of the unit disc at a real parameter

For a real number $r$, this is the
point $e^{2\pi i r}$ of the closed unit disc in $\mathbb{C}$, which lies on its boundary circle.

Formalized by `MathlibExt.Topology.ClassificationOfSurfacesWanted.Complex.ClosedUnitDisc.bdyPtOfReal`, a definition declared in [WantedExt/Topology/ClassificationOfSurfacesWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ClassificationOfSurfacesWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/classification-of-surfaces/index.html#bdy-pt-of-real).

## Gluing relation for the orientable normal form

For natural numbers $p$ and $n$, put
$N = 4p + 3n$ and write $e(t) = e^{2\pi i t}$ for the boundary point of the closed unit disc at
the real parameter $t$. This is the relation on the closed unit disc under which, for every
$x \in [0, 1]$ and every natural number $k < p$, the point $e((4k + x)/N)$ is related to
$e((4k + 3 - x)/N)$ and the point $e((4k + 1 + x)/N)$ is related to $e((4k + 4 - x)/N)$, and
for every $x \in [0, 1]$ and every natural number $k < n$, the point $e(-(3k + x)/N)$ is related
to $e(-(3k + 3 - x)/N)$; no other pairs are related.

Gluing the disc along it identifies the boundary in the pattern $a_1 b_1 a_1^{-1} b_1^{-1}
\cdots a_p b_p a_p^{-1} b_p^{-1} c_1 h_1 c_1^{-1} \cdots c_n h_n c_n^{-1}$, where the arcs $h_j$
are left free.

Formalized by `MathlibExt.Topology.ClassificationOfSurfacesWanted.Topology.ClassificationOfSurfaces.OrientableRel`, an inductive type declared in [WantedExt/Topology/ClassificationOfSurfacesWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ClassificationOfSurfacesWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/classification-of-surfaces/index.html#orientable-rel).

## Gluing relation for the non-orientable normal form

For natural numbers $p$ and $n$, put
$N = 2p + 3n$ and write $e(t) = e^{2\pi i t}$ for the boundary point of the closed unit disc at
the real parameter $t$. This is the relation on the closed unit disc under which, for every
$x \in [0, 1]$ and every natural number $k < p$, the point $e((2k + x)/N)$ is related to
$e((2k + 1 + x)/N)$, and for every $x \in [0, 1]$ and every natural number $k < n$, the point
$e(-(3k + x)/N)$ is related to $e(-(3k + 3 - x)/N)$; no other pairs are related.

Gluing the disc along it identifies the boundary in the pattern
$a_1 a_1 \cdots a_p a_p c_1 h_1 c_1^{-1} \cdots c_n h_n c_n^{-1}$, where the arcs $h_j$ are left
free.

Formalized by `MathlibExt.Topology.ClassificationOfSurfacesWanted.Topology.ClassificationOfSurfaces.NonOrientableRel`, an inductive type declared in [WantedExt/Topology/ClassificationOfSurfacesWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ClassificationOfSurfacesWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/classification-of-surfaces/index.html#non-orientable-rel).

## Classification of compact surfaces

Let $S$ be a nonempty, compact, connected Hausdorff
space that is a topological manifold of dimension $2$ with boundary, with charts in the closed
half-plane $\{x \in \mathbb{R}^2 : x_1 \ge 0\}$. Then $S$ is homeomorphic to the unit sphere in
$\mathbb{R}^3$, or there are natural numbers $p$ and $n$ for which one of the following holds:
$p \ge 1$ or $n \ge 1$, and $S$ is homeomorphic to the quotient of the closed unit disc by the
orientable gluing relation with parameters $p$ and $n$; or $p \ge 1$, and $S$ is homeomorphic to
the quotient of the closed unit disc by the non-orientable gluing relation with parameters $p$
and $n$. Each quotient is taken by the equivalence relation that the gluing relation generates,
with the quotient topology.

## Sources

- Jean Gallier & Dianna Xu, *A Guide to the Classification Theorem for Compact Surfaces*, https://www.cis.upenn.edu/~jean/surfclassif-root.pdf. Problem `topological_classification_of_surfaces` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.ClassificationOfSurfacesWanted.Topology.ClassificationOfSurfaces.classification_of_surfaces` is written with `theorem_wanted` in [WantedExt/Topology/ClassificationOfSurfacesWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ClassificationOfSurfacesWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/classification-of-surfaces/index.html#classification-of-surfaces).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Classification of surfaces](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/classification-of-surfaces/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/manifolds-geometric-topology/classification-of-surfaces)
