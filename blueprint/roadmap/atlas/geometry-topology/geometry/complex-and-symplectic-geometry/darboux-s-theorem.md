---
declaration: section
origin: cited
lean: MathlibExt.Geometry.DarbouxWanted.Geometry.Darboux.E, MathlibExt.Geometry.DarbouxWanted.Geometry.Darboux.idxP, MathlibExt.Geometry.DarbouxWanted.Geometry.Darboux.idxQ, MathlibExt.Geometry.DarbouxWanted.Geometry.Darboux.IsDarbouxNormal, MathlibExt.Geometry.DarbouxWanted.Geometry.Darboux.IsSymplecticOn, MathlibExt.Geometry.DarbouxWanted.Geometry.Darboux.darboux
statement: formalized
---

# Darboux's theorem

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/darboux-s-theorem/index.html).

## Model space $\mathbb{R}^{2n}$ for Darboux's theorem

For a natural number $n$, the model
space is $\mathbb{R}^{2n}$, the Euclidean space of dimension $2n$ with coordinates indexed by
$0, 1, \dots, 2n - 1$ and the standard inner product.

Formalized by `MathlibExt.Geometry.DarbouxWanted.Geometry.Darboux.E`, an abbreviation declared in [WantedExt/Geometry/DarbouxWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/DarbouxWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/darboux-s-theorem/index.html#e).

## Index of the $i$-th $p$-coordinate in $\mathbb{R}^{2n}$

For $i \in \{0, \dots, n - 1\}$,
the index of the $i$-th $p$-coordinate among the coordinates $0, \dots, 2n - 1$ of
$\mathbb{R}^{2n}$ is $i$ itself.

Formalized by `MathlibExt.Geometry.DarbouxWanted.Geometry.Darboux.idxP`, a definition declared in [WantedExt/Geometry/DarbouxWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/DarbouxWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/darboux-s-theorem/index.html#idx-p).

## Index of the $i$-th $q$-coordinate in $\mathbb{R}^{2n}$

For $i \in \{0, \dots, n - 1\}$,
the index of the $i$-th $q$-coordinate among the coordinates $0, \dots, 2n - 1$ of
$\mathbb{R}^{2n}$ is $i + n$.

Formalized by `MathlibExt.Geometry.DarbouxWanted.Geometry.Darboux.idxQ`, a definition declared in [WantedExt/Geometry/DarbouxWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/DarbouxWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/darboux-s-theorem/index.html#idx-q).

## Darboux normal form

Let $n$ be a natural number and let $e_0, \dots, e_{2n-1}$ be the
standard basis of $\mathbb{R}^{2n}$. A continuous alternating 2-form $\omega$ on $\mathbb{R}^{2n}$
is in Darboux normal form if for all $i, j \in \{0, \dots, n - 1\}$ we have
$\omega(e_i, e_{n+j}) = 1$ when $i = j$ and $0$ otherwise, $\omega(e_i, e_j) = 0$, and
$\omega(e_{n+i}, e_{n+j}) = 0$.

By antisymmetry these conditions determine the form uniquely: it is the standard symplectic form
$\omega_0 = \sum_i dx_i \wedge dx_{n+i}$.

Formalized by `MathlibExt.Geometry.DarbouxWanted.Geometry.Darboux.IsDarbouxNormal`, a definition declared in [WantedExt/Geometry/DarbouxWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/DarbouxWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/darboux-s-theorem/index.html#is-darboux-normal).

## Symplectic 2-form fields

Let $n$ be a natural number and $U$ a subset of
$\mathbb{R}^{2n}$. A field $\alpha$ of continuous alternating 2-forms on $\mathbb{R}^{2n}$ is
symplectic on $U$ if $\alpha$ is $C^\infty$ on $U$, its exterior derivative $d\alpha$ vanishes
at every point of $U$, and $\alpha$ is non-degenerate at every point of $U$: for every $x \in U$
and every nonzero $v \in \mathbb{R}^{2n}$ there is $w \in \mathbb{R}^{2n}$ with
$\alpha(x)(v, w) \neq 0$.

Formalized by `MathlibExt.Geometry.DarbouxWanted.Geometry.Darboux.IsSymplecticOn`, a definition declared in [WantedExt/Geometry/DarbouxWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/DarbouxWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/darboux-s-theorem/index.html#is-symplectic-on).

## Darboux's theorem

Let $n$ be a natural number, let $U$ be an open subset of the model
space $\mathbb{R}^{2n}$, and let $\alpha$ be a field of continuous alternating 2-forms on
$\mathbb{R}^{2n}$ that is symplectic on $U$. Then for every $x \in U$ there is an open partial
homeomorphism $\varphi$ of $\mathbb{R}^{2n}$ whose source contains $x$ and is contained in $U$, such
that $\varphi$ is $C^\infty$ on its source, $\varphi^{-1}$ is $C^\infty$ on its target, and for
every $z$ in the target the pullback of $\alpha(\varphi^{-1}(z))$ by the derivative
$D\varphi^{-1}(z)$, namely
$(v, w) \mapsto \alpha(\varphi^{-1}(z))(D\varphi^{-1}(z)\, v, D\varphi^{-1}(z)\, w)$, is in Darboux
normal form.

## Sources

- J. G. Darboux, Sur le problème de Pfaff, Bull. Sci. Math. 6 (1882), 14-36, 49-68. Listed as §39 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `darboux` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.DarbouxWanted.Geometry.Darboux.darboux` is written with `theorem_wanted` in [WantedExt/Geometry/DarbouxWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/DarbouxWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/darboux-s-theorem/index.html#darboux).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Darboux's theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/darboux-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/complex-and-symplectic-geometry/darboux-s-theorem)
