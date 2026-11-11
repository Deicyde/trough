---
declaration: theorem
origin: cited
lean: ENNReal.inner_le_Lp_mul_Lq_tsum
statement: formalized
proof: formalized
---

# Hölder's inequality for unconditional sums in `ℝ≥0∞`

for conjugate exponents `p` and `q`,
`∑' i, f i * g i ≤ (∑' i, f i ^ p) ^ (1 / p) * (∑' i, g i ^ q) ^ (1 / q)`.
No summability hypotheses are needed; both sides may be infinite.

```lean
ENNReal.inner_le_Lp_mul_Lq_tsum.{u_1} {ι : Type u_1} (f g : ι → ENNReal) {p q : ℝ}
  (hpq : p.HolderConjugate q) :
  ∑' (i : ι), f i * g i ≤ (∑' (i : ι), f i ^ p) ^ (1 / p) * (∑' (i : ι), g i ^ q) ^ (1 / q)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ENNReal.inner_le_Lp_mul_Lq_tsum`](https://taucetiproject.org/docs/TauCeti/Analysis/MeanInequalities.html#ENNReal.inner_le_Lp_mul_Lq_tsum).

## Sources

- [Tau Ceti documentation: `ENNReal.inner_le_Lp_mul_Lq_tsum`](https://taucetiproject.org/docs/TauCeti/Analysis/MeanInequalities.html#ENNReal.inner_le_Lp_mul_Lq_tsum)
- [Source of `ENNReal.inner_le_Lp_mul_Lq_tsum` in TauCeti/Analysis/MeanInequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/MeanInequalities.lean#L187)
