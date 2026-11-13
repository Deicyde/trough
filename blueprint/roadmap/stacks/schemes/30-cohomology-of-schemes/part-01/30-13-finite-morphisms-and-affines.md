---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.FiniteSurjectiveCoherentSupport.exists_isCoherent_supp_pushforward_eq_range, Stacks.AlgebraicGeometry.PushforwardIdealSubsheaf.idealPowSmul_pushforward_eq, Stacks.AlgebraicGeometry.Tag01YQClauseThree.isAffine_of_isFinite_surjective
statement: formalized
proof: formalized
---

# 30.13 Finite morphisms and affines

Section 30.13 of the Stacks Project, [Tag 01YN](https://stacks.math.columbia.edu/tag/01YN). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01YO, a lemma

[Tag 01YO](https://stacks.math.columbia.edu/tag/01YO) in the Stacks Project.

**`Stacks.AlgebraicGeometry.FiniteSurjectiveCoherentSupport.exists_isCoherent_supp_pushforward_eq_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteSurjectiveCoherentSupport/Basic.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiniteSurjectiveCoherentSupport/Basic.lean#L341).

> **[Stacks, Tag 01YO].** Let `f : Y ⟶ X` be finite and surjective with `X` locally Noetherian
> and let `i : Z ⟶ X` be an integral closed subscheme with generic point `ξ`. Then there is a
> coherent module `ℱ` on `Y` whose direct image `f_* ℱ` has support exactly `Z` and whose stalk at
> `ξ` is annihilated by the maximal ideal of `𝒪_{X,ξ}`.

```lean
theorem exists_isCoherent_supp_pushforward_eq_range
    {X Y Z : Scheme.{u}} (f : Y ⟶ X) [IsFinite f] [Surjective f]
    [IsLocallyNoetherian X] (i : Z ⟶ X) [IsClosedImmersion i] [IsIntegral Z] :
    ∃ F : Y.Modules, F.IsCoherent ∧
      SheafOfModules.supp ((Scheme.Modules.pushforward f).obj F) = Set.range i ∧
      (let G := (Scheme.Modules.pushforward f).obj F
       let x := i (genericPoint Z)
       letI : Module (X.presheaf.stalk x)
           (TopCat.Presheaf.stalk (C := Ab.{u}) G.val.presheaf x) :=
         PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
           (R := X.presheaf) G.val x
       ∀ a : X.presheaf.stalk x,
         a ∈ IsLocalRing.maximalIdeal (X.presheaf.stalk x) →
         ∀ s : TopCat.Presheaf.stalk (C := Ab.{u}) G.val.presheaf x, a • s = 0)
```

## Tag 01YP, a lemma

[Tag 01YP](https://stacks.math.columbia.edu/tag/01YP) in the Stacks Project.

**`Stacks.AlgebraicGeometry.PushforwardIdealSubsheaf.idealPowSmul_pushforward_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SheafPushforward/Basic.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SheafPushforward/Basic.lean#L228). The attribute's comment: “𝒥 · f₊ℱ = f₊((f⁻¹𝒥) · ℱ) as an equality of subsheaves of f₊ℱ, for f affine, ℱ quasi-coherent and 𝒥 a quasi-coherent sheaf of ideals”.

> **[Stacks, Tag 01YP], as an equality of subsheaves of `f₊ℱ`.** For an affine morphism
> `f : Y ⟶ X`, a quasi-coherent `ℱ` and a quasi-coherent sheaf of ideals `𝒥` on `X`,
>
>     𝒥 · f₊ℱ = f₊((f⁻¹𝒥) · ℱ)
>
> as submodules of `f₊ℱ`. Here `𝒥 · f₊ℱ` is `idealPowSmul J 1 (f₊ℱ)`, the quasi-coherent
> subsheaf of `f₊ℱ` with sections `J(U) · Γ(f₊ℱ, U)` over each affine open `U`; the inverse image
> `f⁻¹𝒥` acts on `ℱ` through `f^♯`, so `(f⁻¹𝒥) · ℱ` is `idealPowSmul (J.comap f) 1 ℱ`, with
> `J.comap f` the ideal sheaf `f⁻¹𝒥 · 𝒪_Y`; and `f₊` of that subsheaf of `ℱ` is the subsheaf
> `pushforwardSubmodule f _` of `f₊ℱ`, whose module sheaf is `f₊` of it by `rfl`
> (`toSheafOfModules_pushforwardSubmodule`).
>
> The proof is the source's: the question is local on `X`, so it reduces to the affine-local
> computation
> `Stacks.AlgebraicGeometry.AffineIdealPushforward.ideal_smul_pushforward_sections_eq`
> (`I(M_A) = ((IB)M)_A`), and `submodule_ext_affineOpens` upgrades that to the subsheaves, since
> both sides are submodules of one module sheaf and affine opens form a basis.

```lean
theorem idealPowSmul_pushforward_eq (f : Y ⟶ X) [IsAffineHom f] (J : X.IdealSheafData)
    (ℱ : Y.Modules) [ℱ.IsQuasicoherent] :
    IdealPowerSmul.idealPowSmul J 1 ((Scheme.Modules.pushforward f).obj ℱ) =
      pushforwardSubmodule f (IdealPowerSmul.idealPowSmul (J.comap f) 1 ℱ)
```

## Tag 01YQ, a lemma

[Tag 01YQ](https://stacks.math.columbia.edu/tag/01YQ) in the Stacks Project.

**`Stacks.AlgebraicGeometry.Tag01YQClauseThree.isAffine_of_isFinite_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClauseThree/GenericStalkInput.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ClauseThree/GenericStalkInput.lean#L61).

> A Noetherian scheme admitting a finite surjective morphism from an affine scheme is affine.

```lean
theorem isAffine_of_isFinite_surjective {X Y : Scheme.{u}} (f : Y ⟶ X)
    [IsFinite f] [Surjective f] [IsAffine Y] [IsNoetherian X] :
    IsAffine X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.13, Tag 01YN](https://stacks.math.columbia.edu/tag/01YN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
