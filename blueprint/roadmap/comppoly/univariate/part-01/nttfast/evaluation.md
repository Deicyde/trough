---
catalog: module
lean: CompPoly.CPolynomial.NTTFast.Plan.forwardImpl_eq_bitRevPermute_evalOnDomain
statement: formalized
proof: formalized
---

# NTTFast and Evaluation

`CompPoly.Univariate.NTTFast.Evaluation`, in [CompPoly/Univariate/NTTFast/Evaluation.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTTFast/Evaluation.lean), by Valerii Huhnin.

> Bridge theorem declarations deriving NTTFast evaluation facts from the shared NTT
> specification layer.

`CompPoly.CPolynomial.NTTFast.Plan.forwardImpl_eq_bitRevPermute_evalOnDomain` (theorem, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTTFast/Evaluation.lean#L33))

> …

```lean
theorem forwardImpl_eq_bitRevPermute_evalOnDomain
    (P : Plan R) (hP : WellFormed P) (p : CPolynomial.Raw R)
    (hdeg : p.toPoly.natDegree < P.domain.n) :
    forwardImpl P p =
      NTT.Transform.bitRevPermute P.domain (NTT.evalOnDomain P.domain p)
```

## Depends on

- [NTT and Evaluation](../ntt/evaluation.md)
- [Basic NTTFast correctness facts](correctness/basic.md)

## Proof depends on

- [NTTFast multiplication correctness](correctness/pipeline.md)

## Sources

- [CompPoly/Univariate/NTTFast/Evaluation.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTTFast/Evaluation.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTTFast.Evaluation.json)
