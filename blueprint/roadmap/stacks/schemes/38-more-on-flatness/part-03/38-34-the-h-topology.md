---
declaration: section
origin: cited
lean: AlgebraicGeometry.isPHCovering_iff_isVCovering, AlgebraicGeometry.IsHCovering, AlgebraicGeometry.isHCovering_of_universallySubmersive_of_isNoetherian, AlgebraicGeometry.universallySubmersive_sigmaDesc_iff_isHCovering_of_isNoetherian, AlgebraicGeometry.universallySubmersive_sigmaDesc_of_isHCovering, AlgebraicGeometry.isHCovering_iff_isPHCovering, AlgebraicGeometry.exists_finitePresentation_proper_refinement_of_isHCovering, AlgebraicGeometry.IsHCovering.of_fppf_syntomic_smooth_etale_zariski
statement: formalized
proof: formalized
---

# 38.34 The h topology

Section 38.34 of the Stacks Project, [Tag 0ETQ](https://stacks.math.columbia.edu/tag/0ETQ). 19 tags here are carried by 51 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ETR, a lemma

[Tag 0ETR](https://stacks.math.columbia.edu/tag/0ETR) in the Stacks Project.

**`AlgebraicGeometry.isPHCovering_iff_isVCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/V/PhVFlatteningModification.lean, line 493](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/V/PhVFlatteningModification.lean#L493). The attribute's comment: “the equivalence of (1) and (2) for a family locally of finite presentation, which is the whole of the lemma”.

> **Stacks 0ETR.** A family of morphisms of schemes which are locally of finite presentation
> is a ph covering if and only if it is a V covering.
>
> The implication from a ph covering to a V covering is
> `AlgebraicGeometry.isVCovering_of_isPHCovering` and needs nothing; the converse is the six-step
> argument of the source, whose last input — the refinement of a standard V covering of an affine
> scheme by a standard ph covering, `AlgebraicGeometry.StandardVCoveringHasPHRefinement` — is
> `AlgebraicGeometry.standardVCoveringHasPHRefinement` above.

```lean
theorem isPHCovering_iff_isVCovering {T : Scheme.{u}} {I : Type v} (X : I → Scheme.{u})
    (f : ∀ i, X i ⟶ T) (hfp : ∀ i, LocallyOfFinitePresentation (f i)) :
    IsPHCovering X f ↔ IsVCovering X f
```

## Tag 0ETS, a definition

[Tag 0ETS](https://stacks.math.columbia.edu/tag/0ETS) in the Stacks Project.

**`AlgebraicGeometry.IsHCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/H/Coverings.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/H/Coverings.lean#L34).

> A family `{X i ⟶ T}` of morphisms of schemes is an *h covering* when
> every member is locally of finite presentation and the family is a ph covering.

```lean
public abbrev IsHCovering {T : Scheme.{u}} {I : Type v} (X : I → Scheme.{u})
    (f : ∀ i, X i ⟶ T) : Prop
```

## Tag 0ETT, a lemma

[Tag 0ETT](https://stacks.math.columbia.edu/tag/0ETT) in the Stacks Project.

**`AlgebraicGeometry.isHCovering_of_universallySubmersive_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SubmersiveFlatteningRefinement.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SubmersiveFlatteningRefinement.lean#L329). The attribute's comment: “(1) implies (2)”.

> **Stacks 0ETT, (1) implies (2).** A finite family of morphisms of finite type to a Noetherian
> scheme whose disjoint-union morphism is universally submersive is an h covering.
>
> This is `AlgebraicGeometry.isHCovering_of_universallySubmersive` with its
> hypothesis supplied by `AlgebraicGeometry.universallySubmersiveHasPHRefinement`.

```lean
theorem isHCovering_of_universallySubmersive_of_isNoetherian {X : Scheme.{u}} [IsNoetherian X]
    {I : Type v} [Finite I] [Small.{u} I] {Y : I → Scheme.{u}} (f : ∀ i, Y i ⟶ X)
    [∀ i, LocallyOfFiniteType (f i)] [∀ i, QuasiCompact (f i)]
    (hsub : UniversallySubmersive (Sigma.desc f)) : IsHCovering Y f
```

**`AlgebraicGeometry.universallySubmersive_sigmaDesc_iff_isHCovering_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SubmersiveFlatteningRefinement.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SubmersiveFlatteningRefinement.lean#L345).

> **Stacks 0ETT.** For a finite family `{X i ⟶ X}` of morphisms of finite type to a Noetherian
> scheme `X`, the morphism `∐ X i ⟶ X` is universally submersive if and only if the family is an h
> covering.
>
> The implication from the h covering condition is
> `AlgebraicGeometry.universallySubmersive_sigmaDesc_of_isHCovering` and needs neither finiteness
> nor the Noetherian hypothesis; the converse is
> `AlgebraicGeometry.isHCovering_of_universallySubmersive_of_isNoetherian` above.

```lean
theorem universallySubmersive_sigmaDesc_iff_isHCovering_of_isNoetherian {X : Scheme.{u}}
    [IsNoetherian X] {I : Type v} [Finite I] [Small.{u} I] {Y : I → Scheme.{u}} (f : ∀ i, Y i ⟶ X)
    [∀ i, LocallyOfFiniteType (f i)] [∀ i, QuasiCompact (f i)] :
    UniversallySubmersive (Sigma.desc f) ↔ IsHCovering Y f
```

**`AlgebraicGeometry.universallySubmersive_sigmaDesc_of_isHCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/UniversallySubmersive.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/UniversallySubmersive.lean#L116). The attribute's comment: “(2) implies (1)”.

> **Stacks 0ETT, (2) implies (1).** The morphism from the disjoint union of the sources of an
> h covering to its target is universally submersive.
>
> An h covering is a ph covering, hence a V covering, and the disjoint-union morphism of a V
> covering is universally submersive. No Noetherian or finiteness hypothesis is involved.

```lean
theorem universallySubmersive_sigmaDesc_of_isHCovering {X : Scheme.{u}} {I : Type v}
    [Small.{u} I] {Y : I → Scheme.{u}} {f : ∀ i, Y i ⟶ X} (hf : IsHCovering Y f) :
    UniversallySubmersive (Sigma.desc f)
```

## Tag 0H45, a lemma

[Tag 0H45](https://stacks.math.columbia.edu/tag/0H45) in the Stacks Project.

**`AlgebraicGeometry.isHCovering_iff_isPHCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/Coverings.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/Coverings.lean#L124).

> **Stacks 0H45.** Over a locally Noetherian scheme a family of morphisms is an h covering
> if and only if it is a ph covering, because there local finite presentation and local finite
> type agree.

```lean
public theorem isHCovering_iff_isPHCovering {T : Scheme.{u}} [IsLocallyNoetherian T]
    {I : Type v} (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T) :
    IsHCovering X f ↔ IsPHCovering X f
```

## Tag 0ETU, a lemma

[Tag 0ETU](https://stacks.math.columbia.edu/tag/0ETU) in the Stacks Project.

**`AlgebraicGeometry.exists_finitePresentation_proper_refinement_of_isHCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/ProperFinitePresentationRefinement.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/ProperFinitePresentationRefinement.lean#L157).

> **Stacks 0ETU.** An h covering of an affine scheme `T` is refined by a finite family of
> affine opens of a single proper surjective morphism `Y ⟶ T` of finite presentation: the opens
> cover `Y` and each of them maps to a member of the h covering over `T`.

```lean
public theorem exists_finitePresentation_proper_refinement_of_isHCovering
    {T : Scheme.{u}} [IsAffine T] {I : Type v}
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T)
    (hf : IsHCovering X f) :
    ∃ (J : Type u) (Y : Scheme.{u}) (p : Y ⟶ T)
      (V : J → Scheme.{u}) (j : ∀ k, V k ⟶ Y),
      Finite J ∧
        IsProper p ∧
        Surjective p ∧
        FinitePresentation p ∧
        (∀ k, IsAffine (V k)) ∧
        (∀ k, IsOpenImmersion (j k)) ∧
        (⋃ k, Set.range (j k)) = Set.univ ∧
        (∀ k, ∃ i : I, ∃ h : V k ⟶ X i, h ≫ f i = j k ≫ p)
```

## Tag 0ETV, a lemma

[Tag 0ETV](https://stacks.math.columbia.edu/tag/0ETV) in the Stacks Project.

**`AlgebraicGeometry.IsHCovering.of_fppf_syntomic_smooth_etale_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/FppfHComparison.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/FppfHComparison.lean#L104).

> **[Stacks, Tag 0ETV].** An fppf covering is an h covering. Hence syntomic, smooth, étale
> and Zariski coverings are h coverings as well.
>
> Here a family `{f i : X i ⟶ T}` is an fppf (resp. syntomic, smooth, étale, Zariski) covering
> when its members are flat and locally of finite presentation (resp. syntomic, smooth, étale,
> open immersions) and jointly surjective, that is, when `Presieve.ofArrows X f` belongs to the
> corresponding precoverage; it is an h covering, `AlgebraicGeometry.IsHCovering` (Stacks 0ETS),
> when its members are locally of finite presentation and it is a ph covering (Stacks 0DBG).
>
> The fppf case holds because the members of an fppf covering are locally of finite
> presentation and an fppf covering is a ph covering, Stacks 0DBT; the other four follow from it
> and Stacks 021N.

```lean
public theorem IsHCovering.of_fppf_syntomic_smooth_etale_zariski {T : Scheme.{u}} {I : Type v}
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T) :
    (Presieve.ofArrows X f ∈ Scheme.fppfPrecoverage T → IsHCovering X f) ∧
    (Presieve.ofArrows X f ∈
      Scheme.precoverage (@Syntomic : MorphismProperty Scheme.{u}) T → IsHCovering X f) ∧
    (Presieve.ofArrows X f ∈
      Scheme.precoverage (@Smooth : MorphismProperty Scheme.{u}) T → IsHCovering X f) ∧
    (Presieve.ofArrows X f ∈ Scheme.etalePrecoverage T → IsHCovering X f) ∧
    (Presieve.ofArrows X f ∈ Scheme.zariskiPrecoverage T → IsHCovering X f)
```

## Tag 0ETW, a lemma

[Tag 0ETW](https://stacks.math.columbia.edu/tag/0ETW) in the Stacks Project.

**`AlgebraicGeometry.surjective_proper_isHCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/Coverings.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/Coverings.lean#L115).

> **Stacks 0ETW.** A surjective proper morphism of schemes of finite presentation is an h
> covering by itself.

```lean
public theorem surjective_proper_isHCovering {X Y : Scheme.{u}} (f : Y ⟶ X)
    [Surjective f] [IsProper f] (hf : FinitePresentation f) :
    IsHCovering (fun _ : Unit ↦ Y) (fun _ ↦ f)
```

## Tag 0ETX, a lemma

[Tag 0ETX](https://stacks.math.columbia.edu/tag/0ETX) in the Stacks Project.

**`AlgebraicGeometry.isHCovering_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/CoveringRefinement.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/CoveringRefinement.lean#L49).

> **Stacks 0ETX.** A family of morphisms of schemes which are locally of finite
> presentation is an h covering if and only if some h covering refines it, if and only if its
> disjoint-union morphism is an h covering.

```lean
public theorem isHCovering_tfae {T : Scheme.{u}} {I : Type v} [Small.{u} I]
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T)
    (hlfp : ∀ i, LocallyOfFinitePresentation (f i)) :
    List.TFAE [
      IsHCovering X f,
      ∃ (K : Type v) (Y : K → Scheme.{u}) (g : ∀ k, Y k ⟶ T),
        IsHCovering Y g ∧
          Nonempty
            (({ I₀ := K, X := Y, f := g } : PreZeroHypercover T).Hom
              ({ I₀ := I, X := X, f := f } : PreZeroHypercover T)),
      IsHCovering (fun _ : Unit ↦ ∐ X) (fun _ ↦ Sigma.desc f)]
```

## Tag 0ETY, a lemma

[Tag 0ETY](https://stacks.math.columbia.edu/tag/0ETY) in the Stacks Project.

**`AlgebraicGeometry.isHCovering_of_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/Coverings.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/Coverings.lean#L108). The attribute's comment: “part (1)”.

> **Stacks 0ETY, part (1).** An isomorphism of schemes, regarded as a family indexed by a
> type with exactly one element, is an h covering.

```lean
public theorem isHCovering_of_isIso {T' T : Scheme.{u}} {I : Type v} [Unique I] (f : T' ⟶ T)
    [IsIso f] : IsHCovering (fun _ : I ↦ T') (fun _ ↦ f)
```

**`AlgebraicGeometry.isHCovering_bind`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/Coverings.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/Coverings.lean#L185). The attribute's comment: “part (2)”.

> **Stacks 0ETY part (2).** Composing an h covering with an h covering of each of its
> members gives an h covering.
>
> Local finite presentation is closed under composition, and the ph-covering condition is
> `AlgebraicGeometry.isPHCovering_bind`, which is Stacks 0DBI part (2).

```lean
public theorem isHCovering_bind {T : Scheme.{u}}
    (E : PreZeroHypercover.{v} T) (hE : IsHCovering E.X E.f)
    (F : ∀ i, PreZeroHypercover.{w} (E.X i))
    (hF : ∀ i, IsHCovering (F i).X (F i).f) :
    IsHCovering (E.bind F).X (E.bind F).f
```

**`AlgebraicGeometry.isHCovering_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/Coverings.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/Coverings.lean#L202). The attribute's comment: “part (3)”.

> **Stacks 0ETY part (3).** The base change of an h covering along an arbitrary morphism of
> schemes is an h covering.
>
> Local finite presentation is stable under base change, and the ph-covering condition is
> `AlgebraicGeometry.isPHCovering_pullback`, which is Stacks 0DBI part (3).

```lean
public theorem isHCovering_pullback {T T' : Scheme.{u}} {I : Type v} {X : I → Scheme.{u}}
    {f : ∀ i, X i ⟶ T} (hf : IsHCovering X f) (g : T' ⟶ T) :
    IsHCovering (fun i ↦ pullback (f i) g) (fun i ↦ pullback.snd (f i) g)
```

## Tag 0ETZ, a definition

[Tag 0ETZ](https://stacks.math.columbia.edu/tag/0ETZ) in the Stacks Project.

**`AlgebraicGeometry.BigHSite`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/H/BigSite.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/H/BigSite.lean#L71).

> **Stacks 0ETZ.** A big h site consists of an initial set of schemes and initial h
> coverings, a sufficiently large cutoff category containing them, and a bounded collection of
> h coverings satisfying the site axioms and representing every h covering.

```lean
public structure BigHSite
```

## Tag 0EUY, a definition

[Tag 0EUY](https://stacks.math.columbia.edu/tag/0EUY) in the Stacks Project.

**`AlgebraicGeometry.IsStandardHCovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/H/StandardCoverings.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/H/StandardCoverings.lean#L50). The attribute's comment: “part (1)”.

> **Stacks 0EUY, part (1).** A family `fᵢ : Xᵢ ⟶ T` over an affine scheme `T` is a
> **standard h covering** when its index type is finite, every `Xᵢ` is affine, every `fᵢ` is of
> finite presentation, and some standard ph covering of `T` refines the family.

```lean
public noncomputable def IsStandardHCovering {T : Scheme.{u}} [IsAffine T] {I : Type v}
    {X : I → Scheme.{u}} (f : ∀ i, X i ⟶ T) : Prop
```

## Tag 0EU0, a lemma

[Tag 0EU0](https://stacks.math.columbia.edu/tag/0EU0) in the Stacks Project.

**`AlgebraicGeometry.BigHSite.exists_isCovering_tautologicallyEquivalent_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SiteCoveringRefinement.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SiteCoveringRefinement.lean#L92). The attribute's comment: “part (3)”.

> **Stacks 0EU0, part (3).** A Zariski covering of an object of a big h site is
> tautologically equivalent to a covering belonging to that site.

```lean
public theorem BigHSite.exists_isCovering_tautologicallyEquivalent_openCover
    (B : BigHSite.{u}) (T : B.Schemes) (𝒰 : (B.inclusion.obj T).OpenCover.{v}) :
    ∃ 𝒱 : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, 𝒱⟩ ∧
        PreZeroHypercover.TautologicallyEquivalent 𝒰.toPreZeroHypercover
          (𝒱.map B.inclusion)
```

**`AlgebraicGeometry.exists_isCovering_refinement_of_isHCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SiteCoveringRefinement.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SiteCoveringRefinement.lean#L144). The attribute's comment: “part (1)”.

> **Stacks 0EU0, part (1).** An arbitrary h covering of an object of a big h site is refined
> by one of the site's own covering families.
>
> The affine opens of the target are a Zariski covering, hence by part (3) tautologically
> equivalent to a chosen family `G`.  Each member of `G` is isomorphic over the target to an
> affine open, so the base change of the given family to it is an h covering of an affine
> scheme; Stacks 0ETU refines that base change by a standard h covering, which part (2)
> realizes inside the site.  The site's composition axiom assembles the realized families into
> the required covering.

```lean
public theorem exists_isCovering_refinement_of_isHCovering
    (B : BigHSite.{u}) (T : B.Schemes) (𝒰 : PreZeroHypercover.{v} (B.inclusion.obj T))
    (h𝒰 : IsHCovering 𝒰.X 𝒰.f) :
    ∃ 𝒱 : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, 𝒱⟩ ∧ Nonempty ((𝒱.map B.inclusion).Hom 𝒰)
```

**`AlgebraicGeometry.exists_isCovering_tautologicallyEquivalent_standardHCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SiteCoverings.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SiteCoverings.lean#L53). The attribute's comment: “part (2)”.

> **Stacks 0EU0, part (2).** A standard h covering of an affine object of a big h site is
> tautologically equivalent to a covering belonging to that site.
>
> Parts (1) and (3) are `AlgebraicGeometry.exists_isCovering_refinement_of_isHCovering` and
> `AlgebraicGeometry.BigHSite.exists_isCovering_tautologicallyEquivalent_openCover`.

```lean
public theorem exists_isCovering_tautologicallyEquivalent_standardHCovering
    (B : BigHSite.{u}) (T : B.Schemes) [IsAffine (B.inclusion.obj T)]
    (𝒰 : PreZeroHypercover.{v} (B.inclusion.obj T))
    (hstandard : IsStandardHCovering 𝒰.f) :
    ∃ 𝒱 : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, 𝒱⟩ ∧
        PreZeroHypercover.TautologicallyEquivalent 𝒰 (𝒱.map B.inclusion)
```

## Tag 0EU1, a definition

[Tag 0EU1](https://stacks.math.columbia.edu/tag/0EU1) in the Stacks Project.

**`AlgebraicGeometry.BigHOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/H/BigSite.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/H/BigSite.lean#L178). The attribute's comment: “part (1), category”.

> **Stacks 0EU1, part (1).** The big h category of `S` is the slice of the chosen big h
> category over its object `S`.

```lean
public abbrev BigHOver
```

**`AlgebraicGeometry.BigHOver.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/H/BigSite.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/H/BigSite.lean#L193). The attribute's comment: “part (1), coverings”.

> **Stacks 0EU1, part (1).** A family in the slice covers precisely when its underlying
> family covers in the chosen big h site.

```lean
public abbrev IsCovering (E : Covering (BigHOver B S hS)) : Prop
```

**`AlgebraicGeometry.BigAffineH`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/H/BigSite.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/H/BigSite.lean#L209). The attribute's comment: “part (2), category”.

> **Stacks 0EU1, part (2).** The big affine h category is the full subcategory of affine
> objects in the big h category over `S`.

```lean
public abbrev BigAffineH
```

**`AlgebraicGeometry.BigAffineH.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/H/BigSite.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/H/BigSite.lean#L233). The attribute's comment: “part (2), coverings”.

> **Stacks 0EU1, part (2).** An affine family covers exactly when it covers in the big h
> site over `S` and is a standard h covering.

```lean
public abbrev IsCovering (E : Covering (BigAffineH B S hS)) : Prop
```

## Tag 0EU2, a lemma

[Tag 0EU2](https://stacks.math.columbia.edu/tag/0EU2) in the Stacks Project.

**`AlgebraicGeometry.BigAffineH.isSite`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigAffineSite.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigAffineSite.lean#L54).

> **Stacks 0EU2.** The standard h covering families of the affine objects of the big h
> category over `S` satisfy the site axioms.

```lean
public lemma BigAffineH.isSite (B : BigHSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    IsSite (BigAffineH.IsCovering B S hS)
```

## Tag 0EU3, a lemma

[Tag 0EU3](https://stacks.math.columbia.edu/tag/0EU3) in the Stacks Project.

**`AlgebraicGeometry.bigHSites_hasPullbacks_preservesPullbacks_final`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/H/Limits.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/H/Limits.lean#L132).

> **Stacks 0EU3.** Let `B` be a big h site containing the scheme `S`. The underlying
> categories of the big h site, of the big h site over `S`, and of the big affine h site over `S`
> have fibre products; in each case the canonical functor to the category of all schemes
> commutes with fibre products; and `S / S` is a final object of the big h site over `S`.

```lean
public theorem bigHSites_hasPullbacks_preservesPullbacks_final :
    (HasPullbacks B.Schemes ∧ HasPullbacks (BigHOver B S hS) ∧
        HasPullbacks (BigAffineH B S hS)) ∧
      (PreservesLimitsOfShape WalkingCospan B.inclusion ∧
        PreservesLimitsOfShape WalkingCospan (BigHOver.toScheme B S hS) ∧
        PreservesLimitsOfShape WalkingCospan (BigAffineH.toScheme B S hS)) ∧
      Nonempty (IsTerminal (Over.mk (𝟙 (B.obj S hS)) : BigHOver B S hS))
```

## Tag 0EU4, a lemma

[Tag 0EU4](https://stacks.math.columbia.edu/tag/0EU4) in the Stacks Project.

**`AlgebraicGeometry.BigAffineH.isCocontinuous_inclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AffineSiteEquivalence.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AffineSiteEquivalence.lean#L175). The attribute's comment: “cocontinuity”.

> Let `B` be a big h site containing a scheme `S`. The inclusion of the big affine h category
> over `S` into the big h category over `S` is cocontinuous for the two topologies of Stacks 0EU1.

```lean
public theorem isCocontinuous_inclusion :
    (inclusion B S hS).IsCocontinuous (topology B S hS) (BigHOver.topology B S hS)
```

**`AlgebraicGeometry.BigAffineH.isDenseSubsite_inclusion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AffineSiteEquivalence.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AffineSiteEquivalence.lean#L307). The attribute's comment: “equivalence of topoi”.

> Let `B` be a big h site containing a scheme `S`. The inclusion of the big affine h category
> over `S` into the big h category over `S` exhibits the big affine h site as a *dense subsite* of
> the big h site over `S`, in the sense of `CategoryTheory.Functor.IsDenseSubsite`; consequently
> the two halves of the induced morphism of topoi are equivalences of categories and
> `Sh((Aff/S)_h) ≃ Sh((Sch/S)_h)`.

```lean
public instance isDenseSubsite_inclusion :
    (inclusion B S hS).IsDenseSubsite (topology B S hS) (BigHOver.topology B S hS)
```

**`AlgebraicGeometry.BigAffineH.toposEquivInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AffineSiteEquivalence.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AffineSiteEquivalence.lean#L340). The attribute's comment: “equivalence of topoi”.

> The topos of set-valued sheaves on the big affine h site over `S` is equivalent to the topos
> of set-valued sheaves on the big h site over `S`, the equivalence being restriction along the
> inclusion.

```lean
public noncomputable def toposEquivInclusion :
    Sheaf (topology B S hS) (Type (u + 1)) ≌
      Sheaf (BigHOver.topology B S hS) (Type (u + 1))
```

## Tag 0EU5, a lemma

[Tag 0EU5](https://stacks.math.columbia.edu/tag/0EU5) in the Stacks Project.

**`AlgebraicGeometry.BigHOver.IsProperFinitePresentationSheaf.affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SheafCriterion.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SheafCriterion.lean#L246). The attribute's comment: “(2) implies (2′)”.

> **Stacks 0EU5, (2) implies (2′).** Condition (2′) is the restriction of condition (2) to
> an affine target, so it is implied by it with no use of condition (1).

```lean
public theorem IsProperFinitePresentationSheaf.affine
    (hF : BigHOver.IsProperFinitePresentationSheaf B S hS F) :
    BigHOver.IsAffineProperFinitePresentationSheaf B S hS F
```

**`AlgebraicGeometry.BigHOver.isZariskiSheaf_of_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SheafCriterion.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SheafCriterion.lean#L301). The attribute's comment: “only if, condition (1)”.

> **Stacks 0EU5, a sheaf satisfies condition (1).** A sheaf on the big h site over `S`
> satisfies the sheaf condition for Zariski coverings.
>
> A jointly surjective family of open immersions is a Zariski covering, hence a ph covering by
> Stacks 0DBH; its members are locally of finite presentation, so the family is an h
> covering.

```lean
public theorem isZariskiSheaf_of_isSheaf
    (hF : Presheaf.IsSheaf (BigHOver.topology B S hS) F) :
    BigHOver.IsZariskiSheaf B S hS F
```

**`AlgebraicGeometry.BigHOver.isProperFinitePresentationSheaf_of_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SheafCriterion.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SheafCriterion.lean#L319). The attribute's comment: “only if, condition (2)”.

> **Stacks 0EU5, a sheaf satisfies condition (2).** A sheaf on the big h site over `S`
> satisfies the sheaf condition for the one-element family attached to a morphism of the site
> which is proper, surjective and of finite presentation.
>
> Such a morphism is an h covering all by itself, by Stacks 0ETW.

```lean
public theorem isProperFinitePresentationSheaf_of_isSheaf
    (hF : Presheaf.IsSheaf (BigHOver.topology B S hS) F) :
    BigHOver.IsProperFinitePresentationSheaf B S hS F
```

**`AlgebraicGeometry.BigHOver.bijective_mapToEqualizer_of_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SheafCriterion.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SheafCriterion.lean#L341). The attribute's comment: “only if, condition (2) in equalizer form”.

> **Stacks 0EU5, condition (2) for a sheaf, in equalizer form.** Let `f : V ⟶ U` be a
> morphism of the big h category over `S` whose underlying morphism of schemes is proper,
> surjective and of finite presentation, and let `p₁, p₂ : W ⟶ V` complete `f` to a cartesian
> square, so that `W = V ×_U V`.  Then a sheaf `F` on the big h site over `S` maps `F(U)`
> bijectively onto the equalizer of the two maps `F(V) ⟶ F(W)`.
>
> This is the form in which the source states condition (2).  The case of an affine target `U`
> is condition (2′).

```lean
public theorem bijective_mapToEqualizer_of_isSheaf
    (hF : Presheaf.IsSheaf (BigHOver.topology B S hS) F)
    {V U W : BigHOver B S hS} (f : V ⟶ U) (p₁ p₂ : W ⟶ V)
    (hW : IsPullback p₁ p₂ f f)
    (hproper : IsProper ((BigHOver.toScheme B S hS).map f))
    (hsurj : Surjective ((BigHOver.toScheme B S hS).map f))
    (hfp : FinitePresentation ((BigHOver.toScheme B S hS).map f)) :
    Function.Bijective (regularTopology.mapToEqualizer F f p₁ p₂ hW.w)
```

**`AlgebraicGeometry.BigHOver.isProperFinitePresentationSheaf_of_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SheafCriterion.lean, line 587](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SheafCriterion.lean#L587). The attribute's comment: “(1) and (2′) imply (2)”.

> **Stacks 0EU5, (1) and (2′) imply (2).** Given the sheaf condition for Zariski coverings,
> the sheaf condition for a proper surjective morphism of finite presentation need only be
> checked when its target has affine underlying scheme.
>
> The target `X` is covered by the affine opens of its underlying scheme, a Zariski covering of
> the site; the base change of `f` over each of them has affine target, so condition (2′)
> applies, and the base change over a fibre product of two of them is separated by
> `properFP_pullback_isSeparated`.  The Zariski covering is strongly sheaf for `F` by condition
> (1), and `CategoryTheory.PreOneHypercover.IsStronglySheafFor.isSheafFor_of_pullback` assembles
> the local sheaf conditions into the sheaf condition for `{f}` itself.

```lean
public theorem isProperFinitePresentationSheaf_of_affine
    {F : (BigHOver B S hS)ᵒᵖ ⥤ Type v}
    (hZ : BigHOver.IsZariskiSheaf B S hS F)
    (hA : BigHOver.IsAffineProperFinitePresentationSheaf B S hS F) :
    BigHOver.IsProperFinitePresentationSheaf B S hS F
```

**`AlgebraicGeometry.BigHOver.isProperFinitePresentationSheaf_iff_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SheafCriterion.lean, line 627](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SheafCriterion.lean#L627). The attribute's comment: “given (1), (2) is equivalent to (2′)”.

> **Stacks 0EU5, the final assertion.** Given the sheaf condition for Zariski coverings,
> condition (2) of Stacks 0EU5 is equivalent to its restriction (2′) to morphisms whose target
> has affine underlying scheme.

```lean
public theorem isProperFinitePresentationSheaf_iff_affine
    {F : (BigHOver B S hS)ᵒᵖ ⥤ Type v}
    (hZ : BigHOver.IsZariskiSheaf B S hS F) :
    BigHOver.IsProperFinitePresentationSheaf B S hS F ↔
      BigHOver.IsAffineProperFinitePresentationSheaf B S hS F
```

**`AlgebraicGeometry.BigHOver.isSheaf_of_isZariskiSheaf_of_isProperFinitePresentationSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SheafCriterion.lean, line 1001](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SheafCriterion.lean#L1001). The attribute's comment: “if, (1) and (2) imply the sheaf condition”.

> **Stacks 0EU5, the sufficiency direction.** Conditions (1) and (2) together force a
> presheaf of sets on the big h category over `S` to be a sheaf for the h topology.

```lean
public theorem isSheaf_of_isZariskiSheaf_of_isProperFinitePresentationSheaf
    {F : (BigHOver B S hS)ᵒᵖ ⥤ Type v}
    (hZ : BigHOver.IsZariskiSheaf B S hS F)
    (hP : BigHOver.IsProperFinitePresentationSheaf B S hS F) :
    Presieve.IsSheaf (BigHOver.topology B S hS) F
```

**`AlgebraicGeometry.BigHOver.isSheaf_iff_isZariskiSheaf_and_isProperFinitePresentationSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SheafCriterion.lean, line 1032](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/SheafCriterion.lean#L1032). The attribute's comment: “sheaf characterization”.

> **Stacks 0EU5, the characterization.** A presheaf of sets on the big h category over `S` is
> a sheaf for the h topology if and only if it satisfies condition (1), the sheaf condition for
> Zariski coverings, and condition (2), the sheaf condition for every morphism of the site which
> is proper, surjective and of finite presentation.
>
> By `AlgebraicGeometry.isSheafFor_singleton_iff_bijective_mapToEqualizer` condition (2) is the
> source's requirement that the sections over the target map bijectively onto the equalizer of
> the two maps to the sections over `V ×_U V`.

```lean
public theorem isSheaf_iff_isZariskiSheaf_and_isProperFinitePresentationSheaf
    (B : BigHSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigHOver B S hS)ᵒᵖ ⥤ Type v) :
    Presheaf.IsSheaf (BigHOver.topology B S hS) F ↔
      (BigHOver.IsZariskiSheaf B S hS F ∧
        BigHOver.IsProperFinitePresentationSheaf B S hS F)
```

## Tag 0EU6, a lemma

[Tag 0EU6](https://stacks.math.columbia.edu/tag/0EU6) in the Stacks Project.

**`AlgebraicGeometry.isCocontinuous_bigHOverMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean#L76). The attribute's comment: “`u : V/T ↦ V/S` is cocontinuous”.

> **Stacks 0EU6.** The functor `u : (Sch/T)_h ⥤ (Sch/S)_h`, `V/T ↦ V/S`, is cocontinuous.

```lean
public theorem isCocontinuous_bigHOverMap :
    (Over.map f).IsCocontinuous (B.topology.over T) (B.topology.over S)
```

**`AlgebraicGeometry.isContinuous_bigHOverMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean#L83). The attribute's comment: “`u : V/T ↦ V/S` is continuous”.

> **Stacks 0EU6**, used in the proof. The functor `u : (Sch/T)_h ⥤ (Sch/S)_h`,
> `V/T ↦ V/S`, is continuous.

```lean
public theorem isContinuous_bigHOverMap :
    (Over.map f).IsContinuous (B.topology.over T) (B.topology.over S)
```

**`AlgebraicGeometry.bigHOverMapPullbackAdj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean#L90). The attribute's comment: “`v : U/S ↦ U ×_S T/T` is a right adjoint of `u`”.

> **Stacks 0EU6.** The functor `v : (Sch/S)_h ⥤ (Sch/T)_h` given by base change along `f` is
> a right adjoint of `u`: for `U/T` and `V/S` one has `Mor_S(u(U), V) = Mor_T(U, V ×_S T)`.

```lean
public noncomputable def bigHOverMapPullbackAdj : Over.map f ⊣ Over.pullback f
```

**`AlgebraicGeometry.isContinuous_bigHOverPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean#L102). The attribute's comment: “`v : U/S ↦ U ×_S T/T` is continuous”.

> **Stacks 0EU6.** The functor `v : (Sch/S)_h ⥤ (Sch/T)_h`, `U/S ↦ U ×_S T/T`, is
> continuous.

```lean
public theorem isContinuous_bigHOverPullback :
    (Over.pullback f).IsContinuous (B.topology.over S) (B.topology.over T)
```

**`AlgebraicGeometry.bigHMorphismOfTopoi_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean#L110). The attribute's comment: “`u` and `v` induce the same morphism of topoi `f_big`, direct images”.

> **Stacks 0EU6.** The functors `u` and `v` induce the same morphism of topoi: the direct
> image `{}_s u` attached to cocontinuity of `u` is the direct image `v^s` of
> `AlgebraicGeometry.bigHMorphismOfTopoi`.

```lean
public noncomputable def bigHMorphismOfTopoi_pushforwardIso :
    (Over.map f).sheafPushforwardCocontinuous (Type (u + 1))
        (B.topology.over T) (B.topology.over S) ≅
      (bigHMorphismOfTopoi B f).pushforward
```

**`AlgebraicGeometry.bigHMorphismOfTopoi_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean#L120). The attribute's comment: “`u` and `v` induce the same morphism of topoi `f_big`, inverse images”.

> **Stacks 0EU6.** The inverse image `(u^p -)^#` attached to cocontinuity of `u` is the
> inverse image of `AlgebraicGeometry.bigHMorphismOfTopoi`, namely plain restriction along `u`:
> the sheafification is unnecessary.

```lean
public noncomputable def bigHMorphismOfTopoi_inverseImageIso :
    (Over.map f).sheafPullbackCocontinuous (Type (u + 1))
        (B.topology.over T) (B.topology.over S) ≅
      (bigHMorphismOfTopoi B f).inverseImage
```

**`AlgebraicGeometry.bigHMorphismOfTopoi_inverseImage_obj_obj_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean#L129). The attribute's comment: “`f_big⁻¹(G)(U/T) = G(U/S)`”.

> **Stacks 0EU6**, the formula `f_big^{-1}(G)(U/T) = G(U/S)`.

```lean
public theorem bigHMorphismOfTopoi_inverseImage_obj_obj_obj
    (G : Sheaf (BigHOver.topology B S.obj S.property) (Type (u + 1))) (U : Over T) :
    ((bigHMorphismOfTopoi B f).inverseImage.obj G).obj.obj (op U) =
      G.obj.obj (op ((Over.map f).obj U))
```

**`AlgebraicGeometry.bigHMorphismOfTopoi_pushforward_obj_obj_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean#L137). The attribute's comment: “`f_big,*(F)(U/S) = F(U ×_S T/T)`”.

> **Stacks 0EU6**, the formula `f_{big,*}(F)(U/S) = F(U ×_S T/T)`.

```lean
public theorem bigHMorphismOfTopoi_pushforward_obj_obj_obj
    (F : Sheaf (BigHOver.topology B T.obj T.property) (Type (u + 1))) (U : Over S) :
    ((bigHMorphismOfTopoi B f).pushforward.obj F).obj.obj (op U) =
      F.obj.obj (op ((Over.pullback f).obj U))
```

**`AlgebraicGeometry.bigHSheafPushforwardCocontinuousObjIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean#L146). The attribute's comment: “`f_big,*(F)(U/S) = F(U ×_S T/T)`”.

> **Stacks 0EU6**, the formula `f_{big,*}(F)(U/S) = F(U ×_S T/T)` for the direct image
> `{}_s u` attached to cocontinuity of `u`.

```lean
public noncomputable def bigHSheafPushforwardCocontinuousObjIso
    (F : Sheaf (BigHOver.topology B T.obj T.property) (Type (u + 1))) (U : Over S) :
    (((Over.map f).sheafPushforwardCocontinuous (Type (u + 1))
        (B.topology.over T) (B.topology.over S)).obj F).obj.obj (op U) ≅
      F.obj.obj (op ((Over.pullback f).obj U))
```

**`AlgebraicGeometry.bigHLowerShriekAdj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean#L157). The attribute's comment: “`f_big⁻¹` has a left adjoint `f_big!`”.

> **Stacks 0EU6.** The inverse image `f_big^{-1}` has a left adjoint `f_{big!}`, namely the
> sheaf pullback along the continuous functor `u`.

```lean
public noncomputable def bigHLowerShriekAdj :
    (Over.map f).sheafPullback (Type (u + 1)) (B.topology.over T) (B.topology.over S) ⊣
      (bigHMorphismOfTopoi B f).inverseImage
```

**`AlgebraicGeometry.preservesLimitsOfShape_bigHLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean#L166). The attribute's comment: “`f_big!` commutes with fibre products and equalizers”.

> **Stacks 0EU6.** The left adjoint `f_{big!}` of `f_big^{-1}` commutes with fibre products
> and equalizers, and more generally with every finite connected limit.

```lean
public theorem preservesLimitsOfShape_bigHLowerShriek
    (I : Type t) [SmallCategory I] [FinCategory I] [IsConnected I] :
    PreservesLimitsOfShape I
      ((Over.map f).sheafPullback (Type (u + 1))
        (B.topology.over T) (B.topology.over S))
```

**`AlgebraicGeometry.preservesLimitsOfShape_walkingCospan_bigHLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean#L183). The attribute's comment: “`f_big!` commutes with fibre products and equalizers”.

> **Stacks 0EU6.** `f_{big!}` commutes with fibre products.

```lean
public theorem preservesLimitsOfShape_walkingCospan_bigHLowerShriek :
    PreservesLimitsOfShape WalkingCospan
      ((Over.map f).sheafPullback (Type (u + 1))
        (B.topology.over T) (B.topology.over S))
```

**`AlgebraicGeometry.preservesLimitsOfShape_walkingParallelPair_bigHLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/BigTopoiFormulas.lean#L191). The attribute's comment: “`f_big!` commutes with fibre products and equalizers”.

> **Stacks 0EU6.** `f_{big!}` commutes with equalizers.

```lean
public theorem preservesLimitsOfShape_walkingParallelPair_bigHLowerShriek :
    PreservesLimitsOfShape WalkingParallelPair
      ((Over.map f).sheafPullback (Type (u + 1))
        (B.topology.over T) (B.topology.over S))
```

Declarations registered for the tag:

- [`StacksRelocalization.sheafPushforwardOverMapIso`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/OverPullbackMorphism.lean#L51), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/BigHTopos.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/BigHTopos.lean#L34) (StacksFrontier): “same\_topos”.

## Tag 0EU7, a lemma

[Tag 0EU7](https://stacks.math.columbia.edu/tag/0EU7) in the Stacks Project.

**`AlgebraicGeometry.bigHMorphismOfTopoi_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/Composition.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/Composition.lean#L53). The attribute's comment: “direct image”.

> **Stacks 0EU7.** The direct image of the morphism of big h topoi attached to a composite
> is canonically isomorphic to the composite of the direct images.

```lean
public noncomputable def bigHMorphismOfTopoi_comp_pushforwardIso (B : BigHSite.{u})
    {X Y Z : B.Schemes} (f : X ⟶ Y) (g : Y ⟶ Z) :
    ((bigHMorphismOfTopoi B g).comp (bigHMorphismOfTopoi B f)).pushforward ≅
      (bigHMorphismOfTopoi B (f ≫ g)).pushforward
```

**`AlgebraicGeometry.bigHMorphismOfTopoi_comp_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/Composition.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/Composition.lean#L67). The attribute's comment: “inverse image”.

> **Stacks 0EU7.** The inverse image of the morphism of big h topoi attached to a composite
> is canonically isomorphic to the composite of the inverse images; the isomorphism is the
> adjunction mate of the comparison of direct images.

```lean
public noncomputable def bigHMorphismOfTopoi_comp_inverseImageIso (B : BigHSite.{u})
    {X Y Z : B.Schemes} (f : X ⟶ Y) (g : Y ⟶ Z) :
    ((bigHMorphismOfTopoi B g).comp (bigHMorphismOfTopoi B f)).inverseImage ≅
      (bigHMorphismOfTopoi B (f ≫ g)).inverseImage
```

**`AlgebraicGeometry.bigHMorphismOfTopoi_comp_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/Composition.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/Composition.lean#L79). The attribute's comment: “compatibility with the adjunction”.

> **Stacks 0EU7.** The comparisons of direct and inverse images for a composite respect the
> units of the geometric adjunctions, so together they form an isomorphism of morphisms of
> topoi.

```lean
public theorem bigHMorphismOfTopoi_comp_unit (B : BigHSite.{u}) {X Y Z : B.Schemes}
    (f : X ⟶ Y) (g : Y ⟶ Z)
    (V : Sheaf (BigHOver.topology B Z.obj Z.property) (Type (u + 1))) :
    (bigHMorphismOfTopoi B (f ≫ g)).adj.unit.app V ≫
        (bigHMorphismOfTopoi B (f ≫ g)).pushforward.map
          ((bigHMorphismOfTopoi_comp_inverseImageIso B f g).inv.app V) ≫
        (bigHMorphismOfTopoi_comp_pushforwardIso B f g).inv.app
          (((bigHMorphismOfTopoi B g).comp (bigHMorphismOfTopoi B f)).inverseImage.obj V) =
      ((bigHMorphismOfTopoi B g).comp (bigHMorphismOfTopoi B f)).adj.unit.app V
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.34, Tag 0ETQ](https://stacks.math.columbia.edu/tag/0ETQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
