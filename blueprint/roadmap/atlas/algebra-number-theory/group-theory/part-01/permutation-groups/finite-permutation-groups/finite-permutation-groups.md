---
declaration: section
origin: cited
lean: Subgroup.card_stabilizer_dvd_card, MulAction.card_add_mul_card_sub_one_eq_card_orbits_mul_card, MathlibExt.GroupTheory.FrobeniusWanted.GroupTheory.frobenius_kernel_isNormal, MathlibExt.GroupTheory.MultiplyTransitiveWanted.GroupTheory.five_transitive_card_classification
statement: formalized
---

# Finite permutation groups: its own results

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/index.html).

Actions of finite groups on finite sets: Burnside-type counting, stabilizers, multiply and doubly transitive finite groups, Frobenius groups, bases and independent sets, 2-closures, regular orbits of linear actions, coverings and products in finite symmetric groups.

## A subgroup stabilizing a subset has order dividing its size

Let $G$ be a finite group,
let $H$ be a subgroup of $G$ and let $U$ be a subset of $G$ such that $hu \in U$ for all
$h \in H$ and $u \in U$. Then $|H|$ divides $|U|$.

The $H$-orbits partition $U$ and each orbit has exactly $|H|$ elements, since left
multiplication is injective.

Formalized by `Subgroup.card_stabilizer_dvd_card`, a theorem declared in [MathlibExt/GroupTheory/GroupAction/StabilizerDivides.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/GroupAction/StabilizerDivides.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/index.html#card-stabilizer-dvd-card).

## Burnside's lemma with a uniform fixed-point count

Let a finite group $G$ act on a finite
set $X$, and let $c$ be a natural number such that every element $g \ne 1$ of $G$ fixes exactly
$c$ points of $X$. Writing $N$ for the number of orbits of $G$ on $X$, we have
$|X| + c\,(|G| - 1) = N \cdot |G|$.

Formalized by `MulAction.card_add_mul_card_sub_one_eq_card_orbits_mul_card`, a theorem declared in [MathlibExt/GroupTheory/GroupAction/UniformFixedPoints.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/GroupAction/UniformFixedPoints.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/index.html#card-add-mul-card-sub-one-eq-card-orbits).

## Frobenius's theorem on the Frobenius kernel

Let a finite group $G$ act faithfully and
transitively on a finite set $X$ with at least two elements, such that every point stabiliser is
nontrivial and no nonidentity element of $G$ fixes two distinct points of $X$. Then the set
consisting of the identity together with the elements of $G$ that fix no point of $X$ is a normal
subgroup of $G$.

## Sources

- G. Frobenius, Über auflösbare Gruppen IV, Sitzungsber. Akad. Wiss. Berlin (1901). Problem `frobenius_kernel_isNormal` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.FrobeniusWanted.GroupTheory.frobenius_kernel_isNormal` is written with `theorem_wanted` in [WantedExt/GroupTheory/FrobeniusWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FrobeniusWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/index.html#frobenius-kernel-is-normal).

## Orders of finite $5$-transitive permutation groups

Let a finite group $G$ act
faithfully on a finite set $X$ with $n = |X| \ge 5$, and suppose that the action is
$5$-transitive: for any two injective maps $a, b \colon \{0, 1, 2, 3, 4\} \to X$ there is
$g \in G$ with $g \cdot a(i) = b(i)$ for all $i$. Then $|G| = n!$, or $n \ge 7$ and
$|G| = n!/2$, or $n = 12$ and $|G| = 95040$, or $n = 24$ and $|G| = 244823040$.

## Sources

- Folklore via CFSG; classical work of Mathieu, Jordan; modern accounts in P. Cameron, Permutation Groups (1999). Problem `five_transitive_card_classification` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.MultiplyTransitiveWanted.GroupTheory.five_transitive_card_classification` is written with `theorem_wanted` in [WantedExt/GroupTheory/MultiplyTransitiveWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MultiplyTransitiveWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/index.html#five-transitive-card-classification).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite permutation groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/permutation-groups/finite-permutation-groups)
