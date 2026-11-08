---
declaration: theorem
origin: cited
lean: TauCeti.krausLocalCondition_iff_exists_integralModel
statement: formalized
proof: formalized
---

# Kraus's local criterion

For a local ring `R` with an algebra map to a field `K` in which
`2` and `3` are invertible, the pair `(c₄, c₆)` is the pair of `c`-invariants of a nonsingular
Weierstrass equation with coefficients in `R` exactly when Kraus's local condition holds.

The correspondence is concrete in both directions: a witness of `KrausLocalCondition` is a change
of variables carrying `ofCInvariants c₄ c₆` to an equation with coefficients in `R`, and that
transform is the model the equivalence produces.

```lean
TauCeti.krausLocalCondition_iff_exists_integralModel.{u_1, u_2} {R : Type u_1} [CommRing R]
  {K : Type u_2} [Field K] [Algebra R K] {c₄ c₆ : K} [Invertible 2] [Invertible 3] [IsLocalRing R] :
  TauCeti.KrausLocalCondition R c₄ c₆ ↔
    ∃ W, WeierstrassCurve.IsIntegral R W ∧ W.c₄ = c₄ ∧ W.c₆ = c₆ ∧ W.Δ ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.krausLocalCondition_iff_exists_integralModel`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GlobalModels/Kraus.html#TauCeti.krausLocalCondition_iff_exists_integralModel).

## Sources

- [Tau Ceti documentation: `TauCeti.krausLocalCondition_iff_exists_integralModel`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GlobalModels/Kraus.html#TauCeti.krausLocalCondition_iff_exists_integralModel)
- [Source of `TauCeti.krausLocalCondition_iff_exists_integralModel` in TauCeti/AlgebraicGeometry/EllipticCurve/GlobalModels/Kraus.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/GlobalModels/Kraus.lean#L231)
