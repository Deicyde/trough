---
declaration: section
origin: cited
lean: Stacks.Duality.qcqsTrace, Stacks.Duality.twistedInverseImageAdjunction_homEquiv_symm_qcqs, Stacks.Duality.map_trace_eq_baseChange_comp_trace_of_torIndependent, Stacks.Duality.map_unit_comp_baseChange_comp_baseChange_of_torIndependent, AlgebraicGeometry.qcqsTrace_specMap_app_derivedTilde, AlgebraicGeometry.qcqsTrace_specMap_app_derivedTilde_Qh
statement: formalized
proof: formalized
---

# 48.7 Right adjoint of pushforward and trace maps

Section 48.7 of the Stacks Project, [Tag 0AWG](https://stacks.math.columbia.edu/tag/0AWG). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AWG, the section

[Tag 0AWG](https://stacks.math.columbia.edu/tag/0AWG) in the Stacks Project.

**`Stacks.Duality.qcqsTrace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/QcqsTrace.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/QcqsTrace.lean#L71). The attribute's comment: “the trace map Tr\_f : Rf\_* ∘ a ⟶ id of a morphism of quasi-compact and quasi-separated schemes, the counit of the adjunction Rf\_* ⊣ a of Tag 0A9E”.

> **The trace map `Tr_f : Rf_* ∘ a ⟶ id`** of a morphism `f : X ⟶ Y` of quasi-compact and
> quasi-separated schemes, where `a` is the right adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`
> ([Stacks, Tag 0A9E]): the counit of the adjunction `Rf_* ⊣ a`.

```lean
def qcqsTrace :
    twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f) ⋙
        quasiCoherentDerivedPushforward f (isQuasicoherent_homology_derivedPushforward_of_qcqs f) ⟶
      𝟭 _
```

**`Stacks.Duality.twistedInverseImageAdjunction_homEquiv_symm_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/QcqsTrace.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/QcqsTrace.lean#L91). The attribute's comment: “the bijection Hom\_X(L, a(K)) ⟶ Hom\_Y(Rf\_*L, K) characterizing the right adjoint is φ ↦ Tr\_\{f,K} ∘ Rf\_*φ”.

> **The trace map characterizes the right adjoint.** For a morphism `f : X ⟶ Y` of
> quasi-compact and quasi-separated schemes, the bijection
> `Hom_X(L, a(K)) ⟶ Hom_Y(Rf_*L, K)` of the adjunction `Rf_* ⊣ a` sends `φ` to
> `Tr_{f,K} ∘ Rf_*φ`.

```lean
theorem twistedInverseImageAdjunction_homEquiv_symm_qcqs (L : quasiCoherentDerivedCategory X)
    (K : quasiCoherentDerivedCategory Y)
    (φ : L ⟶ (twistedInverseImage f
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj K) :
    ((twistedInverseImageAdjunction f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).homEquiv L K).symm φ =
      (quasiCoherentDerivedPushforward f
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).map φ ≫
        (qcqsTrace f).app K
```

## Tag 0B6J, a lemma

[Tag 0B6J](https://stacks.math.columbia.edu/tag/0B6J) in the Stacks Project.

**`Stacks.Duality.map_trace_eq_baseChange_comp_trace_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BaseChangeTrace.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BaseChangeTrace.lean#L79).

> **[Stacks, Tag 0B6J] (trace map and base change).** For a cartesian square of
> quasi-compact and quasi-separated schemes with `f` and `g` Tor independent, the maps
> `1 ⋆ Tr_f : Lg^* ∘ Rf_* ∘ a ⟶ Lg^*` and `Tr_{f'} ⋆ 1 : Rf'_* ∘ a' ∘ Lg^* ⟶ Lg^*` agree via the
> base change maps `β : Lg^* ∘ Rf_* ⟶ Rf'_* ∘ L(g')^*` and `α : L(g')^* ∘ a ⟶ a' ∘ Lg^*`
> (Equation 48.5.0.1): `Lg^*(Tr_{f,K}) = Tr_{f',Lg^*K} ∘ Rf'_*(α_K) ∘ β_{a(K)}` for every `K`.

```lean
theorem map_trace_eq_baseChange_comp_trace_of_torIndependent (sq : IsPullback g' f' f g)
    (hTor : TorIndependent f g) (K : quasiCoherentDerivedCategory Y) :
    haveI := isIso_twistedInverseImagePushforwardBaseChange_of_torIndependent sq hTor
    (quasiCoherentDerivedPullback g (isQuasicoherent_homology_derivedPullback' g)).map
        ((twistedInverseImageAdjunction f
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).counit.app K) =
      (quasiCoherentDerivedBaseChange g' f' f g
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g)
          (isQuasicoherent_homology_derivedPullback' g)
          (isQuasicoherent_homology_derivedPullback' g') sq.w).app
          ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj K) ≫
        (quasiCoherentDerivedPushforward f'
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f')).map
          ((twistedInverseImageBaseChangeMap g' f' f g
            (isQuasicoherent_homology_derivedPushforward_of_qcqs g')
            (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
            (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
            (isQuasicoherent_homology_derivedPushforward_of_qcqs g) sq).app K) ≫
          (twistedInverseImageAdjunction f'
            (isQuasicoherent_homology_derivedPushforward_of_qcqs f')).counit.app
            ((quasiCoherentDerivedPullback g
              (isQuasicoherent_homology_derivedPullback' g)).obj K)
```

## Tag 0B6K, a lemma

[Tag 0B6K](https://stacks.math.columbia.edu/tag/0B6K) in the Stacks Project.

**`Stacks.Duality.map_unit_comp_baseChange_comp_baseChange_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BaseChangeTrace.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BaseChangeTrace.lean#L117).

> **[Stacks, Tag 0B6K] (unit and base change).** For a cartesian square of quasi-compact and
> quasi-separated schemes with `f` and `g` Tor independent, the maps
> `1 ⋆ η_f : L(g')^* ⟶ L(g')^* ∘ a ∘ Rf_*` and `η_{f'} ⋆ 1 : L(g')^* ⟶ a' ∘ Rf'_* ∘ L(g')^*` agree
> via the base change maps `α` (Equation 48.5.0.1) and `β`:
> `a'(β_M) ∘ α_{Rf_*M} ∘ L(g')^*(η_{f,M}) = η_{f',L(g')^*M}` for every `M`.

```lean
theorem map_unit_comp_baseChange_comp_baseChange_of_torIndependent (sq : IsPullback g' f' f g)
    (hTor : TorIndependent f g) (M : quasiCoherentDerivedCategory X) :
    haveI := isIso_twistedInverseImagePushforwardBaseChange_of_torIndependent sq hTor
    (quasiCoherentDerivedPullback g' (isQuasicoherent_homology_derivedPullback' g')).map
        ((twistedInverseImageAdjunction f
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).unit.app M) ≫
      (twistedInverseImageBaseChangeMap g' f' f g
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g) sq).app
          ((quasiCoherentDerivedPushforward f
            (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj M) ≫
        (twistedInverseImage f' (isQuasicoherent_homology_derivedPushforward_of_qcqs f')).map
          ((quasiCoherentDerivedBaseChange g' f' f g
            (isQuasicoherent_homology_derivedPushforward_of_qcqs g')
            (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
            (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
            (isQuasicoherent_homology_derivedPushforward_of_qcqs g)
            (isQuasicoherent_homology_derivedPullback' g)
            (isQuasicoherent_homology_derivedPullback' g') sq.w).app M) =
      (twistedInverseImageAdjunction f'
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f')).unit.app
        ((quasiCoherentDerivedPullback g'
          (isQuasicoherent_homology_derivedPullback' g')).obj M)
```

## Tag 0B6L, an example

[Tag 0B6L](https://stacks.math.columbia.edu/tag/0B6L) in the Stacks Project.

**`AlgebraicGeometry.qcqsTrace_specMap_app_derivedTilde`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/AffineTrace.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/AffineTrace.lean#L291). The attribute's comment: “the trace map Tr\_f of f = Spec(S) → Spec(R) is, under a(K~) ≅ RHom\_R(S, K)~ and Rf\_*(M~) ≅ (M\_R)~, the map RHom\_R(S, K) → K of the derived restriction–Hom adjunction”.

> **Stacks 0B6L.** Let `φ : R ⟶ S` be a ring map, `Y = Spec R`, `X = Spec S` and
> `f = Spec φ : X ⟶ Y`, and let `a` be the right adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`.
> For `K` in `D(R)`, identify `a(K~)` with `RHom_R(S, K)~`
> (`AlgebraicGeometry.derivedTildeCompTwistedInverseImageIsoDerivedHom`, [Stacks, Tag 0A9F]) and
> `Rf_*(M~)` with `(M_R)~` (`AlgebraicGeometry.derivedTildeCompDerivedQuasicoherentPushforwardIso`,
> [Stacks, Tag 0DJK]). Then the trace `Tr_{f, K~} : Rf_* a(K~) ⟶ K~` of [Stacks, Tag 0AWG] is
> derived sheafification of the map `RHom_R(S, K) ⟶ K` which is the counit of the derived
> restriction–Hom adjunction `Dualizing.AnyModel.derivedHomAdjunction`.
>
> That counit is the map induced by the `R`-module map `R ⟶ S`: on complexes it is evaluation at
> `1`, `Hom_R(S, K) ⟶ Hom_R(R, K) = K`
> (`Dualizing.AnyModel.derivedHomAdjunction_counit_app`); the statement with that substituted is
> `AlgebraicGeometry.qcqsTrace_specMap_app_derivedTilde_Qh`.

```lean
theorem qcqsTrace_specMap_app_derivedTilde (K : DerivedCategory (ModuleCat.{u} R)) :
    (Stacks.Duality.qcqsTrace (Spec.map φ)).app ((derivedTilde R).obj K) =
      (derivedQuasicoherentPushforward (Spec.map φ)).map
          ((derivedTildeCompTwistedInverseImageIsoDerivedHom φ).hom.app K) ≫
        (derivedTildeCompDerivedQuasicoherentPushforwardIso φ).hom.app
          ((Dualizing.AnyModel.derivedHom.{u, u, u, u, u} φ.hom).obj K) ≫
        (derivedTilde R).map
          ((Dualizing.AnyModel.derivedHomAdjunction φ.hom).counit.app K)
```

**`AlgebraicGeometry.qcqsTrace_specMap_app_derivedTilde_Qh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/AffineTrace.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/AffineTrace.lean#L318). The attribute's comment: “on complexes: through Hom\_R(S, K) → RHom\_R(S, K), the trace is the map Hom\_R(S, K) → K induced by R → S, an isomorphism for K K-injective”.

> **Stacks 0B6L, on complexes: the trace is induced by `R ⟶ S`.** Let `φ : R ⟶ S`,
> `f = Spec φ`, and let `K` be a complex of `R`-modules. Through the comparison
> `Hom_R(S, K) ⟶ RHom_R(S, K)` and the identifications of
> `AlgebraicGeometry.qcqsTrace_specMap_app_derivedTilde`, the trace `Tr_{f, K~}` is derived
> sheafification of the map `Hom_R(S, K) ⟶ K`, `g ↦ g(1)`, that is of precomposition with the
> `R`-module map `R ⟶ S` followed by `Hom_R(R, K) = K`. When `K` is K-injective the comparison is an
> isomorphism (`Dualizing.AnyModel.isIso_derivedHomComparison_app_of_isKInjective`), so this
> computes `Tr_{f, K~}` itself.

```lean
theorem qcqsTrace_specMap_app_derivedTilde_Qh
    (K : HomotopyCategory (ModuleCat.{u} R) (ComplexShape.up ℤ)) :
    (derivedQuasicoherentPushforward (Spec.map φ)).map
        ((derivedTilde S).map
            ((Dualizing.AnyModel.derivedHomComparison φ.hom).app K) ≫
          (derivedTildeCompTwistedInverseImageIsoDerivedHom φ).inv.app
            (DerivedCategory.Qh.obj K)) ≫
      (Stacks.Duality.qcqsTrace (Spec.map φ)).app
        ((derivedTilde R).obj (DerivedCategory.Qh.obj K)) =
    (derivedTildeCompDerivedQuasicoherentPushforwardIso φ).hom.app
        (DerivedCategory.Qh.obj
          (((ModuleCat.coextendScalars.{u, u, u} φ.hom).mapHomotopyCategory (.up ℤ)).obj K)) ≫
      (derivedTilde R).map
        ((ModuleCat.restrictScalars.{u} φ.hom).mapDerivedCategoryFactorsh.hom.app
            (((ModuleCat.coextendScalars.{u, u, u} φ.hom).mapHomotopyCategory (.up ℤ)).obj K) ≫
          DerivedCategory.Qh.map
            ((Dualizing.homotopyAdjunction (ModuleCat.restrictCoextendScalarsAdj.{u} φ.hom)
              (.up ℤ)).counit.app K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.7, Tag 0AWG](https://stacks.math.columbia.edu/tag/0AWG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
