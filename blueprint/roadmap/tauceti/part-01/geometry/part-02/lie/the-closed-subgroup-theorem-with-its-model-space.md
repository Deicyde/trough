---
declaration: theorem
origin: cited
lean: TauCeti.Lie.nonempty_embeddedLieSubgroupData_lieSubalgebraOfSubgroup_of_isClosed
statement: formalized
proof: formalized
---

# The closed-subgroup theorem, with its model space

A closed subgroup of a
finite-dimensional real Lie group carries embedded-Lie-subgroup data whose model vector space is
the Lie algebra `TauCeti.Lie.lieSubalgebraOfSubgroup` of the subgroup.

```lean
TauCeti.Lie.nonempty_embeddedLieSubgroupData_lieSubalgebraOfSubgroup_of_isClosed.{u, v, w}
  {E : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type v} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {G : Type w} [TopologicalSpace G] [ChartedSpace H G] [Group G]
  [FiniteDimensional ℝ E] [LieGroup I (↑⊤) G] {K : Subgroup G} (hK : IsClosed ↑K) :
  have x := ⋯;
  Nonempty
    (TauCeti.Lie.EmbeddedLieSubgroupData I K ↥(TauCeti.Lie.lieSubalgebraOfSubgroup K).toSubmodule)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hadamard's identity in the algebra of smooth functions](../manifold/part-02/hadamards-identity-in-the-algebra-of-smooth-func.md)
- [Hadamard's lemma](../manifold/part-02/hadamards-lemma.md)
- [The inverse function theorem for manifolds](../manifold/part-02/the-inverse-function-theorem-for-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Lie.nonempty_embeddedLieSubgroupData_lieSubalgebraOfSubgroup_of_isClosed`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/Subgroup/Embedded.html#TauCeti.Lie.nonempty_embeddedLieSubgroupData_lieSubalgebraOfSubgroup_of_isClosed).

## Sources

- [Tau Ceti documentation: `TauCeti.Lie.nonempty_embeddedLieSubgroupData_lieSubalgebraOfSubgroup_of_isClosed`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/Subgroup/Embedded.html#TauCeti.Lie.nonempty_embeddedLieSubgroupData_lieSubalgebraOfSubgroup_of_isClosed)
- [Source of `TauCeti.Lie.nonempty_embeddedLieSubgroupData_lieSubalgebraOfSubgroup_of_isClosed` in TauCeti/Geometry/Lie/Subgroup/Embedded.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Lie/Subgroup/Embedded.lean#L152)
