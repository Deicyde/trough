---
declaration: theorem
origin: cited
lean: TauCeti.weakLpNorm_smul_le, ENNReal.inner_le_Lp_mul_Lq_tsum
statement: formalized
proof: formalized
---

# Hölder's inequality for weak norms

Multiplying a finite family by scalar weights `c`
multiplies its weak norm by at most the `ℓˢ` norm of the weights, when `1 / p = 1 / s + 1 / q`
with finite `p` and `q`.

```lean
TauCeti.weakLpNorm_smul_le.{u_1, u_2, u_4} {𝕜 : Type u_1} {E : Type u_2} {ι : Type u_4}
  [NontriviallyNormedField 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] [Fintype ι] (p : ENNReal)
  [Fact (1 ≤ p)] {q : ENNReal} [Fact (1 ≤ q)] {s : ℝ} (hspq : s.HolderTriple q.toReal p.toReal)
  (c : ι → 𝕜) (x : ι → E) :
  ((TauCeti.weakLpNorm p) fun i => c i • x i) ≤
    (∑ i, ‖c i‖ ^ s) ^ (1 / s) * (TauCeti.weakLpNorm q) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.weakLpNorm_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Lp/Weak.html#TauCeti.weakLpNorm_smul_le).

## Other forms

**Hölder's inequality for unconditional sums in `ℝ≥0∞`.** Formalized in Tau Ceti as [`ENNReal.inner_le_Lp_mul_Lq_tsum`](https://taucetiproject.org/docs/TauCeti/Analysis/MeanInequalities.html#ENNReal.inner_le_Lp_mul_Lq_tsum).

```lean
ENNReal.inner_le_Lp_mul_Lq_tsum.{u_1} {ι : Type u_1} (f g : ι → ENNReal) {p q : ℝ}
  (hpq : p.HolderConjugate q) :
  ∑' (i : ι), f i * g i ≤ (∑' (i : ι), f i ^ p) ^ (1 / p) * (∑' (i : ι), g i ^ q) ^ (1 / q)
```

## Sources

- [Tau Ceti documentation: `TauCeti.weakLpNorm_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Lp/Weak.html#TauCeti.weakLpNorm_smul_le)
- [Source of `TauCeti.weakLpNorm_smul_le` in TauCeti/Analysis/Normed/Lp/Weak.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Lp/Weak.lean#L156)
