---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.LiftsAt.mono, AlgebraicGeometry.Space.isSmoothAt_of_liftsAt_isSmallExtension, AlgebraicGeometry.Space.IsSmoothAt.liftsAt, AlgebraicGeometry.Space.tfae_isSmoothAt_liftsAt, AlgebraicGeometry.Space.not_forall_isSmooth_iff_liftsAgainstFiniteTypeSmallExtensions, AlgebraicGeometry.Space.IsSmooth.liftsAgainstFiniteTypeSmallExtensions, AlgebraicGeometry.Space.isSmooth_iff_forall_exists_lift_isSmallExtension, AlgebraicGeometry.Space.isSmoothAt_of_isSmooth_nthOrderInfinitesimalNeighbourhood
statement: formalized
proof: formalized
---

# 76.20 Smoothness over a Noetherian base

Section 76.20 of the Stacks Project, [Tag 0APM](https://stacks.math.columbia.edu/tag/0APM). 3 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0APN, a lemma

[Tag 0APN](https://stacks.math.columbia.edu/tag/0APN) in the Stacks Project.

**`AlgebraicGeometry.Space.LiftsAt.mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothAtInfinitesimalLifting.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothAtInfinitesimalLifting.lean#L331). The attribute's comment: “condition (2) implies condition (3)”.

> **Stacks 0APN, (2) implies (3).** The lifting property at a point against a class of
> extensions implies the lifting property against any subclass.

```lean
theorem LiftsAt.mono {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y}
    {x : points B S hS X}
    {extension extension' : ∀ ⦃R' R : CommRingCat.{u}⦄, (R' ⟶ R) → Prop}
    (hsub : ∀ ⦃R' R : CommRingCat.{u}⦄ (φ : R' ⟶ R), extension' φ → extension φ)
    (h : LiftsAt B S hS f x extension) :
    LiftsAt B S hS f x extension'
```

**`AlgebraicGeometry.Space.isSmoothAt_of_liftsAt_isSmallExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothAtInfinitesimalLifting.lean, line 752](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothAtInfinitesimalLifting.lean#L752). The attribute's comment: “condition (3) implies condition (1)”.

> **Stacks 0APN, (3) implies (1).** A morphism of algebraic spaces over `S` which is locally
> of finite type, whose target is locally Noetherian, and which has the lifting property at a
> point of its source against small extensions, is smooth at that point.
>
> A pointed étale chart at the point with locally Noetherian target chart receives every lifting
> problem for its morphism of charts along a residually trivial small extension, so Stacks 02HX
> makes that morphism of charts smooth at the chart point; smoothness at a point being an
> étale-local property of germs, Stacks 04NC reads that back as smoothness of the morphism at the
> point.

```lean
theorem isSmoothAt_of_liftsAt_isSmallExtension
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (x : points B S hS X)
    (hNoeth : HasEtaleLocalProperty B S hS Y (fun Z : Scheme.{u} => IsLocallyNoetherian Z))
    (hFiniteType : IsLocallyOfFiniteType B S hS f)
    (hlift : LiftsAt B S hS f x fun ⦃_ _⦄ φ => InfinitesimalLifting.IsSmallExtension φ) :
    IsSmoothAt B S hS f x
```

**`AlgebraicGeometry.Space.IsSmoothAt.liftsAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothAtLiftingCriterion.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothAtLiftingCriterion.lean#L98). The attribute's comment: “condition (1) implies conditions (2) and (3)”. References: SGA 3 XI (1.5), “partial”.

> **Stacks 0APN, (1) implies (2) and (3).** A morphism of algebraic spaces over `S` which is
> smooth at a point of its source has the lifting property at that point against every class of
> square-zero surjections of local rings.
>
> Smoothness at the point gives an open subspace of the source containing it on which the
> morphism is smooth, hence formally smooth by Stacks 04AM
> (`AlgebraicGeometry.Space.formallySmooth_of_isSmooth'`); the spectrum of a local ring whose
> closed point lies over the given point factors through that open subspace, because the closed
> point specializes from every point, so the lifting problem is a lifting problem for the
> restricted morphism.

```lean
theorem IsSmoothAt.liftsAt
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y} {x : points B S hS X}
    (hsm : IsSmoothAt B S hS f x)
    (extension : ∀ ⦃R' R : CommRingCat.{u}⦄, (R' ⟶ R) → Prop)
    (hextension : ∀ ⦃R' R : CommRingCat.{u}⦄ (φ : R' ⟶ R),
      extension φ → InfinitesimalLifting.IsSquareZeroSurjection φ) :
    LiftsAt B S hS f x extension
```

**`AlgebraicGeometry.Space.tfae_isSmoothAt_liftsAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothAtLiftingCriterion.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothAtLiftingCriterion.lean#L156). References: SGA 3 XI (1.5), “partial”.

> **Stacks 0APN.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is
> locally of finite type, with `Y` locally Noetherian, and let `x` be a point of `X`. Then the
> following are equivalent: `f` is smooth at `x`; every lifting problem at `x` along a surjection
> of local rings with square-zero kernel has a solution; every lifting problem at `x` along a
> small extension has a solution.
>
> The implication from (1) to (2) is `AlgebraicGeometry.Space.IsSmoothAt.liftsAt`, from (2) to
> (3) is `AlgebraicGeometry.Space.LiftsAt.mono` and from (3) to (1) is
> `AlgebraicGeometry.Space.isSmoothAt_of_liftsAt_isSmallExtension`.

```lean
theorem tfae_isSmoothAt_liftsAt
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (x : points B S hS X)
    (hNoeth : HasEtaleLocalProperty B S hS Y (fun Z : Scheme.{u} => IsLocallyNoetherian Z))
    (hFiniteType : IsLocallyOfFiniteType B S hS f) :
    [IsSmoothAt B S hS f x,
      LiftsAt B S hS f x fun ⦃_ _⦄ φ => InfinitesimalLifting.IsSquareZeroSurjection φ,
      LiftsAt B S hS f x fun ⦃_ _⦄ φ =>
        InfinitesimalLifting.IsSmallExtension φ].TFAE
```

## Tag 0APP, a lemma

[Tag 0APP](https://stacks.math.columbia.edu/tag/0APP) in the Stacks Project.

**`AlgebraicGeometry.Space.not_forall_isSmooth_iff_liftsAgainstFiniteTypeSmallExtensions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothnessFiniteTypeLiftingCounterexample.lean, line 444](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothnessFiniteTypeLiftingCounterexample.lean#L444). The attribute's comment: “the statement with the test morphism Spec B' ⟶ Y of finite type is false: the point Spec ℚ ⟶ 𝔸¹_ℚ/ℤ of the zero section satisfies that condition (2) and is not smooth. The corrected form, with Spec B' ⟶ Y locally of finite type, is isSmooth_iff_forall_exists_lift_isSmallExtension”.

> **Stacks 0APP, as stated, is false.** The equivalence of smoothness with condition (2) of
> Stacks 0APP, in which the test morphism `Spec B' ⟶ Y` is required to be of finite type, fails for
> some morphism of algebraic spaces locally of finite type over a locally Noetherian target: the
> point `Spec ℚ ⟶ 𝔸¹_ℚ/ℤ` of `exists_not_isSmooth_liftsAgainstFiniteTypeSmallExtensions` satisfies
> condition (2) and is not smooth.
>
> The implication from smoothness does hold, and is
> `AlgebraicGeometry.Space.IsSmooth.liftsAgainstFiniteTypeSmallExtensions`; the corrected
> equivalence, with the test morphism required only to be locally of finite type, is
> `AlgebraicGeometry.Space.isSmooth_iff_forall_exists_lift_isSmallExtension`.

```lean
theorem not_forall_isSmooth_iff_liftsAgainstFiniteTypeSmallExtensions :
    ¬ ∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
      (X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS X →
      IsAlgebraicSpace B S hS Y → ∀ f : X ⟶ Y,
      HasEtaleLocalProperty B S hS Y (fun Z : Scheme.{u} => IsLocallyNoetherian Z) →
      IsLocallyOfFiniteType B S hS f →
      (IsSmooth B S hS f ↔ LiftsAgainstFiniteTypeSmallExtensions B S hS f)
```

**`AlgebraicGeometry.Space.IsSmooth.liftsAgainstFiniteTypeSmallExtensions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothnessOverNoetherianBaseLifting.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothnessOverNoetherianBaseLifting.lean#L172). The attribute's comment: “(1) implies (2) as stated, with the test morphism Spec B' ⟶ Y of finite type”.

> **Stacks 0APP, (1) implies (2), as stated.** A smooth morphism of algebraic spaces
> satisfies condition (2) of Stacks 0APP with the test morphism of finite type. No hypothesis on
> the target is needed.

```lean
theorem IsSmooth.liftsAgainstFiniteTypeSmallExtensions
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hf : IsSmooth B S hS f) : LiftsAgainstFiniteTypeSmallExtensions B S hS f
```

**`AlgebraicGeometry.Space.isSmooth_iff_forall_exists_lift_isSmallExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothnessOverNoetherianBaseLifting.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothnessOverNoetherianBaseLifting.lean#L408). The attribute's comment: “corrected form: the test morphism Spec R' ⟶ Y is required to be locally of finite type. With it of finite type, as in the source, the statement is false: not_forall_isSmooth_iff_liftsAgainstFiniteTypeSmallExtensions”. References: SGA 1 III (3.1), “(iii), (iii)⇒(i)”.

> **Stacks 0APP.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is
> locally of finite type, with `Y` locally Noetherian. Then `f` is smooth if and only if every
> solid square whose vertical map is induced by a small extension `φ : R' ⟶ R` of Artinian local
> rings and whose map `Spec R' ⟶ Y` is locally of finite type admits a dotted arrow making the
> diagram commute.
>
> The implication towards the lifting property is the formal smoothness of a smooth morphism
> (Stacks 04AM). The converse runs the scheme-level criterion of Stacks 02HY on each commuting
> square of étale charts, pushing each scheme-level lifting problem into the algebraic spaces and
> pulling its solution back along the formally étale charts.
>
> The source asks the map `Spec R' ⟶ Y` to be of finite type; with that condition the
> equivalence is false, by
> `AlgebraicGeometry.Space.not_forall_isSmooth_iff_liftsAgainstFiniteTypeSmallExtensions`, so
> here the map is asked only to be locally of finite type. See the module documentation.

```lean
theorem isSmooth_iff_forall_exists_lift_isSmallExtension
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hNoeth : HasEtaleLocalProperty B S hS Y (fun Z : Scheme.{u} => IsLocallyNoetherian Z))
    (hFiniteType : IsLocallyOfFiniteType B S hS f) :
    IsSmooth B S hS f ↔
      ∀ ⦃R' R : CommRingCat.{u}⦄ (φ : R' ⟶ R),
        InfinitesimalLifting.IsSmallExtension φ →
        ∀ (T T' : BigFppfOver B S hS) (i : T ⟶ T')
          (e : (BigFppfOver.toScheme B S hS).obj T ≅ Spec R)
          (e' : (BigFppfOver.toScheme B S hS).obj T' ≅ Spec R'),
          (BigFppfOver.toScheme B S hS).map i = e.hom ≫ Spec.map φ ≫ e'.inv →
          ∀ (α : yoneda.obj T ⟶ X) (β : yoneda.obj T' ⟶ Y),
            IsLocallyOfFiniteType B S hS β →
            α ≫ f = yoneda.map i ≫ β →
            ∃ γ : yoneda.obj T' ⟶ X, yoneda.map i ≫ γ = α ∧ γ ≫ f = β
```

## Tag 0APQ, a lemma

[Tag 0APQ](https://stacks.math.columbia.edu/tag/0APQ) in the Stacks Project.

**`AlgebraicGeometry.Space.isSmoothAt_of_isSmooth_nthOrderInfinitesimalNeighbourhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothnessOnInfinitesimalNeighbourhoods.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothnessOnInfinitesimalNeighbourhoods.lean#L97). The attribute's comment: “part (1): smooth. Z is an arbitrary closed subspace and Zₙ its nth infinitesimal neighbourhood (Tag 05ZV), built on a surjective étale chart from the invariant ideal sheaf cutting out Z, which exists and is unique by exists_isInvariantIdealSheaf_invariantSubspace_eq and ker_rep_snd_eq_of_invariantSubspace_eq; Xₙ is any fibre product Zₙ ×_Y X”.

> **Stacks 0APQ, part (1).** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which
> is locally of finite type, with `Y` locally Noetherian. Let `Z ⊆ Y` be a closed subspace, cut out
> on a surjective étale chart `φ : U ⟶ Y` by the invariant sheaf of ideals `J`, so that its `n`th
> infinitesimal neighbourhood is `Zₙ = nthOrderInfinitesimalNeighbourhood φ J n`, and let
> `Xₙ = Zₙ ×_Y X`. If `Xₙ ⟶ Zₙ` is smooth for every `n`, then `f` is smooth at every point of
> `f⁻¹(Z)`.
>
> Every closed subspace is cut out on every surjective étale chart by exactly one invariant sheaf
> of ideals (`AlgebraicGeometry.Space.exists_isInvariantIdealSheaf_invariantSubspace_eq`), so this
> applies to every closed subspace of `Y`.

```lean
theorem isSmoothAt_of_isSmooth_nthOrderInfinitesimalNeighbourhood
    (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y.1)
    (hNoeth : HasEtaleLocalProperty B S hS Y.1 (fun W : Scheme.{u} => IsLocallyNoetherian W))
    (hFiniteType : IsLocallyOfFiniteType B S hS f)
    (Z : ClosedSubspaces B S hS Y.1)
    {J : ((BigFppfOver.toScheme B S hS).obj U).IdealSheafData}
    (hJ : IsInvariantIdealSheaf B S hS hs J)
    (hZJ : invariantSubspace B S hS φ (Subobject.mk J.subschemeι) = Z.1)
    (Xn : ℕ → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (fn : ∀ n, Xn n ⟶ (nthOrderInfinitesimalNeighbourhood B S hS φ J n).toFunctor)
    (pn : ∀ n, Xn n ⟶ X)
    (hcart : ∀ n, IsPullback (pn n) (fn n) f (nthOrderInfinitesimalNeighbourhood B S hS φ J n).ι)
    (hsmooth : ∀ n, IsSmooth B S hS (fn n))
    (x : points B S hS X)
    (hx : pointsMap B S hS X f x ∈ Set.range (pointsMap B S hS Z.1.toFunctor Z.1.ι)) :
    IsSmoothAt B S hS f x
```

**`AlgebraicGeometry.Space.isEtaleAt_of_isEtale_nthOrderInfinitesimalNeighbourhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothnessOnInfinitesimalNeighbourhoods.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothnessOnInfinitesimalNeighbourhoods.lean#L164). The attribute's comment: “part (2): étale. Z is an arbitrary closed subspace and Zₙ its nth infinitesimal neighbourhood (Tag 05ZV), built on a surjective étale chart from the invariant ideal sheaf cutting out Z, which exists and is unique by exists_isInvariantIdealSheaf_invariantSubspace_eq and ker_rep_snd_eq_of_invariantSubspace_eq; Xₙ is any fibre product Zₙ ×_Y X”.

> **Stacks 0APQ, part (2).** In the situation of
> `AlgebraicGeometry.Space.isSmoothAt_of_isSmooth_nthOrderInfinitesimalNeighbourhood`, if
> `Xₙ = Zₙ ×_Y X ⟶ Zₙ` is étale for every `n`, then `f` is étale at every point of `f⁻¹(Z)`.
>
> Étaleness of every base change gives smoothness of every base change, hence smoothness of `f`
> at the point by part (1). It also gives unramifiedness of the zeroth base change, hence
> unramifiedness of `f` at the point, which lies in the image of `X₀` because the zeroth square
> is cartesian. Stacks 02GK for algebraic spaces assembles the two.

```lean
theorem isEtaleAt_of_isEtale_nthOrderInfinitesimalNeighbourhood
    (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y.1)
    (hNoeth : HasEtaleLocalProperty B S hS Y.1 (fun W : Scheme.{u} => IsLocallyNoetherian W))
    (hFiniteType : IsLocallyOfFiniteType B S hS f)
    (Z : ClosedSubspaces B S hS Y.1)
    {J : ((BigFppfOver.toScheme B S hS).obj U).IdealSheafData}
    (hJ : IsInvariantIdealSheaf B S hS hs J)
    (hZJ : invariantSubspace B S hS φ (Subobject.mk J.subschemeι) = Z.1)
    (Xn : ℕ → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (fn : ∀ n, Xn n ⟶ (nthOrderInfinitesimalNeighbourhood B S hS φ J n).toFunctor)
    (pn : ∀ n, Xn n ⟶ X)
    (hcart : ∀ n, IsPullback (pn n) (fn n) f (nthOrderInfinitesimalNeighbourhood B S hS φ J n).ι)
    (hetale : ∀ n, IsEtale B S hS (fn n))
    (x : points B S hS X)
    (hx : pointsMap B S hS X f x ∈ Set.range (pointsMap B S hS Z.1.toFunctor Z.1.ι)) :
    IsEtaleAt B S hS f x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.20, Tag 0APM](https://stacks.math.columbia.edu/tag/0APM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
