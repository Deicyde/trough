---
catalog: module
lean: CompPoly.GuruswamiSudan.LeeOSullivan.normalizeLeeCandidate?_sound_of_raw, CompPoly.GuruswamiSudan.LeeOSullivan.normalizeLeeCandidate?_some_of_raw
statement: formalized
proof: formalized
---

# Lee-O'Sullivan Candidate Normalization

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Normalization`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Normalization.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Normalization.lean), by Valerii Huhnin.

> Soundness and existence facts for normalizing raw Lee-O'Sullivan candidates.

`CompPoly.GuruswamiSudan.LeeOSullivan.normalizeLeeCandidate?_sound_of_raw` (theorem, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Normalization.lean#L31))

> Normalizing a bounded raw Lee candidate preserves the interpolation witness
> contract when the raw candidate already satisfies the multiplicity constraints.

```lean
theorem normalizeLeeCandidate?_sound_of_raw
    {points : Array (F × F)} {params : GSInterpParams}
    {rawQ Q : CBivariate F}
    (hHigh : ¬ params.messageDegree ≤ 1)
    (hdeg :
      CBivariate.natWeightedDegree rawQ 1 (yWeight params) ≤
        params.weightedDegreeBound)
    (hmult :
      CBivariate.SatisfiesMultiplicityConstraints rawQ points params.multiplicity)
    (hnorm : normalizeLeeCandidate? params rawQ = some Q) :
    ValidInterpolationWitness points params Q
```

`CompPoly.GuruswamiSudan.LeeOSullivan.normalizeLeeCandidate?_some_of_raw` (theorem, [line 101](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Normalization.lean#L101))

> A nonzero bounded raw Lee candidate can be normalized by the shared
> coefficient-vector policy.

```lean
theorem normalizeLeeCandidate?_some_of_raw
    {params : GSInterpParams} {rawQ : CBivariate F}
    (hHigh : ¬ params.messageDegree ≤ 1)
    (hne : rawQ ≠ 0)
    (hdeg :
      CBivariate.natWeightedDegree rawQ 1 (yWeight params) ≤
        params.weightedDegreeBound) :
    ∃ Q, normalizeLeeCandidate? params rawQ = some Q
```

## Depends on

- [Executable Lee-O'Sullivan Interpolation](../algorithm.md)

## Proof depends on

- [Dense Guruswami-Sudan Interpolation Correctness](../../dense/correctness.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Normalization.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Normalization.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Normalization.json)
