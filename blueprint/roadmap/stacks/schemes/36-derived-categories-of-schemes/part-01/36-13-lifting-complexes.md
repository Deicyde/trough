---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_quasicoherentDerived_lift, AlgebraicGeometry.exists_quasicoherentDerived_plus_lift, AlgebraicGeometry.exists_quasicoherentDerived_minus_lift, AlgebraicGeometry.exists_quasicoherentDerived_bounded_lift, AlgebraicGeometry.essSurj_coherentDerivedBoundedRestrict, AlgebraicGeometry.exists_boundedAbove_finiteFree_lift, Stacks.DerivedQCoh.exists_pos_subsingleton_hom_singleFunctor_of_isFiniteLocallyFree, Stacks.DerivedQCoh.exists_window_subsingleton_hom_of_isPerfect_qcqs
statement: formalized
proof: formalized
---

# 36.13 Lifting complexes

Section 36.13 of the Stacks Project, [Tag 08EC](https://stacks.math.columbia.edu/tag/08EC). 12 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08ED, a lemma

[Tag 08ED](https://stacks.math.columbia.edu/tag/08ED) in the Stacks Project.

**`AlgebraicGeometry.exists_quasicoherentDerived_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/EssentialSurjectivity.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/EssentialSurjectivity.lean#L129). The attribute's comment: “unbounded derived category”.

> **Stacks Project, Tag 08ED.** Every quasi-coherent derived object on a quasi-compact open
> subscheme extends to a quasi-coherent derived object on the ambient scheme: the functor
> `D_QCoh(𝒪_X) ⟶ D_QCoh(𝒪_U)` given by restriction is essentially surjective.

```lean
theorem exists_quasicoherentDerived_lift (E : QuasicoherentDerivedCategory U) :
    ∃ F : QuasicoherentDerivedCategory X,
      Nonempty ((derivedPullback j.toLRSHom.toShHom).obj F.obj ≅ E.obj)
```

**`AlgebraicGeometry.exists_quasicoherentDerived_plus_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/EssentialSurjectivity.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/EssentialSurjectivity.lean#L141). The attribute's comment: “bounded-below derived category”.

> **Stacks Project, Tag 08ED.** A bounded-below quasi-coherent derived object on a
> quasi-compact open subscheme has a bounded-below quasi-coherent lift: the functor
> `D⁺_QCoh(𝒪_X) ⟶ D⁺_QCoh(𝒪_U)` given by restriction is essentially surjective.
>
> No quasi-compactness of the ambient scheme is needed, the derived direct image preserving a
> lower cohomological bound for an arbitrary morphism of schemes.

```lean
theorem exists_quasicoherentDerived_plus_lift (E : QuasicoherentDerivedCategory U)
    (hE : DerivedCategory.TStructure.t.plus E.obj) :
    ∃ F : QuasicoherentDerivedCategory X,
      DerivedCategory.TStructure.t.plus F.obj ∧
      Nonempty ((derivedPullback j.toLRSHom.toShHom).obj F.obj ≅ E.obj)
```

**`AlgebraicGeometry.exists_quasicoherentDerived_minus_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/EssentialSurjectivity.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/EssentialSurjectivity.lean#L159). The attribute's comment: “bounded-above derived category”.

> **Stacks Project, Tag 08ED.** A bounded-above quasi-coherent derived object on a
> quasi-compact open subscheme of a quasi-compact scheme has a bounded-above quasi-coherent lift:
> the functor `D⁻_QCoh(𝒪_X) ⟶ D⁻_QCoh(𝒪_U)` given by restriction is essentially surjective.
>
> Quasi-compactness of the ambient scheme is what bounds the cohomological dimension of `j`, and
> so bounds the shift by which the derived direct image can raise an upper bound.

```lean
theorem exists_quasicoherentDerived_minus_lift [CompactSpace X]
    (E : QuasicoherentDerivedCategory U) (hE : DerivedCategory.TStructure.t.minus E.obj) :
    ∃ F : QuasicoherentDerivedCategory X,
      DerivedCategory.TStructure.t.minus F.obj ∧
      Nonempty ((derivedPullback j.toLRSHom.toShHom).obj F.obj ≅ E.obj)
```

**`AlgebraicGeometry.exists_quasicoherentDerived_bounded_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/EssentialSurjectivity.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/EssentialSurjectivity.lean#L177). The attribute's comment: “bounded derived category”.

> **Stacks Project, Tag 08ED.** A bounded quasi-coherent derived object on a quasi-compact
> open subscheme of a quasi-compact scheme has a bounded quasi-coherent lift: the functor
> `D^b_QCoh(𝒪_X) ⟶ D^b_QCoh(𝒪_U)` given by restriction is essentially surjective.

```lean
theorem exists_quasicoherentDerived_bounded_lift [CompactSpace X]
    (E : QuasicoherentDerivedCategory U) (hE : DerivedCategory.TStructure.t.bounded E.obj) :
    ∃ F : QuasicoherentDerivedCategory X,
      DerivedCategory.TStructure.t.bounded F.obj ∧
      Nonempty ((derivedPullback j.toLRSHom.toShHom).obj F.obj ≅ E.obj)
```

## Tag 0G48, a lemma

[Tag 0G48](https://stacks.math.columbia.edu/tag/0G48) in the Stacks Project.

**`AlgebraicGeometry.essSurj_coherentDerivedBoundedRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedCoherent/EssSurjRestrictOpen.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedCoherent/EssSurjRestrictOpen.lean#L88).

> **[Stacks, Tag 0G48].** On a Noetherian scheme, restriction to an open subscheme is
> essentially surjective as a functor `D^b_Coh(𝒪_X) ⥤ D^b_Coh(𝒪_U)`: every bounded complex of
> `𝒪_U`-modules with coherent cohomology is the restriction of one on `X`.

```lean
theorem essSurj_coherentDerivedBoundedRestrict {X : Scheme.{u}} [IsNoetherian X] (U : X.Opens) :
    (coherentDerivedBoundedRestrict U).EssSurj
```

## Tag 08EE, a lemma

[Tag 08EE](https://stacks.math.columbia.edu/tag/08EE) in the Stacks Project.

**`AlgebraicGeometry.exists_boundedAbove_finiteFree_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/FiniteFreeComplex.lean, line 1188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/FiniteFreeComplex.lean#L1188).

> A pseudo-coherent derived object on a quasi-compact open of an affine
> scheme is the restriction of a bounded-above complex of finite free modules.

```lean
theorem exists_boundedAbove_finiteFree_lift
    (X : Scheme.{u}) [IsAffine X] (U : X.Opens)
    (hU : IsCompact (U : Set X))
    [HasDerivedCategory.{d} (OXMod.{u} (X.toRingedSpace.restrict U.isOpenEmbedding))]
    (E : DerivedCategory (OXMod.{u} (X.toRingedSpace.restrict U.isOpenEmbedding)))
    (hE : AlgebraicGeometry.RingedSpace.IsPseudoCoherent
      (X := X.toRingedSpace.restrict U.isOpenEmbedding) E) :
    ∃ P : CochainComplex (OXMod.{u} X.toRingedSpace) ℤ,
      (∃ b : ℤ, ∀ i : ℤ, b < i → CategoryTheory.Limits.IsZero (P.X i)) ∧
      (∀ i : ℤ, ∃ I : Type u, Finite I ∧ Nonempty
        (P.X i ≅ SheafOfModules.free (R := structureSheafOfRings X.toRingedSpace) I)) ∧
      Nonempty (DerivedCategory.Q.obj
        (((RingedSpace.restrictModules X.toRingedSpace U).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj P) ≅ E)
```

## Tag 08EF, a lemma

[Tag 08EF](https://stacks.math.columbia.edu/tag/08EF) in the Stacks Project.

**`Stacks.DerivedQCoh.exists_pos_subsingleton_hom_singleFunctor_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/EventualExtVanishing.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/EventualExtVanishing.lean#L589).

> **Stacks Project, Tag 08EF.** Let `X` be a quasi-compact and quasi-separated scheme and let
> `E ∈ D^b_{QCoh}(𝒪_X)`. There exists an integer `n₀ > 0` such that
> `Ext^n_{D(𝒪_X)}(ℰ, E) = 0` for every finite locally free `𝒪_X`-module `ℰ` and every `n ≥ n₀`.
>
> The Ext group is the group of morphisms `ℰ ⟶ E⟦n⟧` in `D(𝒪_X)`, with `ℰ` placed in
> cohomological degree zero, and its vanishing is subsingletonness of that group.

```lean
theorem exists_pos_subsingleton_hom_singleFunctor_of_isFiniteLocallyFree
    (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X]
    (E : DerivedCategory X.Modules)
    (hE : DerivedCategoryB.derivedCategoryBBounded
      (SheafOfModules.isQuasicoherent X.ringCatSheaf) E) :
    ∃ n₀ : ℤ, 0 < n₀ ∧
      ∀ ℰ : X.Modules, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} ℰ →
        ∀ n : ℤ, n₀ ≤ n →
          Subsingleton ((DerivedCategory.singleFunctor X.Modules 0).obj ℰ ⟶ E⟦n⟧)
```

## Tag 09M4, a lemma

[Tag 09M4](https://stacks.math.columbia.edu/tag/09M4) in the Stacks Project.

**`Stacks.DerivedQCoh.exists_window_subsingleton_hom_of_isPerfect_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DetectingBoundednessOfAPerfectComplex.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DetectingBoundednessOfAPerfectComplex.lean#L147). The attribute's comment: “part (1)”.

> **[Stacks, Tag 09M4], part (1).** Let `X` be a quasi-compact and quasi-separated scheme and
> let `K` be a perfect object of `D(𝒪_X)`. Then there are integers `a ≤ b` such that every
> `L ∈ D_QCoh(𝒪_X)` whose cohomology sheaves vanish in the degrees `a, …, b` admits no nonzero
> morphism `K ⟶ L`.
>
> This is `Stacks.DerivedQCoh.exists_window_subsingleton_hom_of_isPerfect_general` at the derived
> global sections `Stacks.DerivedQCoh.schemeDerivedSections X`, which exist for every scheme; the
> statement mentions no derived global sections functor and carries no hypothesis beyond the
> source's.

```lean
theorem exists_window_subsingleton_hom_of_isPerfect_qcqs (K : DerivedCategory X.Modules)
    (hK : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) K) :
    ∃ a b : ℤ, a ≤ b ∧
      ∀ L : DerivedCategory X.Modules,
        (∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj L).IsQuasicoherent) →
        (∀ i : ℤ, a ≤ i → i ≤ b → IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj L)) →
        Subsingleton (K ⟶ L)
```

**`Stacks.DerivedQCoh.finite_setOf_not_subsingleton_hom_shift_of_isPerfect_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DetectingBoundednessOfAPerfectComplex.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DetectingBoundednessOfAPerfectComplex.lean#L164). The attribute's comment: “part (2)”.

> **[Stacks, Tag 09M4], part (2).** Let `X` be a quasi-compact and quasi-separated scheme, let
> `K` be a perfect object of `D(𝒪_X)` and let `L` be a bounded object of `D_QCoh(𝒪_X)`. Then
> `Ext^n_{D(𝒪_X)}(K, L) = Hom_{D(𝒪_X)}(K, L⟦n⟧)` vanishes for all but finitely many `n`.
>
> This is `Stacks.DerivedQCoh.finite_setOf_not_subsingleton_hom_shift_of_isPerfect_general` at the
> derived global sections `Stacks.DerivedQCoh.schemeDerivedSections X`.

```lean
theorem finite_setOf_not_subsingleton_hom_shift_of_isPerfect_qcqs (K : DerivedCategory X.Modules)
    (hK : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) K)
    (L : DerivedCategory X.Modules)
    (hLqc : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj L).IsQuasicoherent)
    (c d : ℤ) (hLGE : L.IsGE c) (hLLE : L.IsLE d) :
    {n : ℤ | ¬ Subsingleton (K ⟶ L⟦n⟧)}.Finite
```

## Tag 08EG, a lemma

[Tag 08EG](https://stacks.math.columbia.edu/tag/08EG) in the Stacks Project.

**`Stacks.DerivedQCoh.OpenLift.exists_finiteLocallyFree_biprod_iso_restrict_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/ShiftedBundleSummand.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/ShiftedBundleSummand.lean#L428).

> **[Stacks, Tag 08EG].** Let `X` be an affine scheme and `U ⊆ X` a quasi-compact open. For
> every perfect object `E` of `D(𝒪_U)` there are an integer `r`, a finite locally free
> `𝒪_U`-module `ℱ` and a perfect complex `P` of `𝒪_X`-modules with `ℱ[-r] ⊕ E ≅ P|_U`, where
> `ℱ[-r]` is `ℱ` placed in cohomological degree `r`.

```lean
theorem exists_finiteLocallyFree_biprod_iso_restrict_of_isPerfect
    (X : Scheme.{u}) [IsAffine X] (U : X.Opens) (hU : IsCompact (U : Set X))
    (E : DerivedCategory U.toScheme.Modules)
    (hE : IsPerfect (X := U.toScheme.toRingedSpace) E) :
    ∃ (r : ℤ) (F : U.toScheme.Modules) (P : CochainComplex (OXMod.{u, u, u} X.toRingedSpace) ℤ),
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} F ∧
      IsPerfectComplex P ∧
      Nonempty (((DerivedCategory.singleFunctor U.toScheme.Modules r).obj F ⊞ E) ≅
        DerivedCategory.Q.obj
          (((AlgebraicGeometry.RingedSpace.restrictModules.{u, u} X.toRingedSpace
            U).mapHomologicalComplex (ComplexShape.up ℤ)).obj P))
```

## Tag 08EH, a lemma

[Tag 08EH](https://stacks.math.columbia.edu/tag/08EH) in the Stacks Project.

**`Stacks.DerivedQCoh.OpenLift.exists_isPerfect_derivedTensor_lift_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/AffineLift.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/AffineLift.lean#L245).

> Let `X` be an affine scheme and `U ⊆ X` a quasi-compact open. Let `E, E'` be objects of
> `D_QCoh(𝒪_X)` with `E` perfect. For every morphism `α : E|_U ⟶ E'|_U` there are a perfect object
> `I` of `D(𝒪_X)`, a morphism `b : I ⟶ 𝒪_X` whose restriction to `U` is an isomorphism, and a
> morphism `γ : E ⊗^L I ⟶ E'`, such that, writing `β : E ⊗^L I ⟶ E ⊗^L 𝒪_X ≅ E` for the morphism
> induced by `b`, the object `E₁ = E ⊗^L I` is perfect, `β|_U` is an isomorphism and
> `α = γ|_U ∘ (β|_U)⁻¹`.

```lean
theorem exists_isPerfect_derivedTensor_lift_of_isAffine (X : Scheme.{u}) [IsAffine X]
    (U : X.Opens) (hU : IsCompact (U : Set X))
    (E E' : DerivedCategory (SheafOfModules X.ringCatSheaf))
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect.{u, u, u + 1} (X := X.toRingedSpace) E)
    (hE' : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj E').IsQuasicoherent)
    (α : (derivedRestrict U.ι).obj E ⟶ (derivedRestrict U.ι).obj E') :
    letI := derivedMonoidalStructure X.sheaf
    ∃ (I : DerivedCategory (SheafOfModules X.ringCatSheaf))
      (b : I ⟶ 𝟙_ (DerivedCategory (SheafOfModules X.ringCatSheaf))) (γ : E ⊗ I ⟶ E'),
      Stacks.Cohomology.PerfectComplexes.IsPerfect.{u, u, u + 1} (X := X.toRingedSpace) I ∧
      IsIso ((derivedRestrict U.ι).map b) ∧
      Stacks.Cohomology.PerfectComplexes.IsPerfect.{u, u, u + 1} (X := X.toRingedSpace)
        (E ⊗ I : DerivedCategory (SheafOfModules X.ringCatSheaf)) ∧
      IsIso ((derivedRestrict U.ι).map (E ◁ b ≫ (ρ_ E).hom)) ∧
      (derivedRestrict U.ι).map (E ◁ b ≫ (ρ_ E).hom) ≫ α = (derivedRestrict U.ι).map γ
```

## Tag 08EI, a lemma

[Tag 08EI](https://stacks.math.columbia.edu/tag/08EI) in the Stacks Project.

**`Stacks.DerivedQCoh.OpenLift.exists_isPerfectComplex_restrict_iso_biprod_shift_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/AffineLift.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/AffineLift.lean#L361).

> Let `X` be an affine scheme and `U ⊆ X` a quasi-compact open. For every perfect object `F` of
> `D(𝒪_U)` the object `F ⊕ F[1]` is the restriction of a perfect object of `D(𝒪_X)`: there is a
> perfect complex `P` of `𝒪_X`-modules whose degreewise restriction to `U` represents `F ⊕ F[1]`.

```lean
theorem exists_isPerfectComplex_restrict_iso_biprod_shift_of_isAffine (X : Scheme.{u})
    [IsAffine X] (U : X.Opens) (hU : IsCompact (U : Set X))
    (F : DerivedCategory U.toScheme.Modules)
    (hF : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := U.toScheme.toRingedSpace) F) :
    ∃ P : CochainComplex (StrictlyPerfect.OXMod.{u, u, u} X.toRingedSpace) ℤ,
      Stacks.Cohomology.PerfectComplexes.IsPerfectComplex P ∧
      Nonempty ((F ⊞ F⟦(1 : ℤ)⟧) ≅ DerivedCategory.Q.obj
        (((AlgebraicGeometry.RingedSpace.restrictModules.{u, u} X.toRingedSpace
          U).mapHomologicalComplex (ComplexShape.up ℤ)).obj P))
```

## Tag 08EJ, a lemma

[Tag 08EJ](https://stacks.math.columbia.edu/tag/08EJ) in the Stacks Project.

**`Stacks.PowerTorsion.exists_pow_smul_eq_zero_of_isPerfect_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffinePowerTorsion.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffinePowerTorsion.lean#L152). The attribute's comment: “on an affine scheme, in D(𝒪_X); the base case of the induction over the quasi-compact opens that gives the quasi-compact quasi-separated case”.

> **[Stacks, Tag 08EJ] on an affine scheme.** Let `R` be a commutative ring, let `f : R` and
> let `X = Spec R`. Let `α : E ⟶ E'` be a morphism of `D_QCoh(𝒪_X)` such that `E` is perfect and
> `E'` is supported on the closed subset `T = V(f)`, that is, the cohomology sheaves of `E'` have
> vanishing stalks at every point off `V(f)`. Then `f ^ n • α = 0` for some `n ≥ 0`.
>
> Both objects are `Ñ` for an object `N` of `D(R)` by [Stacks, Tag 06Z0], perfectness of `E`
> becomes perfectness of its preimage `M` by [Stacks, Tag 08EB], and the support condition on `E'`
> becomes `f`-power torsion of the cohomology modules of the preimage `N`. The statement in `D(R)`
> is `StacksDraft.Perfect.homPowerTorsion_of_isPerfect`; derived sheafification carries its
> conclusion back, being `R`-linear and fully faithful.
>
> This is the base case of the induction over the quasi-compact opens that proves the statement
> for a quasi-compact quasi-separated scheme,
> `Stacks.PowerTorsion.exists_pow_smul_eq_zero_of_isPerfect_of_cohomologySupportedOn_qcqs`.

```lean
theorem exists_pow_smul_eq_zero_of_isPerfect_of_cohomologySupportedOn (f : R)
    {E E' : DerivedCategory (Spec (CommRingCat.of R)).Modules}
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect
      (X := (Spec (CommRingCat.of R)).toRingedSpace) E)
    (hEq : ∀ n : ℤ, ((DerivedCategory.homologyFunctor
      (Spec (CommRingCat.of R)).Modules n).obj E).IsQuasicoherent)
    (hE'q : ∀ n : ℤ, ((DerivedCategory.homologyFunctor
      (Spec (CommRingCat.of R)).Modules n).obj E').IsQuasicoherent)
    (hsupp : CohomologySupportedOn (Spec (CommRingCat.of R)).ringCatSheaf
      (PrimeSpectrum.zeroLocus {f}) E')
    (α : E ⟶ E') :
    letI : Linear R (Spec (CommRingCat.of R)).Modules := modulesLinear R (specBase R)
    ∃ k : ℕ, f ^ k • α = 0
```

**`Stacks.DerivedQCoh.exists_pow_smul_eq_zero_of_isPerfect_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/PowerTorsionAffineOpen.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/PowerTorsionAffineOpen.lean#L215). The attribute's comment: “on a quasi-compact quasi-separated scheme, the statement in full”.

> Let `X` be a quasi-compact quasi-separated scheme and let
> `f ∈ Γ(X, 𝒪_X)`. Let `E` and `E'` be objects of `D_QCoh(𝒪_X)` with `E` perfect and `E'`
> cohomologically supported on `T = V(f)`. Then for every `α : E ⟶ E'` there is an `n ≥ 0` with
> `f ^ n · α = 0`.

```lean
public theorem exists_pow_smul_eq_zero_of_isPerfect_of_cohomologySupportedOn {X : Scheme.{u}}
    [CompactSpace X] [QuasiSeparatedSpace X] (f : Γ(X, ⊤))
    (E F : DerivedCategory X.Modules)
    (hFqc : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj F).IsQuasicoherent)
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E)
    (hF : AlgebraicGeometry.CohomologySupportedOn X.ringCatSheaf (X.zeroLocus {f}) F)
    (α : E ⟶ F) :
    ∃ n : ℕ, globalScalar X.ringCatSheaf f ^ n • α = 0
```

**`Stacks.PowerTorsion.exists_pow_smul_eq_zero_of_isPerfect_of_cohomologySupportedOn_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/QcqsPowerTorsion.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/QcqsPowerTorsion.lean#L412).

> **[Stacks, Tag 08EJ].** Let `X` be a quasi-compact quasi-separated scheme and let
> `f ∈ Γ(X, 𝒪_X)`. Let `α : E ⟶ E'` be a morphism of `D_QCoh(𝒪_X)` such that `E` is perfect and
> `E'` is supported on the closed subset `T = V(f)`, that is, the cohomology sheaves of `E'` have
> vanishing stalks at every point where `f` does not vanish. Then `f ^ n • α = 0` for some
> `n ≥ 0`.
>
> The scalar acts through the `Γ(X, 𝒪_X)`-linear structure
> `AlgebraicGeometry.Scheme.linearOfRingHom` of the identity ring map, which is a definition and
> not an instance -- a scheme does not determine a base ring -- and so appears as a `letI` in the
> statement.
>
> This is `Stacks.PowerTorsion.powerTorsionProperty_top` at the degree `0`, the shift being
> undone by the unitor of the shift.

```lean
theorem exists_pow_smul_eq_zero_of_isPerfect_of_cohomologySupportedOn_qcqs {X : Scheme.{u}}
    [CompactSpace X] [QuasiSeparatedSpace X] (f : Γ(X, ⊤)) (E E' : DerivedCategory X.Modules)
    (hE : IsPerfect (X := ringedSpace X) E)
    (hEq : ∀ n : ℤ, ((DerivedCategory.homologyFunctor X.Modules n).obj E).IsQuasicoherent)
    (hE'q : ∀ n : ℤ, ((DerivedCategory.homologyFunctor X.Modules n).obj E').IsQuasicoherent)
    (hsupp : CohomologySupportedOn X.ringCatSheaf ((X.basicOpen f : Set X)ᶜ) E')
    (α : E ⟶ E') :
    letI : Linear Γ(X, ⊤) X.Modules := Scheme.linearOfRingHom X Γ(X, ⊤) (RingHom.id Γ(X, ⊤))
    ∃ k : ℕ, f ^ k • α = 0
```

**`StacksDraft.Perfect.exists_pow_smul_eq_zero_of_isPerfect_of_support_subset_zeroLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/PowerTorsionTarget.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Perfect/PowerTorsionTarget.lean#L182). The attribute's comment: “affine case, in D(A); the geometric form on an affine scheme, and the quasi-compact quasi-separated case, are in the AlgebraicGeometry directory”.

> Let `A` be a commutative ring and let `f : A`. Let `α : E ⟶ E'` be a morphism in `D(A)` such
> that `E` is perfect and `E'` is supported on `T = V(f)`, that is, every cohomology module of `E'`
> has support contained in the zero locus of `f`. Then there is an `n ≥ 0` with `f ^ n • α = 0`.

```lean
public theorem exists_pow_smul_eq_zero_of_isPerfect_of_support_subset_zeroLocus (f : A)
    {E E' : DerivedCategory (ModuleCat.{u} A)} (hE : IsPerfect E)
    (hE' : ∀ p : ℤ, Module.support A
      ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj E' : Type u) ⊆
      PrimeSpectrum.zeroLocus {f})
    (α : E ⟶ E') : ∃ n : ℕ, f ^ n • α = 0
```

## Tag 08EK, a lemma

[Tag 08EK](https://stacks.math.columbia.edu/tag/08EK) in the Stacks Project.

**`Stacks.DerivedQCoh.OpenLift.exists_isPerfectComplex_supported_restrict_iso_biprod_shift_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/AffineSupportedLift.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/AffineSupportedLift.lean#L44).

> Let `X` be an affine scheme, `T ⊆ X` a closed subset with
> `X ∖ T` quasi-compact and `U ⊆ X` a quasi-compact open. For every perfect object `F` of
> `D(𝒪_U)` whose cohomology is supported on `T ∩ U`, the object `F ⊕ F[1]` is the restriction of a
> perfect object of `D(𝒪_X)` with cohomology supported on `T`: there is a perfect complex `P` of
> `𝒪_X`-modules, with cohomology supported on `T`, whose degreewise restriction to `U` represents
> `F ⊕ F[1]`.

```lean
theorem exists_isPerfectComplex_supported_restrict_iso_biprod_shift_of_isAffine
    (X : Scheme.{u}) [IsAffine X]
    (T : Set X) (hT : IsClosed T) (hTc : IsCompact Tᶜ)
    (U : X.Opens) (hU : IsCompact (U : Set X))
    (F : DerivedCategory U.toScheme.Modules)
    (hF : IsPerfect (X := U.toScheme.toRingedSpace) F)
    (hFT : CohomologySupportedOn U.toScheme.ringCatSheaf (Subtype.val ⁻¹' T) F) :
    ∃ P : CochainComplex (StrictlyPerfect.OXMod.{u, u, u} X.toRingedSpace) ℤ,
      IsPerfectComplex P ∧
      CohomologySupportedOn X.ringCatSheaf T (DerivedCategory.Q.obj P) ∧
      Nonempty ((F ⊞ F⟦(1 : ℤ)⟧) ≅ DerivedCategory.Q.obj
        (((AlgebraicGeometry.RingedSpace.restrictModules.{u, u} X.toRingedSpace
          U).mapHomologicalComplex (ComplexShape.up ℤ)).obj P))
```

## Tag 09IM, a lemma

[Tag 09IM](https://stacks.math.columbia.edu/tag/09IM) in the Stacks Project.

**`Stacks.Perfect.LiftingComplexes.exists_isPerfect_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/LiftingComplexes/General.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/LiftingComplexes/General.lean#L341).

> **[Stacks, Tag 09IM].** Let `X` be a quasi-compact quasi-separated scheme, `U ⊆ X` a
> quasi-compact open, `T ⊆ X` a closed subset whose complement is retrocompact in `X`, and `E` an
> object of `D_QCoh(𝒪_X)`. Every map `α : P ⟶ E|_U` out of a perfect object `P` of `D(𝒪_U)` whose
> cohomology is supported on `T ∩ U` comes from a map `β : R ⟶ E` out of a perfect object `R` of
> `D(𝒪_X)` whose cohomology is supported on `T`, with `P` a direct summand of `R|_U` by an inclusion
> `i` satisfying `i ≫ β|_U = α`.
>
> Quasi-compactness of `X` gives a finite cover of `X` by affine opens; the statement then follows
> from `Stacks.Perfect.LiftingComplexes.exists_isPerfect_lift_of_list` by the induction over that
> cover, whose single step glues the object already built over a smaller open to the one the affine
> case produces over the next affine.

```lean
theorem exists_isPerfect_lift {X : Scheme.{u}} [CompactSpace X] [QuasiSeparatedSpace X]
    (U : X.Opens) (hU : IsCompact (U : Set X)) (T : Set X) (hT : IsClosed T)
    (hTc : ∀ W : X.Opens, IsCompact (W : Set X) → IsCompact ((W : Set X) ∩ Tᶜ))
    (E : DerivedCategory X.Modules)
    (hE : Stacks.DerivedQCoh.IsDQCoh (R := X.ringCatSheaf) E)
    (P : DerivedCategory U.toScheme.Modules) (hP : IsPerfect (X := ringedSpace U.toScheme) P)
    (hPT : CohomologySupportedOn U.toScheme.ringCatSheaf (⇑U.ι.base ⁻¹' T) P)
    (α : P ⟶ (derivedRestrict U.ι).obj E) :
    ∃ (R : DerivedCategory X.Modules) (β : R ⟶ E),
      IsPerfect (X := ringedSpace X) R ∧
      CohomologySupportedOn X.ringCatSheaf T R ∧
      ∃ (i : P ⟶ (derivedRestrict U.ι).obj R) (p : (derivedRestrict U.ι).obj R ⟶ P),
        i ≫ p = 𝟙 P ∧ i ≫ (derivedRestrict U.ι).map β = α
```

## Tag 09IN, a remark

[Tag 09IN](https://stacks.math.columbia.edu/tag/09IN) in the Stacks Project.

**`Stacks.Perfect.SupportedLiftDegree.exists_isPerfect_supported_hom_biprod_sumShifts_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportedLiftDegree.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportedLiftDegree.lean#L204). The attribute's comment: “The complement of `P` in `R|_U` is a finite biproduct of positive shifts of `P`, and for every degree `n` the construction can be iterated so that the complement has vanishing cohomology in all degrees `≥ n`, which is the agreement of the cohomology sheaves of `R|_U` and of `P` above `n`.”.

> **[Stacks, Tag 09IN].** Let `X` be a quasi-compact quasi-separated scheme, `U ⊆ X` a
> quasi-compact open, `T ⊆ X` closed with `X ∖ T` retrocompact, and `E` an object of `D(𝒪_X)` with
> quasi-coherent cohomology. Let `P` be a perfect object of `D(𝒪_U)` supported on `T ∩ U` and
> `α : P ⟶ E|_U`. Then for every degree `n` there are a perfect object `R` of `D(𝒪_X)` supported on
> `T`, a map `β : R ⟶ E`, an object `Q` of `D(𝒪_U)` and an isomorphism `R|_U ≅ P ⊞ Q` through which
> `β|_U` is the projection onto `P` followed by `α`, with `Q` a finite biproduct of positive shifts
> of `P` and `Hⁱ(Q) = 0` for every `i ≥ n`.
>
> The two clauses are the remark's two sentences: the shape
> `R|_U = P ⊕ P^{⊕n_1}[1] ⊕ ⋯ ⊕ P^{⊕n_m}[m]`, recorded as
> `Stacks.SumOfPositiveShifts.IsSumOfPositiveShifts`, and the agreement of the cohomology sheaves
> of `R|_U` and of `P` above the given degree, which for a splitting is the vanishing of the
> complement there. The degree is fixed first: the other reading, one `R` serving every `n`, is
> false, because a perfect object is bounded, so agreement in every degree would make `P ⟶ R|_U`
> an isomorphism and extend `P` to a perfect object of `D(𝒪_X)`.
>
> The statement proved here is stronger than the remark in one further respect, and that
> strengthening is what makes the iteration possible: `β|_U` is the projection `R|_U ⟶ P` followed
> by `α`, not merely a map restricting to `α` on the summand.
>
> **Where the formalisation departs from the source's recipe.** The remark says to repeat the
> construction "for the map `P^{⊕n_1}[1] ⊕ ⋯ ⊕ P^{⊕n_m}[m] ⟶ R|_U`", that is, with ambient object
> `R` and then to take cones. A map out of `cone(ρ)` extends a map out of `R` only when its
> composite with `ρ` vanishes, and with ambient object `R` nothing makes `ρ ≫ β` vanish, so that
> route loses the map to `E` at the first cone. The route taken instead carries, at each stage `k`,
> the fibre `F_k` of `β_k : R_k ⟶ E` — the first vertex of a distinguished triangle
> `F_k ⟶ R_k ⟶ E ⟶ F_k⟦1⟧` — and applies [Stacks, Tag 09IM] with ambient object `F_k`; the cone is
> then formed on `ρ := β'' ≫ u` with `u : F_k ⟶ R_k`, and `ρ ≫ β_k = β'' ≫ (u ≫ β_k) = 0` because
> `u` and `β_k` are consecutive maps of a distinguished triangle. The octahedral axiom returns both
> the new map to `E` and the new fibre at once. The device is
> `Stacks.SplitLiftTower.exists_biprod_iso_lift_of_fibre_octahedron` and the iteration is
> `DerivedCategory.exists_hom_biprod_iso_of_fibreOracle`.
>
> [Stacks, Tag 09IM] itself is registered on another declaration and is used here
> through
> `Stacks.Perfect.SupportedLiftGeneral.exists_isPerfect_supported_hom_biprod_sumShifts`.

```lean
theorem exists_isPerfect_supported_hom_biprod_sumShifts_isZero (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] (U : X.Opens) (hU : IsCompact ((U : X.Opens) : Set X))
    (T : Set X) (hT : IsClosed T) (hTc : IsRetrocompact (Tᶜ : Set X))
    (E : DerivedModules X.toRingedSpace) (hE : HasQuasicoherentHomology X E)
    (P : DerivedModules (X.toRingedSpace.restrict U.isOpenEmbedding))
    (hP : IsPerfect.{u, u, u + 1} (X := X.toRingedSpace.restrict U.isOpenEmbedding) P)
    (hPT : AlgebraicGeometry.CohomologySupportedOn
      (structureSheafRing (X.toRingedSpace.restrict U.isOpenEmbedding))
      (Subtype.val ⁻¹' T) P)
    (α : P ⟶ (derivedRestrict (openInclusion X U)).obj E) :
    ∀ n : ℤ, ∃ (R : DerivedModules X.toRingedSpace) (β : R ⟶ E),
      (IsPerfect.{u, u, u + 1} (X := X.toRingedSpace) R ∧
          AlgebraicGeometry.CohomologySupportedOn (structureSheafRing X.toRingedSpace) T R) ∧
        ∃ (Q : DerivedModules (X.toRingedSpace.restrict U.isOpenEmbedding))
          (e : (derivedRestrict (openInclusion X U)).obj R ≅ P ⊞ Q),
          IsSumOfPositiveShifts P Q ∧
            (∀ i : ℤ, n ≤ i → IsZero ((DerivedCategory.homologyFunctor (SheafOfModules.{u}
              (structureSheafRing (X.toRingedSpace.restrict U.isOpenEmbedding))) i).obj Q)) ∧
              e.inv ≫ (derivedRestrict (openInclusion X U)).map β = biprod.fst ≫ α
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.13, Tag 08EC](https://stacks.math.columbia.edu/tag/08EC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
