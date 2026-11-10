---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isRelativelyAmple_iff_forall_isCoherent_exists_isZero_rightDerived, AlgebraicGeometry.Space.exists_ampleSchemeFibreTwistConclusion_tensorPow, AlgebraicGeometry.Space.exists_mem_isRelativelyAmple_openSub_of_isAmple_baseChangeModule, AlgebraicGeometry.Space.exists_mem_isRelativelyAmple_openSub_of_forall_isRelativelyAmple_residueField
statement: formalized
proof: formalized
---

# 71.15 Relative ampleness and cohomology

Section 71.15 of the Stacks Project, [Tag 0D37](https://stacks.math.columbia.edu/tag/0D37). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D38, a lemma

[Tag 0D38](https://stacks.math.columbia.edu/tag/0D38) in the Stacks Project.

**`AlgebraicGeometry.Space.isRelativelyAmple_iff_forall_isCoherent_exists_isZero_rightDerived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleTwistVanishing.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeAmpleTwistVanishing.lean#L62).

> **Stacks 0D38.**  Let `R` be a Noetherian ring — here an affine object `V` of the site with
> `Γ(V, 𝒪_V) = R` Noetherian — let `X` be an algebraic space over `R` whose structure morphism
> `f : X ⟶ h_V` is proper, and let `𝓛` be an invertible `𝒪_X`-module.  Then `𝓛` is ample on `X/R`
> (Stacks 0D31) if and only if for every coherent `𝒪_X`-module `𝓕` there is an `n₀ ≥ 0` with
> `H ᵖ(X, 𝓕 ⊗ 𝓛^{⊗ n}) = 0` for all `n ≥ n₀` and all `p > 0`.

```lean
theorem isRelativelyAmple_iff_forall_isCoherent_exists_isZero_rightDerived
    (V : BigFppfOver B S hS) [IsAffine ((BigFppfOver.toScheme B S hS).obj V)]
    [IsNoetherianRing Γ((BigFppfOver.toScheme B S hS).obj V, ⊤)]
    {X : AlgebraicSpaces B S hS} (f : X ⟶ schemeSpace V) (hf : IsProper B S hS f.hom)
    (L : Modules.{u, u} B S hS X.1 X.2)
    [hL : Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O).property L] :
    have := enoughInjectives_modules B S hS X.1 X.2
    IsRelativelyAmple B S hS f L ↔
      ∀ F : Modules.{u, u} B S hS X.1 X.2, IsCoherent B S hS X.1 X.2 F →
        ∃ n₀ : ℕ, ∀ n : ℕ, n₀ ≤ n → ∀ p : ℕ, 0 < p →
          IsZero (((globalSectionsFunctor.{u + 1, u, u, u}
            (Stacks.SheafOfModules.Tensor.ringSheaf
              (smallEtaleRingedSite B S hS X.1 X.2).O)).rightDerived p).obj
              (twistStep B S hS X.1 X.2 L n F))
```

## Tag 0D39, a lemma

[Tag 0D39](https://stacks.math.columbia.edu/tag/0D39) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_ampleSchemeFibreTwistConclusion_tensorPow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AmpleSchemeFibreTwistAndNeighbourhood.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AmpleSchemeFibreTwistAndNeighbourhood.lean#L61).

> **Stacks 0D39.**  Let `Y` be a Noetherian scheme of the site, `f : X ⟶ h_Y` a proper morphism
> from an algebraic space, `ℒ` an invertible and `ℱ` a coherent `𝒪_X`-module, and `y ∈ Y` a point
> such that the fibre `X_y` is a scheme (the cartesian square `hsq` of `f` along `Spec κ(y) ⟶ Y`)
> on which the restriction of `ℒ` is ample.  Then there is a `d₀` such that for every `d ≥ d₀`,
> `R^p f_*(ℱ ⊗ ℒ^{⊗ d})_y = 0` for `p > 0` and every section of `ℱ ⊗ ℒ^{⊗ d}` over `X_y` comes
> from `f_*(ℱ ⊗ ℒ^{⊗ d})_y` (`AlgebraicGeometry.Space.AmpleSchemeFibreTwistConclusion`).

```lean
theorem exists_ampleSchemeFibreTwistConclusion_tensorPow (Y : BigFppfOver B S hS)
    [_root_.AlgebraicGeometry.IsNoetherian ((BigFppfOver.toScheme B S hS).obj Y)]
    {X : AlgebraicSpaces B S hS} (f : X ⟶ representedAlgebraicSpace B S hS Y)
    (hf : IsProper B S hS f.hom) (L : Modules.{u, u} B S hS X.1 X.2)
    [Stacks.SheafOfModules.IsInvertible (structureSheaf B S hS X.1 X.2).obj
      (structureRingPresheaf_isSheaf B S hS X.1 X.2) L]
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : IsCoherent B S hS X.1 X.2 F)
    (y : (BigFppfOver.toScheme B S hS).obj Y) (U : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X.1)
    (q : U ⟶ residuePointObject Y y)
    (hsq : IsPullback p (yoneda.map q) f.hom (yoneda.map (residuePointHom Y y)))
    (hL : ∃ hL : Stacks.Ample.IsInvertibleModule ((BigFppfOver.toScheme B S hS).obj U)
      (baseChangeModule B S hS L U p), @Stacks.Ample.IsAmple _ _ hL) :
    ∃ d₀ : ℕ, ∀ d : ℕ, d₀ ≤ d →
      AmpleSchemeFibreTwistConclusion f y U p (F ⊗ tensorPow B S hS L d)
```

## Tag 0D3A, a lemma

[Tag 0D3A](https://stacks.math.columbia.edu/tag/0D3A) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_mem_isRelativelyAmple_openSub_of_isAmple_baseChangeModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AmpleSchemeFibreTwistAndNeighbourhood.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AmpleSchemeFibreTwistAndNeighbourhood.lean#L85).

> **Stacks 0D3A.**  Let `Y` be a Noetherian scheme of the site, `f : X ⟶ h_Y` a proper morphism
> from an algebraic space, `ℒ` an invertible `𝒪_X`-module, and `y ∈ Y` a point such that the fibre
> `X_y` is a scheme (the cartesian square `hsq` of `f` along `Spec κ(y) ⟶ Y`) on which the
> restriction of `ℒ` is ample.  Then there is an open neighbourhood `V` of `y` such that the
> pullback of `ℒ` to `f⁻¹(V)` is ample on `f⁻¹(V)/V` (Stacks 0D31), for every base change of `f`
> along `V ⟶ Y`.

```lean
theorem exists_mem_isRelativelyAmple_openSub_of_isAmple_baseChangeModule
    {Y : BigFppfOver B S hS}
    [_root_.AlgebraicGeometry.IsNoetherian ((BigFppfOver.toScheme B S hS).obj Y)]
    {X : AlgebraicSpaces B S hS} (f : X ⟶ representedAlgebraicSpace B S hS Y)
    (hf : IsProper B S hS f.hom) (L : Modules.{u, u} B S hS X.1 X.2)
    [Stacks.SheafOfModules.IsInvertible (structureSheaf B S hS X.1 X.2).obj
      (structureRingPresheaf_isSheaf B S hS X.1 X.2) L]
    (y : (BigFppfOver.toScheme B S hS).obj Y) (U : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X.1)
    (q : U ⟶ residuePointObject Y y)
    (hsq : IsPullback p (yoneda.map q) f.hom (yoneda.map (residuePointHom Y y)))
    (hamp : ∃ hL : Stacks.Ample.IsInvertibleModule ((BigFppfOver.toScheme B S hS).obj U)
      (baseChangeModule B S hS L U p), @Stacks.Ample.IsAmple _ _ hL) :
    ∃ V : ((BigFppfOver.toScheme B S hS).obj Y).Opens, y ∈ V ∧
      ∀ ⦃X₁ : AlgebraicSpaces B S hS⦄ (p₁ : X₁ ⟶ X)
        (f₁ : X₁ ⟶ representedAlgebraicSpace B S hS (openSub Y V)),
        IsPullback p₁ f₁ f (ObjectProperty.homMk (yoneda.map (openSubHom Y V))) →
        IsRelativelyAmple B S hS f₁ ((modulePullback B S hS p₁).obj L)
```

**`AlgebraicGeometry.Space.exists_mem_isRelativelyAmple_openSub_of_forall_isRelativelyAmple_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AmpleSchemeFibreTwistAndNeighbourhood.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AmpleSchemeFibreTwistAndNeighbourhood.lean#L113).

> **Stacks 0D3A, the fibre read through Stacks 0D31.**  Let `Y` be a Noetherian scheme of the
> site, `f : X ⟶ h_Y` a proper morphism from an algebraic space, `ℒ` an invertible `𝒪_X`-module, and
> `y ∈ Y` a point such that the pullback of `ℒ` is ample on every base change of `f` along
> `Spec κ(y) ⟶ Y` (so `X_y` is a scheme on which `ℒ_y` is ample).  Then there is an open
> neighbourhood `V` of `y` such that the pullback of `ℒ` is ample on every base change of `f` along
> `V ⟶ Y`.

```lean
theorem exists_mem_isRelativelyAmple_openSub_of_forall_isRelativelyAmple_residueField
    {Y : BigFppfOver B S hS}
    [_root_.AlgebraicGeometry.IsNoetherian ((BigFppfOver.toScheme B S hS).obj Y)]
    {X : AlgebraicSpaces B S hS} (f : X ⟶ representedAlgebraicSpace B S hS Y)
    (hf : IsProper B S hS f.hom) (L : Modules.{u, u} B S hS X.1 X.2)
    (hL : Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS X.1)
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O)).property
        L)
    (y : (BigFppfOver.toScheme B S hS).obj Y)
    (hy : ∀ ⦃X₀ : AlgebraicSpaces B S hS⦄ (p₀ : X₀ ⟶ X)
      (f₀ : X₀ ⟶ representedAlgebraicSpace B S hS
        (residueFieldObject B S hS Y y (B.residueField_spec_contains Y.left.property y))),
      IsPullback p₀ f₀ f (ObjectProperty.homMk (yoneda.map
        (residueFieldMap B S hS Y y (B.residueField_spec_contains Y.left.property y)))) →
      IsRelativelyAmple B S hS f₀ ((modulePullback B S hS p₀).obj L)) :
    ∃ V : ((BigFppfOver.toScheme B S hS).obj Y).Opens, y ∈ V ∧
      ∀ ⦃X₁ : AlgebraicSpaces B S hS⦄ (p₁ : X₁ ⟶ X)
        (f₁ : X₁ ⟶ representedAlgebraicSpace B S hS (openSub Y V)),
        IsPullback p₁ f₁ f (ObjectProperty.homMk (yoneda.map (openSubHom Y V))) →
        IsRelativelyAmple B S hS f₁ ((modulePullback B S hS p₁).obj L)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.15, Tag 0D37](https://stacks.math.columbia.edu/tag/0D37)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
