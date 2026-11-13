---
declaration: section
origin: cited
lean: Stacks.Duality.ExactSupportBaseChange.baseChangeSheafHomExactSupportMap, RingedSpaceModuleAdjunction.ClosedQuotientBaseChange.isIso_rightAdjointBaseChangeMap_iff_of_eq, RingedSpaceModuleAdjunction.ClosedQuotientBaseChange.isIso_rightAdjointBaseChangeMap_iff, Stacks.Duality.ExactSupportBaseChange.isIso_baseChangeSheafHomExactSupportMap_app_iff_isIso_derivedPullbackSheafHomMap, Stacks.Duality.ExactSupportBaseChange.isIso_baseChangeSheafHomExactSupportMap_app_iff_isIso_derivedPullbackSheafHomMap_comp, Stacks.Duality.ExactSupportBaseChange.baseChangeSheafHomExactSupport_isIso_of_flat_pseudoCoherent, Stacks.Duality.ExactSupportBaseChange.baseChangeSheafHomExactSupportMap_isIso_of_flat_pseudoCoherent, Stacks.Duality.TensorHomTorAmplitude.isIso_tensorDerivedSheafHomModelMap_of_closedImmersion
statement: formalized
proof: formalized
---

# 48.10 Right adjoint of pushforward for closed immersions and base change

Section 48.10 of the Stacks Project, [Tag 0E2J](https://stacks.math.columbia.edu/tag/0E2J). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E2K, an equation

[Tag 0E2K](https://stacks.math.columbia.edu/tag/0E2K) in the Stacks Project.

**`Stacks.Duality.ExactSupportBaseChange.baseChangeSheafHomExactSupportMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportFlatBaseChangeMap.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportFlatBaseChangeMap.lean#L158). The attribute's comment: “the canonical base change map (48.10.0.1), functorial in K, for a cartesian square with i a closed immersion and Z, X' Tor independent over X”.

> **Stacks Project, Tag 0E2K.** The canonical base-change map
>
> `Lg^* R ℰom(𝒪_Z, K) ⟶ R ℰom(𝒪_{Z'}, Lf^*K)`
>
> in `D(𝒪_{Z'})`, functorial in `K ∈ D(𝒪_X)`, for a cartesian square whose right-hand column `i`
> is a closed immersion and whose corners `Z`, `X'` are Tor independent over `X`.
>
> Its component at `K` corresponds, under the adjunction `Ri'_* ⊣ R ℰom(𝒪_{Z'}, -)` of
> [Stacks, Tag 0A76] on the left-hand column, to the composite
>
> `Ri'_* Lg^* R ℰom(𝒪_Z, K) = Lf^* Ri_* R ℰom(𝒪_Z, K) ⟶ Lf^*K`
>
> whose equality is the Tor-independent base-change isomorphism of [Stacks, Tag 0E23]
> (`pushforwardBaseChangeIso`), and whose arrow is `Lf^*` of the counit of [Stacks, Tag 0A76];
> `baseChangeSheafHomExactSupportMap_app` spells this out.

```lean
def baseChangeSheafHomExactSupportMap (sq : IsPullback i' g f i) [IsClosedImmersion i]
    (htor : AlgebraicGeometry.TorIndependent i f) :
    (closedQuotientOfClosedImmersion i).derivedSheafHomExactSupport ⋙
        derivedPullback g.toLRSHom.toShHom ⟶
      derivedPullback f.toLRSHom.toShHom ⋙
        (closedQuotientOfBaseChange sq).derivedSheafHomExactSupport
```

## Tag 0E2L, a lemma

[Tag 0E2L](https://stacks.math.columbia.edu/tag/0E2L) in the Stacks Project.

**`RingedSpaceModuleAdjunction.ClosedQuotientBaseChange.isIso_rightAdjointBaseChangeMap_iff_of_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportBaseChange.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportBaseChange.lean#L201). The attribute's comment: “both directions, for a base change map filling the pushforward square; its identification with the map of Cohomology, Remark 08I3, which the source omits, is the hypothesis `hψ`, and the base change isomorphism `Ri'_* ∘ Lg^* ≅ Lf^* ∘ Ri_*` of Stacks 0E23 is the named hypothesis `e`”.

> **Stacks Project, Tag 0E2L.** The map `Lg^* R ℰom(𝒪_Z, K) ⟶ R ℰom(𝒪_{Z'}, Lf^*K)` of
> [Stacks, Tag 0E2K] is an isomorphism if and only if a base change map
> `ψ : Lf^* R SheafHom_{𝒪_X}(𝒪_Z, K) ⟶ R SheafHom_{𝒪_{X'}}(𝒪_{Z'}, Lf^*K)` whose pushforward
> square it fills is an isomorphism.
>
> Both directions: `Ri'_*` carries isomorphisms to isomorphisms, and it reflects them, being
> exact and fully faithful.

```lean
theorem isIso_rightAdjointBaseChangeMap_iff_of_eq
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing S.X)))
    (ψ : Lf.obj (S.derivedHomSheafFromPushforwardStructureSheaf.obj K) ⟶
      S'.derivedHomSheafFromPushforwardStructureSheaf.obj (Lf.obj K))
    (hψ : (modulePushforward S'.i).mapDerivedCategory.map
        (rightAdjointBaseChangeMap S S' Lf Lg e K) =
      (pushforwardSourceIso S S' Lf Lg e K).hom ≫ ψ ≫
        (pushforwardTargetIso S S' Lf K).inv) :
    IsIso (rightAdjointBaseChangeMap S S' Lf Lg e K) ↔ IsIso ψ
```

**`RingedSpaceModuleAdjunction.ClosedQuotientBaseChange.isIso_rightAdjointBaseChangeMap_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportBaseChange.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportBaseChange.lean#L219). The attribute's comment: “both directions, for the base change map induced by Stacks 0E2K; the base change isomorphism `Ri'_* ∘ Lg^* ≅ Lf^* ∘ Ri_*` of Stacks 0E23 is the named hypothesis `e`”.

> **Stacks Project, Tag 0E2L.** The map `Lg^* R ℰom(𝒪_Z, K) ⟶ R ℰom(𝒪_{Z'}, Lf^*K)` of
> [Stacks, Tag 0E2K] is an isomorphism if and only if the base change map
> `Lf^* R SheafHom_{𝒪_X}(𝒪_Z, K) ⟶ R SheafHom_{𝒪_{X'}}(𝒪_{Z'}, Lf^*K)` it induces is an
> isomorphism.

```lean
theorem isIso_rightAdjointBaseChangeMap_iff
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing S.X))) :
    IsIso (rightAdjointBaseChangeMap S S' Lf Lg e K) ↔
      IsIso (derivedSheafHomBaseChangeMap S S' Lf Lg e K)
```

**`Stacks.Duality.ExactSupportBaseChange.isIso_baseChangeSheafHomExactSupportMap_app_iff_isIso_derivedPullbackSheafHomMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportBaseChangeInternalHom.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportBaseChangeInternalHom.lean#L250).

> **Stacks Project, Tag 0E2L.** Consider a cartesian square of schemes
>
> ```
> Z' --i'--> X'
> |g         |f
> Z --i----> X
> ```
>
> with `i` a closed immersion and `Z`, `X'` Tor independent over `X`, and `K ∈ D(𝒪_X)`. The base
> change map `Lg^* R ℰom(𝒪_Z, K) ⟶ R ℰom(𝒪_{Z'}, Lf^*K)` of [Stacks, Tag 0E2K] is an isomorphism
> if and only if the base change map
>
> `Lf^* R SheafHom_{𝒪_X}(𝒪_Z, K) ⟶ R SheafHom_{𝒪_{X'}}(Lf^*𝒪_Z, Lf^*K)`
>
> of Cohomology, Remark [Stacks, Tag 08I3] is an isomorphism, `𝒪_Z` standing for `Ri_*𝒪_Z[0]`.
> The source writes the target as `R SheafHom_{𝒪_{X'}}(𝒪_{Z'}, Lf^*K)`, through
> `𝒪_{Z'} = Lf^*𝒪_Z` (Tor independence); the map of [Stacks, Tag 08I3] has `Lf^*𝒪_Z` there, and
> that is the map stated here.
>
> The source proves this by applying `Ri'_*` and omits the verification that the result is the map
> of [Stacks, Tag 08I3]. Here that verification is
> `isIso_mate_iff_isIso_homComparison_of_projection`: both maps are read off the projection formula
> of [Stacks, Tag 0B55] in its right-handed form, whose compatibility with base change is the
> right-handed [Stacks, Tag 0B6B].

```lean
theorem isIso_baseChangeSheafHomExactSupportMap_app_iff_isIso_derivedPullbackSheafHomMap
    (sq : IsPullback i' g f i) [IsClosedImmersion i]
    (htor : AlgebraicGeometry.TorIndependent i f) :
    IsIso ((baseChangeSheafHomExactSupportMap sq htor).app K) ↔
      IsIso (derivedPullbackSheafHomMap f.toLRSHom.toShHom
        ((derivedPushforward i.toLRSHom.toShHom).obj (unitObject Z.toSheafedSpace)) K)
```

**`Stacks.Duality.ExactSupportBaseChange.isIso_baseChangeSheafHomExactSupportMap_app_iff_isIso_derivedPullbackSheafHomMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportBaseChangeInternalHom.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportBaseChangeInternalHom.lean#L365). The attribute's comment: “the same statement, with the target written R SheafHom(O\_\{Z'}, Lf^*K) through the identification O\_\{Z'} = Lf^*O\_Z of Tor independence, as the source writes it”.

> **Stacks Project, Tag 0E2L**, with the target written as the source writes it. In the
> situation of
> `isIso_baseChangeSheafHomExactSupportMap_app_iff_isIso_derivedPullbackSheafHomMap`, the map of
> [Stacks, Tag 0E2K] is an isomorphism if and only if the base change map
>
> `Lf^* R SheafHom_{𝒪_X}(𝒪_Z, K) ⟶ R SheafHom_{𝒪_{X'}}(Lf^*𝒪_Z, Lf^*K)`
> `= R SheafHom_{𝒪_{X'}}(𝒪_{Z'}, Lf^*K)`
>
> of Cohomology, Remark [Stacks, Tag 08I3] is, the equality being the identification
> `pushforwardStructureSheafBaseChangeIso` of `𝒪_{Z'}` with `Lf^*𝒪_Z` by Tor independence.

```lean
theorem isIso_baseChangeSheafHomExactSupportMap_app_iff_isIso_derivedPullbackSheafHomMap_comp
    (sq : IsPullback i' g f i) [IsClosedImmersion i]
    (htor : AlgebraicGeometry.TorIndependent i f) :
    IsIso ((baseChangeSheafHomExactSupportMap sq htor).app K) ↔
      IsIso (derivedPullbackSheafHomMap f.toLRSHom.toShHom
          ((derivedPushforward i.toLRSHom.toShHom).obj (unitObject Z.toSheafedSpace)) K ≫
        ((Stacks.SheafOfModules.derivedSheafHom X'.toSheafedSpace.sheaf).map
          (pushforwardStructureSheafBaseChangeIso sq htor).hom.op).app
          ((derivedPullback f.toLRSHom.toShHom).obj K))
```

## Tag 0E2M, a lemma

[Tag 0E2M](https://stacks.math.columbia.edu/tag/0E2M) in the Stacks Project.

**`Stacks.Duality.ExactSupportBaseChange.baseChangeSheafHomExactSupport_isIso_of_flat_pseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportFlatBaseChange.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportFlatBaseChange.lean#L244). The attribute's comment: “only the reduction to invertibility after Ri'\_*; see the docstring”.

> **Stacks Project, Tag 0E2M, in part.** In the situation of [Stacks, Tag 0E2J] — a cartesian
> square whose right-hand column `i` is a closed immersion, with `Z` and `X'` Tor independent over
> `X` — assume `f` flat and `i` pseudo-coherent. Then the map of [Stacks, Tag 0E2K] is an
> isomorphism for `K` in `D⁺_QCoh(𝒪_X)`, which is `_hbb` together with `_hqc`.
>
> **What is assumed rather than derived.** The hypothesis `hpush` says the map is already
> invertible after derived pushforward along `i'`, and the proof is only the reduction
> `isIso_of_isIso_modulePushforward_map`, that is, the step "since `i'_*` is exact and faithful it
> suffices to show the map is an isomorphism after applying `Ri'_*`" of the source's proof of
> [Stacks, Tag 0E2L]. The flatness of `f`, the pseudo-coherence of `i`, the boundedness `_hbb`
> and the quasi-coherence `_hqc` are stated, so the statement is the tag's own and no hypothesis
> of it has been dropped or weakened, but they are not consumed: discharging `hpush` from them is
> precisely the remaining content of [Stacks, Tag 0E2M], and the module docstring names the three
> steps it takes.
>
> The attribute's clause string is deliberately narrow, and it is worth being explicit about why.
> Read as an implication this statement is close to circular: `hpush` is invertibility of the map
> after `Ri'_*`, the proof is conservativity of `Ri'_*`, and that conservativity is exactly what
> makes `hpush` and the conclusion interchangeable. What the clause claims is therefore not that
> the map is invertible — the tag's assertion, which is **not** proved here — but only that the
> source's reduction step for [Stacks, Tag 0E2L], "since `i'_*` is exact and faithful it suffices
> to show the map is an isomorphism after applying `Ri'_*`", is available in this library.

```lean
theorem baseChangeSheafHomExactSupport_isIso_of_flat_pseudoCoherent
    (sq : IsPullback i' g f i) [IsClosedImmersion i] [AlgebraicGeometry.Flat f]
    [AlgebraicGeometry.PseudoCoherent i]
    (htor : AlgebraicGeometry.TorIndependent i f) (hst : DerivedStalkBaseChangeEqKFlat sq)
    (K : DerivedCategory
      (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)))
    (_hbb : DerivedCategoryB.IsBoundedBelow K)
    (_hqc : @Stacks.DerivedQCoh.IsDQCoh _ _ _
      (structureSheafRing X.toRingedSpace) _ _ _ _ _ K)
    (hpush : IsIso ((modulePushforward (closedQuotientOfBaseChange sq).i).mapDerivedCategory.map
      (baseChangeSheafHomExactSupport sq htor hst K))) :
    IsIso (baseChangeSheafHomExactSupport sq htor hst K)
```

**`Stacks.Duality.ExactSupportBaseChange.baseChangeSheafHomExactSupportMap_isIso_of_flat_pseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportFlatBaseChangeIso.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportFlatBaseChangeIso.lean#L191).

> **Stacks Project, Tag 0E2M.** Consider a cartesian square of schemes
>
> ```
> Z' --i'--> X'
> |g         |f
> Z --i----> X
> ```
>
> with `i` a closed immersion, and assume `f` is flat and `i` pseudo-coherent. Then the canonical
> base change map of [Stacks, Tag 0E2K]
>
> `Lg^* R ℰom(𝒪_Z, K) ⟶ R ℰom(𝒪_{Z'}, Lf^*K)`
>
> is an isomorphism for `K` in `D⁺_QCoh(𝒪_X)`, which is `hbb` together with `_hqc`.
>
> The Tor independence of `Z` and `X'` over `X` that the map is built from is not a hypothesis: it
> is supplied by the flatness of `f`, `AlgebraicGeometry.torIndependent_of_flat_right`. The proof
> uses only that `K` is bounded below, as the footnote to the source's second proof records;
> `isIso_baseChangeSheafHomExactSupportMap_app_of_flat_of_isBoundedBelow` is that statement.

```lean
theorem baseChangeSheafHomExactSupportMap_isIso_of_flat_pseudoCoherent
    (sq : IsPullback i' g f i) [IsClosedImmersion i] [AlgebraicGeometry.Flat f]
    [PseudoCoherent i]
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)))
    (hbb : DerivedCategoryB.IsBoundedBelow K)
    (_hqc : @Stacks.DerivedQCoh.IsDQCoh _ _ _
      (structureSheafRing X.toRingedSpace) _ _ _ _ _ K) :
    IsIso ((baseChangeSheafHomExactSupportMap sq
      (AlgebraicGeometry.torIndependent_of_flat_right i f)).app K)
```

## Tag 0E2N, a lemma

[Tag 0E2N](https://stacks.math.columbia.edu/tag/0E2N) in the Stacks Project.

**`Stacks.Duality.TensorHomTorAmplitude.isIso_tensorDerivedSheafHomModelMap_of_closedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/TensorHomTorAmplitudeModel.lean, line 449](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/TensorHomTorAmplitudeModel.lean#L449). The attribute's comment: “the canonical map is `tensorDerivedSheafHomModelMap`: on a K-injective model `I` of `K` and a K-flat model `A` of `M` it is the class of the morphism of complexes whose pushforward is the inverse projection formula followed by the interchange of 0BYR, `phi (x) a |-> (s |-> phi(s) (x) a)`, that is the counit `Ri_* R Hom(O_Z, K) -> K` tensored with `M`; the quasi-coherence of `K` and `M` is part of the statement and is not used”.

> **[Stacks, Tag 0E2N].** Let `i : Z ⟶ X` be a pseudo-coherent closed immersion of schemes, let
> `M ∈ D_QCoh(𝒪_X)` locally have Tor amplitude in `[a, ∞)` and let `K ∈ D⁺_QCoh(𝒪_X)`. Then the
> canonical map
>
> `R ℰom(𝒪_Z, K) ⊗^L_{𝒪_Z} Li^*M ⟶ R ℰom(𝒪_Z, K ⊗^L_{𝒪_X} M)`
>
> is an isomorphism in `D(𝒪_Z)`. The quasi-coherence hypotheses on `K` and `M` are part of the
> statement and are not used.

```lean
theorem isIso_tensorDerivedSheafHomModelMap_of_closedImmersion {Z X : Scheme.{u}} (i : Z ⟶ X)
    [IsClosedImmersion i] (hi : AlgebraicGeometry.PseudoCoherent i)
    (K M : DerivedCategory (SheafOfModules.{u}
        (structureSheafRing X.toRingedSpace))) (a : ℤ)
    (_hMq : @Stacks.DerivedQCoh.IsDQCoh _ _ _
        (structureSheafRing X.toRingedSpace) _ _ _ _ _ M)
    (hM : Stacks.Cohomology.TorAmplitude.LocallyHasTorAmplitudeGE X.toRingedSpace M a)
    (hK : DerivedCategoryB.IsBoundedBelow K)
    (_hKq : @Stacks.DerivedQCoh.IsDQCoh _ _ _
        (structureSheafRing X.toRingedSpace) _ _ _ _ _ K) :
    IsIso (tensorDerivedSheafHomModelMap
      (Stacks.ClosedImmersion.closedQuotientOfClosedImmersion i) K M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.10, Tag 0E2J](https://stacks.math.columbia.edu/tag/0E2J)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
