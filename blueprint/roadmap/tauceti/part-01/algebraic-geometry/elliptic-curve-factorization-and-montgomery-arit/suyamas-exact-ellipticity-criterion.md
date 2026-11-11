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

- [TauCeti.Montgomery.model](tauceti-montgomery-model.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Montgomery.isElliptic_model_suyama_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Suyama/Basic.html#TauCeti.Montgomery.isElliptic_model_suyama_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Montgomery.isElliptic_model_suyama_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Suyama/Basic.html#TauCeti.Montgomery.isElliptic_model_suyama_iff)
- [Source of `TauCeti.Montgomery.isElliptic_model_suyama_iff` in TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Suyama/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Suyama/Basic.lean#L158)
- [Tau Ceti roadmap status: Elliptic-curve factorization and Montgomery arithmetic](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ECM/STATUS.md)
