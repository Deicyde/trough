---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.sinThetaFrobenius_eigenvectorSpan_le
statement: formalized
proof: formalized
---

# Population-gap Frobenius sin-theta theorem

For the subspaces selected by the same indices in the canonical eigenbases of
symmetric operators `A` (population) and `B` (perturbed), a gap in the population
eigenvalues alone gives

`norm(sin Theta)_F <= 2 * min(sqrt(card s) * norm(B - A), norm(B - A)_F) / delta`.

No gap is required in the spectrum of `B`. The bases used are `eigenvectorBasis`;
other orthonormal eigenframes of `B` within repeated eigenspaces are not included.

```lean
LinearMap.IsSymmetric.sinThetaFrobenius_eigenvectorSpan_le.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E]
  {A B : E →ₗ[𝕜] E} {n : ℕ} (hA : A.IsSymmetric) (hB : B.IsSymmetric) (hn : Module.finrank 𝕜 E = n)
  (s : Finset (Fin n)) {delta : ℝ} (hd : 0 < delta)
  (hgap : ∀ j ∈ s, ∀ k ∉ s, delta ≤ |hA.eigenvalues hn j - hA.eigenvalues hn k|) :
  (hA.eigenvectorSpan hn ↑s).sinThetaFrobenius (hB.eigenvectorSpan hn ↑s) ≤
    2 *
        min (√↑s.card * ‖LinearMap.toContinuousLinearMap (B - A)‖)
          ((TauCeti.UnitarilyInvariantSeminorm.frobenius 𝕜 E E) (B - A)) /
      delta
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Population-gap sine theorem for arbitrary ordered eigenframes](population-gap-sine-theorem-for-arbitrary-ordere.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.IsSymmetric.sinThetaFrobenius_eigenvectorSpan_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/SinTheta.html#LinearMap.IsSymmetric.sinThetaFrobenius_eigenvectorSpan_le).

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.sinThetaFrobenius_eigenvectorSpan_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/SinTheta.html#LinearMap.IsSymmetric.sinThetaFrobenius_eigenvectorSpan_le)
- [Source of `LinearMap.IsSymmetric.sinThetaFrobenius_eigenvectorSpan_le` in TauCeti/Analysis/InnerProductSpace/YuWangSamworth/SinTheta.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/SinTheta.lean#L116)
