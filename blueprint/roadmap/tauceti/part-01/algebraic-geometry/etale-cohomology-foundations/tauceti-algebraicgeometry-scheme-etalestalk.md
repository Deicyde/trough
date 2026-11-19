---
declaration: abbrev
origin: cited
lean: TauCeti.AlgebraicGeometry.Scheme.etaleStalk
statement: formalized
---

# TauCeti.AlgebraicGeometry.Scheme.etaleStalk

The stalk at the geometric point `s : Spec Ω ⟶ S` of an étale sheaf of `Λ`-modules, as a
`Λ`-module: the fibre functor of the point `pointSmallEtale s` of the small étale site.

```lean
TauCeti.AlgebraicGeometry.Scheme.etaleStalk.{u} {S : AlgebraicGeometry.Scheme} (Λ : Type u) [Ring Λ]
  {Ω : Type u} [Field Ω] [IsSepClosed Ω] (s : AlgebraicGeometry.Spec ↧Ω ⟶ S) :
  CategoryTheory.Functor (CategoryTheory.Sheaf S.smallEtaleTopology (ModuleCat Λ)) (ModuleCat Λ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.Scheme.etaleStalk`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Sites/Etale/ModuleSheaf.html#TauCeti.AlgebraicGeometry.Scheme.etaleStalk).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.Scheme.etaleStalk`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Sites/Etale/ModuleSheaf.html#TauCeti.AlgebraicGeometry.Scheme.etaleStalk)
- [Source of `TauCeti.AlgebraicGeometry.Scheme.etaleStalk` in TauCeti/AlgebraicGeometry/Sites/Etale/ModuleSheaf.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Sites/Etale/ModuleSheaf.lean#L77)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
