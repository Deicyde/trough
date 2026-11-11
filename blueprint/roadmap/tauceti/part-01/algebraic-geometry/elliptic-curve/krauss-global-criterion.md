---
declaration: theorem
origin: cited
lean: TauCeti.krausGlobalCondition_iff_exists_integralModel
statement: formalized
proof: formalized
---

# Kraus's global criterion

Let `O` be a Dedekind domain with fraction field `K`, in which
`2` and `3` are invertible, and assume `O` has a height-one prime, as the ring of integers of a
number field does. Then the pair `(c₄, c₆)` is the pair of `c`-invariants of a nonsingular
Weierstrass equation with coefficients in `O` exactly when Kraus's local condition holds at every
height-one prime.

The equation produced is the `(b₂/12, a₁/2, a₃/2)`-transform of `ofCInvariants c₄ c₆` for elements
`a₁`, `b₂`, `a₃` of `O` approximating the local witnesses modulo `12`. Without a height-one prime
the condition is vacuous and the statement fails, since nothing then forces `c₄³ ≠ c₆²`.

```lean
TauCeti.krausGlobalCondition_iff_exists_integralModel.{u_2, u_3} {K : Type u_2} [Field K]
  {c₄ c₆ : K} {O : Type u_3} [CommRing O] [IsDedekindDomain O] [Algebra O K] [IsFractionRing O K]
  [Invertible 2] [Invertible 3] [Nonempty (IsDedekindDomain.HeightOneSpectrum O)] :
  TauCeti.KrausGlobalCondition O c₄ c₆ ↔
    ∃ W, WeierstrassCurve.IsIntegral O W ∧ W.c₄ = c₄ ∧ W.c₆ = c₆ ∧ W.Δ ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Chinese remainder theorem at maximal ideals, after localization](../../ring-theory/part-02/other-results/part-01/chinese-remainder-theorem-at-maximal-ideals-afte.md)
- [Kraus's local criterion](krauss-local-criterion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.krausGlobalCondition_iff_exists_integralModel`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GlobalModels/Kraus.html#TauCeti.krausGlobalCondition_iff_exists_integralModel).

## Sources

- [Tau Ceti documentation: `TauCeti.krausGlobalCondition_iff_exists_integralModel`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GlobalModels/Kraus.html#TauCeti.krausGlobalCondition_iff_exists_integralModel)
- [Source of `TauCeti.krausGlobalCondition_iff_exists_integralModel` in TauCeti/AlgebraicGeometry/EllipticCurve/GlobalModels/Kraus.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/GlobalModels/Kraus.lean#L348)
