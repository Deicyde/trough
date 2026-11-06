# Cauchy sequence

Cauchy sequences. Usually defined on ℕ, but often it is also useful to say that a function
defined on ℝ is Cauchy at +∞ to deduce convergence. Therefore, we define it in a type class that
is general enough to cover both ℕ and ℝ, which are the main motivating examples.

```lean
CauchySeq.{u, v} {α : Type u} {β : Type v} [uniformSpace : UniformSpace α] [Preorder β]
  (u : β → α) : Prop
```

## Depends on

- [Cauchy filter](cauchy-filter.md)

## Sources

- [Mathlib documentation: `CauchySeq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/UniformSpace/Cauchy.html#CauchySeq)
- [Source of `CauchySeq` in Mathlib/Topology/UniformSpace/Cauchy.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/UniformSpace/Cauchy.lean#L182)
- [Mathlib overview: Topology › Uniform notions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L242)
- [Mathlib undergraduate list: Single Variable Real Analysis › Sequences of real numbers](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L288)
