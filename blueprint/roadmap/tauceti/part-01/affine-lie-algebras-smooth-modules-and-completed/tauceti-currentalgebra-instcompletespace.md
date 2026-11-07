---
declaration: theorem
origin: cited
lean: TauCeti.CurrentAlgebra.instCompleteSpace
statement: formalized
proof: formalized
---

# TauCeti.CurrentAlgebra.instCompleteSpace

The order topology is complete over a finite free coefficient module.

```lean
TauCeti.CurrentAlgebra.instCompleteSpace.{u_1, u_2} (R : Type u_1) (L : Type u_2) [CommRing R]
  [AddCommGroup L] [_root_.Module R L] [Module.Free R L] [Module.Finite R L] :
  CompleteSpace (TauCeti.currentAlgebra R L)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CurrentAlgebra.instCompleteSpace`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/Topology.html#TauCeti.CurrentAlgebra.instCompleteSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.CurrentAlgebra.instCompleteSpace`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/Topology.html#TauCeti.CurrentAlgebra.instCompleteSpace)
- [Source of `TauCeti.CurrentAlgebra.instCompleteSpace` in TauCeti/Algebra/Lie/Current/Topology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Current/Topology.lean#L187)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
