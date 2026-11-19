---
declaration: theorem
origin: cited
lean: TauCeti.eq_zero_of_tsum_prod_pow_smul_eventuallyEq_zero
statement: formalized
proof: formalized
---

# The identity theorem for multi-index series

if `∑ α, ‖c α‖ * r ^ (∑ i, α i)` converges
for some `r > 0` and `z ↦ ∑' α, (∏ i, z i ^ α i) • c α` vanishes near `0`, then every
coefficient `c α` is zero.

```lean
TauCeti.eq_zero_of_tsum_prod_pow_smul_eventuallyEq_zero.{u_1, u_2, u_3} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {ι : Type u_2} [Fintype ι] {F : Type u_3} [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [CompleteSpace F] {c : (ι → ℕ) → F} {r : NNReal} (hr : 0 < r)
  (hsum : Summable fun α => ‖c α‖ * ↑r ^ ∑ i, α i)
  (h0 : (fun z => ∑' (α : ι → ℕ), (∏ i, z i ^ α i) • c α) =ᶠ[nhds 0] 0) (α : ι → ℕ) : c α = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The identity theorem in coefficient form](the-identity-theorem-in-coefficient-form.md)
- [TauCeti.hasFPowerSeriesOnBall_tsum](../../part-02/linear-forms-in-logarithms-bakers-theorem-over-c/tauceti-hasfpowerseriesonball-tsum.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eq_zero_of_tsum_prod_pow_smul_eventuallyEq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/MultiIndex/Coeff.html#TauCeti.eq_zero_of_tsum_prod_pow_smul_eventuallyEq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.eq_zero_of_tsum_prod_pow_smul_eventuallyEq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/MultiIndex/Coeff.html#TauCeti.eq_zero_of_tsum_prod_pow_smul_eventuallyEq_zero)
- [Source of `TauCeti.eq_zero_of_tsum_prod_pow_smul_eventuallyEq_zero` in TauCeti/Analysis/Analytic/MultiIndex/Coeff.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Analytic/MultiIndex/Coeff.lean#L385)
