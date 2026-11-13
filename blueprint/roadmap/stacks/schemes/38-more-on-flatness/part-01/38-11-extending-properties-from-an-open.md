---
declaration: section
origin: cited
lean: AlgebraicGeometry.FinitePresentationFromDenseOpen.isFinitePresentation_of_isFlatOver_of_retrocompact_dense_open, AlgebraicGeometry.FinitePresentationFromDenseOpen.locallyOfFinitePresentation_of_flat_of_retrocompact_dense_open, AlgebraicGeometry.relativeDimensionLE_of_dense_open, AlgebraicGeometry.isFinite_of_isFinite_over_dense_open, AlgebraicGeometry.isOpenImmersion_of_isIso_morphismRestrict
statement: formalized
proof: formalized
---

# 38.11 Extending properties from an open

Section 38.11 of the Stacks Project, [Tag 0B47](https://stacks.math.columbia.edu/tag/0B47). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 081N, a lemma

[Tag 081N](https://stacks.math.columbia.edu/tag/081N) in the Stacks Project.

**`AlgebraicGeometry.FinitePresentationFromDenseOpen.isFinitePresentation_of_isFlatOver_of_retrocompact_dense_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/FinitePresentationFromDenseOpen.lean, line 710](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/FinitePresentationFromDenseOpen.lean#L710).

> **Stacks Project, Tag 081N.** A quasi-coherent module of finite type, flat over the base,
> which is finitely presented over the inverse image of a retrocompact scheme-theoretically dense
> open of the base is finitely presented.

```lean
public theorem isFinitePresentation_of_isFlatOver_of_retrocompact_dense_open
    {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) [F.IsQuasicoherent]
    [LocallyOfFinitePresentation f] [F.IsFiniteType]
    (hflat : AlgebraicGeometry.IsFlatOver f.toLRSHom.toShHom F)
    (U : S.Opens) (hUretro : IsRetrocompact (U : Set S))
    (hUdense : AlgebraicGeometry.Scheme.Opens.IsSchemeTheoreticallyDense U)
    (hfp : ((Scheme.Modules.pullback (f ⁻¹ᵁ U).ι).obj F).IsFinitePresentation) :
    F.IsFinitePresentation
```

## Tag 081P, a lemma

[Tag 081P](https://stacks.math.columbia.edu/tag/081P) in the Stacks Project.

**`AlgebraicGeometry.FinitePresentationFromDenseOpen.locallyOfFinitePresentation_of_flat_of_retrocompact_dense_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/FinitePresentationFromDenseOpen.lean, line 861](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/FinitePresentationFromDenseOpen.lean#L861).

> **Stacks Project, Tag 081P.** A flat morphism of schemes which is locally of finite type,
> and which is locally of finite presentation over a retrocompact scheme-theoretically dense open
> of the target, is locally of finite presentation.

```lean
public theorem locallyOfFinitePresentation_of_flat_of_retrocompact_dense_open
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] [Flat f]
    (U : S.Opens) (hUretro : IsRetrocompact (U : Set S))
    (hUdense : Scheme.Opens.IsSchemeTheoreticallyDense U)
    [LocallyOfFinitePresentation (f ∣_ U)] :
    LocallyOfFinitePresentation f
```

## Tag 081L, a lemma

[Tag 081L](https://stacks.math.columbia.edu/tag/081L) in the Stacks Project.

**`AlgebraicGeometry.relativeDimensionLE_of_dense_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ExtendingFromOpen/RelativeDimension.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/ExtendingFromOpen/RelativeDimension.lean#L221).

> **Stacks Project, Tag 081L.** A relative-dimension bound for a flat morphism locally of finite
> type extends from a dense open of the base when the morphism is locally of finite presentation or
> the open is retrocompact.

```lean
theorem relativeDimensionLE_of_dense_open {X S : Scheme.{u}} (f : X ⟶ S)
    [Flat f] [LocallyOfFiniteType f] (U : S.Opens) (hU : Dense (U : Set S)) (e : ℕ)
    (hfe : RelativeDimensionLE (pullback.snd f U.ι) e)
    (hfin : LocallyOfFinitePresentation f ∨ IsRetrocompact (U : Set S)) :
    RelativeDimensionLE f e
```

## Tag 0B48, a lemma

[Tag 0B48](https://stacks.math.columbia.edu/tag/0B48) in the Stacks Project.

**`AlgebraicGeometry.isFinite_of_isFinite_over_dense_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ExtendingFromOpen/Finite.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/ExtendingFromOpen/Finite.lean#L45).

> A proper flat morphism which is finite over a dense open of the base is finite, provided it is
> locally of finite presentation or the open is retrocompact.

```lean
theorem isFinite_of_isFinite_over_dense_open {X S : Scheme.{u}} (f : X ⟶ S)
    [IsProper f] [Flat f] (U : S.Opens) (hU : Dense (U : Set S))
    [IsFinite (pullback.snd f U.ι)]
    (hfin : LocallyOfFinitePresentation f ∨ IsRetrocompact (U : Set S)) :
    IsFinite f
```

## Tag 081M, a lemma

[Tag 081M](https://stacks.math.columbia.edu/tag/081M) in the Stacks Project.

**`AlgebraicGeometry.isOpenImmersion_of_isIso_morphismRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ExtendingFromOpen/OpenImmersion.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/ExtendingFromOpen/OpenImmersion.lean#L154).

> **Stacks Project, Tag 081M.** A separated flat morphism locally of finite type which is an
> isomorphism over a retrocompact scheme-theoretically dense open subscheme of the target is an
> open immersion.

```lean
theorem isOpenImmersion_of_isIso_morphismRestrict {X S : Scheme.{u}} (f : X ⟶ S) [IsSeparated f]
    [LocallyOfFiniteType f] [Flat f] (U : S.Opens) (hUretro : IsRetrocompact (U : Set S))
    (hUdense : Scheme.Opens.IsSchemeTheoreticallyDense U)
    [IsIso (f ∣_ U)] : IsOpenImmersion f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.11, Tag 0B47](https://stacks.math.columbia.edu/tag/0B47)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
