---
declaration: theorem
origin: cited
lean: WeierstrassCurve.formalThirdRootEval_relation
statement: formalized
proof: formalized
---

# Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient

the third root satisfies
`(1 + a₂λ + a₄λ² + a₆λ³)(t₃ + t₁ + t₂) = -(a₁λ + a₂ν + a₃λ² + 2a₄λν + 3a₆λ²ν)`.

```lean
WeierstrassCurve.formalThirdRootEval_relation.{u_1} {O : Type u_1} [CommRing O] [UniformSpace O]
  [IsUniformAddGroup O] [CompleteSpace O] [T2Space O] [IsTopologicalRing O] [IsLinearTopology O O]
  (W : WeierstrassCurve O) {t₁ t₂ : O} (h₁ : PowerSeries.HasEval t₁) (h₂ : PowerSeries.HasEval t₂) :
  (1 + W.a₂ * W.formalSlopeEval t₁ t₂ + W.a₄ * W.formalSlopeEval t₁ t₂ ^ 2 +
        W.a₆ * W.formalSlopeEval t₁ t₂ ^ 3) *
      (W.formalThirdRootEval t₁ t₂ + t₁ + t₂) =
    -(W.a₁ * W.formalSlopeEval t₁ t₂ + W.a₂ * W.formalInterceptEval t₁ t₂ +
            W.a₃ * W.formalSlopeEval t₁ t₂ ^ 2 +
          2 * W.a₄ * W.formalSlopeEval t₁ t₂ * W.formalInterceptEval t₁ t₂ +
        3 * W.a₆ * W.formalSlopeEval t₁ t₂ ^ 2 * W.formalInterceptEval t₁ t₂)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.formalThirdRootEval_relation`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/PairEval.html#WeierstrassCurve.formalThirdRootEval_relation).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.formalThirdRootEval_relation`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/PairEval.html#WeierstrassCurve.formalThirdRootEval_relation)
- [Source of `WeierstrassCurve.formalThirdRootEval_relation` in TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/PairEval.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/PairEval.lean#L296)
