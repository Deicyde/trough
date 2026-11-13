---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.different, AlgebraicGeometry.Scheme.Hom.isCoherent_different, Stacks.Discriminant.different_obj_affine_eq_dedekindDifferentIdeal, Stacks.Discriminant.different_sections_eq_noetherDifferent, Stacks.Discriminant.exists_bijectiveClosedImmersion_different_baseChange, Stacks.Discriminant.isIso_different_baseChange_of_flat, Stacks.Discriminant.isIso_different_baseChange_of_invertible, Stacks.Discriminant.finiteLocallyFreeNorm_app_mem_discriminantIdeal
statement: formalized
proof: formalized
---

# 49.9 The different

Section 49.9 of the Stacks Project, [Tag 0BTC](https://stacks.math.columbia.edu/tag/0BTC). 7 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BW4, a definition

[Tag 0BW4](https://stacks.math.columbia.edu/tag/0BW4) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.different`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/Basic.lean, line 375](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/Basic.lean#L375). The attribute's comment: “the different”.

> The *different* `𝔇_f ⊆ 𝒪_Y` of a flat locally quasi-finite morphism `f : Y ⟶ X` of locally
> Noetherian schemes: the annihilator of the cokernel of the map `𝒪_Y → ω_{Y/X}`, `1 ↦ τ_{Y/X}`,
> where `ω_{Y/X}` is the relative dualizing module
> `Stacks.Discriminant.relativeDualizingModuleData f` and `τ_{Y/X}` is its trace element
> `Stacks.Discriminant.relativeTraceSection`.
>
> The hypothesis `LocallyOfFiniteType f` is part of the source's "locally quasi-finite", which
> includes being locally of finite type; Mathlib's `LocallyQuasiFinite` does not.  The ideal does
> not depend on the relative dualizing module chosen: `Scheme.Hom.different_eq`.

```lean
def _root_.AlgebraicGeometry.Scheme.Hom.different :
    (SheafOfModules.unit (structureSheafRing Y.toRingedSpace)).Submodule
```

**`AlgebraicGeometry.Scheme.Hom.isCoherent_different`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/Basic.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/Basic.lean#L401). The attribute's comment: “coherence”.

> The different `𝔇_f` of a flat locally quasi-finite morphism of locally Noetherian schemes is
> a coherent ideal of `𝒪_Y`.

```lean
theorem _root_.AlgebraicGeometry.Scheme.Hom.isCoherent_different :
    Stacks.SheafOfModules.IsCoherent f.different.toSheafOfModules
```

## Tag 0BW5, a lemma

[Tag 0BW5](https://stacks.math.columbia.edu/tag/0BW5) in the Stacks Project.

**`Stacks.Discriminant.different_obj_affine_eq_dedekindDifferentIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/DedekindComparison.lean, line 333](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/DedekindComparison.lean#L333).

> **[Stacks, Tag 0BW5].** Let `f : Y → X` be a flat quasi-finite morphism of locally
> Noetherian schemes and let `V = Spec B ⊆ Y` and `U = Spec A ⊆ X` be affine opens with
> `f(V) ⊆ U`.  If the Dedekind different of `A → B` is defined, then the sections of the different
> `𝔇_f` over `V` are the Dedekind different ideal `𝔇_{B/A} ⊆ B`.
>
> Both `𝔇_f` and the ideal sheaf associated with `𝔇_{B/A}` are coherent ideal sheaves on the
> affine `V`, and a coherent sheaf on an affine scheme is the tilde of its module of sections; so
> this equality of ideals of `B` is the assertion that `𝔇_f|_V = (𝔇_{B/A})~`.

```lean
theorem different_obj_affine_eq_dedekindDifferentIdeal (ω : RelativeDualizingModuleData f)
    (τ : RelativeTraceSection ω) (U : X.affineOpens) (V : Y.affineOpens)
    (hVU : V.1 ≤ f ⁻¹ᵁ U.1) :
    letI : Algebra Γ(X, U.1) Γ(Y, V.1) := (f.appLE U V hVU).hom.toAlgebra
    ∀ setup : DedekindDifferentSetup Γ(X, U.1) Γ(Y, V.1),
      (show Ideal Γ(Y, V.1) from (different ω τ).toSubmodule.obj (op V.1)) =
        dedekindDifferentIdeal setup
```

## Tag 0BW6, a lemma

[Tag 0BW6](https://stacks.math.columbia.edu/tag/0BW6) in the Stacks Project.

**`Stacks.Discriminant.different_sections_eq_noetherDifferent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/NoetherComparison.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/NoetherComparison.lean#L167).

> **[Stacks, Tag 0BW6].** Let `f : Y ⟶ X` be flat and locally quasi-finite between locally
> Noetherian schemes, with relative dualizing module `ω` and trace section `τ`.  On affine opens
> `V = Spec B ⊆ Y` and `U = Spec A ⊆ X` with `f(V) ⊆ U`, if the algebraic relative dualizing
> module `ω_{B/A}` is an invertible `B`-module, then the ideal of sections of the different over
> `V` is the Noether different of `B` over `A`.
>
> The source states this as `𝔇_f|_V = 𝔇~` as coherent ideal sheaves on `V`; the different is a
> coherent ideal sheaf, so on the affine `V` it is the tilde of its ideal of sections and the two
> readings agree.

```lean
theorem different_sections_eq_noetherDifferent (ω : RelativeDualizingModuleData f)
    (τ : RelativeTraceSection ω) (U : X.affineOpens) (V : Y.affineOpens)
    (hVU : V.1 ≤ f ⁻¹ᵁ U.1) :
    letI : Algebra Γ(X, U.1) Γ(Y, V.1) := (f.appLE U V hVU).hom.toAlgebra
    letI : IsNoetherianRing Γ(X, U.1) := IsLocallyNoetherian.component_noetherian U
    letI : IsNoetherianRing Γ(Y, V.1) := IsLocallyNoetherian.component_noetherian V
    letI : Module.Flat Γ(X, U.1) Γ(Y, V.1) :=
      RingHom.flat_algebraMap_iff.mp (f.flat_appLE U.2 V.2 hVU)
    letI : Algebra.QuasiFinite Γ(X, U.1) Γ(Y, V.1) :=
      RingHom.quasiFinite_algebraMap.mp (LocallyQuasiFinite.quasiFinite_appLE U.2 V.2 hVU)
    ∀ (F : FiniteOpenFactorization.{u, u, u} Γ(X, U.1) Γ(Y, V.1)),
      Module.Invertible Γ(Y, V.1) (dualizingModule F) →
        (show Ideal Γ(Y, V.1) from (different ω τ).toSubmodule.obj (op V.1)) =
          noetherDifferent Γ(X, U.1) Γ(Y, V.1)
```

## Tag 0BW7, a lemma

[Tag 0BW7](https://stacks.math.columbia.edu/tag/0BW7) in the Stacks Project.

**`Stacks.Discriminant.exists_bijectiveClosedImmersion_different_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/BaseChange.lean, line 677](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/BaseChange.lean#L677). The attribute's comment: “the bijective closed immersion”.

> **[Stacks, Tag 0BW7].** Consider a cartesian diagram of locally Noetherian schemes with
> `f : Y ⟶ X` flat and locally quasi-finite, let `R ⊆ Y` and `R' ⊆ Y'` be the closed subschemes
> cut out by the differents `𝔇_f` and `𝔇_{f'}`. Then `Y' → Y` induces a bijective closed immersion
> `R' → R ×_Y Y'`.

```lean
theorem exists_bijectiveClosedImmersion_different_baseChange
    (hi : i.ker = differentIdealSheaf ω τ) (hi' : i'.ker = differentIdealSheaf ω' τ') :
    ∃ (k : R' ⟶ R) (hk : k ≫ i = i' ≫ pullback.fst f g),
      IsClosedImmersion (pullback.lift k i' hk) ∧
        Function.Bijective (pullback.lift k i' hk).base
```

**`Stacks.Discriminant.isIso_different_baseChange_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/BaseChange.lean, line 688](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/BaseChange.lean#L688). The attribute's comment: “equality under flat base change”.

> **[Stacks, Tag 0BW7], flat base change.** If moreover `g` is flat then `R' = R ×_Y Y'`.

```lean
theorem isIso_different_baseChange_of_flat [Flat g]
    (hi : i.ker = differentIdealSheaf ω τ) (hi' : i'.ker = differentIdealSheaf ω' τ')
    (k : R' ⟶ R) (hk : k ≫ i = i' ≫ pullback.fst f g) :
    IsIso (pullback.lift k i' hk)
```

**`Stacks.Discriminant.isIso_different_baseChange_of_invertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/BaseChange.lean, line 699](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/BaseChange.lean#L699). The attribute's comment: “equality for invertible dualizing module”.

> **[Stacks, Tag 0BW7], invertible dualizing module.** If moreover `ω_{Y/X}` is invertible
> then `R' = R ×_Y Y'`, for an arbitrary `g`.

```lean
theorem isIso_different_baseChange_of_invertible
    (hinv : ∀ V : Y.affineOpens, Module.Invertible Γ(Y, V.1) Γ(ω.sheaf, V.1))
    (hi : i.ker = differentIdealSheaf ω τ) (hi' : i'.ker = differentIdealSheaf ω' τ')
    (k : R' ⟶ R) (hk : k ≫ i = i' ≫ pullback.fst f g) :
    IsIso (pullback.lift k i' hk)
```

## Tag 0BW8, a lemma

[Tag 0BW8](https://stacks.math.columbia.edu/tag/0BW8) in the Stacks Project.

**`Stacks.Discriminant.finiteLocallyFreeNorm_app_mem_discriminantIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/NormDiscriminant.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/NormDiscriminant.lean#L309).

> **[Stacks, Tag 0BW8].** Let `f : Y → X` be a finite flat morphism of locally Noetherian
> schemes, with source `Y` and base `X`, and let `𝔇_f ⊆ 𝒪_Y` be the different attached to a
> relative dualizing module `ω_{Y/X}` and a trace element `τ_{Y/X}`.  Then the norm
> `Norm_f : f_*𝒪_Y → 𝒪_X` carries `f_*𝔇_f` into the ideal sheaf of the discriminant `D_f`: over
> every affine open `U` of the base the norm of a section of `𝔇_f` on `f ⁻¹ᵁ U` lies in the
> discriminant ideal of `U`.

```lean
theorem finiteLocallyFreeNorm_app_mem_discriminantIdeal (ω : RelativeDualizingModuleData f)
    (τ : RelativeTraceSection ω) (U : X.affineOpens) (s : Γ(Y, f ⁻¹ᵁ U.1))
    (hs : s ∈ (show Ideal Γ(Y, f ⁻¹ᵁ U.1) from
      (different ω τ).toSubmodule.obj (op (f ⁻¹ᵁ U.1)))) :
    letI : Stacks.Morphisms.IsFiniteLocallyFree f :=
      (Stacks.Morphisms.isFiniteLocallyFree_iff_isFinite_flat_of_isLocallyNoetherian f).mpr
        ⟨inferInstance, inferInstance⟩
    (Stacks.Norm.finiteLocallyFreeNorm f).app U.1 s ∈ (discriminantIdeal f).ideal U
```

**`Stacks.Discriminant.finiteProjective_mem_algebraDiscriminantIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/NormDifferent.lean, line 458](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Discriminant/NormDifferent.lean#L458). The attribute's comment: “the affine computation”.

> **Stacks Project, Tag 0BW8, the affine computation.** For a finite projective algebra
> `A → B` whose Dedekind different is defined, the norm of an element of the Dedekind different
> belongs to the discriminant ideal of `B` over `A`. The norm here is the projective norm
> `Algebra.projectiveNorm`, which agrees with `Algebra.norm` when `B` is free over `A`.

```lean
theorem finiteProjective_mem_algebraDiscriminantIdeal
    (setup : DedekindDifferentSetup A B) [Module.Finite A B] [Module.Projective A B]
    {b : B} (hb : b ∈ dedekindDifferentIdeal setup) :
    Algebra.projectiveNorm A b ∈ algebraDiscriminantIdeal A B
```

## Tag 0BW9, a lemma

[Tag 0BW9](https://stacks.math.columbia.edu/tag/0BW9) in the Stacks Project.

**`Stacks.Discriminant.range_eq_setOf_not_etaleAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/EtaleLocus.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/EtaleLocus.lean#L327). The attribute's comment: “the non-étale locus”.

> For a flat quasi-finite morphism of locally Noetherian schemes, the closed subscheme
> `R ⊆ Y` cut out by the different `𝔇_f` is exactly the set of points at which `f` is not
> étale.

```lean
theorem range_eq_setOf_not_etaleAt (ω : RelativeDualizingModuleData f)
    (τ : RelativeTraceSection ω) {R : Scheme.{u}} (i : R ⟶ Y) [IsClosedImmersion i]
    (hi : i.ker = differentIdealSheaf ω τ) :
    Set.range i.base = {y : Y | ¬ EtaleAt f y}
```

**`Stacks.Discriminant.range_eq_setOf_not_unramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/EtaleLocus.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/EtaleLocus.lean#L337). The attribute's comment: “the non-unramified locus”.

> Equivalently, the closed subscheme cut out by the different is exactly the set of points at
> which `f` is not unramified.

```lean
theorem range_eq_setOf_not_unramifiedAt (ω : RelativeDualizingModuleData f)
    (τ : RelativeTraceSection ω) {R : Scheme.{u}} (i : R ⟶ Y) [IsClosedImmersion i]
    (hi : i.ker = differentIdealSheaf ω τ) :
    Set.range i.base = {y : Y | ¬ UnramifiedAt f y}
```

## Tag 0BWA, a lemma

[Tag 0BWA](https://stacks.math.columbia.edu/tag/0BWA) in the Stacks Project.

**`Stacks.Discriminant.isEffectiveCartierDivisor_differentIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/EffectiveCartier.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/EffectiveCartier.lean#L165). The attribute's comment: “part (3), R is an effective Cartier divisor”.

> **[Stacks, Tag 0BWA (3)], effectivity.**  Let `f : Y ⟶ X` be a flat quasi-finite morphism of
> locally Noetherian schemes with relative dualizing module `ω_{Y/X}` and trace element `τ_{Y/X}`.
> If `ω_{Y/X}` is invertible and `f` is étale at the associated points of `Y`, then the closed
> subscheme `R ⊆ Y` defined by the different `𝔇_f` is an effective Cartier divisor.
>
> By [Stacks, Tag 0C17 (1)] the different is locally principal, and the local generator is a
> nonzerodivisor because it does not vanish at any associated point of `Y`.

```lean
theorem isEffectiveCartierDivisor_differentIdealSheaf
    (hét : ∀ y ∈ Stacks.Divisors.schemeAssociatedPoints Y, EtaleAt f y) :
    Stacks.Divisors.IsEffectiveCartierDivisor (differentIdealSheaf ω τ)
```

**`Stacks.Discriminant.existsUnique_invertibleSheafIso_differentIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/EffectiveCartier.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/EffectiveCartier.lean#L182). The attribute's comment: “part (3), O\_Y(R) = omega\_\{Y/X}”.

> **[Stacks, Tag 0BWA (3)], the isomorphism `𝒪_Y(R) = ω_{Y/X}`.**  Under the hypotheses of
> [Stacks, Tag 0BWA (3)] there is exactly one isomorphism `𝒪_Y(R) ≅ ω_{Y/X}` carrying the
> canonical section `1_R` of `𝒪_Y(R)` to the trace element `τ_{Y/X}`.
>
> The subscheme `R` is the zero scheme of `τ_{Y/X}`, so its effectivity makes `τ_{Y/X}` a regular
> section of `ω_{Y/X}` ([Stacks, Tag 02OR]), and [Stacks, Tag 01X0] trivializes `𝒪_Y(Z(τ_{Y/X})))`
> along it.

```lean
theorem existsUnique_invertibleSheafIso_differentIdealSheaf
    (hét : ∀ y ∈ Stacks.Divisors.schemeAssociatedPoints Y, EtaleAt f y) :
    ∃! e : Stacks.Divisors.invertibleSheaf' (differentIdealSheaf ω τ) ≅ ω.sheaf,
      Scheme.Modules.Hom.app e.hom ⊤
        ((Stacks.Divisors.canonicalSection' (differentIdealSheaf ω τ)).eval (op ⊤)) = τ.sect
```

**`Stacks.Discriminant.isLocallyPrincipal_different`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/LocallyPrincipal.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/LocallyPrincipal.lean#L100). The attribute's comment: “part (1)”.

> **[Stacks, Tag 0BWA (1)].** Let `f : Y ⟶ X` be a flat locally quasi-finite morphism of
> locally Noetherian schemes with relative dualizing module `ω_{Y/X}` and trace element
> `τ_{Y/X}`. If `ω_{Y/X}` is an invertible `𝒪_Y`-module, then the closed subscheme `R ⊆ Y`
> defined by the different `𝔇_f` is a locally principal closed subscheme.

```lean
theorem isLocallyPrincipal_different (ω : RelativeDualizingModuleData f)
    (τ : RelativeTraceSection ω)
    [Stacks.SheafOfModules.IsInvertible Y.presheaf
      (structureSheafRing
        Y.toRingedSpace).property ω.sheaf] :
    Stacks.Divisors.IsLocallyPrincipal
      (Stacks.Divisors.idealSheafDataOfSubmodule (different ω τ))
```

**`Stacks.Discriminant.discriminantIdeal_eq_normIdealSheaf_differentIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/NormDiscriminant.lean, line 506](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/NormDiscriminant.lean#L506). The attribute's comment: “part (2)”.

> **[Stacks, Tag 0BWA (2)].**  Let `f : Y ⟶ X` be a finite flat morphism of locally Noetherian
> schemes with relative dualizing module `ω_{Y/X}` and trace element `τ_{Y/X}`, and let `R ⊆ Y`
> be the closed subscheme cut out by the different `𝔇_f`.  If `ω_{Y/X}` is invertible, then the
> norm of `R` is the discriminant `D_f`: as ideal sheaves on `X`, `Norm_f(𝔇_f)` is the
> discriminant ideal sheaf.
>
> Every point of `X` has an affine open neighbourhood `U = Spec A` with `f⁻¹U = Spec B` free over
> `A` and `ω_{Y/X}` trivial on `f⁻¹U` (Tag 0BUT), so that `Hom_A(B, A)` is free of rank one on some
> `λ`; there `R` is cut out by the `b` with `Tr_{B/A} = b λ` and `D_f` by `Norm_{B/A}(b)`, and
> both sides are ideal sheaves, so they agree.

```lean
theorem discriminantIdeal_eq_normIdealSheaf_differentIdealSheaf
    (ω : RelativeDualizingModuleData f) (τ : RelativeTraceSection ω)
    [Stacks.SheafOfModules.IsInvertible Y.presheaf
      (structureSheafRing Y.toRingedSpace).property ω.sheaf] :
    letI : Stacks.Morphisms.IsFiniteLocallyFree f :=
      (Stacks.Morphisms.isFiniteLocallyFree_iff_isFinite_flat_of_isLocallyNoetherian f).mpr
        ⟨inferInstance, inferInstance⟩
    discriminantIdeal f = Stacks.Norm.normIdealSheaf f (differentIdealSheaf ω τ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 49.9, Tag 0BTC](https://stacks.math.columbia.edu/tag/0BTC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
