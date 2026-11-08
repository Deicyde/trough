---
declaration: theorem
origin: cited
lean: TauCeti.groupHomology.indIso_inv_naturality, TauCeti.groupHomology.indIso_inv, TauCeti.groupHomology.indIso_inv_naturality_assoc
statement: formalized
proof: formalized
---

# The inverse of Shapiro's isomorphism is natural in the coefficients

for a morphism
`φ : A ⟶ B` of `S`-representations, it intertwines the maps induced by `φ` and by `Ind_S^G φ`.

```lean
TauCeti.groupHomology.indIso_inv_naturality.{u} {k G : Type u} [CommRing k] [Group G]
  [DecidableEq G] (S : Subgroup G) (A : Rep.{u, u, u} k ↥S) {B : Rep.{u, u, u} k ↥S} (φ : A ⟶ B)
  (n : ℕ) :
  CategoryTheory.CategoryStruct.comp (groupHomology.map (MonoidHom.id ↥S) φ n)
      (groupHomology.indIso S B n).inv =
    CategoryTheory.CategoryStruct.comp (groupHomology.indIso S A n).inv
      (groupHomology.map (MonoidHom.id G) ((Rep.indFunctor k S.subtype).map φ) n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.groupHomology.indIso_inv_naturality`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupHomology/Shapiro.html#TauCeti.groupHomology.indIso_inv_naturality).

## Other forms

**The inverse of Shapiro's isomorphism in homology is corestriction of the unit.** Formalized in Tau Ceti as [`TauCeti.groupHomology.indIso_inv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupHomology/Shapiro.html#TauCeti.groupHomology.indIso_inv).

```lean
TauCeti.groupHomology.indIso_inv.{u} {k G : Type u} [CommRing k] [Group G] [DecidableEq G]
  (S : Subgroup G) (A : Rep.{u, u, u} k ↥S) (n : ℕ) :
  (groupHomology.indIso S A n).inv =
    groupHomology.map S.subtype ((Rep.indResAdjunction k S.subtype).unit.app A) n
```

**The inverse of Shapiro's isomorphism is natural in the coefficients.** Formalized in Tau Ceti as [`TauCeti.groupHomology.indIso_inv_naturality_assoc`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupHomology/Shapiro.html#TauCeti.groupHomology.indIso_inv_naturality_assoc).

```lean
TauCeti.groupHomology.indIso_inv_naturality_assoc.{u} {k G : Type u} [CommRing k] [Group G]
  [DecidableEq G] (S : Subgroup G) (A : Rep.{u, u, u} k ↥S) {B : Rep.{u, u, u} k ↥S} (φ : A ⟶ B)
  (n : ℕ) {Z : ModuleCat k} (h : groupHomology (Rep.ind S.subtype B) n ⟶ Z) :
  CategoryTheory.CategoryStruct.comp (groupHomology.map (MonoidHom.id ↥S) φ n)
      (CategoryTheory.CategoryStruct.comp (groupHomology.indIso S B n).inv h) =
    CategoryTheory.CategoryStruct.comp (groupHomology.indIso S A n).inv
      (CategoryTheory.CategoryStruct.comp
        (groupHomology.map (MonoidHom.id G) ((Rep.indFunctor k S.subtype).map φ) n) h)
```

## Sources

- [Tau Ceti documentation: `TauCeti.groupHomology.indIso_inv_naturality`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupHomology/Shapiro.html#TauCeti.groupHomology.indIso_inv_naturality)
- [Source of `TauCeti.groupHomology.indIso_inv_naturality` in TauCeti/RepresentationTheory/Homological/GroupHomology/Shapiro.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/GroupHomology/Shapiro.lean#L151)
