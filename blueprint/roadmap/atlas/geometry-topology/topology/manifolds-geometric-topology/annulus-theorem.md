---
declaration: section
origin: cited
lean: MathlibExt.Topology.AnnulusShared.Amb, MathlibExt.Topology.AnnulusShared.Sph, MathlibExt.Topology.AnnulusShared.modelHyperplane, MathlibExt.Topology.AnnulusShared.LocallyFlat, MathlibExt.Topology.AnnulusShared.FlatSphere, MathlibExt.Topology.AnnulusShared.inside, MathlibExt.Topology.AnnulusShared.regionBetween, MathlibExt.Topology.AnnulusTheoremDimFourWanted.Topology.annulus_theorem_dim_four
statement: formalized
---

# Annulus theorem

9 results, 7 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/annulus-theorem/index.html).

## Ambient Euclidean space

For a natural number $n$, the ambient space is the real
Euclidean space $\mathbb{R}^n$ of dimension $n$, with coordinates indexed by $0, \dots, n-1$ and
the Euclidean norm.

Formalized by `MathlibExt.Topology.AnnulusShared.Amb`, an abbreviation declared in [WantedExt/Topology/AnnulusShared.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/AnnulusShared.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/annulus-theorem/index.html#amb).

## Unit sphere in Euclidean space

For a natural number $n$, the unit sphere
$S^{n-1} \subseteq \mathbb{R}^n$ is the set of points of $\mathbb{R}^n$ at Euclidean distance $1$
from the origin.

Formalized by `MathlibExt.Topology.AnnulusShared.Sph`, an abbreviation declared in [WantedExt/Topology/AnnulusShared.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/AnnulusShared.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/annulus-theorem/index.html#sph).

## Model hyperplane

For $n \ge 1$, the model hyperplane in $\mathbb{R}^n$ is the set of
points $x = (x_0, \dots, x_{n-1})$ whose first coordinate $x_0$ is $0$. It is the local model for
a locally flat embedded sphere.

Formalized by `MathlibExt.Topology.AnnulusShared.modelHyperplane`, a definition declared in [WantedExt/Topology/AnnulusShared.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/AnnulusShared.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/annulus-theorem/index.html#model-hyperplane).

## Locally flat maps of the sphere

Let $n \ge 1$, let $S^{n-1} \subseteq \mathbb{R}^n$ be the
unit sphere and let $H = \{x \in \mathbb{R}^n : x_0 = 0\}$ be the model hyperplane. A map
$c : S^{n-1} \to \mathbb{R}^n$ is locally flat if for every point $p \in S^{n-1}$ there are open
sets $U, V \subseteq \mathbb{R}^n$ with $c(p) \in U$ and a homeomorphism $h : U \to V$ such that
$h(U \cap c(S^{n-1})) = V \cap H$.

Formalized by `MathlibExt.Topology.AnnulusShared.LocallyFlat`, a definition declared in [WantedExt/Topology/AnnulusShared.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/AnnulusShared.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/annulus-theorem/index.html#locally-flat).

## Locally flat embedded sphere

For $n \ge 1$, a locally flat embedded $(n-1)$-sphere in
$\mathbb{R}^n$ is a map $f : S^{n-1} \to \mathbb{R}^n$ from the unit sphere that is continuous,
injective and locally flat.

Formalized by `MathlibExt.Topology.AnnulusShared.FlatSphere`, a structure declared in [WantedExt/Topology/AnnulusShared.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/AnnulusShared.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/annulus-theorem/index.html#flat-sphere).

## Inside of a set

For a set $S \subseteq \mathbb{R}^n$, the inside of $S$ is the set of
points $x \notin S$ whose connected component in the complement $\mathbb{R}^n \setminus S$ is
bounded.

For the image of a locally flat embedded sphere, this is the open ball it bounds.

Formalized by `MathlibExt.Topology.AnnulusShared.inside`, a definition declared in [WantedExt/Topology/AnnulusShared.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/AnnulusShared.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/annulus-theorem/index.html#inside).

## Region between two flat spheres

Let $n \ge 1$ and let $f$ and $g$ be locally flat
embedded $(n-1)$-spheres in $\mathbb{R}^n$. The region between $f$ and $g$ is the closure of the
inside of the image of $f$ with the inside of the image of $g$ removed, where the inside of a set
$S$ is the set of points $x \notin S$ whose connected component in $\mathbb{R}^n \setminus S$ is
bounded.

Formalized by `MathlibExt.Topology.AnnulusShared.regionBetween`, a definition declared in [WantedExt/Topology/AnnulusShared.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/AnnulusShared.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/annulus-theorem/index.html#region-between).

## Annulus theorem in dimension four

Let $f$ and $g$ be locally flat embedded $3$-spheres
in $\mathbb{R}^4$, that is, continuous injective locally flat maps $S^3 \to \mathbb{R}^4$ from the
unit sphere. Suppose that the images of $f$ and $g$ are disjoint and that the image of $g$ lies
in the inside of the image of $f$, the set of points off the image of $f$ whose connected
component in its complement is bounded. Then the region between $f$ and $g$, the closure of the
inside of the image of $f$ minus the inside of the image of $g$, is homeomorphic to
$S^3 \times [0, 1]$.

## Sources

- F. Quinn, *Ends of maps III: dimensions 4 and 5*, J. Differential Geom. 17 (1982), building on M. H. Freedman, *The topology of four-dimensional manifolds*, J. Differential Geom. 17 (1982). Problem `annulus_theorem_dim_four` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.AnnulusTheoremDimFourWanted.Topology.annulus_theorem_dim_four` is written with `theorem_wanted` in [WantedExt/Topology/AnnulusTheoremDimFourWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/AnnulusTheoremDimFourWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/annulus-theorem/index.html#annulus-theorem-dim-four).

## Annulus theorem in dimensions at least five

Let $n \ge 5$ and let $f$ and $g$ be locally
flat embedded $(n-1)$-spheres in $\mathbb{R}^n$, that is, continuous injective locally flat maps
$S^{n-1} \to \mathbb{R}^n$ from the unit sphere. Suppose that the images of $f$ and $g$ are
disjoint and that the image of $g$ lies in the inside of the image of $f$, the set of points off
the image of $f$ whose connected component in its complement is bounded. Then the region between
$f$ and $g$, the closure of the inside of the image of $f$ minus the inside of the image of $g$,
is homeomorphic to $S^{n-1} \times [0, 1]$.

## Sources

- R. C. Kirby, *Stable homeomorphisms and the annulus conjecture*, Ann. of Math. 89 (1969). Problem `annulus_theorem_high_dim` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.AnnulusTheoremHighDimWanted.Topology.annulus_theorem_high_dim` is written with `theorem_wanted` in [WantedExt/Topology/AnnulusTheoremHighDimWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/AnnulusTheoremHighDimWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/annulus-theorem/index.html#annulus-theorem-high-dim).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Annulus theorem](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/annulus-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/manifolds-geometric-topology/annulus-theorem)
