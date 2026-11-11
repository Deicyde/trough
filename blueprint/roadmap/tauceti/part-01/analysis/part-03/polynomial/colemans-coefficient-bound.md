---
declaration: theorem
origin: cited
lean: Polynomial.norm_coeff_colemanDBounded_le
statement: formalized
proof: formalized
---

# Coleman's coefficient bound

Let `P` and `B` be polynomials over an ultrametric seminormed
ring with `‖1‖ = 1` and `B(0) = 0`. If `ρ` is a nonnegative antitone sequence with
`‖coeff j P‖ ≤ ∏ i < j, ρ i` for `j ≤ n`, and `‖coeff l B‖ * ρ t ^ l ≤ β t` for every `t` and every
`l ≥ 1`, then the `k`-th coefficient of Coleman's transform `D_(n,m)(B, P)` has norm at most
`∏ t < k, β t`, for all ranks `n` and degree bounds `m`.

```lean
Polynomial.norm_coeff_colemanDBounded_le.{u_1} {R : Type u_1} [SeminormedCommRing R]
  {B P : Polynomial R} {n m : ℕ} [NormOneClass R] [IsUltrametricDist R] {ρ β : ℕ → ℝ}
  (hB₀ : B.coeff 0 = 0) (hρ₀ : ∀ (i : ℕ), 0 ≤ ρ i) (hρ : Antitone ρ)
  (hP : ∀ j ≤ n, ‖P.coeff j‖ ≤ ∏ i ∈ Finset.range j, ρ i)
  (hβ : ∀ (t j : ℕ), ‖B.coeff (j + 1)‖ * ρ t ^ (j + 1) ≤ β t) (k : ℕ) :
  ‖(B.colemanDBounded P n m).coeff k‖ ≤ ∏ t ∈ Finset.range k, β t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.norm_coeff_colemanDBounded_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Polynomial/Coleman/Basic.html#Polynomial.norm_coeff_colemanDBounded_le).

## Sources

- [Tau Ceti documentation: `Polynomial.norm_coeff_colemanDBounded_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Polynomial/Coleman/Basic.html#Polynomial.norm_coeff_colemanDBounded_le)
- [Source of `Polynomial.norm_coeff_colemanDBounded_le` in TauCeti/Analysis/Polynomial/Coleman/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Polynomial/Coleman/Basic.lean#L215)
