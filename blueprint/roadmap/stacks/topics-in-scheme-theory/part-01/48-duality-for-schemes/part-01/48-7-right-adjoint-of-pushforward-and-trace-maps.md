---
declaration: section
origin: cited
lean: Stacks.Duality.qcqsTrace, Stacks.Duality.twistedInverseImageAdjunction_homEquiv_symm_qcqs, Stacks.Duality.map_trace_eq_baseChange_comp_trace_of_torIndependent, Stacks.Duality.map_unit_comp_baseChange_comp_baseChange_of_torIndependent, Dualizing.derivedHomAdjunction, Dualizing.derivedHomAdjunction_counit_app
statement: formalized
proof: formalized
---

# 48.7 Right adjoint of pushforward and trace maps

Section 48.7 of the Stacks Project, [Tag 0AWG](https://stacks.math.columbia.edu/tag/0AWG). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AWG, the section

[Tag 0AWG](https://stacks.math.columbia.edu/tag/0AWG) in the Stacks Project.

**`Stacks.Duality.qcqsTrace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/QcqsTrace.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/QcqsTrace.lean#L71). The attribute's comment: “the trace map Tr_f : Rf_* ∘ a ⟶ id of a morphism of quasi-compact and quasi-separated schemes, the counit of the adjunction Rf_* ⊣ a of Tag 0A9E”.

> **The trace map `Tr_f : Rf_* ∘ a ⟶ id`** of a morphism `f : X ⟶ Y` of quasi-compact and
> quasi-separated schemes, where `a` is the right adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`
> ([Stacks, Tag 0A9E]): the counit of the adjunction `Rf_* ⊣ a`.

```lean
def qcqsTrace :
    twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f) ⋙
        quasiCoherentDerivedPushforward f (isQuasicoherent_homology_derivedPushforward_of_qcqs f) ⟶
      𝟭 _
```

**`Stacks.Duality.twistedInverseImageAdjunction_homEquiv_symm_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/QcqsTrace.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/QcqsTrace.lean#L91). The attribute's comment: “the bijection Hom_X(L, a(K)) ⟶ Hom_Y(Rf_*L, K) characterizing the right adjoint is φ ↦ Tr_{f,K} ∘ Rf_*φ”.

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

**`Stacks.Duality.map_trace_eq_baseChange_comp_trace_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BaseChangeTrace.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BaseChangeTrace.lean#L79).

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
          (isQuasicoherent_homology_derivedPullback' g') sq.w).natTrans.app
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

**`Stacks.Duality.map_unit_comp_baseChange_comp_baseChange_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BaseChangeTrace.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BaseChangeTrace.lean#L117).

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
            (isQuasicoherent_homology_derivedPullback' g') sq.w).natTrans.app M) =
      (twistedInverseImageAdjunction f'
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f')).unit.app
        ((quasiCoherentDerivedPullback g'
          (isQuasicoherent_homology_derivedPullback' g')).obj M)
```

## Tag 0B6L, an example

[Tag 0B6L](https://stacks.math.columbia.edu/tag/0B6L) in the Stacks Project.

Declarations registered for the tag:

- [`Dualizing.derivedHomAdjunction`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/TrivialDuality/BaseChange.lean#L113), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/AffineTrace.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/AffineTrace.lean#L34) (StacksFrontier): “the trace map”.
- [`Dualizing.derivedHomAdjunction_counit_app`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/TrivialDuality/BaseChange.lean#L136), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/AffineTrace.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/AffineTrace.lean#L35) (StacksFrontier): “induced by the ring map”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.7, Tag 0AWG](https://stacks.math.columbia.edu/tag/0AWG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
