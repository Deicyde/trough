---
declaration: section
origin: cited
lean: AddMonoidAlgebra.weightedDerivation, AddMonoidAlgebra.coeff_weightedDerivation, AddMonoidAlgebra.weightedDerivation_single, AddMonoidAlgebra.weightedDerivation_zero
statement: formalized
proof: formalized
---

# Weighted derivations of monoid algebras

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/weighted-derivations-of-monoid-algebras/index.html).

## Weighted derivation of an additive monoid algebra

Multiply the coefficient at each exponent by an additive weight of that exponent.

Formalized by `AddMonoidAlgebra.weightedDerivation`, a definition declared in [MathlibExt/Algebra/MonoidAlgebra/WeightedDerivation.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/MonoidAlgebra/WeightedDerivation.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/weighted-derivations-of-monoid-algebras/index.html#weighted-derivation).

## Coefficients of a weighted derivation

The coefficient at `g` is multiplied by the weight of `g`.

Formalized by `AddMonoidAlgebra.coeff_weightedDerivation`, a theorem declared in [MathlibExt/Algebra/MonoidAlgebra/WeightedDerivation.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/MonoidAlgebra/WeightedDerivation.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/weighted-derivations-of-monoid-algebras/index.html#coeff-weighted-derivation).

## Weighted derivation of a basis term

A basis term keeps its exponent and has its coefficient multiplied by the weight.

Formalized by `AddMonoidAlgebra.weightedDerivation_single`, a theorem declared in [MathlibExt/Algebra/MonoidAlgebra/WeightedDerivation.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/MonoidAlgebra/WeightedDerivation.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/weighted-derivations-of-monoid-algebras/index.html#weighted-derivation-single).

## Weighted derivation with zero weight

The zero weight determines the zero derivation.

Formalized by `AddMonoidAlgebra.weightedDerivation_zero`, a theorem declared in [MathlibExt/Algebra/MonoidAlgebra/WeightedDerivation.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/MonoidAlgebra/WeightedDerivation.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/weighted-derivations-of-monoid-algebras/index.html#weighted-derivation-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weighted derivations of monoid algebras](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/weighted-derivations-of-monoid-algebras/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/polynomials/weighted-derivations-of-monoid-algebras)
