---
declaration: structure
origin: cited
lean: TauCeti.Huber.IsCompletedPushout
statement: formalized
---

# TauCeti.Huber.IsCompletedPushout

A commuting square of Huber pairs is a *completed pushout* if compatible morphisms into
any complete Hausdorff Huber pair factor uniquely through its bottom-right vertex.
Completeness of the vertices is not part of this predicate.

```lean
TauCeti.Huber.IsCompletedPushout.{u} {A B C E : Type u} [CommRing A] [TopologicalSpace A]
  [IsTopologicalRing A] [TauCeti.Huber.IsHuberRing A] [CommRing B] [TopologicalSpace B]
  [IsTopologicalRing B] [TauCeti.Huber.IsHuberRing B] [CommRing C] [TopologicalSpace C]
  [IsTopologicalRing C] [TauCeti.Huber.IsHuberRing C] [CommRing E] [TopologicalSpace E]
  [IsTopologicalRing E] [TauCeti.Huber.IsHuberRing E] {S : TauCeti.Huber.Pair A}
  {T : TauCeti.Huber.Pair B} {U : TauCeti.Huber.Pair C} {W : TauCeti.Huber.Pair E} (f : S.Hom T)
  (g : S.Hom U) (i : T.Hom W) (j : U.Hom W) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.IsCompletedPushout`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/TensorProduct/Pushout.html#TauCeti.Huber.IsCompletedPushout).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.IsCompletedPushout`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/TensorProduct/Pushout.html#TauCeti.Huber.IsCompletedPushout)
- [Source of `TauCeti.Huber.IsCompletedPushout` in TauCeti/RingTheory/Huber/TensorProduct/Pushout.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Huber/TensorProduct/Pushout.lean#L47)
- [Tau Ceti roadmap status: Analytic adic geometry for diamonds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicEtaleGeometry/STATUS.md)
