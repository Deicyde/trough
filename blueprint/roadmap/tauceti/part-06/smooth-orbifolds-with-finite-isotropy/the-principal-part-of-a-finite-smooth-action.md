---
declaration: theorem
origin: cited
lean: TauCeti.dense_setOf_stabilizer_eq_ker_of_contMDiff
statement: formalized
proof: formalized
---

# The principal part of a finite smooth action

For a finite group acting by `C¹` maps on a
preconnected Hausdorff manifold without boundary, the points whose stabilizer is the kernel of the
action form a dense set. The action need not be faithful: elements acting trivially are retained
in every stabilizer, and generically they are the only ones. The set is also open, by
`TauCeti.isOpen_setOf_stabilizer_eq_ker`.

```lean
TauCeti.dense_setOf_stabilizer_eq_ker_of_contMDiff.{u_1, u_2, u_3, u_4, u_5} {𝕜 : Type u_1}
  {E : Type u_2} {H : Type u_3} {M : Type u_4} {G : Type u_5} [RCLike 𝕜] [NormedAddCommGroup E]
  [NormedSpace 𝕜 E] [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} [I.Boundaryless]
  [TopologicalSpace M] [ChartedSpace H M] [Group G] [MulAction G M] [CompleteSpace E] [Finite G]
  [T2Space M] [PreconnectedSpace M] (hsmooth : ∀ (g : G), ContMDiff I I 1 fun x => g • x) :
  Dense {x | MulAction.stabilizer G x = (MulAction.toPermHom G M).ker}
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.germKernel\_eq\_ker](tauceti-germkernel-eq-ker.md)
- [TauCeti.MulAction.germKernel](tauceti-mulaction-germkernel.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.dense_setOf_stabilizer_eq_ker_of_contMDiff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/GroupAction/GermKernel.html#TauCeti.dense_setOf_stabilizer_eq_ker_of_contMDiff).

## Sources

- [Tau Ceti documentation: `TauCeti.dense_setOf_stabilizer_eq_ker_of_contMDiff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/GroupAction/GermKernel.html#TauCeti.dense_setOf_stabilizer_eq_ker_of_contMDiff)
- [Source of `TauCeti.dense_setOf_stabilizer_eq_ker_of_contMDiff` in TauCeti/Geometry/Manifold/GroupAction/GermKernel.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/GroupAction/GermKernel.lean#L247)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Orbifolds/STATUS.md)
