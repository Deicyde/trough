---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isFiniteType_of_pullback_fpqc, AlgebraicGeometry.Space.isFinitePresentation_of_pullback_fpqc, AlgebraicGeometry.Space.isFlat_of_pullback_fpqc, AlgebraicGeometry.Space.isFiniteLocallyFreeOnSite_of_pullback_isFpqcCovering_of_isQuasicoherentOnSite, AlgebraicGeometry.Space.isLocallyProjective_of_pullback_fpqc, AlgebraicGeometry.Space.isFiniteType_iff_smallBaseChangePushforward_of_isQuasicoherentOnSite, AlgebraicGeometry.Space.isFinitePresentation_iff_smallBaseChangePushforward_of_isQuasicoherentOnSite
statement: formalized
proof: formalized
---

# 74.6 Descent of finiteness properties of modules

Section 74.6 of the Stacks Project, [Tag 060T](https://stacks.math.columbia.edu/tag/060T). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 060U, a lemma

[Tag 060U](https://stacks.math.columbia.edu/tag/060U) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteType_of_pullback_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/ModuleFiniteness.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/ModuleFiniteness.lean#L344). The attribute's comment: “finite type read on the restriction to every etale scheme chart; at the module universe of the structure rings”.

> **Stacks 060U.** A quasi-coherent module on an algebraic space whose inverse image along
> every member of an fpqc covering is of finite type is itself of finite type, finite type being
> read on the restriction to every étale scheme chart.

```lean
theorem isFiniteType_of_pullback_fpqc
    {I : Type v} {X : AlgebraicSpaces B S hS} (Xᵢ : I → AlgebraicSpaces B S hS)
    (f : ∀ i, Xᵢ i ⟶ X) (F : Modules.{u, u} B S hS X.obj X.property)
    (hF : F.IsQuasicoherentOnSite)
    (hf : IsFpqcCovering B S hS fun i ↦ (f i).hom)
    (hft : ∀ (i : I) (W : SmallEtale B S hS (Xᵢ i).obj),
      (restrictToChart B S hS (Xᵢ i).property
        ((modulePullback B S hS (f i)).obj F) W).IsFiniteType) :
    ∀ V : SmallEtale B S hS X.obj,
      (restrictToChart B S hS X.property F V).IsFiniteType
```

## Tag 060V, a lemma

[Tag 060V](https://stacks.math.columbia.edu/tag/060V) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinitePresentation_of_pullback_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/ModuleFinitePresentation.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/ModuleFinitePresentation.lean#L42).

> Let `F` be a quasi-coherent `𝒪_X`-module on an algebraic space `X` and let
> `{f_i : X_i → X}` be an fpqc covering such that each `f_i^* F` is an `𝒪_{X_i}`-module of finite
> presentation. Then `F` is an `𝒪_X`-module of finite presentation.

```lean
theorem isFinitePresentation_of_pullback_fpqc {I : Type v} {X : AlgebraicSpaces B S hS}
    (Xᵢ : I → AlgebraicSpaces B S hS) (f : ∀ i, Xᵢ i ⟶ X)
    (F : Modules.{u, u} B S hS X.obj X.property) (hF : F.IsQuasicoherentOnSite)
    (hf : IsFpqcCovering B S hS fun i ↦ (f i).hom)
    (hfp : ∀ i, ((modulePullback B S hS (f i)).obj F).IsFinitePresentation) :
    F.IsFinitePresentation
```

## Tag 060W, a lemma

[Tag 060W](https://stacks.math.columbia.edu/tag/060W) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_of_pullback_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/ModuleFiniteness.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/ModuleFiniteness.lean#L371). The attribute's comment: “flatness read on the restriction to every etale scheme chart; at the module universe of the structure rings”.

> **Stacks 060W.** A quasi-coherent module on an algebraic space whose inverse image along
> every member of an fpqc covering is flat is itself flat, flatness being read on the restriction
> to every étale scheme chart.

```lean
theorem isFlat_of_pullback_fpqc
    {I : Type v} {X : AlgebraicSpaces B S hS} (Xᵢ : I → AlgebraicSpaces B S hS)
    (f : ∀ i, Xᵢ i ⟶ X) (F : Modules.{u, u} B S hS X.obj X.property)
    (hF : F.IsQuasicoherentOnSite)
    (hf : IsFpqcCovering B S hS fun i ↦ (f i).hom)
    (hflat : ∀ (i : I) (W : SmallEtale B S hS (Xᵢ i).obj),
      SheafOfModules.IsFlat.{u, u, u, u} (O := (etaleChartScheme B S hS W).toRingedSpace.sheaf)
        (restrictToChart B S hS (Xᵢ i).property
          ((modulePullback B S hS (f i)).obj F) W)) :
    ∀ V : SmallEtale B S hS X.obj,
      SheafOfModules.IsFlat.{u, u, u, u} (O := (etaleChartScheme B S hS V).toRingedSpace.sheaf)
        (restrictToChart B S hS X.property F V)
```

## Tag 060X, a lemma

[Tag 060X](https://stacks.math.columbia.edu/tag/060X) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteLocallyFreeOnSite_of_pullback_isFpqcCovering_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeFpqcDescentQuasicoherent.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeFpqcDescentQuasicoherent.lean#L47).

> Let `X` be an algebraic space over `S`, let `𝓕` be a quasi-coherent `𝒪_X`-module and let
> `{f i : X i ⟶ X}` be an fpqc covering of `X` such that every pullback `(f i)^*𝓕` is finite locally
> free. Then `𝓕` is finite locally free.

```lean
theorem isFiniteLocallyFreeOnSite_of_pullback_isFpqcCovering_of_isQuasicoherentOnSite
    {I : Type v} {X : AlgebraicSpaces B S hS} {Xi : I → AlgebraicSpaces B S hS}
    (f : ∀ i, Xi i ⟶ X) (hf : IsFpqcCovering B S hS fun i ↦ (f i).hom)
    (F : Modules.{u, u} B S hS X.obj X.property) (hF : F.IsQuasicoherentOnSite)
    (hFlf : ∀ i, SheafOfModules.IsFiniteLocallyFreeOnSite
      ((modulePullback B S hS (f i)).obj F)) :
    SheafOfModules.IsFiniteLocallyFreeOnSite F
```

## Tag 060Y, a lemma

[Tag 060Y](https://stacks.math.columbia.edu/tag/060Y) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyProjective_of_pullback_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/ModuleFiniteness.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/ModuleFiniteness.lean#L399). The attribute's comment: “local projectivity in the chartwise sense of Tag 060R; at the module universe of the structure rings”.

> **Stacks 060Y.** A quasi-coherent module on an algebraic space whose inverse image along
> every member of an fpqc covering is locally projective is itself locally projective, in the
> chartwise sense of Stacks 060R.

```lean
theorem isLocallyProjective_of_pullback_fpqc
    {I : Type v} {X : AlgebraicSpaces B S hS} (Xᵢ : I → AlgebraicSpaces B S hS)
    (f : ∀ i, Xᵢ i ⟶ X) (F : QuasicoherentSheaves.{u, u} B S hS X.obj X.property)
    (hf : IsFpqcCovering B S hS fun i ↦ (f i).hom)
    (hproj : ∀ i, IsLocallyProjective B S hS (Xᵢ i).property
      ⟨(modulePullback B S hS (f i)).obj F.obj,
        isQuasicoherentOnSite_modulePullback_of_isQuasicoherentOnSite B S hS (f i)
          F.obj F.property⟩) :
    IsLocallyProjective B S hS X.property F
```

## Tag 060Z, a lemma

[Tag 060Z](https://stacks.math.columbia.edu/tag/060Z) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteType_iff_smallBaseChangePushforward_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePushforwardFiniteType.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePushforwardFiniteType.lean#L302).

> For a finite morphism `f : X ⟶ Y` of algebraic spaces a quasi-coherent `𝒪_X`-module `F` is
> of finite type if and only if its direct image `f_*F` is.

```lean
theorem isFiniteType_iff_smallBaseChangePushforward_of_isQuasicoherentOnSite
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsFinite B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hqc : F.IsQuasicoherentOnSite) :
    F.IsFiniteType ↔
      ((smallBaseChangeModulePushforward B S hS f
        (relativelyRepresentable_hom_of_isFinite B S hS f hf)).obj F).IsFiniteType
```

## Tag 0610, a lemma

[Tag 0610](https://stacks.math.columbia.edu/tag/0610) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinitePresentation_iff_smallBaseChangePushforward_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartSchemeFinitePresentationDescent.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChartSchemeFinitePresentationDescent.lean#L166).

> For a finite morphism `f : X ⟶ Y` of finite presentation of algebraic spaces a quasi-coherent
> `𝒪_X`-module `F` is of finite presentation if and only if its direct image `f_*F` is.

```lean
theorem isFinitePresentation_iff_smallBaseChangePushforward_of_isQuasicoherentOnSite
    (f : X ⟶ Y) (hf : IsFinite B S hS f.hom) (hfp : IsFinitePresentation B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hqc : F.IsQuasicoherentOnSite) :
    F.IsFinitePresentation ↔
      ((smallBaseChangeModulePushforward B S hS f
        (relativelyRepresentable_hom_of_isFinite B S hS f hf)).obj F).IsFinitePresentation
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.6, Tag 060T](https://stacks.math.columbia.edu/tag/060T)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
