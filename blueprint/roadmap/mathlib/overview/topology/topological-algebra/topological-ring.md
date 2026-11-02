---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: IsTopologicalRing
mathlib_file: Mathlib/Topology/Algebra/Ring/Basic.lean
---

# Topological ring

A topological ring is a ring `R` where addition, multiplication and negation are continuous.

If `R` is a (unital) ring, then continuity of negation can be derived from continuity of
multiplication as it is multiplication with `-1`. (See `IsTopologicalSemiring.continuousNeg_of_mul`
and `IsTopologicalSemiring.toIsTopologicalRing`)

```lean
IsTopologicalRing.{u_1} (R : Type u_1) [TopologicalSpace R] [NonUnitalNonAssocRing R] : Prop
```

## Depends on

- [Continuous function](../general-topology/part-01/continuous-function.md)
- [Induced topology](../general-topology/part-01/induced-topology.md)
- [Integer](../../general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `IsTopologicalRing`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/Ring/Basic.html#IsTopologicalRing)
- [Source of `IsTopologicalRing` in Mathlib/Topology/Algebra/Ring/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Algebra/Ring/Basic.lean#L55)
- [Mathlib overview: Topology › Topological algebra](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L254)
