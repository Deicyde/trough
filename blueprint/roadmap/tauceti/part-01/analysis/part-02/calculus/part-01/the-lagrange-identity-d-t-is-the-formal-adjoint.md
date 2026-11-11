---
declaration: theorem
origin: cited
lean: TauCeti.sum_euclideanWittenExtDeriv_mul_sub_sum_mul_euclideanWittenCodifferential
statement: formalized
proof: formalized
---

# The Lagrange identity: `d_t^*` is the formal adjoint of `d_t`

For forms `φ`, `ψ`
differentiable at `x`, the pointwise pairings `⟨d_t φ, ψ⟩` and `⟨φ, d_t^* ψ⟩` differ by the
divergence `∑ᵢ ∂ᵢ ⟨φ, ιᵢ ψ⟩`, whose integral vanishes for compactly supported forms.

```lean
TauCeti.sum_euclideanWittenExtDeriv_mul_sub_sum_mul_euclideanWittenCodifferential.{u_1}
  {ι : Type u_1} [Fintype ι] [LinearOrder ι] (f : (ι → ℝ) → ℝ) (t : ℝ)
  {φ ψ : (ι → ℝ) → Finset ι → ℝ} {x : ι → ℝ} (hφ : DifferentiableAt ℝ φ x)
  (hψ : DifferentiableAt ℝ ψ x) :
  ∑ s, TauCeti.euclideanWittenExtDeriv f t φ x s * ψ x s -
      ∑ s, φ x s * TauCeti.euclideanWittenCodifferential f t ψ x s =
    ∑ i,
      (fderiv ℝ (fun y => ∑ s, φ y s * ((Pi.basisFun ℝ ι).exteriorContraction i) (ψ y) s) x)
        (Pi.single i 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_euclideanWittenExtDeriv_mul_sub_sum_mul_euclideanWittenCodifferential`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/WittenLaplacian/Basic.html#TauCeti.sum_euclideanWittenExtDeriv_mul_sub_sum_mul_euclideanWittenCodifferential).

## Sources

- [Tau Ceti documentation: `TauCeti.sum_euclideanWittenExtDeriv_mul_sub_sum_mul_euclideanWittenCodifferential`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/WittenLaplacian/Basic.html#TauCeti.sum_euclideanWittenExtDeriv_mul_sub_sum_mul_euclideanWittenCodifferential)
- [Source of `TauCeti.sum_euclideanWittenExtDeriv_mul_sub_sum_mul_euclideanWittenCodifferential` in TauCeti/Analysis/Calculus/WittenLaplacian/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/WittenLaplacian/Basic.lean#L188)
