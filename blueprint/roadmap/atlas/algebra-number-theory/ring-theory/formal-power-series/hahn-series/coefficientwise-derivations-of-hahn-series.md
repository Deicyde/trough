---
declaration: section
origin: cited
lean: HahnSeries.coefficientLinearMap, HahnSeries.coeff_coefficientLinearMap, HahnSeries.support_coefficientLinearMap, HahnSeries.coefficientDerivation, HahnSeries.coeff_coefficientDerivation, HahnSeries.coefficientDerivation_zero, HahnSeries.coefficientDerivation_single, HahnSeries.coefficientDerivation_C
statement: formalized
proof: formalized
---

# Coefficientwise derivations of Hahn series

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/coefficientwise-derivations-of-hahn-series/index.html).

## Coefficientwise linear operator on Hahn series

Apply a coefficient derivation to a Hahn series as an `R`-linear operator.

Formalized by `HahnSeries.coefficientLinearMap`, a definition declared in [MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/coefficientwise-derivations-of-hahn-series/index.html#coefficient-linear-map).

## Coefficient formula for the coefficientwise linear operator

The coefficient formula for the linear operator underlying the lifted derivation.

Formalized by `HahnSeries.coeff_coefficientLinearMap`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/coefficientwise-derivations-of-hahn-series/index.html#coeff-coefficient-linear-map).

## Coefficientwise linear operator does not enlarge the support

Acting on coefficients cannot introduce new exponents into the support.

Formalized by `HahnSeries.support_coefficientLinearMap`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/coefficientwise-derivations-of-hahn-series/index.html#support-coefficient-linear-map).

## Coefficientwise derivation of Hahn series

Extend a derivation of the coefficient algebra by applying it to each coefficient.

Formalized by `HahnSeries.coefficientDerivation`, a definition declared in [MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/coefficientwise-derivations-of-hahn-series/index.html#coefficient-derivation).

## Coefficients of the coefficientwise derivation

The coefficient of the lifted derivation is the derivative of that coefficient.

Formalized by `HahnSeries.coeff_coefficientDerivation`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/coefficientwise-derivations-of-hahn-series/index.html#coeff-coefficient-derivation).

## Coefficientwise lift of the zero derivation

The lift of the zero derivation is zero.

Formalized by `HahnSeries.coefficientDerivation_zero`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/coefficientwise-derivations-of-hahn-series/index.html#coefficient-derivation-zero).

## Coefficientwise derivation of a single-term series

A one-term series keeps its exponent and differentiates its coefficient.

Formalized by `HahnSeries.coefficientDerivation_single`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/coefficientwise-derivations-of-hahn-series/index.html#coefficient-derivation-single).

## Coefficientwise derivation of a constant series

On a constant series, the lift acts on its constant coefficient.

Formalized by `HahnSeries.coefficientDerivation_C`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/coefficientwise-derivations-of-hahn-series/index.html#coefficient-derivation-c).

## Commuting derivations lift to commuting coefficientwise derivations

Commuting coefficient derivations lift to commuting derivations of Hahn series.

Formalized by `HahnSeries.coefficientDerivation_commute`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/CoefficientDerivation.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/coefficientwise-derivations-of-hahn-series/index.html#coefficient-derivation-commute).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Coefficientwise derivations of Hahn series](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/coefficientwise-derivations-of-hahn-series/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/formal-power-series/hahn-series/coefficientwise-derivations-of-hahn-series)
