---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.Geometry.BanachTarskiWanted.FinitelyEquidecomposableByIsometries, MathlibExt.MeasureTheory.Geometry.BanachTarskiWanted.finitelyEquidecomposableByIsometries_iff_bijOn, MathlibExt.MeasureTheory.Geometry.BanachTarskiWanted.FinitelyEquidecomposableByIsometries.refl, MathlibExt.MeasureTheory.Geometry.BanachTarskiWanted.FinitelyEquidecomposableByIsometries.symm, MathlibExt.MeasureTheory.Geometry.BanachTarskiWanted.FinitelyEquidecomposableByIsometries.trans, MathlibExt.MeasureTheory.Geometry.BanachTarskiWanted.FinitelyEquidecomposableByIsometries.union, MathlibExt.MeasureTheory.Geometry.BanachTarskiWanted.FinitelyEquidecomposableByIsometries.image_isometryEquiv, MathlibExt.MeasureTheory.Geometry.BanachTarskiWanted.banach_tarski_closedBall_unit
statement: formalized
proof: formalized
---

# Banach–Tarski paradox

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/banach-tarski-paradox/index.html).

## Equidecomposability

## Finite equidecomposability by isometries

Let $X$ be a metric space. Subsets $A$ and $B$
of $X$ are finitely equidecomposable by isometries if there are a natural number $n$, sets
$A_1, \dots, A_n$ and $B_1, \dots, B_n$ in $X$, and isometric bijections $g_1, \dots, g_n$ of
$X$ onto itself such that the sets $A_i$ are pairwise disjoint, the sets $B_i$ are pairwise
disjoint, $A = A_1 \cup \dots \cup A_n$, $B = B_1 \cup \dots \cup B_n$, and $g_i(A_i) = B_i$
for every $i$.

Formalized by `MathlibExt.MeasureTheory.Geometry.BanachTarskiWanted.FinitelyEquidecomposableByIsometries`, a definition declared in [MathlibExt/MeasureTheory/Geometry/BanachTarski.lean, line 2201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Geometry/BanachTarski.lean#L2201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/banach-tarski-paradox/index.html#finitely-equidecomposable-by-isometries).

## Equidecomposability via piecewise-isometric bijections

Let $A$ and $B$ be subsets of a
metric space $X$. Then $A$ is finitely equidecomposable by isometries with $B$ if and only if
there are a map $f : X \to X$ and a finite set $S$ of isometric bijections of $X$ onto itself
such that $f$ restricts to a bijection from $A$ onto $B$ and for every $x \in A$ there is
$g \in S$ with $f(x) = g(x)$.

Formalized by `MathlibExt.MeasureTheory.Geometry.BanachTarskiWanted.finitelyEquidecomposableByIsometries_iff_bijOn`, a theorem declared in [MathlibExt/MeasureTheory/Geometry/BanachTarski.lean, line 2366](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Geometry/BanachTarski.lean#L2366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/banach-tarski-paradox/index.html#finitely-equidecomposable-by-isometries-2).

## Finite equidecomposability by isometries is reflexive

Every subset $A$ of a metric
space $X$ is finitely equidecomposable by isometries with itself.

Formalized by `MathlibExt.MeasureTheory.Geometry.BanachTarskiWanted.FinitelyEquidecomposableByIsometries.refl`, a theorem declared in [MathlibExt/MeasureTheory/Geometry/BanachTarski.lean, line 2380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Geometry/BanachTarski.lean#L2380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/banach-tarski-paradox/index.html#refl).

## Finite equidecomposability by isometries is symmetric

Let $A$ and $B$ be subsets of a
metric space $X$. If $A$ is finitely equidecomposable by isometries with $B$, then $B$ is
finitely equidecomposable by isometries with $A$.

Formalized by `MathlibExt.MeasureTheory.Geometry.BanachTarskiWanted.FinitelyEquidecomposableByIsometries.symm`, a theorem declared in [MathlibExt/MeasureTheory/Geometry/BanachTarski.lean, line 2385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Geometry/BanachTarski.lean#L2385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/banach-tarski-paradox/index.html#symm).

## Finite equidecomposability by isometries is transitive

Let $A$, $B$ and $C$ be subsets
of a metric space $X$. If $A$ is finitely equidecomposable by isometries with $B$ and $B$ is
finitely equidecomposable by isometries with $C$, then $A$ is finitely equidecomposable by
isometries with $C$.

Formalized by `MathlibExt.MeasureTheory.Geometry.BanachTarskiWanted.FinitelyEquidecomposableByIsometries.trans`, a theorem declared in [MathlibExt/MeasureTheory/Geometry/BanachTarski.lean, line 2391](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Geometry/BanachTarski.lean#L2391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/banach-tarski-paradox/index.html#trans).

## Finite equidecomposability by isometries respects disjoint unions

Let $A_1$, $A_2$,
$B_1$ and $B_2$ be subsets of a metric space $X$ with $A_1 \cap A_2 = \emptyset$ and
$B_1 \cap B_2 = \emptyset$. If $A_1$ is finitely equidecomposable by isometries with $B_1$ and
$A_2$ is finitely equidecomposable by isometries with $B_2$, then $A_1 \cup A_2$ is finitely
equidecomposable by isometries with $B_1 \cup B_2$.

Formalized by `MathlibExt.MeasureTheory.Geometry.BanachTarskiWanted.FinitelyEquidecomposableByIsometries.union`, a theorem declared in [MathlibExt/MeasureTheory/Geometry/BanachTarski.lean, line 2398](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Geometry/BanachTarski.lean#L2398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/banach-tarski-paradox/index.html#union).

## Equidecomposability of a set with its isometric image

Let $g$ be an isometric bijection
of a metric space $X$ onto itself. Then every subset $A$ of $X$ is finitely equidecomposable by
isometries with its image $g(A)$.

Formalized by `MathlibExt.MeasureTheory.Geometry.BanachTarskiWanted.FinitelyEquidecomposableByIsometries.image_isometryEquiv`, a theorem declared in [MathlibExt/MeasureTheory/Geometry/BanachTarski.lean, line 2406](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Geometry/BanachTarski.lean#L2406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/banach-tarski-paradox/index.html#image-isometry-equiv).

## Banach–Tarski paradox for the closed unit ball

In three-dimensional Euclidean space
$\mathbb{R}^3$, write $\bar B(c, r)$ for the closed ball of radius $r$ about $c$. There are points
$c_1, c_2 \in \mathbb{R}^3$ such that $\bar B(c_1, 1)$ and $\bar B(c_2, 1)$ are disjoint and the
closed unit ball $\bar B(0, 1)$ is finitely equidecomposable by isometries with
$\bar B(c_1, 1) \cup \bar B(c_2, 1)$.

## Sources

- S. Banach and A. Tarski, Fund. Math. 6 (1924) 244–277 original paradox; S. Wagon, The Banach–Tarski Paradox, Cambridge Univ. Press (1993); Lean states closed unit ball duplication specialization in ℝ³ with ambient `≃ᵢ` equidecomposability.

Formalized by `MathlibExt.MeasureTheory.Geometry.BanachTarskiWanted.banach_tarski_closedBall_unit`, a theorem declared in [MathlibExt/MeasureTheory/Geometry/BanachTarski.lean, line 2423](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Geometry/BanachTarski.lean#L2423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/banach-tarski-paradox/index.html#banach-tarski-closed-ball-unit).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Banach–Tarski paradox](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/banach-tarski-paradox/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/measures/banach-tarski-paradox)
