---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isThickeningHom_iff_isThickening_smallEtaleRingedToposHom, AlgebraicGeometry.Space.FlatThickeningDeformation.classes_naturalAddTorsor_and_autMulEquiv, AlgebraicGeometry.Space.isEquivalence_of_isPushoutFunctor_of_isIso_coherator_map_of_qcqs, AlgebraicGeometry.Space.isEquivalence_of_isKernelPushoutFunctor_of_isIso_coherator_map_of_qcqs
statement: formalized
proof: formalized
---

# 91.14 Deformations of algebraic spaces

Section 91.14 of the Stacks Project, [Tag 0D15](https://stacks.math.columbia.edu/tag/0D15). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D16, a lemma

[Tag 0D16](https://stacks.math.columbia.edu/tag/0D16) in the Stacks Project.

**`AlgebraicGeometry.Space.isThickeningHom_iff_isThickening_smallEtaleRingedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SmallEtaleRingedToposThickeningIff.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SmallEtaleRingedToposThickeningIff.lean#L143).

> **Stacks 0D16.**  Let `S` be a scheme and `i : Z ⟶ Z'` a morphism of algebraic spaces over
> `S`.  Then `i` is a thickening of algebraic spaces (Stacks 05ZJ, Definition 05ZK: a closed
> immersion identifying `Z` with a closed subspace of `Z'` having the same points, here in the
> morphism form `AlgebraicGeometry.Space.IsThickeningHom`) if and only if the associated morphism
> `i_small : (Sh(Z_étale), 𝒪_Z) ⟶ (Sh(Z'_étale), 𝒪_{Z'})` of ringed topoi (Stacks 03G8,
> `AlgebraicGeometry.Space.smallEtaleRingedToposHom`) is a thickening in the sense of Stacks 08M6
> (`Deformation.ToposThickening.IsThickening`).

```lean
theorem isThickeningHom_iff_isThickening_smallEtaleRingedToposHom
    {Z Z' : AlgebraicSpaces B S hS} (i : Z ⟶ Z') :
    IsThickeningHom B S hS i ↔
      Deformation.ToposThickening.IsThickening.{u, u + 1, u, u, u + 1, u}
        (smallEtaleRingedToposHom B S hS i)
```

## Tag 0D17, a lemma

[Tag 0D17](https://stacks.math.columbia.edu/tag/0D17) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatThickeningDeformation.classes_naturalAddTorsor_and_autMulEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatThickeningDeformation/NaturalClassification.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FlatThickeningDeformation/NaturalClassification.lean#L128). The attribute's comment: “both parts, with the action on isomorphism classes characterised by the obstruction class of 08UG as in 08UK, and the isomorphism Aut = Ext^0 given explicitly through the automorphism (phi^#)^(-1) of the solution and 08UG”.

> **[Stacks Project, Tag 0D17]**, with its natural structures. Let `S` be a scheme, `Y ⊂ Y'` a
> first order thickening of algebraic spaces over `S` (`hZ`) and `f : X ⟶ Y` a flat morphism of
> algebraic spaces over `S` (`hf`). If there exists a flat `f' : X' ⟶ Y'` with an isomorphism
> `a : X ≅ X' ×_{Y'} Y` over `Y` (`hD`; a `Deformation f` is exactly such a pair, see
> `Deformation.ofPair`, `Deformation.pairIso`), then
> 1. the set `Classes f` of isomorphism classes of pairs `(f', a)` is principal homogeneous under
>    `Ext¹_{𝒪_X}(NL_{X/Y}, f^*𝒞_{Y/Y'})`, for the action of [Stacks 08UK]: `ξ` carries `[D₁]` to
>    `[D₂]` exactly when the obstruction class `Deformation.obstruction D₁ D₂` of [Stacks 08UG] of
>    the two deformations is `ξ`; and
> 2. for every such pair `D`, the group `Aut D` of automorphisms `φ : X' ⟶ X'` over `Y'` reducing to
>    the identity on `X' ×_{Y'} Y` is `Ext⁰_{𝒪_X}(NL_{X/Y}, f^*𝒞_{Y/Y'})`, by the group isomorphism
>    sending `φ` to the class in `Ext⁰` of [Stacks 08UG] of the automorphism `(φ^♯)⁻¹` of the
>    solution `0 → f^*𝒞_{Y/Y'} → i⁻¹𝒪_{X'} → 𝒪_X → 0` (`Deformation.autMulEquivAmbientSolution`
>    followed by `solutionAutMulEquivExtZero`).
>
> `NL_{X/Y}` is the canonical naive cotangent complex `naiveCotangentComplex B S hS f`; the module
> `f^*𝒞_{Y/Y'}` is `liftedPulledBackConormal hZ f`; the `Ext` groups are those of any model of the
> derived category of `𝒪_X`-modules.

```lean
theorem classes_naturalAddTorsor_and_autMulEquiv (hf : IsFlat B S hS f.hom)
    (hD : Nonempty (Deformation f)) :
    (∃ T : AddTorsor
        (DerivedCategory.Ext (DerivedCategory.Q.obj (naiveCotangentComplex B S hS f))
          ((DerivedCategory.singleFunctor _ 0).obj (liftedPulledBackConormal hZ f)) 1)
        (Classes f),
      ∀ (ξ : DerivedCategory.Ext (DerivedCategory.Q.obj (naiveCotangentComplex B S hS f))
          ((DerivedCategory.singleFunctor _ 0).obj (liftedPulledBackConormal hZ f)) 1)
        (D₁ D₂ : Deformation f),
        T.vadd ξ (Quotient.mk (setoid f) D₁) = Quotient.mk (setoid f) D₂ ↔
          D₁.obstruction hZ D₂ = ξ) ∧
      ∀ D : Deformation f, ∃ e : Aut D ≃* Multiplicative (DerivedCategory.Ext
        (DerivedCategory.Q.obj (naiveCotangentComplex B S hS f))
        ((DerivedCategory.singleFunctor _ 0).obj (liftedPulledBackConormal hZ f)) 0),
        ∀ φ : Aut D, e φ = solutionAutMulEquivExtZero hZ f (D.ambientSolution hZ)
          (Deformation.autMulEquivAmbientSolution hZ D φ)
```

## Tag 0D3P, a lemma

[Tag 0D3P](https://stacks.math.columbia.edu/tag/0D3P) in the Stacks Project.

**`AlgebraicGeometry.Space.isEquivalence_of_isPushoutFunctor_of_isIso_coherator_map_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlgebraExtensionPushoutQcqs.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlgebraExtensionPushoutQcqs.lean#L296).

> **[Stacks Project, Tag 0D3P].** Let `f : X ⟶ Y` be a morphism of algebraic spaces with `X`
> quasi-compact and quasi-separated, let `φ : ℱ ⟶ 𝒢` be a morphism of `𝒪_X`-modules such that
> `DQ_X(ℱ) ⟶ DQ_X(𝒢)` is an isomorphism, where `DQ_X` is the right adjoint of
> `D_QCoh(𝒪_X) ⥤ D(𝒪_X)` of [Stacks Project, Tag 0CR4], and let `F` be pushout along `φ`, from
> extensions `0 ⟶ ℱ ⟶ 𝒪' ⟶ 𝒪_X ⟶ 0` of `f⁻¹𝒪_Y`-algebras on `X_étale` to extensions by `𝒢`
> (characterised by the universal property of the pushout). Then `F` is an equivalence of
> categories.
>
> The quasi-coherence of `NL_{X/Y}` which the source's proof uses is
> `AlgebraicGeometry.Space.qcohDerivedProp_modelNaiveCotangentComplex`, from
> [Stacks Project, Tag 0D0Y].

```lean
theorem isEquivalence_of_isPushoutFunctor_of_isIso_coherator_map_of_qcqs
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (hXc : IsQuasiCompactSpace B S hS X.1) (hXs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    {M N : SheafOfModules.{u} ((sheafCompose (SmallEtale.topology B S hS X.1)
      (forget₂ CommRingCat.{u} RingCat.{u})).obj (structureSheaf B S hS X.1 X.2))}
    (φ : M ⟶ N)
    {F : AlgebraExtension (J := SmallEtale.topology B S hS X.1) (inverseImageBaseMap B S hS f) M ⥤
      AlgebraExtension (J := SmallEtale.topology B S hS X.1) (inverseImageBaseMap B S hS f) N}
    (hF : IsPushoutFunctor.{u, u + 1, u} (a := inverseImageBaseMap B S hS f) φ F)
    (hDQ : letI := quasicoherentDerivedInclusion_isLeftAdjoint_of_qcqs B S hS hZ X.1 X.2 hXc hXs
      IsIso ((qcohDerivedProp B S hS X).ι.rightAdjoint.map
        ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS X.1 X.2) 0).map φ))) :
    F.IsEquivalence
```

## Tag 0D3Q, a lemma

[Tag 0D3Q](https://stacks.math.columbia.edu/tag/0D3Q) in the Stacks Project.

**`AlgebraicGeometry.Space.isEquivalence_of_isKernelPushoutFunctor_of_isIso_coherator_map_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ThickenedBasePushoutEquivalence.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ThickenedBasePushoutEquivalence.lean#L66).

> **[Stacks Project, Tag 0D3Q].** Let `f : X ⟶ D` be a morphism of algebraic spaces with `X`
> quasi-compact and quasi-separated, and `i : D ⟶ D'` a closed immersion (for instance a first order
> thickening). Let `P` be a square-zero extension problem (91.13.0.1) of the small étale ringed
> topoi over `f` whose thickened base is `i⁻¹𝒪_{D'}`, its reduction being `i♯`, with prescribed
> ideal module `ℱ`. Let `φ : ℱ ⟶ 𝒢` be a morphism of `𝒪_X`-modules with `DQ_X(ℱ) ⟶ DQ_X(𝒢)` an
> isomorphism, `DQ_X` the right adjoint of `D_QCoh(𝒪_X) ⥤ D(𝒪_X)` of [Stacks Project, Tag 0CR4],
> and let `FT` be pushout along `φ` from the solutions of `P` to those of the problem with ideal
> module `𝒢` (characterised by the universal property of the pushout). Then `FT` is an equivalence
> of categories.
>
> The source asks `D ⊂ D'` to be a first order thickening; the argument only uses that `i` is a
> closed immersion, the square-zero condition being part of the problem `P`.

```lean
theorem isEquivalence_of_isKernelPushoutFunctor_of_isIso_coherator_map_of_qcqs
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (hXc : IsQuasiCompactSpace B S hS X.1) (hXs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (f : X ⟶ D) (i : D ⟶ D') (hi : IsClosedImmersion B S hS i.hom)
    (P : RingedToposExtensionProblem (smallEtaleRingedTopos B S hS X)
      (smallEtaleRingedTopos B S hS D))
    (hPf : P.f = smallEtaleRingedToposHom B S hS f)
    (eBase : P.baseExtension ≅
      (smallEtaleInverseImageRing B S hS i).obj (smallEtaleRingedTopos B S hS D').O)
    (heBase : eBase.hom ≫ (smallEtaleRingedToposHom B S hS i).fSharpInverseImage =
      P.baseReduction)
    {N : SheafOfModules.{u} ((sheafCompose (SmallEtale.topology B S hS X.1)
      (forget₂ CommRingCat.{u} RingCat.{u})).obj (structureSheaf B S hS X.1 X.2))}
    (φ : P.G ⟶ N)
    {FT : P.CompatibleFirstOrderThickening ⥤
      (RingedToposExtensionProblem.changeKernel P φ).CompatibleFirstOrderThickening}
    (hFT : RingedToposExtensionProblem.IsKernelPushoutFunctor.{u, u + 1, u, u, u + 1, u}
      (S := P) φ FT)
    (hDQ : letI := quasicoherentDerivedInclusion_isLeftAdjoint_of_qcqs B S hS hZ X.1 X.2 hXc hXs
      IsIso ((qcohDerivedProp B S hS X).ι.rightAdjoint.map
        ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS X.1 X.2) 0).map φ))) :
    FT.IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 91.14, Tag 0D15](https://stacks.math.columbia.edu/tag/0D15)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
