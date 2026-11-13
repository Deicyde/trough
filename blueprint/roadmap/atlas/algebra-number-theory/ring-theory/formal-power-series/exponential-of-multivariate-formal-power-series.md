---
declaration: section
origin: cited
lean: MvPowerSeries.expTrunc, MvPowerSeries.expOfConstantCoeffZero, MvPowerSeries.expOfConstantCoeffZero_eq_subst, MvPowerSeries.coeff_expOfConstantCoeffZero, MvPowerSeries.coeff_expOfConstantCoeffZero_degree, MvPowerSeries.constantCoeff_expOfConstantCoeffZero, MvPowerSeries.expOfConstantCoeffZero_zero, MvPowerSeries.map_expOfConstantCoeffZero
statement: formalized
proof: formalized
---

# Exponential of multivariate formal power series

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html).

## Truncated exponential of a multivariate power series

The finite sum `∑ n < N, wⁿ/n!`, defined without a constant coefficient restriction.

Formalized by `MvPowerSeries.expTrunc`, a definition declared in [MathlibExt/RingTheory/MvPowerSeries/Exponential.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/Exponential.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#exp-trunc).

## Exponential of a power series with zero constant coefficient

The formal exponential of a series with zero constant coefficient, obtained
by substituting it into Mathlib's canonical exponential power series.

Formalized by `MvPowerSeries.expOfConstantCoeffZero`, a definition declared in [MathlibExt/RingTheory/MvPowerSeries/Exponential.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/Exponential.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#exp-of-constant-coeff-zero).

## Multivariate exponential as substitution into exp

The exponential API is the canonical univariate exponential substituted at `w`.

Formalized by `MvPowerSeries.expOfConstantCoeffZero_eq_subst`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/Exponential.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/Exponential.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#exp-of-constant-coeff-zero-eq-subst).

## Coefficients of the exponential via truncation

A coefficient of the exponential is computed by any truncation extending past its degree.
This is the exact finite-sum formula used by the source's degreewise constructor.

Formalized by `MvPowerSeries.coeff_expOfConstantCoeffZero`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/Exponential.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/Exponential.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#coeff-exp-of-constant-coeff-zero).

## Coefficient of the exponential in a given degree

In particular, the coefficient of degree `d.degree` uses exactly the terms `n ≤ d.degree`.

Formalized by `MvPowerSeries.coeff_expOfConstantCoeffZero_degree`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/Exponential.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/Exponential.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#coeff-exp-of-constant-coeff-zero-degree).

## Constant coefficient of the formal exponential is one

The constant coefficient of the formal exponential is one.

Formalized by `MvPowerSeries.constantCoeff_expOfConstantCoeffZero`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/Exponential.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/Exponential.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#constant-coeff-exp-of-constant-coeff-zer).

## Exponential of the zero series is one

The exponential of the zero series is one.

Formalized by `MvPowerSeries.expOfConstantCoeffZero_zero`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/Exponential.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/Exponential.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#exp-of-constant-coeff-zero-zero).

## Coefficient ring maps commute with the formal exponential

Applying a coefficient ring homomorphism commutes with the formal exponential.

Formalized by `MvPowerSeries.map_expOfConstantCoeffZero`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/Exponential.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/Exponential.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#map-exp-of-constant-coeff-zero).

## Exponential of a variable

Substituting a variable recovers the canonical exponential in that variable.

Formalized by `MvPowerSeries.expOfConstantCoeffZero_X`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/Exponential.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/Exponential.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#exp-of-constant-coeff-zero-x).

## Formal exponential turns sums into products

The formal exponential carries sums of series with zero constant coefficient to products.

Formalized by `MvPowerSeries.expOfConstantCoeffZero_add`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/Exponential.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/Exponential.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#exp-of-constant-coeff-zero-add).

## Partial derivative of the truncated exponential

The partial derivative of the finite exponential sum containing the terms `w ^ n / n!` for
`n ≤ N` is the derivative of its exponent times the sum containing those terms for `n < N`.

Formalized by `MvPowerSeries.pderiv_expTrunc`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/ExponentialDerivative.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/ExponentialDerivative.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#pderiv-exp-trunc).

## Partial derivative of the formal exponential

The partial derivative of the canonical exponential is the derivative of its exponent times
the exponential.

Formalized by `MvPowerSeries.pderiv_expOfConstantCoeffZero`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/ExponentialDerivative.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/ExponentialDerivative.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#pderiv-exp-of-constant-coeff-zero).

## Ring maps commute with truncated exponentials

A ring homomorphism between multivariate power-series rings commutes with
finite exponential truncations.

Formalized by `MvPowerSeries.map_expTrunc`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/ExponentialHom.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/ExponentialHom.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#map-exp-trunc).

## Filtration-preserving endomorphisms commute with the formal exponential

A ring endomorphism preserving the total-degree coefficient filtration
commutes with the formal exponential. The filtration premise itself implies
that the image of a zero-constant series again has zero constant coefficient.

Formalized by `MvPowerSeries.hom_expOfConstantCoeffZero`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/ExponentialHom.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/ExponentialHom.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#hom-exp-of-constant-coeff-zero).

## Coefficients of a weighted rescaling of a rational power series

Mapping rational coefficients and rescaling variable `i` by
`ε ^ wt (Finsupp.single i 1)` multiplies coefficient `d` by `ε ^ wt d`.

Formalized by `MvPowerSeries.coeff_rescale_map_of_weight`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/WeightedRescale.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/WeightedRescale.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#coeff-rescale-map-of-weight).

## Characterization of weighted rescalings of a power series

A series has the weighted coefficients of `q` exactly when it is the
canonical coefficient map of `q` followed by the corresponding rescaling.

Formalized by `MvPowerSeries.eq_rescale_map_of_weight_iff`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/WeightedRescale.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/WeightedRescale.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#eq-rescale-map-of-weight-iff).

## Weighted rescaling commutes with truncated exponentials

Weighted coefficient mapping and rescaling commutes with every finite
exponential truncation, without a constant coefficient restriction.

Formalized by `MvPowerSeries.expTrunc_rescale_map_of_weight`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/WeightedExponential.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/WeightedExponential.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#exp-trunc-rescale-map-of-weight).

## Coefficients of weighted rescaling of truncated exponentials

The coefficient form of weighted finite exponential commutation. It
preserves the source's degreewise expression for arbitrary input series.

Formalized by `MvPowerSeries.coeff_expTrunc_rescale_map_of_weight`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/WeightedExponential.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/WeightedExponential.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#coeff-exp-trunc-rescale-map-of-weight).

## Weighted rescaling commutes with the formal exponential

On the zero-constant domain, weighted coefficient mapping and rescaling
commutes with the lawful full formal exponential.

Formalized by `MvPowerSeries.expOfConstantCoeffZero_rescale_map_of_weight`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/WeightedExponential.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/WeightedExponential.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#exp-of-constant-coeff-zero-rescale-map-o).

## Weighted coefficient equality transfers zero constant coefficient

Weighted coefficient equality transfers a zero constant coefficient from
the rational source series to the target series.

Formalized by `MvPowerSeries.constantCoeff_eq_zero_of_weight`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/WeightedExponential.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/WeightedExponential.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#constant-coeff-eq-zero-of-weight).

## Weighted coefficient relation passes to formal exponentials

If `w` has the coefficients of `q` scaled by an additive weight, then the
same coefficient relation holds for their lawful formal exponentials. The
coefficient hypothesis and `q`'s zero constant imply the required premise for
`w`; no separate zero-constant assumption on `w` is needed.

Formalized by `MvPowerSeries.coeff_expOfConstantCoeffZero_of_weight`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/WeightedExponential.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/WeightedExponential.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html#coeff-exp-of-constant-coeff-zero-of-weig).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exponential of multivariate formal power series](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/formal-power-series/exponential-of-multivariate-formal-power-series)
