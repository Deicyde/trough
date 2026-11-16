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
- [Integer](../../general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `IsTopologicalRing`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/Ring/Basic.html#IsTopologicalRing)
- [Source of `IsTopologicalRing` in Mathlib/Topology/Algebra/Ring/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Topology/Algebra/Ring/Basic.lean#L54)
- [Mathlib overview: Topology › Topological algebra](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L254)
