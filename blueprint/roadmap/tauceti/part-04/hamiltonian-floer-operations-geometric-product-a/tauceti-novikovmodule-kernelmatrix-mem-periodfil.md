---
declaration: theorem
origin: cited
lean: TauCeti.NovikovModule.kernelMatrix_mem_periodFiltration
statement: formalized
proof: formalized
---

# TauCeti.NovikovModule.kernelMatrix\_mem\_periodFiltration

Under a potential bound with constant `C`, the `(i, j, k)` entry of the kernel matrix lies in
the period filtration at level `F₀(r₀ k) - F₁(r₁ i) - F₂(r₂ j) - C`.

```lean
TauCeti.NovikovModule.kernelMatrix_mem_periodFiltration.{u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8}
  {R : Type u_1} {H : Type u_2} {ι₁ : Type u_3} {ι₂ : Type u_4} {ι₀ : Type u_5} [AddGroup H]
  {N : H →+ ℝ} {P₁ : ι₁ → Type u_6} {P₂ : ι₂ → Type u_7} {P₀ : ι₀ → Type u_8}
  [(k : ι₀) → AddTorsor H (P₀ k)] {F₁ : (i : ι₁) × P₁ i → ℝ} {F₂ : (j : ι₂) × P₂ j → ℝ}
  {F₀ : (k : ι₀) × P₀ k → ℝ} {C : ℝ} {n : (i : ι₁) × P₁ i → (j : ι₂) × P₂ j → (k : ι₀) × P₀ k → R}
  [Ring R] [Finite ι₀] (hF₀ : ∀ (k : ι₀) (h : H) (p : P₀ k), F₀ ⟨k, h +ᵥ p⟩ = F₀ ⟨k, p⟩ - N h)
  (hn :
    ∀ (p₁ : (i : ι₁) × P₁ i) (p₂ : (j : ι₂) × P₂ j) (p₀ : (k : ι₀) × P₀ k),
      n p₁ p₂ p₀ ≠ 0 → F₀ p₀ ≤ F₁ p₁ + F₂ p₂ + C)
  (hfin : ∀ (p₁ : (i : ι₁) × P₁ i) (p₂ : (j : ι₂) × P₂ j), n p₁ p₂ ∈ TauCeti.NovikovModule R F₀)
  (r₁ : (i : ι₁) → P₁ i) (r₂ : (j : ι₂) → P₂ j) (r₀ : (k : ι₀) → P₀ k) (i : ι₁) (j : ι₂) (k : ι₀) :
  TauCeti.NovikovModule.kernelMatrix hF₀ hfin r₁ r₂ r₀ i j k ∈
    TauCeti.NovikovSeries.periodFiltration R N (F₀ ⟨k, r₀ k⟩ - F₁ ⟨i, r₁ i⟩ - F₂ ⟨j, r₂ j⟩ - C)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NovikovModule.kernelMatrix_mem_periodFiltration`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovModule/Bilinear.html#TauCeti.NovikovModule.kernelMatrix_mem_periodFiltration).

## Sources

- [Tau Ceti documentation: `TauCeti.NovikovModule.kernelMatrix_mem_periodFiltration`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovModule/Bilinear.html#TauCeti.NovikovModule.kernelMatrix_mem_periodFiltration)
- [Source of `TauCeti.NovikovModule.kernelMatrix_mem_periodFiltration` in TauCeti/RingTheory/NovikovModule/Bilinear.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/NovikovModule/Bilinear.lean#L535)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
