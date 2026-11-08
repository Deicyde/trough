---
declaration: theorem
origin: cited
lean: TauCeti.groupCohomology.map_resCoindToHom_comp_coindIso_hom, TauCeti.groupHomology.δ_comp_indIso_inv, TauCeti.groupHomology.δ_comp_indIso_inv_assoc, TauCeti.groupCohomology.coindIso_hom_naturality, TauCeti.groupCohomology.coindIso_hom_naturality_assoc, TauCeti.groupHomology.indIso_hom_naturality, TauCeti.groupHomology.indIso_hom_naturality_assoc, TauCeti.groupCohomology.coindIso_hom
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

## Proof depends on

- [The inverse of Shapiro's isomorphism is natural in the coefficients](the-inverse-of-shapiros-isomorphism-is-natural-i.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.groupCohomology.map_resCoindToHom_comp_coindIso_hom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/Shapiro.html#TauCeti.groupCohomology.map_resCoindToHom_comp_coindIso_hom).

## Other forms

**Shapiro's isomorphism commutes with the connecting maps.** Formalized in Tau Ceti as [`TauCeti.groupHomology.δ_comp_indIso_inv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupHomology/Transfer/Delta.html#TauCeti.groupHomology.%CE%B4_comp_indIso_inv).

```lean
TauCeti.groupHomology.δ_comp_indIso_inv.{u} {R G : Type u} [CommRing R] [Group G] (S : Subgroup G)
  [DecidableEq G] {Y : CategoryTheory.ShortComplex (Rep.{u, u, u} R ↥S)} (hY : Y.ShortExact)
  (hIY : (Y.map (Rep.indFunctor R S.subtype)).ShortExact) (i j : ℕ) (hij : j + 1 = i) :
  CategoryTheory.CategoryStruct.comp (groupHomology.δ hY i j hij)
      (groupHomology.indIso S Y.X₁ j).inv =
    CategoryTheory.CategoryStruct.comp (groupHomology.indIso S Y.X₃ i).inv
      (groupHomology.δ hIY i j hij)
```

**Shapiro's isomorphism commutes with the connecting maps.** Formalized in Tau Ceti as [`TauCeti.groupHomology.δ_comp_indIso_inv_assoc`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupHomology/Transfer/Delta.html#TauCeti.groupHomology.%CE%B4_comp_indIso_inv_assoc).

```lean
TauCeti.groupHomology.δ_comp_indIso_inv_assoc.{u} {R G : Type u} [CommRing R] [Group G]
  (S : Subgroup G) [DecidableEq G] {Y : CategoryTheory.ShortComplex (Rep.{u, u, u} R ↥S)}
  (hY : Y.ShortExact) (hIY : (Y.map (Rep.indFunctor R S.subtype)).ShortExact) (i j : ℕ)
  (hij : j + 1 = i) {Z : ModuleCat R} (h : groupHomology (Rep.ind S.subtype Y.X₁) j ⟶ Z) :
  CategoryTheory.CategoryStruct.comp (groupHomology.δ hY i j hij)
      (CategoryTheory.CategoryStruct.comp (groupHomology.indIso S Y.X₁ j).inv h) =
    CategoryTheory.CategoryStruct.comp (groupHomology.indIso S Y.X₃ i).inv
      (CategoryTheory.CategoryStruct.comp (groupHomology.δ hIY i j hij) h)
```

**Shapiro's isomorphism is natural in the coefficients.** Formalized in Tau Ceti as [`TauCeti.groupCohomology.coindIso_hom_naturality`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/Shapiro.html#TauCeti.groupCohomology.coindIso_hom_naturality).

```lean
TauCeti.groupCohomology.coindIso_hom_naturality.{u} {k G : Type u} [CommRing k] [Group G]
  (S : Subgroup G) (A : Rep.{u, u, u} k ↥S) {B : Rep.{u, u, u} k ↥S} (φ : A ⟶ B) (n : ℕ) :
  CategoryTheory.CategoryStruct.comp
      (groupCohomology.map (MonoidHom.id G) ((Rep.coindFunctor k S.subtype).map φ) n)
      (groupCohomology.coindIso B n).hom =
    CategoryTheory.CategoryStruct.comp (groupCohomology.coindIso A n).hom
      (groupCohomology.map (MonoidHom.id ↥S) φ n)
```

**Shapiro's isomorphism is natural in the coefficients.** Formalized in Tau Ceti as [`TauCeti.groupCohomology.coindIso_hom_naturality_assoc`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/Shapiro.html#TauCeti.groupCohomology.coindIso_hom_naturality_assoc).

```lean
TauCeti.groupCohomology.coindIso_hom_naturality_assoc.{u} {k G : Type u} [CommRing k] [Group G]
  (S : Subgroup G) (A : Rep.{u, u, u} k ↥S) {B : Rep.{u, u, u} k ↥S} (φ : A ⟶ B) (n : ℕ)
  {Z : ModuleCat k} (h : groupCohomology B n ⟶ Z) :
  CategoryTheory.CategoryStruct.comp
      (groupCohomology.map (MonoidHom.id G) ((Rep.coindFunctor k S.subtype).map φ) n)
      (CategoryTheory.CategoryStruct.comp (groupCohomology.coindIso B n).hom h) =
    CategoryTheory.CategoryStruct.comp (groupCohomology.coindIso A n).hom
      (CategoryTheory.CategoryStruct.comp (groupCohomology.map (MonoidHom.id ↥S) φ n) h)
```

**Shapiro's isomorphism is natural in the coefficients.** Formalized in Tau Ceti as [`TauCeti.groupHomology.indIso_hom_naturality`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupHomology/Shapiro.html#TauCeti.groupHomology.indIso_hom_naturality).

```lean
TauCeti.groupHomology.indIso_hom_naturality.{u} {k G : Type u} [CommRing k] [Group G]
  [DecidableEq G] (S : Subgroup G) (A : Rep.{u, u, u} k ↥S) {B : Rep.{u, u, u} k ↥S} (φ : A ⟶ B)
  (n : ℕ) :
  CategoryTheory.CategoryStruct.comp
      (groupHomology.map (MonoidHom.id G) ((Rep.indFunctor k S.subtype).map φ) n)
      (groupHomology.indIso S B n).hom =
    CategoryTheory.CategoryStruct.comp (groupHomology.indIso S A n).hom
      (groupHomology.map (MonoidHom.id ↥S) φ n)
```

**Shapiro's isomorphism is natural in the coefficients.** Formalized in Tau Ceti as [`TauCeti.groupHomology.indIso_hom_naturality_assoc`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupHomology/Shapiro.html#TauCeti.groupHomology.indIso_hom_naturality_assoc).

```lean
TauCeti.groupHomology.indIso_hom_naturality_assoc.{u} {k G : Type u} [CommRing k] [Group G]
  [DecidableEq G] (S : Subgroup G) (A : Rep.{u, u, u} k ↥S) {B : Rep.{u, u, u} k ↥S} (φ : A ⟶ B)
  (n : ℕ) {Z : ModuleCat k} (h : groupHomology B n ⟶ Z) :
  CategoryTheory.CategoryStruct.comp
      (groupHomology.map (MonoidHom.id G) ((Rep.indFunctor k S.subtype).map φ) n)
      (CategoryTheory.CategoryStruct.comp (groupHomology.indIso S B n).hom h) =
    CategoryTheory.CategoryStruct.comp (groupHomology.indIso S A n).hom
      (CategoryTheory.CategoryStruct.comp (groupHomology.map (MonoidHom.id ↥S) φ n) h)
```

**Shapiro's isomorphism is restriction followed by evaluation at `1`.** Formalized in Tau Ceti as [`TauCeti.groupCohomology.coindIso_hom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/Shapiro.html#TauCeti.groupCohomology.coindIso_hom).

```lean
TauCeti.groupCohomology.coindIso_hom.{u} {k G : Type u} [CommRing k] [Group G] (S : Subgroup G)
  (A : Rep.{u, u, u} k ↥S) (n : ℕ) :
  (groupCohomology.coindIso A n).hom =
    groupCohomology.map S.subtype ((Rep.resCoindAdjunction k S.subtype).counit.app A) n
```

## Sources

- [Tau Ceti documentation: `TauCeti.groupCohomology.map_resCoindToHom_comp_coindIso_hom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/Shapiro.html#TauCeti.groupCohomology.map_resCoindToHom_comp_coindIso_hom)
- [Source of `TauCeti.groupCohomology.map_resCoindToHom_comp_coindIso_hom` in TauCeti/RepresentationTheory/Homological/GroupCohomology/Shapiro.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/GroupCohomology/Shapiro.lean#L136)
