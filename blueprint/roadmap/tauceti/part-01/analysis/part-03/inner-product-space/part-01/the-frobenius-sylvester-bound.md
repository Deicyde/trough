---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.mul_frobenius_le_frobenius_sylvester_apply
statement: formalized
proof: formalized
---

# The Frobenius Sylvester bound

In finite dimension, if `A` and `B` are symmetric and every
eigenvalue of `A` is at distance at least `δ` from every eigenvalue of `B`, then
`δ ‖X‖_F ≤ ‖A X - X B‖_F` for every `X`. In particular every solution of the Sylvester equation
`A X - X B = C` satisfies `δ ‖X‖_F ≤ ‖C‖_F`.

```lean
ContinuousLinearMap.mul_frobenius_le_frobenius_sylvester_apply.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [FiniteDimensional 𝕜 F]
  {A : E →L[𝕜] E} {B : F →L[𝕜] F} {δ : ℝ} (hA : (↑A).IsSymmetric) (hB : (↑B).IsSymmetric)
  (h : Module.End.PointSpectraSeparated ↑A ⊤ ↑B ⊤ δ) (X : F →L[𝕜] E) :
  δ * (TauCeti.UnitarilyInvariantSeminorm.frobenius 𝕜 F E) ↑X ≤
    (TauCeti.UnitarilyInvariantSeminorm.frobenius 𝕜 F E) ↑((A.sylvester B) X)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.mul_frobenius_le_frobenius_sylvester_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Basic.html#ContinuousLinearMap.mul_frobenius_le_frobenius_sylvester_apply).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.mul_frobenius_le_frobenius_sylvester_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Basic.html#ContinuousLinearMap.mul_frobenius_le_frobenius_sylvester_apply)
- [Source of `ContinuousLinearMap.mul_frobenius_le_frobenius_sylvester_apply` in TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Basic.lean#L110)
