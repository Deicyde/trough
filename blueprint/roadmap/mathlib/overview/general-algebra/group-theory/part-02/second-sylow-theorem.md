---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Sylow.isPretransitive_of_finite
mathlib_file: Mathlib/GroupTheory/Sylow.lean
---

# Second Sylow theorem

A generalization of **Sylow's second theorem**.
If the number of Sylow `p`-subgroups is finite, then all Sylow `p`-subgroups are conjugate.

```lean
Sylow.isPretransitive_of_finite.{u_1} {p : ℕ} {G : Type u_1} [Group G] [hp : Fact (Nat.Prime p)]
  [Finite (Sylow p G)] : MulAction.IsPretransitive G (Sylow p G)
```

## Depends on

- [Group action](../part-01/group-action.md)
- [Irreducible element](../../divisibility-in-integral-domains/irreducible-element.md)
- [Subgroup](../part-01/subgroup.md)

## Proof depends on

- [Cardinal](../../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Orbit](../../../../undergraduate/group-theory/basic-definitions/orbit.md)
- [Ring morphism](../../rings/ring-morphism.md)

## Sources

- [Mathlib documentation: `Sylow.isPretransitive_of_finite`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.isPretransitive_of_finite)
- [Source of `Sylow.isPretransitive_of_finite` in Mathlib/GroupTheory/Sylow.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Sylow.lean#L345)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L61)
