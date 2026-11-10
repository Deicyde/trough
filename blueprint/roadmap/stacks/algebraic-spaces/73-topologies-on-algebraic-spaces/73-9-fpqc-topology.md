---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsFpqcCovering, AlgebraicGeometry.Space.isFpqcCovering_of_isFppfCovering, AlgebraicGeometry.Space.isFpqcCovering_of_isSyntomicCovering, AlgebraicGeometry.Space.isFpqcCovering_of_isSmoothCovering, AlgebraicGeometry.Space.isFpqcCovering_of_isEtaleCovering, AlgebraicGeometry.Space.isFpqcCovering_of_isZariskiCovering, AlgebraicGeometry.Space.Topology.precoverage_etale_le_fpqc, AlgebraicGeometry.Space.isFpqcCovering_pullback
statement: formalized
proof: formalized
---

# 73.9 Fpqc topology

Section 73.9 of the Stacks Project, [Tag 03MP](https://stacks.math.columbia.edu/tag/03MP). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03MQ, a definition

[Tag 03MQ](https://stacks.math.columbia.edu/tag/03MQ) in the Stacks Project.

**`AlgebraicGeometry.Space.IsFpqcCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean#L177).

> **Stacks 03MQ.** A family of flat morphisms of algebraic spaces over `S` with common
> target `Y` is an *fpqc covering* when, for every affine object `T` of the big fppf site of
> `S` and every morphism `h : T ⟶ Y`, there is a finite family of affine objects over `T`
> which is an fpqc covering of `T` and refines the family pulled back along `h`.

```lean
abbrev IsFpqcCovering {I : Type v} {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : ∀ i, X i ⟶ Y) : Prop
```

## Tag 0DFQ, a lemma

[Tag 0DFQ](https://stacks.math.columbia.edu/tag/0DFQ) in the Stacks Project.

**`AlgebraicGeometry.Space.isFpqcCovering_of_isFppfCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparison.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparison.lean#L246). The attribute's comment: “fppf coverings”.

> **Stacks 0DFQ**, the fppf case: an fppf covering of algebraic spaces over `S` is an fpqc
> covering.

```lean
theorem isFpqcCovering_of_isFppfCovering
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (f : ∀ i, X i ⟶ F)
    (hf : IsFppfCovering B S hS X f) :
    IsFpqcCovering B S hS f
```

**`AlgebraicGeometry.Space.isFpqcCovering_of_isSyntomicCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean#L207). The attribute's comment: “syntomic coverings”.

> **Stacks 0DFQ**, the syntomic case: a syntomic covering of algebraic spaces over `S` is an
> fpqc covering.

```lean
theorem isFpqcCovering_of_isSyntomicCovering
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, X i ⟶ F)
    (hf : IsSyntomicCovering B S hS X f) :
    IsFpqcCovering B S hS f
```

**`AlgebraicGeometry.Space.isFpqcCovering_of_isSmoothCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean#L218). The attribute's comment: “smooth coverings”.

> **Stacks 0DFQ**, the smooth case: a smooth covering of algebraic spaces over `S` is an fpqc
> covering.

```lean
theorem isFpqcCovering_of_isSmoothCovering
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, X i ⟶ F)
    (hf : IsSmoothCovering B S hS X f) :
    IsFpqcCovering B S hS f
```

**`AlgebraicGeometry.Space.isFpqcCovering_of_isEtaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean#L229). The attribute's comment: “étale coverings”.

> **Stacks 0DFQ**, the étale case: an étale covering of algebraic spaces over `S` is an fpqc
> covering.

```lean
theorem isFpqcCovering_of_isEtaleCovering
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, X i ⟶ F)
    (hf : IsEtaleCovering B S hS X f) :
    IsFpqcCovering B S hS f
```

**`AlgebraicGeometry.Space.isFpqcCovering_of_isZariskiCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean#L278). The attribute's comment: “Zariski coverings”.

> **Stacks 0DFQ**, the Zariski case: a Zariski covering of algebraic spaces over `S` is an
> fpqc covering.

```lean
theorem isFpqcCovering_of_isZariskiCovering
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, X i ⟶ F)
    (hF : IsAlgebraicSpace B S hS F) (hX : ∀ i, IsAlgebraicSpace B S hS (X i))
    (hf : IsZariskiCovering B S hS I X f) :
    IsFpqcCovering B S hS f
```

**`AlgebraicGeometry.Space.Topology.precoverage_etale_le_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoproductChartPropertyDescent.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/CoproductChartPropertyDescent.lean#L111). The attribute's comment: “étale coverings, at the precoverages”.

> The étale precoverage of algebraic spaces over `S` is contained in the fpqc one.

```lean
theorem precoverage_etale_le_fpqc :
    Topology.precoverage.{u, v} .etale B S hS ≤ Topology.precoverage.{u, v} .fpqc B S hS
```

## Tag 03MR, a lemma

[Tag 03MR](https://stacks.math.columbia.edu/tag/03MR) in the Stacks Project.

**`AlgebraicGeometry.Space.isFpqcCovering_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FpqcCoveringBaseChange.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FpqcCoveringBaseChange.lean#L42). The attribute's comment: “part (3): base change”.

> Pulling an fpqc covering family of algebraic spaces over `S`
> back along a morphism `f : X ⟶ Y` of algebraic spaces gives an fpqc covering of `X`: the second
> projections of the fibre products of Stacks 02X2 form an fpqc covering.

```lean
theorem isFpqcCovering_pullback
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {I : Type v} {Y X : AlgebraicSpaces B S hS} {Yi : I → AlgebraicSpaces B S hS}
    (g : ∀ i, Yi i ⟶ Y) (f : X ⟶ Y)
    (hg : IsFpqcCovering B S hS (fun i => (g i).hom)) :
    IsFpqcCovering B S hS (fun i => pullback.snd (g i).hom f.hom)
```

**`AlgebraicGeometry.Space.isFpqcCovering_of_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FpqcCoveringBaseChange.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FpqcCoveringBaseChange.lean#L59). The attribute's comment: “isomorphism”.

> An isomorphism of presheaves on the big fppf site of `S`, regarded as a family indexed by a
> point, is an fpqc covering.

```lean
theorem isFpqcCovering_of_isIso
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ G) [IsIso f] :
    IsFpqcCovering B S hS (fun _ : PUnit.{v + 1} => f)
```

**`AlgebraicGeometry.Space.isFpqcCovering_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FpqcCoveringComposition.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FpqcCoveringComposition.lean#L53). The attribute's comment: “composition”.

> **Stacks 03MR**, the composition clause. Composing an fpqc covering of an algebraic space
> over `S` with fpqc coverings of each of its members gives an fpqc covering.

```lean
theorem isFpqcCovering_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {I : Type v} {J : I → Type w}
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {Xi : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {Xij : (Σ i, J i) → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hXi : ∀ i, IsAlgebraicSpace B S hS (Xi i))
    (hXij : ∀ (i : I) (j : J i), IsAlgebraicSpace B S hS (Xij ⟨i, j⟩))
    (f : ∀ i, Xi i ⟶ X)
    (g : ∀ (i : I) (j : J i), Xij ⟨i, j⟩ ⟶ Xi i)
    (hf : IsFpqcCovering B S hS f)
    (hg : ∀ i, IsFpqcCovering B S hS (g i)) :
    IsFpqcCovering B S hS (fun ij : Σ i, J i => g ij.1 ij.2 ≫ f ij.1)
```

## Tag 03MS, a lemma

[Tag 03MS](https://stacks.math.columbia.edu/tag/03MS) in the Stacks Project.

**`AlgebraicGeometry.Space.isFpqcCovering_iff_pullback_atlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FpqcCoveringAtlas.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FpqcCoveringAtlas.lean#L78).

> A family of morphisms of algebraic spaces over `S` with target `X` is an
> fpqc covering exactly when its pullback along a surjective étale morphism `a : U ⟶ X` from a
> scheme in the site is an fpqc covering of `U`.

```lean
theorem isFpqcCovering_iff_pullback_atlas
    {I : Type v} {X : AlgebraicSpaces B S hS} {Xi : I → AlgebraicSpaces B S hS}
    (f : ∀ i, Xi i ⟶ X)
    (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X.obj)
    (ha_surj : IsSurjective B S hS a) (ha_etale : IsEtale B S hS a) :
    IsFpqcCovering B S hS (fun i ↦ (f i).hom) ↔
      IsFpqcCovering B S hS (fun i ↦ pullback.fst a (f i).hom)
```

## Tag 0419, a lemma

[Tag 0419](https://stacks.math.columbia.edu/tag/0419) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_fpqc_scheme_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FpqcCoverings.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FpqcCoverings.lean#L55).

> **Stacks 0419.** Every fpqc covering of an algebraic space over `S` by algebraic spaces
> has an fpqc refinement by schemes, with each new member factoring through the corresponding
> member of the original covering by a relatively étale morphism.

```lean
theorem exists_fpqc_scheme_refinement
    {I : Type v} {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {Xᵢ : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hXᵢ : ∀ i, IsAlgebraicSpace B S hS (Xᵢ i))
    (f : ∀ i, Xᵢ i ⟶ X) (hf : IsFpqcCovering B S hS f) :
    ∃ (T : I → BigFppfOver B S hS) (e : ∀ i, yoneda.obj (T i) ⟶ Xᵢ i),
      (∀ i, (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf (e i)) ∧
        IsFpqcCovering B S hS (fun i => e i ≫ f i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 73.9, Tag 03MP](https://stacks.math.columbia.edu/tag/03MP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
