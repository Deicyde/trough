---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_addEquiv_coherentKZero_K0, AlgebraicGeometry.exists_addEquiv_coherentKZero_K0_bounded, AlgebraicGeometry.exists_addEquiv_K0_bounded_K0_boundedCoherent, Stacks.Perfect.BoundedLocallyFreeComplexes.perfectDerivedProperty_isTriangulated, Stacks.Perfect.BoundedLocallyFreeComplexes.perfectDerivedProperty_isClosedUnderIsomorphisms, AlgebraicGeometry.coherentModulesAbelian, AlgebraicGeometry.CoherentKZero, Stacks.Perfect.BoundedLocallyFreeComplexes.perfectDerivedProperty_isSaturated
statement: formalized
proof: formalized
---

# 36.38 K-groups

Section 36.38 of the Stacks Project, [Tag 0FDE](https://stacks.math.columbia.edu/tag/0FDE). 9 tags here are carried by 34 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FDF, a lemma

[Tag 0FDF](https://stacks.math.columbia.edu/tag/0FDF) in the Stacks Project.

**`AlgebraicGeometry.exists_addEquiv_coherentKZero_K0`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroup.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroup.lean#L77). The attribute's comment: “the identification K₀(Coh(𝒪\_X)) = K₀(D^b\_Coh(𝒪\_X)), the source's second equality. The source's middle group K₀(D^b(Coh(𝒪\_X))) is `AlgebraicGeometry.exists_addEquiv_coherentKZero_K0_bounded`”. References: SGA 6 IV (2.4), “special case”; SGA 6 IV (3.2.3), “more general”.

> **Stacks Project, Tag 0FDF.** The Grothendieck group `K'₀(X)` of coherent sheaves on a scheme
> `X` is the zeroth `K`-group of `D^b_Coh(𝒪_X)`, the bounded objects of `D(𝒪_X)` with coherent
> cohomology sheaves, by an isomorphism sending the class of a coherent sheaf to the class of that
> sheaf placed in degree `0`; and that property determines it.

```lean
theorem exists_addEquiv_coherentKZero_K0 (X : Scheme.{u})
    [HasDerivedCategory.{d} (SheafOfModules.{u} X.ringCatSheaf)] :
    ∃ e : CoherentKZero X ≃+ Pretriangulated.K0 (DerivedCategoryB.derivedCategoryBBounded
        (Stacks.SheafOfModules.coherentModules X.ringCatSheaf)).FullSubcategory,
      (∀ F : Stacks.SheafOfModules.CoherentModules X.ringCatSheaf,
          ∃ K : (DerivedCategoryB.derivedCategoryBBounded
              (Stacks.SheafOfModules.coherentModules X.ringCatSheaf)).FullSubcategory,
            Nonempty (K.obj ≅ (DerivedCategory.singleFunctor
              (SheafOfModules.{u} X.ringCatSheaf) 0).obj F.obj)) ∧
        ∀ (F : Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)
          (K : (DerivedCategoryB.derivedCategoryBBounded
              (Stacks.SheafOfModules.coherentModules X.ringCatSheaf)).FullSubcategory),
          (K.obj ≅ (DerivedCategory.singleFunctor
              (SheafOfModules.{u} X.ringCatSheaf) 0).obj F.obj) →
            e (KZero.mk _ F) = QuotientAddGroup.mk (FreeAbelianGroup.of K)
```

**`AlgebraicGeometry.exists_addEquiv_coherentKZero_K0_bounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupBoundedCoherent.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupBoundedCoherent.lean#L62). The attribute's comment: “the identification K₀(Coh(𝒪\_X)) = K₀(D^b(Coh(𝒪\_X))), the source's first equality”. References: SGA 6 IV (1.5), “(1.5.3), special case”.

> **Stacks Project, Tag 0FDF.** The Grothendieck group `K'₀(X)` of coherent sheaves on a scheme
> `X` is the zeroth `K`-group of `D^b(Coh(𝒪_X))`, the bounded derived category of the abelian
> category of coherent `𝒪_X`-modules, by an isomorphism sending the class of a coherent sheaf to the
> class of that sheaf placed in degree `0`.

```lean
theorem exists_addEquiv_coherentKZero_K0_bounded (X : Scheme.{u})
    [HasDerivedCategory.{d} (Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)] :
    ∃ e : CoherentKZero X ≃+ Pretriangulated.K0
        (DerivedCategory.Bounded (Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)),
      ∀ F : Stacks.SheafOfModules.CoherentModules X.ringCatSheaf,
        e (KZero.mk _ F) = QuotientAddGroup.mk (FreeAbelianGroup.of
          (⟨(DerivedCategory.singleFunctor
                (Stacks.SheafOfModules.CoherentModules X.ringCatSheaf) 0).obj F,
            ⟨⟨0, inferInstance⟩, ⟨0, inferInstance⟩⟩⟩ :
            DerivedCategory.Bounded (Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)))
```

**`AlgebraicGeometry.exists_addEquiv_K0_bounded_K0_boundedCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupBoundedCoherent.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupBoundedCoherent.lean#L82). The attribute's comment: “the identification K₀(D^b(Coh(𝒪\_X))) = K₀(D^b\_Coh(𝒪\_X)) of the source's two outer groups”.

> **Stacks Project, Tag 0FDF.** For a scheme `X` the two outer groups of the chain of Tag 0FDF
> agree: the zeroth `K`-group of `D^b(Coh(𝒪_X))`, the bounded derived category of the abelian
> category of coherent `𝒪_X`-modules, is isomorphic to the zeroth `K`-group of `D^b_Coh(𝒪_X)`, the
> bounded objects of `D(𝒪_X)` whose cohomology sheaves are coherent. The isomorphism matches the
> classes of a coherent sheaf placed in degree `0` on the two sides: it carries the class of `F` in
> `D^b(Coh(𝒪_X))` to the class of any object of `D^b_Coh(𝒪_X)` isomorphic to `F` in degree `0`.

```lean
theorem exists_addEquiv_K0_bounded_K0_boundedCoherent (X : Scheme.{u})
    [HasDerivedCategory.{d} (SheafOfModules.{u} X.ringCatSheaf)]
    [HasDerivedCategory.{d'} (Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)] :
    ∃ e : Pretriangulated.K0
        (DerivedCategory.Bounded (Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)) ≃+
      Pretriangulated.K0 (DerivedCategoryB.derivedCategoryBBounded
        (Stacks.SheafOfModules.coherentModules X.ringCatSheaf)).FullSubcategory,
      ∀ (F : Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)
        (K : (DerivedCategoryB.derivedCategoryBBounded
            (Stacks.SheafOfModules.coherentModules X.ringCatSheaf)).FullSubcategory),
        (K.obj ≅ (DerivedCategory.singleFunctor
            (SheafOfModules.{u} X.ringCatSheaf) 0).obj F.obj) →
          e (QuotientAddGroup.mk (FreeAbelianGroup.of
              (⟨(DerivedCategory.singleFunctor
                    (Stacks.SheafOfModules.CoherentModules X.ringCatSheaf) 0).obj F,
                ⟨⟨0, inferInstance⟩, ⟨0, inferInstance⟩⟩⟩ :
                DerivedCategory.Bounded
                  (Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)))) =
            QuotientAddGroup.mk (FreeAbelianGroup.of K)
```

## Tag 0FDG, a definition

[Tag 0FDG](https://stacks.math.columbia.edu/tag/0FDG) in the Stacks Project.

**`Stacks.Perfect.BoundedLocallyFreeComplexes.perfectDerivedProperty_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/CanonicalFunctor.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/CanonicalFunctor.lean#L58). The attribute's comment: “(1) D\_perf(𝒪\_X) is TRIANGULATED in D(𝒪\_X) — the adjective of Definition 0FDG (1) that makes `K₀` of the subcategory defined at all, `CategoryTheory.Pretriangulated.K0` taking a `[Pretriangulated]` instance. The definitional clause itself is `AlgebraicGeometry.PerfectKZero`”. References: SGA 6 I (5.8.4), “special case”; SGA 6 III (4.2), “Identity-morphism case”.

> **Perfect objects form a triangulated subcategory of `D(O_X)`.** This is the ringed-space
> statement `Stacks.Cohomology.PerfectTriangulatedSubcategory.isTriangulated_isPerfect`, read on the
> ringed space underlying `X`.

```lean
instance perfectDerivedProperty_isTriangulated (X : Scheme.{u}) :
    (show ObjectProperty (DerivedCategory X.Modules) from
      fun K => IsPerfect (X := X.toRingedSpace) K).IsTriangulated
```

**`Stacks.Perfect.BoundedLocallyFreeComplexes.perfectDerivedProperty_isClosedUnderIsomorphisms`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Defs.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BoundedLocallyFreeComplexes/Defs.lean#L109). The attribute's comment: “(1) D\_perf(𝒪\_X) is STRICTLY FULL in D(𝒪\_X) — the first of the three adjectives Definition 0FDG (1) attaches to the subcategory whose K-group it names. The definitional clause itself is `AlgebraicGeometry.PerfectKZero`”.

> **Perfect objects form a strictly full subcategory of `D(O_X)`.**

```lean
instance perfectDerivedProperty_isClosedUnderIsomorphisms (X : Scheme.{u}) :
    ObjectProperty.IsClosedUnderIsomorphisms
      (fun K : DerivedCategory X.Modules => IsPerfect (X := X.toRingedSpace) K)
```

**`AlgebraicGeometry.coherentModulesAbelian`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroup.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroup.lean#L58). The attribute's comment: “coherent\_abelian”. References: SGA 6 II (2.2.1), “Coh(S) abelian”.

> **Stacks Project, Tag 0FDG.** Coherent sheaves of modules on a scheme form an abelian
> category.

```lean
noncomputable instance coherentModulesAbelian (X : Scheme.{u}) :
    Abelian (Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)
```

**`AlgebraicGeometry.CoherentKZero`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroup.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroup.lean#L65). The attribute's comment: “coherent\_k0”. References: SGA 6 X (1.1); SGA 6 IV (2.2), “K\_•(A\_X)\_naif”.

> **Stacks Project, Tag 0FDG (2).** The Grothendieck group `K'₀(X)` of coherent sheaves on a
> scheme `X`.

```lean
noncomputable abbrev CoherentKZero (X : Scheme.{u}) : Type _
```

**`Stacks.Perfect.BoundedLocallyFreeComplexes.perfectDerivedProperty_isSaturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupPerfect.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupPerfect.lean#L79). The attribute's comment: “(1) D\_perf(𝒪\_X) is SATURATED in D(𝒪\_X) — the third of the three adjectives Definition 0FDG (1) attaches to the subcategory whose K-group it names, and the only one the definition does not consume as an instance. The definitional clause itself is `AlgebraicGeometry.PerfectKZero`”.

> **`D_perf(𝒪_X)` is a saturated subcategory of `D(𝒪_X)`**: both summands of a perfect
> biproduct are perfect. This is Tag 08CS, read on the ringed space underlying `X` at the standard
> derived-category universe, fed to
> `Stacks.Perfect.BoundedLocallyFreeComplexes.isSaturated_isPerfect_of_biprod`.

```lean
theorem perfectDerivedProperty_isSaturated (X : Scheme.{u}) :
    (show ObjectProperty (DerivedCategory X.Modules) from
      fun K => IsPerfect (X := X.toRingedSpace) K).IsSaturated
```

**`AlgebraicGeometry.PerfectKZero`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupPerfect.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupPerfect.lean#L104). The attribute's comment: “(1) the DEFINITIONAL clause: K₀(X) := K₀(D\_perf(𝒪\_X)). Being a definition this states nothing on its own; the three adjectives the source attaches to D\_perf(𝒪\_X) are the assertional part of (1) and are registered separately, on `perfectDerivedProperty_isClosedUnderIsomorphisms` (strictly full), `perfectDerivedProperty_isTriangulated` (triangulated) and `perfectDerivedProperty_isSaturated` (saturated)”.

> **Stacks Project, Tag 0FDG (1).** The *Grothendieck group* `K₀(X)` of a scheme `X`: the
> zeroth `K`-group of the strictly full, saturated, triangulated subcategory `D_perf(𝒪_X)` of
> `D(𝒪_X)` consisting of the perfect objects.

```lean
abbrev PerfectKZero (X : Scheme.{u}) : Type _
```

## Tag 0FDH, a lemma

[Tag 0FDH](https://stacks.math.columbia.edu/tag/0FDH) in the Stacks Project.

**`Stacks.AlgebraicGeometry.GrothendieckGroupAffine.affineCoherentKZeroEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupAffine/Basic.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupAffine/Basic.lean#L325). The attribute's comment: “affine\_k0\_prime”.

> The coherent Grothendieck group of `Spec R` is canonically isomorphic to
> the Grothendieck group of finite `R`-modules.

```lean
def affineCoherentKZeroEquiv (R : Type u) [CommRing R] [IsNoetherianRing R] :
    AlgebraicGeometry.CoherentKZero (Spec (CommRingCat.of R)) ≃+ KPrime0 R
```

**`Stacks.AlgebraicGeometry.GrothendieckGroupAffine.affineCoherentKZeroEquiv_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupAffine/Basic.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupAffine/Basic.lean#L332). The attribute's comment: “affine\_k0\_prime”.

> The affine comparison sends the class of a coherent sheaf associated to a
> finite module to the class of that module.

```lean
theorem affineCoherentKZeroEquiv_mk (R : Type u) [CommRing R] [IsNoetherianRing R]
    (M : FinModule R)
    (F : Stacks.SheafOfModules.CoherentModules (Spec (CommRingCat.of R)).ringCatSheaf)
    (hF : Nonempty (F.obj ≅
      AlgebraicGeometry.tilde (ModuleCat.of (CommRingCat.of R) M.carrier))) :
    affineCoherentKZeroEquiv R (KZero.mk _ F) = M.cls
```

**`Stacks.AlgebraicGeometry.GrothendieckGroupAffine.exists_addEquiv_K0_perfectDerivedCategory_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupAffine/Perfect.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupAffine/Perfect.lean#L185). The attribute's comment: “affine\_k0”. References: SGA 6 0 (3.1), “special case”; SGA 6 VII (2.6), “special case”.

> **[Stacks, Tag 0FDH], the clause `K₀(Spec R) = K₀(R)`.** For a commutative ring `R` the
> Grothendieck group `K₀(Spec R) = K₀(D_perf(𝒪_{Spec R}))` of the affine scheme `Spec R` is
> isomorphic to the Grothendieck group `K₀(R)` of finite projective `R`-modules, by the
> isomorphism taking the class of a perfect object `K` of `D(𝒪_{Spec R})` which is isomorphic to
> `M̃` to the alternating sum of the classes of the terms of a bounded complex of finite projective
> `R`-modules representing `M`.
>
> `perfEquiv` identifies `D_perf(R)` with `D_perf(𝒪_{Spec R})`,
> `CategoryTheory.Pretriangulated.K0.mapEquiv` turns that into an isomorphism of `K`-groups, and
> `K0.exists_k0_perfectDerivedCategory_addEquiv` ([Stacks, Tag 0FCU]) identifies `K₀(D_perf(R))`
> with `K₀(R)` by the Euler characteristic, which is where the alternating sum comes from.

```lean
theorem exists_addEquiv_K0_perfectDerivedCategory_spec :
    ∃ e : Pretriangulated.K0 (PerfectDerivedCategory (Spec R)) ≃+ K0 (R : Type u),
      ∀ (K : PerfectDerivedCategory (Spec R)) (M : DerivedCategory (ModuleCat.{u} R))
        (Q : CochainComplex (ModuleCat.{u} (R : Type u)) ℤ) (a b : ℤ),
        Q.IsStrictlyGE a → Q.IsStrictlyLE b →
        (hfinite : ∀ i : ℤ, Module.Finite (R : Type u) (Q.X i)) →
        (hprojective : ∀ i : ℤ, Module.Projective (R : Type u) (Q.X i)) →
        Nonempty (M ≅ DerivedCategory.Q.obj Q) →
        Nonempty (K.obj ≅ (tilde.functor R).mapDerivedCategory.obj M) →
        e (Pretriangulated.K0.cls K) = ∑ i ∈ Finset.Icc a b,
          (i.negOnePow : ℤ) • K0.mk
            ({ carrier := Q.X i, finite := hfinite i, projective := hprojective i } :
              FGProj (R : Type u))
```

## Tag 0FDI, a lemma

[Tag 0FDI](https://stacks.math.columbia.edu/tag/0FDI) in the Stacks Project.

**`AlgebraicGeometry.exists_addEquiv_K0_coherentKZero_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RegularKGroupComparison.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/RegularKGroupComparison.lean#L88). References: SGA 6 IV (2.5), “(i), special case”.

> **[Stacks, Tag 0FDI].** Let `X` be a Noetherian regular scheme. Then the canonical map
> `K₀(X) ⟶ K'₀(X)` from the Grothendieck group of perfect complexes to the Grothendieck group of
> coherent sheaves is an isomorphism.
>
> Every coherent sheaf placed in degree zero is a perfect complex, the comparison map takes the
> class of such a complex to the class of the sheaf, and it is the only additive homomorphism
> `K₀(X) ⟶ K'₀(X)` which does so.

```lean
theorem exists_addEquiv_K0_coherentKZero_of_isRegular (X : Scheme.{u}) [IsNoetherian X]
    (hX : IsRegular X) :
    ∃ e : Pretriangulated.K0 (PerfectDerivedCategory X) ≃+ CoherentKZero X,
      (∀ F : Stacks.SheafOfModules.CoherentModules X.ringCatSheaf,
          ∃ K : PerfectDerivedCategory X,
            Nonempty (K.obj ≅ (DerivedCategory.singleFunctor X.Modules 0).obj F.obj)) ∧
        (∀ (F : Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)
            (K : PerfectDerivedCategory X),
            (K.obj ≅ (DerivedCategory.singleFunctor X.Modules 0).obj F.obj) →
              e (Pretriangulated.K0.cls K) = KZero.mk _ F) ∧
          ∀ φ : Pretriangulated.K0 (PerfectDerivedCategory X) →+ CoherentKZero X,
            (∀ (F : Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)
                (K : PerfectDerivedCategory X),
                (K.obj ≅ (DerivedCategory.singleFunctor X.Modules 0).obj F.obj) →
                  φ (Pretriangulated.K0.cls K) = KZero.mk _ F) → φ = e.toAddMonoidHom
```

## Tag 0FDJ, a lemma

[Tag 0FDJ](https://stacks.math.columbia.edu/tag/0FDJ) in the Stacks Project.

**`Stacks.Perfect.BoundedLocallyFreeComplexes.bijective_comparisonAddHom_of_hasResolutionProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/VectorBundleComparisonBijectiveUnconditional.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/VectorBundleComparisonBijectiveUnconditional.lean#L143). References: SGA 6 0 (3.1), “more general”.

> **Stacks Project, Tag 0FDJ.**  On a quasi-compact and quasi-separated scheme with the
> resolution property the canonical homomorphism `K₀(Vect(X)) ⟶ K₀(X) = K₀(D_perf(𝒪_X))`, which
> sends the class of a finite locally free `𝒪_X`-module to the class of that module placed in
> degree zero, is an isomorphism: it is bijective, and it is a homomorphism of abelian groups by
> construction.
>
> Surjectivity is
> `Stacks.Perfect.BoundedLocallyFreeComplexes.surjective_comparisonAddHom`, which reads off the
> class of a bounded complex of finite locally free modules as the alternating sum of the classes
> of its terms.  Injectivity is the source's inverse map, the Euler characteristic
> `Σᵢ (-1)ⁱ [ℰⁱ]`; it is well defined because two bounded complexes of finite locally free modules
> isomorphic in `D(𝒪_X)` are connected by a roof of such complexes ([Stacks, Tag 0F8G]) and because
> the Euler characteristic of a bounded acyclic such complex vanishes, the modules of cycles being
> finite locally free.
>
> The affine diagonal that both halves need is [Stacks, Tag 0F8C] at these same three conditions,
> `AlgebraicGeometry.HasResolutionProperty.isAffineHom_diagonal`.

```lean
theorem bijective_comparisonAddHom_of_hasResolutionProperty (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] [HasResolutionProperty X] :
    Function.Bijective (comparisonAddHom X)
```

**`Stacks.Perfect.BoundedLocallyFreeComplexes.surjective_comparisonAddHom_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/VectorBundleComparisonSurjective.lean, line 577](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/VectorBundleComparisonSurjective.lean#L577). The attribute's comment: “surjectivity of `K₀(Vect(X)) ⟶ K₀(X)`, for a Noetherian scheme in place of an arbitrary quasi-compact one: the affine diagonal that the proof needs is deduced from the resolution property by the Noetherian case of Tag 0F8C”. References: SGA 6 IV (2.9), “(i)”.

> **The surjectivity half of [Stacks, Tag 0FDJ].** On a Noetherian, quasi-separated scheme with
> the resolution property the canonical homomorphism `K₀(Vect(X)) ⟶ K₀(X) = K₀(D_perf(𝒪_X))`, which
> sends the class of a finite locally free `𝒪_X`-module to the class of that module placed in
> degree zero, is surjective.
>
> The scheme has affine diagonal by the Noetherian case of [Stacks, Tag 0F8C],
> `AlgebraicGeometry.isAffineHom_diagonal_of_hasResolutionProperty_of_isNoetherian`, so
> `Stacks.Perfect.BoundedLocallyFreeComplexes.exists_boundedFiniteLocallyFree_iso_of_affineDiagonal`
> — [Stacks, Tag 0F8F] with the affine diagonal assumed rather than deduced — writes every perfect
> object of `D(𝒪_X)` as the image of a bounded complex of finite locally free modules. That is the
> hypothesis of `Stacks.Perfect.BoundedLocallyFreeComplexes.surjective_comparisonAddHom`, which
> reads off the class of such a complex as the alternating sum of the classes of its terms.
>
> The whole tag, on a quasi-compact and quasi-separated scheme with the resolution property and
> with the comparison homomorphism an isomorphism, is
> `Stacks.Perfect.BoundedLocallyFreeComplexes.bijective_comparisonAddHom_of_hasResolutionProperty`
> of `StacksFrontier.AlgebraicGeometry.Perfect.VectorBundleComparisonBijectiveUnconditional`.

```lean
theorem surjective_comparisonAddHom_of_isNoetherian (X : Scheme.{u})
    [AlgebraicGeometry.IsNoetherian X] [QuasiSeparatedSpace X]
    [AlgebraicGeometry.HasResolutionProperty X] :
    Function.Surjective (comparisonAddHom X)
```

## Tag 0FDK, a remark

[Tag 0FDK](https://stacks.math.columbia.edu/tag/0FDK) in the Stacks Project.

**`AlgebraicGeometry.derivedCategoryBBounded_coherentModules_derivedTensor_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/CoherentKGroupModule.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/CoherentKGroupModule.lean#L127). The attribute's comment: “the bifunctor D\_perf × D^b\_Coh ⟶ D^b\_Coh”.

> **Stacks Project, Tag 0FDK.** Let `X` be a Noetherian scheme. The derived tensor product of a
> perfect object of `D(𝒪_X)` with an object of `D^b_Coh(𝒪_X)` is an object of `D^b_Coh(𝒪_X)`: the
> derived tensor product produces the bifunctor
> `⊗^𝐋_{𝒪_X} : D_perf(𝒪_X) × D^b_Coh(𝒪_X) ⟶ D^b_Coh(𝒪_X)`.

```lean
theorem derivedCategoryBBounded_coherentModules_derivedTensor_of_isPerfect
    (K L : DerivedCategory (SheafOfModules.{u} X.ringCatSheaf))
    (hK : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) K)
    (hL : DerivedCategoryB.derivedCategoryBBounded
      (Stacks.SheafOfModules.coherentModules X.ringCatSheaf) L) :
    DerivedCategoryB.derivedCategoryBBounded
      (Stacks.SheafOfModules.coherentModules X.ringCatSheaf)
      (((TorFormula.derivedTensor X).obj K).obj L)
```

**`AlgebraicGeometry.exists_derivedTensorProduct_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/CoherentKGroupModule.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/CoherentKGroupModule.lean#L227). The attribute's comment: “K₀(D^b\_Coh(𝒪\_X)) is a module over the Grothendieck ring K₀(D\_perf(𝒪\_X))”.

> **Stacks Project, Tag 0FDK.** Let `X` be a Noetherian scheme. The zeroth `K`-group
> `K₀(D^b_Coh(𝒪_X))` of the cohomologically bounded objects of `D(𝒪_X)` with coherent cohomology
> sheaves carries a module structure over the Grothendieck ring `K₀(D_perf(𝒪_X))` of the perfect
> objects for which the scalar multiple of the class of an object of `D^b_Coh(𝒪_X)` by the class of
> a perfect object is the class of their derived tensor product. In particular that scalar
> multiplication is bilinear.
>
> The ring acting is the commutative ring of
> `AlgebraicGeometry.RingedSpace.exists_derivedTensorProduct_commRing`
> (`perfectTensorStructureScheme_eq`), and the group acted on is `K'₀(X)` by
> [Stacks, Tag 0FDF].

```lean
theorem exists_derivedTensorProduct_module :
    letI := (perfectTensorStructureScheme X).commRing
    ∃ m : Module (K0 (perfectAtScheme X).FullSubcategory)
        (K0 (boundedCoherentAtScheme X).FullSubcategory),
      ∀ (K L : DerivedCategory (SheafOfModules.{u} X.ringCatSheaf))
        (hK : perfectAtScheme X K) (hL : boundedCoherentAtScheme X L)
        (h : boundedCoherentAtScheme X (((TorFormula.derivedTensor X).obj K).obj L)),
        letI := m
        K0.cls (⟨K, hK⟩ : (perfectAtScheme X).FullSubcategory) •
            K0.cls (⟨L, hL⟩ : (boundedCoherentAtScheme X).FullSubcategory) =
          K0.cls (⟨((TorFormula.derivedTensor X).obj K).obj L, h⟩ :
            (boundedCoherentAtScheme X).FullSubcategory)
```

**`AlgebraicGeometry.exists_module_coherentKZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/CoherentKGroupModule.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/CoherentKGroupModule.lean#L254). The attribute's comment: “K'₀(X) is a module over the Grothendieck ring K₀(X)”. References: SGA 6 IV (3.2.3).

> **Stacks Project, Tag 0FDK.** Let `X` be a Noetherian scheme. The Grothendieck group
> `K'₀(X)` of coherent `𝒪_X`-modules is a module over the Grothendieck ring
> `K₀(X) = K₀(D_perf(𝒪_X))`: there is a module structure on `K'₀(X)` and an isomorphism of abelian
> groups `K'₀(X) ≅ K₀(D^b_Coh(𝒪_X))` which takes the class of a coherent module to the class of
> that module placed in degree zero — the isomorphism of [Stacks, Tag 0FDF] — and which carries the
> scalar multiple of the class of a coherent sheaf `ℱ` by the class of a perfect object `K` to the
> class of their derived tensor product `K ⊗^𝐋_{𝒪_X} ℱ[0]`.

```lean
theorem exists_module_coherentKZero :
    letI := (perfectTensorStructureScheme X).commRing
    ∃ (m : Module (K0 (perfectAtScheme X).FullSubcategory) (CoherentKZero X))
      (e : CoherentKZero X ≃+ K0 (boundedCoherentAtScheme X).FullSubcategory),
      (∀ F : Stacks.SheafOfModules.CoherentModules X.ringCatSheaf,
          ∃ K : (boundedCoherentAtScheme X).FullSubcategory,
            Nonempty (K.obj ≅ (DerivedCategory.singleFunctor
              (SheafOfModules.{u} X.ringCatSheaf) 0).obj F.obj)) ∧
      (∀ (F : Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)
          (K : (boundedCoherentAtScheme X).FullSubcategory),
          (K.obj ≅ (DerivedCategory.singleFunctor
              (SheafOfModules.{u} X.ringCatSheaf) 0).obj F.obj) →
            e (KZero.mk _ F) = K0.cls K) ∧
      ∀ (K : (perfectAtScheme X).FullSubcategory)
        (F : Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)
        (L : (boundedCoherentAtScheme X).FullSubcategory)
        (_ : L.obj ≅ (DerivedCategory.singleFunctor
          (SheafOfModules.{u} X.ringCatSheaf) 0).obj F.obj)
        (h : boundedCoherentAtScheme X (((TorFormula.derivedTensor X).obj K.obj).obj L.obj)),
        letI := m
        e (K0.cls K • KZero.mk _ F) =
          K0.cls (⟨((TorFormula.derivedTensor X).obj K.obj).obj L.obj, h⟩ :
            (boundedCoherentAtScheme X).FullSubcategory)
```

**`AlgebraicGeometry.RingedSpace.exists_derivedTensorProduct_commRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectKGroupRing.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PerfectKGroupRing.lean#L187). The attribute's comment: “perfect\_k\_ring”. References: SGA 6 IV (2.7), “b) ring str. on K'”.

> **Stacks Project, Tag 0FDK.** The Grothendieck group `K₀(D_perf(𝒪_X))` of the perfect
> objects of `D(𝒪_X)` carries a commutative ring structure whose additive group is the one it
> already has, whose product of the classes of two perfect objects is the class of their derived
> tensor product, and whose unit is the class of the structure sheaf in degree zero.
>
> The source states this for a scheme; it holds for any ringed space, and for an arbitrary
> derived tensor product of `𝒪_X`-modules, which is the generality Tag 09J5 is stated in.

```lean
theorem exists_derivedTensorProduct_commRing :
    ∃ r : CommRing (K0 (ObjectProperty.FullSubcategory
        (Stacks.Cohomology.PerfectComplexes.IsPerfect.{u, u, d} (X := X)))),
      r.toAddCommGroup = (inferInstance : AddCommGroup (K0 (ObjectProperty.FullSubcategory
        (Stacks.Cohomology.PerfectComplexes.IsPerfect.{u, u, d} (X := X))))) ∧
      (∀ (K L : ObjectProperty.FullSubcategory
            (Stacks.Cohomology.PerfectComplexes.IsPerfect.{u, u, d} (X := X)))
          (h : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X)
            ((T.tensor.obj K.obj).obj L.obj)),
        r.mul (K0.cls K) (K0.cls L) = K0.cls ⟨(T.tensor.obj K.obj).obj L.obj, h⟩) ∧
      (∀ h : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X)
          ((DerivedCategory.Q (C := Mod X.sheaf)).obj
            ((CochainComplex.singleFunctor (Mod X.sheaf) 0).obj
              (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} X.sheaf)))),
        r.one = K0.cls ⟨_, h⟩)
```

**`AlgebraicGeometry.existsUnique_comparisonRingHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/VectorBundleComparison.lean, line 321](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/VectorBundleComparison.lean#L321). The attribute's comment: “vector\_bundle\_comparison\_ring\_map”. References: SGA 6 IV (2.7), “b) K'\_naif→K' ring”.

> There is a unique ring homomorphism from the Grothendieck ring of vector bundles on a scheme
> `X` to the Grothendieck ring of perfect objects of `D(𝒪_X)` which sends the class of a finite
> locally free module to the class of that module placed in degree zero.
>
> The ring structure on the target is the one of
> `AlgebraicGeometry.RingedSpace.exists_derivedTensorProduct_commRing`, for the given derived
> tensor product.

```lean
theorem existsUnique_comparisonRingHom :
    letI := (RingedSpace.perfectTensorStructure X.toRingedSpace T).commRing
    ∃! f : VectorBundleKZero X →+*
        K0 (ObjectProperty.FullSubcategory
          (Stacks.Cohomology.PerfectComplexes.IsPerfect.{u, u, d} (X := X.toRingedSpace))),
      ∀ (M : X.Modules) (_ : IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) M)
        (h : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace)
          ((DerivedCategory.singleFunctor X.Modules 0).obj M)),
        f (VectorBundleKZero.classOf X M) = K0.cls ⟨_, h⟩
```

**`AlgebraicGeometry.VectorBundleKZero.exists_tensorProduct_commRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/VectorBundleKGroup.lean, line 588](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/VectorBundleKGroup.lean#L588). The attribute's comment: “vector\_bundle\_grothendieck\_ring”. References: SGA 6 IV (2.7), “b) K'\_naif ring str.”.

> **Stacks Project, Tag 0FDK.** `K₀(Vect(X))` carries a commutative ring structure whose
> additive group is the one it already has, whose multiplication is the tensor product of finite
> locally free modules, and whose unit is the class of the structure sheaf.

```lean
theorem exists_tensorProduct_commRing (X : Scheme.{u}) :
    ∃ r : CommRing (VectorBundleKZero X),
      r.toAddCommGroup = (inferInstance : AddCommGroup (VectorBundleKZero X)) ∧
        (∀ M N : X.Modules, IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) M →
          IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) N →
            r.mul (classOf X M) (classOf X N) =
              classOf X (Scheme.Modules.tensorObjRingedSpace X M N)) ∧
        classOf X (SheafOfModules.unit X.ringCatSheaf) = r.one
```

## Tag 0FDL, a remark

[Tag 0FDL](https://stacks.math.columbia.edu/tag/0FDL) in the Stacks Project.

**`AlgebraicGeometry.ProperPushforwardKZero.properPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupProperPushforward.lean, line 611](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupProperPushforward.lean#L611). The attribute's comment: “the map f\_* : K'₀(X) ⟶ K'₀(Y). All three of the source's reasons for well definedness are proved: coherence of the R ⁱ f\_* ℱ (Tag 02O5), local finiteness of the nonzero ones, and the long exact sequence of the R ⁱ f\_* with its terms collected by the parity of the degree (`hasParityHexagons`). The remark's quasi-compact restatement f\_*[ℱ] = ∑ (-1)ⁱ [R ⁱ f\_* ℱ] = [Rf\_* ℱ] is `AlgebraicGeometry.ProperPushforwardKZero.properPushforward_mk_eq_finsum` and `AlgebraicGeometry.ProperPushforwardKZero.properPushforward_mk_eq_derivedClass`”. References: SGA 6 0 (3.1); SGA 6 X (1.1.8).

> **[Stacks, Tag 0FDL]: proper pushforward on `K'₀`.** For a proper morphism `f : X ⟶ Y` of
> locally Noetherian schemes, the homomorphism `f_* : K'₀(X) ⟶ K'₀(Y)` of Grothendieck groups of
> coherent sheaves determined by `f_*[ℱ] = [⨁_{i ≥ 0} R ²ⁱ f_* ℱ] − [⨁_{i ≥ 0} R ²ⁱ⁺¹ f_* ℱ]`.
>
> Its existence is `KZero.lift` applied to `parityClass_add_of_shortExact`; the coherence of the
> two sums, which is what makes the right-hand side a difference of classes in `K'₀(Y)`, is
> `isCoherent_parityDirectImageSum`.

```lean
def properPushforward (f : X ⟶ Y) [IsLocallyNoetherian X] [IsLocallyNoetherian Y] [IsProper f] :
    CoherentKZero X →+ CoherentKZero Y
```

**`AlgebraicGeometry.ProperPushforwardKZero.properPushforward_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupProperPushforward.lean, line 621](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupProperPushforward.lean#L621). The attribute's comment: “the value f\_*[ℱ] = [⨁ R ²ⁱ f\_* ℱ] - [⨁ R ²ⁱ⁺¹ f\_* ℱ] of f\_* on the class of a coherent sheaf, the first assertion of the remark”.

> **[Stacks, Tag 0FDL]: the value of `f_*` on the class of a coherent sheaf.** For coherent
> `𝒪_Y`-modules `E` and `O` isomorphic to `⨁_{i ≥ 0} R ²ⁱ f_* ℱ` and `⨁_{i ≥ 0} R ²ⁱ⁺¹ f_* ℱ`,
>
>   `f_*[ℱ] = [E] − [O]`.

```lean
theorem properPushforward_mk (f : X ⟶ Y) [IsLocallyNoetherian X] [IsLocallyNoetherian Y]
    [IsProper f]
    (F : Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)
    (E O : Stacks.SheafOfModules.CoherentModules Y.ringCatSheaf)
    (hE : E.obj ≅ parityDirectImageSum f F.obj 0)
    (hO : O.obj ≅ parityDirectImageSum f F.obj 1) :
    properPushforward f (KZero.mk _ F) = KZero.mk _ E - KZero.mk _ O
```

**`AlgebraicGeometry.ProperPushforwardKZero.existsUnique_properPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupProperPushforward.lean, line 645](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupProperPushforward.lean#L645). The attribute's comment: “the existence and uniqueness of the map f\_* : K'₀(X) ⟶ K'₀(Y) with the value the remark prescribes on the class of a coherent sheaf”.

> **[Stacks, Tag 0FDL].** For a proper morphism `f : X ⟶ Y` of locally Noetherian schemes there
> is exactly one homomorphism `f_* : K'₀(X) ⟶ K'₀(Y)` with
>
>   `f_*[ℱ] = [⨁_{i ≥ 0} R ²ⁱ f_* ℱ] − [⨁_{i ≥ 0} R ²ⁱ⁺¹ f_* ℱ]`
>
> for every coherent `𝒪_X`-module `ℱ`, the two sums being read at any coherent `𝒪_Y`-modules
> isomorphic to them.

```lean
theorem existsUnique_properPushforward (f : X ⟶ Y) [IsLocallyNoetherian X]
    [IsLocallyNoetherian Y] [IsProper f] :
    ∃! φ : CoherentKZero X →+ CoherentKZero Y,
      ∀ (F : Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)
        (E O : Stacks.SheafOfModules.CoherentModules Y.ringCatSheaf),
        (E.obj ≅ parityDirectImageSum f F.obj 0) →
        (O.obj ≅ parityDirectImageSum f F.obj 1) →
          φ (KZero.mk _ F) = KZero.mk _ E - KZero.mk _ O
```

**`AlgebraicGeometry.ProperPushforwardKZero.properPushforward_mk_eq_finsum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupProperPushforwardDerived.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupProperPushforwardDerived.lean#L284). The attribute's comment: “the quasi-compact restatement f\_*[ℱ] = ∑ (-1)ⁱ [R ⁱ f\_* ℱ] of the remark”.

> **[Stacks, Tag 0FDL]: the quasi-compact restatement `f_*[ℱ] = ∑ (−1)ⁱ [R ⁱ f_* ℱ]`.** For a
> proper morphism `f : X ⟶ Y` of locally Noetherian schemes with `Y` quasi-compact, the proper
> pushforward of the class of a coherent `𝒪_X`-module is the alternating sum of the classes of its
> higher direct images; the sum is finite because they vanish in all large degrees.
>
> The value of `f_*` on `[ℱ]` is `[⨁_{i ≥ 0} R ²ⁱ f_* ℱ] − [⨁_{i ≥ 0} R ²ⁱ⁺¹ f_* ℱ]`
> (`properPushforward_mk`); each of the two sums has only finitely many nonzero summands by
> `exists_isZero_higherDirectImage_of_compactSpace`, so `mk_eq_sum_range_of_iso_sigma` expands its
> class as a finite sum, and `alternating_sum_range` recombines the two finite sums by parity.

```lean
theorem properPushforward_mk_eq_finsum (f : X ⟶ Y) [IsLocallyNoetherian X]
    [IsLocallyNoetherian Y] [IsProper f] [CompactSpace Y]
    (F : Stacks.SheafOfModules.CoherentModules X.ringCatSheaf) :
    properPushforward f (KZero.mk _ F) =
      ∑ᶠ i : ℕ, ((i : ℤ).negOnePow : ℤ) • KZero.mk _ (coherentHigherDirectImage f F i)
```

**`AlgebraicGeometry.ProperPushforwardKZero.properPushforward_mk_eq_derivedClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupProperPushforwardDerived.lean, line 656](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupProperPushforwardDerived.lean#L656). The attribute's comment: “the quasi-compact restatement f\_*[ℱ] = [Rf\_* ℱ] of the remark, under the identification K'₀(Y) = K₀(D^b\_Coh(𝒪\_Y)) of Tag 0FDF”.

> **[Stacks, Tag 0FDL]: the quasi-compact restatement `f_*[ℱ] = [Rf_* ℱ]`.** For a proper
> morphism `f : X ⟶ Y` of locally Noetherian schemes with `Y` quasi-compact and a coherent
> `𝒪_X`-module `ℱ`, the total derived direct image `Rf_*(ℱ[0])` is an object of `D^b_Coh(𝒪_Y)`, and
> under every identification `K'₀(Y) = K₀(D^b_Coh(𝒪_Y))` which sends the class of a coherent sheaf
> to the class of that sheaf placed in degree `0` — the identification of [Stacks, Tag 0FDF] —
> the class `f_*[ℱ]` is the class of `Rf_*(ℱ[0])`.
>
> The identity `f_*[ℱ] = ∑ (−1)ⁱ [R ⁱ f_* ℱ]` is `properPushforward_mk_eq_finsum`, and
> `∑ (−1)ⁱ [H ⁱ(K)] ↦ [K]` is the inverse of the identification: the homomorphism `φ` of
> [Stacks, Tag 0FCR] for the zeroth homology functor takes `[K]` to `∑ (−1)ⁱ [H ⁱ(K)]`, and the
> composite of the identification with `φ` is the identity on the classes of coherent sheaves,
> hence the identity.

```lean
theorem properPushforward_mk_eq_derivedClass (f : X ⟶ Y) [IsLocallyNoetherian X]
    [IsLocallyNoetherian Y] [IsProper f] [CompactSpace Y]
    (F : Stacks.SheafOfModules.CoherentModules X.ringCatSheaf) :
    ∃ E : (DerivedCategoryB.derivedCategoryBBounded
        (Stacks.SheafOfModules.coherentModules Y.ringCatSheaf)).FullSubcategory,
      Nonempty (E.obj ≅ (derivedPushforwardModules f).obj
          ((DerivedCategory.singleFunctor X.Modules 0).obj F.obj)) ∧
        ∀ e : CoherentKZero Y ≃+ Pretriangulated.K0 (DerivedCategoryB.derivedCategoryBBounded
            (Stacks.SheafOfModules.coherentModules Y.ringCatSheaf)).FullSubcategory,
          (∀ (G : Stacks.SheafOfModules.CoherentModules Y.ringCatSheaf)
              (D : (DerivedCategoryB.derivedCategoryBBounded
                (Stacks.SheafOfModules.coherentModules Y.ringCatSheaf)).FullSubcategory),
              (D.obj ≅ (DerivedCategory.singleFunctor
                (SheafOfModules.{u} Y.ringCatSheaf) 0).obj G.obj) →
                e (KZero.mk _ G) = Pretriangulated.K0.cls D) →
            e (properPushforward f (KZero.mk _ F)) = Pretriangulated.K0.cls E
```

**`AlgebraicGeometry.ProperPushforwardKZero.exists_addEquiv_properPushforward_eq_derivedClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupProperPushforwardDerived.lean, line 682](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/GrothendieckGroupProperPushforwardDerived.lean#L682). The attribute's comment: “the quasi-compact restatement f\_*[ℱ] = [Rf\_* ℱ] of the remark, with the identification K'₀(Y) = K₀(D^b\_Coh(𝒪\_Y)) of Tag 0FDF exhibited”.

> **[Stacks, Tag 0FDL]: the quasi-compact restatement `f_*[ℱ] = [Rf_* ℱ]`**, with the
> identification `K'₀(Y) = K₀(D^b_Coh(𝒪_Y))` of [Stacks, Tag 0FDF] exhibited.

```lean
theorem exists_addEquiv_properPushforward_eq_derivedClass (f : X ⟶ Y) [IsLocallyNoetherian X]
    [IsLocallyNoetherian Y] [IsProper f] [CompactSpace Y] :
    ∃ e : CoherentKZero Y ≃+ Pretriangulated.K0 (DerivedCategoryB.derivedCategoryBBounded
        (Stacks.SheafOfModules.coherentModules Y.ringCatSheaf)).FullSubcategory,
      (∀ (G : Stacks.SheafOfModules.CoherentModules Y.ringCatSheaf)
          (D : (DerivedCategoryB.derivedCategoryBBounded
            (Stacks.SheafOfModules.coherentModules Y.ringCatSheaf)).FullSubcategory),
          (D.obj ≅ (DerivedCategory.singleFunctor
            (SheafOfModules.{u} Y.ringCatSheaf) 0).obj G.obj) →
            e (KZero.mk _ G) = Pretriangulated.K0.cls D) ∧
        ∀ F : Stacks.SheafOfModules.CoherentModules X.ringCatSheaf,
          ∃ E : (DerivedCategoryB.derivedCategoryBBounded
              (Stacks.SheafOfModules.coherentModules Y.ringCatSheaf)).FullSubcategory,
            Nonempty (E.obj ≅ (derivedPushforwardModules f).obj
                ((DerivedCategory.singleFunctor X.Modules 0).obj F.obj)) ∧
              e (properPushforward f (KZero.mk _ F)) = Pretriangulated.K0.cls E
```

## Tag 0FDM, a lemma

[Tag 0FDM](https://stacks.math.columbia.edu/tag/0FDM) in the Stacks Project.

**`AlgebraicGeometry.properPushforward_perfectCoherentSMul_perfectPullbackKZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProjectionFormulaKZero/ProjectionFormula.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/ProjectionFormulaKZero/ProjectionFormula.lean#L153).

> **[Stacks, Tag 0FDM]: the projection formula on `K`-groups.** Let `f : X ⟶ Y` be a proper
> morphism of locally Noetherian schemes. Then
>
>   `f_*(α · f^*β) = f_*α · β`
>
> for `α ∈ K'₀(X)` and `β ∈ K₀(Y)`. Here `f_* : K'₀(X) ⟶ K'₀(Y)` is the proper pushforward of
> [Stacks, Tag 0FDL] (`AlgebraicGeometry.ProperPushforwardKZero.properPushforward`),
> `f^* : K₀(Y) ⟶ K₀(X)` is induced by the derived pullback of perfect objects
> (`AlgebraicGeometry.RingedSpace.perfectPullbackKZero`), and `K₀(X) × K'₀(X) ⟶ K'₀(X)` is the
> product of [Stacks, Tag 0FDK] given by the derived tensor product
> (`AlgebraicGeometry.ParityEulerClass.perfectCoherentSMul`); on a Noetherian scheme that product is
> the scalar multiplication of the module structure of
> `AlgebraicGeometry.exists_module_coherentKZero`
> (`AlgebraicGeometry.ParityEulerClass.perfectCoherentSMul_eq_smul`).
>
> Both sides are biadditive, so it suffices to treat `α = [ℱ]` and `β = [P]`, which is
> `AlgebraicGeometry.ParityEulerClass.properPushforward_perfectCoherentSMul_cls_mk`: the derived
> projection formula `Rf_*(ℱ ⊗^𝐋 Lf^*P) ≅ Rf_*ℱ ⊗^𝐋 P` of [Stacks, Tag 08EU], here at a perfect
> object `P` where it is [Stacks, Tag 0B54], read through the identification `f_*[ℱ] = [Rf_*ℱ]` of
> Remark 0FDL and the definition of the product in Remark 0FDK.

```lean
theorem properPushforward_perfectCoherentSMul_perfectPullbackKZero {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsLocallyNoetherian X] [IsLocallyNoetherian Y] [IsProper f]
    (α : CoherentKZero X) (β : PerfectKZero Y) :
    ProperPushforwardKZero.properPushforward f
        (perfectCoherentSMul X (RingedSpace.perfectPullbackKZero f.toLRSHom.toShHom β) α) =
      perfectCoherentSMul Y β (ProperPushforwardKZero.properPushforward f α)
```

## Tag 0FDN, a remark

[Tag 0FDN](https://stacks.math.columbia.edu/tag/0FDN) in the Stacks Project.

**`AlgebraicGeometry.supportedPerfectDerivedCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/KGroups/Basic.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/KGroups/Basic.lean#L62). The attribute's comment: “supported\_perfect\_definition”.

> The strictly full subcategory of perfect derived objects whose every cohomology sheaf
> is set-theoretically supported on a closed subscheme.

```lean
public abbrev supportedPerfectDerivedCategory {X Z : Scheme.{u}} (i : Z ⟶ X)
    [IsClosedImmersion i] [HasDerivedCategory.{d} (OXMod.{u} X.toRingedSpace)]
```

**`AlgebraicGeometry.isClosedUnderIsomorphisms_supportedPerfect`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/KGroups/Basic.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/KGroups/Basic.lean#L81). The attribute's comment: “strict fullness of the supported perfect subcategory”.

> **Supported perfect objects form a strictly full subcategory.** Perfectness only depends on
> the isomorphism class, and an isomorphism of derived objects induces an isomorphism of each
> cohomology sheaf, which has no effect on its support.

```lean
instance isClosedUnderIsomorphisms_supportedPerfect {X Z : Scheme.{u}} (i : Z ⟶ X)
    [IsClosedImmersion i] [HasDerivedCategory.{d} (OXMod.{u, u} X.toRingedSpace)] :
    ObjectProperty.IsClosedUnderIsomorphisms
      (show ObjectProperty (DerivedCategory (OXMod.{u, u} X.toRingedSpace)) from
        fun K => RingedSpace.IsPerfect K ∧
          ∀ n : ℤ, SheafOfModules.supp
            ((DerivedCategory.homologyFunctor (OXMod.{u, u} X.toRingedSpace) n).obj K) ⊆
              Set.range i.base)
```

**`AlgebraicGeometry.isTriangulated_supportedPerfect`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/KGroups/Basic.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/KGroups/Basic.lean#L103). The attribute's comment: “triangulatedness of the supported perfect subcategory”. References: SGA 6 I (5.8.4), “5.8.4 a), special case”.

> **Perfect complexes supported on a closed subscheme form a triangulated subcategory** of the
> derived category of `O_X`-modules: the subcategory `D_{Z, perf}(O_X)` contains a zero object, is
> stable under all shifts, and the middle object of a distinguished triangle whose other two
> objects are perfect and supported on `Z` is again perfect and supported on `Z`.
>
> Saturation, the remaining adjective of the source, is
> `AlgebraicGeometry.isSaturated_supportedPerfect`; its perfect half is Tag 08CS.

```lean
instance isTriangulated_supportedPerfect {X Z : Scheme.{u}} (i : Z ⟶ X)
    [IsClosedImmersion i] [HasDerivedCategory.{d} (OXMod.{u, u} X.toRingedSpace)] :
    ObjectProperty.IsTriangulated
      (show ObjectProperty (DerivedCategory (OXMod.{u, u} X.toRingedSpace)) from
        fun K => RingedSpace.IsPerfect K ∧
          ∀ n : ℤ, SheafOfModules.supp
            ((DerivedCategory.homologyFunctor (OXMod.{u, u} X.toRingedSpace) n).obj K) ⊆
              Set.range i.base)
```

**`AlgebraicGeometry.exists_supportedPerfect_not_exists_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/KGroups/NoUnit.lean, line 583](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/KGroups/NoUnit.lean#L583). The attribute's comment: “in general `K_0(D_{Z, perf}(O_X))` has no unit: for `X = Spec ℤ` and `Z = Spec(ℤ/2)` the multiplication given by the derived tensor product exists, and no multiplication on `K_0(D_{Z, perf}(O_X))` distributive over its addition and computing the derived tensor product on classes has a unit”.

> **In general `K₀(D_{Z, perf}(𝒪_X))` has no unit.** There are a scheme `X` and a closed
> subscheme `Z` for which `K₀(D_{Z, perf}(𝒪_X))` carries a multiplication — a non-unital
> commutative ring structure on its additive group whose product of two classes is the class of
> the derived tensor product — and no multiplication of that kind has a unit. Here `X = Spec ℤ` and
> `Z = Spec(ℤ/2)`; the general statement is
> `AlgebraicGeometry.SupportedPerfectNoUnit.not_exists_unit`, for `V(f)` in the spectrum of any
> Noetherian domain of dimension at most one and any nonzero nonunit `f`.

```lean
theorem exists_supportedPerfect_not_exists_unit :
    ∃ (X Z : Scheme.{u}) (i : Z ⟶ X) (_ : IsClosedImmersion i),
      (∃ r : NonUnitalCommRing (K0 (supportedPerfectDerivedCategory i)),
        r.toAddCommGroup = (inferInstance : AddCommGroup (K0 (supportedPerfectDerivedCategory i))) ∧
          ∀ K L : supportedPerfectDerivedCategory i,
            r.mul (K0.cls K) (K0.cls L) = K0.cls (supportedPerfectTensorObj i K L)) ∧
      ∀ r : NonUnitalCommRing (K0 (supportedPerfectDerivedCategory i)),
        r.toAddCommGroup = (inferInstance : AddCommGroup (K0 (supportedPerfectDerivedCategory i))) →
          (∀ K L : supportedPerfectDerivedCategory i,
            r.mul (K0.cls K) (K0.cls L) = K0.cls (supportedPerfectTensorObj i K L)) →
          ¬ ∃ e, ∀ a, r.mul e a = a
```

**`AlgebraicGeometry.exists_supportedPerfect_nonUnitalCommRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/KGroups/Ring.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/KGroups/Ring.lean#L273). The attribute's comment: “the multiplication on `K_0(D_{Z, perf}(O_X))` given by the derived tensor product, together with its associativity and commutativity -- the fields of `NonUnitalCommRing`. Stated at the standard derived-category model, which the source does not fix. The absence of a unit in general is `AlgebraicGeometry.exists_supportedPerfect_not_exists_unit`; the definition of the subcategory and its three adjectives are in `StacksFrontier/AlgebraicGeometry/Perfect/KGroups/Basic.lean` and `StacksFrontier/AlgebraicGeometry/Perfect/KGroups/Saturation.lean`”.

> **Stacks Project, Tag 0FDN.** The `K`-group `K₀(D_{Z, perf}(𝒪_X))` of the perfect objects
> of `D(𝒪_X)` supported on a closed subscheme `Z` carries a non-unital commutative ring
> structure: its additive group is the one `K₀` already has, and the product of the classes of
> two objects is the class of their derived tensor product. Associativity,
> commutativity and distributivity are the fields of `NonUnitalCommRing`; no unit is asserted,
> and none exists in general: `AlgebraicGeometry.exists_supportedPerfect_not_exists_unit`.

```lean
theorem exists_supportedPerfect_nonUnitalCommRing :
    ∃ r : NonUnitalCommRing (K0 (supportedPerfectDerivedCategory i)),
      r.toAddCommGroup = (inferInstance : AddCommGroup (K0 (supportedPerfectDerivedCategory i))) ∧
        ∀ K L : supportedPerfectDerivedCategory i,
          r.mul (K0.cls K) (K0.cls L) = K0.cls (supportedPerfectTensorObj i K L)
```

**`AlgebraicGeometry.isSaturated_supportedPerfect`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/KGroups/Saturation.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/KGroups/Saturation.lean#L69). The attribute's comment: “saturation of the supported perfect subcategory -- the adjective `saturated` of the source, which is closure under direct summands (Tag 05RB). The two other adjectives, strict fullness and triangulatedness, and the definition of the subcategory itself, are in `StacksFrontier/AlgebraicGeometry/Perfect/KGroups/Basic.lean`. The multiplication on `K_0(D_{Z, perf}(O_X))` is in `StacksFrontier/AlgebraicGeometry/Perfect/KGroups/Ring.lean` and the absence of a unit in general in `StacksFrontier/AlgebraicGeometry/Perfect/KGroups/NoUnit.lean`”.

> **Perfect complexes supported on a closed subscheme form a saturated subcategory** of
> `D(O_X)`: if a binary biproduct is perfect with all its cohomology sheaves supported on `Z`,
> then so is each of its two summands.
>
> Together with `AlgebraicGeometry.isClosedUnderIsomorphisms_supportedPerfect` and
> `AlgebraicGeometry.isTriangulated_supportedPerfect` this gives all three adjectives the source
> attaches to `D_{Z, perf}(O_X)`: strictly full, saturated, triangulated.

```lean
instance isSaturated_supportedPerfect {X Z : Scheme.{u}} (i : Z ⟶ X)
    [IsClosedImmersion i] [HasDerivedCategory.{d} (OXMod.{u, u} X.toRingedSpace)] :
    ObjectProperty.IsSaturated
      (show ObjectProperty (DerivedCategory (OXMod.{u, u} X.toRingedSpace)) from
        fun K => RingedSpace.IsPerfect K ∧
          ∀ n : ℤ, SheafOfModules.supp
            ((DerivedCategory.homologyFunctor (OXMod.{u, u} X.toRingedSpace) n).obj K) ⊆
              Set.range i.base)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.38, Tag 0FDE](https://stacks.math.columbia.edu/tag/0FDE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
