---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isEffectiveCartierDivisor_hasPropertySk, AlgebraicGeometry.Space.isNormal_effectiveCartierDivisor_hasPropertySk_one, AlgebraicGeometry.Space.exists_isEffectiveCartierDivisor_compl_denseAffineOpen', AlgebraicGeometry.Space.exists_isEffectiveCartierDivisor_iso_differenceDivisorSheaf, AlgebraicGeometry.Space.exists_isEffectiveCartierDivisor_genericFibre_eq
statement: formalized
proof: formalized
---

# 71.8 Effective Cartier divisors on Noetherian spaces

Section 71.8 of the Stacks Project, [Tag 0CPH](https://stacks.math.columbia.edu/tag/0CPH). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B4G, a lemma

[Tag 0B4G](https://stacks.math.columbia.edu/tag/0B4G) in the Stacks Project.

**`AlgebraicGeometry.Space.isEffectiveCartierDivisor_hasPropertySk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisorSerreCondition.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisorSerreCondition.lean#L228).

> **Stacks 0B4G.** Let `X` be a locally Noetherian algebraic space over a scheme `S`
> satisfying Serre's condition `(S_k)`, and let `D ⊆ X` be an effective Cartier divisor.  Then
> `D` satisfies `(S_{k-1})`.
>
> Both hypothesis and conclusion are Stacks 03E6 taken at the property of schemes "locally
> Noetherian and `(S_k)`", which is item (3) of Remark 03E7.  By Stacks 083C the divisor is cut
> out on a surjective étale chart `U` of `X` by an effective Cartier ideal sheaf; `U` inherits
> `(S_k)` from `X` by Stacks 03E8, and the closed subscheme it cuts out satisfies `(S_{k-1})` by
> the scheme case `AlgebraicGeometry.isEffectiveCartierDivisor_hasPropertySk` (Stacks 0B3R).
> That closed subscheme is a surjective étale chart of `D`.
>
> The index `k - 1` is truncated subtraction of natural numbers; at `k = 0` the conclusion is
> the vacuous condition `(S_0)` and is supplied by
> `AlgebraicGeometry.hasPropertySk_zero`, so no hypothesis `1 ≤ k` is required.

```lean
theorem isEffectiveCartierDivisor_hasPropertySk
    (X : AlgebraicSpaces B S hS) (D : ClosedSubspaces B S hS X.1)
    (hD : IsEffectiveCartierDivisor B S hS X D) (k : ℕ)
    (hX : HasEtaleLocalProperty B S hS X.1
      (fun T : Scheme.{u} => ∃ h : IsLocallyNoetherian T, @HasPropertySk T h k)) :
    HasEtaleLocalProperty B S hS D.1.toFunctor
      (fun T : Scheme.{u} => ∃ h : IsLocallyNoetherian T, @HasPropertySk T h (k - 1))
```

## Tag 0B4H, a lemma

[Tag 0B4H](https://stacks.math.columbia.edu/tag/0B4H) in the Stacks Project.

**`AlgebraicGeometry.Space.isNormal_effectiveCartierDivisor_hasPropertySk_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisorSerreCondition.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisorSerreCondition.lean#L260).

> **Stacks 0B4H.** Let `X` be a locally Noetherian normal algebraic space over a scheme `S`
> and let `D ⊆ X` be an effective Cartier divisor.  Then `D` satisfies Serre's condition
> `(S_1)`.
>
> Normality and local Noetherianity of `X` are each Stacks 03E6 taken at the corresponding
> property of schemes, items (7) and (1) of Remark 03E7.  By Stacks 083C the divisor is cut out
> on a surjective étale chart `U` of `X` by an effective Cartier ideal sheaf; `U` is locally
> Noetherian and normal by Stacks 03E8, and the closed subscheme it cuts out satisfies `(S_1)`
> by the scheme case `AlgebraicGeometry.isNormal_effectiveCartierDivisor_hasPropertySk_one`
> (Stacks 0B3S), which is where Serre's criterion is used.  That closed subscheme is a
> surjective étale chart of `D`.

```lean
theorem isNormal_effectiveCartierDivisor_hasPropertySk_one
    (X : AlgebraicSpaces B S hS)
    (hXnoeth : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hXnormal : IsNormal B S hS X.1) (D : ClosedSubspaces B S hS X.1)
    (hD : IsEffectiveCartierDivisor B S hS X D) :
    HasEtaleLocalProperty B S hS D.1.toFunctor
      (fun T : Scheme.{u} => ∃ h : IsLocallyNoetherian T, @HasPropertySk T h 1)
```

## Tag 0DML, a lemma

[Tag 0DML](https://stacks.math.columbia.edu/tag/0DML) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isEffectiveCartierDivisor_compl_denseAffineOpen'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDenseAffineOpen.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDenseAffineOpen.lean#L401).

> **Stacks Project, Tag 0DML.** Let `S` be a scheme and let `X` be a regular Noetherian
> separated algebraic space over `S`.  Let `U ⊆ X` be a dense affine open subspace, presented by
> an open immersion `u : h_W ⟶ X` whose source has affine underlying scheme and whose set of
> points is dense.  Then there is an effective Cartier divisor `D ⊆ X` with `U = X ∖ D`.
>
> This is `AlgebraicGeometry.Space.exists_isEffectiveCartierDivisor_compl_denseAffineOpen` with
> both of its inputs supplied: the reduced induced form of Stacks 0BCW on a scheme by
> `AlgebraicGeometry.isEffectiveCartierDivisor_vanishingIdeal_compl_denseAffineOpen`, and the
> implication (2) ⟹ (1) of Stacks 083C by
> `AlgebraicGeometry.Space.isEffectiveCartierDivisor_of_hasEffectiveCartierEtaleCover`.

```lean
theorem exists_isEffectiveCartierDivisor_compl_denseAffineOpen'
    (X : AlgebraicSpaces B S hS)
    (hsep : IsAbsolutelySeparated B S hS hZ X.1)
    (hnoeth : IsNoetherian B S hS hZ X.1)
    (hreg : HasEtaleLocalProperty B S hS X.1
      (fun T : Scheme.{u} => _root_.AlgebraicGeometry.IsRegular T))
    (W : BigFppfOver B S hS) (hWaff : IsAffine ((BigFppfOver.toScheme B S hS).obj W))
    (u : yoneda.obj W ⟶ X.1) (hu : IsOpenImmersion B S hS u)
    (hudense : Dense (Set.range (pointsMap B S hS (yoneda.obj W) u))) :
    ∃ D : ClosedSubspaces B S hS X.1,
      IsEffectiveCartierDivisor B S hS X D ∧
        Set.range (pointsMap B S hS D.1.toFunctor D.1.ι) =
          (Set.range (pointsMap B S hS (yoneda.obj W) u))ᶜ
```

## Tag 0DMM, a lemma

[Tag 0DMM](https://stacks.math.columbia.edu/tag/0DMM) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isEffectiveCartierDivisor_iso_differenceDivisorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InvertibleDivisorDifference.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/InvertibleDivisorDifference.lean#L408).

> **Stacks Project, Tag 0DMM.**  Let `S` be a scheme and let `X` be a regular Noetherian
> separated algebraic space over `S`.  Then every invertible `𝒪_X`-module `L` is isomorphic to
> `𝒪_X(D - D') = 𝒪_X(D) ⊗_{𝒪_X} 𝒪_X(D')^{⊗ -1}` for effective Cartier divisors `D, D' ⊆ X`.
>
> Following the source: choose a dense affine open subspace `U ⊆ X` on which `L` is trivial
> (`AlgebraicGeometry.Space.exists_denseAffineOpenChart_bijective_smul`); its complement is an
> effective Cartier divisor `D₀` by Stacks 0DML; the trivialization `𝒪_U ≅ L|_U` extends to a
> monomorphism `𝓘_{D₀}^{n} ⟶ L` for some `n > 0` by Stacks 07UM
> (`AlgebraicGeometry.Space.exists_mono_idealPowModule_of_iso`), and `𝓘_{D₀}^{n}` is the ideal
> sheaf of the effective Cartier divisor `n D₀` (Stacks 083U, 083V).  Twisting by `𝒪_X(n D₀)`
> gives a regular global section of `L ⊗ 𝒪_X(n D₀)`, which is `𝒪_X(D)` for an effective Cartier
> divisor `D` by Stacks 0847, part (2); so `L ≅ 𝒪_X(D - n D₀)`.

```lean
theorem exists_isEffectiveCartierDivisor_iso_differenceDivisorSheaf
    (X : AlgebraicSpaces B S hS)
    (separated : IsAbsolutelySeparated B S hS hZ X.1)
    (noetherian : IsNoetherian B S hS hZ X.1)
    (regular : HasEtaleLocalProperty B S hS X.1
      (fun T : Scheme.{u} => _root_.AlgebraicGeometry.IsRegular T))
    (L : SheafOfModules.{u} (structureRingSheaf B S hS X))
    (invertible : AlgebraicGeometry.SheafOfModules.IsInvertible (structureCommRings B S hS X)
      (structureRingSheaf B S hS X).property L) :
    ∃ (D D' : ClosedSubspaces B S hS X.1) (cD : IsEffectiveCartierDivisor B S hS X D)
      (cD' : IsEffectiveCartierDivisor B S hS X D'),
      Nonempty (L ≅ differenceDivisorSheaf B S hS X D D' cD cD')
```

## Tag 0DMC, a lemma

[Tag 0DMC](https://stacks.math.columbia.edu/tag/0DMC) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isEffectiveCartierDivisor_genericFibre_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierGenericFibreExtension.lean, line 960](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierGenericFibreExtension.lean#L960).

> Let `R` be a valuation ring with fraction field `K`, and let `X` be an algebraic space over
> `R` whose structure morphism `X → Spec R` is smooth. For every effective Cartier divisor
> `D ⊆ X_K` there is an effective Cartier divisor `D' ⊆ X` with `D'_K = D`.
>
> Here `X_K` is the base change of `X` along `Spec K → Spec R`, that is the restriction of `X`
> along `CategoryTheory.OverShriek.relocalizeRestrict`, and `D'_K` is the base change of the
> closed subspace `D'`, `CategoryTheory.OverShriek.relocalizeRestrictSubfunctor`, a closed subspace
> of `X_K`. The divisor `D'` is the scheme-theoretic image of `D → X_K → X`.

```lean
theorem _root_.AlgebraicGeometry.Space.exists_isEffectiveCartierDivisor_genericFibre_eq
    {R : Type u} [CommRing R] [IsDomain R] [ValuationRing R]
    {K : Type u} [Field K] [Algebra R K] [IsFractionRing R K]
    (B : BigFppfSite.{u}) (hR : B.Contains (Spec (.of R))) (hK : B.Contains (Spec (.of K)))
    (X : AlgebraicSpaces B (Spec (.of R)) hR)
    (hX : Space.IsSmooth B (Spec (.of R)) hR (Space.toBaseSiteMap B (Spec (.of R)) hR X.1))
    (D : Space.ClosedSubspaces B (Spec (.of K)) hK
      ((OverShriek.relocalizeRestrict (Space.specAlgebraMapHom B R K hR hK)).obj X.1))
    (hD : Space.IsEffectiveCartierDivisor B (Spec (.of K)) hK
      ⟨(OverShriek.relocalizeRestrict (Space.specAlgebraMapHom B R K hR hK)).obj X.1,
        isAlgebraicSpace_relocalizeRestrict B (Spec (.of K)) (Spec (.of R)) hK hR
          (Space.specAlgebraMapHom B R K hR hK) X.1 X.2⟩ D) :
    ∃ D' : Space.ClosedSubspaces B (Spec (.of R)) hR X.1,
      Space.IsEffectiveCartierDivisor B (Spec (.of R)) hR X D' ∧
        OverShriek.relocalizeRestrictSubfunctor (Space.specAlgebraMapHom B R K hR hK) D'.1 =
          D.1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.8, Tag 0CPH](https://stacks.math.columbia.edu/tag/0CPH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
