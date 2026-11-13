---
declaration: section
origin: cited
lean: LatticePointCubeSandwich.integerUnitCube, LatticePointCubeSandwich.mem_integerUnitCube_iff, LatticePointCubeSandwich.outerCubeSet, LatticePointCubeSandwich.mem_outerCubeSet_iff, LatticePointCubeSandwich.innerCubeSet, LatticePointCubeSandwich.mem_innerCubeSet_iff, LatticePointCubeSandwich.innerCubeSet_subset_outerCubeSet, LatticePointCubeSandwich.finite_outerCubeSet
statement: formalized
proof: formalized
---

# Lattice points in dilated regions

47 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html).

## Integer unit cube

For $v \in \mathbb{Z}^n$, the integer unit cube at $v$ is the half-open
cube $Q_v = \prod_i [v_i, v_i + 1) \subseteq \mathbb{R}^n$, the set of $x \in \mathbb{R}^n$ with
$v_i \le x_i < v_i + 1$ for every coordinate $i$.

Formalized by `LatticePointCubeSandwich.integerUnitCube`, a definition declared in [MathlibExt/Geometry/LatticePointCubeSandwich.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointCubeSandwich.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#integer-unit-cube).

## Membership in an integer unit cube

For $v \in \mathbb{Z}^n$ and $x \in \mathbb{R}^n$, $x$
lies in the integer unit cube at $v$ if and only if $v_i \le x_i < v_i + 1$ for every
coordinate $i$.

Formalized by `LatticePointCubeSandwich.mem_integerUnitCube_iff`, a theorem declared in [MathlibExt/Geometry/LatticePointCubeSandwich.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointCubeSandwich.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#mem-integer-unit-cube-iff).

## Outer cube set

For a set $S \subseteq \mathbb{R}^n$ and a real number $t$, the outer cube
set of $S$ at scale $t$ is the set of $v \in \mathbb{Z}^n$ such that
$(x_1/t, \dots, x_n/t) \in S$ for some $x$ in the integer unit cube
$Q_v = \prod_i [v_i, v_i + 1)$. For $t > 0$ these are the $v$ with $Q_v$ meeting $tS$; for $t = 0$
the division is read as $x_i/0 = 0$.

Formalized by `LatticePointCubeSandwich.outerCubeSet`, a definition declared in [MathlibExt/Geometry/LatticePointCubeSandwich.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointCubeSandwich.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#outer-cube-set).

## Membership in the outer cube set

For $S \subseteq \mathbb{R}^n$, $t \in \mathbb{R}$ and
$v \in \mathbb{Z}^n$, $v$ belongs to the outer cube set of $S$ at scale $t$ if and only if
$(x_1/t, \dots, x_n/t) \in S$ for some $x$ in the integer unit cube at $v$.

Formalized by `LatticePointCubeSandwich.mem_outerCubeSet_iff`, a theorem declared in [MathlibExt/Geometry/LatticePointCubeSandwich.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointCubeSandwich.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#mem-outer-cube-set-iff).

## Inner cube set

For a set $S \subseteq \mathbb{R}^n$ and a real number $t$, the inner cube
set of $S$ at scale $t$ is the set of $v \in \mathbb{Z}^n$ such that
$(x_1/t, \dots, x_n/t) \in S$ for every $x$ in the integer unit cube
$Q_v = \prod_i [v_i, v_i + 1)$. For $t > 0$ these are the $v$ with $Q_v \subseteq tS$; for $t = 0$
the division is read as $x_i/0 = 0$.

Formalized by `LatticePointCubeSandwich.innerCubeSet`, a definition declared in [MathlibExt/Geometry/LatticePointCubeSandwich.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointCubeSandwich.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#inner-cube-set).

## Membership in the inner cube set

For $S \subseteq \mathbb{R}^n$, $t \in \mathbb{R}$ and
$v \in \mathbb{Z}^n$, $v$ belongs to the inner cube set of $S$ at scale $t$ if and only if
$(x_1/t, \dots, x_n/t) \in S$ for every $x$ in the integer unit cube at $v$.

Formalized by `LatticePointCubeSandwich.mem_innerCubeSet_iff`, a theorem declared in [MathlibExt/Geometry/LatticePointCubeSandwich.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointCubeSandwich.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#mem-inner-cube-set-iff).

## Inner cube indices are outer cube indices

For every set $S \subseteq \mathbb{R}^n$ and
every real $t$, the inner cube set of $S$ at scale $t$ is contained in the outer cube set of $S$
at scale $t$.

Formalized by `LatticePointCubeSandwich.innerCubeSet_subset_outerCubeSet`, a theorem declared in [MathlibExt/Geometry/LatticePointCubeSandwich.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointCubeSandwich.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#inner-cube-set-subset-outer-cube-set).

## Finiteness of the outer cube set

If $S \subseteq \mathbb{R}^n$ is bounded and $t > 0$,
then the outer cube set of $S$ at scale $t$, the set of $v \in \mathbb{Z}^n$ whose integer unit
cube $\prod_i [v_i, v_i + 1)$ meets $tS$, is finite.

Formalized by `LatticePointCubeSandwich.finite_outerCubeSet`, a theorem declared in [MathlibExt/Geometry/LatticePointCubeSandwich.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointCubeSandwich.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#finite-outer-cube-set).

## Cubical measure sandwich

Let $S \subseteq \mathbb{R}^n$ be bounded, let $t > 0$, and let
$\mathrm{vol}(S)$ be the Lebesgue (outer) measure of $S$, which is finite. For
$v \in \mathbb{Z}^n$ let $Q_v = \prod_i [v_i, v_i + 1)$. Let $I$ be the inner cube set of $S$ at
scale $t$, the $v$ with $Q_v \subseteq tS$, and $O$ the outer cube set, the $v$ with $Q_v$
meeting $tS$. Then $|I| \le \mathrm{vol}(S)\, t^n \le |O|$.

Formalized by `LatticePointCubeSandwich.cube_measure_sandwich`, a theorem declared in [MathlibExt/Geometry/LatticePointCubeSandwich.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointCubeSandwich.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#cube-measure-sandwich).

## The standard integer lattice

For $d \in \mathbb{N}$, the standard integer lattice
$\mathbb{Z}^d$ is the $\mathbb{Z}$-submodule of $\mathbb{R}^d$ (the real-valued functions on
$\{0, \dots, d-1\}$) spanned by the standard basis vectors $e_0, \dots, e_{d-1}$.

Formalized by `LatticePointEnumerator.stdLattice`, a definition declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#std-lattice).

## Membership in the standard lattice

For a natural number $d$, a vector
$x \in \mathbb{R}^d$ lies in the standard lattice $\mathbb{Z}^d$, the integer span of the standard
basis vectors of $\mathbb{R}^d$, exactly when every coordinate $x_i$ of $x$ is an integer.

Formalized by `LatticePointEnumerator.mem_stdLattice_iff`, a theorem declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#mem-std-lattice-iff).

## Lattice points in a dilate

For a natural number $d$, a set $P \subseteq \mathbb{R}^d$
and a real number $t$, this is the set $(tP) \cap \mathbb{Z}^d$ of points of the integer lattice
$\mathbb{Z}^d$ in the dilate $tP = \{tp : p \in P\}$.

The source only uses this set for $t > 0$.

Formalized by `LatticePointEnumerator.latticePointSet`, a definition declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#lattice-point-set).

## Lattice-point count of a real dilate

For a natural number $d$, a set
$P \subseteq \mathbb{R}^d$ and a real number $t$, this is the number of elements of the set
$(tP) \cap \mathbb{Z}^d$ of points of the integer lattice $\mathbb{Z}^d$ in the dilate
$tP = \{tp : p \in P\}$, where an infinite set is assigned the value $0$.

For unbounded $P$ the set can be infinite, so the value $0$ is a convention and not a count;
the lattice-point enumerator for bounded $P$ and $t > 0$ is the faithful count.

Formalized by `LatticePointEnumerator.latticeEnumerator`, a definition declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#lattice-enumerator).

## Translated lattice-point set

For $d \in \mathbb{N}$, a set $P \subseteq \mathbb{R}^d$, a
real $t$ and $x \in \mathbb{R}^d$, the translated lattice-point set is
$((t \cdot P) + x) \cap \mathbb{Z}^d$, the set of points of the standard integer lattice
$\mathbb{Z}^d$ in the dilate $t \cdot P$ translated by $x$.

The dilation comes first: in general this set differs from $(t \cdot (P + x)) \cap \mathbb{Z}^d$.

## Sources

- Rocha-Neves, arXiv:2608.11078v1, lines 62-67.

Formalized by `LatticePointEnumerator.translatedLatticePointSet`, a definition declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#translated-lattice-point-set).

## Translated lattice-point count for arbitrary sets

For $d \in \mathbb{N}$, a set
$P \subseteq \mathbb{R}^d$, a real $t$ and $x \in \mathbb{R}^d$, the translated lattice-point
count is the number of elements of the translated lattice-point set
$((t \cdot P) + x) \cap \mathbb{Z}^d$, taken to be $0$ when this set is infinite.

Formalized by `LatticePointEnumerator.translatedLatticeEnumerator`, a definition declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#translated-lattice-enumerator).

## Lattice points in a positive dilate

For a natural number $d$, a set
$P \subseteq \mathbb{R}^d$ and a real number $t > 0$, this is the set $(tP) \cap \mathbb{Z}^d$ of
points of the integer lattice $\mathbb{Z}^d$ in the dilate $tP = \{tp : p \in P\}$.

No boundedness of $P$ is assumed.

Formalized by `LatticePointEnumerator.latticePointSetPos`, a definition declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#lattice-point-set-pos).

## Lattice-point enumerator

For a natural number $d$, a bounded set
$P \subseteq \mathbb{R}^d$ and a real number $t > 0$, the lattice-point enumerator $L_P(t)$ is
the number of points of the integer lattice $\mathbb{Z}^d$ in the dilate
$tP = \{tp : p \in P\}$, that is, $L_P(t) = |(tP) \cap \mathbb{Z}^d|$.

Since $P$ is bounded, the set $(tP) \cap \mathbb{Z}^d$ is finite, so $L_P(t)$ is its actual
number of elements.

## Sources

- Rocha-Neves, A Fourier-analytic Uniqueness Theorem for Lattice-point Enumerators, arXiv:2608.11078v1, lines 24-31.

Formalized by `LatticePointEnumerator.latticeEnumeratorPos`, a definition declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#lattice-enumerator-pos).

## Translated lattice-point set at a positive dilation

For $d \in \mathbb{N}$, a set
$P \subseteq \mathbb{R}^d$, a real $t > 0$ and $x \in \mathbb{R}^d$, this is the set
$((t \cdot P) + x) \cap \mathbb{Z}^d$ of points of the standard integer lattice $\mathbb{Z}^d$
in the dilate $t \cdot P$ translated by $x$. No boundedness of $P$ is assumed.

Formalized by `LatticePointEnumerator.translatedLatticePointSetPos`, a definition declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#translated-lattice-point-set-pos).

## Translated lattice-point enumerator of a bounded set

Let $d \in \mathbb{N}$, let
$P \subseteq \mathbb{R}^d$ be a bounded set, let $t > 0$ be real and let $x \in \mathbb{R}^d$. The
translated lattice-point enumerator is $F_{t,P}(x) = |((t \cdot P) + x) \cap \mathbb{Z}^d|$, the
number of points of the standard integer lattice $\mathbb{Z}^d$ in the dilate $t \cdot P$
translated by $x$.

## Sources

- Rocha-Neves, arXiv:2608.11078v1, lines 62-67.

Formalized by `LatticePointEnumerator.translatedLatticeEnumeratorPos`, a definition declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#translated-lattice-enumerator-pos).

## The origin is a lattice point

For every $d \in \mathbb{N}$, the origin of $\mathbb{R}^d$
lies in the standard integer lattice $\mathbb{Z}^d$.

Formalized by `LatticePointEnumerator.zero_mem_stdLattice`, a theorem declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#zero-mem-std-lattice).

## The lattice-point count of the empty set vanishes

For every natural number $d$ and every
real number $t$, the lattice-point count of the empty set $\emptyset \subseteq \mathbb{R}^d$ at the
dilate $t$ is $0$.

Formalized by `LatticePointEnumerator.latticeEnumerator_empty`, a theorem declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#lattice-enumerator-empty).

## The translated lattice-point count of the empty set is zero

For every $d \in \mathbb{N}$,
every real $t$ and every $x \in \mathbb{R}^d$, the translated lattice-point count
$|((t \cdot \emptyset) + x) \cap \mathbb{Z}^d|$ is $0$.

Formalized by `LatticePointEnumerator.translatedLatticeEnumerator_empty`, a theorem declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#translated-lattice-enumerator-empty).

## Finiteness of the lattice points in a dilate

For a natural number $d$, a bounded set
$P \subseteq \mathbb{R}^d$ and any real number $t$, the set $(tP) \cap \mathbb{Z}^d$ of points of
the integer lattice $\mathbb{Z}^d$ in the dilate $tP = \{tp : p \in P\}$ is finite.

No positivity of $t$ is needed.

Formalized by `LatticePointEnumerator.finite_latticePointSet`, a theorem declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#finite-lattice-point-set).

## Finiteness of the lattice points in a positive dilate

For a natural number $d$, a
bounded set $P \subseteq \mathbb{R}^d$ and a real number $t > 0$, the set $(tP) \cap \mathbb{Z}^d$
of points of the integer lattice $\mathbb{Z}^d$ in the dilate $tP = \{tp : p \in P\}$ is
finite.

Formalized by `LatticePointEnumerator.finite_latticePointSetPos`, a theorem declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#finite-lattice-point-set-pos).

## Finiteness of the lattice points in a translated dilate

For a natural number $d$, a
bounded set $P \subseteq \mathbb{R}^d$, any real number $t$ and a vector $x \in \mathbb{R}^d$,
the set $(tP + x) \cap \mathbb{Z}^d$ of points of the integer lattice $\mathbb{Z}^d$ in the
translated dilate $tP + x = \{tp + x : p \in P\}$ is finite.

Formalized by `LatticePointEnumerator.finite_translatedLatticePointSet`, a theorem declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#finite-translated-lattice-point-set).

## Finiteness of the lattice points in a translated positive dilate

For a natural number
$d$, a bounded set $P \subseteq \mathbb{R}^d$, a real number $t > 0$ and a vector
$x \in \mathbb{R}^d$, the set $(tP + x) \cap \mathbb{Z}^d$ of points of the integer lattice
$\mathbb{Z}^d$ in the translated dilate $tP + x = \{tp + x : p \in P\}$ is finite.

Formalized by `LatticePointEnumerator.finite_translatedLatticePointSetPos`, a theorem declared in [MathlibExt/Geometry/LatticePointEnumerator.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointEnumerator.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#finite-translated-lattice-point-set-pos).

## The unit cube

For a natural number $d$, the closed unit cube $[0, 1]^d$ is the set of
points $x \in \mathbb{R}^d$ with $0 \le x_i \le 1$ for every coordinate $i$.

Formalized by `unitCube`, a definition declared in [MathlibExt/Topology/MetricSpace/LipschitzParametrizable.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/MetricSpace/LipschitzParametrizable.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#unit-cube).

## Lipschitz parametrizable sets

Let $X$ be a metric space and $d$ a natural number. A set
$B \subseteq X$ is $d$-Lipschitz parametrizable if there are a natural number $n$ (possibly $0$)
and Lipschitz maps $f_1, \dots, f_n : [0, 1]^d \to X$ out of the closed unit cube
$[0, 1]^d \subseteq \mathbb{R}^d$ such that $B$ equals the union of their images,
$B = f_1([0, 1]^d) \cup \dots \cup f_n([0, 1]^d)$.

Formalized by `IsLipschitzParametrizable`, a definition declared in [MathlibExt/Topology/MetricSpace/LipschitzParametrizable.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/MetricSpace/LipschitzParametrizable.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#is-lipschitz-parametrizable).

## The origin lies in the unit cube

For every natural number $d$, the origin of
$\mathbb{R}^d$ lies in the closed unit cube $[0, 1]^d$.

Formalized by `unitCube_zero_mem`, a theorem declared in [MathlibExt/Topology/MetricSpace/LipschitzParametrizable.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/MetricSpace/LipschitzParametrizable.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#unit-cube-zero-mem).

## The empty set is Lipschitz parametrizable

Let $X$ be a metric space. For every natural
number $d$, the empty subset of $X$ is $d$-Lipschitz parametrizable, via the empty family of
maps.

Formalized by `isLipschitzParametrizable_empty`, a theorem declared in [MathlibExt/Topology/MetricSpace/LipschitzParametrizable.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/MetricSpace/LipschitzParametrizable.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#is-lipschitz-parametrizable-empty).

## Singletons are Lipschitz parametrizable

Let $X$ be a metric space. For every natural
number $d$ and every point $x \in X$, the set $\lbrace x \rbrace$ is $d$-Lipschitz parametrizable,
via a single constant map.

Formalized by `isLipschitzParametrizable_singleton`, a theorem declared in [MathlibExt/Topology/MetricSpace/LipschitzParametrizable.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/MetricSpace/LipschitzParametrizable.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#is-lipschitz-parametrizable-singleton).

## Finsets are Lipschitz parametrizable

Let $X$ be a metric space and $d$ a natural number.
Every finite set $s$ of points of $X$, given as a finset, is $d$-Lipschitz parametrizable.

Formalized by `Finset.isLipschitzParametrizable_coe`, a theorem declared in [MathlibExt/Topology/MetricSpace/LipschitzParametrizable.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/MetricSpace/LipschitzParametrizable.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#is-lipschitz-parametrizable-coe).

## Finite sets are Lipschitz parametrizable

Let $X$ be a metric space. Every finite set
$B \subseteq X$ is $d$-Lipschitz parametrizable for every natural number $d$.

Formalized by `Set.Finite.isLipschitzParametrizable`, a theorem declared in [MathlibExt/Topology/MetricSpace/LipschitzParametrizable.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/MetricSpace/LipschitzParametrizable.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#is-lipschitz-parametrizable-2).

## Lipschitz images of Lipschitz parametrizable sets

Let $X$ and $Y$ be metric spaces,
let $d$ be a natural number and let $f : X \to Y$ be a Lipschitz map. If a set $B \subseteq X$ is
$d$-Lipschitz parametrizable, then its image $f(B) \subseteq Y$ is $d$-Lipschitz parametrizable.

Formalized by `IsLipschitzParametrizable.image_lipschitzWith`, a theorem declared in [MathlibExt/Topology/MetricSpace/LipschitzParametrizable.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/MetricSpace/LipschitzParametrizable.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#image-lipschitz-with).

## Integer cube set

Let $f$ be a map from the unit cube $[0, 1]^d$ to $\mathbb{R}^n$ and let
$t$ be a real number. The integer cube set of $f$ at scale $t$ is the set of integer vectors
$v \in \mathbb{Z}^n$ for which some point $y$ of the unit cube satisfies
$v_i \le t f(y)_i < v_i + 1$ for every coordinate $i$, that is, the set of integer vectors whose
half-open unit cube $\prod_i [v_i, v_i + 1)$ meets the dilate $t \cdot f([0, 1]^d)$.

Formalized by `LipschitzImageCubeCount.integerCubeSet`, a definition declared in [MathlibExt/Geometry/LipschitzImageCubeCount.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LipschitzImageCubeCount.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#integer-cube-set).

## Membership in the integer cube set

Let $f$ be a map from the unit cube $[0, 1]^d$ to
$\mathbb{R}^n$, let $t$ be a real number and let $v \in \mathbb{Z}^n$. Then $v$ belongs to the
integer cube set of $f$ at scale $t$ if and only if some point $y$ of the unit cube satisfies
$v_i \le t f(y)_i < v_i + 1$ for every coordinate $i$.

Formalized by `LipschitzImageCubeCount.mem_integerCubeSet_iff`, a theorem declared in [MathlibExt/Geometry/LipschitzImageCubeCount.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LipschitzImageCubeCount.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#mem-integer-cube-set-iff).

## Floor differences are bounded by a ceiling

For real numbers $a$, $b$ and $D$ with
$|a - b| \le D$, the integers $\lfloor a \rfloor$ and $\lfloor b \rfloor$ satisfy
$|\lfloor a \rfloor - \lfloor b \rfloor| \le \lceil D \rceil$.

Formalized by `LipschitzImageCubeCount.abs_floor_sub_le_ceil`, a theorem declared in [MathlibExt/Geometry/LipschitzImageCubeCount.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LipschitzImageCubeCount.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#abs-floor-sub-le-ceil).

## Dilated Lipschitz maps vary by at most $K$ on cells of size $1/T$

Let $K \ge 0$, let $f$
be a $K$-Lipschitz map from the unit cube $[0, 1]^d$ to $\mathbb{R}^n$, both carrying the sup
distance, and let $t$ and $T$ be real numbers with $0 < t \le T$. If $y$ and $y'$ are points of
the unit cube at distance at most $1/T$, then $|t f(y)_i - t f(y')_i| \le K$ for every coordinate
$i$.

Formalized by `LipschitzImageCubeCount.scaled_coord_abs_le`, a theorem declared in [MathlibExt/Geometry/LipschitzImageCubeCount.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LipschitzImageCubeCount.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#scaled-coord-abs-le).

## Counting integer cubes met by a dilated Lipschitz image

Let $d$ and $n$ be natural
numbers, let $K \ge 0$, and let $f$ be a $K$-Lipschitz map from the unit cube $[0, 1]^d$ to
$\mathbb{R}^n$, both carrying the sup distance. For every real $t \ge 1$, the cardinality of the
integer cube set of $f$ at scale $t$, taken as a natural number, is at most
$\lceil t \rceil^d \, (2 \lceil K \sqrt{d} \rceil + 3)^n$.

The proof puts $T = \lceil t \rceil$, partitions the cube into $T^d$ cells with lower-corner
representatives, bounds every floor-coordinate offset from the representative by
$L = \lceil K \sqrt{d} \rceil$, and encodes each met integer cube injectively by its cell and an
offset in $\{0, \dots, 2L + 2\}^n$.

Formalized by `LipschitzImageCubeCount.card_integerCubeSet_le`, a theorem declared in [MathlibExt/Geometry/LipschitzImageCubeCount.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LipschitzImageCubeCount.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#card-integer-cube-set-le).

## Dilated Lipschitz images meet finitely many integer cubes

Let $d$ and $n$ be natural
numbers, let $K \ge 0$, and let $f$ be a $K$-Lipschitz map from the unit cube $[0, 1]^d$ to
$\mathbb{R}^n$, both carrying the sup distance. For every real $t \ge 1$, the integer cube set of
$f$ at scale $t$ is finite.

The image of $f$ is bounded, since each coordinate of $f(y)$ differs from the corresponding
coordinate of $f(0)$ by at most $K \sqrt{d}$, so every met cube index lies in an explicit
finite box.

Formalized by `LipschitzImageCubeCount.finite_integerCubeSet`, a theorem declared in [MathlibExt/Geometry/LipschitzImageCubeCount.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LipschitzImageCubeCount.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#finite-integer-cube-set).

## Dilated Lipschitz images meet $O(t^d)$ integer cubes

Let $d$ and $n$ be natural numbers,
let $K \ge 0$, and let $f$ be a $K$-Lipschitz map from the unit cube $[0, 1]^d$ to $\mathbb{R}^n$,
both carrying the sup distance. Then there is a real number $C > 0$ such that for every real
$t \ge 1$, the cardinality of the integer cube set of $f$ at scale $t$, taken as a natural number,
is at most $C t^d$.

The proof takes $C = 2^d M^n$ with $M = 2 \lceil K \sqrt{d} \rceil + 3$, which depends on $f$ only
through $K$, and on $n$ and $d$, but not on $t$; it uses $\lceil t \rceil \le 2t$ for $t \ge 1$.

Formalized by `LipschitzImageCubeCount.exists_cubeCount_le_const_mul_pow`, a theorem declared in [MathlibExt/Geometry/LipschitzImageCubeCount.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LipschitzImageCubeCount.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#exists-cube-count-le-const-mul-pow).

## Boundary cubes meet the dilated frontier charts

Let $S \subseteq \mathbb{R}^n$, let
$f_1, \dots, f_m : [0,1]^d \to \mathbb{R}^n$ be maps whose ranges together cover the frontier of
$S$, and let $t$ be a real number. For $v \in \mathbb{Z}^n$ write $Q_v$ for the half-open unit
cube $\prod_i [v_i, v_i + 1)$. If $v$ lies in the outer cube set of $S$ at scale $t$ (some
$x \in Q_v$ has $x / t \in S$, coordinatewise, with $x / 0 = 0$) but not in the inner cube set
(not every $x \in Q_v$ has $x / t \in S$), then $v$ lies in the integer cube set of some $f_i$ at
scale $t$: there is $y \in [0,1]^d$ with $t f_i(y) \in Q_v$.

Formalized by `LatticePointBoundaryCubes.outer_diff_inner_subset_iUnion_integerCubeSet`, a theorem declared in [MathlibExt/Geometry/LatticePointBoundaryCubes.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointBoundaryCubes.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#outer-diff-inner-subset-i-union-integer).

## Counting outer cubes by inner cubes and boundary charts

Let $S \subseteq \mathbb{R}^n$,
let $f_1, \dots, f_m : [0,1]^d \to \mathbb{R}^n$ be maps whose ranges together cover the frontier
of $S$, and let $t$ be a real number. Let $O$ and $I$ be the outer and inner cube sets of $S$ at
scale $t$: the $v \in \mathbb{Z}^n$ for which some, respectively every, point $x$ of the half-open
unit cube $\prod_i [v_i, v_i + 1)$ has $x / t \in S$ (coordinatewise, with $x / 0 = 0$). Let $C_i$
be the integer cube set of $f_i$ at scale $t$: the $v$ whose half-open unit cube contains
$t f_i(y)$ for some $y \in [0,1]^d$. If $O$ and every $C_i$ are finite, then
$|O| \le |I| + \sum_{i=1}^m |C_i|$.

Formalized by `LatticePointBoundaryCubes.card_outer_le_card_inner_add_sum`, a theorem declared in [MathlibExt/Geometry/LatticePointBoundaryCubes.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointBoundaryCubes.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#card-outer-le-card-inner-add-sum).

## Integer points of a dilate

Let $S \subseteq \mathbb{R}^n$ and $t > 0$. Viewing an
integer vector as a real vector gives a bijection from the set of $x \in \mathbb{Z}^n$ with
$x / t \in S$ onto the lattice point set $tS \cap \mathbb{Z}^n$.

Formalized by `LatticePointAsymptotics.rawSubtypeEquivCanonicalPointSet`, a definition declared in [MathlibExt/Geometry/LatticePointAsymptotics.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointAsymptotics.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#raw-subtype-equiv-canonical-point-set).

## Integer count of a dilate

Let $S \subseteq \mathbb{R}^n$ and $t > 0$. The number of
integer vectors $x \in \mathbb{Z}^n$ with $x / t \in S$ equals the lattice enumerator of $S$ at
$t$, the number of points of $\mathbb{Z}^n$ in the dilate $tS$; here an infinite set is counted
as $0$.

Formalized by `LatticePointAsymptotics.card_raw_eq_latticeEnumerator`, a theorem declared in [MathlibExt/Geometry/LatticePointAsymptotics.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointAsymptotics.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#card-raw-eq-lattice-enumerator).

## Lattice-point error bound from boundary charts

Let $S \subseteq \mathbb{R}^n$ be
bounded, let $f_1, \dots, f_m$ be maps from the unit cube $[0,1]^d$ to $\mathbb{R}^n$ whose
ranges cover the boundary $\partial S$, and let $t > 0$. For each $i$, let $N_i(t)$ be the number
of $v \in \mathbb{Z}^n$ such that $t f_i(y)$ lies in the half-open cube $\prod_j [v_j, v_j + 1)$
for some $y \in [0,1]^d$, and assume each of these sets of $v$ is finite. Then the lattice
enumerator $L_S(t)$, the number of points of $\mathbb{Z}^n$ in $tS$, satisfies
$|L_S(t) - \operatorname{vol}(S)\, t^n| \le N_1(t) + \dots + N_m(t)$, where $\operatorname{vol}$
is Lebesgue (outer) measure.

Formalized by `LatticePointAsymptotics.lattice_point_count_error_bound`, a theorem declared in [MathlibExt/Geometry/LatticePointAsymptotics.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointAsymptotics.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#lattice-point-count-error-bound).

## Lattice-point count of a dilate with boundary error

Let $S \subseteq \mathbb{R}^n$ be
bounded, and suppose its boundary $\partial S$ is $(n-1)$-Lipschitz parametrizable: it is the
union of the ranges of finitely many Lipschitz maps from the unit cube $[0,1]^{n-1}$, where
$n - 1$ is read as $0$ when $n = 0$. Then there is a real constant $C$ such that for all
sufficiently large real $t$, the lattice enumerator $L_S(t)$, the number of points of
$\mathbb{Z}^n$ in $tS$, satisfies $|L_S(t) - \operatorname{vol}(S)\, t^n| \le C\, t^{n-1}$, where
$\operatorname{vol}$ is Lebesgue (outer) measure.

Formalized by `LatticePointAsymptotics.lattice_point_count_asymptotics`, a theorem declared in [MathlibExt/Geometry/LatticePointAsymptotics.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LatticePointAsymptotics.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html#lattice-point-count-asymptotics).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lattice points in dilated regions](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/discrete-geometry/part-01/lattice-points-in-dilated-regions)
