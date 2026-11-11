---
declaration: section
origin: cited
lean: HahnSeries.ofAddMonoidAlgebra, HahnSeries.coeff_ofAddMonoidAlgebra, HahnSeries.ofAddMonoidAlgebra_apply, HahnSeries.ofAddMonoidAlgebra_injective, HahnSeries.ofBivariateAddMonoidAlgebra, HahnSeries.coeff_coeff_ofBivariateAddMonoidAlgebra, HahnSeries.ofBivariateAddMonoidAlgebra_injective
statement: formalized
proof: formalized
---

# Finite monoid algebras as Hahn series

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/finite-monoid-algebras-as-hahn-series/index.html).

## Finite

## Embedding of a finite additive monoid algebra into Hahn series

Embed a finite additive monoid algebra into Hahn series.

Formalized by `HahnSeries.ofAddMonoidAlgebra`, a definition declared in [MathlibExt/RingTheory/HahnSeries/MonoidAlgebra.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/HahnSeries/MonoidAlgebra.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/finite-monoid-algebras-as-hahn-series/index.html#of-add-monoid-algebra).

## Monoid algebra embedding into Hahn series preserves coefficients

The finite Hahn embedding preserves every coefficient.

Formalized by `HahnSeries.coeff_ofAddMonoidAlgebra`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/MonoidAlgebra.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/HahnSeries/MonoidAlgebra.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/finite-monoid-algebras-as-hahn-series/index.html#coeff-of-add-monoid-algebra).

## Monoid algebra embedding into Hahn series as a ring map

The finite Hahn embedding is Mathlib's `ofFinsupp`, bundled as a ring homomorphism.

Formalized by `HahnSeries.ofAddMonoidAlgebra_apply`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/MonoidAlgebra.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/HahnSeries/MonoidAlgebra.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/finite-monoid-algebras-as-hahn-series/index.html#of-add-monoid-algebra-apply).

## Injectivity of the monoid algebra embedding into Hahn series

The finite Hahn embedding is injective.

Formalized by `HahnSeries.ofAddMonoidAlgebra_injective`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/MonoidAlgebra.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/HahnSeries/MonoidAlgebra.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/finite-monoid-algebras-as-hahn-series/index.html#of-add-monoid-algebra-injective).

## Embedding of a bivariate monoid algebra into Hahn series

Embed a bivariate finite monoid algebra into Hahn series, with the second coordinate outer.

Formalized by `HahnSeries.ofBivariateAddMonoidAlgebra`, a definition declared in [MathlibExt/RingTheory/HahnSeries/MonoidAlgebra.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/HahnSeries/MonoidAlgebra.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/finite-monoid-algebras-as-hahn-series/index.html#of-bivariate-add-monoid-algebra).

## Coefficients of the bivariate monoid algebra embedding

The two coefficient projections of the bivariate embedding recover the original coefficient.

Formalized by `HahnSeries.coeff_coeff_ofBivariateAddMonoidAlgebra`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/MonoidAlgebra.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/HahnSeries/MonoidAlgebra.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/finite-monoid-algebras-as-hahn-series/index.html#coeff-coeff-of-bivariate-add-monoid-alge).

## Injectivity of the bivariate monoid algebra embedding

The bivariate finite Hahn embedding is injective.

Formalized by `HahnSeries.ofBivariateAddMonoidAlgebra_injective`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/MonoidAlgebra.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/HahnSeries/MonoidAlgebra.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/finite-monoid-algebras-as-hahn-series/index.html#of-bivariate-add-monoid-algebra-injectiv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite monoid algebras as Hahn series](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/finite-monoid-algebras-as-hahn-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/formal-power-series/hahn-series/finite-monoid-algebras-as-hahn-series)
