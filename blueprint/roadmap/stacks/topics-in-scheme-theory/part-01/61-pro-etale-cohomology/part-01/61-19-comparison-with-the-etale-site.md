---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.etaleSectionsPresheaf_isSheaf, AlgebraicGeometry.Scheme.proetaleInverseImageIsoEtaleSectionsSheaf, AlgebraicGeometry.Scheme.etaleSectionsFormulaIso, AlgebraicGeometry.Scheme.proetaleInverseImageSectionsIso, AlgebraicGeometry.Scheme.isIso_unit_of_etaleToProetale, AlgebraicGeometry.Scheme.isIso_proetaleInverseImageAdjunction_unit, AlgebraicGeometry.Scheme.proetaleInverseImageEtaleSectionsIso, AlgebraicGeometry.Scheme.proetaleInverseImageFullyFaithful
statement: formalized
proof: formalized
---

# 61.19 Comparison with the étale site

Section 61.19 of the Stacks Project, [Tag 099R](https://stacks.math.columbia.edu/tag/099R). 12 tags here are carried by 25 declarations of the repository (all in StacksFrontier) and 13 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GLZ, a lemma

[Tag 0GLZ](https://stacks.math.columbia.edu/tag/0GLZ) in the Stacks Project.

**`AlgebraicGeometry.Scheme.etaleSectionsPresheaf_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullback.lean, line 920](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullback.lean#L920). The attribute's comment: “the formula is a sheaf”.

> For a sheaf `ℱ` on the small étale site of `S`, the rule
> `(f : Y → S) ↦ Γ(Y_étale, f_étale⁻¹ℱ)` is a sheaf on the small pro-étale site of `S`.

```lean
public theorem Scheme.etaleSectionsPresheaf_isSheaf (S : Scheme.{u})
    (F : Sheaf S.smallEtaleTopology (Type (max (u + 1) v))) :
    Presheaf.IsSheaf (Scheme.ProEt.topology S)
      ((Scheme.etaleSectionsPresheaf.{u, v} S).obj F)
```

**`AlgebraicGeometry.Scheme.proetaleInverseImageIsoEtaleSectionsSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullback.lean, line 965](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullback.lean#L965). The attribute's comment: “the identification with ε⁻¹”.

> The sheaf defined by the rule is the inverse image `ε⁻¹ℱ` of the morphism of sites
> `ε : S_proétale → S_étale`, through the canonical comparison of two left adjoints of `ε_*`.

```lean
public def Scheme.proetaleInverseImageIsoEtaleSectionsSheaf :
    Functor.sheafPullbackConstruction.sheafPullback S.etaleToProetale
        (Type (max (u + 1) v)) S.smallEtaleTopology (Scheme.ProEt.topology S) ≅
      Scheme.etaleSectionsSheaf.{u, v} S
```

**`AlgebraicGeometry.Scheme.etaleSectionsFormulaIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullback.lean, line 1029](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullback.lean#L1029). The attribute's comment: “the formula for sections”.

> At a pro-étale object `f : Y → S`, the sheaf defined by the rule has as its sections the
> global sections on the small étale site of `Y` of the inverse image `f_étale⁻¹ℱ`, naturally in
> the étale sheaf `ℱ`.

```lean
public def Scheme.etaleSectionsFormulaIso (S : Scheme.{u}) (Y : S.ProEt) :
    Scheme.etaleSectionsSheaf.{u, v} S ⋙
        (sheafSections (Scheme.ProEt.topology S)
          (Type (max (u + 1) v))).obj (Opposite.op Y) ≅
      Stacks.EtaleCohomology.smallEtaleInverseImage.{u, v} Y.hom ⋙
        Sheaf.Γ Y.left.smallEtaleTopology (Type (max (u + 1) v))
```

**`AlgebraicGeometry.Scheme.proetaleInverseImageSectionsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullback.lean, line 1040](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullback.lean#L1040). The attribute's comment: “the formula for sections”.

> The sections of `ε⁻¹ℱ` at a pro-étale object `f : Y → S` are the global
> sections on the small étale site of `Y` of `f_étale⁻¹ℱ`.

```lean
public def Scheme.proetaleInverseImageSectionsIso (S : Scheme.{u}) (Y : S.ProEt) :
    Functor.sheafPullbackConstruction.sheafPullback S.etaleToProetale
          (Type (max (u + 1) v)) S.smallEtaleTopology (Scheme.ProEt.topology S) ⋙
        (sheafSections (Scheme.ProEt.topology S)
          (Type (max (u + 1) v))).obj (Opposite.op Y) ≅
      Stacks.EtaleCohomology.smallEtaleInverseImage.{u, v} Y.hom ⋙
        Sheaf.Γ Y.left.smallEtaleTopology (Type (max (u + 1) v))
```

## Tag 099T, a lemma

[Tag 099T](https://stacks.math.columbia.edu/tag/099T) in the Stacks Project.

**`AlgebraicGeometry.Scheme.isIso_unit_of_etaleToProetale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackUnit.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackUnit.lean#L86). The attribute's comment: “the adjunction map ℱ ⟶ ε_*ε⁻¹ℱ is an isomorphism, for an arbitrary left adjoint ε⁻¹ of ε_*”.

> For every sheaf `ℱ` on the small étale site of a scheme `S`, the adjunction map
> `ℱ ⟶ ε_*ε⁻¹ℱ` is an isomorphism, where `ε : S_proétale → S_étale` is the morphism of sites given
> by the inclusion of the small étale category into the small pro-étale category and `ε⁻¹` is an
> arbitrary left adjoint of `ε_*`.

```lean
public theorem Scheme.isIso_unit_of_etaleToProetale
    {L : Sheaf S.smallEtaleTopology (Type (max (u + 1) v)) ⥤
      Sheaf (Scheme.ProEt.topology S) (Type (max (u + 1) v))}
    (adj : L ⊣ S.etaleToProetale.sheafPushforwardContinuous (Type (max (u + 1) v))
      S.smallEtaleTopology (Scheme.ProEt.topology S)) :
    IsIso adj.unit
```

**`AlgebraicGeometry.Scheme.isIso_proetaleInverseImageAdjunction_unit`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackUnit.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackUnit.lean#L102). The attribute's comment: “the unit of the adjunction ε⁻¹ ⊣ ε_* is an isomorphism”.

> The unit `ℱ ⟶ ε_*ε⁻¹ℱ` of the adjunction between the sheafified left Kan extension along the
> inclusion of the small étale category and restriction along it is an isomorphism.

```lean
public instance Scheme.isIso_proetaleInverseImageAdjunction_unit :
    IsIso (Functor.sheafPullbackConstruction.sheafAdjunctionContinuous S.etaleToProetale
      (Type (max (u + 1) v)) S.smallEtaleTopology (Scheme.ProEt.topology S)).unit
```

**`AlgebraicGeometry.Scheme.proetaleInverseImageEtaleSectionsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackUnit.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackUnit.lean#L110). The attribute's comment: “the sections form: ε⁻¹ℱ(U) = ℱ(U) for U in S_étale”.

> At an étale object `U` of `S` the sections of `ε⁻¹ℱ` are the sections of `ℱ`, naturally in
> `ℱ`.

```lean
public def Scheme.proetaleInverseImageEtaleSectionsIso (U : S.Etale) :
    Functor.sheafPullbackConstruction.sheafPullback S.etaleToProetale
          (Type (max (u + 1) v)) S.smallEtaleTopology (Scheme.ProEt.topology S) ⋙
        (sheafSections (Scheme.ProEt.topology S) (Type (max (u + 1) v))).obj
          (op (S.etaleToProetale.obj U)) ≅
      (sheafSections S.smallEtaleTopology (Type (max (u + 1) v))).obj (op U)
```

**`AlgebraicGeometry.Scheme.proetaleInverseImageFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackUnit.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackUnit.lean#L123). The attribute's comment: “equivalently, ε⁻¹ is fully faithful”.

> The inverse image `ε⁻¹` along the inclusion of the small étale site of `S` into its small
> pro-étale site is fully faithful.

```lean
public def Scheme.proetaleInverseImageFullyFaithful :
    (Functor.sheafPullbackConstruction.sheafPullback S.etaleToProetale
      (Type (max (u + 1) v)) S.smallEtaleTopology (Scheme.ProEt.topology S)).FullyFaithful
```

## Tag 099S, a lemma

[Tag 099S](https://stacks.math.columbia.edu/tag/099S) in the Stacks Project.

**`AlgebraicGeometry.Scheme.proetaleInverseImage_exists_map_eq_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackLimit.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackLimit.lean#L113). The attribute's comment: “the injectivity half of ε⁻¹ℱ(Y) = colim ε⁻¹ℱ(Y_i), proved: two sections over a stage that agree over the limit agree over a later stage. The surjectivity half, hence the formula itself, is not proved here. `Y = lim Y_i` is the scheme-theoretic limit, as in the source; the index category is small in the universe of the schemes”.

> **Stacks 099S, the injectivity half.** Let `Y = lim Y_i` be the limit of an inverse system of
> quasi-compact objects of `X_proétale` with affine transition morphisms, and let `ℱ` be a sheaf on
> `X_étale`.  Two sections of `ε⁻¹ℱ` over a stage `Y_i` with the same restriction to `Y` already
> have the same restriction to some later stage `Y_j`; equivalently, the canonical map
> `colim ε⁻¹ℱ(Y_i) → ε⁻¹ℱ(Y)` is injective.
>
> The sections are computed by the formula of Stacks 0GLZ through
> `AlgebraicGeometry.Scheme.proetaleInverseImageIsoEtaleSectionsSheaf`, which turns this into
> `AlgebraicGeometry.Scheme.etaleSectionsSheaf_exists_map_eq_of_isLimit`.

```lean
public theorem Scheme.proetaleInverseImage_exists_map_eq_of_isLimit
    {I : Type u} [SmallCategory I] [IsCofiltered I] (X : Scheme.{u}) (Y : I ⥤ X.ProEt)
    (c : Cone Y) (hc : IsLimit ((Scheme.ProEt.forget X ⋙ Over.forget X).mapCone c))
    (haffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom (Y.map f).left)
    (hqc : ∀ i : I, CompactSpace (Y.obj i).left)
    (F : Sheaf X.smallEtaleTopology (Type (max (u + 1) v))) (i : I)
    (s t : ((Functor.sheafPullbackConstruction.sheafPullback X.etaleToProetale
      (Type (max (u + 1) v)) X.smallEtaleTopology
      (Scheme.ProEt.topology X)).obj F).obj.obj (op (Y.obj i)))
    (hst : ((Functor.sheafPullbackConstruction.sheafPullback X.etaleToProetale
        (Type (max (u + 1) v)) X.smallEtaleTopology
        (Scheme.ProEt.topology X)).obj F).obj.map (c.π.app i).op s =
      ((Functor.sheafPullbackConstruction.sheafPullback X.etaleToProetale
        (Type (max (u + 1) v)) X.smallEtaleTopology
        (Scheme.ProEt.topology X)).obj F).obj.map (c.π.app i).op t) :
    ∃ (j : I) (f : j ⟶ i),
      ((Functor.sheafPullbackConstruction.sheafPullback X.etaleToProetale
          (Type (max (u + 1) v)) X.smallEtaleTopology
          (Scheme.ProEt.topology X)).obj F).obj.map (Y.map f).op s =
        ((Functor.sheafPullbackConstruction.sheafPullback X.etaleToProetale
          (Type (max (u + 1) v)) X.smallEtaleTopology
          (Scheme.ProEt.topology X)).obj F).obj.map (Y.map f).op t
```

**`AlgebraicGeometry.Scheme.injective_desc_proetaleInverseImage_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackLimit.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackLimit.lean#L155). The attribute's comment: “proved: the comparison map colim ε⁻¹ℱ(Y_i) → ε⁻¹ℱ(Y) of the displayed formula is INJECTIVE, for every colimit cocone of the sections at the stages. Its surjectivity is not proved, so the formula itself is not”.

> **Stacks 099S, the injectivity half, for the comparison map out of the colimit.** The
> canonical map `colim ε⁻¹ℱ(Y_i) → ε⁻¹ℱ(Y)` induced by the limit cone is injective, for any cocone
> exhibiting the colimit of the sections at the stages.
>
> Elements of a filtered colimit come from a stage and the comparison map restricts on a stage to
> restriction along the cone leg, so this is
> `AlgebraicGeometry.Scheme.proetaleInverseImage_exists_map_eq_of_isLimit` at a stage below both.

```lean
public theorem Scheme.injective_desc_proetaleInverseImage_of_isLimit
    {I : Type u} [SmallCategory I] [IsCofiltered I] (X : Scheme.{u}) (Y : I ⥤ X.ProEt)
    (c : Cone Y) (hc : IsLimit ((Scheme.ProEt.forget X ⋙ Over.forget X).mapCone c))
    (haffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom (Y.map f).left)
    (hqc : ∀ i : I, CompactSpace (Y.obj i).left)
    (F : Sheaf X.smallEtaleTopology (Type (max (u + 1) v)))
    (E : Cocone (Y.op ⋙ ((Functor.sheafPullbackConstruction.sheafPullback X.etaleToProetale
      (Type (max (u + 1) v)) X.smallEtaleTopology (Scheme.ProEt.topology X)).obj F).obj))
    (hE : IsColimit E) :
    Function.Injective (hE.desc (((Functor.sheafPullbackConstruction.sheafPullback
      X.etaleToProetale (Type (max (u + 1) v)) X.smallEtaleTopology
      (Scheme.ProEt.topology X)).obj F).obj.mapCocone c.op))
```

**`AlgebraicGeometry.Scheme.etaleSections_exists_map_eq_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackLimit.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackLimit.lean#L201). The attribute's comment: “the final statement ε⁻¹ℱ(Y) = colim ℱ(Y_i) for étale stages, injectivity half proved: two sections of ℱ over a stage with the same image in ε⁻¹ℱ(Y) agree over a later stage. Surjectivity is not proved, so the formula itself is not”.

> **Stacks 099S for étale stages, the injectivity half.** If the stages `Y_i` are objects of
> `X_étale`, two sections of `ℱ` over a stage whose images in `ε⁻¹ℱ(Y)` under the unit
> `ℱ ⟶ ε_*ε⁻¹ℱ` agree already agree over some later stage; equivalently, the canonical map
> `colim ℱ(Y_i) → ε⁻¹ℱ(Y)` is injective.
>
> The unit is an isomorphism by Stacks 099T, naturally in the étale object, which reduces this to
> `AlgebraicGeometry.Scheme.proetaleInverseImage_exists_map_eq_of_isLimit`.

```lean
public theorem Scheme.etaleSections_exists_map_eq_of_isLimit
    {I : Type u} [SmallCategory I] [IsCofiltered I] (X : Scheme.{u}) (Y : I ⥤ X.Etale)
    (c : Cone (Y ⋙ X.etaleToProetale))
    (hc : IsLimit ((Scheme.ProEt.forget X ⋙ Over.forget X).mapCone c))
    (haffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom (Y.map f).left)
    (hqc : ∀ i : I, CompactSpace (Y.obj i).left)
    (F : Sheaf X.smallEtaleTopology (Type (max (u + 1) v))) (i : I)
    (s t : F.obj.obj (op (Y.obj i)))
    (hst : ((Functor.sheafPullbackConstruction.sheafPullback X.etaleToProetale
          (Type (max (u + 1) v)) X.smallEtaleTopology
          (Scheme.ProEt.topology X)).obj F).obj.map (c.π.app i).op
        (((Functor.sheafPullbackConstruction.sheafAdjunctionContinuous X.etaleToProetale
          (Type (max (u + 1) v)) X.smallEtaleTopology
          (Scheme.ProEt.topology X)).unit.app F).hom.app (op (Y.obj i)) s) =
      ((Functor.sheafPullbackConstruction.sheafPullback X.etaleToProetale
          (Type (max (u + 1) v)) X.smallEtaleTopology
          (Scheme.ProEt.topology X)).obj F).obj.map (c.π.app i).op
        (((Functor.sheafPullbackConstruction.sheafAdjunctionContinuous X.etaleToProetale
          (Type (max (u + 1) v)) X.smallEtaleTopology
          (Scheme.ProEt.topology X)).unit.app F).hom.app (op (Y.obj i)) t)) :
    ∃ (j : I) (f : j ⟶ i), F.obj.map (Y.map f).op s = F.obj.map (Y.map f).op t
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.proetaleInverseImageIsColimit`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackColimit.lean#L464), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackRegistrations.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackRegistrations.lean#L19) (StacksFrontier): “the displayed formula ε⁻¹ℱ(Y) = colim ε⁻¹ℱ(Y_i); `Y = lim Y_i` is the limit of the underlying schemes, as in the source”.
- [`AlgebraicGeometry.Scheme.proetaleInverseImageIsColimitOfEtale`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackColimit.lean#L499), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackRegistrations.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackRegistrations.lean#L23) (StacksFrontier): “the final statement ε⁻¹ℱ(Y) = colim ℱ(Y_i) for stages Y_i in X_étale, the maps being the unit ℱ ⟶ ε_*ε⁻¹ℱ followed by restriction”.
- [`AlgebraicGeometry.Scheme.proetaleInverseImageIsColimitAddCommGrp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackAbelian.lean#L196), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackRegistrations.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProetaleEtaleSheafPullbackRegistrations.lean#L27) (StacksFrontier): “the displayed formula for abelian sheaves, for an arbitrary left adjoint ε⁻¹ of ε_*; `Y = lim Y_i` is the limit of the underlying schemes”.

## Tag 099U, a lemma

[Tag 099U](https://stacks.math.columbia.edu/tag/099U) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.ProEtale.subsingleton_sheafH_proetaleInverseImage_of_injective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/InverseImageInjective.lean#L818), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean#L34) (StacksFrontier): “pro-étale cohomology is `Ext` out of the constant sheaf `ℤ`, and `ε⁻¹` is an arbitrary left adjoint of the restriction `ε_*` to the small étale site”.

## Tag 099V, a lemma

[Tag 099V](https://stacks.math.columbia.edu/tag/099V) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.ProEtale.isIso_unit_app_and_isZero_rightDerived_epsilonDirectImage`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtale.lean#L256), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean#L38) (StacksFrontier): “part (1): `ε_* ε⁻¹ ℱ = ℱ` by the unit, and `R^q ε_*(ε⁻¹ ℱ) = 0` for `q > 0`”.
- [`AlgebraicGeometry.ProEtale.isIso_epsilonAdjunction_rightDerivedFunctorPlus_unit`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtale.lean#L248), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean#L41) (StacksFrontier): “part (2); `ε⁻¹` on `D⁺` is `ε⁻¹` applied termwise (its right derived functor), and the map is the unit of the derived adjunction”.

## Tag 099W, a lemma

[Tag 099W](https://stacks.math.columbia.edu/tag/099W) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.ProEtale.epsilonInverseImageCompFunctorHIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtale.lean#L332), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean#L45) (StacksFrontier): “part (1), naturally in the sheaf; cohomology is `Ext` out of the constant sheaf `ℤ`”.
- [`AlgebraicGeometry.ProEtale.rightDerivedFunctorPlusΓIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtale.lean#L370), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean#L49) (StacksFrontier): “part (2), naturally in `K`; `ε⁻¹` on `D⁺` is `ε⁻¹` applied termwise”.

## Tag 099X, a lemma

[Tag 099X](https://stacks.math.columbia.edu/tag/099X) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.ProEtale.bijective_torsorClassesMap`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/TorsorComparison.lean#L679), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean#L52) (StacksFrontier): “`H¹` is the set of isomorphism classes of torsors and the map is `ε⁻¹`”.

## Tag 09B1, a lemma

[Tag 09B1](https://stacks.math.columbia.edu/tag/09B1) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.isWeakSerreClass_etaleInverseImage_essImage`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ModuleComparisonWithEtale.lean#L216), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean#L70) (StacksFrontier): “part (1)”.
- [`AlgebraicGeometry.Scheme.exists_equivalence_etaleInverseImage_derivedCategoryPlus`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ModuleComparisonWithEtale.lean#L235), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean#L72) (StacksFrontier): “part (2); the equivalence has functor `ε⁻¹` applied termwise and inverse `Rε_*`”.

## Tag 099Y, a lemma

[Tag 099Y](https://stacks.math.columbia.edu/tag/099Y) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.ProEtale.isEquivalence_etaleInverseImageLocallyConstant`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/LocallyConstantComparison.lean#L618), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean#L55) (StacksFrontier).

## Tag 099Z, a lemma

[Tag 099Z](https://stacks.math.columbia.edu/tag/099Z) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.ProEtale.isEquivalence_etaleInverseImageDerivedLocallyConstant`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ModuleComparisonWithEtale.lean#L304), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/ComparisonWithEtaleRegistrations.lean#L57) (StacksFrontier).

## Tag 09B2, a lemma

[Tag 09B2](https://stacks.math.columbia.edu/tag/09B2) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.essImage_mapDerivedCategory_and_hasTorAmplitude_derivedExtendScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/AdicReductionComparison.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Cohomology/AdicReductionComparison.lean#L277).

> **Stacks 09B2.** Let `X` be a scheme, `Λ` a Noetherian ring, `I ⊆ Λ` an ideal and `K` an
> object of `D(X_proétale, Λ)`. Set `Kₙ = K ⊗_Λ^L Λ/Iⁿ`, the derived extension of scalars of `K`
> along `Λ → Λ/Iⁿ`. If `K₁` is in the essential image of `ε⁻¹ : D(X_étale, Λ/I) ⥤
> D(X_proétale, Λ/I)` and has Tor amplitude in `[a, ∞)`, then, for every `n`, `Kₙ` is in the
> essential image of `ε⁻¹ : D(X_étale, Λ/Iⁿ) ⥤ D(X_proétale, Λ/Iⁿ)` and has Tor amplitude in
> `[a, ∞)`.
>
> Here `ε⁻¹` on derived categories is `ε⁻¹` applied termwise, and Tor amplitude in `[a, ∞)` is
> `Stacks.ModuleSheaf.HasTorAmplitude` for `Set.Ici a`: `Hⁱ(L ⊗^L F) = 0` for `i < a` and every
> sheaf of modules `F`.

```lean
theorem essImage_mapDerivedCategory_and_hasTorAmplitude_derivedExtendScalars
    [IsNoetherianRing Λ]
    (K : DerivedCategory (Sheaf (Scheme.ProEt.topology X) (ModuleCat.{max (u + 1) w} Λ)))
    (a : ℤ)
    (h₁ : (Scheme.etaleInverseImage.{u, w} X (Λ ⧸ I)).mapDerivedCategory.essImage
      ((derivedExtendScalars _ (Ideal.Quotient.mk I)).obj K))
    (h₂ : HasTorAmplitude (J := Scheme.ProEt.topology X)
      ((derivedExtendScalars _ (Ideal.Quotient.mk I)).obj K) (Set.Ici a))
    (n : ℕ) :
    (Scheme.etaleInverseImage.{u, w} X (Λ ⧸ I ^ n)).mapDerivedCategory.essImage
        ((derivedExtendScalars _ (Ideal.Quotient.mk (I ^ n))).obj K) ∧
      HasTorAmplitude (J := Scheme.ProEt.topology X)
        ((derivedExtendScalars _ (Ideal.Quotient.mk (I ^ n))).obj K)
        (Set.Ici a)
```

## Tag 0F6D, an example

[Tag 0F6D](https://stacks.math.columbia.edu/tag/0F6D) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.pointFunctions_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean#L235). The attribute's comment: “`fun(-, A)` is a sheaf on the pro-étale site”.

> **The point functions form a sheaf.** The rule `U ↦ (|U| → A)` is a sheaf for the pro-étale
> topology: it is the sheaf of continuous maps to `A` with the indiscrete topology, which is an
> fpqc sheaf.

```lean
theorem pointFunctions_isSheaf (X : Scheme.{u}) (A : Type v) [AddCommGroup A] :
    Presheaf.IsSheaf (Scheme.ProEt.topology X) (pointFunctions.{u, v} X A)
```

**`AlgebraicGeometry.ProEtale.mono_constantToPointFunctions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean#L289). The attribute's comment: “exactness on the left of `0 → A → fun(-, A) → F → 0`”.

> **The constant sheaf is a subsheaf of `fun(-, A)`**: the map `A ⟶ fun(-, A)` is a
> monomorphism, which is exactness on the left of `0 → A → fun(-, A) → F → 0`.

```lean
theorem mono_constantToPointFunctions (X : Scheme.{u}) (A : Type v) [AddCommGroup A] :
    Mono (constantToPointFunctions.{u, v} X A)
```

**`AlgebraicGeometry.ProEtale.pointFunctionsShortComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean#L333). The attribute's comment: “the sequence `0 → A → fun(-, A) → F → 0` is exact”.

> **The sequence `0 → A → fun(-, A) → F → 0` is short exact.**

```lean
theorem pointFunctionsShortComplex_shortExact (X : Scheme.{u}) (A : Type v) [AddCommGroup A] :
    (pointFunctionsShortComplex X A).ShortExact
```

**`AlgebraicGeometry.ProEtale.ker_pointFunctionsQuotientProjApp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean#L352). The attribute's comment: “the kernel of `fun(U, A) → F(U)` is `A(U)`”.

> **The kernel of `fun(U, A) ⟶ F(U)` is `A(U)`**, for every object `U` of the small pro-étale
> site: sections are left exact.

```lean
theorem ker_pointFunctionsQuotientProjApp (X : Scheme.{u}) (A : Type v) [AddCommGroup A]
    (U : X.ProEt) :
    (pointFunctionsQuotientProjApp X A U).ker = (constantToPointFunctionsApp X A U).range
```

**`AlgebraicGeometry.ProEtale.constantSheafCompEpsilonInverseImageIsoConstantSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean#L374). The attribute's comment: “`A = ε⁻¹A`: the constant sheaf is pulled back from the étale site”.

> **The constant sheaf is pulled back from the étale site: `A = ε⁻¹A`.** Both the constant
> sheaf functor of the small pro-étale site and the constant sheaf functor of the small étale site
> followed by `ε⁻¹` are left adjoint to taking sections over the final object `X ⟶ X`, that is,
> both are the pullback from the final topos; the isomorphism is the comparison of these two left
> adjoints, natural in the coefficient group.

```lean
def constantSheafCompEpsilonInverseImageIsoConstantSheaf (X : Scheme.{u}) :
    constantSheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v} ⋙
        epsilonInverseImage.{u, v} X ≅
      constantSheaf (Scheme.ProEt.topology X) AddCommGrpCat.{max (u + 1) v}
```

**`AlgebraicGeometry.ProEtale.not_etalePullback_pointFunctionsSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean, line 603](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean#L603). The attribute's comment: “if `A` has more than one element, `fun(-, A)` is not pulled back from the étale site (for `X` nonempty)”.

> **`fun(-, A)` is not pulled back from the étale site.** If `X` is nonempty and `A` has more
> than one element, `fun(-, A)` is not in the essential image of `ε⁻¹`.
>
> A pulled back sheaf restricted to the fibre over a point `x` only sees continuous functions on the
> fibres of its sections' domains with the discrete topology on `A`, since the fibres of étale
> `X`-schemes over `x` are discrete; but there is a weakly étale `X`-scheme whose fibre over `x`
> contains a Cantor set, on which not every function is continuous.

```lean
theorem not_etalePullback_pointFunctionsSheaf (X : Scheme.{u}) (A : Type v)
    [AddCommGroup A] (hX : Nonempty X) (hA : Nontrivial A) :
    ¬ (epsilonInverseImage.{u, v} X).essImage (pointFunctionsSheaf X A)
```

**`AlgebraicGeometry.ProEtale.isClosed_singleton_of_proetale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean, line 632](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean#L632). The attribute's comment: “if all points of `X` are closed, then all points of `U` are closed”.

> **Closed points pass to weakly étale `X`-schemes.** If all points of `X` are closed, then all
> points of every object `U` of the small pro-étale site of `X` are closed: over an affine open of
> `X`, whose spectrum is then profinite, an affine open of `U` has profinite spectrum too.

```lean
theorem isClosed_singleton_of_proetale (X : Scheme.{u})
    (hclosed : ∀ x : X, IsClosed ({x} : Set X))
    (U : X.ProEt) (y : U.left) : IsClosed ({y} : Set U.left)
```

**`AlgebraicGeometry.ProEtale.isSepClosed_residueField_of_proetale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean, line 698](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean#L698). The attribute's comment: “if all residue fields of `X` are separably closed, then so are those of `U`”.

> **Separably closed residue fields pass to weakly étale `X`-schemes.** If all residue fields
> of `X` are separably closed, then so are all residue fields of every object `U` of the small
> pro-étale site of `X`: the residue field extensions of a weakly étale morphism are separable
> algebraic.

```lean
theorem isSepClosed_residueField_of_proetale (X : Scheme.{u})
    (hsep : ∀ x : X, IsSepClosed (X.residueField x))
    (U : X.ProEt) (y : U.left) : IsSepClosed (U.left.residueField y)
```

**`AlgebraicGeometry.ProEtale.subsingleton_etaleH_one_constantSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean, line 717](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean#L717). The attribute's comment: “`H¹_étale(U, A) = 0` for affine `U`, when all points of `X` are closed with separably closed residue fields”.

> **`H¹_étale(U, A) = 0`** for an affine object `U` of the small pro-étale site of a scheme `X`
> all of whose points are closed with separably closed residue fields: the points of `U` are then
> closed with separably closed residue fields, and étale cohomology in positive degrees vanishes on
> such an affine scheme.

```lean
theorem subsingleton_etaleH_one_constantSheaf (X : Scheme.{u}) (A : Type v) [AddCommGroup A]
    (hclosed : ∀ x : X, IsClosed ({x} : Set X))
    (hsep : ∀ x : X, IsSepClosed (X.residueField x))
    (U : X.ProEt) [IsAffine U.left]
    [HasExt.{w} (Sheaf U.left.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})] :
    Subsingleton (Sheaf.H.{w}
      ((constantSheaf U.left.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}).obj
        (pointFunctionsCoeff.{u} A)) 1)
```

**`AlgebraicGeometry.ProEtale.subsingleton_proetaleH_one_constantSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean, line 740](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean#L740). The attribute's comment: “`H¹_proétale(U, A) = 0` for affine `U`, when all points of `X` are closed with separably closed residue fields”.

> **`H¹_proétale(U, A) = 0`** for an affine object `U` of the small pro-étale site of a scheme
> `X` all of whose points are closed with separably closed residue fields: by the comparison
> `H^i(U_étale, ℱ) = H^i(U_proétale, ε⁻¹ℱ)` of étale and pro-étale cohomology on `U` (Stacks 099W
> (1), `AlgebraicGeometry.ProEtale.epsilonInverseImageCompFunctorHIso`) and `A = ε⁻¹A`, it reduces
> to `H¹_étale(U, A) = 0`.

```lean
theorem subsingleton_proetaleH_one_constantSheaf (X : Scheme.{u})
    (A : Type v) [AddCommGroup A]
    (hclosed : ∀ x : X, IsClosed ({x} : Set X))
    (hsep : ∀ x : X, IsSepClosed (X.residueField x))
    (U : X.ProEt) [IsAffine U.left]
    [HasExt.{w} (Sheaf (Scheme.ProEt.topology U.left) AddCommGrpCat.{max (u + 1) v})] :
    Subsingleton (Sheaf.H.{w}
      ((constantSheaf (Scheme.ProEt.topology U.left) AddCommGrpCat.{max (u + 1) v}).obj
        (pointFunctionsCoeff.{u} A)) 1)
```

**`AlgebraicGeometry.ProEtale.surjective_pointFunctionsQuotientProjApp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean, line 812](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean#L812). The attribute's comment: “`F(U) = fun(U, A)/A(U)` for affine `U`: every section of `F` over `U` lifts to `fun(U, A)`”.

> **`fun(U, A) ⟶ F(U)` is surjective** for an affine object `U` of the small pro-étale site of
> a scheme `X` all of whose points are closed with separably closed residue fields: the obstruction
> lies in `H¹_proétale(U, A)`, which vanishes.

```lean
theorem surjective_pointFunctionsQuotientProjApp (X : Scheme.{u})
    (A : Type v) [AddCommGroup A]
    (hclosed : ∀ x : X, IsClosed ({x} : Set X))
    (hsep : ∀ x : X, IsSepClosed (X.residueField x))
    (U : X.ProEt) [IsAffine U.left] :
    Function.Surjective (pointFunctionsQuotientProjApp.{u, v} X A U)
```

**`AlgebraicGeometry.ProEtale.pointFunctionsQuotientAppEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean, line 874](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean#L874). The attribute's comment: “`F(U) = fun(U, A)/A(U)` for affine `U`, when all points of `X` are closed with separably closed residue fields”.

> **`F(U) = fun(U, A)/A(U)`** for an affine object `U` of the small pro-étale site of a scheme
> `X` all of whose points are closed with separably closed residue fields: the projection
> `fun(U, A) ⟶ F(U)` is surjective with kernel the constant sections `A(U)`.

```lean
def pointFunctionsQuotientAppEquiv (X : Scheme.{u})
    (A : Type v) [AddCommGroup A]
    (hclosed : ∀ x : X, IsClosed ({x} : Set X))
    (hsep : ∀ x : X, IsSepClosed (X.residueField x))
    (U : X.ProEt) [IsAffine U.left] :
    (U.left → ULift.{max (u + 1) v} A) ⧸ (constantToPointFunctionsApp.{u, v} X A U).range ≃+
      (pointFunctionsQuotient.{u, v} X A).obj.obj (op U)
```

**`AlgebraicGeometry.ProEtale.not_etalePullback_pointFunctionsQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean, line 892](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/PointFunctions.lean#L892). The attribute's comment: “if `A` has more than one element, the quotient `F` is not pulled back from the étale site (for `X` nonempty)”.

> **`F` is not pulled back from the étale site.** If `X` is nonempty and `A` has more than one
> element, the quotient `F = fun(-, A)/A` is not in the essential image of `ε⁻¹`: since
> `Rε_*ε⁻¹ℱ = ℱ` for abelian sheaves `ℱ` on `X_étale` (Stacks 099V (1),
> `AlgebraicGeometry.ProEtale.isIso_unit_app_and_isZero_rightDerived_epsilonDirectImage`), the
> essential image of `ε⁻¹` is closed under extensions, `A = ε⁻¹A`, and `fun(-, A)` is not in it.

```lean
theorem not_etalePullback_pointFunctionsQuotient (X : Scheme.{u}) (A : Type v)
    [AddCommGroup A] (hX : Nonempty X) (hA : Nontrivial A) :
    ¬ (epsilonInverseImage.{u, v} X).essImage (pointFunctionsQuotient X A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.19, Tag 099R](https://stacks.math.columbia.edu/tag/099R)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
