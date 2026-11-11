---
declaration: instance
origin: cited
lean: TauCeti.PointTopology.instTopologicalSpaceWithConv
statement: formalized
---

# TauCeti.PointTopology.instTopologicalSpaceWithConv

The point topology on the convolution type `WithConv (A →ₐ[k] R)`, which carries the group of
points of an affine group scheme: the topology transported from `A →ₐ[k] R` along
`WithConv.ofConv`.

```lean
TauCeti.PointTopology.instTopologicalSpaceWithConv.{u_1, u_2, u_3} {k : Type u_1} {A : Type u_2}
  {R : Type u_3} [CommSemiring k] [Semiring A] [Algebra k A] [Semiring R] [Algebra k R]
  [TopologicalSpace R] : TopologicalSpace (WithConv (A →ₐ[k] R))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PointTopology.instTopologicalSpaceWithConv`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/PointTopology/Basic.html#TauCeti.PointTopology.instTopologicalSpaceWithConv).

## Sources

- [Tau Ceti documentation: `TauCeti.PointTopology.instTopologicalSpaceWithConv`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/PointTopology/Basic.html#TauCeti.PointTopology.instTopologicalSpaceWithConv)
- [Source of `TauCeti.PointTopology.instTopologicalSpaceWithConv` in TauCeti/Topology/Algebra/PointTopology/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/PointTopology/Basic.lean#L109)
- [Tau Ceti roadmap status: Reductive algebraic groups, part II — local structure and arithmetic models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReductiveGroupsPartII/STATUS.md)
