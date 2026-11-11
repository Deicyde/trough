---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidScheme.exists_finite_openClosed_subgroupoid, AlgebraicGeometry.GroupoidScheme.exists_finite_openClosed_restriction
statement: formalized
proof: formalized
---

# 40.13 Étale localization of groupoids

Section 40.13 of the Stacks Project, [Tag 03FK](https://stacks.math.columbia.edu/tag/03FK). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03FL, a lemma

[Tag 03FL](https://stacks.math.columbia.edu/tag/03FL) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.exists_finite_openClosed_subgroupoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/EtaleLocalizationFiniteSubgroupoid/FiniteSubgroupoid.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/EtaleLocalizationFiniteSubgroupoid/FiniteSubgroupoid.lean#L308).

> Around a point at which the object map is quasi-finite and whose source fibre is finite, a
> flat finitely presented groupoid has, after an elementary étale base change, a finite
> open-and-closed subgroupoid containing precisely the orbit of the point in the distinguished
> fibre.

```lean
public theorem exists_finite_openClosed_subgroupoid
    {S : Scheme.{u}} (G : Stacks.Groupoids.GroupoidScheme S) (p : S)
    (u : G.objects.left) (hu : G.objects.hom u = p)
    [LocallyOfFiniteType G.objects.hom]
    (hqu : AlgebraicGeometry.quasiFiniteAt G.objects.hom u)
    [IsSeparated G.objects.hom] [IsSeparated G.arrows.hom]
    [Flat G.source.left] [LocallyOfFinitePresentation G.source.left]
    [Flat G.target.left] [LocallyOfFinitePresentation G.target.left]
    (hfinite : Set.Finite (G.source.left ⁻¹' {u})) :
    ∃ (N : AlgebraicGeometry.EtaleNeighborhood S p), N.IsElementary ∧
      ∃ (H : Stacks.Groupoids.GroupoidScheme N.scheme) (W W' : Scheme.{u})
        (jU : H.objects.left ⟶ pullback G.objects.hom N.toBase)
        (jW : W ⟶ pullback G.objects.hom N.toBase)
        (jR : H.arrows.left ⟶ pullback G.arrows.hom N.toBase)
        (jW' : W' ⟶ pullback G.arrows.hom N.toBase),
        IsOpenImmersion jU ∧ IsClosedImmersion jU ∧
        IsOpenImmersion jW ∧ IsClosedImmersion jW ∧
        IsIso (coprod.desc jU jW) ∧
        IsOpenImmersion jR ∧ IsClosedImmersion jR ∧
        IsOpenImmersion jW' ∧ IsClosedImmersion jW' ∧
        IsIso (coprod.desc jR jW') ∧
        H.objects.hom = jU ≫ pullback.snd G.objects.hom N.toBase ∧
        H.arrows.hom = jR ≫ pullback.snd G.arrows.hom N.toBase ∧
        (∃ u' : H.objects.left,
          (jU ≫ pullback.fst G.objects.hom N.toBase) u' = u ∧
          jU '' {x : H.objects.left | H.objects.hom x = N.point} =
            (pullback.map G.arrows.hom N.toBase G.objects.hom N.toBase
              G.target.left (𝟙 _) (𝟙 _) (by simp) (by simp)) ''
              ((pullback.map G.arrows.hom N.toBase G.objects.hom N.toBase
                G.source.left (𝟙 _) (𝟙 _) (by simp) (by simp)) ⁻¹' {jU u'}) ∧
          jR '' {r : H.arrows.left | H.arrows.hom r = N.point} =
            (pullback.map G.arrows.hom N.toBase G.objects.hom N.toBase
              G.source.left (𝟙 _) (𝟙 _) (by simp) (by simp)) ⁻¹'
                (jU '' {x : H.objects.left | H.objects.hom x = N.point})) ∧
        IsFinite H.objects.hom ∧ IsFinite H.arrows.hom ∧
        H.source.left ≫ jU ≫ pullback.fst G.objects.hom N.toBase =
          jR ≫ pullback.fst G.arrows.hom N.toBase ≫ G.source.left ∧
        H.target.left ≫ jU ≫ pullback.fst G.objects.hom N.toBase =
          jR ≫ pullback.fst G.arrows.hom N.toBase ≫ G.target.left ∧
        ∃ k : (pullback H.source H.target).left ⟶
            (pullback G.source G.target).left,
          k ≫ (pullback.fst G.source G.target).left =
              (pullback.fst H.source H.target).left ≫ jR ≫
                pullback.fst G.arrows.hom N.toBase ∧
          k ≫ (pullback.snd G.source G.target).left =
              (pullback.snd H.source H.target).left ≫ jR ≫
                pullback.fst G.arrows.hom N.toBase ∧
          H.comp.left ≫ jR ≫ pullback.fst G.arrows.hom N.toBase =
            k ≫ G.comp.left
```

## Tag 03X5, a lemma

[Tag 03X5](https://stacks.math.columbia.edu/tag/03X5) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.exists_finite_openClosed_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/EtaleLocalizationFiniteSubgroupoid/FiniteRestriction.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/EtaleLocalizationFiniteSubgroupoid/FiniteRestriction.lean#L416).

> The finite open-and-closed subgroupoid around a quasi-finite point can be chosen as the
> full restriction when the relation morphism is universally closed.

```lean
public theorem exists_finite_openClosed_restriction
    {S : Scheme.{u}} (G : Stacks.Groupoids.GroupoidScheme S) (p : S)
    (u : G.objects.left) (hu : G.objects.hom u = p)
    [LocallyOfFiniteType G.objects.hom]
    (hqu : AlgebraicGeometry.quasiFiniteAt G.objects.hom u)
    [IsSeparated G.objects.hom] [IsSeparated G.arrows.hom]
    [Flat G.source.left] [LocallyOfFinitePresentation G.source.left]
    [Flat G.target.left] [LocallyOfFinitePresentation G.target.left]
    (hfinite : Set.Finite (G.source.left ⁻¹' {u}))
    [UniversallyClosed (prod.lift G.target G.source).left] :
    ∃ (N : AlgebraicGeometry.EtaleNeighborhood S p), N.IsElementary ∧
      ∃ (H : Stacks.Groupoids.GroupoidScheme N.scheme) (W W' : Scheme.{u})
        (jU : H.objects.left ⟶ pullback G.objects.hom N.toBase)
        (jW : W ⟶ pullback G.objects.hom N.toBase)
        (jR : H.arrows.left ⟶ pullback G.arrows.hom N.toBase)
        (jW' : W' ⟶ pullback G.arrows.hom N.toBase),
        IsOpenImmersion jU ∧ IsClosedImmersion jU ∧
        IsOpenImmersion jW ∧ IsClosedImmersion jW ∧
        IsIso (coprod.desc jU jW) ∧
        IsOpenImmersion jR ∧ IsClosedImmersion jR ∧
        IsOpenImmersion jW' ∧ IsClosedImmersion jW' ∧
        IsIso (coprod.desc jR jW') ∧
        H.objects.hom = jU ≫ pullback.snd G.objects.hom N.toBase ∧
        H.arrows.hom = jR ≫ pullback.snd G.arrows.hom N.toBase ∧
        (∃ u' : H.objects.left,
          (jU ≫ pullback.fst G.objects.hom N.toBase) u' = u ∧
          jU '' {x : H.objects.left | H.objects.hom x = N.point} =
            (pullback.map G.arrows.hom N.toBase G.objects.hom N.toBase
              G.target.left (𝟙 _) (𝟙 _) (by simp) (by simp)) ''
              ((pullback.map G.arrows.hom N.toBase G.objects.hom N.toBase
                G.source.left (𝟙 _) (𝟙 _) (by simp) (by simp)) ⁻¹' {jU u'}) ∧
          jR '' {r : H.arrows.left | H.arrows.hom r = N.point} =
            (pullback.map G.arrows.hom N.toBase G.objects.hom N.toBase
              G.source.left (𝟙 _) (𝟙 _) (by simp) (by simp)) ⁻¹'
                (jU '' {x : H.objects.left | H.objects.hom x = N.point})) ∧
        IsFinite H.objects.hom ∧ IsFinite H.arrows.hom ∧
        H.source.left ≫ jU ≫ pullback.fst G.objects.hom N.toBase =
          jR ≫ pullback.fst G.arrows.hom N.toBase ≫ G.source.left ∧
        H.target.left ≫ jU ≫ pullback.fst G.objects.hom N.toBase =
          jR ≫ pullback.fst G.arrows.hom N.toBase ≫ G.target.left ∧
        (∃ k : (pullback H.source H.target).left ⟶
            (pullback G.source G.target).left,
          k ≫ (pullback.fst G.source G.target).left =
              (pullback.fst H.source H.target).left ≫ jR ≫
                pullback.fst G.arrows.hom N.toBase ∧
          k ≫ (pullback.snd G.source G.target).left =
              (pullback.snd H.source H.target).left ≫ jR ≫
                pullback.fst G.arrows.hom N.toBase ∧
          H.comp.left ≫ jR ≫ pullback.fst G.arrows.hom N.toBase =
            k ≫ G.comp.left) ∧
        (∀ (T : Scheme.{u})
          (f : T ⟶ pullback G.arrows.hom N.toBase)
          (x y : T ⟶ H.objects.left),
          (f ≫ pullback.map G.arrows.hom N.toBase G.objects.hom N.toBase
              G.source.left (𝟙 _) (𝟙 _) (by simp) (by simp) = x ≫ jU) →
          (f ≫ pullback.map G.arrows.hom N.toBase G.objects.hom N.toBase
              G.target.left (𝟙 _) (𝟙 _) (by simp) (by simp) = y ≫ jU) →
          (∃! g : T ⟶ H.arrows.left,
            g ≫ jR = f ∧ g ≫ H.source.left = x ∧ g ≫ H.target.left = y))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 40.13, Tag 03FK](https://stacks.math.columbia.edu/tag/03FK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
