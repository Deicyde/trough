---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: omegaLimit
mathlib_file: Mathlib/Dynamics/OmegaLimit.lean
---

# Omega-limit sets

The ω-limit of a set `s` under `ϕ` with respect to a filter `f` is `⋂ u ∈ f, cl (ϕ u s)`.

```lean
omegaLimit.{u_1, u_2, u_3} {τ : Type u_1} {α : Type u_2} {β : Type u_3} [TopologicalSpace β]
  (f : Filter τ) (ϕ : τ → α → β) (s : Set α) : Set β
```

## Depends on

- [Closure](../../topology/general-topology/part-01/closure.md)
- [Filter](../../topology/general-topology/part-01/filter.md)

## Sources

- [Mathlib documentation: `omegaLimit`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Dynamics/OmegaLimit.html#omegaLimit)
- [Source of `omegaLimit` in Mathlib/Dynamics/OmegaLimit.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Dynamics/OmegaLimit.lean#L49)
- [Mathlib overview: Dynamics › General theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L563)
