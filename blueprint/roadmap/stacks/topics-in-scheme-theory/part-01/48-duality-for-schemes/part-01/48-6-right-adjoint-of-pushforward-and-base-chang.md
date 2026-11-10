---
declaration: section
origin: cited
lean: Stacks.Duality.torIndependentTwistedInverseImageBaseChange_restrict_comm, Stacks.Duality.torIndependentTwistedInverseImageBaseChangeRestrictArrowIso, Stacks.Duality.isIso_twistedInverseImageBaseChangeMap_app_of_finiteTorDimension, Stacks.Duality.isIso_twistedInverseImageBaseChangeMap_app_of_flat, Stacks.Duality.isIso_twistedInverseImageBaseChangeMap_app_of_perfect
statement: formalized
proof: formalized
---

# 48.6 Right adjoint of pushforward and base change, II

Section 48.6 of the Stacks Project, [Tag 0BZF](https://stacks.math.columbia.edu/tag/0BZF). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E9S, a remark

[Tag 0E9S](https://stacks.math.columbia.edu/tag/0E9S) in the Stacks Project.

**`Stacks.Duality.torIndependentTwistedInverseImageBaseChange_restrict_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/TorIndependentBaseChangeRestriction.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/TorIndependentBaseChangeRestriction.lean#L243). The attribute's comment: “the commutative square of maps exhibiting the isomorphism: the two maps of 0A9L and the identifications of restriction with derived pullback carry the restriction to U' of the base change map 0AA6 to that of the square of opens”.

> **The restriction of the base change map to `U'`, as a commutative square.** For a Tor
> independent cartesian square of quasi-compact quasi-separated schemes and quasi-compact opens
> `V ⊆ Y`, `V' ⊆ Y'` with `g(V') ⊆ V`, write `γ` for the base change map of [Stacks, Tag 0AA6],
> `γ_V` for that of the square of opens `U' ⟶ U` over `V' ⟶ V`, and `ρ`, `ρ'` for the maps of
> [Stacks, Tag 0A9L] for `U ⊆ X` over `V ⊆ Y` and `U' ⊆ X'` over `V' ⊆ Y'`. Then
> ```
> γ(K)|_{U'} ≫ ρ'(Lg^* K) ≫ a_{U'}((Lg^*K)|_{V'} ≅ L(g|)^*(K|_V))
>   = ((L(g')^* a(K))|_{U'} ≅ L(g'|)^*(a(K)|_U)) ≫ L(g'|)^* ρ(K) ≫ γ_V(K|_V).
> ```

```lean
theorem torIndependentTwistedInverseImageBaseChange_restrict_comm
    (K : quasiCoherentDerivedCategory Y) :
    Rs[(f' ⁻¹ᵁ V').ι].map ((torIndependentTwistedInverseImageBaseChange sq hTor).app K) ≫
        (qcqsTwistedInverseImageRestrictionMap f' V').app (Lq[g].obj K) ≫
        a[f' ∣_ V'].map ((quasiCoherentDerivedRestrictPullbackIso V.ι V'.ι (g.resLE V V' hVV') g
          (Scheme.Hom.resLE_comp_ι g hVV').symm).hom.app K) =
      (quasiCoherentDerivedRestrictPullbackIso (f ⁻¹ᵁ V).ι (f' ⁻¹ᵁ V').ι
          (g'.resLE (f ⁻¹ᵁ V) (f' ⁻¹ᵁ V')
            (preimage_le_of_comm sq.w hVV')) g'
          (Scheme.Hom.resLE_comp_ι g'
            (preimage_le_of_comm sq.w hVV')).symm).hom.app
          (a[f].obj K) ≫
        Lq[g'.resLE (f ⁻¹ᵁ V) (f' ⁻¹ᵁ V')
            (preimage_le_of_comm sq.w hVV')].map
          ((qcqsTwistedInverseImageRestrictionMap f V).app K) ≫
        (torIndependentTwistedInverseImageBaseChange (isPullback_restrictBasesSquare sq V hVV')
          (torIndependent_morphismRestrict_resLE f g hTor hVV')).app (Rs[V.ι].obj K)
```

**`Stacks.Duality.torIndependentTwistedInverseImageBaseChangeRestrictArrowIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/TorIndependentBaseChangeRestriction.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/TorIndependentBaseChangeRestriction.lean#L320).

> **[Stacks, Tag 0E9S].** Consider a cartesian square of quasi-compact and quasi-separated
> schemes
> ```
> X' --g'--> X
> |          |
> f'         f
> v          v
> Y' --g---> Y
> ```
> with `f` and `g` Tor independent, and quasi-compact (for instance affine) opens `V ⊆ Y`,
> `V' ⊆ Y'` with `g(V') ⊆ V`; set `U = f⁻¹(V)`, `U' = (f')⁻¹(V')`. Assume that the map of
> [Stacks, Tag 0A9L] for `U ⊆ X` over `V ⊆ Y` is an isomorphism at `K`, and that for `U' ⊆ X'` over
> `V' ⊆ Y'` it is an isomorphism at `Lg^* K`. Then the restriction to `U'` of the base change map
> `L(g')^* a(K) ⟶ a'(Lg^* K)` of [Stacks, Tag 0AA6] is isomorphic, as an arrow, to the base change
> map of Tag 0AA6 for `K|_V` and the cartesian square `U' ⟶ U` over `V' ⟶ V`
> (`Stacks.AlgebraicGeometry.FlatBaseChangeCohomology.isPullback_restrictBasesSquare`, Tor
> independent by `AlgebraicGeometry.torIndependent_morphismRestrict_resLE`). The two components are
> the two maps of Tag 0A9L composed with the identifications of restriction and derived pullback;
> the square commutes by
> `Stacks.Duality.torIndependentTwistedInverseImageBaseChange_restrict_comm`.

```lean
def torIndependentTwistedInverseImageBaseChangeRestrictArrowIso
    (K : quasiCoherentDerivedCategory Y)
    [IsIso ((qcqsTwistedInverseImageRestrictionMap f V).app K)]
    [IsIso ((qcqsTwistedInverseImageRestrictionMap f' V').app (Lq[g].obj K))] :
    Arrow.mk (Rs[(f' ⁻¹ᵁ V').ι].map ((torIndependentTwistedInverseImageBaseChange sq hTor).app K)) ≅
      Arrow.mk ((torIndependentTwistedInverseImageBaseChange
        (isPullback_restrictBasesSquare sq V hVV')
          (torIndependent_morphismRestrict_resLE f g hTor hVV')).app
          (Rs[V.ι].obj K))
```

## Tag 0AA8, a lemma

[Tag 0AA8](https://stacks.math.columbia.edu/tag/0AA8) in the Stacks Project.

**`Stacks.Duality.isIso_twistedInverseImageBaseChangeMap_app_of_finiteTorDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/AffineBaseChangeFiniteTorDimension.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/AffineBaseChangeFiniteTorDimension.lean#L202). The attribute's comment: “(3)”.

> **[Stacks, Tag 0AA8] part (3).** In a cartesian square of quasi-compact and quasi-separated
> schemes, let `g : Y' ⟶ Y` be a morphism of affine schemes, `f : X ⟶ Y` proper, and `f`, `g` Tor
> independent. If `g` has finite Tor dimension and `Y` is Noetherian, the base change map
> `L(g')^* a(K) ⟶ a'(Lg^*K)` of [Stacks, Tag 0AA6] is an isomorphism for every
> `K ∈ D^+_QCoh(𝒪_Y)`.
>
> For a morphism of affine schemes, having finite Tor dimension means that `Γ(Y', 𝒪)` has finite
> Tor dimension as a `Γ(Y, 𝒪)`-module (`AlgebraicGeometry.HasFiniteTorDimensionRingHom` of the map
> on global sections): the stalks `𝒪_{Y', y'}` then have Tor dimension bounded uniformly over
> `𝒪_{Y, g(y')}`, which is the definition of a morphism of finite Tor dimension; finite Tor
> dimension of each stalk separately, without a uniform bound, is weaker.

```lean
theorem isIso_twistedInverseImageBaseChangeMap_app_of_finiteTorDimension
    (sq : IsPullback g' f' f g) [IsAffine Y] [IsAffine Y'] [IsProper f] [IsNoetherian Y]
    (hTor : TorIndependent f g) (hg : HasFiniteTorDimensionRingHom g.appTop.hom)
    (K : quasiCoherentDerivedCategory Y) (hK : DerivedCategoryB.IsBoundedBelow K.obj) :
    haveI := isIso_twistedInverseImagePushforwardBaseChange_of_torIndependent sq hTor
    IsIso ((twistedInverseImageBaseChangeMap g' f' f g
      (isQuasicoherent_homology_derivedPushforward_of_qcqs g')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs g)
      sq).app K)
```

**`Stacks.Duality.isIso_twistedInverseImageBaseChangeMap_app_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/AffineBaseChangeFlat.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/AffineBaseChangeFlat.lean#L37). The attribute's comment: “(1)”.

> In a cartesian square of quasi-compact and quasi-separated schemes, let `g : Y' ⟶ Y` be a
> morphism of affine schemes, `f : X ⟶ Y` proper, and `f`, `g` Tor independent. If `f` is flat and
> of finite presentation, the base change map `L(g')^* a(K) ⟶ a'(Lg^*K)` of [Stacks, Tag 0AA6] is an
> isomorphism for every `K ∈ D_QCoh(𝒪_Y)`.

```lean
theorem isIso_twistedInverseImageBaseChangeMap_app_of_flat (sq : IsPullback g' f' f g)
    [IsAffine Y] [IsAffine Y'] [IsProper f] [Flat f] [LocallyOfFinitePresentation f]
    (hTor : TorIndependent f g) (K : quasiCoherentDerivedCategory Y) :
    haveI := isIso_twistedInverseImagePushforwardBaseChange_of_torIndependent sq hTor
    IsIso ((twistedInverseImageBaseChangeMap g' f' f g
      (isQuasicoherent_homology_derivedPushforward_of_qcqs g')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs g)
      sq).app K)
```

Declarations registered for the tag:

- [`Stacks.Duality.isIso_twistedInverseImageBaseChangeMap_app_of_perfect`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/AffineBaseChangePerfect.lean#L43), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/AffineBaseChangePerfectRegistration.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/AffineBaseChangePerfectRegistration.lean#L17) (StacksFrontier): “(2)”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.6, Tag 0BZF](https://stacks.math.columbia.edu/tag/0BZF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
