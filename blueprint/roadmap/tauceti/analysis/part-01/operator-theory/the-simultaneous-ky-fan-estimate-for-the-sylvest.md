---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.mul_kyFanSum_le_pi_div_two_mul_kyFanSum_sylvester_apply
statement: formalized
proof: formalized
---

# The simultaneous Ky Fan estimate for the Sylvester equation

Let `A` and `B` be symmetric
operators on finite-dimensional inner product spaces. If every eigenvalue of `A` is at distance at
least `δ` from every eigenvalue of `B`, then for every `k` the Ky Fan `k`-sums satisfy
`δ Kₖ(X) ≤ (π / 2) Kₖ(A X - X B)`. In particular every solution of the Sylvester equation
`A X - X B = C` satisfies `δ Kₖ(X) ≤ (π / 2) Kₖ(C)` for all `k` at once.

```lean
ContinuousLinearMap.mul_kyFanSum_le_pi_div_two_mul_kyFanSum_sylvester_apply.{u_1, u_2, u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F]
  [FiniteDimensional 𝕜 F] {A : E →L[𝕜] E} {B : F →L[𝕜] F} {δ : ℝ} (hA : (↑A).IsSymmetric)
  (hB : (↑B).IsSymmetric) (h : Module.End.PointSpectraSeparated ↑A ⊤ ↑B ⊤ δ) (X : F →L[𝕜] E)
  (k : ℕ) : δ * (↑X).kyFanSum k ≤ Real.pi / 2 * (↑((A.sylvester B) X)).kyFanSum k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The exterior reciprocal Fourier identity](../../part-02/fourier/the-exterior-reciprocal-fourier-identity.md)
- [Ky Fan's maximum principle, attainment](../../part-02/inner-product-space/part-02/ky-fans-maximum-principle-attainment.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.mul_kyFanSum_le_pi_div_two_mul_kyFanSum_sylvester_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Pairwise.html#ContinuousLinearMap.mul_kyFanSum_le_pi_div_two_mul_kyFanSum_sylvester_apply).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.mul_kyFanSum_le_pi_div_two_mul_kyFanSum_sylvester_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Pairwise.html#ContinuousLinearMap.mul_kyFanSum_le_pi_div_two_mul_kyFanSum_sylvester_apply)
- [Source of `ContinuousLinearMap.mul_kyFanSum_le_pi_div_two_mul_kyFanSum_sylvester_apply` in TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Pairwise.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Pairwise.lean#L203)
