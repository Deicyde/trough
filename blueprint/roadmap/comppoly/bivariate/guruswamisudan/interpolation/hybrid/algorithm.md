---
catalog: module
lean: CompPoly.GuruswamiSudan.Hybrid.hybridPositiveInterpolate, CompPoly.GuruswamiSudan.Hybrid.hybridInterpolate
statement: formalized
proof: formalized
---

# Hybrid Guruswami-Sudan Interpolation

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.Hybrid.Algorithm`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/Hybrid/Algorithm.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Hybrid/Algorithm.lean), by Valerii Huhnin.

> Output-sensitive interpolation backend combining the adaptive Lee-O'Sullivan
> route with the order-driven approximant-basis route through a ski-rental
> budget policy.
>
> The Mulders-Storjohann reduction of the Lee-O'Sullivan basis terminates after
> a number of steps that vanishes on codewords and scales with the distance of
> the received word from the code, while the approximant-basis backend costs
> the same on every input. The hybrid runs the reduction with a calibrated step
> budget `B` as fuel; if the budget is exhausted before the basis is
> conflict-free, it falls back to the approximant solver, so the total cost is
> within a constant factor of the cheaper route on every input.
>
> The budget is the entire fuel policy: the reduction loop stops by itself as
> soon as the basis is conflict-free, so unused fuel is free and any cap below
> `B` could only trigger premature fallback. (In particular the excess of the
> initial shifted-degree sum over the weak-Popov floor is *not* a usable cap:
> the step count includes leading-position moves that leave the shifted-degree
> sum unchanged, so reductions routinely need more steps than that excess.)
>
> The dispatch affects performance only: both branches are complete verified
> interpolators, and `Interpolation/Hybrid/Correctness.lean` shows the hybrid
> result always coincides with one of them.
>
> ## References
>
> * [Karlin, A. R., Manasse, M. S., Rudolph, L., and Sleator, D. D.,
>     *Competitive snoopy caching*][KMRS88]

`CompPoly.GuruswamiSudan.Hybrid.hybridPositiveInterpolate` (definition, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Hybrid/Algorithm.lean#L61))

> Positive-`Y`-weight hybrid interpolation branch: reduce the
> Lee-O'Sullivan basis with the budgeted fuel and keep the result when it
> reached shifted weak Popov form (no leading conflict remains), otherwise fall
> back to the approximant-basis solver.

```lean
def hybridPositiveInterpolate
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (solver : ModularSolutionBasisContext F)
    (budget : GSInterpParams → Nat)
    (points : Array (F × F)) (params : GSInterpParams) :
    Option (CBivariate F)
```

`CompPoly.GuruswamiSudan.Hybrid.hybridInterpolate` (definition, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Hybrid/Algorithm.lean#L96))

> Hybrid interpolation with the shared low-message branch.

```lean
def hybridInterpolate
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (solver : ModularSolutionBasisContext F)
    (budget : GSInterpParams → Nat)
    (points : Array (F × F)) (params : GSInterpParams) :
    Option (CBivariate F)
```

## Depends on

- [Executable Approximant-Basis Interpolation](../approximantbasis/algorithm.md)
- [Executable Lee-O'Sullivan Interpolation](../leeosullivan/algorithm.md)
- [Mulders-Storjohann Shifted Row Reduction](../../../../linearalgebra/polynomialmatrix/muldersstorjohann.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/Hybrid/Algorithm.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Hybrid/Algorithm.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.Hybrid.Algorithm.json)
