---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsStandardVCovering, AlgebraicGeometry.isStandardVCovering_of_flat_affineCover, AlgebraicGeometry.StandardPHCovering.isStandardVCovering, AlgebraicGeometry.isStandardVCovering_pullback, AlgebraicGeometry.IsStandardVCovering.comp, AlgebraicGeometry.isStandardVCovering_tfae, AlgebraicGeometry.IsVCovering, AlgebraicGeometry.isVCovering_tfae
statement: formalized
proof: formalized
---

# 34.10 The V topology

Section 34.10 of the Stacks Project, [Tag 0ETA](https://stacks.math.columbia.edu/tag/0ETA). 14 tags here are carried by 24 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ETB, a definition

[Tag 0ETB](https://stacks.math.columbia.edu/tag/0ETB) in the Stacks Project.

**`AlgebraicGeometry.IsStandardVCovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/V/StandardCoverings.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/V/StandardCoverings.lean#L68).

> A finite family of morphisms from affine schemes to an affine scheme is a **standard V
> covering** if every morphism from the spectrum of a valuation ring lifts to one member
> after an extension of valuation rings.

```lean
public def IsStandardVCovering {T : Scheme.{u}} [IsAffine T] {I : Type v} [Finite I]
    (X : I → Scheme.{u}) [∀ i, IsAffine (X i)] (f : ∀ i, X i ⟶ T) : Prop
```

## Tag 0ETC, a lemma

[Tag 0ETC](https://stacks.math.columbia.edu/tag/0ETC) in the Stacks Project.

**`AlgebraicGeometry.isStandardVCovering_of_flat_affineCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/StandardFpqcCoverings.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/StandardFpqcCoverings.lean#L41).

> A standard fpqc covering of an affine scheme is a standard V covering.

```lean
theorem isStandardVCovering_of_flat_affineCover
    {T : Scheme.{u}} [IsAffine T] (𝒰 : T.AffineCover.{v} @Flat) [Finite 𝒰.I₀] :
    AlgebraicGeometry.IsStandardVCovering (fun i ↦ Spec (𝒰.X i)) 𝒰.f
```

## Tag 0ETD, a lemma

[Tag 0ETD](https://stacks.math.columbia.edu/tag/0ETD) in the Stacks Project.

**`AlgebraicGeometry.StandardPHCovering.isStandardVCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/V/PhComparison.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/V/PhComparison.lean#L50).

> A standard ph covering is a standard V covering.

```lean
public theorem StandardPHCovering.isStandardVCovering
    {T : Scheme.{u}} [IsAffine T] {I : Type v} {X : I → Scheme.{u}}
    {f : ∀ i, X i ⟶ T} (hf : StandardPHCovering f) :
    @IsStandardVCovering T _ I hf.finite X hf.isAffine f
```

## Tag 0ETE, a lemma

[Tag 0ETE](https://stacks.math.columbia.edu/tag/0ETE) in the Stacks Project.

**`AlgebraicGeometry.isStandardVCovering_pullback`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/V/StandardCoverings.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/V/StandardCoverings.lean#L91).

> A standard V covering of an affine scheme remains a standard V covering after pullback
> along a morphism from another affine scheme.

```lean
public lemma isStandardVCovering_pullback
    {T T' : Scheme.{u}} [IsAffine T] [IsAffine T']
    {I : Type v} [Finite I] (X : I → Scheme.{u}) [∀ i, IsAffine (X i)]
    (f : ∀ i, X i ⟶ T) (g : T' ⟶ T)
    (hf : IsStandardVCovering X f) :
    IsStandardVCovering (fun i ↦ pullback (f i) g)
      (fun i ↦ pullback.snd (f i) g)
```

## Tag 0ETF, a lemma

[Tag 0ETF](https://stacks.math.columbia.edu/tag/0ETF) in the Stacks Project.

**`AlgebraicGeometry.IsStandardVCovering.comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/V/StandardCoverings.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/V/StandardCoverings.lean#L107).

> Composing a standard V covering with a standard V covering of each member gives a
> standard V covering.

```lean
public lemma IsStandardVCovering.comp
    {T : Scheme.{u}} [IsAffine T]
    {J : Type v} [Finite J] (X : J → Scheme.{u}) [∀ j, IsAffine (X j)]
    (f : ∀ j, X j ⟶ T) (hf : IsStandardVCovering X f)
    {I : J → Type w} [∀ j, Finite (I j)]
    (Y : ∀ j, I j → Scheme.{u}) [∀ j i, IsAffine (Y j i)]
    (g : ∀ j i, Y j i ⟶ X j)
    (hg : ∀ j, IsStandardVCovering (Y j) (g j)) :
    IsStandardVCovering (fun ji : Σ j, I j ↦ Y ji.1 ji.2)
      (fun ji ↦ g ji.1 ji.2 ≫ f ji.1)
```

## Tag 0ETG, a lemma

[Tag 0ETG](https://stacks.math.columbia.edu/tag/0ETG) in the Stacks Project.

**`AlgebraicGeometry.isStandardVCovering_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/V/StandardCoverings.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/V/StandardCoverings.lean#L150).

> A finite family of affine schemes over an affine scheme is a standard V covering if and only
> if it admits a refining standard V covering, if and only if the morphism from the disjoint union
> of the family is a standard V covering.

```lean
public theorem isStandardVCovering_tfae {T : Scheme.{u}} [IsAffine T]
    {I : Type v} [Finite I] (X : I → Scheme.{u}) [∀ i, IsAffine (X i)]
    (f : ∀ i, X i ⟶ T) :
    List.TFAE [
      IsStandardVCovering X f,
      ∃ (K : Type v) (_ : Finite K) (Y : K → Scheme.{u}) (_ : ∀ k, IsAffine (Y k))
          (g : ∀ k, Y k ⟶ T),
        IsStandardVCovering Y g ∧
          Nonempty
            (({ I₀ := K, X := Y, f := g } : PreZeroHypercover T).Hom
              ({ I₀ := I, X := X, f := f } : PreZeroHypercover T)),
      IsStandardVCovering
        (fun _ : Unit ↦ ∐ X) (fun _ ↦ Sigma.desc f)]
```

## Tag 0ETH, a definition

[Tag 0ETH](https://stacks.math.columbia.edu/tag/0ETH) in the Stacks Project.

**`AlgebraicGeometry.IsVCovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/V/Coverings.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/V/Coverings.lean#L48).

> **Stacks 0ETH.** A family of morphisms of schemes is a **V covering** if, over every
> affine open of the target, a finite standard V covering by affine schemes refines the
> pullback of the family.

```lean
public noncomputable def IsVCovering {T : Scheme.{u}} {I : Type v}
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T) : Prop
```

## Tag 0ETI, a lemma

[Tag 0ETI](https://stacks.math.columbia.edu/tag/0ETI) in the Stacks Project.

**`AlgebraicGeometry.isVCovering_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/VCoveringRefinement.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/VCoveringRefinement.lean#L241).

> A family of morphisms of schemes is a V covering if and only if a V covering refines it,
> if and only if its disjoint-union morphism is a V covering.

```lean
public theorem isVCovering_tfae {T : Scheme.{u}} {I : Type v} [Small.{u} I]
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T) :
    List.TFAE [
      IsVCovering X f,
      ∃ (K : Type v) (Y : K → Scheme.{u}) (g : ∀ k, Y k ⟶ T),
        IsVCovering Y g ∧
          Nonempty
            (({ I₀ := K, X := Y, f := g } : PreZeroHypercover T).Hom
              ({ I₀ := I, X := X, f := f } : PreZeroHypercover T)),
      IsVCovering
        (fun _ : Unit ↦ ∐ X) (fun _ ↦ Sigma.desc f)]
```

## Tag 0ETJ, a lemma

[Tag 0ETJ](https://stacks.math.columbia.edu/tag/0ETJ) in the Stacks Project.

**`AlgebraicGeometry.isVCovering_of_isIso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/Permanence.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/Permanence.lean#L69). The attribute's comment: “isomorphism”.

> An isomorphism of schemes, regarded as a singleton family, is a V covering.

```lean
lemma isVCovering_of_isIso {T' T : Scheme.{u}} (f : T' ⟶ T) [IsIso f] :
    AlgebraicGeometry.IsVCovering (fun _ : Unit ↦ T') (fun _ ↦ f)
```

**`AlgebraicGeometry.isVCovering_pullback`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/Permanence.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/Permanence.lean#L89). The attribute's comment: “base\_change”.

> The pullback of a V covering along any morphism of schemes is a V covering.

```lean
lemma isVCovering_pullback {T : Scheme.{u}} {I : Type v}
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T) {T' : Scheme.{u}}
    (g : T' ⟶ T) (hf : AlgebraicGeometry.IsVCovering X f) :
    AlgebraicGeometry.IsVCovering
      (fun i ↦ pullback (f i) g)
      (fun i ↦ pullback.snd (f i) g)
```

**`AlgebraicGeometry.IsVCovering.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/Permanence.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/Permanence.lean#L192). The attribute's comment: “composition”.

> Composing a V covering with V coverings of each of its members gives a V
> covering.

```lean
theorem IsVCovering.comp {T : Scheme.{u}} {I : Type v}
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T)
    (hf : AlgebraicGeometry.IsVCovering X f) {J : I → Type w}
    (Y : ∀ i, J i → Scheme.{u}) (g : ∀ i j, Y i j ⟶ X i)
    (hg : ∀ i, AlgebraicGeometry.IsVCovering (Y i) (g i)) :
    AlgebraicGeometry.IsVCovering
      (fun ij : Σ i, J i ↦ Y ij.1 ij.2)
      (fun ij ↦ g ij.1 ij.2 ≫ f ij.1)
```

## Tag 0ETK, a lemma

[Tag 0ETK](https://stacks.math.columbia.edu/tag/0ETK) in the Stacks Project.

**`AlgebraicGeometry.isVCovering_of_mem_fpqcPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/V/FpqcComparison.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/V/FpqcComparison.lean#L66). The attribute's comment: “fpqc\_v”.

> **Stacks 0ETK.** Every fpqc covering is a V covering.
>
> Above an affine open of the target, Stacks 022E refines the base change of the family by a
> standard fpqc covering, and Stacks 0ETC says that a standard fpqc covering is a standard V
> covering.

```lean
public theorem isVCovering_of_mem_fpqcPrecoverage {T : Scheme.{u}} {I : Type v}
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T)
    (hf : Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage T) :
    IsVCovering X f
```

**`AlgebraicGeometry.isVCovering_of_mem_fppfPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/V/FpqcComparison.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/V/FpqcComparison.lean#L89). The attribute's comment: “fppf\_v”.

> **Stacks 0ETK.** Every fppf covering is a V covering, being an fpqc covering by
> Stacks 022C.

```lean
public theorem isVCovering_of_mem_fppfPrecoverage {T : Scheme.{u}} {I : Type v}
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T)
    (hf : Presieve.ofArrows X f ∈ Scheme.fppfPrecoverage T) :
    IsVCovering X f
```

**`AlgebraicGeometry.isVCovering_of_mem_syntomicPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/V/FpqcComparison.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/V/FpqcComparison.lean#L98). The attribute's comment: “syntomic\_v”.

> **Stacks 0ETK.** Every syntomic covering is a V covering, being an fpqc covering by
> Stacks 022C.

```lean
public theorem isVCovering_of_mem_syntomicPrecoverage {T : Scheme.{u}} {I : Type v}
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T)
    (hf : Presieve.ofArrows X f ∈
      Scheme.precoverage (@Syntomic : MorphismProperty Scheme.{u}) T) :
    IsVCovering X f
```

**`AlgebraicGeometry.isVCovering_of_mem_smoothPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/V/FpqcComparison.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/V/FpqcComparison.lean#L108). The attribute's comment: “smooth\_v”.

> **Stacks 0ETK.** Every smooth covering is a V covering, being an fpqc covering by
> Stacks 022C.

```lean
public theorem isVCovering_of_mem_smoothPrecoverage {T : Scheme.{u}} {I : Type v}
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T)
    (hf : Presieve.ofArrows X f ∈
      Scheme.precoverage (@Smooth : MorphismProperty Scheme.{u}) T) :
    IsVCovering X f
```

**`AlgebraicGeometry.isVCovering_of_mem_etalePrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/V/FpqcComparison.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/V/FpqcComparison.lean#L118). The attribute's comment: “etale\_v”.

> **Stacks 0ETK.** Every étale covering is a V covering, being an fpqc covering by
> Stacks 022C.

```lean
public theorem isVCovering_of_mem_etalePrecoverage {T : Scheme.{u}} {I : Type v}
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T)
    (hf : Presieve.ofArrows X f ∈ Scheme.etalePrecoverage T) :
    IsVCovering X f
```

**`AlgebraicGeometry.isVCovering_of_mem_zariskiPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/V/FpqcComparison.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/V/FpqcComparison.lean#L127). The attribute's comment: “zariski\_v”.

> **Stacks 0ETK.** Every Zariski covering is a V covering, being an fpqc covering by
> Stacks 022C.

```lean
public theorem isVCovering_of_mem_zariskiPrecoverage {T : Scheme.{u}} {I : Type v}
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T)
    (hf : Presieve.ofArrows X f ∈ Scheme.zariskiPrecoverage T) :
    IsVCovering X f
```

**`AlgebraicGeometry.isVCovering_of_isPHCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/V/PhComparison.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/V/PhComparison.lean#L162). The attribute's comment: “ph\_v”.

> **Stacks 0ETK.** Every ph covering is a V covering. It needs no finiteness hypothesis on the
> members of the family.
>
> This is also one half of Stacks 0ETR, which for a family locally of finite presentation asserts
> that being a ph covering and being a V covering are *equivalent*; it carries no 0ETR
> registration. The two conditions 0ETR compares are the numbered items of one assertion, that
> equivalence, so a single implication is a fragment of that assertion and not a part of it; 0ETR
> belongs where the equivalence is stated in full, which is
> `AlgebraicGeometry.isPHCovering_iff_isVCovering` in
> `StacksFrontier/AlgebraicGeometry/Topologies/V/PhVFlatteningModification.lean`. The converse
> implication is `AlgebraicGeometry.isPHCovering_of_isVCovering`, which carries
> `AlgebraicGeometry.StandardVCoveringHasPHRefinement`; the inputs the Stacks argument needs for
> that predicate are the generic flatness stratification of the base (Stacks 0H3Z),
> `AlgebraicGeometry.finitePresentationHasFlatStratification`, and the Raynaud-Gruson flattening
> theorem for an admissible blowup (Stacks 0815), and both are available.

```lean
public theorem isVCovering_of_isPHCovering {T : Scheme.{u}} {I : Type v}
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T)
    (hph : IsPHCovering X f) :
    IsVCovering X f
```

## Tag 0ETL, a definition

[Tag 0ETL](https://stacks.math.columbia.edu/tag/0ETL) in the Stacks Project.

**`AlgebraicGeometry.IsVSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/V/Coverings.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/V/Coverings.lean#L72).

> **Stacks 0ETL.** A set-valued presheaf on schemes is a sheaf for the V topology if it
> satisfies the sheaf condition for every V covering family.

```lean
public abbrev IsVSheaf (F : Scheme.{u}ᵒᵖ ⥤ Type w) : Prop
```

## Tag 0ETM, a lemma

[Tag 0ETM](https://stacks.math.columbia.edu/tag/0ETM) in the Stacks Project.

**`AlgebraicGeometry.isVSheaf_iff_zariski_and_standard`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/Sheaves.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/Sheaves.lean#L471). The attribute's comment: “Zariski and standard V criterion”.

> **Stacks Project, Tag 0ETM.** The V sheaf condition is equivalent to the
> Zariski sheaf condition together with the sheaf condition for all standard V
> coverings.

```lean
theorem isVSheaf_iff_zariski_and_standard
    (F : Scheme.{u}ᵒᵖ ⥤ Type w) :
    AlgebraicGeometry.IsVSheaf.{u, max u v, w} F ↔
      (∀ (T : Scheme.{u}) (𝒰 : T.OpenCover.{max u v}),
        (Presieve.ofArrows 𝒰.X 𝒰.f).IsSheafFor F) ∧
      (∀ (T : Scheme.{u}) [IsAffine T] (I : Type (max u v)) [Finite I]
        (X : I → Scheme.{u}) [∀ i, IsAffine (X i)] (f : ∀ i, X i ⟶ T),
        AlgebraicGeometry.IsStandardVCovering X f →
          (Presieve.ofArrows X f).IsSheafFor F)
```

**`AlgebraicGeometry.isStandardVSheaf_iff_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/Sheaves.lean, line 526](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/Sheaves.lean#L526). The attribute's comment: “single-arrow standard V criterion”.

> **Stacks Project, Tag 0ETM, moreover.** Under the Zariski sheaf condition,
> the sheaf condition for standard V coverings can be tested on one-arrow
> standard V coverings.

```lean
theorem isStandardVSheaf_iff_singleton
    (F : Scheme.{u}ᵒᵖ ⥤ Type w)
    (hZ : ∀ (T : Scheme.{u}) (𝒰 : T.OpenCover.{max u v}),
      (Presieve.ofArrows 𝒰.X 𝒰.f).IsSheafFor F) :
    (∀ (T : Scheme.{u}) [IsAffine T] (I : Type (max u v)) [Finite I]
      (X : I → Scheme.{u}) [∀ i, IsAffine (X i)] (f : ∀ i, X i ⟶ T),
      AlgebraicGeometry.IsStandardVCovering X f →
        (Presieve.ofArrows X f).IsSheafFor F) ↔
    (∀ (T X : Scheme.{u}) [IsAffine T] [IsAffine X] (f : X ⟶ T),
      AlgebraicGeometry.IsStandardVCovering (fun _ : Unit ↦ X) (fun _ ↦ f) →
        (Presieve.ofArrows (fun _ : Unit ↦ X) (fun _ ↦ f)).IsSheafFor F)
```

## Tag 0ETN, a lemma

[Tag 0ETN](https://stacks.math.columbia.edu/tag/0ETN) in the Stacks Project.

**`AlgebraicGeometry.isVCovering_iff_valuation_lifting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/QuasiCompactCoverings.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/QuasiCompactCoverings.lean#L157). The attribute's comment: “part (1) iff part (2)”.

> A quasi-compact morphism is a singleton V covering exactly when every map from
> a valuation spectrum lifts after an extension of valuation rings.

```lean
theorem isVCovering_iff_valuation_lifting {X Y : Scheme.{u}} (f : X ⟶ Y)
    [QuasiCompact f] :
    AlgebraicGeometry.IsVCovering (fun _ : Unit ↦ X) (fun _ ↦ f) ↔
      (∀ (V : Type u) [CommRing V] [IsDomain V] [ValuationRing V]
        (g : Spec (.of V) ⟶ Y),
        ∃ (W : Type u) (_ : CommRing W) (_ : IsDomain W) (_ : ValuationRing W)
          (e : V →+* W),
          AlgebraicGeometry.IsExtensionOfValuationRings e ∧
            ∃ (h : Spec (.of W) ⟶ X),
              Spec.map (CommRingCat.ofHom e) ≫ g = h ≫ f)
```

**`AlgebraicGeometry.valuation_lifting_iff_specialization_lifting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/QuasiCompactCoverings.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Vtopology/QuasiCompactCoverings.lean#L252). The attribute's comment: “part (2) iff part (3)”.

> Valuation-ring lifting is equivalent to lifting every specialization after
> arbitrary base change.

```lean
theorem valuation_lifting_iff_specialization_lifting {X Y : Scheme.{u}}
    (f : X ⟶ Y) :
    (∀ (V : Type u) [CommRing V] [IsDomain V] [ValuationRing V]
      (g : Spec (.of V) ⟶ Y),
      ∃ (W : Type u) (_ : CommRing W) (_ : IsDomain W) (_ : ValuationRing W)
        (e : V →+* W),
        AlgebraicGeometry.IsExtensionOfValuationRings e ∧
          ∃ (h : Spec (.of W) ⟶ X),
            Spec.map (CommRingCat.ofHom e) ≫ g = h ≫ f) ↔
      (∀ (Z : Scheme.{u}) (g : Z ⟶ Y) (z' z : Z),
        z' ⤳ z →
          ∃ (w' w : (pullback g f : Scheme.{u})),
            (w' ⤳ w) ∧
              (pullback.fst g f) w' = z' ∧
                (pullback.fst g f) w = z)
```

## Tag 0ETP, a lemma

[Tag 0ETP](https://stacks.math.columbia.edu/tag/0ETP) in the Stacks Project.

**`AlgebraicGeometry.isVCovering_universallySubmersive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/VCoveringSubmersive.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/VCoveringSubmersive.lean#L191).

> **Stacks Project, Tag 0ETP.** The morphism from the disjoint union of a
> V covering to its target is universally submersive.

```lean
public theorem isVCovering_universallySubmersive {T : Scheme.{u}} {I : Type v}
    [Small.{u} I] (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T)
    (hf : IsVCovering X f) :
    universally (topologically @Topology.IsQuotientMap) (Sigma.desc f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 34.10, Tag 0ETA](https://stacks.math.columbia.edu/tag/0ETA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
