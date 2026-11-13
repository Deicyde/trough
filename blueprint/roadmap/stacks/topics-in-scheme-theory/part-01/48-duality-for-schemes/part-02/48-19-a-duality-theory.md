---
declaration: section
origin: cited
lean: Stacks.Duality.LocallySmall.upperShriek_closedImmersion_of_fts, Stacks.Duality.isNormalTensorPullbackRightAdjoint_of_fts, Stacks.Duality.nonempty_upperShriekFiniteIsoDerivedHomSheaf, Stacks.Duality.nonempty_upperShriekIsoPullbackTensorOfKoszulRegular, Stacks.Duality.upperShriek_rightAdjoint_and_duality_of_isProper, Stacks.Duality.nonempty_sheafHomDualizingIsoOfIsProper, Stacks.Duality.nonempty_upperShriekIsoPullbackTensorOfSmoothOfIsProper, Stacks.Duality.exists_upperShriekPseudofunctor
statement: formalized
proof: formalized
---

# 48.19 A duality theory

Section 48.19 of the Stacks Project, [Tag 0AU3](https://stacks.math.columbia.edu/tag/0AU3). 1 tag here is carried by 7 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AU3, the section

[Tag 0AU3](https://stacks.math.columbia.edu/tag/0AU3) in the Stacks Project.

**`Stacks.Duality.LocallySmall.upperShriek_closedImmersion_of_fts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTwistedInverseImageQcqs.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTwistedInverseImageQcqs.lean#L160). The attribute's comment: “clause (5): for a closed immersion f^! = RHom(O\_X, -), at the locally small derived categories”.

> **Stacks Project, Tag 0AA2 (Lemma 48.17.4).** In Situation 48.16.1 — `S` a Noetherian scheme
> and `FTS S` the schemes separated and of finite type over `S` — let `i : X ⟶ Y` be a morphism of
> `FTS S` whose underlying morphism of schemes is a closed immersion. Then
> `i^!(-) = R𝓗om(𝒪_X, -)`:
>
> 1. `Ri_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` has a right adjoint;
> 2. the upper shriek `i^! = j^* ∘ a` of [Stacks, Tag 0A9Y] at the compactification `X̄ = X` that a
>    proper morphism is (`Stacks.Duality.properCompactification`), with its right adjoint `a`
>    *produced* by (1) and its quasi-coherence inputs discharged, agrees with `R𝓗om(𝒪_X, -)` on
>    `D⁺_QCoh(𝒪_Y)`;
> 3. for every right adjoint `a` of `Ri_*` the canonical comparison `a(K) ⟶ R𝓗om(𝒪_X, K)` — the
>    mate of the counit of `a` under [Stacks, Tag 0A76] — is an isomorphism for every `K` in
>    `D⁺_QCoh(𝒪_Y)`.
>
> The existence (1) is
> `Stacks.Duality.LocallySmall.isLeftAdjoint_affineHomQuasiCoherentDerivedPushforward`, which builds
> the right adjoint as `DQ_X ∘ R𝓗om(𝒪_X, -)` from the coherator of [Stacks, Tag 0CR0]; `X` is
> quasi-compact and quasi-separated, being of finite type over a Noetherian scheme. The
> identification (2), (3) is [Stacks, Tag 0A9X] at this model
> (`Stacks.Duality.LocallySmall.isIso_rightAdjointToDerivedSheafHom_app`), whose hypotheses —
> pseudo-coherence of `i` — hold in Situation 48.16.1.

```lean
theorem upperShriek_closedImmersion_of_fts {S : Scheme.{u}} [IsNoetherian S] {X Y : FTS S}
    (i : X ⟶ Y) [IsClosedImmersion i.left] :
    (affineHomQuasiCoherentDerivedPushforward i.left).IsLeftAdjoint ∧
      IsDerivedSheafHomRightAdjoint i.left
        (upperShriek i (properCompactification i)) ∧
      ∀ (a : quasiCoherentDerivedCategory Y.left ⥤ quasiCoherentDerivedCategory X.left)
        (adj : affineHomQuasiCoherentDerivedPushforward i.left ⊣ a)
        (K : (isBoundedBelowQuasiCoherent Y.left).FullSubcategory),
        IsIso ((rightAdjointToDerivedSheafHom i.left
          (isQuasicoherent_homology_derivedPushforward_of_isAffineHom i.left) a adj).app
            K.obj)
```

**`Stacks.Duality.isNormalTensorPullbackRightAdjoint_of_fts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheoryDivisor.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheoryDivisor.lean#L175). The attribute's comment: “clause (7) of Section 48.19: for the inclusion of an effective Cartier divisor into an object of FTS S, f^! is derived pullback tensored with the shifted normal sheaf i^*O\_Y(D)[-1]. Both inputs are proved unconditionally: clause (5) of the same section (Tag 0AA2) as Stacks.Duality.isDerivedSheafHomRightAdjoint\_of\_fts\_closedImmersion, and Tag 0AA4 as Stacks.Divisors.normalTensorDerivedSheafHomIso. As in clause (5), i^! is the explicit parameter a with its adjunction, the existence statement being Tag 0A9E”.

> **Stacks Project, Section 0AU3, clause (7).** Let `S` be a Noetherian scheme, let `Y` be an
> object of `AlgebraicGeometry.FTS S` — a scheme separated and of finite type over `S` — and let
> `D ⊆ Y` be an effective Cartier divisor, with closed immersion `i : D ⟶ Y` and normal sheaf
> `𝒩 = i^*𝒪_Y(D)`. Let `a` be a right adjoint of `Ri_* : D_QCoh(𝒪_D) ⥤ D_QCoh(𝒪_Y)`. Then `a`,
> which is `i^!`, is `Li^*(-) ⊗^L_{𝒪_D} 𝒩[-1]` on bounded-below complexes with quasi-coherent
> cohomology:
>
> `i^!(-) = Li^*(-) ⊗_{𝒪_D} i^*𝒪_Y(D)[-1]`.
>
> The proof is the section's own: clause (5) of the section, which is [Stacks, Tag 0AA2] and is
> formalized as `Stacks.Duality.isDerivedSheafHomRightAdjoint_of_fts_closedImmersion`, identifies
> `i^!` with `R𝓗om_{𝒪_Y}(𝒪_D, -)`; and [Stacks, Tag 0AA4],
> `Stacks.Divisors.normalTensorDerivedSheafHomIso`, identifies that with
> `Li^*(-) ⊗^L_{𝒪_D} 𝒩[-1]`.

```lean
theorem isNormalTensorPullbackRightAdjoint_of_fts
    (a : quasiCoherentDerivedCategory Y.left ⥤ quasiCoherentDerivedCategory D.subscheme)
    (adj : affineHomQuasiCoherentDerivedPushforward D.subschemeι ⊣ a) :
    IsNormalTensorPullbackRightAdjoint D a
```

**`Stacks.Duality.nonempty_upperShriekFiniteIsoDerivedHomSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheoryFinite.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheoryFinite.lean#L72). The attribute's comment: “clause (6): for a finite morphism f : Y to X of FTS S and any compactification, f\_* f^! = RHom(f\_* O\_Y, -) as functors from D^+\_QCoh(O\_X) to D(f\_* O\_Y), f\_* read as an f\_* O\_Y-module through the equivalence of Tag 0AVW; from clause (2) and Tag 0AX2”.

> **Stacks Project, Section 0AU3, clause (6).** Let `S` be a Noetherian scheme and let
> `f : Y ⟶ X` be a finite morphism of `FTS S`, with `f^!` computed at any compactification. Then
> `f_* f^!(-) = R𝓗om_{𝒪_X}(f_*𝒪_Y, -)` as functors `D⁺_QCoh(𝒪_X) ⥤ D(f_*𝒪_Y)`.

```lean
theorem nonempty_upperShriekFiniteIsoDerivedHomSheaf :
    haveI := pseudoCoherent_of_isFinite_of_isLocallyNoetherian f.left
    Nonempty (upperShriekPlus f j ⋙ ObjectProperty.ι _ ⋙
        (derivedQuasicoherentPushforwardOverRingEquivalence f.left).functor ⋙
          ObjectProperty.ι _ ≅
      ObjectProperty.ι _ ⋙ ObjectProperty.ι _ ⋙ (structureSheafModelEquiv X.left).inverse ⋙
        derivedHomSheaf f.left ⋙ (pushforwardRingModelEquiv f.left).functor)
```

**`Stacks.Duality.nonempty_upperShriekIsoPullbackTensorOfKoszulRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheoryKoszul.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheoryKoszul.lean#L136). The attribute's comment: “clause (8): for a Koszul-regular immersion f : X to Y of codimension c into an object of FTS S (the conormal sheaf of its canonical closed factor into an open of Y finite locally free of rank c) and any compactification, f^!(-) = Lf^*(-) tensor wedge^c N[-c] as functors on D^+\_QCoh(O\_Y), N the normal sheaf; from Tag 0BR0 and Tag 0B6U (e)”.

> **Stacks Project, Section 0AU3, clause (8).** Let `S` be a Noetherian scheme and let
> `f : X ⟶ Y` be a Koszul-regular immersion of codimension `c` into an object of `FTS S`: an
> immersion whose canonical closed factor `i = f.liftCoborder : X ⟶ f.coborderRange` (a closed
> immersion into an open of `Y`) has conormal sheaf finite locally free of rank `c`. Write `𝒩` for
> the normal sheaf of `f`, the dual of the conormal sheaf of `i`. Then, with `f^!` computed at any
> compactification,
>
> `f^!(-) ≅ Lf^*(-) ⊗ᴸ_{𝒪_X} ∧^c 𝒩[-c]`
>
> as functors on `D⁺_QCoh(𝒪_Y)`.

```lean
theorem nonempty_upperShriekIsoPullbackTensorOfKoszulRegular [IsImmersion f.left]
    (hf : IsKoszulRegularImmersion f.left)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
      (R := X.left.ringCatSheaf) (Stacks.Conormal.conormalSheaf f.left.liftCoborder) c] :
    Nonempty (((ObjectProperty.ι _ : quasiCoherentDerivedCategoryPlusOfModel Y.left ⥤ _) ⋙
        quasiCoherentDerivedPullback' f.left ⋙ ObjectProperty.ι _) ⋙
      (derivedTensor X.left).flip.obj
        ((DerivedCategory.singleFunctor X.left.Modules (c : ℤ)).obj
          (Scheme.Modules.exteriorPower (Stacks.Divisors.normalSheaf f.left.liftCoborder) c)) ≅
      (ObjectProperty.ι _ : quasiCoherentDerivedCategoryPlusOfModel Y.left ⥤ _) ⋙
        upperShriek f j ⋙ ObjectProperty.ι _)
```

**`Stacks.Duality.upperShriek_rightAdjoint_and_duality_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheoryProperDuality.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheoryProperDuality.lean#L147). The attribute's comment: “clause (2) in full: for a proper morphism f of FTS S and any compactification, f^! carries D^+\_QCoh into D^+\_QCoh and is the restriction to D^+\_QCoh of every right adjoint of Rf\_* on D\_QCoh, and Rf\_* RHom(K, f^! M) = RHom(Rf\_* K, M) for K in D^-\_Coh(O\_X) and M in D^+\_QCoh(O\_Y) (the sheafy trace of Tag 0B6H, invertible by Tag 0GEW)”.

> **Stacks Project, Section 0AU3, clause (2).** Let `S` be a Noetherian scheme and let
> `f : X ⟶ Y` be a proper morphism of `FTS S`, with `f^!` computed at any compactification `j`.
> Then `f^!` is the restriction of the right adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` to
> `D⁺_QCoh(𝒪_Y)`, and there is a canonical isomorphism
>
> `Rf_* R𝓗om_{𝒪_X}(K, f^!M) ≅ R𝓗om_{𝒪_Y}(Rf_*K, M)`
>
> for all `K ∈ D⁻_Coh(𝒪_X)` and `M ∈ D⁺_QCoh(𝒪_Y)`:
>
> 1. `f^!` carries `D⁺_QCoh(𝒪_Y)` into `D⁺_QCoh(𝒪_X)`;
> 2. for every right adjoint `a` of `Rf_*`, the functor `f^! : D⁺_QCoh(𝒪_Y) ⥤ D⁺_QCoh(𝒪_X)` is
>    isomorphic to the restriction of `a`;
> 3. the isomorphism, `Stacks.Duality.sheafHomUpperShriekIsoOfIsProper`, with the derived internal
>    Homs and `Rf_*` read at the standard model.

```lean
theorem upperShriek_rightAdjoint_and_duality_of_isProper :
    (∀ M : quasiCoherentDerivedCategory Y.left, DerivedCategoryB.IsBoundedBelow M.obj →
        DerivedCategoryB.IsBoundedBelow ((upperShriek f j).obj M).obj) ∧
      (∀ (a : quasiCoherentDerivedCategory Y.left ⥤ quasiCoherentDerivedCategory X.left)
          (_ : DerivedPushforward.qcqsRestrictedDerivedPushforward f.left ⊣ a),
        Nonempty (upperShriekPlus f j ⋙ ObjectProperty.ι _ ≅ ObjectProperty.ι _ ⋙ a)) ∧
      ∀ (K : Std X.left) (_ : minusCoh X.left K) (M : (qcoh Y.left).FullSubcategory)
        (_ : @DerivedCategoryB.IsBoundedBelow Y.left.Modules _ _
          (PerfectApproximation.standardModel Y.left) M.obj),
        Nonempty ((push f.left).obj (((sheafHom X.left).obj (op K)).obj
            ((comparison X.left).inverse.obj
              ((upperShriek f j).obj ⟨(comparison Y.left).functor.obj M.obj, M.property⟩).obj)) ≅
          ((sheafHom Y.left).obj (op ((push f.left).obj K))).obj M.obj)
```

**`Stacks.Duality.nonempty_sheafHomDualizingIsoOfIsProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheoryProperDuality.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheoryProperDuality.lean#L187). The attribute's comment: “clause (4)(c): for a proper morphism f : X to Y of FTS S, a dualizing complex omega\_Y on Y and omega\_X = f^! omega\_Y at any compactification, Rf\_* RHom(K, omega\_X) = RHom(Rf\_* K, omega\_Y) for K in D^-\_Coh(O\_X); clause (2) at M = omega\_Y”.

> **Stacks Project, Section 0AU3, clause (4)(c).** Let `S` be a Noetherian scheme, let
> `f : X ⟶ Y` be a proper morphism of `FTS S`, let `ω_Y` be a dualizing complex on `Y` and
> `ω_X = f^!ω_Y` (at any compactification). Then
> `Rf_* R𝓗om_{𝒪_X}(K, ω_X) ≅ R𝓗om_{𝒪_Y}(Rf_*K, ω_Y)` for `K ∈ D⁻_Coh(𝒪_X)`.

```lean
theorem nonempty_sheafHomDualizingIsoOfIsProper {ω : Std Y.left}
    (hω : TwistedInverseImageDuality.IsDualizing ω) (K : Std X.left) (hK : minusCoh X.left K) :
    Nonempty ((push f.left).obj (((sheafHom X.left).obj (op K)).obj
        (upperShriekDualizing f j hω)) ≅
      ((sheafHom Y.left).obj (op ((push f.left).obj K))).obj ω)
```

**`Stacks.Duality.nonempty_upperShriekIsoPullbackTensorOfSmoothOfIsProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheorySmooth.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheorySmooth.lean#L87). The attribute's comment: “clause (9): for a smooth proper morphism f of relative dimension d of FTS S and any compactification, f^!(-) = Lf^*(-) tensor Omega^d\_\{X/Y}[d] as functors on D^+\_QCoh(O\_Y); from Tag 0B6U (e) (f is perfect), clause (2) and Tag 0BRT”.

> **Stacks Project, Section 0AU3, clause (9).** Let `S` be a Noetherian scheme and let
> `f : X ⟶ Y` be a smooth proper morphism of relative dimension `d` of `FTS S`, with `f^!`
> computed at any compactification. Then `f^!(-) ≅ Lf^*(-) ⊗ᴸ_{𝒪_X} Ω^d_{X/Y}[d]` as functors on
> `D⁺_QCoh(𝒪_Y)`, where `Ω^d_{X/Y} = ∧^d Ω_{X/Y}` and `[d]` places it in degree `-d`.

```lean
theorem nonempty_upperShriekIsoPullbackTensorOfSmoothOfIsProper :
    Nonempty (((ObjectProperty.ι _ : quasiCoherentDerivedCategoryPlusOfModel Y.left ⥤ _) ⋙
        quasiCoherentDerivedPullback' f.left ⋙ ObjectProperty.ι _) ⋙
      (derivedTensor X.left).flip.obj
        ((DerivedCategory.singleFunctor X.left.Modules (-(d : ℤ))).obj
          (Scheme.Modules.exteriorPower (Scheme.Hom.relativeDifferentials f.left) d)) ≅
      (ObjectProperty.ι _ : quasiCoherentDerivedCategoryPlusOfModel Y.left ⥤ _) ⋙
        upperShriek f j ⋙ ObjectProperty.ι _)
```

Declarations registered for the tag:

- [`Stacks.Duality.exists_upperShriekPseudofunctor`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/Compactification/ShriekPseudofunctor/Pseudofunctor.lean#L222), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheory.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheory.lean#L53) (StacksFrontier): “clause (1): the functors f^! of Tag 0AA0 on D^+\_QCoh, with the canonical isomorphisms (g o f)^! = f^! o g^! of Tag 0ATX, form a pseudofunctor on FTS\_S (Tag 0ATY)”.
- [`Stacks.Duality.coherentDuality_spec`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizing/CoherentDuality.lean#L226), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheory.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheory.lean#L57) (StacksFrontier): “clause (3): for a dualizing complex omega on a locally Noetherian scheme X (in particular an object of FTS\_S), D = RHom(-, omega) is an anti-equivalence of D\_Coh(O\_X) with the canonical isomorphism id = D o D, exchanging D^+\_Coh and D^-\_Coh and inducing an anti-equivalence of D^b\_Coh when X is quasi-compact (Tag 0A89)”.
- [`Stacks.Duality.isDualizingComplex_upperShriek_obj`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekDualizingComplexOfCharts.lean#L72), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheory.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheory.lean#L63) (StacksFrontier): “clause (4)(a): for f : X to Y in FTS\_S and omega\_Y a dualizing complex on Y, f^! omega\_Y (at any compactification) is a dualizing complex on X (Tag 0AA3)”.
- [`Stacks.Duality.UpperShriekDuality.upperShriekDualityIso`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekDuality.lean#L272), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheory.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheory.lean#L67) (StacksFrontier): “clause (4)(b): for f : X to Y in FTS\_S and K a dualizing complex on Y, f^! M = D\_X(Lf^* D\_Y(M)) naturally in M in D^+\_Coh(O\_Y), D\_Y = RHom(-, K), D\_X = RHom(-, f^! K) (Tag 0AU2)”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.19, Tag 0AU3](https://stacks.math.columbia.edu/tag/0AU3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
