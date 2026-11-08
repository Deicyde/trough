---
declaration: theorem
origin: cited
lean: TauCeti.Montgomery.isElliptic_model_suyama_iff
statement: formalized
proof: formalized
---

# Suyama's exact ellipticity criterion

Under the denominator restrictions, precisely
these five factors detect singular models. No odd characteristic is excluded.

```lean
TauCeti.Montgomery.isElliptic_model_suyama_iff.{u_1} {K : Type u_1} [Field K] {σ : K} (h₂ : 2 ≠ 0)
  (hσ : σ ≠ 0) (hu : σ ^ 2 ≠ 5) :
  (TauCeti.Montgomery.model (TauCeti.Montgomery.suyamaA σ)
        (TauCeti.Montgomery.suyamaB σ)).IsElliptic ↔
    (σ ^ 2 - 1) * (σ ^ 2 - 9) * (σ ^ 2 - 25) * (9 * σ ^ 2 - 25) * (σ ^ 2 + 5) ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Montgomery.isElliptic_model_suyama_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Suyama/Basic.html#TauCeti.Montgomery.isElliptic_model_suyama_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Montgomery.isElliptic_model_suyama_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Suyama/Basic.html#TauCeti.Montgomery.isElliptic_model_suyama_iff)
- [Source of `TauCeti.Montgomery.isElliptic_model_suyama_iff` in TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Suyama/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Suyama/Basic.lean#L158)
