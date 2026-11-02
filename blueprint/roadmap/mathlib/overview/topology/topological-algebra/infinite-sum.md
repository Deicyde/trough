---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: HasSum
mathlib_file: Mathlib/Topology/Algebra/InfiniteSum/Defs.lean
---

# Infinite sum

`HasSum f a L` means that the (potentially infinite) sum of the `f b` for `b : β`
converges to `a` along the SummationFilter `L`.

By default `L` is the `unconditional` one, corresponding to the limit of all finite sets towards
the entire type. So we take the sum over bigger and bigger finite sets. This sum operation is
invariant under permuting the terms (while sums for more general summation filters usually are not).
This is based on Mario Carneiro's
[infinite sum `df-tsms` in Metamath](http://us.metamath.org/mpeuni/df-tsms.html).

In particular, the function `ℕ → ℝ` sending `n` to `(-1) ^ n / (n + 1)` does not have a
sum for this definition, although it is summable for the `conditional` summation filter that
takes limits of sums over `n ∈ {0, ..., X}` as `X → ∞`. However, a series which is *absolutely*
convergent with respect to the conditional summation filter is in fact unconditionally summable.

For the definition and many statements, `α` does not need to be a topological additive monoid,
only an additive monoid with a topology (i.e. the addition is not assumed to be continuous). We
only add this assumption later, for the lemmas where it is relevant.

```lean
HasSum.{u_1, u_2} {α : Type u_1} {β : Type u_2} [AddCommMonoid α] [TopologicalSpace α] (f : β → α)
  (a : α) (L : SummationFilter β := SummationFilter.unconditional β) : Prop
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Limit of a map with respect to filters](../general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Topological space](../general-topology/part-01/topological-space.md)

## Sources

- [Mathlib documentation: `HasSum`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/InfiniteSum/Defs.html#HasSum)
- [Source of `HasSum` in Mathlib/Topology/Algebra/InfiniteSum/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Algebra/InfiniteSum/Defs.lean#L90)
- [Mathlib overview: Topology › Topological algebra](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L253)
