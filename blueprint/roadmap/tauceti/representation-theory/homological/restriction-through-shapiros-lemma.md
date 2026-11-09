---
declaration: theorem
origin: cited
lean: TauCeti.groupCohomology.map_unit_comp_coindIso_hom
statement: formalized
proof: formalized
---

# Restriction through Shapiro's lemma

For a `G`-representation `B`, the map induced by the
unit `B ⟶ Coind_S^G Res_S B` of restriction–coinduction, followed by Shapiro's isomorphism, is
restriction `Hⁿ(G, B) ⟶ Hⁿ(S, Res_S B)`.

```lean
TauCeti.groupCohomology.map_unit_comp_coindIso_hom.{u} {k G : Type u} [CommRing k] [Group G]
  (S : Subgroup G) (B : Rep.{u, u, u} k G) (n : ℕ) :
  CategoryTheory.CategoryStruct.comp
      (groupCohomology.map (MonoidHom.id G) ((Rep.resCoindAdjunction k S.subtype).unit.app B) n)
      (groupCohomology.coindIso (Rep.res S.subtype B) n).hom =
    groupCohomology.map S.subtype (CategoryTheory.CategoryStruct.id (Rep.res S.subtype B)) n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.groupCohomology.map_unit_comp_coindIso_hom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/Shapiro.html#TauCeti.groupCohomology.map_unit_comp_coindIso_hom).

## Sources

- [Tau Ceti documentation: `TauCeti.groupCohomology.map_unit_comp_coindIso_hom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/Shapiro.html#TauCeti.groupCohomology.map_unit_comp_coindIso_hom)
- [Source of `TauCeti.groupCohomology.map_unit_comp_coindIso_hom` in TauCeti/RepresentationTheory/Homological/GroupCohomology/Shapiro.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/GroupCohomology/Shapiro.lean#L149)
