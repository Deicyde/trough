---
declaration: theorem
origin: cited
lean: LowerSemicontinuous.exists_add_mul_dist_le_and_lt_add_mul_dist
statement: formalized
proof: formalized
---

# Ekeland's variational principle

Let `φ` be a lower semicontinuous function, bounded below,
on a complete metric space, and let `ε > 0`. For every `x` there is a point `y` such that
`φ y + ε * dist y x ≤ φ x` and `y` is the strict global minimum of `z ↦ φ z + ε * dist z y`.

```lean
LowerSemicontinuous.exists_add_mul_dist_le_and_lt_add_mul_dist.{u_1} {X : Type u_1} [MetricSpace X]
  [CompleteSpace X] {φ : X → ℝ} (hφ : LowerSemicontinuous φ) (hbdd : BddBelow (Set.range φ)) {ε : ℝ}
  (hε : 0 < ε) (x : X) : ∃ y, φ y + ε * dist y x ≤ φ x ∧ ∀ (z : X), z ≠ y → φ y < φ z + ε * dist z y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LowerSemicontinuous.exists_add_mul_dist_le_and_lt_add_mul_dist`](https://taucetiproject.org/docs/TauCeti/Topology/MetricSpace/Ekeland.html#LowerSemicontinuous.exists_add_mul_dist_le_and_lt_add_mul_dist).

## Sources

- [Tau Ceti documentation: `LowerSemicontinuous.exists_add_mul_dist_le_and_lt_add_mul_dist`](https://taucetiproject.org/docs/TauCeti/Topology/MetricSpace/Ekeland.html#LowerSemicontinuous.exists_add_mul_dist_le_and_lt_add_mul_dist)
- [Source of `LowerSemicontinuous.exists_add_mul_dist_le_and_lt_add_mul_dist` in TauCeti/Topology/MetricSpace/Ekeland.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/MetricSpace/Ekeland.lean#L43)
