---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_isLimit_isProper_isFinitePresentation_of_isProper, AlgebraicGeometry.Space.exists_isLimit_isProper_isFinitePresentation_arrow_of_isProper, AlgebraicGeometry.Space.MorphismDescentData.exists_isProper_schemeTheoreticSupport_moduleAt
statement: formalized
proof: formalized
---

# 70.12 Approximating proper morphisms

Section 70.12 of the Stacks Project, [Tag 0A0V](https://stacks.math.columbia.edu/tag/0A0V). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A0W, a lemma

[Tag 0A0W](https://stacks.math.columbia.edu/tag/0A0W) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isLimit_isProper_isFinitePresentation_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperLimitOfFinitePresentationEmbedding.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperLimitOfFinitePresentationEmbedding.lean#L213).

> Let `f : X ⟶ Y` be a proper morphism of algebraic spaces over `S`, with `Y` quasi-compact and
> quasi-separated. Then `X` is the directed limit, along closed immersions and over `Y`, of algebraic
> spaces proper and of finite presentation over `Y`, the projections from `X` being closed
> immersions.

```lean
theorem exists_isLimit_isProper_isFinitePresentation_of_isProper
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsProper B S hS f)
    (hYqc : IsQuasiCompactSpace B S hS Y)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y) :
    ∃ (I : Type u) (_ : Preorder I) (_ : IsDirected I (· ≤ ·)) (_ : Nonempty I)
      (D : Iᵒᵖ ⥤ (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (t : D ⟶ (Functor.const Iᵒᵖ).obj Y)
      (π : (Functor.const Iᵒᵖ).obj X ⟶ D),
      (∀ i, IsAlgebraicSpace B S hS (D.obj i)) ∧
      (∀ i, IsProper B S hS (t.app i) ∧ IsFinitePresentation B S hS (t.app i)) ∧
      (∀ ⦃i j : Iᵒᵖ⦄ (e : i ⟶ j), IsClosedImmersion B S hS (D.map e)) ∧
      (∀ i, IsClosedImmersion B S hS (π.app i)) ∧
      π ≫ t = (Functor.const Iᵒᵖ).map f ∧
      Nonempty (IsLimit (Cone.mk X π))
```

## Tag 0A0X, a lemma

[Tag 0A0X](https://stacks.math.columbia.edu/tag/0A0X) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isLimit_isProper_isFinitePresentation_arrow_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperLimitOfFinitePresentationEmbedding.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperLimitOfFinitePresentationEmbedding.lean#L263).

> Let `f : X ⟶ Y` be a proper morphism of algebraic spaces over `Spec ℤ`, with `Y`
> quasi-compact and quasi-separated. Then `f` is the limit of a directed system of proper morphisms
> of finite presentation `X_i ⟶ Y_i` between algebraic spaces of finite presentation over `Spec ℤ`,
> the systems `X_i` and `Y_i` having affine transition morphisms.

```lean
theorem exists_isLimit_isProper_isFinitePresentation_arrow_of_isProper
    (hZ : B.Contains (⊤_ Scheme.{u}))
    {X Y : ((BigFppfOver B (⊤_ Scheme.{u}) hZ)ᵒᵖ ⥤ Type u)} (hX : IsAlgebraicSpace B _ hZ X) (hY :
      IsAlgebraicSpace B _ hZ Y)
    (f : X ⟶ Y) (hf : IsProper B _ hZ f) (hYqc : IsQuasiCompactSpace B _ hZ Y)
    (hYqs : IsAbsolutelyQuasiSeparated B _ hZ hZ Y) :
    ∃ (I : Type u) (_ : Preorder I) (_ : IsDirected I (· ≤ ·))
      (DX DY : DescentSituation B (⊤_ Scheme.{u}) hZ hZ I) (φ : DX.system ⟶ DY.system)
      (eX : DX.limitCone.pt ≅ X) (eY : DY.limitCone.pt ≅ Y),
      (∀ i : I, DX.limitCone.π.app (op i) ≫ φ.app (op i) =
        eX.hom ≫ f ≫ eY.inv ≫ DY.limitCone.π.app (op i)) ∧
      (∀ i : I, IsProper B _ hZ (φ.app (op i)) ∧ IsFinitePresentation B _ hZ (φ.app (op i))) ∧
      (∀ i : I, IsFinitePresentation B _ hZ (terminal.from (DY.system.obj (op i))))
```

## Tag 08K2, a lemma

[Tag 08K2](https://stacks.math.columbia.edu/tag/08K2) in the Stacks Project.

**`AlgebraicGeometry.Space.MorphismDescentData.exists_isProper_schemeTheoreticSupport_moduleAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/MorphismDescentData.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/MorphismDescentData.lean#L251).

> In Situation 084W, under the chapter's convention of Section 70.2, let `F₀`
> be a quasi-coherent `𝒪_{X₀}`-module of finite type and let `F` and `F_i` be its pullbacks to `X`
> and `X_i`. If `f₀` is locally of finite type and the scheme-theoretic support of `F` is proper
> over `Y`, then the scheme-theoretic support of `F_i` is proper over `Y_i` for some `i ≥ 0`.

```lean
theorem exists_isProper_schemeTheoreticSupport_moduleAt
    (hconv : SiteContainsBaseChangeLimits B S hS D.base)
    (F₀ : Modules.{u, u} B S hS (D.toMorphismDescentSituation hconv).source₀Space.1
      (D.toMorphismDescentSituation hconv).source₀Space.2)
    (hqc : F₀.IsQuasicoherentOnSite)
    (hf₀ : IsLocallyOfFiniteType B S hS D.map₀)
    (hft : SheafOfModules.IsFiniteTypeOnSite F₀)
    (hproper : IsProper B S hS
      ((schemeTheoreticSupport B S hS (D.toMorphismDescentSituation hconv).sourceLimitSpace
        ((D.toMorphismDescentSituation hconv).moduleLimit F₀)).ι ≫
          (D.toMorphismDescentSituation hconv).mapLimit)) :
    ∃ (i : I) (hi : D.initial ≤ i), IsProper B S hS
      ((schemeTheoreticSupport B S hS ((D.toMorphismDescentSituation hconv).sourceAtSpace i hi)
        ((D.toMorphismDescentSituation hconv).moduleAt F₀ i hi)).ι ≫
          (D.toMorphismDescentSituation hconv).mapAt i hi)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.12, Tag 0A0V](https://stacks.math.columbia.edu/tag/0A0V)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
