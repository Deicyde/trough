---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_forall_topologicalKrullDim_fiber_le_of_isLimit_of_essentiallySmall, AlgebraicGeometry.exists_quasiFinite_baseChange_of_quasiFinite_limitBaseChange, AlgebraicGeometry.exists_relativeDimensionLE_baseChange_of_limitBaseChange, AlgebraicGeometry.exists_relativeDimension_baseChange_of_relativeDimension_limitBaseChange, AlgebraicGeometry.exists_finitePresentation_closedImmersion_of_forall_topologicalKrullDim_fiber_le
statement: formalized
proof: formalized
---

# 32.18 Limits and dimensions of fibres

Section 32.18 of the Stacks Project, [Tag 05M4](https://stacks.math.columbia.edu/tag/05M4). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05M5, a lemma

[Tag 05M5](https://stacks.math.columbia.edu/tag/05M5) in the Stacks Project.

**`AlgebraicGeometry.exists_forall_topologicalKrullDim_fiber_le_of_isLimit_of_essentiallySmall`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/FibreDimensionBound.lean, line 824](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/FibreDimensionBound.lean#L824).

> **Stacks Project, Tag 05M5**, for an index category that is essentially small relative to
> the universe of the schemes: a uniform bound on the dimensions of the fibres of a morphism
> between inverse limits already holds at some stage.

```lean
public lemma exists_forall_topologicalKrullDim_fiber_le_of_isLimit_of_essentiallySmall
    {I : Type v} [Category.{w} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (X S : I ⥤ Scheme.{u}) (f : X ⟶ S)
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (S.map g)]
    [∀ i : I, CompactSpace (S.obj i)] [∀ i : I, QuasiSeparatedSpace (S.obj i)]
    [∀ i : I, LocallyOfFiniteType (f.app i)] [∀ i : I, QuasiCompact (f.app i)]
    [∀ {i j : I} (g : i ⟶ j),
      IsClosedImmersion (pullback.lift (X.map g) (f.app i) (f.naturality g))]
    (cX : Cone X) (hcX : IsLimit cX) (cS : Cone S) (hcS : IsLimit cS) (d : ℕ)
    (hdim : ∀ s : cS.pt,
      topologicalKrullDim
        ((hcS.lift ((Cone.postcompose f).obj cX)).fiber s) ≤ (d : WithBot ℕ∞)) :
    ∃ i : I, ∀ s : S.obj i,
      topologicalKrullDim ((f.app i).fiber s) ≤ (d : WithBot ℕ∞)
```

## Tag 094M, a lemma

[Tag 094M](https://stacks.math.columbia.edu/tag/094M) in the Stacks Project.

**`AlgebraicGeometry.exists_quasiFinite_baseChange_of_quasiFinite_limitBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/QuasiFinite.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/QuasiFinite.lean#L91).

> Let `c` be a limit cone of a cofiltered diagram `D` of schemes with affine transition
> morphisms, and let `f₀ : X₀ ⟶ Y₀` be a morphism locally of finite type of quasi-compact and
> quasi-separated schemes over the quasi-compact and quasi-separated stage `D.obj i₀`. If the base
> change of `f₀` to the limit is quasi-finite, then the base change of `f₀` to some later stage is
> quasi-finite.

```lean
theorem exists_quasiFinite_baseChange_of_quasiFinite_limitBaseChange
    {I : Type u} [Category.{u} I] [IsCofiltered I] (D : I ⥤ Scheme.{u})
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    (c : Cone D) (hc : IsLimit c) (i₀ : I)
    (X₀ Y₀ : Over (D.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [CompactSpace (D.obj i₀)] [QuasiSeparatedSpace (D.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFiniteType f₀.left]
    [LocallyOfFiniteType ((Over.pullback (c.π.app i₀)).map f₀).left]
    [QuasiCompact ((Over.pullback (c.π.app i₀)).map f₀).left]
    [LocallyQuasiFinite ((Over.pullback (c.π.app i₀)).map f₀).left] :
    ∃ (i : I) (g : i ⟶ i₀),
      (LocallyOfFiniteType ((Over.pullback (D.map g)).map f₀).left ∧
          QuasiCompact ((Over.pullback (D.map g)).map f₀).left) ∧
        LocallyQuasiFinite ((Over.pullback (D.map g)).map f₀).left
```

## Tag 0H3V, a lemma

[Tag 0H3V](https://stacks.math.columbia.edu/tag/0H3V) in the Stacks Project.

**`AlgebraicGeometry.exists_relativeDimensionLE_baseChange_of_limitBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/RelativeDimension.lean, line 431](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/RelativeDimension.lean#L431).

> In the situation of Tag 081D, if the base change of `f₀` to the limit has relative
> dimension at most `d` and `f₀` is locally of finite type, then the base change of `f₀` to some
> later stage has relative dimension at most `d`.

```lean
theorem exists_relativeDimensionLE_baseChange_of_limitBaseChange
    (D : DescentSituation.{u, u} I)
    (X₀ Y₀ : Over (D.system.obj (op D.base))) (f₀ : X₀ ⟶ Y₀)
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFiniteType f₀.left] (d : ℕ)
    (h : RelativeDimensionLE (baseChangeMap (D.limitCone.π.app (op D.base)) X₀ Y₀ f₀) d) :
    ∃ (i : I) (hi : D.base ≤ i),
      RelativeDimensionLE (baseChangeMap (D.system.map (homOfLE hi).op) X₀ Y₀ f₀) d
```

## Tag 0EY2, a lemma

[Tag 0EY2](https://stacks.math.columbia.edu/tag/0EY2) in the Stacks Project.

**`AlgebraicGeometry.exists_relativeDimension_baseChange_of_relativeDimension_limitBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/RelativeDimension.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/RelativeDimension.lean#L348).

> In the situation of Tag 081D, if the base change of `f₀` to the limit has relative
> dimension `d` and `f₀` is locally of finite presentation, then the base change of `f₀` to some
> later stage has relative dimension `d`.

```lean
theorem exists_relativeDimension_baseChange_of_relativeDimension_limitBaseChange
    (D : DescentSituation.{u, u} I)
    (X₀ Y₀ : Over (D.system.obj (op D.base))) (f₀ : X₀ ⟶ Y₀)
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFinitePresentation f₀.left] (d : ℕ)
    (h : RelativeDimension (baseChangeMap (D.limitCone.π.app (op D.base)) X₀ Y₀ f₀) d) :
    ∃ (i : I) (hi : D.base ≤ i),
      RelativeDimension (baseChangeMap (D.system.map (homOfLE hi).op) X₀ Y₀ f₀) d
```

## Tag 05M6, a lemma

[Tag 05M6](https://stacks.math.columbia.edu/tag/05M6) in the Stacks Project.

**`AlgebraicGeometry.exists_finitePresentation_closedImmersion_of_forall_topologicalKrullDim_fiber_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/FibreDimensionEnlargement.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/FibreDimensionEnlargement.lean#L79).

> **Stacks Project, Tag 05M6.** Let `S` be a quasi-compact and quasi-separated scheme, let
> `f : X ⟶ S` be a morphism of finite presentation and let `d` be a natural number.  A closed
> subscheme `Z ⊆ X`, given by the closed immersion `i`, all of whose fibres over `S` have
> dimension at most `d`, is contained in a closed subscheme `Z' ⊆ X`, given by the closed
> immersion `j`, such that `j` is of finite presentation and all fibres of `Z'` over `S` still
> have dimension at most `d`.

```lean
theorem exists_finitePresentation_closedImmersion_of_forall_topologicalKrullDim_fiber_le
    {S X Z : Scheme.{u}} [CompactSpace S] [QuasiSeparatedSpace S]
    (f : X ⟶ S) (hf : FinitePresentation f) (i : Z ⟶ X) [IsClosedImmersion i] (d : ℕ)
    (hdim : ∀ s : S, topologicalKrullDim ((i ≫ f).fiber s) ≤ (d : WithBot ℕ∞)) :
    ∃ (Z' : Scheme.{u}) (j : Z' ⟶ X) (h : Z ⟶ Z'),
      IsClosedImmersion j ∧ IsClosedImmersion h ∧ i = h ≫ j ∧ FinitePresentation j ∧
        ∀ s : S, topologicalKrullDim ((j ≫ f).fiber s) ≤ (d : WithBot ℕ∞)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.18, Tag 05M4](https://stacks.math.columbia.edu/tag/05M4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
