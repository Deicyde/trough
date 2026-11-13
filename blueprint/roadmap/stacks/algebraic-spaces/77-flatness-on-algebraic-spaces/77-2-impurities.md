---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.PrePureSituation, AlgebraicGeometry.Space.ImpurityDiagram, AlgebraicGeometry.Space.ImpurityDiagram.IsImpurity, AlgebraicGeometry.Space.AffineLimitSystem.exists_isImpurity_stageDiagram, AlgebraicGeometry.Space.exists_isImpurity_baseChange_etale_of_isFlatAt, AlgebraicGeometry.Space.exists_isImpurity_pointedBaseChange_of_isFlatAt, AlgebraicGeometry.Space.exists_isImpurity_isQuasiFiniteAt_of_exists_isImpurity_isEtale, AlgebraicGeometry.Space.hasImpurityOverStrictHenselization_iff_hasRelativeAssociatedPointAvoidingClosedFibre
statement: formalized
proof: formalized
---

# 77.2 Impurities

Section 77.2 of the Stacks Project, [Tag 0CV5](https://stacks.math.columbia.edu/tag/0CV5). 6 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CV6, a situation

[Tag 0CV6](https://stacks.math.columbia.edu/tag/0CV6) in the Stacks Project.

**`AlgebraicGeometry.Space.PrePureSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/Impurities.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/Impurities.lean#L112).

> **Stacks 0CV6.** The standing situation for impurities: a finite type, decent morphism
> `f : X ⟶ Y` of algebraic spaces over `S`, a finite type quasi-coherent module `F` on the
> source, and a point `y` of the target.

```lean
structure PrePureSituation (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
```

## Tag 0CV7, an equation

[Tag 0CV7](https://stacks.math.columbia.edu/tag/0CV7) in the Stacks Project.

**`AlgebraicGeometry.Space.ImpurityDiagram`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/Impurities.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/Impurities.lean#L145).

> **Stacks 0CV7.** The diagram from which an impurity is defined: a scheme `T` with a
> morphism `g : T ⟶ Y` to the target, a specialization `t' ⤳ t` in `T` whose specialized point
> lies over the chosen point `y`, and a point `ξ` of the base change `X_T = T ×_Y X` lying over
> the generalization `t'`.

```lean
structure ImpurityDiagram (P : PrePureSituation.{u, m} B S hS)
```

## Tag 0CV8, a definition

[Tag 0CV8](https://stacks.math.columbia.edu/tag/0CV8) in the Stacks Project.

**`AlgebraicGeometry.Space.ImpurityDiagram.IsImpurity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/Impurities.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/Impurities.lean#L250).

> **Stacks 0CV8.** The diagram defines an *impurity of `F` above `y`* when the distinguished
> point `ξ` of the base change `X_T` lies in the relative assassin `Ass_{X_T/T}(F_T)` and the
> point `t` of `T` does not lie in the image under `f_T` of the closure of `{ξ}`.

```lean
noncomputable def IsImpurity : Prop
```

## Tag 0CV9, a lemma

[Tag 0CV9](https://stacks.math.columbia.edu/tag/0CV9) in the Stacks Project.

**`AlgebraicGeometry.Space.AffineLimitSystem.exists_isImpurity_stageDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/ImpurityAffineLimitDescentGeneral.lean, line 843](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/ImpurityAffineLimitDescentGeneral.lean#L843). The attribute's comment: “for an arbitrary directed limit of affine schemes over the target; the source's `g : T → S` is read as `g : T → Y`, as Definition 0CV8 requires”.

> **Stacks 0CV9.** In Situation 0CV6, let `(g : T ⟶ Y, t' ⤳ t, ξ)` be an impurity of `ℱ`
> above `y` and let `T = lim_{i} Tᵢ` be a directed limit of affine schemes over `Y`. Then for
> some stage `i` the triple `(Tᵢ ⟶ Y, t'ᵢ ⤳ tᵢ, ξᵢ)` is an impurity of `ℱ` above `y`, where the
> three points are the images of `t'`, `t` and `ξ` under the canonical projections.
>
> No condition is put on the size of the system. The proof replaces it by a bounded one with the
> same limit, the closed subschemes `Zᵢ = Spec (image of Γ(Tᵢ) in Γ(T))` over a small directed set
> of indices (`AffineLimitSystem.shrunkPresentation`), applies the bounded form
> `AlgebraicGeometry.Space.AffineLimitPresentation.exists_isImpurity_stageDiagram`, and moves the
> impurity found at some `Zᵢ` up to `Tᵢ` along the closed immersion `Zᵢ ⟶ Tᵢ`
> (`ImpurityDiagram.isImpurity_push_of_isClosedImmersion`).

```lean
theorem exists_isImpurity_stageDiagram {P : PrePureSituation.{u, u} B S hS}
    {D : ImpurityDiagram P} (A : AffineLimitSystem D) (hD : D.IsImpurity) :
    ∃ i : A.J, (A.stageDiagram i).IsImpurity
```

## Tag 0CVA, a lemma

[Tag 0CVA](https://stacks.math.columbia.edu/tag/0CVA) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isImpurity_baseChange_etale_of_isFlatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/ImpurityFlatAscent.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/ImpurityFlatAscent.lean#L178).

> **Stacks 0CVA.** Let `(Y', y') ⟶ (Y, y)` be a morphism of pointed algebraic spaces over `S`
> with `Y' ⟶ Y` flat at `y'`. An impurity `(T ⟶ Y, t' ⤳ t, ξ)` of `F` above `y` gives an
> impurity `(T₁ ⟶ Y', t₁' ⤳ t₁, ξ₁)` of the pullback `F'` of `F` to `X' = Y' ×_Y X` above `y'`
> such that `T₁` is étale over `Y' ×_Y T`: the structure morphism `T₁ ⟶ Y'` is an étale morphism
> `T₁ ⟶ Y' ×_Y T` followed by the projection.

```lean
theorem exists_isImpurity_baseChange_etale_of_isFlatAt (P : PrePureSituation.{u, u} B S hS)
    (c : PointedOver P) (hflat : IsFlatAt B S hS c.g c.y')
    (D : ImpurityDiagram P) (hD : D.IsImpurity) :
    ∃ (E : ImpurityDiagram c.baseChange) (e : yoneda.obj E.T ⟶ pullback c.g D.g),
      IsEtale B S hS e ∧ e ≫ pullback.fst c.g D.g = E.g ∧ E.IsImpurity
```

**`AlgebraicGeometry.Space.exists_isImpurity_pointedBaseChange_of_isFlatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/ImpurityFlatAscent.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/ImpurityFlatAscent.lean#L192). The attribute's comment: “the field-valued representative that Stacks 05DC supplies always exists, by ImpurityDiagram.hasFibreWitnessAboveGeneralization”.

> **Stacks 0CVA**, the pointed base change form. The field-valued representative of
> Stacks 05DC needs no hypothesis, as it always exists, by
> `AlgebraicGeometry.Space.ImpurityDiagram.hasFibreWitnessAboveGeneralization`: the statement is
> `AlgebraicGeometry.Space.exists_isImpurity_baseChange_etale_of_isFlatAt`.

```lean
theorem exists_isImpurity_pointedBaseChange_of_isFlatAt (P : PrePureSituation.{u, u} B S hS)
    (c : PointedOver P) (hflat : IsFlatAt B S hS c.g c.y')
    (D : ImpurityDiagram P) (hD : D.IsImpurity) :
    ∃ (E : ImpurityDiagram c.baseChange) (e : yoneda.obj E.T ⟶ pullback c.g D.g),
      IsEtale B S hS e ∧ e ≫ pullback.fst c.g D.g = E.g ∧ E.IsImpurity
```

## Tag 0CVB, a lemma

[Tag 0CVB](https://stacks.math.columbia.edu/tag/0CVB) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isImpurity_isQuasiFiniteAt_of_exists_isImpurity_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/RelativelyPureModules.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/RelativelyPureModules.lean#L259). The attribute's comment: “condition (3) implies condition (4)”.

> **Stacks 0CVB, condition (3) implies condition (4).** An impurity of `F` above `y` whose
> structure morphism `T ⟶ Y` is étale, so that `(T, t) ⟶ (Y, y)` is an étale neighbourhood, is an
> impurity whose structure morphism is quasi-finite at `t`: an étale morphism of algebraic spaces
> is locally quasi-finite by Stacks 03XU.
>
> The implications (1) ⟹ (3) and (1) ⟹ (4) are
> `AlgebraicGeometry.Space.exists_isImpurity_isEtale_of_isImpurity_strictHenselization` and
> `AlgebraicGeometry.Space.exists_isImpurity_isQuasiFiniteAt_of_isImpurity_strictHenselization`.

```lean
theorem exists_isImpurity_isQuasiFiniteAt_of_exists_isImpurity_isEtale
    (P : PrePureSituation.{u, u} B S hS)
    (h : ∃ D : ImpurityDiagram P, IsEtale B S hS D.g ∧ D.IsImpurity) :
    ∃ D : ImpurityDiagram P, IsQuasiFiniteAt B S hS D.g D.t ∧ D.IsImpurity
```

**`AlgebraicGeometry.Space.hasImpurityOverStrictHenselization_iff_hasRelativeAssociatedPointAvoidingClosedFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/StrictHenselizationConditionsTwo.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/StrictHenselizationConditionsTwo.lean#L207). The attribute's comment: “(1) ⟺ (2), with (2) corrected as in `AlgebraicGeometry.Space.HasRelativeAssociatedPointAvoidingClosedFibre`”.

> **Stacks 0CVB, (1) ⟺ (2).** For a geometric point `ȳ` of `Y` lying over `y`, there is an
> impurity of `ℱ` above `y` over the strict henselization `Y^{sh}` exactly when some point of the
> relative assassin of `ℱ^{sh}` does not specialize to a point of the closed fibre.

```lean
theorem hasImpurityOverStrictHenselization_iff_hasRelativeAssociatedPointAvoidingClosedFibre
    (hybar : ybar.LiesOver P.y) :
    HasImpurityOverStrictHenselization P ybar ↔
      HasRelativeAssociatedPointAvoidingClosedFibre P ybar
```

**`AlgebraicGeometry.Space.tfae_hasImpurityOverStrictHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/StrictHenselizationTFAE.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/StrictHenselizationTFAE.lean#L46). The attribute's comment: “condition (2) in the corrected reading recorded in the note of StrictHenselizationConditions: some associated point does not specialize into the closed fibre”.

> **Stacks 0CVB.** In Situation 0CV6, for a geometric point `ȳ` of `Y` lying over `y`, the four
> conditions of the source are equivalent: an impurity of `ℱ` above `y` over `Y^{sh}` with
> specialized point `ȳ`; a point of `Ass_{X^{sh}/Y^{sh}}(ℱ^{sh})` not specializing into the closed
> fibre; an impurity over an étale neighbourhood of `y`; an impurity whose structure morphism is
> quasi-finite at its specialized point.

```lean
theorem tfae_hasImpurityOverStrictHenselization (P : PrePureSituation.{u, u} B S hS)
    (ybar : GeometricPoint B S hS P.Y) (hybar : ybar.LiesOver P.y) :
    [HasImpurityOverStrictHenselization P ybar,
      HasRelativeAssociatedPointAvoidingClosedFibre P ybar,
      HasImpurityOverEtaleNeighborhood P,
      HasImpurityQuasiFiniteAtPoint P].TFAE
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 77.2, Tag 0CV5](https://stacks.math.columbia.edu/tag/0CV5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
