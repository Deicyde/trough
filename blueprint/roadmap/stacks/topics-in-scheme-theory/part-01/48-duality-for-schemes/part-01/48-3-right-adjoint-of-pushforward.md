---
declaration: section
origin: cited
lean: Stacks.Duality.DerivedPushforward.isLeftAdjoint_qcqsRestrictedDerivedPushforward_of_qcqs, AlgebraicGeometry.exists_adj_derivedQuasicoherentPushforward_isoDerivedHom, AlgebraicGeometry.polynomialRightAdjoint_homologyZero_not_isCoherent, AlgebraicGeometry.dualNumberRightAdjoint_not_minus, AlgebraicGeometry.dualNumberRightAdjoint_not_preserves_minus, Stacks.Duality.isBoundedBelow_twistedInverseImage_obj_and_exists_bound, Stacks.Duality.qcqsSheafyTrace, Stacks.Duality.isIso_coherator_map_sheafyTrace_of_qcqs
statement: formalized
proof: formalized
---

# 48.3 Right adjoint of pushforward

Section 48.3 of the Stacks Project, [Tag 0A9D](https://stacks.math.columbia.edu/tag/0A9D). 12 tags here are carried by 22 declarations of the repository (all in StacksFrontier) and 16 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A9D, the section

[Tag 0A9D](https://stacks.math.columbia.edu/tag/0A9D) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.Duality.DerivedPushforward.isLeftAdjoint_qcqsRestrictedDerivedPushforward_of_qcqs`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QcqsCompactGeneration.lean#L991), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean#L99) (StacksFrontier): “section tag; 0A9E (Lemma 48.3.1), Rf\_* has a right adjoint for qcqs schemes”.
- [`AlgebraicGeometry.exists_adj_derivedQuasicoherentPushforward_isoDerivedHom`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/AffineRightAdjointDerivedHom.lean#L426), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean#L101) (StacksFrontier): “section tag; 0A9F (Example 48.3.2), the affine case: Rf\_* is restriction of scalars and the adjoint is R Hom\_A(B, -)”.
- [`AlgebraicGeometry.polynomialRightAdjoint_homologyZero_not_isCoherent`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/CoherentCohomologySheaves.lean#L264), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean#L104) (StacksFrontier): “section tag; 0A9G (Example 48.3.3), the adjoint of the affine line does not preserve coherence”.
- [`AlgebraicGeometry.dualNumberRightAdjoint_not_minus`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/DualNumbersNotBoundedAbove.lean#L434), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean#L107) (StacksFrontier): “section tag; 0A9H (Example 48.3.4), the dual numbers: a(O\_Y) is unbounded above”.
- [`AlgebraicGeometry.dualNumberRightAdjoint_not_preserves_minus`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/DualNumbersNotBoundedAbove.lean#L480), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean#L110) (StacksFrontier): “section tag; 0A9H (Example 48.3.4), so the adjoint does not preserve D-minus-QCoh even for a finite morphism”.
- [`Stacks.Duality.isBoundedBelow_twistedInverseImage_obj_and_exists_bound`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BoundedBelow.lean#L93), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean#L113) (StacksFrontier): “section tag; 0A9I (Lemma 48.3.5), the adjoint preserves D-plus-QCoh, with the shift bound N”.
- [`Stacks.Duality.qcqsSheafyTrace`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceQcqs.lean#L79), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean#L116) (StacksFrontier): “section tag; 0B6H (Equation 48.3.5.1), the sheafy trace map”.
- [`Stacks.Duality.isIso_coherator_map_sheafyTrace_of_qcqs`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceCoheratorQCQS.lean#L210), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean#L118) (StacksFrontier): “section tag; 0A9Q (Lemma 48.3.6), the trace map is an isomorphism after the coherator DQ\_Y”.
- [`Stacks.Duality.AffineLine.uncoheratedTrace_example`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/AffineLineUncoheratedTrace.lean#L316), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean#L121) (StacksFrontier): “section tag; 0GEU (Example 48.3.7), the coherator cannot be dropped: the right-hand side is a product of copies of O\_Y”.
- [`Stacks.Duality.AffineLine.uncoheratedTrace_example_int`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/AffineLineUncoheratedTrace.lean#L341), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean#L124) (StacksFrontier): “section tag; 0GEU (Example 48.3.7), the witness over Z for which the product really fails to be quasi-coherent”.
- [`Stacks.Duality.isIso_coherator_homEquiv_sheafyTrace_of_qcqs`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceCoheratorErasure.lean#L68), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean#L127) (StacksFrontier): “section tag; 0GEV (Remark 48.3.8), erasing the coherator on the left of the arrow, where RHom(L, a(K)) is quasi-coherent”.
- [`Stacks.Duality.isIso_coherator_counit_comp_sheafyTrace_of_qcqs`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceCoheratorErasure.lean#L96), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean#L130) (StacksFrontier): “section tag; 0GEV (Remark 48.3.8), erasing the coherator on the right of the arrow, where RHom(Rf\_*L, K) is quasi-coherent”.
- [`Stacks.Duality.isIso_sheafyTrace_of_derivedCategoryB_of_qcqs`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceCoheratorErasure.lean#L123), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean#L133) (StacksFrontier): “section tag; 0GEV (Remark 48.3.8), both erasures at once: the map of Equation 48.3.5.1 is an isomorphism”.
- [`Stacks.Duality.sheafyTrace_quasiCoherent_criteria`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceQuasiCoherentCriterionUnconditional.lean#L102), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean#L136) (StacksFrontier): “section tag; 0GEV (Remark 48.3.8), the appeal to Tag 0CR1 and the two criteria: clause (1), L and Rf\_*L perfect, and clause (2), K bounded below and L, Rf\_*L pseudo-coherent”.
- [`Stacks.Duality.isIso_sheafyTrace_of_isProper_of_derivedCategoryBMinus`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceProperIso.lean#L141), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean#L140) (StacksFrontier): “section tag; 0GEW (Example 48.3.9), f proper between Noetherian schemes”.
- [`Stacks.Duality.bijective_comp_sheafyTrace_structureSheaf_of_qcqs`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceGlobalHomQcqs.lean#L254), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointOfPushforwardSection.lean#L142) (StacksFrontier): “section tag; 0B6I (Lemma 48.3.10), the isomorphism of global derived homs”.

## Tag 0A9E, a lemma

[Tag 0A9E](https://stacks.math.columbia.edu/tag/0A9E) in the Stacks Project.

**`AlgebraicGeometry.isLeftAdjoint_qcqsQuasiCoherentDerivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineOpensChaoticQuasicoherentEquality.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineOpensChaoticQuasicoherentEquality.lean#L248). The attribute's comment: “for a quasi-compact quasi-separated morphism with quasi-compact target”.

> **[Stacks, Tag 0A9E].** Let `f : X ⟶ Y` be a quasi-compact quasi-separated morphism of
> schemes with `Y` quasi-compact. Then `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` has a right adjoint, the
> twisted inverse image `f^×`.
>
> The source assumes `X` and `Y` quasi-compact and quasi-separated, which gives these hypotheses:
> `Y` is quasi-compact; `f` is quasi-compact because `X` is and `Y` is quasi-separated; and `f` is
> quasi-separated because `X` is.
>
> The generating family of [Stacks, Tag 0GYG] is
> `AlgebraicGeometry.exists_generating_family_quasiCoherentDerivedCategory`, and
> `Stacks.Duality.DerivedPushforward.isLeftAdjoint_qcqsQuasiCoherentDerivedPushforward_of_generating`
> supplies the rest of the source's argument: part (1) of [Stacks, Tag 08D5], that `Rf_*` preserves
> quasi-coherence of cohomology, and [Stacks, Tag 08DZ], that the restricted functor commutes with
> direct sums.

```lean
theorem isLeftAdjoint_qcqsQuasiCoherentDerivedPushforward {X Y : Scheme.{u}} (f : X ⟶ Y)
    [QuasiCompact f] [QuasiSeparated f] [CompactSpace Y] :
    (Stacks.Duality.quasiCoherentDerivedPushforward f
      (Stacks.Duality.isQuasicoherent_homology_derivedPushforward_of_qcqs f)).IsLeftAdjoint
```

**`Stacks.Duality.AnyModel.isLeftAdjoint_restrictedDerivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/AnyModelRightAdjoint/QcqsRightAdjointAnyModel.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/AnyModelRightAdjoint/QcqsRightAdjointAnyModel.lean#L302). The attribute's comment: “at an arbitrary chosen model of the two derived categories, the Brown representability argument of the source being available only at a locally small one”.

> **[Stacks, Tag 0A9E] at an arbitrary chosen model of the two derived categories.** Let
> `f : X ⟶ Y` be a morphism between quasi-compact and quasi-separated schemes. Then
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` has a right adjoint — the twisted inverse image `f^×` — at
> every chosen model of `D(𝒪_X)` and `D(𝒪_Y)`, and not only at the locally small model at which the
> Brown representability argument of the source can be run.
>
> The functor is the canonical `Stacks.Duality.AnyModel.restrictedDerivedPushforward`: that `Rf_*`
> carries `D_QCoh(𝒪_X)` into `D_QCoh(𝒪_Y)` at all is part (1) of [Stacks, Tag 08D5] and is
> discharged, at any model.

```lean
theorem isLeftAdjoint_restrictedDerivedPushforward (hX : HasDerivedCategory.{w} X.Modules)
    (hY : HasDerivedCategory.{w} Y.Modules) :
    (restrictedDerivedPushforward f hX hY).IsLeftAdjoint
```

**`Stacks.Duality.DerivedPushforward.isLeftAdjoint_qcqsRestrictedDerivedPushforward_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QcqsCompactGeneration.lean, line 991](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QcqsCompactGeneration.lean#L991).

> **Stacks Project, Tag 0A9E.** Let `f : X ⟶ Y` be a morphism between quasi-compact and
> quasi-separated schemes. The functor `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` has a right adjoint.
>
> The proof is the source's: Brown representability ([Stacks, Tag 0A8G]) applies because
> `D_QCoh(𝒪_X)` has direct sums ([Stacks, Tag 08DT]) and is compactly generated
> ([Stacks, Tag 09IS],
> `Stacks.Duality.QcqsGeneration.isCompactlyGenerated_quasiCoherentDerivedCategory`), and because
> `f`, a morphism between quasi-compact quasi-separated schemes, is quasi-compact and
> quasi-separated, so that `Rf_*` carries `D_QCoh(𝒪_X)` into `D_QCoh(𝒪_Y)` ([Stacks, Tag 08D5])
> and commutes with direct sums ([Stacks, Tag 08DZ]); those two facts about `f` are found by
> instance search (`AlgebraicGeometry.quasiCompact_of_compactSpace`,
> `AlgebraicGeometry.QuasiSeparated.of_quasiSeparatedSpace`).
>
> The derived categories are the locally small models
> `AlgebraicGeometry.Scheme.Modules.hasDerivedCategory`, whose morphisms live in the universe `u`
> of the schemes. This is the only model at which the statement has content: Brown representability
> asks for direct sums indexed by the morphism universe, and at
> `CategoryTheory.HasDerivedCategory.standard`, whose morphisms live in `Type (u + 1)`, those direct
> sums do not exist in the category of `𝒪_X`-modules. The functor is the canonical
> `Stacks.Duality.DerivedPushforward.qcqsRestrictedDerivedPushforward`.

```lean
theorem isLeftAdjoint_qcqsRestrictedDerivedPushforward_of_qcqs :
    (qcqsRestrictedDerivedPushforward f).IsLeftAdjoint
```

**`Stacks.Duality.DerivedPushforward.exists_isTriangulated_rightAdjoint_qcqsRestrictedDerivedPushforward_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QcqsCompactGeneration.lean, line 1013](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/QcqsCompactGeneration.lean#L1013). The attribute's comment: “the adjoint is exact”.

> **Stacks Project, Tag 0A9E, with the adjoint exhibited as exact.** For a morphism
> `f : X ⟶ Y` between quasi-compact and quasi-separated schemes there is a functor
> `a : D_QCoh(𝒪_Y) ⥤ D_QCoh(𝒪_X)`, an adjunction `Rf_* ⊣ a`, and a shift structure on `a` for which
> the adjunction is triangulated: Brown representability returns the right adjoint as an exact
> functor.

```lean
theorem exists_isTriangulated_rightAdjoint_qcqsRestrictedDerivedPushforward_of_qcqs :
    ∃ (a : _) (adj : qcqsRestrictedDerivedPushforward f ⊣ a) (_ : a.CommShift ℤ),
      adj.IsTriangulated
```

## Tag 0A9F, an example

[Tag 0A9F](https://stacks.math.columbia.edu/tag/0A9F) in the Stacks Project.

**`AlgebraicGeometry.derivedTilde_comp_rightAdjoint_derivedQuasicoherentPushforwardIsoDerivedHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/AffineRightAdjointDerivedHom.lean, line 344](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/AffineRightAdjointDerivedHom.lean#L344). The attribute's comment: “the right adjoint is derived Hom; the general form, which takes the adjunction adjP for an arbitrary right adjoint a of Rf\_* as data. THAT DATA IS NOT HYPOTHETICAL: it is constructed by AlgebraicGeometry.derivedQuasicoherentPushforward\_adj\_affineTwistedInverseImage below, at the functor AlgebraicGeometry.affineTwistedInverseImage, by conjugating the adjunction of Tag 0A70 (Dualizing.AnyModel.restrictScalarsDerived\_adj\_derivedHom) along the derived sheafification equivalences of Tag 06Z0; the two combine into AlgebraicGeometry.exists\_adj\_derivedQuasicoherentPushforward\_isoDerivedHom below, which assumes nothing beyond the ring map. This form is kept because quantifying over an arbitrary right adjoint says more, a right adjoint being unique up to canonical isomorphism”.

> **Stacks 0A9F.** Let `φ : R ⟶ S` be a homomorphism of commutative rings, `Y = Spec R`,
> `X = Spec S` and `f = Spec φ : X ⟶ Y`. Let `a` be a right adjoint of
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`. Then `a` corresponds to `RHom_R(S, -)` under derived
> sheafification.
>
> This is the second assertion of [Stacks, Tag 0A9F]; the first — that `Rf_*` corresponds to
> restriction of scalars — is
> `AlgebraicGeometry.derivedTildeCompDerivedQuasicoherentPushforwardIso`, which is also
> [Stacks, Tag 0DJK] and is what discharges the hypothesis `hP` of
> `AlgebraicGeometry.derivedTilde_comp_rightAdjointIsoDerivedHom` here. The other two hypotheses of
> that statement, that the comparison functor of [Stacks, Tag 06VT] is an equivalence on the two
> affine schemes, are `Stacks.DerivedQCoh.derivedQuasicoherentComparison_isEquivalence`.
>
> `a` is arbitrary, so this says more than the corresponding statement about the particular right
> adjoint `AlgebraicGeometry.affineTwistedInverseImage` constructed below; its existence is
> `AlgebraicGeometry.derivedQuasicoherentPushforward_adj_affineTwistedInverseImage`, and
> `AlgebraicGeometry.exists_adj_derivedQuasicoherentPushforward_isoDerivedHom` combines the two into
> the tag with no hypothesis. The adjunction `adjP` is therefore **not** hypothetical: it is
> constructed, and this statement is kept in the general form only because quantifying over `a`
> says more.

```lean
theorem derivedTilde_comp_rightAdjoint_derivedQuasicoherentPushforwardIsoDerivedHom
    {R S : CommRingCat.{u}} (φ : R ⟶ S)
    {a : (DerivedCategoryB.derivedCategoryB (A := (Spec R).Modules)
        (SheafOfModules.isQuasicoherent (Spec R).ringCatSheaf)).FullSubcategory ⥤
      (DerivedCategoryB.derivedCategoryB (A := (Spec S).Modules)
        (SheafOfModules.isQuasicoherent (Spec S).ringCatSheaf)).FullSubcategory}
    (adjP : derivedQuasicoherentPushforward (Spec.map φ) ⊣ a) :
    Nonempty (derivedTilde R ⋙ a ≅
      Dualizing.AnyModel.derivedHom.{u, u, u, u, u} φ.hom ⋙ derivedTilde S)
```

**`AlgebraicGeometry.derivedQuasicoherentPushforward_adj_affineTwistedInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/AffineRightAdjointDerivedHom.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/AffineRightAdjointDerivedHom.lean#L390). The attribute's comment: “the right adjoint exists, affine case”.

> **Stacks 0A9F, the existence of the right adjoint in the affine case.** Let `φ : R ⟶ S` be a
> homomorphism of commutative rings and `f = Spec φ`. Then
> `Rf_* : D_QCoh(𝒪_{Spec S}) ⥤ D_QCoh(𝒪_{Spec R})` *has* a right adjoint, namely
> `AlgebraicGeometry.affineTwistedInverseImage φ`.
>
> No hypothesis is assumed: the source cites [Stacks, Tag 0A9E] for existence, whose proof goes
> through Brown representability and compact generation of `D_QCoh` ([Stacks, Tag 09IS]), but over
> an affine base the adjoint can be produced directly. Derived sheafification is an equivalence on
> either side ([Stacks, Tag 06Z0], `AlgebraicGeometry.derivedTilde_isEquivalence`) and carries
> derived restriction of scalars to `Rf_*` ([Stacks, Tag 0DJK],
> `AlgebraicGeometry.derivedTildeCompDerivedQuasicoherentPushforwardIso`), so `Rf_*` is conjugate to
> a functor which already has a right adjoint, `RHom_R(S, -)` ([Stacks, Tag 0A70],
> `Dualizing.AnyModel.restrictScalarsDerived_adj_derivedHom`); the conjugate of that right adjoint
> is a right adjoint of `Rf_*`, which is
> `CategoryTheory.Adjunction.ofSquare`.

```lean
theorem derivedQuasicoherentPushforward_adj_affineTwistedInverseImage
    {R S : CommRingCat.{u}} (φ : R ⟶ S) :
    Nonempty (derivedQuasicoherentPushforward (Spec.map φ) ⊣ affineTwistedInverseImage φ)
```

**`AlgebraicGeometry.exists_adj_derivedQuasicoherentPushforward_isoDerivedHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/AffineRightAdjointDerivedHom.lean, line 426](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/AffineRightAdjointDerivedHom.lean#L426). The attribute's comment: “existence and identification of the right adjoint, affine case”.

> **Stacks 0A9F in full, with nothing assumed.** Let `φ : R ⟶ S` be a homomorphism of
> commutative rings, `Y = Spec R`, `X = Spec S` and `f = Spec φ : X ⟶ Y`. Then
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` has a right adjoint `a`, and `a` corresponds to `RHom_R(S, -)`
> under derived sheafification.
>
> This packages the two halves of the tag that the declarations above prove separately — existence,
> `AlgebraicGeometry.derivedQuasicoherentPushforward_adj_affineTwistedInverseImage`, and the
> identification, `AlgebraicGeometry.derivedTilde_comp_affineTwistedInverseImageIsoDerivedHom` —
> into the single unconditional statement. The first assertion of the tag, that `Rf_*` itself is
> derived restriction of scalars, is
> `AlgebraicGeometry.derivedTildeCompDerivedQuasicoherentPushforwardIso`, which is also
> [Stacks, Tag 0DJK].

```lean
theorem exists_adj_derivedQuasicoherentPushforward_isoDerivedHom
    {R S : CommRingCat.{u}} (φ : R ⟶ S) :
    ∃ a : (DerivedCategoryB.derivedCategoryB (A := (Spec R).Modules)
          (SheafOfModules.isQuasicoherent (Spec R).ringCatSheaf)).FullSubcategory ⥤
        (DerivedCategoryB.derivedCategoryB (A := (Spec S).Modules)
          (SheafOfModules.isQuasicoherent (Spec S).ringCatSheaf)).FullSubcategory,
      Nonempty (derivedQuasicoherentPushforward (Spec.map φ) ⊣ a) ∧
        Nonempty (derivedTilde R ⋙ a ≅
          Dualizing.AnyModel.derivedHom.{u, u, u, u, u} φ.hom ⋙ derivedTilde S)
```

**`AlgebraicGeometry.derivedTildeCompDerivedQuasicoherentPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/AffineDerivedPushforward.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/AffineDerivedPushforward.lean#L424). The attribute's comment: “Rf\_* is derived restriction of scalars”.

> **Stacks 0DJK.** Let `φ : R ⟶ S` and let `f = Spec φ : Spec S ⟶ Spec R`. Then the square
> `D(S) ⟶ D_QCoh(𝒪_{Spec S}) ⟶^{Rf_*} D_QCoh(𝒪_{Spec R})`,
> `D(S) ⟶^{restriction of scalars} D(R) ⟶ D_QCoh(𝒪_{Spec R})`
> commutes: derived direct image along a morphism of affine schemes corresponds, under derived
> sheafification, to derived restriction of scalars.
>
> This is `AlgebraicGeometry.derivedTildeCompIso_of_comparisonSquare` with its hypothesis `hsq`
> discharged by `AlgebraicGeometry.derivedQuasicoherentComparisonSquare`, the commuting square of
> [Stacks, Tag 08D7]. It is also the first assertion of [Stacks, Tag 0A9F].

```lean
public def derivedTildeCompDerivedQuasicoherentPushforwardIso :
    derivedTilde S ⋙ derivedQuasicoherentPushforward (Spec.map φ) ≅
      (ModuleCat.restrictScalars φ.hom).mapDerivedCategory ⋙ derivedTilde R
```

## Tag 0A9G, an example

[Tag 0A9G](https://stacks.math.columbia.edu/tag/0A9G) in the Stacks Project.

**`AlgebraicGeometry.polynomialRightAdjoint_homologyZero_not_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/CoherentCohomologySheaves.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/CoherentCohomologySheaves.lean#L264).

> **Stacks Project, Tag 0A9G.** Let `k` be a field and `f : 𝔸¹_k ⟶ Spec k` the structure
> morphism of the affine line, which is a separated morphism of finite type between Noetherian
> schemes (`AlgebraicGeometry.affineLine_isSeparated`,
> `AlgebraicGeometry.affineLine_locallyOfFiniteType`, `AlgebraicGeometry.affineLine_quasiCompact`,
> `AlgebraicGeometry.affineLine_isLocallyNoetherian` and
> `AlgebraicGeometry.isLocallyNoetherian_Spec_of_field`). Let `a` be a right adjoint of
> `Rf_* : D_QCoh(𝒪_{𝔸¹_k}) ⥤ D_QCoh(𝒪_{Spec k})`. Then the degree-zero cohomology sheaf of
> `a(𝒪_{Spec k})` is not coherent, so `a` does not carry `D_Coh(𝒪_{Spec k})` into
> `D_Coh(𝒪_{𝔸¹_k})`.
>
> The input is coherent: it is `𝒪_{Spec k}` in degree zero by
> `AlgebraicGeometry.homologyZeroDerivedTildeSelfIso`, and lies in `D_Coh` by
> `AlgebraicGeometry.isCoherent_homologyDerivedTildeSingle`. By [Stacks, Tag 0A9F] the output is
> `RHom_k(k[X], k)^~`, whose degree-zero cohomology module is the linear dual `Hom_k(k[X], k)`; that
> module is the product of countably many copies of `k`, and multiplication by `X` on it is a
> surjective endomorphism with nonzero kernel, so it is not finite over the Noetherian ring `k[X]`
> (`Dualizing.AnyModel.polynomialDerivedHom_not_finite`, resting on
> `Dualizing.polynomialDerivedHom_not_finite`). The passage from that to non-coherence of the sheaf
> is `AlgebraicGeometry.finite_of_isFiniteType_homologyDerivedTilde`.
>
> The existence of `a` is not asserted, exactly as the source does not assert it: it comes from
> [Stacks, Tag 0A9E] and enters as the hypothesis `adjP`.

```lean
theorem polynomialRightAdjoint_homologyZero_not_isCoherent (k : Type u) [Field k]
    {a : (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent (Spec (CommRingCat.of k)).ringCatSheaf)).FullSubcategory ⥤
      (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent
          (Spec (CommRingCat.of (Polynomial k))).ringCatSheaf)).FullSubcategory}
    (adjP : derivedQuasicoherentPushforward (Spec.map
      (CommRingCat.ofHom (Polynomial.C : k →+* Polynomial k))) ⊣ a) :
    ¬ ((DerivedCategory.homologyFunctor
          (Spec (CommRingCat.of (Polynomial k))).Modules 0).obj
        ((DerivedCategoryB.derivedCategoryB
          (SheafOfModules.isQuasicoherent
            (Spec (CommRingCat.of (Polynomial k))).ringCatSheaf)).ι.obj
          (a.obj ((derivedTilde (CommRingCat.of k)).obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} k) 0).obj
              (ModuleCat.of k k)))))).IsCoherent
```

## Tag 0A9H, an example

[Tag 0A9H](https://stacks.math.columbia.edu/tag/0A9H) in the Stacks Project.

**`AlgebraicGeometry.dualNumberRightAdjoint_not_minus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/DualNumbersNotBoundedAbove.lean, line 434](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/DualNumbersNotBoundedAbove.lean#L434).

> **Stacks Project, Tag 0A9H.** Let `k` be a field, `Y = Spec(k[ε])` the spectrum of the dual
> numbers, `X = Spec(k)` and `f : X ⟶ Y` the closed immersion of the closed point, a finite
> morphism of Noetherian schemes (`AlgebraicGeometry.dualNumberSpecMap_isFinite`,
> `AlgebraicGeometry.isLocallyNoetherian_Spec_dualNumber`,
> `AlgebraicGeometry.isLocallyNoetherian_Spec_of_field`). Let `a` be a right adjoint of
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`. Then the image under `a` of the sheafification of the residue
> field `k[ε]/(ε)` in degree zero is not bounded above. That object is itself bounded above
> (`AlgebraicGeometry.minus_derivedTildeSingle`), so `a` does not map `D^-_QCoh(𝒪_Y)` into
> `D^-_QCoh(𝒪_X)`, which is
> `AlgebraicGeometry.dualNumberRightAdjoint_not_preserves_minus`.
>
> By [Stacks, Tag 0A9F] that image is `RHom_{k[ε]}(k, k[ε]/(ε))^~`, which is unbounded above
> because `Ext^i_{k[ε]}(k, k)` is nonzero for every `i ≥ 0`
> (`Dualizing.dualNumberDerivedHom_not_minus`, resting on
> `Dualizing.dualNumberResidue_zExt_nontrivial`); sheafification reflects the vanishing of a
> cohomology module, being faithful. The existence of `a` is not asserted: it comes from
> [Stacks, Tag 0A9E] and enters as the hypothesis `adjP`.

```lean
theorem dualNumberRightAdjoint_not_minus (k : Type u) [Field k]
    {a : (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent
          (Spec (CommRingCat.of (DualNumber k))).ringCatSheaf)).FullSubcategory ⥤
      (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent (Spec (CommRingCat.of k)).ringCatSheaf)).FullSubcategory}
    (adjP : derivedQuasicoherentPushforward
      (Spec.map (CommRingCat.ofHom (Dualizing.dualNumberFst k))) ⊣ a) :
    ¬ (DerivedCategory.TStructure.t (C := (Spec (CommRingCat.of k)).Modules)).minus
      ((DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent (Spec (CommRingCat.of k)).ringCatSheaf)).ι.obj
          (a.obj ((derivedTilde (CommRingCat.of (DualNumber k))).obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} (DualNumber k)) 0).obj
              (Dualizing.dualNumberResidue k)))))
```

**`AlgebraicGeometry.dualNumberRightAdjoint_not_preserves_minus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/DualNumbersNotBoundedAbove.lean, line 480](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/DualNumbersNotBoundedAbove.lean#L480).

> **Stacks Project, Tag 0A9H.** For `f : Spec(k) ⟶ Spec(k[ε])` the closed immersion of the
> closed point of the spectrum of the dual numbers over a field, a finite morphism of Noetherian
> schemes, a right adjoint `a` of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` does not map
> `D^-_QCoh(𝒪_Y)` into `D^-_QCoh(𝒪_X)`.
>
> The residue field `k[ε]/(ε)`, in degree zero and sheafified, is a bounded-above object
> (`AlgebraicGeometry.minus_derivedTildeSingle`) whose image under `a` is not
> (`AlgebraicGeometry.dualNumberRightAdjoint_not_minus`).

```lean
theorem dualNumberRightAdjoint_not_preserves_minus (k : Type u) [Field k]
    {a : (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent
          (Spec (CommRingCat.of (DualNumber k))).ringCatSheaf)).FullSubcategory ⥤
      (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent (Spec (CommRingCat.of k)).ringCatSheaf)).FullSubcategory}
    (adjP : derivedQuasicoherentPushforward
      (Spec.map (CommRingCat.ofHom (Dualizing.dualNumberFst k))) ⊣ a) :
    ¬ ∀ K : (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent
          (Spec (CommRingCat.of (DualNumber k))).ringCatSheaf)).FullSubcategory,
      (DerivedCategory.TStructure.t
          (C := (Spec (CommRingCat.of (DualNumber k))).Modules)).minus
        ((DerivedCategoryB.derivedCategoryB
          (SheafOfModules.isQuasicoherent
            (Spec (CommRingCat.of (DualNumber k))).ringCatSheaf)).ι.obj K) →
        (DerivedCategory.TStructure.t (C := (Spec (CommRingCat.of k)).Modules)).minus
          ((DerivedCategoryB.derivedCategoryB
            (SheafOfModules.isQuasicoherent
              (Spec (CommRingCat.of k)).ringCatSheaf)).ι.obj (a.obj K))
```

## Tag 0A9I, a lemma

[Tag 0A9I](https://stacks.math.columbia.edu/tag/0A9I) in the Stacks Project.

**`Stacks.Duality.isBoundedBelow_twistedInverseImage_obj_and_exists_bound`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BoundedBelow.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BoundedBelow.lean#L93).

> **[Stacks, Tag 0A9I].** Let `f : X ⟶ Y` be a morphism of quasi-compact and quasi-separated
> schemes and let `a = f^× : D_QCoh(𝒪_Y) ⥤ D_QCoh(𝒪_X)` be the right adjoint of `Rf_*` of
> [Stacks, Tag 0A9E]. Then `a` maps `D^+_QCoh(𝒪_Y)` into `D^+_QCoh(𝒪_X)`. In fact, there exists an
> integer `N` such that `H^i(K) = 0` for `i ≤ c` implies `H^i(a(K)) = 0` for `i ≤ c - N`.

```lean
theorem isBoundedBelow_twistedInverseImage_obj_and_exists_bound :
    (∀ K : quasiCoherentDerivedCategory Y, DerivedCategoryB.IsBoundedBelow K.obj →
      DerivedCategoryB.IsBoundedBelow
        ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
          K).obj) ∧
    ∃ N : ℤ, ∀ (K : quasiCoherentDerivedCategory Y) (c : ℤ),
      (∀ i ≤ c, IsZero ((DerivedCategory.homologyFunctor Y.Modules i).obj K.obj)) →
      ∀ i ≤ c - N, IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj
        ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
          K).obj)
```

## Tag 0B6H, an equation

[Tag 0B6H](https://stacks.math.columbia.edu/tag/0B6H) in the Stacks Project.

**`Stacks.Duality.sheafyTrace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/SheafyTrace.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTrace.lean#L142). The attribute's comment: “variant: the map for a supplied right adjoint `a`, adjunction `Rf_* ⊣ a` and tensor–Hom data; the tag is Stacks.Duality.qcqsSheafyTrace”.

> **Equation 48.3.0.1 of [Stacks, Tag 0B6H].** For a morphism of schemes `f : X ⟶ Y`, a right
> adjoint `a` of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`, and objects `L` of `D_QCoh(𝒪_X)` and `K` of
> `D_QCoh(𝒪_Y)`, the canonical map `Rf_*R𝓗om_{𝒪_X}(L, a(K)) ⟶ R𝓗om_{𝒪_Y}(Rf_*L, K)`: the map of
> [Stacks, Tag 0B69] at `L` and `a(K)`, followed by `R𝓗om_{𝒪_Y}(Rf_*L, −)` applied to the counit
> `Rf_*a(K) ⟶ K` of `Rf_* ⊣ a`.

```lean
def sheafyTrace (L : quasiCoherentDerivedCategory X) (K : quasiCoherentDerivedCategory Y) :
    (derivedPushforward f).obj
        (((Stacks.SheafOfModules.derivedSheafHom X.sheaf).obj (op L.obj)).obj
          (a.obj K).obj) ⟶
      ((Stacks.SheafOfModules.derivedSheafHom Y.sheaf).obj
          (op ((derivedPushforward f).obj L.obj))).obj K.obj
```

**`Stacks.Duality.qcqsSheafyTrace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceQcqs.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceQcqs.lean#L79).

> **Equation 48.3.0.1 of [Stacks, Tag 0B6H].** Let `f : X ⟶ Y` be a morphism of quasi-compact
> and quasi-separated schemes and `a` the right adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` of
> [Stacks, Tag 0A9E]. For `L` in `D_QCoh(𝒪_X)` and `K` in `D_QCoh(𝒪_Y)`, the canonical map
> `Rf_*R𝓗om_{𝒪_X}(L, a(K)) ⟶ R𝓗om_{𝒪_Y}(Rf_*L, K)`: the map
> `Rf_*R𝓗om_{𝒪_X}(L, a(K)) ⟶ R𝓗om_{𝒪_Y}(Rf_*L, Rf_*a(K))` of [Stacks, Tag 0B69], followed by
> `R𝓗om_{𝒪_Y}(Rf_*L, -)` applied to the counit `Rf_*a(K) ⟶ K` of the adjunction.

```lean
def qcqsSheafyTrace (L : quasiCoherentDerivedCategory X) (K : quasiCoherentDerivedCategory Y) :
    (derivedPushforward f).obj
        (((Stacks.SheafOfModules.derivedSheafHom X.sheaf).obj (op L.obj)).obj
          ((twistedInverseImage f
            (StandardModel.isQuasicoherent_homology_derivedPushforward f)).obj K).obj) ⟶
      ((Stacks.SheafOfModules.derivedSheafHom Y.sheaf).obj
          (op ((derivedPushforward f).obj L.obj))).obj K.obj
```

## Tag 0A9Q, a lemma

[Tag 0A9Q](https://stacks.math.columbia.edu/tag/0A9Q) in the Stacks Project.

**`Stacks.Duality.isIso_coherator_map_sheafyTrace_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceCoheratorQCQS.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceCoheratorQCQS.lean#L210).

> **[Stacks, Tag 0A9Q].** Let `f : X ⟶ Y` be a morphism of quasi-compact quasi-separated
> schemes, let `a = f^×` be the right adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`
> ([Stacks, Tag 0A9E]), and let `DQ_Y : D(𝒪_Y) ⥤ D_QCoh(𝒪_Y)` be the coherator, the right adjoint
> of the inclusion ([Stacks, Tag 0CR0]). For `L` in `D_QCoh(𝒪_X)` and `K` in `D_QCoh(𝒪_Y)` the map
> of [Stacks, Tag 0B6H]
>
> `Rf_*R𝓗om_{𝒪_X}(L, a(K)) ⟶ R𝓗om_{𝒪_Y}(Rf_*L, K)`
>
> becomes an isomorphism after applying `DQ_Y`. The trace map is built, as in the source, from the
> tensor–internal-Hom adjunctions of [Stacks, Tag 08J8] on `X` and on `Y`,
> `Stacks.Cohomology.ProjectionFormulaInternalHomOnRingedTopoi.derivedTensorHomAdjunction`.
>
> The source's argument: the reduction to morphisms out of the quasi-coherent objects,
> `Stacks.Duality.isIso_coherator_map_of_bijective`, and the chain of five bijections,
> `Stacks.Duality.bijective_comp_sheafyTrace`.

```lean
theorem isIso_coherator_map_sheafyTrace_of_qcqs
    (L : quasiCoherentDerivedCategory X) (K : quasiCoherentDerivedCategory Y) :
    IsIso ((DerivedCategoryB.derivedCategoryB (A := Y.Modules)
        (SheafOfModules.isQuasicoherent Y.ringCatSheaf)).ι.rightAdjoint.map
      (sheafyTrace f
        (derivedTensorHomAdjunction (Stacks.SheafOfModules.ringedSite X.sheaf))
        (derivedTensorHomAdjunction (Stacks.SheafOfModules.ringedSite Y.sheaf))
        (StandardModel.isQuasicoherent_homology_derivedPushforward f)
        (twistedInverseImageAdjunction f
          (StandardModel.isQuasicoherent_homology_derivedPushforward f)) L K))
```

## Tag 0GEU, an example

[Tag 0GEU](https://stacks.math.columbia.edu/tag/0GEU) in the Stacks Project.

**`Stacks.Duality.AffineLine.uncoheratedTrace_example`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/AffineLineUncoheratedTrace.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/AffineLineUncoheratedTrace.lean#L316). The attribute's comment: “the full example in corrected form: the left side is in D\_QCoh, the right side is the product of copies of the structure sheaf, which is quasi-coherent exactly when every t satisfies t^j = t^(j+1) b (false over Z, true over a field), and then no isomorphism exists”.

> **[Stacks, Tag 0GEU].** Let `Y = Spec R`, `X = 𝐀¹_R` and `f : X ⟶ Y` the structure morphism,
> and take `L = 𝒪_X`, `K = 𝒪_Y` in the trace map `Rf_*R𝓗om_{𝒪_X}(L, a(K)) ⟶ R𝓗om_{𝒪_Y}(Rf_*L, K)`.
>
> 1. The left hand side is in `D_QCoh(𝒪_Y)`: this holds for `Rf_*R𝓗om_{𝒪_X}(𝒪_X, M)` for every
>    `M` in `D_QCoh(𝒪_X)`, so for `M = a(K)` whatever the right adjoint `a`.
> 2. The right hand side is isomorphic to `∏_{n ≥ 0} 𝒪_Y` placed in degree zero.
> 3. `∏_{n ≥ 0} 𝒪_Y` is quasi-coherent exactly when every `t ∈ R` satisfies an equation
>    `t^j = t^{j+1} b`.
> 4. So when some `t ∈ R` satisfies no such equation, the right hand side is not in `D_QCoh(𝒪_Y)`,
>    it is not isomorphic to the left hand side, and the trace map is not an isomorphism
>    (`Stacks.Duality.AffineLine.not_isIso_sheafyTrace`).
>
> The source asserts in (3) that the product is not quasi-coherent for an arbitrary `R`. That is
> false for a field (`Stacks.Duality.isQuasicoherent_piStructureSheaf_of_isField`), and (3) is the
> corrected form: the product fails to be quasi-coherent precisely for the rings with an element
> `t` admitting no equation `t^j = t^{j+1} b`, such as `ℤ` (`uncoheratedTrace_example_int`).

```lean
theorem uncoheratedTrace_example :
    (∀ M : quasiCoherentDerivedCategory (affineLine R),
      DerivedCategoryB.derivedCategoryB (A := (Spec R).Modules)
      (SheafOfModules.isQuasicoherent (Spec R).ringCatSheaf)
        (traceSource R M.obj)) ∧
    Nonempty (traceTarget R ≅ (DerivedCategory.singleFunctor (Spec R).Modules 0).obj
      (∏ᶜ (fun _ : ℕ ↦ SheafOfModules.unit (Spec R).ringCatSheaf))) ∧
    ((∏ᶜ (fun _ : ℕ ↦ SheafOfModules.unit (Spec R).ringCatSheaf)).IsQuasicoherent ↔
      ∀ t : R, ∃ (j : ℕ) (b : R), t ^ j = t ^ (j + 1) * b) ∧
    ((∃ t : R, ∀ (j : ℕ) (b : R), t ^ j ≠ t ^ (j + 1) * b) →
      ¬ DerivedCategoryB.derivedCategoryB (A := (Spec R).Modules)
        (SheafOfModules.isQuasicoherent (Spec R).ringCatSheaf) (traceTarget R) ∧
      ∀ M : quasiCoherentDerivedCategory (affineLine R),
        IsEmpty (traceSource R M.obj ≅ traceTarget R))
```

## Tag 0GEV, a remark

[Tag 0GEV](https://stacks.math.columbia.edu/tag/0GEV) in the Stacks Project.

**`Stacks.Duality.isIso_coherator_homEquiv_sheafyTrace_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceCoheratorErasure.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceCoheratorErasure.lean#L68). The attribute's comment: “if RHom(L, a(K)) is in D\_QCoh, erase DQ\_Y on the left hand side of the arrow”.

> **[Stacks, Tag 0GEV], erasing `DQ_Y` on the left.** Let `f : X ⟶ Y` be a morphism of
> quasi-compact quasi-separated schemes, `L ∈ D_QCoh(𝒪_X)` and `K ∈ D_QCoh(𝒪_Y)`. If
> `R𝓗om_{𝒪_X}(L, a(K))` lies in `D_QCoh(𝒪_X)`, the map
> `Rf_*R𝓗om_{𝒪_X}(L, a(K)) ⟶ DQ_Y(R𝓗om_{𝒪_Y}(Rf_*L, K))` in `D_QCoh(𝒪_Y)` adjoint to the trace of
> [Stacks, Tag 0B6H] is an isomorphism. All derived categories are at the standard model.

```lean
theorem isIso_coherator_homEquiv_sheafyTrace_of_qcqs :
    letI := HasDerivedCategory.standard X.Modules
    letI := HasDerivedCategory.standard Y.Modules
    ∀ (L : quasiCoherentDerivedCategory X) (K : quasiCoherentDerivedCategory Y)
      (hsrc : DerivedCategoryB.derivedCategoryB (A := X.Modules)
        (SheafOfModules.isQuasicoherent X.ringCatSheaf)
        (((Stacks.SheafOfModules.derivedSheafHom X.sheaf).obj (op L.obj)).obj
          ((twistedInverseImage f
            (StandardModel.isQuasicoherent_homology_derivedPushforward f)).obj K).obj)),
      IsIso ((Adjunction.ofIsLeftAdjoint (DerivedCategoryB.derivedCategoryB (A := Y.Modules)
        (SheafOfModules.isQuasicoherent Y.ringCatSheaf)).ι).homEquiv
        ⟨_, StandardModel.isQuasicoherent_homology_derivedPushforward f ⟨_, hsrc⟩⟩ _
        (sheafyTrace f
          (derivedTensorHomAdjunction (Stacks.SheafOfModules.ringedSite X.sheaf))
          (derivedTensorHomAdjunction (Stacks.SheafOfModules.ringedSite Y.sheaf))
          (StandardModel.isQuasicoherent_homology_derivedPushforward f)
          (twistedInverseImageAdjunction f
            (StandardModel.isQuasicoherent_homology_derivedPushforward f)) L K))
```

**`Stacks.Duality.isIso_coherator_counit_comp_sheafyTrace_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceCoheratorErasure.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceCoheratorErasure.lean#L96). The attribute's comment: “if RHom(Rf\_*L, K) is in D\_QCoh, erase DQ\_Y on the right hand side of the arrow”.

> **[Stacks, Tag 0GEV], erasing `DQ_Y` on the right.** Let `f : X ⟶ Y` be a morphism of
> quasi-compact quasi-separated schemes, `L ∈ D_QCoh(𝒪_X)` and `K ∈ D_QCoh(𝒪_Y)`. If
> `R𝓗om_{𝒪_Y}(Rf_*L, K)` lies in `D_QCoh(𝒪_Y)`, the map
> `DQ_Y(Rf_*R𝓗om_{𝒪_X}(L, a(K))) ⟶ R𝓗om_{𝒪_Y}(Rf_*L, K)`, the counit of the coherator followed by
> the trace of [Stacks, Tag 0B6H], is an isomorphism. All derived categories are at the standard
> model.

```lean
theorem isIso_coherator_counit_comp_sheafyTrace_of_qcqs :
    letI := HasDerivedCategory.standard X.Modules
    letI := HasDerivedCategory.standard Y.Modules
    ∀ (L : quasiCoherentDerivedCategory X) (K : quasiCoherentDerivedCategory Y)
      (_htgt : DerivedCategoryB.derivedCategoryB (A := Y.Modules)
        (SheafOfModules.isQuasicoherent Y.ringCatSheaf)
        (((Stacks.SheafOfModules.derivedSheafHom Y.sheaf).obj
          (op ((derivedPushforward f).obj L.obj))).obj K.obj)),
      IsIso ((Adjunction.ofIsLeftAdjoint (DerivedCategoryB.derivedCategoryB (A := Y.Modules)
        (SheafOfModules.isQuasicoherent Y.ringCatSheaf)).ι).counit.app _ ≫
        sheafyTrace f
          (derivedTensorHomAdjunction (Stacks.SheafOfModules.ringedSite X.sheaf))
          (derivedTensorHomAdjunction (Stacks.SheafOfModules.ringedSite Y.sheaf))
          (StandardModel.isQuasicoherent_homology_derivedPushforward f)
          (twistedInverseImageAdjunction f
            (StandardModel.isQuasicoherent_homology_derivedPushforward f)) L K)
```

**`Stacks.Duality.isIso_sheafyTrace_of_derivedCategoryB_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceCoheratorErasure.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceCoheratorErasure.lean#L123). The attribute's comment: “if both RHom's are in D\_QCoh, then the map of Tag 0B6H is an isomorphism”.

> **[Stacks, Tag 0GEV], both sides in `D_QCoh`.** Let `f : X ⟶ Y` be a morphism of
> quasi-compact quasi-separated schemes, `L ∈ D_QCoh(𝒪_X)` and `K ∈ D_QCoh(𝒪_Y)`. If
> `R𝓗om_{𝒪_X}(L, a(K))` lies in `D_QCoh(𝒪_X)` and `R𝓗om_{𝒪_Y}(Rf_*L, K)` lies in `D_QCoh(𝒪_Y)`, the
> trace `Rf_*R𝓗om_{𝒪_X}(L, a(K)) ⟶ R𝓗om_{𝒪_Y}(Rf_*L, K)` of [Stacks, Tag 0B6H] is an isomorphism.
> All derived categories are at the standard model.

```lean
theorem isIso_sheafyTrace_of_derivedCategoryB_of_qcqs :
    letI := HasDerivedCategory.standard X.Modules
    letI := HasDerivedCategory.standard Y.Modules
    ∀ (L : quasiCoherentDerivedCategory X) (K : quasiCoherentDerivedCategory Y)
      (_hsrc : DerivedCategoryB.derivedCategoryB (A := X.Modules)
        (SheafOfModules.isQuasicoherent X.ringCatSheaf)
        (((Stacks.SheafOfModules.derivedSheafHom X.sheaf).obj (op L.obj)).obj
          ((twistedInverseImage f
            (StandardModel.isQuasicoherent_homology_derivedPushforward f)).obj K).obj))
      (_htgt : DerivedCategoryB.derivedCategoryB (A := Y.Modules)
        (SheafOfModules.isQuasicoherent Y.ringCatSheaf)
        (((Stacks.SheafOfModules.derivedSheafHom Y.sheaf).obj
          (op ((derivedPushforward f).obj L.obj))).obj K.obj)),
      IsIso (sheafyTrace f
          (derivedTensorHomAdjunction (Stacks.SheafOfModules.ringedSite X.sheaf))
          (derivedTensorHomAdjunction (Stacks.SheafOfModules.ringedSite Y.sheaf))
          (StandardModel.isQuasicoherent_homology_derivedPushforward f)
          (twistedInverseImageAdjunction f
            (StandardModel.isQuasicoherent_homology_derivedPushforward f)) L K)
```

**`Stacks.Duality.sheafyTrace_quasiCoherent_criteria`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceQuasiCoherentCriterionUnconditional.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceQuasiCoherentCriterionUnconditional.lean#L102). The attribute's comment: “the 0CR1 identity for DQ\_Y and Rf\_*, and the trace of 0B6H is an isomorphism in cases (1) L and Rf\_*L perfect, (2) K bounded below and L and Rf\_*L pseudo-coherent”.

> **Stacks Project, Tag 0GEV.** Let `f : X ⟶ Y` be a morphism of quasi-compact quasi-separated
> schemes, `a` the right adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`, `DQ_X`, `DQ_Y` the
> coherators, `L ∈ D_QCoh(𝒪_X)` and `K ∈ D_QCoh(𝒪_Y)`. Then
> `DQ_Y(Rf_*R𝓗om(L, a(K))) ≅ Rf_*DQ_X(R𝓗om(L, a(K)))` ([Stacks, Tag 0CR1]), and the map
> `Rf_*R𝓗om_{𝒪_X}(L, a(K)) ⟶ R𝓗om_{𝒪_Y}(Rf_*L, K)` of [Stacks, Tag 0B6H] is an isomorphism if
> (1) `L` and `Rf_*L` are perfect, or (2) `K` is bounded below and `L` and `Rf_*L` are
> pseudo-coherent.
>
> The coherator is the one constructed for qcqs schemes ([Stacks, Tag 0CR0]); [Stacks, Tag 0A9Q],
> [Stacks, Tag 0A6H] and [Stacks, Tag 0A9I] enter through their proofs in this development. The
> erasure statements of the remark are in
> `StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceCoheratorErasure.lean`.

```lean
theorem sheafyTrace_quasiCoherent_criteria (L : quasiCoherentDerivedCategory X)
    (K : quasiCoherentDerivedCategory Y) :
    Nonempty ((DerivedCategoryB.derivedCategoryB (A := Y.Modules)
        (SheafOfModules.isQuasicoherent Y.ringCatSheaf)).ι.rightAdjoint.obj
          ((derivedPushforward f).obj (((Stacks.SheafOfModules.derivedSheafHom X.sheaf).obj
            (op L.obj)).obj ((twistedInverseImage f
              (StandardModel.isQuasicoherent_homology_derivedPushforward f)).obj K).obj)) ≅
        (quasiCoherentDerivedPushforward f
          (StandardModel.isQuasicoherent_homology_derivedPushforward f)).obj
          ((DerivedCategoryB.derivedCategoryB (A := X.Modules)
            (SheafOfModules.isQuasicoherent X.ringCatSheaf)).ι.rightAdjoint.obj
              (((Stacks.SheafOfModules.derivedSheafHom X.sheaf).obj (op L.obj)).obj
                ((twistedInverseImage f
                  (StandardModel.isQuasicoherent_homology_derivedPushforward f)).obj K).obj))) ∧
    (RingedSpace.IsPerfect (X := X.toRingedSpace) L.obj →
      RingedSpace.IsPerfect (X := Y.toRingedSpace)
        ((quasiCoherentDerivedPushforward f
          (StandardModel.isQuasicoherent_homology_derivedPushforward f)).obj L).obj →
      IsIso (sheafyTrace f
        (derivedTensorHomAdjunction (Stacks.SheafOfModules.ringedSite X.sheaf))
        (derivedTensorHomAdjunction (Stacks.SheafOfModules.ringedSite Y.sheaf))
        (StandardModel.isQuasicoherent_homology_derivedPushforward f)
        (twistedInverseImageAdjunction f
          (StandardModel.isQuasicoherent_homology_derivedPushforward f)) L K)) ∧
    (DerivedCategoryB.IsBoundedBelow K.obj →
      RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) L.obj →
      RingedSpace.IsPseudoCoherent (X := Y.toRingedSpace)
        ((quasiCoherentDerivedPushforward f
          (StandardModel.isQuasicoherent_homology_derivedPushforward f)).obj L).obj →
      IsIso (sheafyTrace f
        (derivedTensorHomAdjunction (Stacks.SheafOfModules.ringedSite X.sheaf))
        (derivedTensorHomAdjunction (Stacks.SheafOfModules.ringedSite Y.sheaf))
        (StandardModel.isQuasicoherent_homology_derivedPushforward f)
        (twistedInverseImageAdjunction f
          (StandardModel.isQuasicoherent_homology_derivedPushforward f)) L K))
```

## Tag 0GEW, an example

[Tag 0GEW](https://stacks.math.columbia.edu/tag/0GEW) in the Stacks Project.

**`Stacks.Duality.isIso_sheafyTrace_of_isProper_of_derivedCategoryBMinus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceProperIso.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceProperIso.lean#L141).

> **Stacks Project, Tag 0GEW.** Let `f : X ⟶ Y` be a proper morphism of Noetherian schemes, let
> `L ∈ D^-_Coh(𝒪_X)` and `K ∈ D^+_QCoh(𝒪_Y)`. Then the map
> `Rf_*R𝓗om_{𝒪_X}(L, a(K)) ⟶ R𝓗om_{𝒪_Y}(Rf_*L, K)` of [Stacks, Tag 0B6H], for `a` the right
> adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`, is an isomorphism.

```lean
theorem isIso_sheafyTrace_of_isProper_of_derivedCategoryBMinus [IsProper f] [IsNoetherian X]
    [IsNoetherian Y] (L : quasiCoherentDerivedCategory X) (K : quasiCoherentDerivedCategory Y)
    (hL : DerivedCategoryB.derivedCategoryBMinus (fun N : X.Modules => N.IsCoherent) L.obj)
    (hK : DerivedCategoryB.IsBoundedBelow K.obj) :
    IsIso (sheafyTrace f
      (derivedTensorHomAdjunction (Stacks.SheafOfModules.ringedSite X.sheaf))
      (derivedTensorHomAdjunction (Stacks.SheafOfModules.ringedSite Y.sheaf))
      (StandardModel.isQuasicoherent_homology_derivedPushforward f)
      (twistedInverseImageAdjunction f
        (StandardModel.isQuasicoherent_homology_derivedPushforward f)) L K)
```

## Tag 0B6I, a lemma

[Tag 0B6I](https://stacks.math.columbia.edu/tag/0B6I) in the Stacks Project.

**`Stacks.Duality.bijective_comp_sheafyTrace_structureSheaf_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceGlobalHomQcqs.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/SheafyTraceGlobalHomQcqs.lean#L254). The attribute's comment: “the whole lemma, for every right adjoint a of Rf\_* on D\_QCoh and every adjunction exhibiting it: a is the tag's own datum, the statement being written with a(K) in it and the map built from the counit, so the parameters a and adj quantify over more than the source's fixed choice rather than assuming anything; likewise DX and DY, every tensor-internal-hom adjunction of Tag 08J8 the trace map is built from, one being derivedTensorHomAdjunction. Nothing is assumed beyond these data: the projection formula of Tag 08EU, the quasi-coherence of Lf^*(O\_Y[-n]) ⊗ᴸ L of Tag 08DX part (1) and the quasi-coherence of Rf\_* of Tag 08D5 part (1) are all proved from the hypotheses the tag states, f quasi-compact and quasi-separated and Y quasi-compact. The two global derived homs are read degreewise as the morphism groups Hom(O\_Y[-n], -) they corepresent by Tags 0B6A and 08DK, the left-hand one on Y after Rf\_*, which is the source's own second expression RGamma(Y, Rf\_* RHom(L, a(K))) for it”.

> **[Stacks, Tag 0B6I].** Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of
> schemes with `Y` quasi-compact, let `a` be a right adjoint of
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`, and let `L` be an object of `D_QCoh(𝒪_X)` and `K` one of
> `D_QCoh(𝒪_Y)`. Then in every degree `n` the sheafy trace map of [Stacks, Tag 0B6H] induces a
> bijection
>
> `Hom_{D(𝒪_Y)}(𝒪_Y⟦-n⟧, Rf_*R𝓗om_{𝒪_X}(L, a K)) ⟶ Hom_{D(𝒪_Y)}(𝒪_Y⟦-n⟧, R𝓗om_{𝒪_Y}(Rf_*L, K))`,
>
> that is, an isomorphism of global derived Homs `R Hom_X(L, a K) ⟶ R Hom_Y(Rf_*L, K)` read degree
> by degree through `H^n(Y, E) = Ext^n_Y(𝒪_Y, E) = Hom(𝒪_Y⟦-n⟧, E)`.
>
> No input of [Stacks, Tag 0A9Q] is a hypothesis. The projection formula of [Stacks, Tag 08EU] is
> `Stacks.Duality.isIso_pullbackProjectionFormulaMap`; the quasi-coherence of
> `Lf^*(𝒪_Y⟦-n⟧) ⊗^L_{𝒪_X} L` comes from
> `Stacks.RingedSpace.pullbackShiftedUnitTensorIso`, which identifies that object with `L⟦-n⟧`,
> and the stability of `D_QCoh(𝒪_X)` under shifts; and the quasi-coherence of `Rf_*` of part (1) of
> [Stacks, Tag 08D5], which `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` and hence `a` cannot be written
> down without, is `Stacks.Duality.isQuasicoherent_homology_derivedPushforward_qcqs`. All three
> need only the quasi-compactness and quasi-separatedness of `f` and the quasi-compactness of `Y`,
> which the tag states. `a` and `adj` are parameters because they are the tag's data: `a(K)` is
> named by the statement of this tag and the trace map is built from the counit of `Rf_* ⊣ a`, so
> quantifying over every right adjoint and every adjunction exhibiting it — which is what the
> binders do — is stronger than fixing the one the source fixes. Their existence is the separate
> [Stacks, Tag 0A9E], proved at this model as
> `Stacks.Duality.AnyModel.isLeftAdjoint_quasiCoherentDerivedPushforward_of_qcqs`. The same holds
> for `DX` and `DY`: the trace map is built from a tensor–internal-Hom adjunction of
> [Stacks, Tag 08J8] on each side, the statement holds for every choice, and one exists, namely
> `Stacks.Cohomology.ProjectionFormulaInternalHomOnRingedTopoi.derivedTensorHomAdjunction`.
>
> No coherator is needed in this form: the chain of five bijections of Tag 0A9Q is already a
> statement about morphisms out of the quasi-coherent objects, and `𝒪_Y⟦-n⟧` is one of them.

```lean
public theorem bijective_comp_sheafyTrace_structureSheaf_of_qcqs
    (L : quasiCoherentDerivedCategory X) (K : quasiCoherentDerivedCategory Y) (n : ℤ) :
    Function.Bijective (fun g : (ι _).obj (derivedStructureSheafInDegree Y n) ⟶
        (derivedPushforward f).obj
          (((Stacks.SheafOfModules.derivedSheafHom X.sheaf).obj (op L.obj)).obj
            (a.obj K).obj) =>
      g ≫ sheafyTrace f DX DY (isQuasicoherent_homology_derivedPushforward_qcqs f) adj L K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.3, Tag 0A9D](https://stacks.math.columbia.edu/tag/0A9D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
