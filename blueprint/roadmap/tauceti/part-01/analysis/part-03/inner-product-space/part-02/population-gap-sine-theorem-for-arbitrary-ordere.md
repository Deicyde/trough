---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.sinThetaFrobenius_orderedEigenframe_le
statement: formalized
proof: formalized
---

# Population-gap sine theorem for arbitrary ordered eigenframes

The frames select the same sorted indices. Only the population eigenvalues
need a gap from the unselected indices; the perturbed frame may be any
orthonormal choice inside repeated sample eigenspaces.

Adapted from `yuWangSamworth_sinTheta_frame_le` in
`YuWangSamworth2015/YuWangSamworth2015/Core/Statistics.lean`, Kitware DKPS
(Jon Crall and GPT 5.6 High; Apache-2.0).

```lean
LinearMap.IsSymmetric.sinThetaFrobenius_orderedEigenframe_le.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E]
  {A B : E →ₗ[𝕜] E} {n : ℕ} {hA : A.IsSymmetric} {hB : B.IsSymmetric} {hn : Module.finrank 𝕜 E = n}
  {ι : Type u_3} [Fintype ι] {e : ι ↪ Fin n} {u v : ι → E} (hu : hA.IsOrderedEigenframe hn e u)
  (hv : hB.IsOrderedEigenframe hn e v) {δ : ℝ} (hd : 0 < δ)
  (hgap : ∀ (i : ι), ∀ k ∉ Set.range ⇑e, δ ≤ |hA.eigenvalues hn (e i) - hA.eigenvalues hn k|) :
  (Submodule.span 𝕜 (Set.range u)).sinThetaFrobenius (Submodule.span 𝕜 (Set.range v)) ≤
    2 *
        min (√↑(Fintype.card ι) * ‖LinearMap.toContinuousLinearMap (B - A)‖)
          ((TauCeti.UnitarilyInvariantSeminorm.frobenius 𝕜 E E) (B - A)) /
      δ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hoffman–Wielandt inequality](../part-01/the-hoffman-wielandt-inequality.md)
- [Parseval's identity for a functional](parsevals-identity-for-a-functional.md)
- [Weyl's inequality](../part-03/weyls-inequality.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.IsSymmetric.sinThetaFrobenius_orderedEigenframe_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/SinTheta.html#LinearMap.IsSymmetric.sinThetaFrobenius_orderedEigenframe_le).

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.sinThetaFrobenius_orderedEigenframe_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/SinTheta.html#LinearMap.IsSymmetric.sinThetaFrobenius_orderedEigenframe_le)
- [Source of `LinearMap.IsSymmetric.sinThetaFrobenius_orderedEigenframe_le` in TauCeti/Analysis/InnerProductSpace/YuWangSamworth/SinTheta.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/SinTheta.lean#L51)
