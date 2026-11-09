---
declaration: theorem
origin: cited
lean: ProbabilityTheory.Kernel.pow_apply_singleton_mul_le_pow_add_apply
statement: formalized
proof: formalized
---

# Chapman–Kolmogorov lower bound

The `m + n`-step mass of a measurable set `s` is at least
the mass of the paths that sit at the intermediate state `y` at time `m`.

```lean
ProbabilityTheory.Kernel.pow_apply_singleton_mul_le_pow_add_apply.{u_1} {α : Type u_1}
  [MeasurableSpace α] (κ : ProbabilityTheory.Kernel α α) (m n : ℕ) (x y : α) {s : Set α}
  (hs : MeasurableSet s) : ((κ ^ m) x) {y} * ((κ ^ n) y) s ≤ ((κ ^ (m + n)) x) s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.Kernel.pow_apply_singleton_mul_le_pow_add_apply`](https://taucetiproject.org/docs/TauCeti/Probability/Kernel/Composition/Power.html#ProbabilityTheory.Kernel.pow_apply_singleton_mul_le_pow_add_apply).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.Kernel.pow_apply_singleton_mul_le_pow_add_apply`](https://taucetiproject.org/docs/TauCeti/Probability/Kernel/Composition/Power.html#ProbabilityTheory.Kernel.pow_apply_singleton_mul_le_pow_add_apply)
- [Source of `ProbabilityTheory.Kernel.pow_apply_singleton_mul_le_pow_add_apply` in TauCeti/Probability/Kernel/Composition/Power.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Kernel/Composition/Power.lean#L88)
