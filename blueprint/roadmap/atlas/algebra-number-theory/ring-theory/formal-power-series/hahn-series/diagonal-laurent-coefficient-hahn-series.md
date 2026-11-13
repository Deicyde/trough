---
declaration: section
origin: cited
lean: HahnSeries.diagonalLaurentSeries, HahnSeries.coeff_diagonalLaurentSeries, HahnSeries.coeff_coeff_diagonalLaurentSeries, HahnSeries.coeff_coeff_variableDifference_mul, HahnSeries.variableDifferenceUnit, HahnSeries.coe_variableDifferenceUnit, HahnSeries.coe_inv_variableDifferenceUnit, HahnSeries.coe_inv_variableDifferenceUnit_pow_succ
statement: formalized
proof: formalized
---

# Diagonal Laurent-coefficient Hahn series

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/diagonal-laurent-coefficient-hahn-series/index.html).

## Diagonal Laurent-coefficient Hahn series

The Hahn series with coefficient `c y` at inner exponent `d - y` and outer exponent `y`
for every `y ≥ j₀`.

Formalized by `HahnSeries.diagonalLaurentSeries`, a definition declared in [MathlibExt/RingTheory/HahnSeries/DiagonalLaurent.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/DiagonalLaurent.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/diagonal-laurent-coefficient-hahn-series/index.html#diagonal-laurent-series).

## Outer coefficient of a diagonal Laurent series

The outer coefficient of a diagonal Laurent series.

Formalized by `HahnSeries.coeff_diagonalLaurentSeries`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/DiagonalLaurent.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/DiagonalLaurent.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/diagonal-laurent-coefficient-hahn-series/index.html#coeff-diagonal-laurent-series).

## Double coefficients of a diagonal Laurent series

Both coefficients of a diagonal Laurent series, exposing its cutoff and diagonal equation.

Formalized by `HahnSeries.coeff_coeff_diagonalLaurentSeries`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/DiagonalLaurent.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/DiagonalLaurent.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/diagonal-laurent-coefficient-hahn-series/index.html#coeff-coeff-diagonal-laurent-series).

## Multiplying by the variable difference on diagonal coefficients

Multiplication by the difference of the two variables takes a difference of adjacent
diagonal coefficients.

Formalized by `HahnSeries.coeff_coeff_variableDifference_mul`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/DiagonalLaurent.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/DiagonalLaurent.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/diagonal-laurent-coefficient-hahn-series/index.html#coeff-coeff-variable-difference-mul).

## Variable difference as a unit of Hahn series

The formal difference of the inner and outer variables, bundled with its diagonal-series
inverse.

Formalized by `HahnSeries.variableDifferenceUnit`, a definition declared in [MathlibExt/RingTheory/HahnSeries/DiagonalLaurent.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/DiagonalLaurent.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/diagonal-laurent-coefficient-hahn-series/index.html#variable-difference-unit).

## Value of the variable difference unit

The value of `variableDifferenceUnit` is the difference of the two formal variables.

Formalized by `HahnSeries.coe_variableDifferenceUnit`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/DiagonalLaurent.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/DiagonalLaurent.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/diagonal-laurent-coefficient-hahn-series/index.html#coe-variable-difference-unit).

## Inverse of the variable difference as a diagonal series

The inverse of the formal variable difference is its infinite diagonal Laurent series.

Formalized by `HahnSeries.coe_inv_variableDifferenceUnit`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/DiagonalLaurent.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/DiagonalLaurent.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/diagonal-laurent-coefficient-hahn-series/index.html#coe-inv-variable-difference-unit).

## Powers of the inverse variable difference have binomial coefficients

The `(N + 1)`-st power of the inverse variable difference has negative-binomial
coefficients on one diagonal.

Formalized by `HahnSeries.coe_inv_variableDifferenceUnit_pow_succ`, a theorem declared in [MathlibExt/RingTheory/HahnSeries/DiagonalLaurent.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/HahnSeries/DiagonalLaurent.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/diagonal-laurent-coefficient-hahn-series/index.html#coe-inv-variable-difference-unit-pow-suc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Diagonal Laurent-coefficient Hahn series](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/hahn-series/diagonal-laurent-coefficient-hahn-series/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/formal-power-series/hahn-series/diagonal-laurent-coefficient-hahn-series)
