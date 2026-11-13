---
declaration: section
origin: cited
lean: AlgebraicGeometry.ConnectedAlongSection.mem_locus_iff_asFiber_mem, AlgebraicGeometry.ConnectedAlongSection.ofGrpObj, AlgebraicGeometry.GroupScheme.neutralLocus, AlgebraicGeometry.GroupScheme.fiberι_preimage_neutralLocus, AlgebraicGeometry.ConnectedAlongSection, AlgebraicGeometry.ConnectedAlongSection.fiberComponent, AlgebraicGeometry.ConnectedAlongSection.locus, AlgebraicGeometry.ConnectedAlongSection.locus_eq_preimage_of_isPullback
statement: formalized
proof: formalized
---

# 37.29 Connected components meeting a section

Section 37.29 of the Stacks Project, [Tag 055K](https://stacks.math.columbia.edu/tag/055K). 7 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 055K, the section

[Tag 055K](https://stacks.math.columbia.edu/tag/055K) in the Stacks Project.

**`AlgebraicGeometry.ConnectedAlongSection.mem_locus_iff_asFiber_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ConnectedComponentSection/GroupScheme.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ConnectedComponentSection/GroupScheme.lean#L57). The attribute's comment: “Situation 055L: X⁰ = ⋃\_y X⁰\_y, pointwise”.

> For a morphism `f : X ⟶ Y` with a section `s`, the subset `X⁰ = ⋃_y X⁰_y` of `X` consists of
> the points `x` which, viewed as points of their own fibre `X_{f(x)}`, lie in the connected
> component `X⁰_{f(x)}` of that fibre containing `s(f(x))`.

```lean
theorem mem_locus_iff_asFiber_mem (D : ConnectedAlongSection.{u}) (x : D.X) :
    x ∈ D.locus ↔ D.f.asFiber x ∈ D.fiberComponent (D.f x)
```

**`AlgebraicGeometry.ConnectedAlongSection.ofGrpObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ConnectedComponentSection/GroupScheme.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ConnectedComponentSection/GroupScheme.lean#L67). The attribute's comment: “a group scheme G → S with its neutral section e : S → G”.

> A group scheme `G ⟶ S` together with its neutral section `e : S ⟶ G`, as a morphism of
> schemes with a section. The neutral section is the morphism of schemes underlying the unit
> `η[G] : 𝟙_ (Over S) ⟶ G` of the group object `G`.

```lean
noncomputable def ofGrpObj : ConnectedAlongSection.{u}
```

**`AlgebraicGeometry.GroupScheme.neutralLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ConnectedComponentSection/GroupScheme.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ConnectedComponentSection/GroupScheme.lean#L98). The attribute's comment: “G⁰ = ⋃\_s G⁰\_s for the neutral section”. References: EGA IV (15.6.8), “special case”; EGA IV (9.7.12), “special case”; SGA 3 XIX (5.10).

> For a group scheme `G ⟶ S` with neutral section `e`, the subset `G⁰ ⊆ G`: the union over
> `s : S` of the connected components `G⁰_s` of the fibres `G_s` containing `e(s)`, that is, the
> locus `X⁰` for `f = (G ⟶ S)` and the section `e`.

```lean
noncomputable def neutralLocus : Set G.left
```

**`AlgebraicGeometry.GroupScheme.fiberι_preimage_neutralLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ConnectedComponentSection/GroupScheme.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ConnectedComponentSection/GroupScheme.lean#L104). The attribute's comment: “the trace of G⁰ on G\_s is the component of G\_s containing e(s)”.

> For a group scheme `G ⟶ S` with neutral section `e` and a point `s : S`, the trace of `G⁰` on
> the fibre `G_s` is the connected component of `G_s` containing the point `e(s)`.

```lean
theorem fiberι_preimage_neutralLocus (s : S) (z : G.hom.fiber s)
    (hz : G.hom.fiberι s z = η[G].left s) :
    (G.hom.fiberι s) ⁻¹' neutralLocus G = connectedComponent z
```

## Tag 055L, a situation

[Tag 055L](https://stacks.math.columbia.edu/tag/055L) in the Stacks Project.

**`AlgebraicGeometry.ConnectedAlongSection`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/Section.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/Section.lean#L55). The attribute's comment: “the sectioned morphism”.

> **Stacks Project, Tag 055L (standing data).** A morphism of schemes together with a
> specified section.

```lean
structure ConnectedAlongSection
```

**`AlgebraicGeometry.ConnectedAlongSection.fiberComponent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/Section.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/Section.lean#L79). The attribute's comment: “the component X⁰\_y”. References: EGA IV (15.6.5); EGA IV (15.6.8).

> **Stacks Project, Tag 055L (the fibrewise component).** The connected component of the
> fibre over `y` which contains the point supplied by the section.

```lean
noncomputable def fiberComponent (D : ConnectedAlongSection) (y : D.Y) : Set (D.f.fiber y)
```

**`AlgebraicGeometry.ConnectedAlongSection.locus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/Section.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/Section.lean#L85). The attribute's comment: “the union X⁰”. References: EGA IV (15.6.4).

> **Stacks Project, Tag 055L (the union).** The subset `X⁰ ⊆ X` obtained by taking, for
> every `y : Y`, the image in `X` of the connected component `X⁰_y`.

```lean
noncomputable def locus (D : ConnectedAlongSection) : Set D.X
```

## Tag 055M, a lemma

[Tag 055M](https://stacks.math.columbia.edu/tag/055M) in the Stacks Project.

**`AlgebraicGeometry.ConnectedAlongSection.locus_eq_preimage_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ConnectedComponentSection/BaseChange.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ConnectedComponentSection/BaseChange.lean#L287).

> **Stacks Project, Tag 055M.** In a cartesian square of sectioned morphisms, where the
> sections are compatible with the horizontal maps, the union of the connected components of
> the fibres containing the section pulls back to the corresponding union upstairs.

```lean
theorem locus_eq_preimage_of_isPullback
    (D D' : ConnectedAlongSection.{u})
    (g' : D'.X ⟶ D.X) (g : D'.Y ⟶ D.Y)
    (h : IsPullback g' D'.f D.f g)
    (hs : D'.s ≫ g' = g ≫ D.s) :
    D'.locus = g' ⁻¹' D.locus
```

## Tag 055N, a lemma

[Tag 055N](https://stacks.math.columbia.edu/tag/055N) in the Stacks Project.

**`AlgebraicGeometry.ConnectedAlongSection.clopenLocusAfterShrinking`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean#L90).

> **Stacks Project, Tag 055N.** For a finite type morphism with a section and a point `y` of
> the target, the locus `X⁰` is open and closed in the inverse image of a nonempty open subset of
> the closure of `y`.

```lean
theorem clopenLocusAfterShrinking : ClopenLocusAfterShrinking.{u}
```

## Tag 055P, a lemma

[Tag 055P](https://stacks.math.columbia.edu/tag/055P) in the Stacks Project.

**`AlgebraicGeometry.ConnectedAlongSection.isLocallyConstructible_locus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean#L96). References: EGA IV (9.7.12).

> **Stacks Project, Tag 055P.** For a morphism of finite presentation with a section, the
> locus `X⁰` is locally constructible in the source.

```lean
theorem isLocallyConstructible_locus : Statement055P.{u}
```

## Tag 055Q, a lemma

[Tag 055Q](https://stacks.math.columbia.edu/tag/055Q) in the Stacks Project.

**`AlgebraicGeometry.locus_mem_nhds_of_isDiscreteValuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/SectionLocusDVR.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/SectionLocusDVR.lean#L328). The attribute's comment: “the case of a discrete valuation ring base; the source's reduction to this case, and hence the statement for a general base, is not proved here”. References: EGA IV (15.6.5), “DVR base”.

> **Stacks 055Q over a discrete valuation ring base.** The locus `X⁰` is a neighbourhood of
> every point of the connected component of the closed fibre containing the section.

```lean
theorem locus_mem_nhds_of_isDiscreteValuationRing
    {X : Scheme.{u}} (f : X ⟶ Spec (.of R)) (sec : Spec (.of R) ⟶ X)
    (hsec : sec ≫ f = 𝟙 _) [Flat f] [LocallyOfFiniteType f]
    [IsReduced (f.fiber (IsLocalRing.closedPoint R))]
    {x : X} (hx : x ∈ connectedComponentIn (f ⁻¹' {IsLocalRing.closedPoint R} : Set X)
      (sec (IsLocalRing.closedPoint R))) :
    ConnectedAlongSection.locus ⟨X, Spec (.of R), f, sec, hsec⟩ ∈ nhds x
```

**`AlgebraicGeometry.ConnectedAlongSection.locus_mem_nhds_of_isConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/SectionLocusReduction.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/SectionLocusReduction.lean#L253). The attribute's comment: “the topological reduction to the discrete valuation ring case, for a Noetherian source”. References: EGA IV (15.6.5), “Noeth. source”.

> **Stacks 055Q for a Noetherian source.** If `X` is a Noetherian scheme, `f` is flat and
> locally of finite type and the fibre of `f` through `x ∈ X⁰` is geometrically reduced, then `X⁰`
> is a neighbourhood of `x`.
>
> Quantified over the points `x` of `X⁰` lying over a point `y` of `Y`, this is the conclusion of
> the source: `X⁰` is a neighbourhood of `X⁰_y`.

```lean
theorem locus_mem_nhds_of_isConstructible (D : ConnectedAlongSection.{u})
    [AlgebraicGeometry.IsNoetherian D.X] [Flat D.f] [LocallyOfFiniteType D.f]
    {x : D.X} (hx : x ∈ D.locus)
    (hred : GeometricallyReduced (D.f.fiberToSpecResidueField (D.f x))) :
    D.locus ∈ nhds x
```

**`AlgebraicGeometry.ConnectedAlongSection.locus_mem_nhdsSet_fiberComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean#L103). References: EGA IV (15.6.5), “nbhd of X⁰\_y”; EGA IV (15.6.4), “special case”.

> **Stacks Project, Tag 055Q.** For a flat morphism of finite presentation with a section
> whose fibre over `y` is geometrically reduced, the locus `X⁰` is a neighbourhood of the
> connected component of that fibre meeting the section.

```lean
theorem locus_mem_nhdsSet_fiberComponent (D : ConnectedAlongSection.{u})
    (hfp : FinitePresentation D.f) [Flat D.f] (y : D.Y)
    (hgr : GeometricallyReduced (D.f.fiberToSpecResidueField y)) :
    D.locus ∈ nhdsSet (D.f.fiberι y '' D.fiberComponent y)
```

## Tag 055R, a lemma

[Tag 055R](https://stacks.math.columbia.edu/tag/055R) in the Stacks Project.

**`AlgebraicGeometry.isOpen_locus_of_isDiscreteValuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/SectionLocusDVR.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/SectionLocusDVR.lean#L302). The attribute's comment: “the case of a discrete valuation ring base; the source's reduction to this case, and hence the statement for a general base, is not proved here”. References: EGA IV (15.6.5), “DVR base”.

> **Stacks 055R over a discrete valuation ring base.** The locus `X⁰` of connected components
> of fibres meeting the section is open. Only reducedness of the closed fibre is needed; the
> source's hypothesis that all fibres be geometrically reduced is not used, and the two reductions
> of the source that pass from a general base to this one are not proved here.

```lean
theorem isOpen_locus_of_isDiscreteValuationRing
    {X : Scheme.{u}} (f : X ⟶ Spec (.of R)) (sec : Spec (.of R) ⟶ X)
    (hsec : sec ≫ f = 𝟙 _) [Flat f] [LocallyOfFiniteType f]
    [IsReduced (f.fiber (IsLocalRing.closedPoint R))] :
    IsOpen (ConnectedAlongSection.locus ⟨X, Spec (.of R), f, sec, hsec⟩)
```

**`AlgebraicGeometry.ConnectedAlongSection.isOpen_locus_of_isConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/SectionLocusReduction.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/SectionLocusReduction.lean#L270). The attribute's comment: “the topological reduction to the discrete valuation ring case, for a Noetherian source”. References: EGA IV (15.6.5), “Noeth. source”.

> **Stacks 055R for a Noetherian source.** If `X` is a Noetherian scheme and `f` is flat and
> locally of finite type with geometrically reduced fibres, then `X⁰` is open.

```lean
theorem isOpen_locus_of_isConstructible (D : ConnectedAlongSection.{u})
    [AlgebraicGeometry.IsNoetherian D.X] [Flat D.f] [LocallyOfFiniteType D.f]
    [GeometricallyReduced D.f] :
    IsOpen D.locus
```

**`AlgebraicGeometry.ConnectedAlongSection.isOpen_locus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean#L112). References: EGA IV (15.6.5), “In particular: X⁰ open”.

> **Stacks Project, Tag 055R.** For a flat morphism of finite presentation with a section and
> geometrically reduced fibres, the locus `X⁰` is open in the source.

```lean
theorem isOpen_locus : Statement055R.{u}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.29, Tag 055K](https://stacks.math.columbia.edu/tag/055K)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
