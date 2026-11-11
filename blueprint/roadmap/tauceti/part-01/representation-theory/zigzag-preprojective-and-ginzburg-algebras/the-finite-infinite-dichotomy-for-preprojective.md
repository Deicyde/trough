---
declaration: theorem
origin: cited
lean: TauCeti.finiteDimensional_preprojectiveAlgebra_orientedQuiver_iff
statement: formalized
proof: formalized
---

# The finite/infinite dichotomy for preprojective algebras of oriented graphs

for a
connected finite simple graph `G` and any orientation `o` of `G`, the preprojective algebra
`Π_k(OrientedQuiver G o)` is finite-dimensional over `k` if and only if `G` is isomorphic to the
diagram of a valid Dynkin type.

```lean
TauCeti.finiteDimensional_preprojectiveAlgebra_orientedQuiver_iff.{u_1, u_2} (k : Type u_1)
  [Field k] {V : Type u_2} [Finite V] {G : SimpleGraph V} (hG : G.Connected)
  (o : TauCeti.DoubledQuiver.Orientation G) :
  FiniteDimensional k (TauCeti.preprojectiveAlgebra k (TauCeti.DoubledQuiver.OrientedQuiver G o)) ↔
    ∃ t, t.Valid ∧ Nonempty (G ≃g TauCeti.diagramGraph t.cartanMatrix)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.finiteDimensional_preprojectiveAlgebra_orientedQuiver_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Preprojective/ADE/FiniteDimensional.html#TauCeti.finiteDimensional_preprojectiveAlgebra_orientedQuiver_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.finiteDimensional_preprojectiveAlgebra_orientedQuiver_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Preprojective/ADE/FiniteDimensional.html#TauCeti.finiteDimensional_preprojectiveAlgebra_orientedQuiver_iff)
- [Source of `TauCeti.finiteDimensional_preprojectiveAlgebra_orientedQuiver_iff` in TauCeti/RepresentationTheory/Quiver/Preprojective/ADE/FiniteDimensional.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Quiver/Preprojective/ADE/FiniteDimensional.lean#L106)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
