---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsZariskiCovering, AlgebraicGeometry.Space.isZariskiCovering_yoneda_of_openCover, AlgebraicGeometry.Space.isZariskiCovering_of_isIso, AlgebraicGeometry.Space.isZariskiCovering_comp, AlgebraicGeometry.Space.isZariskiCovering_pullback
statement: formalized
proof: formalized
---

# 73.3 Zariski topology

Section 73.3 of the Stacks Project, [Tag 03YD](https://stacks.math.columbia.edu/tag/03YD). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 041G, a definition

[Tag 041G](https://stacks.math.columbia.edu/tag/041G) in the Stacks Project.

**`AlgebraicGeometry.Space.IsZariskiCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/Zariski.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/Zariski.lean#L81).

> **Stacks 041G.** A family of open immersions whose images cover every point of the
> target.

```lean
abbrev IsZariskiCovering (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (I : Type v) (Xᵢ : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (f : ∀ i, Xᵢ i ⟶ X) : Prop
```

**`AlgebraicGeometry.Space.isZariskiCovering_yoneda_of_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiCoveringOfOpenCover.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiCoveringOfOpenCover.lean#L103). The attribute's comment: “an open cover of an object of the site”.

> **Stacks 041G for an open cover of an object of the big fppf site of `S`.** A family of
> morphisms of the site whose underlying morphisms of schemes are open immersions covering the
> underlying scheme of the target induces a Zariski covering of the presheaf represented by the
> target.

```lean
theorem isZariskiCovering_yoneda_of_openCover
    {I : Type v} {T : BigFppfOver B S hS} (X : I → BigFppfOver B S hS) (g : ∀ i, X i ⟶ T)
    (hopen : ∀ i, _root_.AlgebraicGeometry.IsOpenImmersion
      ((BigFppfOver.toScheme B S hS).map (g i)))
    (hcov : ∀ x : (BigFppfOver.toScheme B S hS).obj T,
      ∃ i, x ∈ Set.range ((BigFppfOver.toScheme B S hS).map (g i))) :
    IsZariskiCovering B S hS I (fun i => yoneda.obj (X i)) (fun i => yoneda.map (g i))
```

## Tag 041H, a lemma

[Tag 041H](https://stacks.math.columbia.edu/tag/041H) in the Stacks Project.

**`AlgebraicGeometry.Space.isZariskiCovering_of_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/Zariski.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/Zariski.lean#L92). The attribute's comment: “isomorphism_cover”.

> **Stacks 041H.** An isomorphism gives a singleton Zariski covering.

```lean
theorem isZariskiCovering_of_isIso
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X X' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (f : X' ⟶ X) [IsIso f] :
    IsZariskiCovering B S hS PUnit (fun _ => X') (fun _ => f)
```

**`AlgebraicGeometry.Space.isZariskiCovering_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/Zariski.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/Zariski.lean#L107). The attribute's comment: “composition_cover”.

> **Stacks 041H.** Composing a Zariski covering with a covering of each member gives a
> Zariski covering.

```lean
theorem isZariskiCovering_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (I : Type v) (J : I → Type w)
    (Xᵢ : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (Xᵢⱼ : ∀ i, J i → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (f : ∀ i, Xᵢ i ⟶ X)
    (g : ∀ i j, Xᵢⱼ i j ⟶ Xᵢ i)
    (hf : IsZariskiCovering B S hS I Xᵢ f)
    (hg : ∀ i, IsZariskiCovering B S hS (J i) (Xᵢⱼ i) (g i)) :
    IsZariskiCovering B S hS (Σ i, J i)
      (fun p => Xᵢⱼ p.1 p.2) (fun p => g p.1 p.2 ≫ f p.1)
```

**`AlgebraicGeometry.Space.isZariskiCovering_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/Zariski.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/Zariski.lean#L137). The attribute's comment: “base_change_cover”.

> **Stacks 041H.** Zariski coverings are stable under base change: the first projections of
> the fibre products of a Zariski covering `{Xᵢ ⟶ X}` with a morphism `g : X' ⟶ X` form a
> Zariski covering of `X'`.

```lean
theorem isZariskiCovering_pullback
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X X' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (I : Type v) (Xᵢ : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (f : ∀ i, Xᵢ i ⟶ X) (g : X' ⟶ X)
    (h : IsZariskiCovering B S hS I Xᵢ f) :
    IsZariskiCovering B S hS I (fun i => Limits.pullback g (f i))
      (fun i => Limits.pullback.fst g (f i))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 73.3, Tag 03YD](https://stacks.math.columbia.edu/tag/03YD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
