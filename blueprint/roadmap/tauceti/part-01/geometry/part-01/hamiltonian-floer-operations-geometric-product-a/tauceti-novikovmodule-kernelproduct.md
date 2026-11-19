---
declaration: def
origin: cited
lean: TauCeti.NovikovModule.kernelProduct
statement: formalized
---

# TauCeti.NovikovModule.kernelProduct

The bilinear product of completed combinations given by a kernel `n` with potential bound `C`
and completed outputs: the coefficient of `p₀` in the product of `a` and `b` is the finite sum
`∑ a(p₁) b(p₂) n(p₁, p₂, p₀)` over all pairs of generators.

```lean
TauCeti.NovikovModule.kernelProduct.{u_1, u_2, u_3, u_4} {R : Type u_1} {S₁ : Type u_2}
  {S₂ : Type u_3} {S₀ : Type u_4} {F₁ : S₁ → ℝ} {F₂ : S₂ → ℝ} {F₀ : S₀ → ℝ} [CommSemiring R] {C : ℝ}
  {n : S₁ → S₂ → S₀ → R}
  (hn : ∀ (p₁ : S₁) (p₂ : S₂) (p₀ : S₀), n p₁ p₂ p₀ ≠ 0 → F₀ p₀ ≤ F₁ p₁ + F₂ p₂ + C)
  (hfin : ∀ (p₁ : S₁) (p₂ : S₂), n p₁ p₂ ∈ TauCeti.NovikovModule R F₀) :
  ↥(TauCeti.NovikovModule R F₁) →ₗ[R]
    ↥(TauCeti.NovikovModule R F₂) →ₗ[R] ↥(TauCeti.NovikovModule R F₀)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NovikovModule.kernelProduct`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovModule/Bilinear.html#TauCeti.NovikovModule.kernelProduct).

## Sources

- [Tau Ceti documentation: `TauCeti.NovikovModule.kernelProduct`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovModule/Bilinear.html#TauCeti.NovikovModule.kernelProduct)
- [Source of `TauCeti.NovikovModule.kernelProduct` in TauCeti/RingTheory/NovikovModule/Bilinear.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/NovikovModule/Bilinear.lean#L204)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
