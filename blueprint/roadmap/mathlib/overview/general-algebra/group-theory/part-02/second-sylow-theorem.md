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
- [Group morphism](../part-01/group-morphism.md)
- [Irreducible element](../../divisibility-in-integral-domains/irreducible-element.md)
- [Subgroup](../part-01/subgroup.md)

## Proof depends on

- [Cantor’s Theorem](../../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cauchy's theorem (group theory)](../../../../thousand-plus/algebra/20-group-theory-and-generalizations/part-01/cauchys-theorem-group-theory.md)
- [Characteristic p](../../field-theory/characteristic-p.md)
- [Congruence in $\Z$](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in.md)
- [Finitely supported function](../../../data-structures/maps/finitely-supported-function.md)
- [First isomorphism theorem](../part-01/first-isomorphism-theorem.md)
- [Index of a subgroup](../part-01/index-of-a-subgroup.md)
- [Ordered ring](../../rings/ordered-ring.md)
- [Quotient space](../../../../undergraduate/group-theory/basic-definitions/quotient-space.md)
- [Schroeder-Bernstein Theorem](../../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [The Fundamental Theorem of Arithmetic](../../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Sources

- [Mathlib documentation: `Sylow.isPretransitive_of_finite`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.isPretransitive_of_finite)
- [Source of `Sylow.isPretransitive_of_finite` in Mathlib/GroupTheory/Sylow.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Sylow.lean#L345)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L61)
