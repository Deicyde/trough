---
declaration: theorem
origin: cited
lean: TauCeti.Floer.novikovProductOfMatrix_sub_negOnePowCast_smul_novikovProductOfMatrix_mem_coboundaries
statement: formalized
proof: formalized
---

# Graded commutativity of class-indexed counts on cohomology

Under the identity of
`novikovProductOfMatrix_sub_negOnePowCast_smul_novikovProductOfMatrix_coefficientComparison`,
suppose that every class counted by `K` satisfies the index condition
`μ₀(r₀) - 2 c₁(A) = μ₁(r₁) + μ₂(r₂) - n + 1` of rigid members of the input-exchange family, whose
Fredholm index at a fixed parameter is `-1`, so that `K` lowers the cochain degree by one. Then
for cocycles `a` and `b` of the cylinder differentials, of cochain degrees `e` and `f`, the graded
commutator `a ⋆ b - (-1)^(e f) b ⋆' a` is the coboundary of `K(a, b)` in cochain degree `e + f`.
The differentials are the ground-ring linear maps of the cylinder counts, for any potential bounds
of their kernels.

```lean
TauCeti.Floer.novikovProductOfMatrix_sub_negOnePowCast_smul_novikovProductOfMatrix_mem_coboundaries.{u_1,
    u_2, u_3, u_4, u_5, u_6, u_7, u_8, u_9}
  {R : Type u_1} {S : Type u_2} [AddCommGroup S] {ω : S →+ ℝ} {c : S →+ ℤ} {ι₁ : Type u_3}
  {ι₂ : Type u_4} {ι₀ : Type u_5} {P₁ : ι₁ → Type u_6} {P₂ : ι₂ → Type u_7} {P₀ : ι₀ → Type u_8}
  [(i : ι₁) → AddTorsor (TauCeti.Floer.PeriodGroup ω c) (P₁ i)]
  [(j : ι₂) → AddTorsor (TauCeti.Floer.PeriodGroup ω c) (P₂ j)]
  [(k : ι₀) → AddTorsor (TauCeti.Floer.PeriodGroup ω c) (P₀ k)] (r₁ : (i : ι₁) → P₁ i)
  (r₂ : (j : ι₂) → P₂ j) (r₀ : (k : ι₀) → P₀ k) {G : Type u_9} [AddMonoid G] {ωG : G →+ ℝ}
  (q : G →+ TauCeti.Floer.PeriodGroup ω c)
  (hq : ∀ (A : G), (TauCeti.Floer.PeriodGroup.area ω c) (q A) = ωG A) [CommRing R] [Fintype ι₁]
  [Fintype ι₂] [Fintype ι₀] {F₁ : (i : ι₁) × P₁ i → ℝ} {F₂ : (j : ι₂) × P₂ j → ℝ}
  {F₀ : (k : ι₀) × P₀ k → ℝ}
  (hF₁ :
    ∀ (i : ι₁) (γ : TauCeti.Floer.PeriodGroup ω c) (D : P₁ i),
      F₁ ⟨i, γ +ᵥ D⟩ = F₁ ⟨i, D⟩ - (-TauCeti.Floer.PeriodGroup.area ω c) γ)
  (hF₂ :
    ∀ (j : ι₂) (γ : TauCeti.Floer.PeriodGroup ω c) (D : P₂ j),
      F₂ ⟨j, γ +ᵥ D⟩ = F₂ ⟨j, D⟩ - (-TauCeti.Floer.PeriodGroup.area ω c) γ)
  (hF₀ :
    ∀ (k : ι₀) (γ : TauCeti.Floer.PeriodGroup ω c) (D : P₀ k),
      F₀ ⟨k, γ +ᵥ D⟩ = F₀ ⟨k, D⟩ - (-TauCeti.Floer.PeriodGroup.area ω c) γ)
  {μ₁ : (i : ι₁) × P₁ i → ℤ}
  (hμ₁ :
    ∀ (i : ι₁) (γ : TauCeti.Floer.PeriodGroup ω c) (D : P₁ i),
      μ₁ ⟨i, γ +ᵥ D⟩ = (TauCeti.Floer.PeriodGroup.degree ω c) γ + μ₁ ⟨i, D⟩)
  {μ₂ : (j : ι₂) × P₂ j → ℤ}
  (hμ₂ :
    ∀ (j : ι₂) (γ : TauCeti.Floer.PeriodGroup ω c) (D : P₂ j),
      μ₂ ⟨j, γ +ᵥ D⟩ = (TauCeti.Floer.PeriodGroup.degree ω c) γ + μ₂ ⟨j, D⟩)
  (Q : ι₁ → ι₂ → ι₀ → TauCeti.NovikovSeries R G ωG)
  (Q' : ι₂ → ι₁ → ι₀ → TauCeti.NovikovSeries R G ωG)
  (K : ι₁ → ι₂ → ι₀ → TauCeti.NovikovSeries R G ωG) (D₁ : ι₁ → ι₁ → TauCeti.NovikovSeries R G ωG)
  (D₂ : ι₂ → ι₂ → TauCeti.NovikovSeries R G ωG) (D₀ : ι₀ → ι₀ → TauCeti.NovikovSeries R G ωG)
  (n : ℤ) {μ₀ : (k : ι₀) × P₀ k → ℤ}
  (hμ₀ :
    ∀ (k : ι₀) (γ : TauCeti.Floer.PeriodGroup ω c) (D : P₀ k),
      μ₀ ⟨k, γ +ᵥ D⟩ = (TauCeti.Floer.PeriodGroup.degree ω c) γ + μ₀ ⟨k, D⟩)
  (hK :
    ∀ (i : ι₁) (j : ι₂) (k : ι₀),
      ∀ A ∈ (K i j k).support,
        μ₀ ⟨k, r₀ k⟩ - (TauCeti.Floer.PeriodGroup.degree ω c) (q A) =
          μ₁ ⟨i, r₁ i⟩ + μ₂ ⟨j, r₂ j⟩ - n + 1)
  (hC :
    ∀ (i : ι₁) (j : ι₂) (l : ι₀),
      Q i j l - TauCeti.negOnePowCast R ((n - μ₁ ⟨i, r₁ i⟩) * (n - μ₂ ⟨j, r₂ j⟩)) • Q' j i l =
        ∑ k, K i j k * D₀ k l + ∑ k, D₁ i k * K k j l +
          TauCeti.negOnePowCast R (n - μ₁ ⟨i, r₁ i⟩) • ∑ k, D₂ j k * K i k l)
  {C₁ C₂ C₀ : ℝ}
  (hδ₁ :
    ∀ (p p' : (k : ι₁) × P₁ k),
      TauCeti.NovikovModule.mapKernelOfMatrix r₁ r₁
            (fun i k => (TauCeti.Floer.coefficientComparison q hq) (D₁ i k)) p p' ≠
          0 →
        F₁ p' ≤ F₁ p + C₁)
  (hδ₂ :
    ∀ (p p' : (k : ι₂) × P₂ k),
      TauCeti.NovikovModule.mapKernelOfMatrix r₂ r₂
            (fun j k => (TauCeti.Floer.coefficientComparison q hq) (D₂ j k)) p p' ≠
          0 →
        F₂ p' ≤ F₂ p + C₂)
  (hδ₀ :
    ∀ (p p' : (k : ι₀) × P₀ k),
      TauCeti.NovikovModule.mapKernelOfMatrix r₀ r₀
            (fun k l => (TauCeti.Floer.coefficientComparison q hq) (D₀ k l)) p p' ≠
          0 →
        F₀ p' ≤ F₀ p + C₀)
  {e f : ℤ} {a : ↥(TauCeti.NovikovModule R F₁)} {b : ↥(TauCeti.NovikovModule R F₂)}
  (ha :
    a ∈
      (TauCeti.NovikovModule.kernelMap hδ₁ ⋯).cocycles
        (TauCeti.NovikovModule.gradeBy R F₁ fun p => n - μ₁ p) e)
  (hb :
    b ∈
      (TauCeti.NovikovModule.kernelMap hδ₂ ⋯).cocycles
        (TauCeti.NovikovModule.gradeBy R F₂ fun p => n - μ₂ p) f) :
  ((TauCeti.NovikovModule.novikovProductOfMatrix hF₁ hF₂ hF₀ r₁ r₂ r₀ fun i j k =>
            (TauCeti.Floer.coefficientComparison q hq) (Q i j k))
          a)
        b -
      TauCeti.negOnePowCast R (e * f) •
        ((TauCeti.NovikovModule.novikovProductOfMatrix hF₂ hF₁ hF₀ r₂ r₁ r₀ fun j i k =>
              (TauCeti.Floer.coefficientComparison q hq) (Q' j i k))
            b)
          a ∈
    (TauCeti.NovikovModule.kernelMap hδ₀ ⋯).coboundaries
      (TauCeti.NovikovModule.gradeBy R F₀ fun p => n - μ₀ p) (e + f)
```

## Depends on

- [TauCeti.NovikovModule.kernelProduct](tauceti-novikovmodule-kernelproduct.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Floer.novikovProductOfMatrix_sub_negOnePowCast_smul_novikovProductOfMatrix_mem_coboundaries`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Cap/Product.html#TauCeti.Floer.novikovProductOfMatrix_sub_negOnePowCast_smul_novikovProductOfMatrix_mem_coboundaries).

## Sources

- [Tau Ceti documentation: `TauCeti.Floer.novikovProductOfMatrix_sub_negOnePowCast_smul_novikovProductOfMatrix_mem_coboundaries`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Cap/Product.html#TauCeti.Floer.novikovProductOfMatrix_sub_negOnePowCast_smul_novikovProductOfMatrix_mem_coboundaries)
- [Source of `TauCeti.Floer.novikovProductOfMatrix_sub_negOnePowCast_smul_novikovProductOfMatrix_mem_coboundaries` in TauCeti/Geometry/Symplectic/Floer/Cap/Product.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Floer/Cap/Product.lean#L462)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
