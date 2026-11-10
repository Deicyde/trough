---
declaration: section
origin: cited
lean: RingHom.finitePresentation_of_comp_of_faithfullyFlat, RingHom.finiteType_of_comp_of_faithfullyFlat_of_finitePresentation, AlgebraicGeometry.locallyOfFinitePresentation_of_comp_of_fppf, AlgebraicGeometry.locallyOfFiniteType_of_comp_of_fppf, Stacks.Smooth.smooth_of_comp_surjective_smooth, Stacks.Etale.etale_of_comp_surjective_etale, Stacks.Syntomic.syntomic_of_comp, Stacks.Smooth.smooth_of_comp_of_fppf
statement: formalized
proof: formalized
---

# 35.14 Descent of finiteness and smoothness properties of morphisms

Section 35.14 of the Stacks Project, [Tag 02KJ](https://stacks.math.columbia.edu/tag/02KJ). 7 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02KK, a lemma

[Tag 02KK](https://stacks.math.columbia.edu/tag/02KK) in the Stacks Project.

**`RingHom.finitePresentation_of_comp_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/MorphismProperty/FaithfullyFlatRing.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/MorphismProperty/FaithfullyFlatRing.lean#L98). References: EGA IV (11.3.17), “finite presentation case”; EGA IV (11.3.16), “affine, fin. pres. case”; SGA 3 V (9.1), “affine, finite pres.”; SGA 3 XIX (2.1), “special case”.

> **Stacks Project, Tag 02KK.** If `R → B` is of finite presentation and `A → B` is
> faithfully flat and of finite presentation, then `R → A` is of finite presentation.

```lean
theorem finitePresentation_of_comp_of_faithfullyFlat
    {R : Type u} {A : Type v} {B : Type w} [CommRing R] [CommRing A] [CommRing B]
    (f : R →+* A) (g : A →+* B) (hcomp : (g.comp f).FinitePresentation)
    (hff : g.FaithfullyFlat) (hfp : g.FinitePresentation) : f.FinitePresentation
```

## Tag 0367, a lemma

[Tag 0367](https://stacks.math.columbia.edu/tag/0367) in the Stacks Project.

**`RingHom.finiteType_of_comp_of_faithfullyFlat_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/MorphismProperty/FaithfullyFlatRing.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/MorphismProperty/FaithfullyFlatRing.lean#L167). References: EGA IV (11.3.17), “finite type case”; EGA IV (11.3.16), “affine, finite type case”; EGA IV (17.7.5), “affine schemes”; SGA 3 V (9.1), “affine, finite type”.

> **Stacks Project, Tag 0367.** If `R → A → B` are ring maps, the
> composite is of finite type, and `A → B` is faithfully flat and of finite
> presentation, then `R → A` is of finite type.

```lean
theorem finiteType_of_comp_of_faithfullyFlat_of_finitePresentation
    {R : Type u} {A : Type v} {B : Type w}
    [CommRing R] [CommRing A] [CommRing B]
    {f : R →+* A} {g : A →+* B}
    (hgf : (g.comp f).FiniteType) (hflat : g.FaithfullyFlat)
    (hfp : g.FinitePresentation) :
    f.FiniteType
```

## Tag 02KL, a lemma

[Tag 02KL](https://stacks.math.columbia.edu/tag/02KL) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFinitePresentation_of_comp_of_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/MorphismProperty/LocalFiniteness.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/MorphismProperty/LocalFiniteness.lean#L183). The attribute's comment: “locally of finite presentation”. References: EGA IV (17.7.5), “(ii)”; EGA IV (11.3.16), “loc. fin. presentation”.

> **Stacks Project, Tag 02KL (finite-presentation case).** Local finite presentation
> descends through a surjective flat morphism which is locally of finite presentation.

```lean
theorem locallyOfFinitePresentation_of_comp_of_fppf
    {X Y S : Scheme.{u}} (f : X ⟶ Y) (q : Y ⟶ S)
    [Surjective f] [Flat f] [LocallyOfFinitePresentation f]
    [LocallyOfFinitePresentation (f ≫ q)] :
    LocallyOfFinitePresentation q
```

**`AlgebraicGeometry.locallyOfFiniteType_of_comp_of_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/MorphismProperty/LocalFiniteness.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/MorphismProperty/LocalFiniteness.lean#L196). The attribute's comment: “locally of finite type”. References: EGA IV (17.7.5), “(i)”; EGA IV (11.3.16), “locally of finite type”.

> **Stacks Project, Tag 02KL (finite-type case).** Local finite type descends through a
> surjective flat morphism which is locally of finite presentation.

```lean
theorem locallyOfFiniteType_of_comp_of_fppf
    {X Y S : Scheme.{u}} (f : X ⟶ Y) (q : Y ⟶ S)
    [Surjective f] [Flat f] [LocallyOfFinitePresentation f]
    [LocallyOfFiniteType (f ≫ q)] :
    LocallyOfFiniteType q
```

## Tag 02KM, a lemma

[Tag 02KM](https://stacks.math.columbia.edu/tag/02KM) in the Stacks Project.

**`Stacks.Smooth.smooth_of_comp_surjective_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SmoothDescent.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SmoothDescent.lean#L143). The attribute's comment: “smooth\_case”.

> **Stacks Project, Tag 02KM (smooth case).** If `f` is surjective and smooth and `f ≫ q` is
> smooth, then `q` is smooth.
>
> This is also Stacks 02K5: there the target of `f ≫ q` is additionally assumed locally of finite
> presentation, which that source's own footnote observes is implied by the other hypotheses.

```lean
theorem smooth_of_comp_surjective_smooth (f : X ⟶ Y) (q : Y ⟶ S) [Surjective f] [Smooth f]
    [Smooth (f ≫ q)] : Smooth q
```

**`Stacks.Etale.etale_of_comp_surjective_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SurjectiveEtaleDescent.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SurjectiveEtaleDescent.lean#L76). The attribute's comment: “etale\_case”. References: EGA IV (17.7.5), “special case”.

> **Stacks 02KM**, étale case. If `f : X ⟶ Y` is surjective and étale and the composite
> `f ≫ q` is étale, then `q : Y ⟶ S` is étale.
>
> The missing hypothesis of Tag 02K6, that `q` be locally of finite presentation, follows from
> Tag 02KL: `f` is surjective, flat and locally of finite presentation, and `f ≫ q` is locally
> of finite presentation because it is étale.

```lean
theorem etale_of_comp_surjective_etale {X Y S : Scheme.{u}}
    (f : X ⟶ Y) (q : Y ⟶ S) [Surjective f] [Etale f] [Etale (f ≫ q)] :
    Etale q
```

**`Stacks.Syntomic.syntomic_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SyntomicLciDescent.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SyntomicLciDescent.lean#L317). The attribute's comment: “syntomic\_case”.

> **Stacks Project, Tag 02KM (syntomic case).** Syntomicity descends along a surjective
> syntomic morphism: if `f : X ⟶ Y` is surjective and syntomic and `f ≫ q` is syntomic, then
> `q : Y ⟶ S` is syntomic.
>
> This is the syntomic one of the lemma's three cases; the étale case is
> `Stacks.Etale.etale_of_comp_surjective_etale` and the smooth case is
> `Stacks.Smooth.smooth_of_comp_surjective_smooth`.

```lean
theorem syntomic_of_comp (f : X ⟶ Y) (q : Y ⟶ S) [Surjective f] (hf : Syntomic f)
    (hcomp : Syntomic (f ≫ q)) : Syntomic q
```

## Tag 05B5, a lemma

[Tag 05B5](https://stacks.math.columbia.edu/tag/05B5) in the Stacks Project.

**`Stacks.Smooth.smooth_of_comp_of_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SmoothDescent.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SmoothDescent.lean#L116). The attribute's comment: “smooth\_permanence”.

> **Stacks Project, Tag 05B5 (smooth case).** Smoothness descends along a surjective flat
> morphism which is locally of finite presentation: if `f : X ⟶ Y` is surjective, flat and locally
> of finite presentation and `f ≫ q` is smooth, then `q : Y ⟶ S` is smooth.

```lean
theorem smooth_of_comp_of_fppf (f : X ⟶ Y) (q : Y ⟶ S) [Surjective f] [Flat f]
    [LocallyOfFinitePresentation f] [Smooth (f ≫ q)] : Smooth q
```

**`Stacks.Etale.etale_of_comp_of_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Descent.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Descent.lean#L169). The attribute's comment: “etale\_permanence”.

> **Stacks Project, Tag 05B5 (étale case).** Étaleness descends along a surjective flat
> morphism which is locally of finite presentation: if `f : X ⟶ Y` is surjective, flat and locally
> of finite presentation and `f ≫ q` is étale, then `q : Y ⟶ S` is étale.

```lean
theorem etale_of_comp_of_fppf (f : X ⟶ Y) (q : Y ⟶ S) [Surjective f] [Flat f]
    [LocallyOfFinitePresentation f] [Etale (f ≫ q)] : Etale q
```

## Tag 05B7, a lemma

[Tag 05B7](https://stacks.math.columbia.edu/tag/05B7) in the Stacks Project.

**`AlgebraicGeometry.syntomic_of_comp_of_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SyntomicDescent.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SyntomicDescent.lean#L130). The attribute's comment: “q\_syntomic”.

> **Stacks Project, Tag 05B7.** Syntomicity descends along a surjective flat morphism which is
> locally of finite presentation: if `f : X ⟶ Y` is surjective, flat and locally of finite
> presentation and `f ≫ q` is syntomic, then `q : Y ⟶ S` is syntomic.

```lean
theorem syntomic_of_comp_of_fppf (f : X ⟶ Y) (q : Y ⟶ S) [Surjective f] [Flat f]
    [LocallyOfFinitePresentation f] (hp : Syntomic (f ≫ q)) : Syntomic q
```

**`AlgebraicGeometry.syntomic_of_syntomic_comp_of_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Descent/Fppf.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Descent/Fppf.lean#L101). The attribute's comment: “f\_syntomic”.

> **Stacks Project, Tag 05B7.** A surjective flat morphism locally of finite presentation is
> syntomic as soon as its composite with another morphism is syntomic.

```lean
theorem syntomic_of_syntomic_comp_of_fppf [Surjective f] [Flat f]
    [LocallyOfFinitePresentation f] (hp : Syntomic (f ≫ q)) : Syntomic f
```

**`AlgebraicGeometry.syntomic_of_syntomic_comp_of_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FactorSyntomic.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FactorSyntomic.lean#L198). The attribute's comment: “f\_syntomic”.

> If `f : X ⟶ Y` is surjective, flat and locally of finite presentation and `f ≫ q` is
> syntomic, then `f` is syntomic.

```lean
theorem syntomic_of_syntomic_comp_of_fppf (f : X ⟶ Y) (q : Y ⟶ S) [Surjective f] [Flat f]
    [LocallyOfFinitePresentation f] (hcomp : Syntomic (f ≫ q)) : Syntomic f
```

## Tag 06NB, a lemma

[Tag 06NB](https://stacks.math.columbia.edu/tag/06NB) in the Stacks Project.

**`AlgebraicGeometry.flat_of_comp_of_fppf_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/MorphismProperty/FppfRefinement.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/MorphismProperty/FppfRefinement.lean#L114). The attribute's comment: “flat”.

> **Stacks Project, Tag 06NB (flat).** If `f ≫ g` is flat and the singleton family
> consisting of `f` is refined by an fppf covering of `Y`, then `g` is flat.

```lean
theorem flat_of_comp_of_fppf_refinement
    {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z) [Flat (f ≫ g)]
    (h : ∃ 𝒰 : Y.Cover.{v} Scheme.fppfPrecoverage,
      Nonempty (𝒰.toPreZeroHypercover.Hom (PreZeroHypercover.singleton f))) :
    Flat g
```

**`AlgebraicGeometry.locallyOfFiniteType_of_comp_of_fppf_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/MorphismProperty/FppfRefinement.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/MorphismProperty/FppfRefinement.lean#L199). The attribute's comment: “locally\_finite\_type”.

> **Stacks Project, Tag 06NB (locally finite type).** If `f ≫ g` is locally of finite type
> and the singleton family consisting of `f` is refined by an fppf covering of `Y`, then `g` is
> locally of finite type.

```lean
theorem locallyOfFiniteType_of_comp_of_fppf_refinement
    {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z) [LocallyOfFiniteType (f ≫ g)]
    (h : ∃ 𝒰 : Y.Cover.{v} Scheme.fppfPrecoverage,
      Nonempty (𝒰.toPreZeroHypercover.Hom (PreZeroHypercover.singleton f))) :
    LocallyOfFiniteType g
```

**`AlgebraicGeometry.locallyOfFinitePresentation_of_comp_of_fppf_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/MorphismProperty/FppfRefinement.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/MorphismProperty/FppfRefinement.lean#L249). The attribute's comment: “locally\_finite\_presentation”.

> **Stacks Project, Tag 06NB (locally finite presentation).** If `f ≫ g` is locally of
> finite presentation and the singleton family consisting of `f` is refined by an fppf covering
> of `Y`, then `g` is locally of finite presentation.

```lean
theorem locallyOfFinitePresentation_of_comp_of_fppf_refinement
    {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z) [LocallyOfFinitePresentation (f ≫ g)]
    (h : ∃ 𝒰 : Y.Cover.{v} Scheme.fppfPrecoverage,
      Nonempty (𝒰.toPreZeroHypercover.Hom (PreZeroHypercover.singleton f))) :
    LocallyOfFinitePresentation g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.14, Tag 02KJ](https://stacks.math.columbia.edu/tag/02KJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
