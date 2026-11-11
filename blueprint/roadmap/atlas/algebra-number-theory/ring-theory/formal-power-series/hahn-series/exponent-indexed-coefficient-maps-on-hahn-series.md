---
declaration: section
origin: cited
lean: HahnSeries.gradedCoefficientMap, HahnSeries.coeff_gradedCoefficientMap, HahnSeries.support_gradedCoefficientMap, HahnSeries.gradedCoefficientMap_zero_family, HahnSeries.gradedCoefficientMap_single, HahnSeries.gradedCoefficientMap_C, HahnSeries.gradedCoefficientMap_mul
statement: formalized
proof: formalized
---

# Exponent-indexed coefficient maps on Hahn series

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/exponent-indexed-coefficient-maps-on-hahn-series/index.html).

## Exponent-indexed coefficient map on Hahn series

Apply the map indexed by each exponent to the coefficient at that exponent.

Formalized by `HahnSeries.gradedCoefficientMap`, a definition declared in [MathlibExt/RingTheory/HahnSeries/GradedCoefficientMap.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/HahnSeries/GradedCoefficientMap.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/exponent-indexed-coefficient-maps-on-hahn-series/index.html#graded-coefficient-map).

## Coefficient formula for an exponent-indexed coefficient map

The coefficient formula for an exponent-indexed coefficient map.

Formalized by `HahnSeries.coeff_gradedCoefficientMap`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/GradedCoefficientMap.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/HahnSeries/GradedCoefficientMap.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/exponent-indexed-coefficient-maps-on-hahn-series/index.html#coeff-graded-coefficient-map).

## Exponent-indexed coefficient maps do not enlarge the support

Acting coefficientwise cannot introduce new exponents into the support.

Formalized by `HahnSeries.support_gradedCoefficientMap`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/GradedCoefficientMap.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/HahnSeries/GradedCoefficientMap.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/exponent-indexed-coefficient-maps-on-hahn-series/index.html#support-graded-coefficient-map).

## Exponent-indexed coefficient map of the zero family

The family consisting of zero maps induces the zero additive map.

Formalized by `HahnSeries.gradedCoefficientMap_zero_family`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/GradedCoefficientMap.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/HahnSeries/GradedCoefficientMap.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/exponent-indexed-coefficient-maps-on-hahn-series/index.html#graded-coefficient-map-zero-family).

## Exponent-indexed coefficient map on a single-term series

A one-term series keeps its exponent and applies the map indexed by that exponent.

Formalized by `HahnSeries.gradedCoefficientMap_single`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/GradedCoefficientMap.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/HahnSeries/GradedCoefficientMap.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/exponent-indexed-coefficient-maps-on-hahn-series/index.html#graded-coefficient-map-single).

## Exponent-indexed coefficient map on a constant series

On a constant series, the map indexed by zero acts on the constant coefficient.

Formalized by `HahnSeries.gradedCoefficientMap_C`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/GradedCoefficientMap.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/HahnSeries/GradedCoefficientMap.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/exponent-indexed-coefficient-maps-on-hahn-series/index.html#graded-coefficient-map-c).

## Product rule for graded Leibniz coefficient maps

An exponent-indexed coefficient map satisfying the graded Leibniz identity obeys the product
rule on Hahn series.

Formalized by `HahnSeries.gradedCoefficientMap_mul`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/GradedCoefficientMap.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/HahnSeries/GradedCoefficientMap.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/exponent-indexed-coefficient-maps-on-hahn-series/index.html#graded-coefficient-map-mul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exponent-indexed coefficient maps on Hahn series](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/exponent-indexed-coefficient-maps-on-hahn-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/formal-power-series/hahn-series/exponent-indexed-coefficient-maps-on-hahn-series)
