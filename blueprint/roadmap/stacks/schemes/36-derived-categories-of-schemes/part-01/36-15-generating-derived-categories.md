---
declaration: section
origin: cited
lean: Stacks.DerivedQCoh.AnyModel.exists_isPerfect_retract_derivedRestrict, Stacks.DerivedQCoh.OpenLift.exists_isPerfectComplex_retract_of_isPerfect_of_qcqs, Stacks.DerivedQCoh.OpenLift.exists_isPerfect_retract_derivedRestrict, Stacks.DerivedQCoh.OpenLift.exists_isPerfectComplex_retract_restrict_of_isPerfect, Stacks.Duality.OpenImmersion.exists_isPerfect_retract_derivedRestrict, Stacks.Koszul.Truncation.hom_koszulObject_eq_zero_of_isIso_unit, Stacks.Koszul.Truncation.isIso_unit_of_hom_koszulObject_eq_zero, Stacks.DerivedQCoh.AnyModel.hasPerfectGenerator_of_qcqs
statement: formalized
proof: formalized
---

# 36.15 Generating derived categories

Section 36.15 of the Stacks Project, [Tag 09IP](https://stacks.math.columbia.edu/tag/09IP). 4 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09IQ, a lemma

[Tag 09IQ](https://stacks.math.columbia.edu/tag/09IQ) in the Stacks Project.

**`Stacks.DerivedQCoh.AnyModel.exists_isPerfect_retract_derivedRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AnyModel/PerfectSummandOfRestriction.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AnyModel/PerfectSummandOfRestriction.lean#L79).

> **[Stacks, Tag 09IQ].** Let `X` be a quasi-compact quasi-separated scheme and `U ⊆ X` a
> quasi-compact open. Every perfect object `P` of `D(𝒪_U)` is a direct summand -- a retract -- of
> the restriction to `U` of a perfect object of `D(𝒪_X)`.
>
> This is [Stacks, Tag 09IM] with `T` the whole space and the zero object, transported from the
> model that tag is proved at to the locally small one.

```lean
theorem exists_isPerfect_retract_derivedRestrict {X : Scheme.{u}} [CompactSpace X]
    [QuasiSeparatedSpace X] (U : X.Opens) (hU : IsCompact (U : Set X))
    (P : DerivedCategory U.toScheme.Modules)
    (hP : IsPerfect (X := ringedSpace U.toScheme) P) :
    ∃ R : DerivedCategory X.Modules, IsPerfect (X := ringedSpace X) R ∧
      ∃ (i : P ⟶ (Stacks.Duality.OpenImmersion.derivedRestrict U.ι).obj R)
        (p : (Stacks.Duality.OpenImmersion.derivedRestrict U.ι).obj R ⟶ P), i ≫ p = 𝟙 P
```

**`Stacks.DerivedQCoh.OpenLift.exists_isPerfectComplex_retract_of_isPerfect_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/QcqsSummandOfRestriction.lean, line 459](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/QcqsSummandOfRestriction.lean#L459). The attribute's comment: “the perfect object on X exhibited by a perfect complex; any model of D(O_U)”.

> **[Stacks, Tag 09IQ].** Let `X` be a quasi-compact and quasi-separated scheme and `U ⊆ X` a
> quasi-compact open. Every perfect object `P` of `D(𝒪_U)` is a direct summand -- a retract -- of
> the restriction to `U` of a perfect object of `D(𝒪_X)`, here exhibited by a perfect complex `M` of
> `𝒪_X`-modules: `P` is a retract of the class of `M|_U`.
>
> The derived category of `𝒪_U` is an arbitrary model, and none is needed on `X`.

```lean
theorem exists_isPerfectComplex_retract_of_isPerfect_of_qcqs (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] (U : X.Opens) (hU : IsCompact (U : Set X))
    [hd : HasDerivedCategory.{d₁} U.toScheme.Modules] (P : DerivedCategory U.toScheme.Modules)
    (hP : @IsPerfect U.toScheme.toRingedSpace hd P) :
    ∃ M : CochainComplex X.Modules ℤ, IsPerfectComplex (X := X.toRingedSpace) M ∧
      Nonempty (Retract P (DerivedCategory.Q.obj
        (((Scheme.Modules.restrictFunctor U.ι).mapHomologicalComplex (ComplexShape.up ℤ)).obj
          M)))
```

**`Stacks.DerivedQCoh.OpenLift.exists_isPerfect_retract_derivedRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/QcqsSummandOfRestriction.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/QcqsSummandOfRestriction.lean#L484). The attribute's comment: “in D(O_X), at any models of the two derived categories”.

> **[Stacks, Tag 09IQ], in `D(𝒪_X)`.** Let `X` be a quasi-compact and quasi-separated scheme
> and `U ⊆ X` a quasi-compact open. Every perfect object `P` of `D(𝒪_U)` is a retract of the
> restriction to `U` of a perfect object `R` of `D(𝒪_X)`, at any models of the two derived
> categories, in independent universes; restriction is `j^*` for the open immersion `j : U ⟶ X`,
> which `Stacks.Duality.OpenImmersion.derivedRestrict` names when the two universes agree.

```lean
theorem exists_isPerfect_retract_derivedRestrict (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] (U : X.Opens) (hU : IsCompact (U : Set X))
    [hU' : HasDerivedCategory.{d₁} U.toScheme.Modules] [hX : HasDerivedCategory.{d₂} X.Modules]
    (P : DerivedCategory U.toScheme.Modules) (hP : @IsPerfect U.toScheme.toRingedSpace hU' P) :
    ∃ R : DerivedCategory X.Modules, @IsPerfect X.toRingedSpace hX R ∧
      Nonempty (Retract P ((Scheme.Modules.restrictFunctor U.ι).mapDerivedCategory.obj R))
```

**`Stacks.DerivedQCoh.OpenLift.exists_isPerfectComplex_retract_restrict_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/SummandOfRestriction.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/SummandOfRestriction.lean#L76). The attribute's comment: “for X affine; the quasi-compact quasi-separated case is deduced in the source from 09IM, whose induction over an affine cover needs 08EK and 08EH, neither of which this library has”.

> **[Stacks, Tag 09IQ] for `X` affine.** Let `X` be an affine scheme and `U ⊆ X` a
> quasi-compact open. Every perfect object `P` of `D(𝒪_U)` is a direct summand -- a retract -- of
> the restriction to `U` of a perfect complex of `𝒪_X`-modules.

```lean
theorem exists_isPerfectComplex_retract_restrict_of_isPerfect
    (X : Scheme.{u}) [IsAffine X] (U : X.Opens) (hU : IsCompact (U : Set X))
    (P : DerivedCategory U.toScheme.Modules)
    (hP : IsPerfect (X := U.toScheme.toRingedSpace) P) :
    ∃ M : CochainComplex (OXMod.{u, u, u} X.toRingedSpace) ℤ,
      IsPerfectComplex M ∧
      Nonempty (Retract P (DerivedCategory.Q.obj
        (((AlgebraicGeometry.RingedSpace.restrictModules.{u, u} X.toRingedSpace
          U).mapHomologicalComplex (ComplexShape.up ℤ)).obj M)))
```

**`Stacks.Duality.OpenImmersion.exists_isPerfect_retract_derivedRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/SummandOfRestriction.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PerfectApproximation/SummandOfRestriction.lean#L61).

> **[Stacks, Tag 09IQ].** Let `X` be a quasi-compact quasi-separated scheme and `U ⊆ X` a
> quasi-compact open. Every perfect object `P` of `D(𝒪_U)` is a direct summand -- a retract -- of
> the restriction to `U` of a perfect object `R` of `D(𝒪_X)`.

```lean
theorem exists_isPerfect_retract_derivedRestrict (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] (U : X.Opens) (hU : IsCompact (U : Set X))
    (P : DerivedCategory U.toScheme.Modules)
    (hP : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := U.toScheme.toRingedSpace) P) :
    ∃ R : DerivedCategory X.Modules,
      Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) R ∧
        Nonempty (Retract P ((derivedRestrict U.ι).obj R))
```

## Tag 09IR, a lemma

[Tag 09IR](https://stacks.math.columbia.edu/tag/09IR) in the Stacks Project.

**`Stacks.Koszul.Truncation.hom_koszulObject_eq_zero_of_isIso_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/KoszulOrthogonality/AffineSituation.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/KoszulOrthogonality/AffineSituation.lean#L186). The attribute's comment: “(1) implies (2)”.

> **[Stacks, Tag 09IR], the implication "(1) implies (2)".** In Situation [Stacks, Tag 08CZ],
> if the canonical map `E ⟶ Rj_*(E|_U)` is invertible then `Hom_{D(𝒪_X)}(K[n], E) = 0` for every
> `n ∈ ℤ`, where `K` is the sheafified Koszul complex on `f₁, …, f_r`.
>
> There is nothing to assume. The Koszul object restricts to zero on `U = ⋃ᵢ D(f_i)` by
> `Stacks.Koszul.OpenComplement.isZero_derivedRestrict_koszulObject`, so a morphism `K⟦n⟧ ⟶ Rj_* Z`
> is adjoint to a morphism out of `(j^* K)⟦n⟧ = 0` and hence zero; and `E` is isomorphic to
> `Rj_*(E|_U)` through the unit, while the condition is closed under isomorphism.

```lean
theorem hom_koszulObject_eq_zero_of_isIso_unit
    (E : DerivedCategory (Spec (CommRingCat.of A)).Modules)
    (h : IsIso ((derivedRestrictPushforwardAdjunction (openComplement f).ι).unit.app E)) :
    ∀ (n : ℤ) (g : (koszulObject f)⟦n⟧ ⟶ E), g = 0
```

**`Stacks.Koszul.Truncation.isIso_unit_of_hom_koszulObject_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/KoszulOrthogonality/AffineSituation.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/KoszulOrthogonality/AffineSituation.lean#L261). The attribute's comment: “(2) implies (1)”.

> **[Stacks, Tag 09IR], the implication "(2) implies (1)".** In Situation [Stacks, Tag 08CZ],
> let `E` be an object of `D_QCoh(𝒪_X)`, that is one whose cohomology sheaves are quasi-coherent.
> If `Hom_{D(𝒪_X)}(K[n], E) = 0` for every `n ∈ ℤ` then the canonical map `E ⟶ Rj_*(E|_U)` is
> invertible.
>
> Take a distinguished triangle `E ⟶ Rj_*(E|_U) ⟶ M ⟶ E⟦1⟧`; the claim is that `M = 0`. Three
> things are known about `M`.
>
> * `M|_U = 0`, because `j^*` of the unit at `E` is a section of the counit at `E|_U`, which is
>   invertible — `Rj_*` is fully faithful along an open immersion.
> * `Hom(K⟦n⟧, M) = 0` for every `n`, because right orthogonality to the shifts of `K` is a
>   triangulated subcategory and both `E` and `Rj_*(E|_U)` lie in it, the latter for the formal
>   reason that `j^* K = 0`.
> * The cohomology sheaves of `M` are quasi-coherent, because those of `E` are and `Rj_*` preserves
>   quasi-coherent cohomology along a quasi-compact open immersion ([Stacks, Tag 08D5]).
>
> Those three force `M = 0` by `Stacks.Koszul.Truncation.isZero_of_forall_hom_koszulObject_eq_zero`,
> which is the source's argument: pass to `D(A)` along the affine comparison of [Stacks, Tag 06Z0]
> and apply the Koszul detection statement over the ring. A distinguished triangle whose third
> vertex vanishes has invertible first morphism.

```lean
theorem isIso_unit_of_hom_koszulObject_eq_zero
    (E : DerivedCategory (Spec (CommRingCat.of A)).Modules)
    (hE : DerivedCategoryB.derivedCategoryB (A := (Spec (CommRingCat.of A)).Modules)
      (SheafOfModules.isQuasicoherent (Spec (CommRingCat.of A)).ringCatSheaf) E)
    (h : ∀ (n : ℤ) (g : (koszulObject f)⟦n⟧ ⟶ E), g = 0) :
    IsIso ((derivedRestrictPushforwardAdjunction (openComplement f).ι).unit.app E)
```

## Tag 09IS, a theorem

[Tag 09IS](https://stacks.math.columbia.edu/tag/09IS) in the Stacks Project.

**`Stacks.DerivedQCoh.AnyModel.hasPerfectGenerator_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/PerfectGeneratorInduction.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/PerfectGeneratorInduction.lean#L415). The attribute's comment: “the generator, in the ObjectProperty.IsWeakTriangulatedGenerator spelling”.

> **[Stacks, Tag 09IS], the theorem of Bondal and Van den Bergh**, in the form that
> `D_QCoh(𝒪_X)` is weakly generated by a single perfect object: on a quasi-compact quasi-separated
> scheme the property `Stacks.DerivedQCoh.AnyModel.HasPerfectGenerator` holds.
>
> This is the induction principle [Stacks, Tag 08DR] — in the clause `induction_top` for the whole
> space — applied to `Stacks.DerivedQCoh.AnyModel.HasPerfectGeneratorOn`, whose two clauses are
> `Stacks.DerivedQCoh.AnyModel.hasPerfectGeneratorOn_of_isAffineOpen` and
> `Stacks.DerivedQCoh.AnyModel.hasPerfectGeneratorOn_sup`; the conclusion is read at the identity
> of `X`, an open immersion whose image is all of `X`.

```lean
theorem hasPerfectGenerator_of_qcqs (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X] :
    HasPerfectGenerator X
```

**`Stacks.DerivedQCoh.AnyModel.exists_isPerfect_isZero_iff_forall_hom_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/PerfectGeneratorInduction.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/PerfectGeneratorInduction.lean#L431).

> **[Stacks, Tag 09IS], the theorem of Bondal and Van den Bergh, in the source's own words.**
> Let `X` be a quasi-compact quasi-separated scheme. There is a perfect object `P` of `D(𝒪_X)` such
> that for every object `E` of `D_QCoh(𝒪_X)` the following are equivalent: `E = 0`, and
> `Hom_{D(𝒪_X)}(P⟦n⟧, E) = 0` for all `n : ℤ`.
>
> This is `Stacks.DerivedQCoh.AnyModel.hasPerfectGenerator_of_qcqs` read in the ambient derived
> category by `CategoryTheory.ObjectProperty.isWeakTriangulatedGenerator_singleton_iff`; the
> converse implication holds for any object, a morphism into a zero object being zero.

```lean
theorem exists_isPerfect_isZero_iff_forall_hom_eq_zero (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] :
    ∃ P : DerivedCategory X.Modules, IsPerfect (X := X.toRingedSpace) P ∧
      ∀ E : DerivedCategory X.Modules, DerivedCategoryB.derivedCategoryB (A := X.Modules)
        (SheafOfModules.isQuasicoherent X.ringCatSheaf) E →
          (IsZero E ↔ ∀ (n : ℤ) (g : P⟦n⟧ ⟶ E), g = 0)
```

**`Stacks.Duality.AffineGeneration.exists_isCompactObject_isWeakTriangulatedGenerator_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/AffineQuasiCoherent.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/AffineQuasiCoherent.lean#L370). The attribute's comment: “FOR AN AFFINE SCHEME ONLY, and with the generator exhibited as a COMPACT rather than a perfect object. The source's induction over the quasi-compact opens, Tag 08DR, is available and so is its generation step, but two of its inputs are not: Tag 09IQ at a quasi-compact quasi-separated scheme (the library has only the affine case, Stacks.DerivedQCoh.OpenLift.exists_isPerfectComplex_retract_restrict_of_isPerfect; the source deduces the rest from Tag 09IM, needing Tags 08EK and 08EH, none of the three being present), and the implication perfect implies compact of Tag 09M1, which the source draws from the Hom formula of Tag 08DQ, absent. The generator here is the image of the regular module in degree zero under the comparison of Tag 06Z0, that is the structure sheaf in degree zero, which is the source's generator for an affine scheme; that it is perfect as well as compact is Tag 07LT carried across Tag 06Z0, which is not done here because the library's statement of the affine case of Tag 09M1, AlgebraicGeometry.isCompactObject_iff_isPerfect_spec, is pinned to CategoryTheory.HasDerivedCategory.standard and so speaks of a different derived category. Compactness is what the consumers of the tag ask for”.

> **[Stacks, Tag 09IS] for an affine scheme.** `D_QCoh(𝒪_X)` is generated by a single compact
> object: there is an object `P` of `D_QCoh(𝒪_X)` which is compact and such that an object of
> `D_QCoh(𝒪_X)` receiving only zero morphisms from the shifts of `P` is zero.
>
> The object produced is the image under
> `Stacks.Duality.AffineGeneration.affineComparison` of the regular module in degree zero, which is
> the structure sheaf in degree zero — the source's own generator for an affine scheme. See the
> implementation notes for why it is exhibited as compact rather than as perfect, and for what
> separates this from the tag's quasi-compact quasi-separated statement.

```lean
theorem exists_isCompactObject_isWeakTriangulatedGenerator_of_isAffine (X : Scheme.{u})
    [IsAffine X] :
    ∃ P : (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent X.ringCatSheaf)).FullSubcategory,
      IsCompactObject.{u} P ∧ (ObjectProperty.singleton P).IsWeakTriangulatedGenerator
```

**`Stacks.Duality.AffineGeneration.isCompactlyGenerated_derivedQuasiCoherent_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/AffineQuasiCoherent.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/AffineQuasiCoherent.lean#L397). The attribute's comment: “FOR AN AFFINE SCHEME ONLY, in the IsCompactlyGenerated form of Tag 09SQ and with the generator exhibited as compact rather than perfect; see Stacks.Duality.AffineGeneration.exists_isCompactObject_isWeakTriangulatedGenerator_of_isAffine for the full caveat”.

> **[Stacks, Tag 09IS] for an affine scheme, in the form [Stacks, Tag 09SQ] defines and Brown
> representability consumes.** `D_QCoh(𝒪_X)` is compactly generated: the one-element family
> consisting of the generator of
> `Stacks.Duality.AffineGeneration.exists_isCompactObject_isWeakTriangulatedGenerator_of_isAffine`
> is a family of compact objects which jointly generate.
>
> The category is spelled over `AlgebraicGeometry.SheafOfModules X.ringCatSheaf`, which is the
> spelling the hypothesis of [Stacks, Tag 0CR0] uses.

```lean
theorem isCompactlyGenerated_derivedQuasiCoherent_of_isAffine (X : Scheme.{u}) [IsAffine X] :
    IsCompactlyGenerated.{u}
      (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent X.ringCatSheaf)).FullSubcategory
```

**`Stacks.Duality.AffineGeneration.isCompactlyGenerated_quasiCoherentDerivedCategory_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/AffineQuasiCoherent.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/AffineQuasiCoherent.lean#L413). The attribute's comment: “FOR AN AFFINE SCHEME ONLY, in the IsCompactlyGenerated form of Tag 09SQ at the Scheme.Modules spelling of the category, which is the one Tag 0A9E's statement uses; see Stacks.Duality.AffineGeneration.exists_isCompactObject_isWeakTriangulatedGenerator_of_isAffine for the full caveat”.

> **[Stacks, Tag 09IS] for an affine scheme**, at the spelling of `D_QCoh(𝒪_X)` over
> `AlgebraicGeometry.Scheme.Modules X` — the one the statement of [Stacks, Tag 0A9E] uses. The two
> spellings are the same type with separately declared `HasDerivedCategory` instances; see the
> implementation notes.

```lean
theorem isCompactlyGenerated_quasiCoherentDerivedCategory_of_isAffine (X : Scheme.{u})
    [IsAffine X] :
    IsCompactlyGenerated.{u} (Stacks.Duality.quasiCoherentDerivedCategory X)
```

**`Stacks.Duality.QuasiAffineGeneration.exists_isCompactObject_isWeakTriangulatedGenerator_of_isQuasiAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QuasiAffineQuasiCoherent.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QuasiAffineQuasiCoherent.lean#L334). The attribute's comment: “FOR A QUASI-AFFINE SCHEME, and with the generator exhibited as a COMPACT rather than a perfect object. This weakens the affine hypothesis of Stacks.Duality.AffineGeneration.exists_isCompactObject_isWeakTriangulatedGenerator_of_isAffine but does NOT reach the tag's quasi-compact quasi-separated statement. The route is the reverse of the source's: compact generation passes DOWN from a scheme to a quasi-compact open of it, by Stacks.Duality.OpenImmersion.isCompactlyGenerated_quasiCoherentDerivedCategory_of_isOpenImmersion, so from the affine case it reaches exactly the schemes with a quasi-compact open immersion into an affine scheme, the quasi-affine ones. The source's own induction over the quasi-compact opens, Tag 08DR, goes the other way and still needs Tag 09IQ at a quasi-compact quasi-separated scheme and the implication perfect implies compact of Tag 09M1, neither of which is in the library; see the implementation notes of StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/AffineQuasiCoherent.lean. Nothing here needs either: the generator is compact by construction and compactness is what the consumers of the tag ask for”.

> **[Stacks, Tag 09IS] for a quasi-affine scheme.** `D_QCoh(𝒪_X)` is generated by a single
> compact object.
>
> A quasi-affine scheme is quasi-compact and `X ⟶ Spec Γ(X, ⊤)` is an open immersion
> ([Stacks, Tag 01P6], Mathlib's `AlgebraicGeometry.Scheme.IsQuasiAffine`), so this is the affine
> case `AffineGeneration.exists_isCompactObject_isWeakTriangulatedGenerator_of_isAffine`
> restricted along that immersion by
> `OpenImmersion.exists_isCompactObject_isWeakTriangulatedGenerator_of_isOpenImmersion`.
> The generator is therefore the restriction to `X` of the structure sheaf of `Spec Γ(X, ⊤)` in
> degree zero, which is `𝒪_X` in degree zero — the source's own generator.

```lean
theorem exists_isCompactObject_isWeakTriangulatedGenerator_of_isQuasiAffine (X : Scheme.{u})
    [X.IsQuasiAffine] :
    ∃ P : Stacks.Duality.quasiCoherentDerivedCategory X,
      IsCompactObject.{u} P ∧ (ObjectProperty.singleton P).IsWeakTriangulatedGenerator
```

**`Stacks.Duality.QuasiAffineGeneration.isCompactlyGenerated_quasiCoherentDerivedCategory_of_isQuasiAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QuasiAffineQuasiCoherent.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QuasiAffineQuasiCoherent.lean#L350). The attribute's comment: “FOR A QUASI-AFFINE SCHEME, in the IsCompactlyGenerated form of Tag 09SQ at the Scheme.Modules spelling of the category, which is the one Tag 0A9E's statement uses; see Stacks.Duality.QuasiAffineGeneration.exists_isCompactObject_isWeakTriangulatedGenerator_of_isQuasiAffine for the full caveat”.

> **[Stacks, Tag 09IS] for a quasi-affine scheme, in the form [Stacks, Tag 09SQ] defines and
> Brown representability consumes**, at the spelling of `D_QCoh(𝒪_X)` over
> `AlgebraicGeometry.Scheme.Modules X` — the one the statement of [Stacks, Tag 0A9E] uses.

```lean
theorem isCompactlyGenerated_quasiCoherentDerivedCategory_of_isQuasiAffine (X : Scheme.{u})
    [X.IsQuasiAffine] :
    IsCompactlyGenerated.{u} (Stacks.Duality.quasiCoherentDerivedCategory X)
```

**`Stacks.Duality.QuasiAffineGeneration.isCompactlyGenerated_derivedQuasiCoherent_of_isQuasiAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QuasiAffineQuasiCoherent.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QuasiAffineQuasiCoherent.lean#L366). The attribute's comment: “FOR A QUASI-AFFINE SCHEME, in the IsCompactlyGenerated form of Tag 09SQ at the SheafOfModules spelling of the category, which is the one Tag 0CR0's hypothesis uses; see Stacks.Duality.QuasiAffineGeneration.exists_isCompactObject_isWeakTriangulatedGenerator_of_isQuasiAffine for the full caveat”.

> **[Stacks, Tag 09IS] for a quasi-affine scheme**, at the spelling of `D_QCoh(𝒪_X)` over
> `AlgebraicGeometry.SheafOfModules X.ringCatSheaf` — the one the hypothesis of [Stacks, Tag 0CR0]
> uses. The two spellings are the same type with separately declared `HasDerivedCategory`
> instances.

```lean
theorem isCompactlyGenerated_derivedQuasiCoherent_of_isQuasiAffine (X : Scheme.{u})
    [X.IsQuasiAffine] :
    IsCompactlyGenerated.{u}
      (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent X.ringCatSheaf)).FullSubcategory
```

**`Stacks.SheafOfModules.exists_isPerfect_generator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/QcqsPerfectGenerator.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/QcqsPerfectGenerator.lean#L292).

> **[Stacks, Tag 09IS].** Let `X` be a quasi-compact and quasi-separated scheme. Then
> `D_QCoh(𝒪_X)` has a perfect generator: there is a perfect object `G` of `D(𝒪_X)` such that every
> object `K` of `D(𝒪_X)` with quasi-coherent cohomology sheaves which receives no nonzero morphism
> from any shift `G⟦n⟧` is zero.
>
> This is `Stacks.SheafOfModules.exists_isPerfect_generator_modules` read in the spelling
> `StructureSheafModules X.sheaf` with perfectness for the ringed site of opens, the spelling of the
> generator hypotheses of Stacks 0GEN in `DetectingBoundedAboveGenerator`; the two notions of
> perfectness agree by `Stacks.Cohomology.PerfectComplexes.isPerfect_ringedSite_of_isPerfect`.
>
> The proof is the source's: induction over a finite affine cover produces finitely many compact
> generators of `D_QCoh(𝒪_X)` (`Stacks.Duality.QcqsGeneration.exists_finite_compact_generators`),
> compact objects of `D_QCoh(𝒪_X)` are perfect
> (`Stacks.Duality.QcqsPerfect.isPerfect_of_isCompactObject_of_qcqs`), and their direct sum is a
> single perfect generator.

```lean
theorem exists_isPerfect_generator {X : Scheme.{u}}
    [HasSheafify (Opens.grothendieckTopology X.toPresheafedSpace.carrier) AddCommGrpCat.{u}]
    [(Opens.grothendieckTopology X.toPresheafedSpace.carrier).WEqualsLocallyBijective
      AddCommGrpCat.{u}]
    (hqc : CompactSpace X) (hqs : QuasiSeparatedSpace X) :
    ∃ G : DerivedCategory (StructureSheafModules X.sheaf), (ringedSite X.sheaf).IsPerfect G ∧
      ∀ K : DerivedCategory (StructureSheafModules X.sheaf),
        (∀ i : ℤ, ((DerivedCategory.homologyFunctor (StructureSheafModules X.sheaf) i).obj
          K).IsQuasicoherent) →
        (∀ (n : ℤ) (f : G⟦n⟧ ⟶ K), f = 0) → IsZero K
```

## Tag 0A9A, a lemma

[Tag 0A9A](https://stacks.math.columbia.edu/tag/0A9A) in the Stacks Project.

**`Stacks.Duality.SupportedGeneration.exists_isPerfect_quasiCoherentSupported_isWeakGenerator_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QcqsPerfectGenerator.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QcqsPerfectGenerator.lean#L282).

> **[Stacks, Tag 0A9A]** (Rouquier, Theorem 6.8). Let `X` be a quasi-compact and
> quasi-separated scheme and let `T ⊆ X` be a closed subset such that `X ∖ T` is quasi-compact.
> Then `D_{QCoh,T}(𝒪_X)` is generated by a single perfect object: there is a perfect object `P` of
> `D(𝒪_X)` lying in `D_{QCoh,T}(𝒪_X)` such that every object `E` of `D_{QCoh,T}(𝒪_X)` with
> `Hom(P[n], E) = 0` for all `n ∈ ℤ` is zero.
>
> Generation is [Stacks, Tag 09SJ] for `D_{QCoh,T}(𝒪_X)`, written out; morphisms of the full
> subcategory are morphisms of `D(𝒪_X)`. The generator is the compact one of
> `Stacks.Duality.SupportedGeneration.hasCompactSupportedGenerators`, built by the induction of the
> source, and it is perfect by
> `Stacks.Duality.SupportedGeneration.isPerfect_of_isCompactObject`.

```lean
theorem exists_isPerfect_quasiCoherentSupported_isWeakGenerator_of_qcqs (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X] (T : Set X) (hT : IsClosed T) (hTc : IsCompact Tᶜ) :
    ∃ P : DerivedCategory X.Modules,
      AlgebraicGeometry.RingedSpace.IsPerfect (X := X.toRingedSpace) P ∧
        quasiCoherentSupported X T P ∧
        ∀ E : DerivedCategory X.Modules, quasiCoherentSupported X T E →
          (∀ (n : ℤ) (g : P⟦n⟧ ⟶ E), g = 0) → IsZero E
```

**`Stacks.Rouquier.exists_isPerfect_isWeakTriangulatedGenerator_supported`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Rouquier/SupportedGeneratorQcqs.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Rouquier/SupportedGeneratorQcqs.lean#L128). The attribute's comment: “the generator, in the ObjectProperty.IsWeakTriangulatedGenerator spelling”.

> **The theorem of Rouquier.** Let `X` be a quasi-compact quasi-separated
> scheme and let `T ⊆ X` be closed with quasi-compact complement. Then `D_{QCoh,T}(𝒪_X)` has a weak
> triangulated generator which is perfect as an object of `D(𝒪_X)`.

```lean
theorem exists_isPerfect_isWeakTriangulatedGenerator_supported (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] (T : Set X) (hT : IsClosed T) (hTc : IsCompact Tᶜ) :
    ∃ G : Stacks.Duality.QuasiCoherentSupportedDerivedCategory X T,
      IsPerfect (X := X.toRingedSpace) G.obj ∧
        (ObjectProperty.singleton G).IsWeakTriangulatedGenerator
```

**`Stacks.Rouquier.exists_isPerfect_isZero_iff_forall_hom_eq_zero_supported`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Rouquier/SupportedGeneratorQcqs.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Rouquier/SupportedGeneratorQcqs.lean#L145).

> **The theorem of Rouquier, with the generator condition spelled out.** Let `X` be a
> quasi-compact quasi-separated scheme and let `T ⊆ X` be closed with quasi-compact complement.
> There is a perfect object `P` of `D(𝒪_X)` such that for every object `E` of `D_{QCoh,T}(𝒪_X)` the
> following are equivalent: `E = 0`, and `Hom_{D(𝒪_X)}(P⟦n⟧, E) = 0` for all `n : ℤ`.

```lean
theorem exists_isPerfect_isZero_iff_forall_hom_eq_zero_supported (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] (T : Set X) (hT : IsClosed T) (hTc : IsCompact Tᶜ) :
    ∃ P : DerivedCategory X.Modules, IsPerfect (X := X.toRingedSpace) P ∧
      ∀ E : DerivedCategory X.Modules, Stacks.Duality.quasiCoherentSupported X T E →
        (IsZero E ↔ ∀ (n : ℤ) (g : P⟦n⟧ ⟶ E), g = 0)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.15, Tag 09IP](https://stacks.math.columbia.edu/tag/09IP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
