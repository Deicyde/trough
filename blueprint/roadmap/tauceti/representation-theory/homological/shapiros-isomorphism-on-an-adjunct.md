---
declaration: theorem
origin: cited
lean: TauCeti.groupCohomology.map_resCoindToHom_comp_coindIso_hom
statement: formalized
proof: formalized
---

# Shapiro's isomorphism on an adjunct

For a `G`-representation `B` and a morphism
`f : Res_S B ⟶ A`, the map induced by the adjunct `B ⟶ Coind_S^G A` of `f`, followed by Shapiro's
isomorphism, is the change-of-group map `Hⁿ(G, B) ⟶ Hⁿ(S, A)` induced by `f` along `S ≤ G`.

```lean
TauCeti.groupCohomology.map_resCoindToHom_comp_coindIso_hom.{u} {k G : Type u} [CommRing k]
  [Group G] (S : Subgroup G) (A : Rep.{u, u, u} k ↥S) {B : Rep.{u, u, u} k G}
  (f : Rep.res S.subtype B ⟶ A) (n : ℕ) :
  CategoryTheory.CategoryStruct.comp
      (groupCohomology.map (MonoidHom.id G) (Rep.resCoindToHom S.subtype B A f) n)
      (groupCohomology.coindIso A n).hom =
    groupCohomology.map S.subtype f n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.groupCohomology.map_resCoindToHom_comp_coindIso_hom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/Shapiro.html#TauCeti.groupCohomology.map_resCoindToHom_comp_coindIso_hom).

## Sources

- [Tau Ceti documentation: `TauCeti.groupCohomology.map_resCoindToHom_comp_coindIso_hom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/Shapiro.html#TauCeti.groupCohomology.map_resCoindToHom_comp_coindIso_hom)
- [Source of `TauCeti.groupCohomology.map_resCoindToHom_comp_coindIso_hom` in TauCeti/RepresentationTheory/Homological/GroupCohomology/Shapiro.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/GroupCohomology/Shapiro.lean#L136)
