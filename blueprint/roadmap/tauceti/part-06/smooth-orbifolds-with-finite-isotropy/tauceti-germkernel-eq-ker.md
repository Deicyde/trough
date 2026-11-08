---
declaration: theorem
origin: cited
lean: TauCeti.germKernel_eq_ker
statement: formalized
proof: formalized
---

# TauCeti.germKernel_eq_ker

For a group with torsion stabilizers acting by `C¹` maps on a preconnected Hausdorff manifold
without boundary, the germ kernel at every point is the kernel of the action: an element acting as
the identity near one point acts as the identity everywhere.

```lean
TauCeti.germKernel_eq_ker.{u_1, u_2, u_3, u_4, u_5} {𝕜 : Type u_1} {E : Type u_2} {H : Type u_3}
  {M : Type u_4} {G : Type u_5} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} [I.Boundaryless] [TopologicalSpace M]
  [ChartedSpace H M] [Group G] [MulAction G M] [CompleteSpace E] [T2Space M] [PreconnectedSpace M]
  (hsmooth : ∀ (g : G), ContMDiff I I 1 fun x => g • x)
  (hG : ∀ (x : M), IsMulTorsion ↥(MulAction.stabilizer G x)) (x : M) :
  TauCeti.MulAction.germKernel G x = (MulAction.toPermHom G M).ker
```

## Depends on

- [TauCeti.MulAction.germKernel](tauceti-mulaction-germkernel.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.germKernel_eq_ker`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/GroupAction/GermKernel.html#TauCeti.germKernel_eq_ker).

## Sources

- [Tau Ceti documentation: `TauCeti.germKernel_eq_ker`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/GroupAction/GermKernel.html#TauCeti.germKernel_eq_ker)
- [Source of `TauCeti.germKernel_eq_ker` in TauCeti/Geometry/Manifold/GroupAction/GermKernel.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/GroupAction/GermKernel.lean#L224)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Orbifolds/STATUS.md)
