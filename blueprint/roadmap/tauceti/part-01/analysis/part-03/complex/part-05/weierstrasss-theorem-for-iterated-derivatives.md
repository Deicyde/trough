---
declaration: theorem
origin: cited
lean: TendstoLocallyUniformlyOn.iteratedDeriv, TendstoLocallyUniformlyOn.iteratedFDeriv
statement: formalized
proof: formalized
---

# Weierstrass's theorem for iterated derivatives

If holomorphic maps `F n` converge to `f`
locally uniformly on an open set `U ⊆ ℂ`, then so do their iterated derivatives. This is the
iterated form of Mathlib's `TendstoLocallyUniformlyOn.deriv`.

```lean
TendstoLocallyUniformlyOn.iteratedDeriv.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [CompleteSpace E] {ι : Type u_2} {l : Filter ι} {F : ι → ℂ → E} {f : ℂ → E}
  {U : Set ℂ} (hf : TendstoLocallyUniformlyOn F f l U)
  (hF : ∀ᶠ (n : ι) in l, DifferentiableOn ℂ (F n) U) (hU : IsOpen U) (k : ℕ) :
  TendstoLocallyUniformlyOn (fun n => iteratedDeriv k (F n)) (iteratedDeriv k f) l U
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TendstoLocallyUniformlyOn.iteratedDeriv`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/IteratedDeriv.html#TendstoLocallyUniformlyOn.iteratedDeriv).

## Other forms

**Weierstrass's theorem for real iterated derivatives.** Formalized in Tau Ceti as [`TendstoLocallyUniformlyOn.iteratedFDeriv`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/IteratedDeriv.html#TendstoLocallyUniformlyOn.iteratedFDeriv).

```lean
TendstoLocallyUniformlyOn.iteratedFDeriv.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [CompleteSpace E] (𝕜 : Type u_2) [NontriviallyNormedField 𝕜] [NormedAlgebra 𝕜 ℂ]
  [NormedSpace 𝕜 E] [IsScalarTower 𝕜 ℂ E] {ι : Type u_3} {l : Filter ι} {F : ι → ℂ → E} {f : ℂ → E}
  {U : Set ℂ} (hf : TendstoLocallyUniformlyOn F f l U)
  (hF : ∀ᶠ (n : ι) in l, DifferentiableOn ℂ (F n) U) (hU : IsOpen U) (k : ℕ) :
  TendstoLocallyUniformlyOn (fun n => iteratedFDeriv 𝕜 k (F n)) (iteratedFDeriv 𝕜 k f) l U
```

## Sources

- [Tau Ceti documentation: `TendstoLocallyUniformlyOn.iteratedDeriv`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/IteratedDeriv.html#TendstoLocallyUniformlyOn.iteratedDeriv)
- [Source of `TendstoLocallyUniformlyOn.iteratedDeriv` in TauCeti/Analysis/Complex/IteratedDeriv.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/IteratedDeriv.lean#L55)
