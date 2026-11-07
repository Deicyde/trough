---
declaration: def
origin: cited
lean: TauCeti.toRelativeCWComplex
statement: formalized
---

# A classical relative CW complex in a Hausdorff space is a categorical relative CW complex

The inclusion of the base `D` into `C` is the transfinite composition of the inclusions of the
skeleta `skeletonLT C n`, and the step from `skeletonLT C n` to `skeletonLT C (n + 1)` attaches
the `n`-cells of `C` along their attaching maps.  The body is exposed so that the `n`-th space is
the skeleton `skeletonObj C n` and the cells attached at step `n` are `cell C n` by definition.

```lean
TauCeti.toRelativeCWComplex.{w} {X : Type w} [TopologicalSpace X] [T2Space X] {D : Set X}
  (C : Set X) [Topology.RelCWComplex C D] :
  TopCat.RelativeCWComplex (TopCat.ofHom (ContinuousMap.inclusion ⋯))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.toRelativeCWComplex`](https://taucetiproject.org/docs/TauCeti/Topology/CWComplex/Classical/RelativeCWComplex.html#TauCeti.toRelativeCWComplex).

## Sources

- [Tau Ceti documentation: `TauCeti.toRelativeCWComplex`](https://taucetiproject.org/docs/TauCeti/Topology/CWComplex/Classical/RelativeCWComplex.html#TauCeti.toRelativeCWComplex)
- [Source of `TauCeti.toRelativeCWComplex` in TauCeti/Topology/CWComplex/Classical/RelativeCWComplex.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/CWComplex/Classical/RelativeCWComplex.lean#L198)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
