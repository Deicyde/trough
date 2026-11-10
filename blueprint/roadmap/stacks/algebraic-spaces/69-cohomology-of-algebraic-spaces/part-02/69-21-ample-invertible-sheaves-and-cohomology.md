---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.tfae_isAmple_of_isProper_toAffine, AlgebraicGeometry.Space.exists_isAmple_iff_exists_isAmple_modulePullback
statement: formalized
proof: formalized
---

# 69.21 Ample invertible sheaves and cohomology

Section 69.21 of the Stacks Project, [Tag 0GF9](https://stacks.math.columbia.edu/tag/0GF9). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GFA, a lemma

[Tag 0GFA](https://stacks.math.columbia.edu/tag/0GFA) in the Stacks Project.

**`AlgebraicGeometry.Space.tfae_isAmple_of_isProper_toAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AmpleTwistVanishing.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AmpleTwistVanishing.lean#L302).

> **Stacks 0GFA.**  Let `X` be an algebraic space proper over a Noetherian ring `R` — here an
> affine object `V` of the site with `Γ(V, 𝒪_V) = R` Noetherian and a proper `f : X ⟶ h_V` — and let
> `𝓛` be an invertible `𝒪_X`-module.  The following are equivalent:
>
> 1. `X` is a scheme and `𝓛` is ample on it: there are an object `U` of the site and an
>    isomorphism `e : h_U ≅ X` for which the restriction of `𝓛` to `U` is an invertible and ample
>    module;
> 2. for every coherent `𝒪_X`-module `𝓕` there is an `n₀ ≥ 0` with `H ᵖ(X, 𝓕 ⊗ 𝓛^{⊗ n}) = 0` for
>    all `n ≥ n₀` and `p > 0`;
> 3. for every coherent `𝒪_X`-module `𝓕` there is an `n ≥ 1` with `H¹(X, 𝓕 ⊗ 𝓛^{⊗ n}) = 0`.
>
> (1) ⟹ (2) is `AlgebraicGeometry.Space.exists_isZero_rightDerived_twistStep_of_isAmple` (Serre's
> vanishing theorem on the scheme, Stacks 0B5T), (2) ⟹ (3) is immediate, and (3) ⟹ (1) is Stacks
> 0D2W (`exists_isAmple_of_forall_isCoherent_isZero_rightDerived_one_twistStep`), `X` being
> Noetherian as it is proper over a Noetherian affine scheme.

```lean
theorem tfae_isAmple_of_isProper_toAffine
    (V : BigFppfOver B S hS) [IsAffine ((BigFppfOver.toScheme B S hS).obj V)]
    [IsNoetherianRing Γ((BigFppfOver.toScheme B S hS).obj V, ⊤)]
    {X : AlgebraicSpaces B S hS} (f : X ⟶ schemeSpace V) (hf : IsProper B S hS f.hom)
    (L : Modules.{u, u} B S hS X.1 X.2)
    [hL : Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O).property L] :
    have := enoughInjectives_modules B S hS X.1 X.2
    List.TFAE [
      ∃ (U : BigFppfOver B S hS) (eX : yoneda.obj U ≅ X.1)
        (_ : Stacks.Ample.IsInvertibleModule ((BigFppfOver.toScheme B S hS).obj U)
          (baseChangeModule B S hS L U eX.hom)),
        Stacks.Ample.IsAmple ((BigFppfOver.toScheme B S hS).obj U)
          (baseChangeModule B S hS L U eX.hom),
      ∀ F : Modules.{u, u} B S hS X.1 X.2, IsCoherent B S hS X.1 X.2 F →
        ∃ n₀ : ℕ, ∀ n : ℕ, n₀ ≤ n → ∀ p : ℕ, 0 < p →
          IsZero (((globalSectionsFunctor.{u + 1, u, u, u} (Stacks.SheafOfModules.Tensor.ringSheaf
              (smallEtaleRingedSite B S hS X.1 X.2).O)).rightDerived p).obj
              (twistStep B S hS X.1 X.2 L n F)),
      ∀ F : Modules.{u, u} B S hS X.1 X.2, IsCoherent B S hS X.1 X.2 F →
        ∃ n : ℕ, 1 ≤ n ∧ IsZero (((globalSectionsFunctor.{u + 1, u, u, u}
            (Stacks.SheafOfModules.Tensor.ringSheaf
              (smallEtaleRingedSite B S hS X.1 X.2).O)).rightDerived 1).obj
            (twistStep B S hS X.1 X.2 L n F))]
```

## Tag 0GFB, a lemma

[Tag 0GFB](https://stacks.math.columbia.edu/tag/0GFB) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isAmple_iff_exists_isAmple_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AmpleFiniteSurjective.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AmpleFiniteSurjective.lean#L241).

> **Stacks 0GFB.**  Let `R` be a Noetherian ring, `X` an algebraic space proper over `R` — a
> proper `pX : X ⟶ h_V` with `V` affine and `Γ(V, 𝒪_V) = R` — and `f : Y ⟶ X` a finite surjective
> morphism of algebraic spaces.  Let `𝓛` be an invertible `𝒪_X`-module.  Then `X` is a scheme and `𝓛`
> is ample on it if and only if `Y` is a scheme and `f^*𝓛` is ample on it.
>
> A scheme is an object `U` of the site with an isomorphism `h_U ≅ X`, and `𝓛` is ample on it when
> its restriction to `U` (`AlgebraicGeometry.Space.baseChangeModule`) is invertible and ample.  The
> source also assumes `Y` proper over `R`; that follows, a finite morphism being proper.

```lean
theorem exists_isAmple_iff_exists_isAmple_modulePullback
    (V : BigFppfOver B S hS) [IsAffine ((BigFppfOver.toScheme B S hS).obj V)]
    [IsNoetherianRing Γ((BigFppfOver.toScheme B S hS).obj V, ⊤)]
    {X Y : AlgebraicSpaces B S hS} (pX : X ⟶ schemeSpace V) (hpX : IsProper B S hS pX.hom)
    (f : Y ⟶ X) (hf : IsFinite B S hS f.hom) (hfs : IsSurjective B S hS f.hom)
    (L : Modules.{u, u} B S hS X.1 X.2)
    [hL : Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O).property L] :
    (∃ (U : BigFppfOver B S hS) (eX : yoneda.obj U ≅ X.1)
      (_ : Stacks.Ample.IsInvertibleModule ((BigFppfOver.toScheme B S hS).obj U)
        (baseChangeModule B S hS L U eX.hom)),
      Stacks.Ample.IsAmple ((BigFppfOver.toScheme B S hS).obj U)
        (baseChangeModule B S hS L U eX.hom)) ↔
    ∃ (U' : BigFppfOver B S hS) (eY : yoneda.obj U' ≅ Y.1)
      (_ : Stacks.Ample.IsInvertibleModule ((BigFppfOver.toScheme B S hS).obj U')
        (baseChangeModule B S hS ((modulePullback B S hS f).obj L) U' eY.hom)),
      Stacks.Ample.IsAmple ((BigFppfOver.toScheme B S hS).obj U')
        (baseChangeModule B S hS ((modulePullback B S hS f).obj L) U' eY.hom)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.21, Tag 0GF9](https://stacks.math.columbia.edu/tag/0GF9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
