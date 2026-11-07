---
declaration: theorem
origin: cited
lean: TauCeti.dense_setOf_stabilizer_eq_ker
statement: formalized
proof: formalized
---

# Generic stabilizer of a finite linear action

For a finite group acting linearly and
continuously on a Hausdorff topological module over a ring in which `0` is a limit of units, for
instance a finite-dimensional real vector space, the points whose stabilizer is the kernel of the
action form a dense set. The action need not be faithful. The set is also open, by
`TauCeti.isOpen_setOf_stabilizer_eq_ker`.

```lean
TauCeti.dense_setOf_stabilizer_eq_ker.{u_1, u_3, u_4} {G : Type u_1} [Group G] (R : Type u_3)
  {V : Type u_4} [Ring R] [TopologicalSpace R] [(nhdsWithin 0 {r | IsUnit r}).NeBot]
  [AddCommGroup V] [_root_.Module R V] [TopologicalSpace V] [ContinuousAdd V] [ContinuousSMul R V]
  [DistribMulAction G V] [SMulCommClass G R V] [T2Space V] [ContinuousConstSMul G V] [Finite G] :
  Dense {v | MulAction.stabilizer G v = (MulAction.toPermHom G V).ker}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.dense_setOf_stabilizer_eq_ker`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/GroupAction/GenericStabilizer.html#TauCeti.dense_setOf_stabilizer_eq_ker).

## Sources

- [Tau Ceti documentation: `TauCeti.dense_setOf_stabilizer_eq_ker`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/GroupAction/GenericStabilizer.html#TauCeti.dense_setOf_stabilizer_eq_ker)
- [Source of `TauCeti.dense_setOf_stabilizer_eq_ker` in TauCeti/Topology/Algebra/GroupAction/GenericStabilizer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/GroupAction/GenericStabilizer.lean#L136)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Orbifolds/STATUS.md)
