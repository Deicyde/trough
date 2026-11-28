---
catalog: module
lean: CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanInterpolate_sound
statement: formalized
proof: formalized
---

# Lee-O'Sullivan Interpolation Soundness

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Soundness`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Soundness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Soundness.lean), by Valerii Huhnin.

> Soundness for the executable Lee-O'Sullivan interpolation operation.

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanInterpolate_sound` (theorem, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Soundness.lean#L32))

> Soundness for the executable Lee-O'Sullivan interpolation operation.

```lean
theorem leeOSullivanInterpolate_sound
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (reducer : ShiftedRowReducerContext F)
    {points : Array (F × F)} {params : GSInterpParams} {Q : CBivariate F}
    (h : leeOSullivanInterpolate V E reducer points params = some Q) :
    ValidInterpolationWitness points params Q
```

## Depends on

- [Executable Lee-O'Sullivan Interpolation](../algorithm.md)

## Proof depends on

- [Lee-O'Sullivan Candidate Normalization](normalization.md)
- [Lee-O'Sullivan Row-Span Transport Helpers](rows.md)
- [Lee-O'Sullivan Row Selection Helpers](selection.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Soundness.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Soundness.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Soundness.json)
