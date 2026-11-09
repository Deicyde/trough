---
declaration: theorem
origin: cited
lean: TauCeti.NovikovModule.kernelComp_eq_add_of_functionalBoundary_eq_zero
statement: formalized
proof: formalized
---

# The Leibniz kernel identity from a closed product functional

Let the product kernel `n`
have cochain degree `0`. If the readout of `n`, a functional on `C₁ ⊗ C₂ ⊗ C₀^∨`, is annihilated
by the total differential built from the Koszul tensor differential of `C₁ ⊗ C₂`, then `n` obeys
the Leibniz identity between kernels
`∑ n(p₁, p₂, p) δ₀(p, p₀) = ∑ δ₁(p₁, p) n(p, p₂, p₀) + (-1)^(d₁ p₁) ∑ δ₂(p₂, p) n(p₁, p, p₀)`
of `TauCeti.NovikovModule.kernelMap_kernelProduct_eq_add`.

```lean
TauCeti.NovikovModule.kernelComp_eq_add_of_functionalBoundary_eq_zero.{u_1, u_3, u_4, u_5}
  {R : Type u_1} {S₀ : Type u_3} [CommRing R] {S₁ : Type u_4} {S₂ : Type u_5} [DecidableEq S₁]
  [DecidableEq S₂] {F₁ : S₁ → ℝ} {F₂ : S₂ → ℝ} {F₀ : S₀ → ℝ} {C : ℝ} {n : S₁ → S₂ → S₀ → R}
  (hn : ∀ (p₁ : S₁) (p₂ : S₂) (p₀ : S₀), n p₁ p₂ p₀ ≠ 0 → F₀ p₀ ≤ F₁ p₁ + F₂ p₂ + C)
  {δ₁ : S₁ → S₁ → R} (hδ₁fin : ∀ (p : S₁), δ₁ p ∈ TauCeti.NovikovModule R F₁) {δ₂ : S₂ → S₂ → R}
  (hδ₂fin : ∀ (p : S₂), δ₂ p ∈ TauCeti.NovikovModule R F₂) {δ₀ : S₀ → S₀ → R} {d₁ : S₁ → ℤ}
  {d₂ : S₂ → ℤ} {d₀ : S₀ → ℤ}
  (hdeg : ∀ (p₁ : S₁) (p₂ : S₂) (p₀ : S₀), n p₁ p₂ p₀ ≠ 0 → d₀ p₀ = d₁ p₁ + d₂ p₂) {p₁ : S₁}
  {p₂ : S₂} {p₀ : S₀}
  (hφ :
    TauCeti.NovikovModule.functionalBoundary (fun q => d₁ q.1 + d₂ q.2) d₀
        (TauCeti.NovikovModule.tensorDifferential d₁ δ₁ δ₂) δ₀
        (TauCeti.NovikovModule.kernelReadout d₀ fun q => n q.1 q.2) (p₁, p₂) p₀ =
      0) :
  TauCeti.NovikovModule.kernelComp (n p₁) δ₀ p₂ p₀ =
    TauCeti.NovikovModule.kernelComp δ₁ (fun p => n p p₂) p₁ p₀ +
      TauCeti.negOnePowCast R (d₁ p₁) * TauCeti.NovikovModule.kernelComp δ₂ (n p₁) p₂ p₀
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NovikovModule.kernelComp_eq_add_of_functionalBoundary_eq_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovModule/Readout.html#TauCeti.NovikovModule.kernelComp_eq_add_of_functionalBoundary_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.NovikovModule.kernelComp_eq_add_of_functionalBoundary_eq_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovModule/Readout.html#TauCeti.NovikovModule.kernelComp_eq_add_of_functionalBoundary_eq_zero)
- [Source of `TauCeti.NovikovModule.kernelComp_eq_add_of_functionalBoundary_eq_zero` in TauCeti/RingTheory/NovikovModule/Readout.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/NovikovModule/Readout.lean#L286)
