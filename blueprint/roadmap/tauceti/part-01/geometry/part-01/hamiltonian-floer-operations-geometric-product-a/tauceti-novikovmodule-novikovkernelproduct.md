---
declaration: def
origin: cited
lean: TauCeti.NovikovModule.novikovKernelProduct
statement: formalized
---

# TauCeti.NovikovModule.novikovKernelProduct

The product of an invariant kernel, as a bilinear map over the Novikov ring, for the Novikov
module structures of `TauCeti.NovikovModule.module`.

```lean
TauCeti.NovikovModule.novikovKernelProduct.{u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8} {R : Type u_1}
  {H : Type u_2} {ι₁ : Type u_3} {ι₂ : Type u_4} {ι₀ : Type u_5} [CommSemiring R] [AddCommGroup H]
  {N : H →+ ℝ} {P₁ : ι₁ → Type u_6} {P₂ : ι₂ → Type u_7} {P₀ : ι₀ → Type u_8}
  [(i : ι₁) → AddTorsor H (P₁ i)] [(j : ι₂) → AddTorsor H (P₂ j)] [(k : ι₀) → AddTorsor H (P₀ k)]
  [Finite ι₁] [Finite ι₂] [Finite ι₀] {F₁ : (i : ι₁) × P₁ i → ℝ} {F₂ : (j : ι₂) × P₂ j → ℝ}
  {F₀ : (k : ι₀) × P₀ k → ℝ} {C : ℝ} {n : (i : ι₁) × P₁ i → (j : ι₂) × P₂ j → (k : ι₀) × P₀ k → R}
  (hF₁ : ∀ (i : ι₁) (h : H) (p : P₁ i), F₁ ⟨i, h +ᵥ p⟩ = F₁ ⟨i, p⟩ - N h)
  (hF₂ : ∀ (j : ι₂) (h : H) (p : P₂ j), F₂ ⟨j, h +ᵥ p⟩ = F₂ ⟨j, p⟩ - N h)
  (hF₀ : ∀ (k : ι₀) (h : H) (p : P₀ k), F₀ ⟨k, h +ᵥ p⟩ = F₀ ⟨k, p⟩ - N h)
  (hn :
    ∀ (p₁ : (i : ι₁) × P₁ i) (p₂ : (j : ι₂) × P₂ j) (p₀ : (k : ι₀) × P₀ k),
      n p₁ p₂ p₀ ≠ 0 → F₀ p₀ ≤ F₁ p₁ + F₂ p₂ + C)
  (hfin : ∀ (p₁ : (i : ι₁) × P₁ i) (p₂ : (j : ι₂) × P₂ j), n p₁ p₂ ∈ TauCeti.NovikovModule R F₀)
  (hn₁ :
    ∀ (g : H) (i : ι₁) (p₁ : P₁ i) (p₂ : (j : ι₂) × P₂ j) (k : ι₀) (p₀ : P₀ k),
      n ⟨i, g +ᵥ p₁⟩ p₂ ⟨k, g +ᵥ p₀⟩ = n ⟨i, p₁⟩ p₂ ⟨k, p₀⟩)
  (hn₂ :
    ∀ (g : H) (p₁ : (i : ι₁) × P₁ i) (j : ι₂) (p₂ : P₂ j) (k : ι₀) (p₀ : P₀ k),
      n p₁ ⟨j, g +ᵥ p₂⟩ ⟨k, g +ᵥ p₀⟩ = n p₁ ⟨j, p₂⟩ ⟨k, p₀⟩) :
  ↥(TauCeti.NovikovModule R F₁) →ₗ[TauCeti.NovikovSeries R H N]
    ↥(TauCeti.NovikovModule R F₂) →ₗ[TauCeti.NovikovSeries R H N] ↥(TauCeti.NovikovModule R F₀)
```

## Depends on

- [TauCeti.NovikovModule.kernelProduct](tauceti-novikovmodule-kernelproduct.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NovikovModule.novikovKernelProduct`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovModule/Bilinear.html#TauCeti.NovikovModule.novikovKernelProduct).

## Sources

- [Tau Ceti documentation: `TauCeti.NovikovModule.novikovKernelProduct`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovModule/Bilinear.html#TauCeti.NovikovModule.novikovKernelProduct)
- [Source of `TauCeti.NovikovModule.novikovKernelProduct` in TauCeti/RingTheory/NovikovModule/Bilinear.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/NovikovModule/Bilinear.lean#L716)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
