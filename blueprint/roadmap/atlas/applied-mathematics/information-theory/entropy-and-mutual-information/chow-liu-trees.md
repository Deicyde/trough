---
declaration: section
origin: cited
lean: InformationTheory.DependenceForest, InformationTheory.DependenceForest.approx, InformationTheory.DependenceForest.approx_nonneg, InformationTheory.DependenceForest.approx_pos, InformationTheory.DependenceForest.sum_approx, InformationTheory.DependenceForest.approxPMF, InformationTheory.DependenceForest.weight, InformationTheory.DependenceForest.divergence
statement: formalized
proof: formalized
---

# Chow–Liu trees

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/chow-liu-trees/index.html).

## Information Theory

## Dependence forest

A dependence forest on the variables `ι` (Chow–Liu 1968): each variable has at most one parent,
and `rank` strictly increases from parent to child, so the parent relation has no cycles.

Formalized by `InformationTheory.DependenceForest`, a structure declared in [MathlibExt/InformationTheory/ChowLiu.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/ChowLiu.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/chow-liu-trees/index.html#dependence-forest).

## Chow–Liu product approximation of a joint law

Chow–Liu's product approximation `P_τ(x) = ∏_i P(x_i | x_{j(i)})` of a joint law `p`, with the
marginal `P(x_i)` for a parentless `i`. The conditional `P(x_i | x_j)` is
`P(x_i, x_j) / P(x_j)`; where `P(x_j) = 0` the quotient is `0`, and such `x` have `P(x) = 0`.

Formalized by `InformationTheory.DependenceForest.approx`, a definition declared in [MathlibExt/InformationTheory/ChowLiu.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/ChowLiu.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/chow-liu-trees/index.html#approx).

## Nonnegativity of the Chow–Liu approximation

The approximation is nonnegative.

Formalized by `InformationTheory.DependenceForest.approx_nonneg`, a theorem declared in [MathlibExt/InformationTheory/ChowLiu.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/ChowLiu.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/chow-liu-trees/index.html#approx-nonneg).

## Joint law is absolutely continuous w.r.t. its Chow–Liu approximation

`P ≪ P_τ`: the approximation is positive wherever `p` is.

Formalized by `InformationTheory.DependenceForest.approx_pos`, a theorem declared in [MathlibExt/InformationTheory/ChowLiu.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/ChowLiu.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/chow-liu-trees/index.html#approx-pos).

## Chow–Liu approximation sums to one

The approximation is a probability law: `∑_x P_τ(x) = 1`.

Formalized by `InformationTheory.DependenceForest.sum_approx`, a theorem declared in [MathlibExt/InformationTheory/ChowLiu.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/ChowLiu.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/chow-liu-trees/index.html#sum-approx).

## Chow–Liu approximation as a probability mass function

Chow–Liu's approximation `P_τ` as a probability mass function.

Formalized by `InformationTheory.DependenceForest.approxPMF`, a definition declared in [MathlibExt/InformationTheory/ChowLiu.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/ChowLiu.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/chow-liu-trees/index.html#approx-pmf).

## Mutual-information weight of a dependence forest

The mutual-information weight `∑_i I(X_i; X_{j(i)})` of a dependence forest, in bits.

Formalized by `InformationTheory.DependenceForest.weight`, a definition declared in [MathlibExt/InformationTheory/ChowLiu.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/ChowLiu.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/chow-liu-trees/index.html#weight).

## Divergence from the Chow–Liu approximation

The divergence `D(P ‖ P_τ) = ∑_x P(x) log₂ (P(x) / P_τ(x))` of `P` from Chow–Liu's approximation, in bits (`divergence_eq_klDiv`).

Formalized by `InformationTheory.DependenceForest.divergence`, a definition declared in [MathlibExt/InformationTheory/ChowLiu.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/ChowLiu.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/chow-liu-trees/index.html#divergence).

## Chow–Liu divergence as a Kullback–Leibler divergence

`divergence` is Mathlib's Kullback–Leibler divergence `klDiv` of `P` relative to `P_τ`, converted to
bits; the finite alphabet carries the discrete σ-algebra.

Formalized by `InformationTheory.DependenceForest.divergence_eq_klDiv`, a theorem declared in [MathlibExt/InformationTheory/ChowLiu.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/ChowLiu.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/chow-liu-trees/index.html#divergence-eq-kl-div).

## Chow–Liu identity

`D(P ‖ P_τ) = ∑_i H(X_i) - H(X) - ∑_i I(X_i; X_{j(i)})`.

Formalized by `InformationTheory.DependenceForest.divergence_eq`, a theorem declared in [MathlibExt/InformationTheory/ChowLiu.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/ChowLiu.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/chow-liu-trees/index.html#divergence-eq).

## Nonnegativity of the Chow–Liu divergence

The divergence of `P` from Chow–Liu's approximation is nonnegative, so
`∑_i I(X_i; X_{j(i)}) ≤ ∑_i H(X_i) - H(X)` for every dependence forest.

Formalized by `InformationTheory.DependenceForest.divergence_nonneg`, a theorem declared in [MathlibExt/InformationTheory/ChowLiu.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/ChowLiu.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/chow-liu-trees/index.html#divergence-nonneg).

## Chow–Liu optimality

Among dependence forests, a smaller divergence is the same as a
larger mutual-information weight, so minimizing `D(P ‖ P_τ)` over dependence trees is maximizing
the total mutual information `∑_i I(X_i; X_{j(i)})` of their edges.

Formalized by `InformationTheory.DependenceForest.divergence_le_divergence_iff`, a theorem declared in [MathlibExt/InformationTheory/ChowLiu.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/ChowLiu.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/chow-liu-trees/index.html#divergence-le-divergence-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chow–Liu trees](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/chow-liu-trees/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/InformationTheory/entropy-and-mutual-information/chow-liu-trees)
