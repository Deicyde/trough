---
declaration: theorem
origin: cited
lean: TauCeti.mk_sum_aeval_schurPoly_mul_aeval_schurPoly, TauCeti.sum_aeval_schurPoly_mul_aeval_schurPoly
statement: formalized
proof: formalized
---

# The Cauchy identity

for families `f : σ → S` and `g : τ → S`,

`∑_λ s_λ(f) s_λ(g) t^{|λ|} = ∏_{i,j} (1 - fᵢ gⱼ t)⁻¹`,

as power series over `S`, the coefficient of `tⁿ` on the left summing over the partitions `λ` of
`n`, and the factor `(1 - fᵢ gⱼ t)⁻¹` on the right written as the geometric series
`∑ₘ (fᵢ gⱼ)ᵐ tᵐ`.

```lean
TauCeti.mk_sum_aeval_schurPoly_mul_aeval_schurPoly.{u_1, u_2, u_3, u_4} {σ : Type u_1}
  {τ : Type u_2} {R : Type u_3} {S : Type u_4} [Fintype σ] [Fintype τ] [CommSemiring R]
  [CommSemiring S] [Algebra R S] (f : σ → S) (g : τ → S) :
  (PowerSeries.mk fun n =>
      ∑ μ,
        (MvPolynomial.aeval f) (TauCeti.schurPoly σ R μ) *
          (MvPolynomial.aeval g) (TauCeti.schurPoly τ R μ)) =
    ∏ i, ∏ j, PowerSeries.mk fun m => (f i * g j) ^ m
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobi's bialternant formula](jacobis-bialternant-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mk_sum_aeval_schurPoly_mul_aeval_schurPoly`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/Cauchy.html#TauCeti.mk_sum_aeval_schurPoly_mul_aeval_schurPoly).

## Other forms

**The Cauchy identity in degree `n`.** Formalized in Tau Ceti as [`TauCeti.sum_aeval_schurPoly_mul_aeval_schurPoly`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/Cauchy.html#TauCeti.sum_aeval_schurPoly_mul_aeval_schurPoly).

```lean
TauCeti.sum_aeval_schurPoly_mul_aeval_schurPoly.{u_1, u_2, u_3, u_4} {σ : Type u_1} {τ : Type u_2}
  {R : Type u_3} {S : Type u_4} [Fintype σ] [DecidableEq σ] [Fintype τ] [DecidableEq τ]
  [CommSemiring R] [CommSemiring S] [Algebra R S] (f : σ → S) (g : τ → S) (n : ℕ) :
  ∑ μ,
      (MvPolynomial.aeval f) (TauCeti.schurPoly σ R μ) *
        (MvPolynomial.aeval g) (TauCeti.schurPoly τ R μ) =
    (MvPolynomial.aeval fun p => f p.1 * g p.2) (MvPolynomial.hsymm (σ × τ) R n)
```

## Sources

- [Tau Ceti documentation: `TauCeti.mk_sum_aeval_schurPoly_mul_aeval_schurPoly`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/Cauchy.html#TauCeti.mk_sum_aeval_schurPoly_mul_aeval_schurPoly)
- [Source of `TauCeti.mk_sum_aeval_schurPoly_mul_aeval_schurPoly` in TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/Cauchy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/Cauchy.lean#L89)
