---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: TendstoUniformly
mathlib_file: Mathlib/Topology/UniformSpace/UniformConvergence.lean
---

# Uniform convergence

A sequence of functions `Fₙ` converges uniformly to a limiting function `f` with respect to a
filter `p` if, for any entourage of the diagonal `u`, one has `p`-eventually
`(f x, Fₙ x) ∈ u` for all `x`.

```lean
TendstoUniformly.{u_1, u_2, u_4} {α : Type u_1} {β : Type u_2} {ι : Type u_4} [UniformSpace β]
  (F : ι → α → β) (f : α → β) (p : Filter ι) : Prop
```

## Depends on

- [Uniform space](uniform-space.md)

## Sources

- [Mathlib documentation: `TendstoUniformly`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/UniformSpace/UniformConvergence.html#TendstoUniformly)
- [Source of `TendstoUniformly` in Mathlib/Topology/UniformSpace/UniformConvergence.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/UniformSpace/UniformConvergence.lean#L112)
- [Mathlib overview: Topology › Uniform notions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L240)
- [Mathlib undergraduate list: Single Variable Real Analysis › Sequences and series of functions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L350)
