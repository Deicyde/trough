---
declaration: def
origin: cited
lean: TauCeti.quotientIneffectiveKernelMulEquivAut
statement: formalized
---

# TauCeti.quotientIneffectiveKernelMulEquivAut

The isotropy group of the effective quotient of an étale groupoid at `x` is `Aut x` divided by
the ineffective kernel: effective reduction keeps exactly the effective part of the isotropy.

```lean
TauCeti.quotientIneffectiveKernelMulEquivAut.{u_1, u_2} {C : Type u_1} [CategoryTheory.Groupoid C]
  [TopologicalSpace (Quiver.Total C)] [TopologicalSpace C] [TauCeti.IsTopologicalGroupoid C]
  (hs : IsLocalHomeomorph Quiver.Total.left) (x : C) :
  CategoryTheory.Aut x ⧸ TauCeti.ineffectiveKernel hs x ≃*
    CategoryTheory.Aut ((TauCeti.toEffectiveQuotient C).obj x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.quotientIneffectiveKernelMulEquivAut`](https://taucetiproject.org/docs/TauCeti/Topology/CategoryTheory/Groupoid/Effective/Basic.html#TauCeti.quotientIneffectiveKernelMulEquivAut).

## Sources

- [Tau Ceti documentation: `TauCeti.quotientIneffectiveKernelMulEquivAut`](https://taucetiproject.org/docs/TauCeti/Topology/CategoryTheory/Groupoid/Effective/Basic.html#TauCeti.quotientIneffectiveKernelMulEquivAut)
- [Source of `TauCeti.quotientIneffectiveKernelMulEquivAut` in TauCeti/Topology/CategoryTheory/Groupoid/Effective/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/CategoryTheory/Groupoid/Effective/Basic.lean#L478)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Orbifolds/STATUS.md)
