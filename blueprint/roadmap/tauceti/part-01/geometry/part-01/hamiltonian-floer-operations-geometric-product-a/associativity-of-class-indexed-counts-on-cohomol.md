---
declaration: theorem
origin: cited
lean: TauCeti.Floer.cohomologyProduct_kernelProduct_coefficientComparison_assoc
statement: formalized
proof: formalized
---

# Associativity of class-indexed counts on cohomology

Let the four products of
class-indexed counts in `(x ⋆ y) ⋆' z` and `x ⋆''' (y ⋆'' z)`, as ground-ring bilinear maps for any
potential bounds of their kernels, induce products on the cohomology of the cylinder
differentials, graded by the cochain degrees `n - μ`. The intermediate complexes of `x ⋆ y` and
`y ⋆'' z` may carry any differentials and gradings for which the products obey the Leibniz rule,
and the degree shifts `ε₁` and `ε₂` of the first bracketing must add up to zero, as the shifts of
products of rigid counts do. Under the identity and the index condition of
`TauCeti.Floer.novikovProductOfMatrix_coefficientComparison_assoc_sub_mem_coboundaries`, the
induced products are associative: `([x] ⋆ [y]) ⋆' [z] = [x] ⋆''' ([y] ⋆'' [z])`.

```lean
TauCeti.Floer.cohomologyProduct_kernelProduct_coefficientComparison_assoc.{u_1, u_2, u_3, u_4, u_5,
    u_6, u_7, u_8, u_9, u_10, u_11, u_12, u_13, u_14, u_15}
  {R : Type u_1} {S : Type u_2} [AddCommGroup S] {ω : S →+ ℝ} {c : S →+ ℤ} {ι₁ : Type u_3}
  {ι₂ : Type u_4} {ι₀ : Type u_5} {P₁ : ι₁ → Type u_6} {P₂ : ι₂ → Type u_7} {P₀ : ι₀ → Type u_8}
  [(i : ι₁) → AddTorsor (TauCeti.Floer.PeriodGroup ω c) (P₁ i)]
  [(j : ι₂) → AddTorsor (TauCeti.Floer.PeriodGroup ω c) (P₂ j)]
  [(k : ι₀) → AddTorsor (TauCeti.Floer.PeriodGroup ω c) (P₀ k)] (r₁ : (i : ι₁) → P₁ i)
  (r₂ : (j : ι₂) → P₂ j) (r₀ : (k : ι₀) → P₀ k) {G : Type u_9} [AddMonoid G] {ωG : G →+ ℝ}
  (q : G →+ TauCeti.Floer.PeriodGroup ω c)
  (hq : ∀ (A : G), (TauCeti.Floer.PeriodGroup.area ω c) (q A) = ωG A) {ι₃ : Type u_10}
  {ι₁₂ : Type u_11} {ι₂₃ : Type u_12} {P₃ : ι₃ → Type u_13} {P₁₂ : ι₁₂ → Type u_14}
  {P₂₃ : ι₂₃ → Type u_15} [(k : ι₃) → AddTorsor (TauCeti.Floer.PeriodGroup ω c) (P₃ k)]
  [(t : ι₁₂) → AddTorsor (TauCeti.Floer.PeriodGroup ω c) (P₁₂ t)]
  [(u : ι₂₃) → AddTorsor (TauCeti.Floer.PeriodGroup ω c) (P₂₃ u)] (r₃ : (k : ι₃) → P₃ k)
  (r₁₂ : (t : ι₁₂) → P₁₂ t) (r₂₃ : (u : ι₂₃) → P₂₃ u) [Fintype ι₁] [Fintype ι₂] [Fintype ι₃]
  [Fintype ι₀] {F₁ : (i : ι₁) × P₁ i → ℝ} {F₂ : (j : ι₂) × P₂ j → ℝ} {F₃ : (k : ι₃) × P₃ k → ℝ}
  {F₀ : (l : ι₀) × P₀ l → ℝ}
  (hF₁ :
    ∀ (i : ι₁) (γ : TauCeti.Floer.PeriodGroup ω c) (D : P₁ i),
      F₁ ⟨i, γ +ᵥ D⟩ = F₁ ⟨i, D⟩ - (-TauCeti.Floer.PeriodGroup.area ω c) γ)
  (hF₂ :
    ∀ (j : ι₂) (γ : TauCeti.Floer.PeriodGroup ω c) (D : P₂ j),
      F₂ ⟨j, γ +ᵥ D⟩ = F₂ ⟨j, D⟩ - (-TauCeti.Floer.PeriodGroup.area ω c) γ)
  (hF₃ :
    ∀ (k : ι₃) (γ : TauCeti.Floer.PeriodGroup ω c) (D : P₃ k),
      F₃ ⟨k, γ +ᵥ D⟩ = F₃ ⟨k, D⟩ - (-TauCeti.Floer.PeriodGroup.area ω c) γ)
  (hF₀ :
    ∀ (l : ι₀) (γ : TauCeti.Floer.PeriodGroup ω c) (D : P₀ l),
      F₀ ⟨l, γ +ᵥ D⟩ = F₀ ⟨l, D⟩ - (-TauCeti.Floer.PeriodGroup.area ω c) γ)
  {μ₁ : (i : ι₁) × P₁ i → ℤ} {μ₂ : (j : ι₂) × P₂ j → ℤ}
  (hμ₁ :
    ∀ (i : ι₁) (γ : TauCeti.Floer.PeriodGroup ω c) (D : P₁ i),
      μ₁ ⟨i, γ +ᵥ D⟩ = (TauCeti.Floer.PeriodGroup.degree ω c) γ + μ₁ ⟨i, D⟩)
  (hμ₂ :
    ∀ (j : ι₂) (γ : TauCeti.Floer.PeriodGroup ω c) (D : P₂ j),
      μ₂ ⟨j, γ +ᵥ D⟩ = (TauCeti.Floer.PeriodGroup.degree ω c) γ + μ₂ ⟨j, D⟩)
  [CommRing R] [Fintype ι₁₂] [Fintype ι₂₃] {F₁₂ : (t : ι₁₂) × P₁₂ t → ℝ}
  {F₂₃ : (u : ι₂₃) × P₂₃ u → ℝ}
  (hF₁₂ :
    ∀ (t : ι₁₂) (γ : TauCeti.Floer.PeriodGroup ω c) (D : P₁₂ t),
      F₁₂ ⟨t, γ +ᵥ D⟩ = F₁₂ ⟨t, D⟩ - (-TauCeti.Floer.PeriodGroup.area ω c) γ)
  (hF₂₃ :
    ∀ (u : ι₂₃) (γ : TauCeti.Floer.PeriodGroup ω c) (D : P₂₃ u),
      F₂₃ ⟨u, γ +ᵥ D⟩ = F₂₃ ⟨u, D⟩ - (-TauCeti.Floer.PeriodGroup.area ω c) γ)
  {μ₃ : (k : ι₃) × P₃ k → ℤ} {μ₀ : (l : ι₀) × P₀ l → ℤ}
  (hμ₃ :
    ∀ (k : ι₃) (γ : TauCeti.Floer.PeriodGroup ω c) (D : P₃ k),
      μ₃ ⟨k, γ +ᵥ D⟩ = (TauCeti.Floer.PeriodGroup.degree ω c) γ + μ₃ ⟨k, D⟩)
  (hμ₀ :
    ∀ (l : ι₀) (γ : TauCeti.Floer.PeriodGroup ω c) (D : P₀ l),
      μ₀ ⟨l, γ +ᵥ D⟩ = (TauCeti.Floer.PeriodGroup.degree ω c) γ + μ₀ ⟨l, D⟩)
  (Q : ι₁ → ι₂ → ι₁₂ → TauCeti.NovikovSeries R G ωG)
  (Q' : ι₁₂ → ι₃ → ι₀ → TauCeti.NovikovSeries R G ωG)
  (T : ι₂ → ι₃ → ι₂₃ → TauCeti.NovikovSeries R G ωG)
  (T' : ι₁ → ι₂₃ → ι₀ → TauCeti.NovikovSeries R G ωG)
  (K : ι₁ → ι₂ → ι₃ → ι₀ → TauCeti.NovikovSeries R G ωG)
  (D₁ : ι₁ → ι₁ → TauCeti.NovikovSeries R G ωG) (D₂ : ι₂ → ι₂ → TauCeti.NovikovSeries R G ωG)
  (D₃ : ι₃ → ι₃ → TauCeti.NovikovSeries R G ωG) (D₀ : ι₀ → ι₀ → TauCeti.NovikovSeries R G ωG)
  (n : ℤ) {C₁ C₂ C₃ C₀ : ℝ}
  (hδ₁ :
    ∀ (p p' : (k : ι₁) × P₁ k),
      TauCeti.NovikovModule.mapKernelOfMatrix r₁ r₁
            (fun i m => (TauCeti.Floer.coefficientComparison q hq) (D₁ i m)) p p' ≠
          0 →
        F₁ p' ≤ F₁ p + C₁)
  (hδ₂ :
    ∀ (p p' : (k : ι₂) × P₂ k),
      TauCeti.NovikovModule.mapKernelOfMatrix r₂ r₂
            (fun j m => (TauCeti.Floer.coefficientComparison q hq) (D₂ j m)) p p' ≠
          0 →
        F₂ p' ≤ F₂ p + C₂)
  (hδ₃ :
    ∀ (p p' : (k : ι₃) × P₃ k),
      TauCeti.NovikovModule.mapKernelOfMatrix r₃ r₃
            (fun k m => (TauCeti.Floer.coefficientComparison q hq) (D₃ k m)) p p' ≠
          0 →
        F₃ p' ≤ F₃ p + C₃)
  (hδ₀ :
    ∀ (p p' : (k : ι₀) × P₀ k),
      TauCeti.NovikovModule.mapKernelOfMatrix r₀ r₀
            (fun m l => (TauCeti.Floer.coefficientComparison q hq) (D₀ m l)) p p' ≠
          0 →
        F₀ p' ≤ F₀ p + C₀)
  {G₁₂ : ℤ → Submodule R ↥(TauCeti.NovikovModule R F₁₂)}
  {G₂₃ : ℤ → Submodule R ↥(TauCeti.NovikovModule R F₂₃)}
  {δ₁₂ : ↥(TauCeti.NovikovModule R F₁₂) →ₗ[R] ↥(TauCeti.NovikovModule R F₁₂)}
  {δ₂₃ : ↥(TauCeti.NovikovModule R F₂₃) →ₗ[R] ↥(TauCeti.NovikovModule R F₂₃)} {CQ CQ' CT CT' : ℝ}
  (hnQ :
    ∀ (p₁ : (i : ι₁) × P₁ i) (p₂ : (j : ι₂) × P₂ j) (p₀ : (k : ι₁₂) × P₁₂ k),
      TauCeti.NovikovModule.kernelOfMatrix r₁ r₂ r₁₂
            (fun i j t => (TauCeti.Floer.coefficientComparison q hq) (Q i j t)) p₁ p₂ p₀ ≠
          0 →
        F₁₂ p₀ ≤ F₁ p₁ + F₂ p₂ + CQ)
  (hnQ' :
    ∀ (p₁ : (i : ι₁₂) × P₁₂ i) (p₂ : (j : ι₃) × P₃ j) (p₀ : (k : ι₀) × P₀ k),
      TauCeti.NovikovModule.kernelOfMatrix r₁₂ r₃ r₀
            (fun t k l => (TauCeti.Floer.coefficientComparison q hq) (Q' t k l)) p₁ p₂ p₀ ≠
          0 →
        F₀ p₀ ≤ F₁₂ p₁ + F₃ p₂ + CQ')
  (hnT :
    ∀ (p₁ : (i : ι₂) × P₂ i) (p₂ : (j : ι₃) × P₃ j) (p₀ : (k : ι₂₃) × P₂₃ k),
      TauCeti.NovikovModule.kernelOfMatrix r₂ r₃ r₂₃
            (fun j k u => (TauCeti.Floer.coefficientComparison q hq) (T j k u)) p₁ p₂ p₀ ≠
          0 →
        F₂₃ p₀ ≤ F₂ p₁ + F₃ p₂ + CT)
  (hnT' :
    ∀ (p₁ : (i : ι₁) × P₁ i) (p₂ : (j : ι₂₃) × P₂₃ j) (p₀ : (k : ι₀) × P₀ k),
      TauCeti.NovikovModule.kernelOfMatrix r₁ r₂₃ r₀
            (fun i u l => (TauCeti.Floer.coefficientComparison q hq) (T' i u l)) p₁ p₂ p₀ ≠
          0 →
        F₀ p₀ ≤ F₁ p₁ + F₂₃ p₂ + CT')
  {ε₁ ε₂ ε₃ ε₄ : ℤ}
  {hQdeg :
    ∀ {i j : ℤ} {a : ↥(TauCeti.NovikovModule R F₁)} {b : ↥(TauCeti.NovikovModule R F₂)},
      a ∈ TauCeti.NovikovModule.gradeBy R F₁ (fun p => n - μ₁ p) i →
        b ∈ TauCeti.NovikovModule.gradeBy R F₂ (fun p => n - μ₂ p) j →
          ((TauCeti.NovikovModule.kernelProduct hnQ ⋯) a) b ∈ G₁₂ (i + j + ε₁)}
  {hQL :
    ∀ {i : ℤ} {a : ↥(TauCeti.NovikovModule R F₁)},
      a ∈ TauCeti.NovikovModule.gradeBy R F₁ (fun p => n - μ₁ p) i →
        ∀ (b : ↥(TauCeti.NovikovModule R F₂)),
          δ₁₂ (((TauCeti.NovikovModule.kernelProduct hnQ ⋯) a) b) =
            ((TauCeti.NovikovModule.kernelProduct hnQ ⋯)
                  ((TauCeti.NovikovModule.kernelMap hδ₁ ⋯) a))
                b +
              TauCeti.negOnePowCast R i •
                ((TauCeti.NovikovModule.kernelProduct hnQ ⋯) a)
                  ((TauCeti.NovikovModule.kernelMap hδ₂ ⋯) b)}
  {hQ'deg :
    ∀ {i j : ℤ} {a : ↥(TauCeti.NovikovModule R F₁₂)} {b : ↥(TauCeti.NovikovModule R F₃)},
      a ∈ G₁₂ i →
        b ∈ TauCeti.NovikovModule.gradeBy R F₃ (fun p => n - μ₃ p) j →
          ((TauCeti.NovikovModule.kernelProduct hnQ' ⋯) a) b ∈
            TauCeti.NovikovModule.gradeBy R F₀ (fun p => n - μ₀ p) (i + j + ε₂)}
  {hQ'L :
    ∀ {i : ℤ} {a : ↥(TauCeti.NovikovModule R F₁₂)},
      a ∈ G₁₂ i →
        ∀ (b : ↥(TauCeti.NovikovModule R F₃)),
          (TauCeti.NovikovModule.kernelMap hδ₀ ⋯)
              (((TauCeti.NovikovModule.kernelProduct hnQ' ⋯) a) b) =
            ((TauCeti.NovikovModule.kernelProduct hnQ' ⋯) (δ₁₂ a)) b +
              TauCeti.negOnePowCast R i •
                ((TauCeti.NovikovModule.kernelProduct hnQ' ⋯) a)
                  ((TauCeti.NovikovModule.kernelMap hδ₃ ⋯) b)}
  {hTdeg :
    ∀ {i j : ℤ} {a : ↥(TauCeti.NovikovModule R F₂)} {b : ↥(TauCeti.NovikovModule R F₃)},
      a ∈ TauCeti.NovikovModule.gradeBy R F₂ (fun p => n - μ₂ p) i →
        b ∈ TauCeti.NovikovModule.gradeBy R F₃ (fun p => n - μ₃ p) j →
          ((TauCeti.NovikovModule.kernelProduct hnT ⋯) a) b ∈ G₂₃ (i + j + ε₃)}
  {hTL :
    ∀ {i : ℤ} {a : ↥(TauCeti.NovikovModule R F₂)},
      a ∈ TauCeti.NovikovModule.gradeBy R F₂ (fun p => n - μ₂ p) i →
        ∀ (b : ↥(TauCeti.NovikovModule R F₃)),
          δ₂₃ (((TauCeti.NovikovModule.kernelProduct hnT ⋯) a) b) =
            ((TauCeti.NovikovModule.kernelProduct hnT ⋯)
                  ((TauCeti.NovikovModule.kernelMap hδ₂ ⋯) a))
                b +
              TauCeti.negOnePowCast R i •
                ((TauCeti.NovikovModule.kernelProduct hnT ⋯) a)
                  ((TauCeti.NovikovModule.kernelMap hδ₃ ⋯) b)}
  {hT'deg :
    ∀ {i j : ℤ} {a : ↥(TauCeti.NovikovModule R F₁)} {b : ↥(TauCeti.NovikovModule R F₂₃)},
      a ∈ TauCeti.NovikovModule.gradeBy R F₁ (fun p => n - μ₁ p) i →
        b ∈ G₂₃ j →
          ((TauCeti.NovikovModule.kernelProduct hnT' ⋯) a) b ∈
            TauCeti.NovikovModule.gradeBy R F₀ (fun p => n - μ₀ p) (i + j + ε₄)}
  {hT'L :
    ∀ {i : ℤ} {a : ↥(TauCeti.NovikovModule R F₁)},
      a ∈ TauCeti.NovikovModule.gradeBy R F₁ (fun p => n - μ₁ p) i →
        ∀ (b : ↥(TauCeti.NovikovModule R F₂₃)),
          (TauCeti.NovikovModule.kernelMap hδ₀ ⋯)
              (((TauCeti.NovikovModule.kernelProduct hnT' ⋯) a) b) =
            ((TauCeti.NovikovModule.kernelProduct hnT' ⋯)
                  ((TauCeti.NovikovModule.kernelMap hδ₁ ⋯) a))
                b +
              TauCeti.negOnePowCast R i • ((TauCeti.NovikovModule.kernelProduct hnT' ⋯) a) (δ₂₃ b)}
  (hK :
    ∀ (i : ι₁) (j : ι₂) (k : ι₃) (l : ι₀),
      ∀ A ∈ (K i j k l).support,
        μ₀ ⟨l, r₀ l⟩ - (TauCeti.Floer.PeriodGroup.degree ω c) (q A) =
          μ₁ ⟨i, r₁ i⟩ + μ₂ ⟨j, r₂ j⟩ + μ₃ ⟨k, r₃ k⟩ - 2 * n + 1)
  (hA :
    ∀ (i : ι₁) (j : ι₂) (k : ι₃) (l : ι₀),
      ∑ t, Q i j t * Q' t k l - ∑ u, T j k u * T' i u l =
        ∑ m, K i j k m * D₀ m l + ∑ m, D₁ i m * K m j k l +
            TauCeti.negOnePowCast R (n - μ₁ ⟨i, r₁ i⟩) • ∑ m, D₂ j m * K i m k l +
          TauCeti.negOnePowCast R (n - μ₁ ⟨i, r₁ i⟩ + (n - μ₂ ⟨j, r₂ j⟩)) • ∑ m, D₃ k m * K i j m l)
  (hε : ε₁ + ε₂ = 0) {e₁ e₂ e₃ e₁₂ e₂₃ e₀ : ℤ} (h₁₂ : e₁ + e₂ + ε₁ = e₁₂) (h₀ : e₁₂ + e₃ + ε₂ = e₀)
  (h₂₃ : e₂ + e₃ + ε₃ = e₂₃) (h₀' : e₁ + e₂₃ + ε₄ = e₀)
  (x :
    (TauCeti.NovikovModule.kernelMap hδ₁ ⋯).cohomology
      (TauCeti.NovikovModule.gradeBy R F₁ fun p => n - μ₁ p) e₁)
  (y :
    (TauCeti.NovikovModule.kernelMap hδ₂ ⋯).cohomology
      (TauCeti.NovikovModule.gradeBy R F₂ fun p => n - μ₂ p) e₂)
  (z :
    (TauCeti.NovikovModule.kernelMap hδ₃ ⋯).cohomology
      (TauCeti.NovikovModule.gradeBy R F₃ fun p => n - μ₃ p) e₃) :
  ((LinearMap.cohomologyProduct (TauCeti.NovikovModule.kernelProduct hnQ' ⋯) ⋯ ⋯ h₀)
        (((LinearMap.cohomologyProduct (TauCeti.NovikovModule.kernelProduct hnQ ⋯) ⋯ ⋯ h₁₂) x) y))
      z =
    ((LinearMap.cohomologyProduct (TauCeti.NovikovModule.kernelProduct hnT' ⋯) ⋯ ⋯ h₀') x)
      (((LinearMap.cohomologyProduct (TauCeti.NovikovModule.kernelProduct hnT ⋯) ⋯ ⋯ h₂₃) y) z)
```

## Depends on

- [TauCeti.NovikovModule.kernelProduct](tauceti-novikovmodule-kernelproduct.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Floer.cohomologyProduct_kernelProduct_coefficientComparison_assoc`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Cap/Product.html#TauCeti.Floer.cohomologyProduct_kernelProduct_coefficientComparison_assoc).

## Sources

- [Tau Ceti documentation: `TauCeti.Floer.cohomologyProduct_kernelProduct_coefficientComparison_assoc`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Cap/Product.html#TauCeti.Floer.cohomologyProduct_kernelProduct_coefficientComparison_assoc)
- [Source of `TauCeti.Floer.cohomologyProduct_kernelProduct_coefficientComparison_assoc` in TauCeti/Geometry/Symplectic/Floer/Cap/Product.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Floer/Cap/Product.lean#L874)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
