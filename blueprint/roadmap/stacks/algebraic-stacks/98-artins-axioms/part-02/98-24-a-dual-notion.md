---
declaration: section
origin: cited
lean: Deformation.Artin.SectionsObstructionModel.exists_finiteProjectiveModel_obstructionSpace, Deformation.Artin.SectionsObstructionModel.exists_finiteProjectiveModel_homology_iso_obstruction, Deformation.Artin.SectionsPerfectComplex.nonempty_derivedCohomology_two_iso_homology_one, Deformation.Artin.DualDeformationSituation, Deformation.Artin.exists_obstructionEvaluation_eq_obstruction, Deformation.Artin.exists_isCotangentObstructionClass, Deformation.Artin.DualNotion.exists_isOpen_isVersalAt_of_isPerfect
statement: formalized
proof: formalized
---

# 98.24 A dual notion

Section 98.24 of the Stacks Project, [Tag 07YV](https://stacks.math.columbia.edu/tag/07YV). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07YW, an example

[Tag 07YW](https://stacks.math.columbia.edu/tag/07YW) in the Stacks Project.

**`Deformation.Artin.SectionsObstructionModel.exists_finiteProjectiveModel_obstructionSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/SectionsObstructionModel.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/SectionsObstructionModel.lean#L208). The attribute's comment: “the obstruction spaces of the example of Tag 07YH are 𝒪\_x(M) = H¹(N ⊗\_Λ M)”.

> **[Stacks, Tag 07YW], the obstruction spaces.** Let `Λ` be Noetherian, let
> `g : W ⟶ Spec Λ` be proper and let `𝓕` be a coherent `𝒪_W`-module flat over `Λ`. Then there is a
> finite complex `N` of finite projective `Λ`-modules such that, for every `Λ`-algebra `A`, every
> cartesian square exhibiting `W_A` as the base change of `W`, and every `A`-module `M`,
>
> `𝒪_x(M) = H¹(W_A, 𝓕_A ⊗_A M) ≅ H¹((N ⊗_Λ A) ⊗_A M)`,
>
> the obstruction space of the obstruction theory of [Stacks, Tag 07YH] at `M`. In degree `i` the
> right-hand complex is `M ⊗_Λ Nⁱ` by
> `Deformation.Artin.SectionsPerfectComplex.tensorComplexXLinearEquiv`, so the right-hand side is
> the source's `H¹(N ⊗_Λ M)`.
>
> Composed with
> `Deformation.Artin.SectionsPerfectComplex.nonempty_derivedCohomology_two_iso_homology_one` this
> is the source's reformulation `𝒪_x(M) = H²(K ⊗^𝐋_A M)` with `K = (N ⊗_Λ A)[-1]`.

```lean
theorem exists_finiteProjectiveModel_obstructionSpace {Λ : Type u} [CommRing Λ]
    {W : Scheme.{u}} (g : W ⟶ Spec (CommRingCat.of Λ)) (F : W.Modules)
    [IsNoetherianRing Λ] [IsProper g] [F.IsCoherent]
    (hflat : IsFlatOver g.toLRSHom.toShHom F) :
    ∃ (N : CochainComplex (ModuleCat.{u} Λ) ℤ) (a b : ℤ),
      N.IsStrictlyGE a ∧ N.IsStrictlyLE b ∧
        (∀ i : ℤ, Module.Finite Λ (N.X i)) ∧ (∀ i : ℤ, Module.Projective Λ (N.X i)) ∧
        ∀ (A : Type u) [CommRing A] (φ : Λ →+* A) {W' : Scheme.{u}}
          {g' : W' ⟶ Spec (CommRingCat.of A)} {p : W' ⟶ W}
          (_hsq : IsPullback p g' g (Spec.map (CommRingCat.ofHom φ)))
          (M : ModuleCat.{u} A),
          Nonempty ((obstructionFunctor g' ((Scheme.Modules.pullback p).obj F)).obj M ≅
            ((tensorComplex M).obj (extendScalarsComplex φ N)).homology 1)
```

**`Deformation.Artin.SectionsObstructionModel.exists_finiteProjectiveModel_homology_iso_obstruction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/SectionsObstructionModel.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/SectionsObstructionModel.lean#L284). The attribute's comment: “there exists a finite complex N of finite projective Λ-modules which universally computes the cohomology of 𝓕”.

> **[Stacks, Tag 07YW], the complex `N`.** Let `Λ` be Noetherian, let `g : W ⟶ Spec Λ` be
> proper and let `𝓕` be a coherent `𝒪_W`-module flat over `Λ`. Then there is a finite complex `N`
> of finite projective `Λ`-modules which universally computes the cohomology of `𝓕` — for every
> base change `φ : Λ → Λ'`, `Hⁱ(W_{Λ'}, 𝓕_{Λ'}) ≅ Hⁱ(N ⊗_Λ Λ')` — and, writing
> `K = (N ⊗_Λ A)[-1]` for a `Λ`-algebra `A`, the degree-one cohomology of `N ⊗_Λ M` is the
> degree-two cohomology of `K ⊗^𝐋_A M` for every `A`-module `M`.
>
> This is `Deformation.Artin.SectionsPerfectComplex.exists_finiteProjectiveModel_obstruction`
> without its binder `_haffineBase`, the affine-base case of [Stacks, Tag 02O5], which that proof
> never uses: [Stacks, Tag 07VL]
> (`Stacks.AlgebraicGeometry.ProperFlatGlobalSections.exists_finiteProjectiveModel_homology_iso`)
> is unconditional.

```lean
theorem exists_finiteProjectiveModel_homology_iso_obstruction {Λ : Type u} [CommRing Λ]
    {W : Scheme.{u}} (g : W ⟶ Spec (CommRingCat.of Λ)) (F : W.Modules)
    [IsNoetherianRing Λ] [IsProper g] [F.IsCoherent]
    (hflat : IsFlatOver g.toLRSHom.toShHom F) :
    ∃ (N : CochainComplex (ModuleCat.{u} Λ) ℤ) (a b : ℤ),
      N.IsStrictlyGE a ∧ N.IsStrictlyLE b ∧
        (∀ i : ℤ, Module.Finite Λ (N.X i)) ∧ (∀ i : ℤ, Module.Projective Λ (N.X i)) ∧
        (∀ {Λ' : Type u} [CommRing Λ'] (φ : Λ →+* Λ') {W' : Scheme.{u}}
          {g' : W' ⟶ Spec (.of Λ')} {p : W' ⟶ W}
          (_hsq : IsPullback p g' g (Spec.map (CommRingCat.ofHom φ))) (i : ℤ),
          Nonempty ((DerivedCategory.homologyFunctor (ModuleCat.{u} Λ') i).obj
              (derivedGlobalSectionsOverBase g' ((Scheme.Modules.pullback p).obj F)) ≅
            (extendScalarsComplex φ N).homology i)) ∧
        ∀ (A : Type u) [CommRing A] (φ : Λ →+* A) (M : ModuleCat.{u} A),
          Nonempty ((Deformation.Artin.derivedCohomology A
                (DerivedCategory.Q.obj
                  (Deformation.Artin.SectionsPerfectComplex.shiftedBaseChange φ N)) 2).obj M ≅
            ((tensorComplex M).obj (extendScalarsComplex φ N)).homology 1)
```

**`Deformation.Artin.SectionsPerfectComplex.nonempty_derivedCohomology_two_iso_homology_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/SectionsPerfectComplex.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/SectionsPerfectComplex.lean#L185). The attribute's comment: “the reformulation 𝒪(M) = H²(K ⊗^𝐋\_A M) with K = (N ⊗\_Λ A)[-1], from the description 𝒪(M) = H¹(N ⊗\_Λ M)”.

> **[Stacks, Tag 07YW], the degree shift.** With `K = (N ⊗_Λ A)[-1]` for a bounded above
> complex `N` of flat `Λ`-modules, the degree-one cohomology of `N ⊗_Λ M` — the obstruction module
> of [Stacks, Tag 07YH] in the form the source reaches through [Stacks, Tag 07VL] — is the
> degree-two cohomology of `K ⊗^𝐋_A M`:
>
> `H¹((N ⊗_Λ A) ⊗_A M) ≅ H²(K ⊗^𝐋_A M)`.
>
> In degree `i` the left-hand complex is `M ⊗_Λ Nⁱ` by `tensorComplexXLinearEquiv`, so the
> left-hand side is the source's `H¹(N ⊗_Λ M)`.

```lean
public theorem nonempty_derivedCohomology_two_iso_homology_one {Λ : Type u} [CommRing Λ]
    (φ : Λ →+* A) (N : CochainComplex (ModuleCat.{u} Λ) ℤ) (b : ℤ) [N.IsStrictlyLE b]
    (hN : ∀ i : ℤ, Module.Flat Λ (N.X i)) (M : ModuleCat.{u} A) :
    Nonempty ((Deformation.Artin.derivedCohomology A
          (DerivedCategory.Q.obj (shiftedBaseChange φ N)) 2).obj M ≅
      ((tensorComplex M).obj
        (Stacks.AlgebraicGeometry.ProperFlatGlobalSections.extendScalarsComplex φ N)).homology
          1)
```

## Tag 07YX, a situation

[Tag 07YX](https://stacks.math.columbia.edu/tag/07YX) in the Stacks Project.

**`Deformation.Artin.DualDeformationSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/DualSituation.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/DualSituation.lean#L167).

> **Stacks 07YX.** A dual deformation situation: a complex `K` of `A`-modules whose first
> derived-tensor cohomology is the tangent functor of `x`, together with obstruction elements
> in its second derived-tensor cohomology which are functorial in the deformation situation and
> vanish exactly when `x` lifts.

```lean
public structure DualDeformationSituation (A Λ : Type u) [CommRing A] [CommRing Λ]
    [Algebra Λ A] (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [IsLocallyNoetherian S] (toS : Spec (.of A) ⟶ S) (hA : B.Contains (Spec (.of A)))
    (X : Type v) [Category.{w} X] (p : X ⥤ BigFppfOver B S hS)
```

## Tag 07YY, a lemma

[Tag 07YY](https://stacks.math.columbia.edu/tag/07YY) in the Stacks Project.

**`Deformation.Artin.exists_obstructionEvaluation_eq_obstruction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/CotangentClass/ClauseOne.lean, line 550](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/CotangentClass/ClauseOne.lean#L550). The attribute's comment: “clause (1) alone, and WITHOUT the boundary condition (iv): a single class ξ on NL\_\{A/Λ} whose canonical evaluation `obstructionEvaluation` at every deformation situation is that situation's obstruction element. The whole tag — clause (1) together with clause (2), that ξ's image in H¹(K ⊗ᴸ Ω\_\{A/Λ}) is the canonical element of the tangent functor — is `Deformation.Artin.exists_isCotangentObstructionClass`, which assumes (iv) and whose conclusion is `Deformation.Artin.IsCotangentObstructionClass`, the full conjunction. This theorem is kept beside it because clause (1) needs no hypothesis: the class it produces is adjusted there by an element of H¹(K ⊗ᴸ Ω\_\{P/Λ} ⊗\_P A) to achieve clause (2), an adjustment clause (1) cannot see because `mor₁ ≫ mor₂ = 0`.”.

> There is a class `ξ` in `H¹(K ⊗ᴸ NL_{A/Λ})` such that every square-zero thickening
> `D : A' → A` of the situation `sit` admits a ring map `Λ → A'` compatible with `sit.affineOpen`
> and with `Λ → A`, along which the evaluation `obstructionEvaluation` of `ξ` is the obstruction
> element `sit.obstruction A' D`.

```lean
public theorem exists_obstructionEvaluation_eq_obstruction :
    ∃ ξ : (derivedTensorCohomology A sit.K 1).obj (derivedNaiveCotangentComplex Λ A),
      ∀ (A' : Type u) [CommRing A'] (D : SquareZeroThickening A B S hS toS hA A'),
        ∃ f : Λ →+* A',
          Spec.map (CommRingCat.ofHom f) ≫ sit.affineOpen = B.inclusion.map D.toS' ∧
          ∃ hf : D.q.comp f = algebraMap Λ A,
          letI : Algebra Λ A' := f.toAlgebra
          letI : Algebra A' A := D.q.toAlgebra
          letI : IsScalarTower Λ A' A :=
            IsScalarTower.of_algebraMap_eq fun r =>
              (congrArg (fun g : Λ →+* A => g r) hf).symm
          obstructionEvaluation Λ A' A sit.K D.squareZeroSurjection.1
              D.squareZeroSurjection.2 ξ = sit.obstruction A' D
```

**`Deformation.Artin.exists_isCotangentObstructionClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/CotangentClassCanonical/ObstructionClass.lean, line 692](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/CotangentClassCanonical/ObstructionClass.lean#L692).

> **Stacks 07YY.** A dual deformation situation satisfying the boundary condition (iv) has a
> cotangent obstruction class: a single class `ξ` on `NL_{A/Λ}` whose evaluation at every
> square-zero thickening is that thickening's obstruction element, and whose image in
> `H¹(K ⊗ᴸ Ω_{A/Λ})` is the canonical element of the tangent functor.
>
> The class of clause (1), built at a chosen presentation, need not satisfy clause (2); it is
> corrected by an element of `H¹(K ⊗ᴸ Ω_{P/Λ} ⊗_P A)` supplied by
> `Deformation.Artin.exists_correction_of_boundaryCondition`, and the correction is invisible to
> clause (1) because the inclusion of the degree-zero term of `NL(α)` followed by the projection
> onto the conormal module is zero.

```lean
public theorem exists_isCotangentObstructionClass
    (hiv : DualNotion.ObstructionBoundaryCondition Λ A B S hS toS hA X p sit) :
    ∃ ξ, IsCotangentObstructionClass Λ A B S hS toS hA X p sit ξ
```

## Tag 07YZ, a lemma

[Tag 07YZ](https://stacks.math.columbia.edu/tag/07YZ) in the Stacks Project.

**`Deformation.Artin.DualNotion.exists_isOpen_isVersalAt_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/DualNotionTag.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/DualNotionTag.lean#L156).

> **Stacks 07YZ.** In Situation 07YX assume that (iv) of Lemma 07YY holds and that `K` is a
> perfect object of `D(A)`. In this case, if `x` is versal at a closed point `u₀ ∈ U = Spec A`
> then there exists an open neighbourhood `u₀ ∈ U' ⊆ U` such that `x` is versal at every finite
> type point of `U'`.

```lean
public theorem exists_isOpen_isVersalAt_of_isPerfect
    (hboundary : ObstructionBoundaryCondition Λ A B S hS toS hA X p sit)
    (hperfect : StacksDraft.Perfect.IsPerfect sit.K)
    (u₀ : Spec (.of A)) (hu₀ : IsClosed ({u₀} : Set (Spec (.of A))))
    (hversal : IsVersalAt (Over.mk toS) (p ⋙ Over.post B.inclusion) u₀ sit.x
      (versalityBase Λ A B S hS toS hA X p sit)) :
    ∃ V : Set (Spec (.of A)), IsOpen V ∧ u₀ ∈ V ∧
      ∀ u ∈ V, IsFiniteTypePoint u →
        IsVersalAt (Over.mk toS) (p ⋙ Over.post B.inclusion) u sit.x
          (versalityBase Λ A B S hS toS hA X p sit)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.24, Tag 07YV](https://stacks.math.columbia.edu/tag/07YV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
