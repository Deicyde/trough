---
declaration: section
origin: cited
lean: InfinitesimalLifting.infinitesimal_lifting_criterion_for_smoothness, AlgebraicGeometry.smooth_iff_lifts_finiteType_smallExtensions, AlgebraicGeometry.smoothAt_of_smooth_infinitesimalNeighbourhoods, AlgebraicGeometry.etaleAt_of_etale_infinitesimalNeighbourhoods, AlgebraicGeometry.isFlatAt_of_flat_infinitesimalNeighbourhoods
statement: formalized
proof: formalized
---

# 37.12 Smoothness over a Noetherian base

Section 37.12 of the Stacks Project, [Tag 02HW](https://stacks.math.columbia.edu/tag/02HW). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02HX, a lemma

[Tag 02HX](https://stacks.math.columbia.edu/tag/02HX) in the Stacks Project.

Declarations registered for the tag:

- [`InfinitesimalLifting.infinitesimal_lifting_criterion_for_smoothness`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Smooth/InfinitesimalLifting.lean#L2699), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/SmoothnessOverNoetherianBase.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/SmoothnessOverNoetherianBase.lean#L49) (StacksFrontier).

## Tag 02HY, a lemma

[Tag 02HY](https://stacks.math.columbia.edu/tag/02HY) in the Stacks Project.

**`AlgebraicGeometry.smooth_iff_lifts_finiteType_smallExtensions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/SmoothnessOverNoetherianBase.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/SmoothnessOverNoetherianBase.lean#L172). References: EGA IV (17.5.4); SGA 1 III (3.1), “(i)<=>(iii), Noetherian”.

> A locally finite type morphism to a locally Noetherian scheme
> is smooth exactly when it lifts against all Artinian small extensions whose map to the base is
> of finite type.

```lean
public theorem smooth_iff_lifts_finiteType_smallExtensions
    {X S : Scheme.{u}} (f : X ⟶ S)
    [IsLocallyNoetherian S] [LocallyOfFiniteType f] :
    Smooth f ↔
      ∀ ⦃B' B : CommRingCat.{u}⦄ (φ : B' ⟶ B),
        InfinitesimalLifting.IsSmallExtension φ →
        ∀ (α : Spec B ⟶ X) (β : Spec B' ⟶ S),
          (LocallyOfFiniteType β ∧ QuasiCompact β) →
          α ≫ f = Spec.map φ ≫ β →
          ∃ γ : Spec B' ⟶ X, Spec.map φ ≫ γ = α ∧ γ ≫ f = β
```

## Tag 0A43, a lemma

[Tag 0A43](https://stacks.math.columbia.edu/tag/0A43) in the Stacks Project.

**`AlgebraicGeometry.smoothAt_of_smooth_infinitesimalNeighbourhoods`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/SmoothnessOverNoetherianBase.lean, line 339](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/SmoothnessOverNoetherianBase.lean#L339). The attribute's comment: “smooth”.

> Let `f : X ⟶ S` be a morphism locally of finite type to a locally Noetherian scheme and let
> `i : Z ⟶ S` be a closed subscheme. If the base change `Xₙ = Zₙ ×_S X ⟶ Zₙ` of `f` to the `n`th
> infinitesimal neighbourhood of `Z` is smooth for every `n`, then `f` is smooth at every point of
> `f⁻¹(Z)`.

```lean
public theorem smoothAt_of_smooth_infinitesimalNeighbourhoods
    {X S Z : Scheme.{u}} [IsLocallyNoetherian S]
    (f : X ⟶ S) (i : Z ⟶ S) [LocallyOfFiniteType f] [IsClosedImmersion i]
    (hsmooth : ∀ n : ℕ, Smooth (pullback.snd f (Stacks.Thickenings.nthOrderToBase i n)))
    (x : X) (hx : f x ∈ Set.range i) :
    InfinitesimalLifting.SmoothAt f x
```

**`AlgebraicGeometry.etaleAt_of_etale_infinitesimalNeighbourhoods`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/SmoothnessOverNoetherianBase.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/SmoothnessOverNoetherianBase.lean#L386). The attribute's comment: “etale”.

> Let `f : X ⟶ S` be a morphism locally of finite type to a locally Noetherian scheme and let
> `i : Z ⟶ S` be a closed subscheme. If the base change `Xₙ = Zₙ ×_S X ⟶ Zₙ` of `f` to the `n`th
> infinitesimal neighbourhood of `Z` is étale for every `n`, then `f` is étale at every point of
> `f⁻¹(Z)`.

```lean
public theorem etaleAt_of_etale_infinitesimalNeighbourhoods
    {X S Z : Scheme.{u}} [IsLocallyNoetherian S]
    (f : X ⟶ S) (i : Z ⟶ S) [LocallyOfFiniteType f] [IsClosedImmersion i]
    (hetale : ∀ n : ℕ, Etale (pullback.snd f (Stacks.Thickenings.nthOrderToBase i n)))
    (x : X) (hx : f x ∈ Set.range i) :
    EtaleAt f x
```

## Tag 0D4G, a lemma

[Tag 0D4G](https://stacks.math.columbia.edu/tag/0D4G) in the Stacks Project.

**`AlgebraicGeometry.isFlatAt_of_flat_infinitesimalNeighbourhoods`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalNeighbourhood/Flatness.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalNeighbourhood/Flatness.lean#L380).

> Flatness over a closed subscheme can be checked on every infinitesimal
> neighbourhood of that subscheme when the schemes are locally Noetherian.

```lean
theorem isFlatAt_of_flat_infinitesimalNeighbourhoods
    {X S Z : Scheme.{u}} [IsLocallyNoetherian X] [IsLocallyNoetherian S]
    (f : X ⟶ S) (i : Z ⟶ S) [IsClosedImmersion i]
    (hflat : ∀ n : ℕ, Flat (pullback.snd f (Stacks.Thickenings.nthOrderToBase i n)))
    (x : X) (hx : f x ∈ Set.range i) :
    IsFlatAt f.toLRSHom.toShHom x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.12, Tag 02HW](https://stacks.math.columbia.edu/tag/02HW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
