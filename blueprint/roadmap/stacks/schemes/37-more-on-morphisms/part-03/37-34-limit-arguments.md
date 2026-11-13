---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_finiteTypeAffineModel, AlgebraicGeometry.exists_finiteTypeAffineModel_isCoherent, AlgebraicGeometry.exists_finiteTypeAffineModel_isCoherent_isFlatOver, AlgebraicGeometry.exists_flat_finiteTypeAffineModel, AlgebraicGeometry.exists_smooth_finiteTypeAffineModel, AlgebraicGeometry.exists_finiteTypeAffineModel_geometricallyReduced, AlgebraicGeometry.exists_finiteTypeAffineModel_geometricallyIrreducible, AlgebraicGeometry.exists_finiteTypeAffineModel_geometricallyConnected
statement: formalized
proof: formalized
---

# 37.34 Limit arguments

Section 37.34 of the Stacks Project, [Tag 05FA](https://stacks.math.columbia.edu/tag/05FA). 11 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05FB, a lemma

[Tag 05FB](https://stacks.math.columbia.edu/tag/05FB) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteTypeAffineModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximation.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximation.lean#L99).

> **Stacks Project, Tag 05FB.** An affine morphism of finite presentation between affine
> schemes admits an affine finite-type model over a base of finite type over `ℤ`.

```lean
theorem exists_finiteTypeAffineModel {X S : Scheme.{u}} [IsAffine X] [IsAffine S]
    (f : X ⟶ S) (hf : FinitePresentation f) :
    Nonempty (FiniteTypeAffineModel ⊤ f)
```

## Tag 05FC, a lemma

[Tag 05FC](https://stacks.math.columbia.edu/tag/05FC) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteTypeAffineModel_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximationModule.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximationModule.lean#L228).

> **Stacks Project, Tag 05FC.** A quasi-coherent module of finite presentation on the source of
> a morphism of affine schemes of finite presentation descends to a coherent module on an affine
> finite-type model of that morphism over a base of finite type over `ℤ`.

```lean
theorem exists_finiteTypeAffineModel_isCoherent
    {X S : Scheme.{u}} [IsAffine X] [IsAffine S]
    (f : X ⟶ S) (hf : FinitePresentation f)
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFinitePresentation] :
    ∃ (m : FiniteTypeAffineModel ⊤ f) (F₀ : m.X₀.Modules),
      F₀.IsCoherent ∧ Nonempty ((Scheme.Modules.pullback m.toSource).obj F₀ ≅ F)
```

## Tag 05FD, a lemma

[Tag 05FD](https://stacks.math.columbia.edu/tag/05FD) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteTypeAffineModel_isCoherent_isFlatOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximationModule.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximationModule.lean#L266).

> **Stacks Project, Tag 05FD.** A quasi-coherent module of finite presentation on the source of
> a morphism of affine schemes of finite presentation which is moreover flat over the target
> descends to a coherent module, flat over the base, on an affine finite-type model of that
> morphism over a base of finite type over `ℤ`.

```lean
theorem exists_finiteTypeAffineModel_isCoherent_isFlatOver
    {X S : Scheme.{u}} [IsAffine X] [IsAffine S]
    (f : X ⟶ S) (hf : FinitePresentation f)
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFinitePresentation]
    (hF : IsFlatOver f.toLRSHom.toShHom F) :
    ∃ (m : FiniteTypeAffineModel ⊤ f) (F₀ : m.X₀.Modules),
      F₀.IsCoherent ∧ Nonempty ((Scheme.Modules.pullback m.toSource).obj F₀ ≅ F) ∧
        IsFlatOver m.f₀.toLRSHom.toShHom F₀
```

## Tag 05FE, a lemma

[Tag 05FE](https://stacks.math.columbia.edu/tag/05FE) in the Stacks Project.

**`AlgebraicGeometry.exists_flat_finiteTypeAffineModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximation.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximation.lean#L159).

> **Stacks Project, Tag 05FE.** A flat morphism of finite presentation between affine
> schemes admits an affine finite-type model whose modeled morphism is flat.

```lean
theorem exists_flat_finiteTypeAffineModel
    {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S)
    (hf : FinitePresentation f) [Flat f] :
    Nonempty (FiniteTypeAffineModel @Flat f)
```

## Tag 05FF, a lemma

[Tag 05FF](https://stacks.math.columbia.edu/tag/05FF) in the Stacks Project.

**`AlgebraicGeometry.exists_smooth_finiteTypeAffineModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximation.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximation.lean#L221).

> **Stacks Project, Tag 05FF.** A smooth morphism between affine schemes
> admits an affine finite-type model whose modeled morphism is smooth.

```lean
theorem exists_smooth_finiteTypeAffineModel
    {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S) [Smooth f] :
    Nonempty (FiniteTypeAffineModel @Smooth f)
```

## Tag 05FG, a lemma

[Tag 05FG](https://stacks.math.columbia.edu/tag/05FG) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteTypeAffineModel_geometricallyReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximationFibre.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximationFibre.lean#L182). References: EGA IV (8.9.1), “(i), special case”.

> **Stacks Project, Tag 05FG.** A morphism of affine schemes of finite presentation with
> geometrically reduced fibres admits an affine finite-type model over a base of finite type over
> `ℤ` whose fibres are geometrically reduced as well.
>
> The limit argument is `AlgebraicGeometry.exists_finiteTypeAffineModel_fiberwise`, applied to the
> locus of geometrically reduced fibres. Its compatibility with base change is Tag 0576,
> `AlgebraicGeometry.geometricallyReduced_fiber_set_eq_preimage_of_isPullback`, and its local
> constructibility over an affine Noetherian base is Tag 0579,
> `AlgebraicGeometry.isLocallyConstructible_geometricallyReduced_fiber_of_isAffine`.

```lean
theorem exists_finiteTypeAffineModel_geometricallyReduced
    {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S)
    (hf : FinitePresentation f) (hfib : GeometricallyReduced f) :
    Nonempty (FiniteTypeAffineModel @GeometricallyReduced f)
```

## Tag 05FH, a lemma

[Tag 05FH](https://stacks.math.columbia.edu/tag/05FH) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteTypeAffineModel_geometricallyIrreducible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximationFibre.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximationFibre.lean#L127).

> **Stacks Project, Tag 05FH.** A morphism of affine schemes of finite presentation with
> geometrically irreducible fibres admits an affine finite-type model over a base of finite type
> over `ℤ` whose fibres are geometrically irreducible as well.

```lean
theorem exists_finiteTypeAffineModel_geometricallyIrreducible
    {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S)
    (hf : FinitePresentation f) (hfib : GeometricallyIrreducible f) :
    Nonempty (FiniteTypeAffineModel @GeometricallyIrreducible f)
```

## Tag 05FI, a lemma

[Tag 05FI](https://stacks.math.columbia.edu/tag/05FI) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteTypeAffineModel_geometricallyConnected`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximationFibre.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximationFibre.lean#L163).

> **Stacks Project, Tag 05FI.** A morphism of affine schemes of finite presentation with
> geometrically connected fibres admits an affine finite-type model over a base of finite type
> over `ℤ` whose fibres are geometrically connected as well.

```lean
theorem exists_finiteTypeAffineModel_geometricallyConnected
    {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S)
    (hf : FinitePresentation f) (hfib : GeometricallyConnected f) :
    Nonempty (FiniteTypeAffineModel @GeometricallyConnected f)
```

## Tag 05FJ, a lemma

[Tag 05FJ](https://stacks.math.columbia.edu/tag/05FJ) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteTypeAffineModel_fiberDimension_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Approximation.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Approximation.lean#L327).

> **Stacks Project, Tag 05FJ.** An affine morphism of finite presentation all of whose fibres
> have dimension `d` admits an affine finite-type model all of whose fibres have dimension `d`.

```lean
public theorem exists_finiteTypeAffineModel_fiberDimension_eq {X S : Scheme.{u}} [IsAffine X]
    [IsAffine S] (f : X ⟶ S) (hf : FinitePresentation f) (d : ℕ)
    (hd : ∀ s : S, f.fiberDimension s = (d : WithBot ℕ∞)) :
    ∃ m : FiniteTypeAffineModel ⊤ f,
      ∀ s₀ : m.S₀, m.f₀.fiberDimension s₀ = (d : WithBot ℕ∞)
```

## Tag 05FK, a lemma

[Tag 05FK](https://stacks.math.columbia.edu/tag/05FK) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteTypeAffineModel_standardSyntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximation.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineApproximation.lean#L370).

> **Stacks Project, Tag 05FK.** A standard syntomic morphism of affine schemes
> admits an affine finite-type model whose modeled morphism is standard syntomic.

```lean
theorem exists_finiteTypeAffineModel_standardSyntomic
    {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S)
    (hf : IsStandardSyntomic f) :
    Nonempty {m : FiniteTypeAffineModel ⊤ f //
      letI : IsAffine m.X₀ := m.source_affine
      letI : IsAffine m.S₀ := m.base_affine
      IsStandardSyntomic m.f₀}
```

## Tag 05FL, a lemma

[Tag 05FL](https://stacks.math.columbia.edu/tag/05FL) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteTypeAffineModel_inf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineModel.lean, line 443](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/AffineModel.lean#L443).

> Two finite-type affine models of an affine morphism of finite presentation, for properties
> stable under base change, can be combined into one model on which both properties hold.

```lean
theorem exists_finiteTypeAffineModel_inf
    (P Q : MorphismProperty Scheme.{u}) [P.IsStableUnderBaseChange]
    [Q.IsStableUnderBaseChange] {X S : Scheme.{u}} [IsAffine X] [IsAffine S]
    (f : X ⟶ S) [LocallyOfFinitePresentation f] [QuasiCompact f]
    (hP : FiniteTypeAffineModel P f) (hQ : FiniteTypeAffineModel Q f) :
    Nonempty (FiniteTypeAffineModel (P ⊓ Q) f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.34, Tag 05FA](https://stacks.math.columbia.edu/tag/05FA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
