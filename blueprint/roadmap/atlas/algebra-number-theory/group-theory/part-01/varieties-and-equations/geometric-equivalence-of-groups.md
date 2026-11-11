---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.QuasiIdentity, MathlibExt.GroupTheory.QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.QuasiIdentity.HoldsIn, MathlibExt.GroupTheory.QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.gClosure, MathlibExt.GroupTheory.QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.GeometricallyEquivalent, MathlibExt.GroupTheory.QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.sameQuasiIdentitiesImpliesGeometricallyEquivalent, MathlibExt.GroupTheory.QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.sameQuasiIdentitiesImpliesGeometricallyEquivalent_refuted
statement: formalized
---

# Geometric equivalence of groups

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/geometric-equivalence-of-groups/index.html).

## Quasi-identities of groups

A quasi-identity consists of a natural number $n$, a finite
list of premises $w_1, \dots, w_k$ and a conclusion $w$, all elements of the free group $F_n$ on
the unknowns $x_0, \dots, x_{n-1}$. It stands for the formula
$\forall x_0, \dots, x_{n-1}\, (w_1 = 1 \wedge \dots \wedge w_k = 1 \to w = 1)$.

Formalized by `MathlibExt.GroupTheory.QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.QuasiIdentity`, a structure declared in [WantedExt/GroupTheory/QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/geometric-equivalence-of-groups/index.html#quasi-identity).

## Satisfaction of a quasi-identity in a group

Let $q$ be a quasi-identity with unknowns
$x_0, \dots, x_{n-1}$, premises $w_1, \dots, w_k$ and conclusion $w$, all in the free group $F_n$
on $x_0, \dots, x_{n-1}$. For $g_0, \dots, g_{n-1}$ in a group $G$ and $u \in F_n$, write
$u(g_0, \dots, g_{n-1})$ for the image of $u$ under the homomorphism $F_n \to G$ sending each
$x_j$ to $g_j$. Then $q$ holds in $G$ when for all $g_0, \dots, g_{n-1} \in G$ with
$w_i(g_0, \dots, g_{n-1}) = 1$ for every premise $w_i$, also $w(g_0, \dots, g_{n-1}) = 1$.

Formalized by `MathlibExt.GroupTheory.QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.QuasiIdentity.HoldsIn`, a definition declared in [WantedExt/GroupTheory/QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/geometric-equivalence-of-groups/index.html#holds-in).

## Closure of a set of words with respect to a group

Let $G$ be a group, let $F_n$ be the
free group on the basis $x_0, \dots, x_{n-1}$, and let $T \subseteq F_n$. The $G$-closure
$\mathrm{cl}_G(T)$ is the set of $w \in F_n$ such that $\mu(w) = 1$ for every homomorphism
$\mu : F_n \to G$ with $\mu(t) = 1$ for all $t \in T$, that is, the intersection of the kernels
of all homomorphisms $F_n \to G$ that vanish on $T$.

Formalized by `MathlibExt.GroupTheory.QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.gClosure`, a definition declared in [WantedExt/GroupTheory/QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/geometric-equivalence-of-groups/index.html#g-closure).

## Geometrically equivalent groups

Two groups $G$ and $H$ are geometrically equivalent
(B. I. Plotkin) when $\mathrm{cl}_G(T) = \mathrm{cl}_H(T)$ for every natural number $n$ and
every subset $T$ of the free group $F_n$ of rank $n$, where $\mathrm{cl}_G(T)$ is the
$G$-closure of $T$: the intersection of the kernels of all homomorphisms $F_n \to G$ that
vanish on $T$.

Formalized by `MathlibExt.GroupTheory.QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.GeometricallyEquivalent`, a definition declared in [WantedExt/GroupTheory/QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/geometric-equivalence-of-groups/index.html#geometrically-equivalent).

## Plotkin's problem on quasi-identities and geometric equivalence

The proposition
(Kourovka Problem 14.71, B. I. Plotkin) that any two groups $G$ and $H$ satisfying the same
quasi-identities, meaning that every quasi-identity holds in $G$ if and only if it holds in $H$,
are geometrically equivalent.

Formalized by `MathlibExt.GroupTheory.QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.sameQuasiIdentitiesImpliesGeometricallyEquivalent`, a definition declared in [WantedExt/GroupTheory/QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/geometric-equivalence-of-groups/index.html#same-quasi-identities-implies-geometrica).

## Groups with the same quasi-identities need not be geometrically equivalent

The statement
of Kourovka Problem 14.71 is false: there are groups $G$ and $H$ such that every quasi-identity
holds in $G$ if and only if it holds in $H$, but $G$ and $H$ are not geometrically equivalent.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 14.71 (B. I. Plotkin); resolution: V. V. Bludov, Abstracts of the 7th Int. Conf. Groups and Group Rings, Supraśl, 1999, p. 6; R. Göbel and S. Shelah, Proc. Amer. Math. Soc. 130 (2002), 673-674; A. G. Myasnikov and V. N. Remeslennikov, J. Algebra 234 (2000), no. 1, 225-276, Kourovka Archive, Problem 14.71 (answer: No, not always).

Stated but not proved: `MathlibExt.GroupTheory.QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.sameQuasiIdentitiesImpliesGeometricallyEquivalent_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/QuasiIdentitiesGeometricEquivalenceKourovka14Problem71Wanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/geometric-equivalence-of-groups/index.html#same-quasi-identities-implies-geometrica-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Geometric equivalence of groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/geometric-equivalence-of-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/varieties-and-equations/geometric-equivalence-of-groups)
