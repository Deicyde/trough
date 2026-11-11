---
declaration: theorem
origin: cited
lean: Matrix.tendsto_spectralMeasure_iff_of_rank_sub_div_card_tendsto_zero
statement: formalized
proof: formalized
---

# Matrix.tendsto_spectralMeasure_iff_of_rank_sub_div_card_tendsto_zero

A perturbation whose rank divided by the matrix dimension tends to zero preserves, in both
directions, weak convergence of the empirical spectral measures. The limiting law may have
atoms, and the perturbation need not have bounded operator norm.

```lean
Matrix.tendsto_spectralMeasure_iff_of_rank_sub_div_card_tendsto_zero.{u_1, u_2, u_3} {ι : Type u_1}
  {𝕜 : Type u_2} {n : ι → Type u_3} [(i : ι) → Fintype (n i)] [(i : ι) → DecidableEq (n i)]
  [∀ (i : ι), Nonempty (n i)] [RCLike 𝕜] {l : Filter ι} [l.IsCountablyGenerated]
  {μ : MeasureTheory.ProbabilityMeasure ℝ} (A B : (i : ι) → Matrix (n i) (n i) 𝕜)
  (hA : ∀ (i : ι), (A i).IsHermitian) (hB : ∀ (i : ι), (B i).IsHermitian)
  (hrank : Filter.Tendsto (fun i => ↑(A i - B i).rank / ↑(Fintype.card (n i))) l (nhds 0)) :
  Filter.Tendsto (fun i => (A i).spectralMeasure ⋯) l (nhds μ) ↔
    Filter.Tendsto (fun i => (B i).spectralMeasure ⋯) l (nhds μ)
```

## Depends on

- [TauCeti.Probability.empiricalFiniteMeasure](tauceti-probability-empiricalfinitemeasure.md)

## Proof depends on

- [Helly–Bray theorem](../../measure-theory/measure/helly-bray-theorem.md)
- [Weyl's additive inequality for Hermitian matrices, upper form](../../analysis/part-03/matrix/weyls-additive-inequality-for-hermitian-matrices.md)

## Lean

Formalized in Tau Ceti as [`Matrix.tendsto_spectralMeasure_iff_of_rank_sub_div_card_tendsto_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/SpectralMeasure/WeakConvergence.html#Matrix.tendsto_spectralMeasure_iff_of_rank_sub_div_card_tendsto_zero).

## Sources

- [Tau Ceti documentation: `Matrix.tendsto_spectralMeasure_iff_of_rank_sub_div_card_tendsto_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/SpectralMeasure/WeakConvergence.html#Matrix.tendsto_spectralMeasure_iff_of_rank_sub_div_card_tendsto_zero)
- [Source of `Matrix.tendsto_spectralMeasure_iff_of_rank_sub_div_card_tendsto_zero` in TauCeti/Analysis/Matrix/SpectralMeasure/WeakConvergence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Matrix/SpectralMeasure/WeakConvergence.lean#L42)
- [Tau Ceti roadmap status: Random matrices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RandomMatrices/STATUS.md)
