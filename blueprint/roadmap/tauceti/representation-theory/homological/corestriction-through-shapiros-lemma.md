---
declaration: theorem
origin: cited
lean: TauCeti.groupCohomology.coindIso_hom_comp_corestriction, TauCeti.groupHomology.indIso_inv_comp_map_counit, TauCeti.groupHomology.indIso_inv_comp_map_counit_assoc
statement: formalized
proof: formalized
---

# Corestriction through Shapiro's lemma

Precomposed with Shapiro's isomorphism
`Hⁿ(G, Coind_S^G Res_S A) ≅ Hⁿ(S, Res_S A)`, corestriction is the map induced by the trace
`Coind_S^G Res_S A ⟶ A`, the counit of `Rep.coindResAdjunction`.

```lean
TauCeti.groupCohomology.coindIso_hom_comp_corestriction.{u} {k G : Type u} [CommRing k] [Group G]
  (S : Subgroup G) [S.FiniteIndex] (A : Rep.{u, u, u} k G) (n : ℕ) :
  CategoryTheory.CategoryStruct.comp (groupCohomology.coindIso (Rep.res S.subtype A) n).hom
      (TauCeti.groupCohomology.corestriction S A n) =
    groupCohomology.map (MonoidHom.id G) ((Rep.coindResAdjunction k S).counit.app A) n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse of Shapiro's isomorphism in homology is corestriction of the unit](the-inverse-of-shapiros-isomorphism-in-homology.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.groupCohomology.coindIso_hom_comp_corestriction`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/Corestriction.html#TauCeti.groupCohomology.coindIso_hom_comp_corestriction).

## Other forms

**Corestriction through Shapiro's lemma.** Formalized in Tau Ceti as [`TauCeti.groupHomology.indIso_inv_comp_map_counit`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupHomology/Shapiro.html#TauCeti.groupHomology.indIso_inv_comp_map_counit).

```lean
TauCeti.groupHomology.indIso_inv_comp_map_counit.{u} {k G : Type u} [CommRing k] [Group G]
  [DecidableEq G] (S : Subgroup G) (B : Rep.{u, u, u} k G) (n : ℕ) :
  CategoryTheory.CategoryStruct.comp (groupHomology.indIso S (Rep.res S.subtype B) n).inv
      (groupHomology.map (MonoidHom.id G) ((Rep.indResAdjunction k S.subtype).counit.app B) n) =
    groupHomology.map S.subtype (CategoryTheory.CategoryStruct.id (Rep.res S.subtype B)) n
```

**Corestriction through Shapiro's lemma.** Formalized in Tau Ceti as [`TauCeti.groupHomology.indIso_inv_comp_map_counit_assoc`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupHomology/Shapiro.html#TauCeti.groupHomology.indIso_inv_comp_map_counit_assoc).

```lean
TauCeti.groupHomology.indIso_inv_comp_map_counit_assoc.{u} {k G : Type u} [CommRing k] [Group G]
  [DecidableEq G] (S : Subgroup G) (B : Rep.{u, u, u} k G) (n : ℕ) {Z : ModuleCat k}
  (h : groupHomology B n ⟶ Z) :
  CategoryTheory.CategoryStruct.comp (groupHomology.indIso S (Rep.res S.subtype B) n).inv
      (CategoryTheory.CategoryStruct.comp
        (groupHomology.map (MonoidHom.id G) ((Rep.indResAdjunction k S.subtype).counit.app B) n)
        h) =
    CategoryTheory.CategoryStruct.comp
      (groupHomology.map S.subtype (CategoryTheory.CategoryStruct.id (Rep.res S.subtype B)) n) h
```

## Sources

- [Tau Ceti documentation: `TauCeti.groupCohomology.coindIso_hom_comp_corestriction`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/Corestriction.html#TauCeti.groupCohomology.coindIso_hom_comp_corestriction)
- [Source of `TauCeti.groupCohomology.coindIso_hom_comp_corestriction` in TauCeti/RepresentationTheory/Homological/GroupCohomology/Corestriction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/GroupCohomology/Corestriction.lean#L146)
