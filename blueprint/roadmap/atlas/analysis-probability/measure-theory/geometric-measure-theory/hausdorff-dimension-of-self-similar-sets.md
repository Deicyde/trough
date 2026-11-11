---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.MoranDimensionWanted.Dynamics.IsAttractor, MathlibExt.Dynamics.MoranDimensionWanted.Dynamics.IsAffineSymmetricIFS, MathlibExt.Dynamics.MoranDimensionWanted.Dynamics.OpenSetCondition, MathlibExt.Dynamics.MoranDimensionWanted.Dynamics.moran_equality_affine
statement: formalized
---

# Hausdorff dimension of self-similar sets

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/hausdorff-dimension-of-self-similar-sets/index.html).

## Attractor of an iterated function system

Let $X$ be a topological space and let
$(f_i)_{i < n}$ be a finite family of maps $X \to X$. A set $S \subseteq X$ is an attractor of the
family if it is nonempty and compact and is fixed by the Hutchinson operator, that is,
$S = \bigcup_{i < n} f_i(S)$.

Formalized by `MathlibExt.Dynamics.MoranDimensionWanted.Dynamics.IsAttractor`, a definition declared in [WantedExt/Dynamics/MoranDimensionWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/MoranDimensionWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/hausdorff-dimension-of-self-similar-sets/index.html#is-attractor).

## Affine-symmetric iterated function system

Let $(f_i)_{i < n}$ be a finite family of maps
$f_i \colon \mathbb{R}^d \to \mathbb{R}^d$ on Euclidean space. The family is affine-symmetric with
common contraction factor $\lambda$ if $0 < \lambda < 1$ and there are linear isometries
$A_i \colon \mathbb{R}^d \to \mathbb{R}^d$ (orthogonal transformations) and vectors
$\beta_i \in \mathbb{R}^d$ such that $f_i(x) = \lambda A_i(x) + \beta_i$ for every $i < n$ and every
$x \in \mathbb{R}^d$.

Formalized by `MathlibExt.Dynamics.MoranDimensionWanted.Dynamics.IsAffineSymmetricIFS`, a definition declared in [WantedExt/Dynamics/MoranDimensionWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/MoranDimensionWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/hausdorff-dimension-of-self-similar-sets/index.html#is-affine-symmetric-ifs).

## Open set condition

A finite family of maps $f_i \colon \mathbb{R}^d \to \mathbb{R}^d$,
$i < n$, satisfies the open set condition if there is a nonempty open set $G \subseteq \mathbb{R}^d$
such that $f_i(G) \subseteq G$ for every $i < n$ and the images $f_i(G)$ and $f_j(G)$ are disjoint
whenever $i \neq j$.

Formalized by `MathlibExt.Dynamics.MoranDimensionWanted.Dynamics.OpenSetCondition`, a definition declared in [WantedExt/Dynamics/MoranDimensionWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/MoranDimensionWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/hausdorff-dimension-of-self-similar-sets/index.html#open-set-condition).

## Moran's equality for affine-symmetric iterated function systems

Let $n \ge 1$ and let
$(f_i)_{i < n}$ be an affine-symmetric iterated function system on $\mathbb{R}^d$ with common
contraction factor $\lambda \in (0,1)$ that satisfies the open set condition. Then every attractor
$S \subseteq \mathbb{R}^d$ of the system has Hausdorff dimension

$$\dim_H S = -\frac{\log n}{\log \lambda}.$$

## Sources

- P. A. P. Moran, *Additive functions of intervals and Hausdorff measure*, Proc. Cambridge Philos. Soc. 42 (1946); J. E. Hutchinson, *Fractals and self similarity*, Indiana Univ. Math. J. 30 (1981). Knill, *Some fundamental theorems in mathematics*, §105. Problem `moran_equality_affine` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.MoranDimensionWanted.Dynamics.moran_equality_affine` is written with `theorem_wanted` in [WantedExt/Dynamics/MoranDimensionWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/MoranDimensionWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/hausdorff-dimension-of-self-similar-sets/index.html#moran-equality-affine).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hausdorff dimension of self-similar sets](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/geometric-measure-theory/hausdorff-dimension-of-self-similar-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/geometric-measure-theory/hausdorff-dimension-of-self-similar-sets)
