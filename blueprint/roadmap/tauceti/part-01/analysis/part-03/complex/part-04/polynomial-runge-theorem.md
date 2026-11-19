---
declaration: theorem
origin: cited
lean: IsCompact.isConnected_compl_iff_forall_differentiableOn_exists_polynomial_norm_sub_lt
statement: formalized
proof: formalized
---

# Polynomial Runge theorem

a compact set `K ⊆ ℂ` has connected complement `Kᶜ` if and only
if every holomorphic function on an open neighbourhood `U ⊇ K` can be approximated uniformly on `K`
by polynomials `p : Polynomial ℂ`.

```lean
IsCompact.isConnected_compl_iff_forall_differentiableOn_exists_polynomial_norm_sub_lt {K : Set ℂ}
  (hK : IsCompact K) :
  IsConnected Kᶜ ↔
    ∀ (U : Set ℂ),
      IsOpen U →
        K ⊆ U →
          ∀ (f : ℂ → ℂ),
            DifferentiableOn ℂ f U → ∀ ε > 0, ∃ p, ∀ z ∈ K, ‖f z - Polynomial.eval z p‖ < ε
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Pompeiu formula with a cutoff](../part-01/the-cauchy-pompeiu-formula-with-a-cutoff.md)
- [Runge's approximation theorem (domain-relative form)](runges-approximation-theorem-domain-relative-for.md)

## Lean

Formalized in Tau Ceti as [`IsCompact.isConnected_compl_iff_forall_differentiableOn_exists_polynomial_norm_sub_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Runge/Approximation.html#IsCompact.isConnected_compl_iff_forall_differentiableOn_exists_polynomial_norm_sub_lt).

## Sources

- [Tau Ceti documentation: `IsCompact.isConnected_compl_iff_forall_differentiableOn_exists_polynomial_norm_sub_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Runge/Approximation.html#IsCompact.isConnected_compl_iff_forall_differentiableOn_exists_polynomial_norm_sub_lt)
- [Source of `IsCompact.isConnected_compl_iff_forall_differentiableOn_exists_polynomial_norm_sub_lt` in TauCeti/Analysis/Complex/Runge/Approximation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Runge/Approximation.lean#L283)
