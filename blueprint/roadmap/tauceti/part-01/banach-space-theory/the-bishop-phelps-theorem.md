---
declaration: theorem
origin: cited
lean: TauCeti.dense_setOf_exists_norm_apply_eq_norm
statement: formalized
proof: formalized
---

# The Bishop–Phelps theorem

The continuous linear functionals on a Banach space which
attain their norm on the closed unit ball are norm dense in the dual.

```lean
TauCeti.dense_setOf_exists_norm_apply_eq_norm.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] [CompleteSpace E] :
  Dense {g | ∃ x, ‖x‖ ≤ 1 ∧ ‖g x‖ = ‖g‖}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.dense_setOf_exists_norm_apply_eq_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.html#TauCeti.dense_setOf_exists_norm_apply_eq_norm).

## Sources

- [Tau Ceti documentation: `TauCeti.dense_setOf_exists_norm_apply_eq_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.html#TauCeti.dense_setOf_exists_norm_apply_eq_norm)
- [Source of `TauCeti.dense_setOf_exists_norm_apply_eq_norm` in TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.lean#L326)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
