---
declaration: theorem
origin: cited
lean: ENNReal.Lp_add_le_tsum
statement: formalized
proof: formalized
---

# Minkowski's inequality for unconditional sums in `ℝ≥0∞`

for `1 ≤ p`,
`(∑' i, (f i + g i) ^ p) ^ (1 / p) ≤ (∑' i, f i ^ p) ^ (1 / p) + (∑' i, g i ^ p) ^ (1 / p)`.
No summability hypotheses are needed; both sides may be infinite.

```lean
ENNReal.Lp_add_le_tsum.{u_1} {ι : Type u_1} (f g : ι → ENNReal) {p : ℝ} (hp : 1 ≤ p) :
  (∑' (i : ι), (f i + g i) ^ p) ^ (1 / p) ≤
    (∑' (i : ι), f i ^ p) ^ (1 / p) + (∑' (i : ι), g i ^ p) ^ (1 / p)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ENNReal.Lp_add_le_tsum`](https://taucetiproject.org/docs/TauCeti/Analysis/MeanInequalities.html#ENNReal.Lp_add_le_tsum).

## Sources

- [Tau Ceti documentation: `ENNReal.Lp_add_le_tsum`](https://taucetiproject.org/docs/TauCeti/Analysis/MeanInequalities.html#ENNReal.Lp_add_le_tsum)
- [Source of `ENNReal.Lp_add_le_tsum` in TauCeti/Analysis/MeanInequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/MeanInequalities.lean#L147)
