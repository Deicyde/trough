---
declaration: section
origin: cited
lean: DiscreteGroups.E2, DiscreteGroups.M₂, DiscreteGroups.linearPart, DiscreteGroups.pointGroupSet, DiscreteGroups.translationLattice, DiscreteGroups.translationHom, DiscreteGroups.translationLatticeSubgroup, DiscreteGroups.mem_translationLatticeSubgroup
statement: formalized
proof: formalized
---

# Discrete groups of plane isometries

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html).

## The Euclidean plane for discrete isometry groups

$E_2$ is the Euclidean plane:
the real vector space $\mathbb{R}^2$ of pairs of real numbers with the standard Euclidean inner
product and norm.

Formalized by `DiscreteGroups.E2`, an abbreviation declared in [MathlibExt/Geometry/Euclidean/DiscreteGroups.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DiscreteGroups.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html#e2).

## Isometry group of the Euclidean plane

$M_2$ is the group, under composition, of affine
isometries of the Euclidean plane onto itself.

Formalized by `DiscreteGroups.M₂`, an abbreviation declared in [MathlibExt/Geometry/Euclidean/DiscreteGroups.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DiscreteGroups.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html#m).

## Linear part of a plane isometry

The linear part of an affine isometry $f$ of the
Euclidean plane is the linear isometry $A$ of the plane such that $f(x + v) = f(x) + A v$ for
every point $x$ and every vector $v$.

Formalized by `DiscreteGroups.linearPart`, a definition declared in [MathlibExt/Geometry/Euclidean/DiscreteGroups.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DiscreteGroups.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html#linear-part).

## Point group of a group of plane isometries

The point group of a group $G$ of affine
isometries of the Euclidean plane is the set of linear parts of the elements of $G$.

Formalized by `DiscreteGroups.pointGroupSet`, a definition declared in [MathlibExt/Geometry/Euclidean/DiscreteGroups.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DiscreteGroups.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html#point-group-set).

## Translation lattice

The translation lattice of a subgroup $G$ of the group $M_2$ of
affine isometries of the Euclidean plane $E_2$ is the set of vectors $v \in E_2$ such that the
translation $x \mapsto v + x$ belongs to $G$.

Formalized by `DiscreteGroups.translationLattice`, a definition declared in [MathlibExt/Geometry/Euclidean/DiscreteGroups.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DiscreteGroups.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html#translation-lattice).

## Translation homomorphism

The group homomorphism from the additive group of the Euclidean
plane $\mathbb{R}^2$ (written multiplicatively) to the group of affine isometries of the plane that
sends a vector $v$ to translation by $v$, the isometry $x \mapsto v + x$.

Formalized by `DiscreteGroups.translationHom`, a definition declared in [MathlibExt/Geometry/Euclidean/DiscreteGroups.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DiscreteGroups.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html#translation-hom).

## Translation lattice as an additive subgroup

For a group $G$ of affine isometries of the
Euclidean plane $\mathbb{R}^2$, the additive subgroup of $\mathbb{R}^2$ consisting of the vectors
$v$ such that translation by $v$ belongs to $G$; it is the preimage of $G$ under the translation
homomorphism $v \mapsto (x \mapsto v + x)$.

Formalized by `DiscreteGroups.translationLatticeSubgroup`, a definition declared in [MathlibExt/Geometry/Euclidean/DiscreteGroups.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DiscreteGroups.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html#translation-lattice-subgroup).

## Membership in the translation lattice subgroup

For every group $G$ of affine isometries
of the Euclidean plane and every vector $v$ of the plane, $v$ belongs to the translation lattice
subgroup of $G$ if and only if $v$ belongs to the translation lattice of $G$.

Formalized by `DiscreteGroups.mem_translationLatticeSubgroup`, a theorem declared in [MathlibExt/Geometry/Euclidean/DiscreteGroups.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DiscreteGroups.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html#mem-translation-lattice-subgroup).

## Carrier of the translation lattice subgroup

For every group $G$ of affine isometries of
the Euclidean plane, the underlying set of the translation lattice subgroup of $G$ is the
translation lattice of $G$.

Formalized by `DiscreteGroups.coe_translationLatticeSubgroup`, a theorem declared in [MathlibExt/Geometry/Euclidean/DiscreteGroups.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DiscreteGroups.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html#coe-translation-lattice-subgroup).

## Translations are determined by their vectors

For vectors $v$ and $w$ of the Euclidean
plane $\mathbb{R}^2$, if translation by $v$ and translation by $w$ are the same affine isometry,
then $v = w$. Equivalently, the translation homomorphism $v \mapsto (x \mapsto v + x)$ from the
additive group of the plane to the group of affine isometries of the plane is injective.

Formalized by `DiscreteGroups.translationHom_injective`, a theorem declared in [MathlibExt/Geometry/Euclidean/DiscreteGroups.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DiscreteGroups.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html#translation-hom-injective).

## Separation criterion for groups of plane isometries

A group $G$ of affine isometries of
the Euclidean plane satisfies the separation criterion if there is $\varepsilon > 0$ such that
every element $f \ne \mathrm{id}$ of $G$ whose linear part is the identity satisfies
$\|f(0)\| \ge \varepsilon$, and every element $f$ of $G$ whose linear part $A$ is not the
identity satisfies $\|A - I\| \ge \varepsilon$, where $I$ is the identity map and the norm is
the operator norm.

Its linear-part condition measures operator-norm separation from the identity, rather than the
numerical rotation angle.

Formalized by `DiscreteGroups.IsDiscrete`, a definition declared in [MathlibExt/Geometry/Euclidean/DiscreteGroups.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DiscreteGroups.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html#is-discrete).

## The translation lattice of a discrete isometry group is discrete

Let $G$ be a group of
affine isometries of the Euclidean plane $\mathbb{R}^2$, and suppose there is $\varepsilon > 0$
such that every non-identity translation in $G$ moves the origin by at least $\varepsilon$, and
every element of $G$ whose linear part $A$ is not the identity satisfies
$\|A - I\| \ge \varepsilon$ in operator norm. Then the translation lattice of $G$, the additive
subgroup of vectors $v$ such that translation by $v$ lies in $G$, is discrete in the subspace
topology of $\mathbb{R}^2$.

Formalized by `DiscreteGroups.translationLatticeSubgroup_discreteTopology`, a theorem declared in [MathlibExt/Geometry/Euclidean/DiscreteGroups.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DiscreteGroups.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html#translation-lattice-subgroup-discrete-to).

## Conjugating a translation by a plane isometry

Let $g$ be an affine isometry of the
Euclidean plane with linear part $A$, let $v$ be a vector, and write $\tau_w$ for translation by
a vector $w$. Then $g \circ \tau_v \circ g^{-1} = \tau_{A v}$.

Formalized by `DiscreteGroups.conj_translation`, a lemma declared in [MathlibExt/Geometry/Euclidean/DiscreteGroups.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DiscreteGroups.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html#conj-translation).

## The point group preserves the translation lattice

Let $G$ be a group of affine
isometries of the Euclidean plane. If $A$ belongs to the point group of $G$, that is, $A$ is the
linear part of some element of $G$, and $v$ belongs to the translation lattice of $G$, then $A v$
belongs to the translation lattice of $G$.

Formalized by `DiscreteGroups.point_group_preserves_lattice`, a theorem declared in [MathlibExt/Geometry/Euclidean/DiscreteGroups.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DiscreteGroups.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html#point-group-preserves-lattice).

## Classification of discrete additive subgroups of the plane

Every
discrete additive subgroup `G` of `ℝ²` is trivial, cyclic (generated by a
single nonzero vector), or a rank-two lattice (generated by two
`ℝ`-linearly independent vectors).

Formalized by `DiscreteGroups.discrete_subgroup_R2_classification`, a theorem declared in [MathlibExt/Geometry/Euclidean/DiscreteGroups.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DiscreteGroups.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html#discrete-subgroup-r2-classification).

## Classification of translation lattices

Let $G$ be a group of affine isometries of the
Euclidean plane $\mathbb{R}^2$, and suppose there is $\varepsilon > 0$ such that every
non-identity translation in $G$ moves the origin by at least $\varepsilon$, and every element of
$G$ whose linear part $A$ is not the identity satisfies $\|A - I\| \ge \varepsilon$ in operator
norm. Let $L$ be the translation lattice of $G$, the additive subgroup of vectors $v$ such that
translation by $v$ lies in $G$. Then either $L = \{0\}$, or $L = \mathbb{Z}\alpha$ for some nonzero
vector $\alpha$, or $L = \mathbb{Z}a + \mathbb{Z}b$ for some $\mathbb{R}$-linearly independent
vectors $a$ and $b$.

Formalized by `DiscreteGroups.translation_lattice_classification`, a theorem declared in [MathlibExt/Geometry/Euclidean/DiscreteGroups.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DiscreteGroups.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html#translation-lattice-classification).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Discrete groups of plane isometries](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/discrete-groups-of-plane-isometries)
