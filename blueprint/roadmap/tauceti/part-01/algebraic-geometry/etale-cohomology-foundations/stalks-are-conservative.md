---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.Scheme.isIso_of_forall_isIso_etaleStalk
statement: formalized
proof: formalized
---

# Stalks are conservative

A morphism of étale sheaves of `Λ`-modules on `S` is an
isomorphism as soon as it induces isomorphisms on the stalks at all geometric points.

```lean
TauCeti.AlgebraicGeometry.Scheme.isIso_of_forall_isIso_etaleStalk.{u} {S : AlgebraicGeometry.Scheme}
  {Λ : Type u} [Ring Λ] {F G : CategoryTheory.Sheaf S.smallEtaleTopology (ModuleCat Λ)} (φ : F ⟶ G)
  (h :
    ∀ (Ω : Type u) [inst : Field Ω] [inst_1 : IsSepClosed Ω] (s : AlgebraicGeometry.Spec ↧Ω ⟶ S),
      CategoryTheory.IsIso ((TauCeti.AlgebraicGeometry.Scheme.etaleStalk Λ s).map φ)) :
  CategoryTheory.IsIso φ
```

## Depends on

- [TauCeti.AlgebraicGeometry.Scheme.etaleStalk](tauceti-algebraicgeometry-scheme-etalestalk.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.Scheme.isIso_of_forall_isIso_etaleStalk`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Sites/Etale/ModuleSheaf.html#TauCeti.AlgebraicGeometry.Scheme.isIso_of_forall_isIso_etaleStalk).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.Scheme.isIso_of_forall_isIso_etaleStalk`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Sites/Etale/ModuleSheaf.html#TauCeti.AlgebraicGeometry.Scheme.isIso_of_forall_isIso_etaleStalk)
- [Source of `TauCeti.AlgebraicGeometry.Scheme.isIso_of_forall_isIso_etaleStalk` in TauCeti/AlgebraicGeometry/Sites/Etale/ModuleSheaf.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Sites/Etale/ModuleSheaf.lean#L143)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
