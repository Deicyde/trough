---
declaration: theorem
origin: cited
lean: IsCompact.exists_norm_sub_sum_mul_sub_inv_smul_le
statement: formalized
proof: formalized
---

# Discretized Cauchy–Pompeiu formula

Let `K` be a compact subset of an open set `V ⊆ ℂ`.
For every `ε > 0` there are finitely many poles `ζ i ∈ V \ K` and coefficients `c i` such that every
`f : ℂ → F` into a complex normed space, holomorphic on `V` and bounded by `M` there, satisfies
`‖f w - ∑ i, (c i * (w - ζ i)⁻¹) • f (ζ i)‖ ≤ ε * M` for every `w ∈ K`.

The poles and coefficients depend only on `K`, `V` and `ε`, not on `f` or `F`, so the approximation
is a linear operator in `f` through the finitely many values `f (ζ i)`, uniformly accurate on the
bounded holomorphic functions; for scalar `f` it has finite rank.

```lean
IsCompact.exists_norm_sub_sum_mul_sub_inv_smul_le.{u} {K V : Set ℂ} (hK : IsCompact K)
  (hV : IsOpen V) (hKV : K ⊆ V) {ε : ℝ} (hε : 0 < ε) :
  ∃ N ζ c,
    (∀ (i : Fin N), ζ i ∈ V \ K) ∧
      ∀ {F : Type u} [inst : NormedAddCommGroup F] [inst_1 : NormedSpace ℂ F] (f : ℂ → F) (M : ℝ),
        DifferentiableOn ℂ f V →
          (∀ z ∈ V, ‖f z‖ ≤ M) → ∀ w ∈ K, ‖f w - ∑ i, (c i * (w - ζ i)⁻¹) • f (ζ i)‖ ≤ ε * M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy estimate](cauchy-estimate.md)
- [The Cauchy–Pompeiu formula with a cutoff](the-cauchy-pompeiu-formula-with-a-cutoff.md)

## Lean

Formalized in Tau Ceti as [`IsCompact.exists_norm_sub_sum_mul_sub_inv_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pompeiu/Discretization.html#IsCompact.exists_norm_sub_sum_mul_sub_inv_smul_le).

## Sources

- [Tau Ceti documentation: `IsCompact.exists_norm_sub_sum_mul_sub_inv_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pompeiu/Discretization.html#IsCompact.exists_norm_sub_sum_mul_sub_inv_smul_le)
- [Source of `IsCompact.exists_norm_sub_sum_mul_sub_inv_smul_le` in TauCeti/Analysis/Complex/Pompeiu/Discretization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Pompeiu/Discretization.lean#L103)
