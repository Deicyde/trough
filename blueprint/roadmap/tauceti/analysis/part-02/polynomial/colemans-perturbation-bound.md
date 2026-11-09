---
declaration: theorem
origin: cited
lean: Polynomial.dist_coeff_colemanDBounded_mul_le
statement: formalized
proof: formalized
---

# Coleman's perturbation bound

Let `ρ` be a nonnegative antitone sequence and `r ≥ 1`. If
`P₁` has Newton majorant `ρ` up to degree `n`, the perturbation `P₂ - P₁` satisfies the same
bound after multiplication by `r`, and the coefficients of positive degree of `B₁` and of
`r (B₂ - B₁)` are bounded by `β` at every radius `ρ t`, where `B₁(0) = B₂(0) = 0`, then the
coefficients of the bounded Coleman transforms satisfy
`dist (coeff k D_(n,m)(B₂, P₂)) (coeff k D_(n,m)(B₁, P₁)) * r ≤ ∏ t < k, β t`.

Thus perturbing the inputs by a factor `r⁻¹` relative to their majorants moves every coefficient
of the transform by at most `r⁻¹` times its coefficient bound
`Polynomial.norm_coeff_colemanDBounded_le`, uniformly in the ranks `n` and degree bounds `m`.

```lean
Polynomial.dist_coeff_colemanDBounded_mul_le.{u_1} {R : Type u_1} [NormedCommRing R]
  [NormOneClass R] [IsUltrametricDist R] {B₁ B₂ P₁ P₂ : Polynomial R} {n m : ℕ} {ρ β : ℕ → ℝ}
  {r : ℝ} (hB₁ : B₁.coeff 0 = 0) (hB₂ : B₂.coeff 0 = 0) (hρ₀ : ∀ (i : ℕ), 0 ≤ ρ i) (hρ : Antitone ρ)
  (hr : 1 ≤ r) (hP₁ : ∀ j ≤ n, ‖P₁.coeff j‖ ≤ ∏ i ∈ Finset.range j, ρ i)
  (hP : ∀ j ≤ n, ‖(P₂ - P₁).coeff j‖ * r ≤ ∏ i ∈ Finset.range j, ρ i)
  (hβ₁ : ∀ (t j : ℕ), ‖B₁.coeff (j + 1)‖ * ρ t ^ (j + 1) ≤ β t)
  (hβ : ∀ (t j : ℕ), ‖(B₂ - B₁).coeff (j + 1)‖ * r * ρ t ^ (j + 1) ≤ β t) (k : ℕ) :
  dist ((B₂.colemanDBounded P₂ n m).coeff k) ((B₁.colemanDBounded P₁ n m).coeff k) * r ≤
    ∏ t ∈ Finset.range k, β t
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Coleman's coefficient bound](colemans-coefficient-bound.md)

## Lean

Formalized in Tau Ceti as [`Polynomial.dist_coeff_colemanDBounded_mul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Polynomial/Coleman/Basic.html#Polynomial.dist_coeff_colemanDBounded_mul_le).

## Sources

- [Tau Ceti documentation: `Polynomial.dist_coeff_colemanDBounded_mul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Polynomial/Coleman/Basic.html#Polynomial.dist_coeff_colemanDBounded_mul_le)
- [Source of `Polynomial.dist_coeff_colemanDBounded_mul_le` in TauCeti/Analysis/Polynomial/Coleman/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Polynomial/Coleman/Basic.lean#L312)
