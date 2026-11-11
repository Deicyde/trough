---
declaration: section
origin: cited
lean: MathlibExt.Geometry.InfiniteTransversalsSpannedHyperplanesWanted.ITSP.IsAffineHyperplane, MathlibExt.Geometry.InfiniteTransversalsSpannedHyperplanesWanted.ITSP.SpannedHyperplaneSet, MathlibExt.Geometry.InfiniteTransversalsSpannedHyperplanesWanted.ITSP.OWR1183Question, MathlibExt.Geometry.InfiniteTransversalsSpannedHyperplanesWanted.OWR1183Question_holds
statement: formalized
---

# Points and spanned hyperplanes

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/points-and-spanned-hyperplanes/index.html).

## Hyperplanes spanned by point sets

## Affine hyperplanes in $\mathbb{R}^d$

An affine subspace $A$ of $\mathbb{R}^d$ is an affine
hyperplane when there are a nonzero linear functional $\ell \colon \mathbb{R}^d \to \mathbb{R}$ and
a real number $c$ such that $A = \{x \in \mathbb{R}^d : \ell(x) = c\}$.

## Sources

- `OWR-1183-011`.

Formalized by `MathlibExt.Geometry.InfiniteTransversalsSpannedHyperplanesWanted.ITSP.IsAffineHyperplane`, a definition declared in [WantedExt/Geometry/InfiniteTransversalsSpannedHyperplanesWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/InfiniteTransversalsSpannedHyperplanesWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/points-and-spanned-hyperplanes/index.html#is-affine-hyperplane).

## Hyperplanes spanned by a point set

For a set $P \subseteq \mathbb{R}^d$, the hyperplanes
spanned by $P$ are the affine hyperplanes of $\mathbb{R}^d$ that equal the affine span of some
subset of $P$.

## Sources

- `OWR-1183-011`.

Formalized by `MathlibExt.Geometry.InfiniteTransversalsSpannedHyperplanesWanted.ITSP.SpannedHyperplaneSet`, a definition declared in [WantedExt/Geometry/InfiniteTransversalsSpannedHyperplanesWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/InfiniteTransversalsSpannedHyperplanesWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/points-and-spanned-hyperplanes/index.html#spanned-hyperplane-set).

## Injective point-to-hyperplane matching question

The statement that for every $d \ge 1$
and every set $P \subseteq \mathbb{R}^d$ whose affine span is all of $\mathbb{R}^d$, writing
$\mathcal{H}$ for the set of affine hyperplanes of $\mathbb{R}^d$ that equal the affine span of
some subset of $P$, there is an injective map $f \colon P \to \mathcal{H}$ with $p \in f(p)$ for
every $p \in P$.

## Sources

- the question of `OWR-1183-011`.

Formalized by `MathlibExt.Geometry.InfiniteTransversalsSpannedHyperplanesWanted.ITSP.OWR1183Question`, a definition declared in [WantedExt/Geometry/InfiniteTransversalsSpannedHyperplanesWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/InfiniteTransversalsSpannedHyperplanesWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/points-and-spanned-hyperplanes/index.html#owr1183-question).

## Spanning point sets have injective point-to-hyperplane matchings

For every $d \ge 1$ and
every set $P \subseteq \mathbb{R}^d$ whose affine span is all of $\mathbb{R}^d$, let $\mathcal{H}$
be the set of affine hyperplanes of $\mathbb{R}^d$ that equal the affine span of some subset of
$P$. Then there is an injective map $f \colon P \to \mathcal{H}$ with $p \in f(p)$ for every
$p \in P$.

This answers the question of `OWR-1183-011` affirmatively. It follows from Farley's Theorem 11:
every geometric lattice of finite rank greater than $1$, of any cardinality, has an injective
map sending each atom to a coatom containing it; apply it to the lattice of affine flats
spanned by subsets of $P$.

## Sources

- J. D. Farley, A question of Björner from 1981: infinite geometric lattices of finite rank have matchings, Australasian Journal of Combinatorics 82 (2022) 228-235, arXiv:2004.11972, https://arxiv.org/abs/2004.11972.

Stated but not proved: `MathlibExt.Geometry.InfiniteTransversalsSpannedHyperplanesWanted.OWR1183Question_holds` is written with `theorem_wanted` in [WantedExt/Geometry/InfiniteTransversalsSpannedHyperplanesWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/InfiniteTransversalsSpannedHyperplanesWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/points-and-spanned-hyperplanes/index.html#owr1183-question-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Points and spanned hyperplanes](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/points-and-spanned-hyperplanes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/discrete-geometry/part-01/points-and-spanned-hyperplanes)
