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
- [Source of `TendstoUniformly` in Mathlib/Topology/UniformSpace/UniformConvergence.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/UniformSpace/UniformConvergence.lean#L112)
- [Mathlib overview: Topology › Uniform notions](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L240)
- [Mathlib undergraduate list: Single Variable Real Analysis › Sequences and series of functions](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L350)
