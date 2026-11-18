---
declaration: theorem
origin: cited
lean: TauCeti.le_integral_sum_euclideanWittenLaplacian_mul_of_sq_add_sum_sq_eq_one
statement: formalized
proof: formalized
---

# Witten's localization estimate

Let `φ` be a compactly supported `C²` form, `f` a function
that is `C²` on the support of `φ`, and `J₀`, `J p` (`p ∈ P`) `C²` functions with
`J₀² + ∑ₚ (J p)² = 1` and `∑ᵢ (∂ᵢJ₀)² + ∑ₚ ∑ᵢ (∂ᵢ J p)² ≤ K` wherever `φ` does not vanish.
Suppose that near every point where `J p` does not vanish, `f` is the translated quadratic model
`y ↦ b p + ∑ᵢ a p i (yᵢ - pᵢ)² / 2` with every `|a p i| ≥ c`, and that `|df|² ≥ c₀` and
`∑_{i,j} |∂ᵢ∂ⱼf| ≤ h` wherever `J₀ φ` does not vanish. Then for `t ≥ 0`

`2 t c ∑ₚ ‖(J p φ)_{≠ s₀(p)}‖² + (t² c₀ - t h) ‖J₀ φ‖² - K ‖φ‖² ≤ ∫ ⟨Δ_t φ, φ⟩`,

where `(J p φ)_{≠ s₀(p)}` omits the component at the multi-index `s₀(p) = {i | a p i < 0}`, whose
cardinality is the Morse index of `p`, and `‖ψ‖² = ∫ ∑ s, ψ_s²`.

```lean
TauCeti.le_integral_sum_euclideanWittenLaplacian_mul_of_sq_add_sum_sq_eq_one.{u_1} {ι : Type u_1}
  [Fintype ι] [LinearOrder ι] {f : (ι → ℝ) → ℝ} {φ : (ι → ℝ) → Finset ι → ℝ} {P : Finset (ι → ℝ)}
  {J₀ : (ι → ℝ) → ℝ} {J : (ι → ℝ) → (ι → ℝ) → ℝ} {a : (ι → ℝ) → ι → ℝ} {b : (ι → ℝ) → ℝ}
  {t c c₀ h K : ℝ} (hf : ∀ x ∈ tsupport φ, ContDiffAt ℝ 2 f x) (hφ : ContDiff ℝ 2 φ)
  (hφc : HasCompactSupport φ) (hJ₀ : ContDiff ℝ 2 J₀) (hJ : ∀ p ∈ P, ContDiff ℝ 2 (J p))
  (hJ1 : ∀ (x : ι → ℝ), φ x ≠ 0 → J₀ x ^ 2 + ∑ p ∈ P, J p x ^ 2 = 1)
  (hK :
    ∀ (x : ι → ℝ),
      φ x ≠ 0 →
        ∑ i, (fderiv ℝ J₀ x) (Pi.single i 1) ^ 2 +
            ∑ p ∈ P, ∑ i, (fderiv ℝ (J p) x) (Pi.single i 1) ^ 2 ≤
          K)
  (hmodel :
    ∀ p ∈ P,
      ∀ (x : ι → ℝ),
        J p x ≠ 0 → f =ᶠ[nhds x] fun y => b p + TauCeti.diagonalQuadratic (a p) (y - p))
  (hc : ∀ p ∈ P, ∀ (i : ι), c ≤ |a p i|)
  (hc₀ : ∀ (x : ι → ℝ), J₀ x ≠ 0 → φ x ≠ 0 → c₀ ≤ ∑ i, (fderiv ℝ f x) (Pi.single i 1) ^ 2)
  (hh :
    ∀ (x : ι → ℝ),
      J₀ x ≠ 0 →
        φ x ≠ 0 → ∑ i, ∑ j, |((fderiv ℝ (fderiv ℝ f) x) (Pi.single i 1)) (Pi.single j 1)| ≤ h)
  (ht : 0 ≤ t) :
  ((2 * t * c *
          ∑ p ∈ P, ∫ (x : ι → ℝ), ∑ s ∈ Finset.univ.erase {i | a p i < 0}, (J p • φ) x s ^ 2) +
        (t ^ 2 * c₀ - t * h) * ∫ (x : ι → ℝ), ∑ s, (J₀ • φ) x s ^ 2) -
      K * ∫ (x : ι → ℝ), ∑ s, φ x s ^ 2 ≤
    ∫ (x : ι → ℝ), ∑ s, TauCeti.euclideanWittenLaplacian f t φ x s * φ x s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Witten's frame formula](wittens-frame-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.le_integral_sum_euclideanWittenLaplacian_mul_of_sq_add_sum_sq_eq_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/WittenLaplacian/Gap.html#TauCeti.le_integral_sum_euclideanWittenLaplacian_mul_of_sq_add_sum_sq_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.le_integral_sum_euclideanWittenLaplacian_mul_of_sq_add_sum_sq_eq_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/WittenLaplacian/Gap.html#TauCeti.le_integral_sum_euclideanWittenLaplacian_mul_of_sq_add_sum_sq_eq_one)
- [Source of `TauCeti.le_integral_sum_euclideanWittenLaplacian_mul_of_sq_add_sum_sq_eq_one` in TauCeti/Analysis/Calculus/WittenLaplacian/Gap.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/WittenLaplacian/Gap.lean#L135)
