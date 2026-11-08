---
declaration: theorem
origin: cited
lean: TauCeti.weakLpNorm_smul_le
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

## Sources

- [Tau Ceti documentation: `TauCeti.weakLpNorm_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Lp/Weak.html#TauCeti.weakLpNorm_smul_le)
- [Source of `TauCeti.weakLpNorm_smul_le` in TauCeti/Analysis/Normed/Lp/Weak.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Lp/Weak.lean#L156)
