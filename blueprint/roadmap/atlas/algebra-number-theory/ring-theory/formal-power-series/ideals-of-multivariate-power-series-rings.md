---
declaration: section
origin: cited
lean: MvPowerSeries.mem_span_C_sup_ofList_take_iff, MvPowerSeries.span_range_X_eq_ker_constantCoeff
statement: formalized
proof: formalized
---

# Ideals of multivariate power series rings

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/ideals-of-multivariate-power-series-rings/index.html).

## Membership in the span of a constant and initial variables

A power series lies in the span of `C ϖ` and the first `k` variables
exactly when every coefficient of a monomial supported on the last `n - k`
variables is divisible by `ϖ`.

Formalized by `MvPowerSeries.mem_span_C_sup_ofList_take_iff`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/Span.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/Span.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/ideals-of-multivariate-power-series-rings/index.html#mem-span-c-sup-of-list-take-iff).

## The variables span the kernel of the constant coefficient map

The kernel of the constant coefficient map on multivariate power series
is the span of the variables.

Formalized by `MvPowerSeries.span_range_X_eq_ker_constantCoeff`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/Span.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/Span.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/ideals-of-multivariate-power-series-rings/index.html#span-range-x-eq-ker-constant-coeff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ideals of multivariate power series rings](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/ideals-of-multivariate-power-series-rings/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/formal-power-series/ideals-of-multivariate-power-series-rings)
