---
declaration: abbrev
origin: cited
lean: TauCeti.Huber.NoetherianCech.completedTerm
statement: formalized
---

# TauCeti.Huber.NoetherianCech.completedTerm

The separated completion of the degree-`p` term of the rational-localization Čech complex,
for the product of the natural module topologies on its faces.

```lean
TauCeti.Huber.NoetherianCech.completedTerm.{u_1, u_2, u_3} {B : Type u_1} [CommRing B]
  [TopologicalSpace B] [IsTopologicalRing B] {ι : Type u_2} (f : ι → B)
  (P : TauCeti.Huber.PairOfDefinition B) (M : Type u_3) [AddCommGroup M] [_root_.Module B M]
  (hf : Ideal.span (Set.range f) = ⊤) (p : ℕ) : Type (max (max u_2 u_3) u_1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.NoetherianCech.completedTerm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/NoetherianCech/Completion.html#TauCeti.Huber.NoetherianCech.completedTerm).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.NoetherianCech.completedTerm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/NoetherianCech/Completion.html#TauCeti.Huber.NoetherianCech.completedTerm)
- [Source of `TauCeti.Huber.NoetherianCech.completedTerm` in TauCeti/RingTheory/Huber/NoetherianCech/Completion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Huber/NoetherianCech/Completion.lean#L44)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
