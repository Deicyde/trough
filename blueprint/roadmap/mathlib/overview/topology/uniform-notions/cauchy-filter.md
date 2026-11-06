# Cauchy filter

A filter `f` is Cauchy if for every entourage `r`, there exists an
`s ∈ f` such that `s × s ⊆ r`. This is a generalization of Cauchy
sequences, because if `a : ℕ → α` then the filter of sets containing
cofinitely many of the `a n` is Cauchy iff `a` is a Cauchy sequence.

```lean
Cauchy.{u} {α : Type u} [uniformSpace : UniformSpace α] (f : Filter α) : Prop
```

## Depends on

- [Uniform space](uniform-space.md)

## Sources

- [Mathlib documentation: `Cauchy`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/UniformSpace/Cauchy.html#Cauchy)
- [Source of `Cauchy` in Mathlib/Topology/UniformSpace/Cauchy.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/UniformSpace/Cauchy.lean#L26)
- [Mathlib overview: Topology › Uniform notions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L241)
