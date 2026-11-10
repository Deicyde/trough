---
declaration: theorem
origin: cited
lean: TauCeti.exists_hasSum_apply_of_almost_orthogonal, TauCeti.norm_sum_le_of_almost_orthogonal
statement: formalized
proof: formalized
---

# The Cotlar–Stein lemma

Let `T i` be operators between Hilbert spaces which are almost
orthogonal in the sense that `∑ j, √‖(T i)† ∘L T j‖ ≤ A` and `∑ j, √‖T i ∘L (T j)†‖ ≤ A` for
every `i`, the sums over `j` being taken over arbitrary finite sets. Then for every `x` the
series `∑ i, T i x` converges unconditionally, and its sum is a bounded operator of norm at
most `A`.

```lean
TauCeti.exists_hasSum_apply_of_almost_orthogonal.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} {ι : Type u_4} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [CompleteSpace E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [CompleteSpace F]
  (T : ι → E →L[𝕜] F) {A : ℝ} (hA : 0 ≤ A)
  (h₁ : ∀ (i : ι) (s : Finset ι), ∑ j ∈ s, √‖ContinuousLinearMap.adjoint (T i) ∘SL T j‖ ≤ A)
  (h₂ : ∀ (i : ι) (s : Finset ι), ∑ j ∈ s, √‖T i ∘SL ContinuousLinearMap.adjoint (T j)‖ ≤ A) :
  ∃ S, ‖S‖ ≤ A ∧ ∀ (x : E), HasSum (fun i => (T i) x) (S x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_hasSum_apply_of_almost_orthogonal`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/CotlarStein.html#TauCeti.exists_hasSum_apply_of_almost_orthogonal).

## Other forms

**The Cotlar–Stein lemma, finite form.** Formalized in Tau Ceti as [`TauCeti.norm_sum_le_of_almost_orthogonal`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/CotlarStein.html#TauCeti.norm_sum_le_of_almost_orthogonal).

```lean
TauCeti.norm_sum_le_of_almost_orthogonal.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} {ι : Type u_4} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [CompleteSpace E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [CompleteSpace F]
  (T : ι → E →L[𝕜] F) {A : ℝ} (s : Finset ι) (hA : 0 ≤ A)
  (h₁ : ∀ i ∈ s, ∑ j ∈ s, √‖ContinuousLinearMap.adjoint (T i) ∘SL T j‖ ≤ A)
  (h₂ : ∀ i ∈ s, ∑ j ∈ s, √‖T i ∘SL ContinuousLinearMap.adjoint (T j)‖ ≤ A) : ‖∑ i ∈ s, T i‖ ≤ A
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_hasSum_apply_of_almost_orthogonal`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/CotlarStein.html#TauCeti.exists_hasSum_apply_of_almost_orthogonal)
- [Source of `TauCeti.exists_hasSum_apply_of_almost_orthogonal` in TauCeti/Analysis/InnerProductSpace/CotlarStein.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/CotlarStein.lean#L281)
