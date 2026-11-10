---
declaration: section
origin: cited
lean: Stacks.MayerVietoris.CanonicalMapOfComplexes.firstMap, Stacks.MayerVietoris.CanonicalMapOfComplexes.secondMap, Stacks.MayerVietoris.CanonicalMapOfComplexes.cSquare, Stacks.MayerVietoris.CanonicalMapOfComplexes.firstMap_comp_secondMap, Stacks.MayerVietoris.CanonicalMapOfComplexes.cSquare_natural, Stacks.MayerVietoris.CanonicalMapOfComplexes.cSquare_arrow_iso_of_isKInjective, Stacks.MayerVietoris.CanonicalMapOfComplexes.DerivedCSquareData.cSquareTriangle, Stacks.MayerVietoris.CanonicalMapOfComplexes.DerivedCSquareData.isCSquareIso_iff_quasiIso
statement: formalized
proof: formalized
---

# 21.26 Mayer-Vietoris

Section 21.26 of the Stacks Project, [Tag 0EVX](https://stacks.math.columbia.edu/tag/0EVX). 4 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F16, a lemma

[Tag 0F16](https://stacks.math.columbia.edu/tag/0F16) in the Stacks Project.

**`Stacks.MayerVietoris.CanonicalMapOfComplexes.firstMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/CanonicalMapOfComplexes.lean, line 561](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/CanonicalMapOfComplexes.lean#L561). The attribute's comment: “the map alpha”.

> The map `I(X) ⟶ I(Z) ⊞ I(Y)`.

```lean
noncomputable def firstMap (I : CochainComplex (SheafOfModules.{v} R) ℤ) :
    (sectionsComplex R sq.X₄).obj I ⟶
      (sectionsComplex R sq.X₃).obj I ⊞ (sectionsComplex R sq.X₂).obj I
```

**`Stacks.MayerVietoris.CanonicalMapOfComplexes.secondMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/CanonicalMapOfComplexes.lean, line 568](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/CanonicalMapOfComplexes.lean#L568). The attribute's comment: “the map beta”.

> The signed map `I(Z) ⊞ I(Y) ⟶ I(E)`.

```lean
noncomputable def secondMap (I : CochainComplex (SheafOfModules.{v} R) ℤ) :
    (sectionsComplex R sq.X₃).obj I ⊞ (sectionsComplex R sq.X₂).obj I ⟶
      (sectionsComplex R sq.X₁).obj I
```

**`Stacks.MayerVietoris.CanonicalMapOfComplexes.cSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/CanonicalMapOfComplexes.lean, line 575](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/CanonicalMapOfComplexes.lean#L575). The attribute's comment: “the canonical map of complexes”.

> The canonical map `I(X) ⟶ C(β)[-1]`, using the zero null-homotopy.

```lean
noncomputable def cSquare (I : CochainComplex (SheafOfModules.{v} R) ℤ) :
    (sectionsComplex R sq.X₄).obj I ⟶ CochainComplex.mappingCocone (secondMap sq I)
```

**`Stacks.MayerVietoris.CanonicalMapOfComplexes.firstMap_comp_secondMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/CanonicalMapOfComplexes.lean, line 581](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/CanonicalMapOfComplexes.lean#L581). The attribute's comment: “the relation beta composed with alpha is zero”.

> Signed restriction maps compose to zero.

```lean
theorem firstMap_comp_secondMap (I : CochainComplex (SheafOfModules.{v} R) ℤ) :
    firstMap sq I ≫ secondMap sq I = 0
```

**`Stacks.MayerVietoris.CanonicalMapOfComplexes.cSquare_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/CanonicalMapOfComplexes.lean, line 631](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/CanonicalMapOfComplexes.lean#L631). The attribute's comment: “functoriality on complexes”.

> The chain-level canonical maps commute with chain maps.

```lean
theorem cSquare_natural {I I' : CochainComplex (SheafOfModules.{v} R) ℤ} (f : I ⟶ I') :
    (sectionsComplex R sq.X₄).map f ≫ cSquare sq I' =
      cSquare sq I ≫ mappingCoconeMap sq f
```

**`Stacks.MayerVietoris.CanonicalMapOfComplexes.cSquare_arrow_iso_of_isKInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/CanonicalMapOfComplexes.lean, line 652](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/CanonicalMapOfComplexes.lean#L652). The attribute's comment: “independence of the K-injective representative”.

> Changing a K-injective representative gives an isomorphic arrow in `D(Ab)`.
>
> Two K-injective representatives of the same derived object are homotopy equivalent, and
> the chain-level canonical map is natural; the induced map of mapping cocones is inverted
> by the localization functor because it is the third component of a morphism of
> distinguished triangles whose other two components are inverted.

```lean
theorem cSquare_arrow_iso_of_isKInjective
    (K : DerivedCategory (SheafOfModules.{v} R))
    (I I' : CochainComplex (SheafOfModules.{v} R) ℤ)
    [I.IsKInjective] [I'.IsKInjective]
    (_ : DerivedCategory.Q.obj I ≅ K) (_ : DerivedCategory.Q.obj I' ≅ K) :
    Nonempty (Arrow.mk (DerivedCategory.Q.map (cSquare sq I)) ≅
      Arrow.mk (DerivedCategory.Q.map (cSquare sq I')))
```

**`Stacks.MayerVietoris.CanonicalMapOfComplexes.DerivedCSquareData.cSquareTriangle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/DerivedCanonicalMapAndTriangle.lean, line 1147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/DerivedCanonicalMapAndTriangle.lean#L1147). The attribute's comment: “the canonical triangle on derived objects”.

> The triangle on derived sections, with boundary obtained using the inverse of `c`.

```lean
noncomputable def cSquareTriangle (K : DerivedCategory (SheafOfModules.{v} R))
    [D.IsCSquareIso K] : Triangle (DerivedCategory AddCommGrpCat.{v})
```

**`Stacks.MayerVietoris.CanonicalMapOfComplexes.DerivedCSquareData.isCSquareIso_iff_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/DerivedCanonicalMapAndTriangle.lean, line 1154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/DerivedCanonicalMapAndTriangle.lean#L1154). The attribute's comment: “computation of the isomorphism condition”.

> The canonical condition on a derived object can be tested on any K-injective
> representative.

```lean
theorem isCSquareIso_iff_quasiIso (K : DerivedCategory (SheafOfModules.{v} R))
    (I : CochainComplex (SheafOfModules.{v} R) ℤ) [I.IsKInjective]
    (e : DerivedCategory.Q.obj I ≅ K) :
    D.IsCSquareIso K ↔ QuasiIso (cSquare sq I)
```

**`Stacks.MayerVietoris.CanonicalMapOfComplexes.DerivedCSquareData.cSquareTriangle_functorial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/DerivedCanonicalMapAndTriangle.lean, line 1163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/DerivedCanonicalMapAndTriangle.lean#L1163). The attribute's comment: “functoriality of the triangle in the derived object”.

> Every derived morphism induces a unique morphism of the derived triangles with the given
> three components.

```lean
theorem cSquareTriangle_functorial {K K' : DerivedCategory (SheafOfModules.{v} R)} (f : K ⟶ K')
    [D.IsCSquareIso K] [D.IsCSquareIso K'] :
    ∃! t : D.cSquareTriangle K ⟶ D.cSquareTriangle K',
      t.hom₁ = (D.derivedSections sq.X₄).map f ∧
        t.hom₂ = biprod.map ((D.derivedSections sq.X₃).map f)
          ((D.derivedSections sq.X₂).map f) ∧
        t.hom₃ = (D.derivedSections sq.X₁).map f
```

**`Stacks.MayerVietoris.CanonicalMapOfComplexes.derivedCSquareData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/DerivedCanonicalMapAndTriangle.lean, line 1319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/DerivedCanonicalMapAndTriangle.lean#L1319). The attribute's comment: “the functorial derived construction and its K-injective computation”.

> **The derived construction of the canonical map of a square**, under `UnivLE` between the
> universes of the site, of its homs, of the rings and of the modules.

```lean
noncomputable def derivedCSquareData [UnivLE.{u, v}] [UnivLE.{w, v}] [UnivLE.{r, v}] :
    DerivedCSquareData.{u, v} (R := R) sq
```

**`Stacks.MayerVietoris.CanonicalMapOfComplexes.cSquareTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/DerivedCanonicalMapAndTriangle.lean, line 1330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/DerivedCanonicalMapAndTriangle.lean#L1330). The attribute's comment: “the triangle is distinguished”.

> **The derived-section triangle is distinguished** at every derived object where the
> canonical map is invertible, under `UnivLE` between the universes of the site, of its homs, of
> the rings and of the modules.

```lean
theorem cSquareTriangle_distinguished [UnivLE.{u, v}] [UnivLE.{w, v}] [UnivLE.{r, v}]
    (K : DerivedCategory (SheafOfModules.{v} R))
    [(derivedCSquareData.{u, v} (R := R) sq).IsCSquareIso K] :
    (derivedCSquareData.{u, v} (R := R) sq).cSquareTriangle K ∈
      distTriang (DerivedCategory AddCommGrpCat.{v})
```

## Tag 0EWP, a lemma

[Tag 0EWP](https://stacks.math.columbia.edu/tag/0EWP) in the Stacks Project.

**`Stacks.MayerVietoris.CanonicalMapOfComplexes.isCSquareIso_obj₃_of_distTriang`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/TwoOutOfThree.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/TwoOutOfThree.lean#L390). The attribute's comment: “first and second vertices imply the third”.

> **Stacks Project, Tag 0EWP.** The comparison for the third vertex is an isomorphism if it is
> so for the first two vertices of a distinguished triangle.

```lean
theorem isCSquareIso_obj₃_of_distTriang
    (T : Triangle (DerivedCategory
      (SheafOfModules.{v} (Stacks.SheafOfModules.Tensor.ringSheaf S.O))))
    (hT : T ∈ distTriang (DerivedCategory
      (SheafOfModules.{v} (Stacks.SheafOfModules.Tensor.ringSheaf S.O))))
    (h₁ : (derivedCSquareData.{u, v} (R := (Stacks.SheafOfModules.Tensor.ringSheaf S.O))
      sq).IsCSquareIso T.obj₁)
    (h₂ : (derivedCSquareData.{u, v} (R := (Stacks.SheafOfModules.Tensor.ringSheaf S.O))
      sq).IsCSquareIso T.obj₂) :
    (derivedCSquareData.{u, v} (R := (Stacks.SheafOfModules.Tensor.ringSheaf S.O))
        sq).IsCSquareIso T.obj₃
```

**`Stacks.MayerVietoris.CanonicalMapOfComplexes.isCSquareIso_obj₁_of_distTriang`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/TwoOutOfThree.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/TwoOutOfThree.lean#L406). The attribute's comment: “second and third vertices imply the first”.

> **Stacks Project, Tag 0EWP.** The comparison for the first vertex is an isomorphism if it is
> so for the second and third vertices of a distinguished triangle.

```lean
theorem isCSquareIso_obj₁_of_distTriang
    (T : Triangle (DerivedCategory
      (SheafOfModules.{v} (Stacks.SheafOfModules.Tensor.ringSheaf S.O))))
    (hT : T ∈ distTriang (DerivedCategory
      (SheafOfModules.{v} (Stacks.SheafOfModules.Tensor.ringSheaf S.O))))
    (h₂ : (derivedCSquareData.{u, v} (R := (Stacks.SheafOfModules.Tensor.ringSheaf S.O))
      sq).IsCSquareIso T.obj₂)
    (h₃ : (derivedCSquareData.{u, v} (R := (Stacks.SheafOfModules.Tensor.ringSheaf S.O))
      sq).IsCSquareIso T.obj₃) :
    (derivedCSquareData.{u, v} (R := (Stacks.SheafOfModules.Tensor.ringSheaf S.O))
        sq).IsCSquareIso T.obj₁
```

**`Stacks.MayerVietoris.CanonicalMapOfComplexes.isCSquareIso_obj₂_of_distTriang`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/TwoOutOfThree.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/TwoOutOfThree.lean#L422). The attribute's comment: “first and third vertices imply the second”.

> **Stacks Project, Tag 0EWP.** The comparison for the second vertex is an isomorphism if it
> is so for the first and third vertices of a distinguished triangle.

```lean
theorem isCSquareIso_obj₂_of_distTriang
    (T : Triangle (DerivedCategory
      (SheafOfModules.{v} (Stacks.SheafOfModules.Tensor.ringSheaf S.O))))
    (hT : T ∈ distTriang (DerivedCategory
      (SheafOfModules.{v} (Stacks.SheafOfModules.Tensor.ringSheaf S.O))))
    (h₁ : (derivedCSquareData.{u, v} (R := (Stacks.SheafOfModules.Tensor.ringSheaf S.O))
      sq).IsCSquareIso T.obj₁)
    (h₃ : (derivedCSquareData.{u, v} (R := (Stacks.SheafOfModules.Tensor.ringSheaf S.O))
      sq).IsCSquareIso T.obj₃) :
    (derivedCSquareData.{u, v} (R := (Stacks.SheafOfModules.Tensor.ringSheaf S.O))
        sq).IsCSquareIso T.obj₂
```

## Tag 0EVY, a lemma

[Tag 0EVY](https://stacks.math.columbia.edu/tag/0EVY) in the Stacks Project.

**`Stacks.Cohomology.MayerVietoris.isIso_derivedCSquare_of_isPushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/TriangleOfAPushoutSquare.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/TriangleOfAPushoutSquare.lean#L196).

> **Stacks 0EVY.** If the sheafified representables of the square form a pushout square and
> `h_E^# ⟶ h_Y^#` is a monomorphism, then the canonical natural transformation of Stacks 0F16 is
> an isomorphism, so that the Mayer-Vietoris triangle is distinguished and functorial for every
> object of the derived category of module sheaves.

```lean
theorem isIso_derivedCSquare_of_isPushout (sq : Square S.C)
    (hpushout : (sq.map (Sheaf.sheafifiedYoneda S.J)).IsPushout)
    (hmono : Mono ((Sheaf.sheafifiedYoneda S.J).map sq.f₁₂)) :
    IsIso (CanonicalMapOfComplexes.derivedCSquareData.{u, v}
      (R := (Stacks.SheafOfModules.Tensor.ringSheaf S.O)) sq).derivedCSquare
```

## Tag 0EVZ, a lemma

[Tag 0EVZ](https://stacks.math.columbia.edu/tag/0EVZ) in the Stacks Project.

**`Stacks.MayerVietoris.PresheafSquare.isIso_derivedCSquare_of_isPushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/TriangleOfAPresheafPushoutSquare.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/TriangleOfAPresheafPushoutSquare.lean#L126). The attribute's comment: “the canonical comparison”.

> **Stacks 0EVZ.** If the sheafifications of a square of presheaves of sets form a pushout
> square and `D^# ⟶ F^#` is a monomorphism, then the canonical natural transformation of
> Stacks 0F16 from derived sections over `G` to the mapping cocone is an isomorphism, so that the
> Mayer–Vietoris triangle is defined at every object of the derived category of abelian
> sheaves.

```lean
theorem isIso_derivedCSquare_of_isPushout
    (hpushout : (sq.map (presheafToSheaf J (Type u))).IsPushout)
    (hmono : Mono ((presheafToSheaf J (Type u)).map sq.f₁₂)) :
    IsIso (derivedCSquareData J sq).derivedCSquare
```

**`Stacks.MayerVietoris.PresheafSquare.cSquareTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/TriangleOfAPresheafPushoutSquare.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/TriangleOfAPresheafPushoutSquare.lean#L161). The attribute's comment: “the triangle is distinguished”.

> **Stacks 0EVZ.** The Mayer–Vietoris triangle of a square of presheaves of sets whose
> sheafifications form a pushout square with monomorphic `D^# ⟶ F^#` is a distinguished triangle
> of the derived category of abelian groups, at every object of the derived category of abelian
> sheaves.

```lean
theorem cSquareTriangle_distinguished (K : DerivedCategory (Sheaf J AddCommGrpCat.{u})) :
    cSquareTriangle J sq hpushout hmono K ∈ distTriang (DerivedCategory AddCommGrpCat.{u})
```

**`Stacks.MayerVietoris.PresheafSquare.cSquareTriangle_functorial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/TriangleOfAPresheafPushoutSquare.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/TriangleOfAPresheafPushoutSquare.lean#L170). The attribute's comment: “functoriality of the triangle in the derived object”.

> **Stacks 0EVZ, the functoriality in the derived object.** Every morphism of derived objects
> induces a unique morphism of Mayer–Vietoris triangles whose three components are the maps
> induced on derived sections and on the mapping cocone.

```lean
theorem cSquareTriangle_functorial
    {K K' : DerivedCategory (Sheaf J AddCommGrpCat.{u})} (f : K ⟶ K') :
    ∃! t : cSquareTriangle J sq hpushout hmono K ⟶ cSquareTriangle J sq hpushout hmono K',
      t.hom₁ = ((derivedCSquareData J sq).derivedSections sq.X₄).map f ∧
        t.hom₂ = ((derivedCSquareData J sq).sectionsData.biprodFunctor sq).map f ∧
        t.hom₃ = ((derivedCSquareData J sq).derivedSections sq.X₁).map f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.26, Tag 0EVX](https://stacks.math.columbia.edu/tag/0EVX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
