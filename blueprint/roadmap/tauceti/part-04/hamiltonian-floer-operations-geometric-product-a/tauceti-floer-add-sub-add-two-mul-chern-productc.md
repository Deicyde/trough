---
declaration: theorem
origin: cited
lean: TauCeti.Floer.add_sub_add_two_mul_chern_productClass_eq
statement: formalized
proof: formalized
---

# TauCeti.Floer.add\_sub\_add\_two\_mul\_chern\_productClass\_eq

Cap independence of the index `μ₁(D₁) + μ₂(D₂) − μ₀(D₀) + 2 c₁(A)` of a product coefficient,
for gradings `mᵢ` obeying the recapping law for twice the first Chern number. The Fredholm index
of a pair of pants in class `A` is this quantity minus half the dimension of the target.

```lean
TauCeti.Floer.add_sub_add_two_mul_chern_productClass_eq.{u_1, u_2, u_3, u_4} {S : Type u_1}
  [AddGroup S] {ω : S →+ ℝ} {c : S →+ ℤ} {C₁ : Type u_2} {C₂ : Type u_3} {C₀ : Type u_4}
  [AddTorsor (TauCeti.Floer.PeriodGroup ω c) C₀] {glue : C₁ → C₂ → C₀}
  [AddTorsor (TauCeti.Floer.PeriodGroup ω c) C₁] [AddTorsor (TauCeti.Floer.PeriodGroup ω c) C₂]
  {m₁ : C₁ → ℤ} {m₂ : C₂ → ℤ} {m₀ : C₀ → ℤ}
  (hglue₁ :
    ∀ (γ : TauCeti.Floer.PeriodGroup ω c) (D₁ : C₁) (D₂ : C₂), glue (γ +ᵥ D₁) D₂ = γ +ᵥ glue D₁ D₂)
  (hglue₂ :
    ∀ (γ : TauCeti.Floer.PeriodGroup ω c) (D₁ : C₁) (D₂ : C₂), glue D₁ (γ +ᵥ D₂) = γ +ᵥ glue D₁ D₂)
  (hm₁ :
    ∀ (γ : TauCeti.Floer.PeriodGroup ω c) (D : C₁),
      m₁ (γ +ᵥ D) = 2 * (TauCeti.Floer.PeriodGroup.chern ω c) γ + m₁ D)
  (hm₂ :
    ∀ (γ : TauCeti.Floer.PeriodGroup ω c) (D : C₂),
      m₂ (γ +ᵥ D) = 2 * (TauCeti.Floer.PeriodGroup.chern ω c) γ + m₂ D)
  (hm₀ :
    ∀ (γ : TauCeti.Floer.PeriodGroup ω c) (D : C₀),
      m₀ (γ +ᵥ D) = 2 * (TauCeti.Floer.PeriodGroup.chern ω c) γ + m₀ D)
  (D₁ D₁' : C₁) (D₂ D₂' : C₂) (D₀ D₀' : C₀) :
  m₁ D₁ + m₂ D₂ - m₀ D₀ +
      2 * (TauCeti.Floer.PeriodGroup.chern ω c) (TauCeti.Floer.productClass glue D₁ D₂ D₀) =
    m₁ D₁' + m₂ D₂' - m₀ D₀' +
      2 * (TauCeti.Floer.PeriodGroup.chern ω c) (TauCeti.Floer.productClass glue D₁' D₂' D₀')
```

## Depends on

- [TauCeti.Floer.PeriodGroup](tauceti-floer-periodgroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Floer.add_sub_add_two_mul_chern_productClass_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Cap/Basic.html#TauCeti.Floer.add_sub_add_two_mul_chern_productClass_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Floer.add_sub_add_two_mul_chern_productClass_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Cap/Basic.html#TauCeti.Floer.add_sub_add_two_mul_chern_productClass_eq)
- [Source of `TauCeti.Floer.add_sub_add_two_mul_chern_productClass_eq` in TauCeti/Geometry/Symplectic/Floer/Cap/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Floer/Cap/Basic.lean#L260)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
