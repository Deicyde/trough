---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.ValuativeCriterion.Uniqueness, AlgebraicGeometry.Space.ValuativeCriterion.Existence, AlgebraicGeometry.Space.ValuativeCriterion, AlgebraicGeometry.Space.valuativeCriterion_existence_iff_lift, AlgebraicGeometry.Space.valuativeCriterion_existence_iff_finiteSeparable, AlgebraicGeometry.Space.exists_lift_of_dominatingExtension, AlgebraicGeometry.Space.valuativeCriterion_existence_iff_lift_of_isSeparated, AlgebraicGeometry.TwistedDoubledOrigin.universallyClosed_surjective_specMap_algebraMap
statement: formalized
proof: formalized
---

# 67.41 Valuative criteria

Section 67.41 of the Stacks Project, [Tag 03IW](https://stacks.math.columbia.edu/tag/03IW). 8 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03IX, a definition

[Tag 03IX](https://stacks.math.columbia.edu/tag/03IX) in the Stacks Project.

**`AlgebraicGeometry.Space.ValuativeCriterion.Uniqueness`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Criterion.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Criterion.lean#L173). The attribute's comment: “uniqueness”.

> There is at most one extension of a compatible generic point to any valuation ring.

```lean
public def Uniqueness (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.ValuativeCriterion.Existence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Criterion.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Criterion.lean#L178). The attribute's comment: “existence”.

> A compatible generic point extends after a field extension and passage to a
> dominating valuation ring.

```lean
public def Existence (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.ValuativeCriterion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Criterion.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Criterion.lean#L192). The attribute's comment: “both parts”.

> A morphism satisfies both parts of the valuative criterion.

```lean
public abbrev ValuativeCriterion
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) : Prop
```

## Tag 03K8, a lemma

[Tag 03K8](https://stacks.math.columbia.edu/tag/03K8) in the Stacks Project.

**`AlgebraicGeometry.Space.valuativeCriterion_existence_iff_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Representable.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Representable.lean#L255).

> For a representable morphism, a lift after a dominating extension exists
> exactly when every valuative square has a lift before extension.

```lean
public theorem valuativeCriterion_existence_iff_lift
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y) (hf : yoneda.relativelyRepresentable f) :
    ValuativeCriterion.Existence f ↔
      (∀ q : ValuativeSquare f, Nonempty q.Lift)
```

## Tag 03KH, a lemma

[Tag 03KH](https://stacks.math.columbia.edu/tag/03KH) in the Stacks Project.

**`AlgebraicGeometry.Space.valuativeCriterion_existence_iff_finiteSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Valuative/FiniteSeparable.lean, line 614](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/FiniteSeparable.lean#L614).

> Allowing arbitrary field extensions in the existence valuative criterion
> is equivalent to allowing only finite separable ones.

```lean
public theorem valuativeCriterion_existence_iff_finiteSeparable
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    ValuativeCriterion.Existence f ↔ ExistenceFiniteSeparable f
```

## Tag 0ARH, a lemma

[Tag 0ARH](https://stacks.math.columbia.edu/tag/0ARH) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_lift_of_dominatingExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Valuative/PushDownSolution.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/PushDownSolution.lean#L319).

> **A lift of a dominating extension of a valuative square for a separated morphism of
> algebraic spaces descends to a lift of the square itself.** The extension `K'/K` of fraction
> fields is arbitrary: no finiteness or separability condition is imposed on it.
>
> The descent step needs the sheaf condition for the single faithfully flat covering
> `Spec A' ⟶ Spec A`; it is supplied by the fpqc sheaf condition
> `AlgebraicGeometry.IsAlgebraicSpace.isSheaf_fpqc` for `X`, which is Stacks 0APL.

```lean
public theorem exists_lift_of_dominatingExtension
    (hX : AlgebraicGeometry.IsAlgebraicSpace B S hS X)
    (hY : AlgebraicGeometry.IsAlgebraicSpace B S hS Y)
    (hf : AlgebraicGeometry.Space.IsSeparated B S hS f)
    (q : ValuativeSquare f) (e : q.DominatingExtension)
    (he : Nonempty e.square.Lift) :
    Nonempty q.Lift
```

## Tag 0A3W, a lemma

[Tag 0A3W](https://stacks.math.columbia.edu/tag/0A3W) in the Stacks Project.

**`AlgebraicGeometry.Space.valuativeCriterion_existence_iff_lift_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Valuative/PushDownSolution.lean, line 761](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/PushDownSolution.lean#L761).

> **For a separated morphism of algebraic spaces, allowing a dominating extension of the
> valuation ring does not change the existence half of the valuative criterion**: the criterion
> holds exactly when every valuative square already has a lift over the original valuation ring.

```lean
public theorem valuativeCriterion_existence_iff_lift_of_isSeparated
    (hX : AlgebraicGeometry.IsAlgebraicSpace B S hS X)
    (hY : AlgebraicGeometry.IsAlgebraicSpace B S hS Y)
    (hf : AlgebraicGeometry.Space.IsSeparated B S hS f) :
    ValuativeCriterion.Existence f ↔ ∀ q : ValuativeSquare f, Nonempty q.Lift
```

## Tag 03KI, an example

[Tag 03KI](https://stacks.math.columbia.edu/tag/03KI) in the Stacks Project.

**`AlgebraicGeometry.TwistedDoubledOrigin.universallyClosed_surjective_specMap_algebraMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean#L124). The attribute's comment: “Spec(k') → Spec(k) is universally closed and surjective”.

> **Stacks 03KI, the morphism `Spec k' ⟶ Spec k`.** For a finite extension `k'/k` of fields,
> the morphism `Spec k' ⟶ Spec k` is universally closed, being finite, and surjective, its
> target being a single point.

```lean
theorem universallyClosed_surjective_specMap_algebraMap [FiniteDimensional k K] :
    UniversallyClosed (Spec.map (CommRingCat.ofHom (algebraMap k K))) ∧
      Surjective (Spec.map (CommRingCat.ofHom (algebraMap k K)))
```

**`AlgebraicGeometry.TwistedDoubledOrigin.isQuasiCompact_quotientBaseMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean#L218). The attribute's comment: “π is quasi-compact”.

> **Stacks 03KI, the quasi-compactness clause.** The structure morphism `π : X ⟶ S = 𝔸¹_k` of
> the Galois twist of the affine line with zero doubled is quasi-compact.
>
> The quotient is a quasi-compact algebraic space, its chart being the affine line over `k'`, and
> the base is quasi-separated, being affine; so part (1) of Stacks 073B applies.

```lean
theorem isQuasiCompact_quotientBaseMap :
    Space.IsQuasiCompact B (base k) hS (quotientBaseMap k K hdegree σ hσ B hS)
```

**`AlgebraicGeometry.TwistedDoubledOrigin.universallyClosed_quotientBaseMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean#L289). The attribute's comment: “π is universally closed”.

> **Stacks 03KI, the universal closedness clause.** The structure morphism
> `π : X ⟶ S = 𝔸¹_k` of the Galois twist of the affine line with zero doubled is universally
> closed.
>
> The chart `U = Spec k'[x] ⟶ X` is surjective and `U ⟶ S` is universally closed, being finite, so
> Stacks 08AJ pushes universal closedness down to `π`.

```lean
theorem universallyClosed_quotientBaseMap :
    Space.UniversallyClosed B (base k) hS (quotientBaseMap k K hdegree σ hσ B hS)
```

**`AlgebraicGeometry.TwistedDoubledOrigin.universallyClosed_doubledProjOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean#L314). The attribute's comment: “the affine line with zero doubled is universally closed over the affine line”.

> **Stacks 03KI, the affine line with zero doubled.** The affine line over `k'` with zero
> doubled is universally closed over the affine line over `k'`.
>
> The two copies of the affine line cover it, and their union maps to the affine line by the
> codiagonal, which is finite; so Mathlib's descent of universal closedness along a surjection
> applies.

```lean
theorem universallyClosed_doubledProjOver : UniversallyClosed (doubledProjOver k K).left
```

**`AlgebraicGeometry.TwistedDoubledOrigin.exists_isIso_baseChangePresheaf_comp_doubledProjOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean#L346). The attribute's comment: “after base change by Spec(k') → Spec(k), π is the affine line with zero doubled over the affine line”.

> **Stacks 03KI, the base change to `k'`.** After base change along
> `U = S ×_{Spec k} Spec k' = 𝔸¹_{k'} ⟶ S`, the structure morphism `π` is identified with the
> morphism from the affine line over `k'` with zero doubled to the affine line over `k'`: the base
> change `U ×_S X` is isomorphic to the functor of points of the glued scheme, compatibly with the
> projections to `U`.
>
> The isomorphism is the one of part (6) of Stacks 03FN; both it and the projections are
> determined on the self-product `U ×_S U`, where both projections are the first one.

```lean
theorem exists_isIso_baseChangePresheaf_comp_doubledProjOver :
    ∃ χ : baseChangePresheaf k K B hS hdegree σ hσ ⟶
        (pointsFunctor k B hS).obj (doubledOverBase k K),
      IsIso χ ∧ χ ≫ (pointsFunctor k B hS).map (doubledProjOver k K) =
        pullback.fst (pointsCoverToBase k K B hS) (quotientBaseMap k K hdegree σ hσ B hS)
```

**`AlgebraicGeometry.TwistedDoubledOrigin.exists_mono_isPullback_zeroFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean#L443). The attribute's comment: “the point of X above 0 corresponds to a monomorphism Spec(k') → X”.

> **Stacks 03KI, the point above the origin.** The point of `X` above `0 ∈ 𝔸¹_k` is a
> monomorphism `Spec k' ⟶ X`: there is a monomorphism from the functor of points of `Spec k'`
> into `X` whose square over the origin `Spec k ⟶ 𝔸¹_k` is Cartesian, so `Spec k'` is the whole
> fibre of `π` over the origin.
>
> The fibre is computed in
> `AlgebraicGeometry.TwistedDoubledOrigin.twistedRelationQuotient_zeroFibre`; its map to `X` is a
> monomorphism because the origin is a monomorphism into the base.

```lean
theorem exists_mono_isPullback_zeroFibre :
    ∃ m : (pointsFunctor k B hS).obj (zeroCoverOverBase k K) ⟶
        (quadraticGaloisTwistedDoubledOrigin k K hdegree σ hσ B hS).obj,
      Mono m ∧ IsPullback m ((pointsFunctor k B hS).map (zeroCoverToZeroBase k K))
        (quotientBaseMap k K hdegree σ hσ B hS)
        ((pointsFunctor k B hS).map (zeroBaseToBase k))
```

**`AlgebraicGeometry.TwistedDoubledOrigin.formalDiskValuativeSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean, line 538](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean#L538). The attribute's comment: “the solid square of the displayed diagram, over the valuation ring k⟦x⟧”.

> **Stacks 03KI, the solid square.** The square displayed in the example: its valuation ring is
> the ring `k⟦x⟧` of formal power series, its fraction field the field `k((x))` of Laurent series,
> its structure morphism over the base the coordinate map `Spec k⟦x⟧ ⟶ 𝔸¹_k` of
> `AlgebraicGeometry.TwistedDoubledOrigin.formalDiskBaseMap`, and its top edge the point
> `Spec k((x)) ⟶ X` of
> `AlgebraicGeometry.TwistedDoubledOrigin.laurentGenericPoint`.
>
> Only the top edge carries content: the target of `π` is the terminal presheaf, so the edge of the
> square into it, and the commutativity of the square, are the only ones there are.

```lean
def formalDiskValuativeSquare :
    Space.ValuativeSquare (quotientBaseMap k K hdegree σ hσ B hS)
```

**`AlgebraicGeometry.TwistedDoubledOrigin.isEmpty_lift_formalDiskValuativeSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean, line 555](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean#L555). The attribute's comment: “there cannot exist a dotted arrow”.

> **Stacks 03KI, the missing dotted arrow.** The square of the example has no dotted arrow: a
> dotted arrow is in particular a point of the quotient over the formal disc, and there is none,
> the point of `X` above the origin being `Spec k'`, which has no `k`-point.

```lean
theorem isEmpty_lift_formalDiskValuativeSquare :
    IsEmpty (formalDiskValuativeSquare k K B hS hdegree σ hσ).Lift
```

**`AlgebraicGeometry.TwistedDoubledOrigin.existenceFiniteSeparable_and_not_forall_nonempty_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean, line 568](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean#L568). The attribute's comment: “a finite separable field extension is needed in general”.

> **Stacks 03KI, a finite separable extension is needed.** The structure morphism `π` satisfies
> the existence part of the valuative criterion when the fraction field may be replaced by a
> finite separable extension, but not when it may not be extended at all.
>
> The first half is Stacks 0A3X, part (1), for the quasi-separated (Stacks 03FN, part (5)) and
> universally closed morphism `π`, refined by Stacks 03KH; the second is the square of the example
> over `k⟦x⟧`.

```lean
theorem existenceFiniteSeparable_and_not_forall_nonempty_lift :
    Space.ExistenceFiniteSeparable (quotientBaseMap k K hdegree σ hσ B hS) ∧
      ¬ ∀ q : Space.ValuativeSquare (quotientBaseMap k K hdegree σ hσ B hS), Nonempty q.Lift
```

**`AlgebraicGeometry.TwistedDoubledOrigin.quotientBaseMap_example`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean, line 599](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginUniversallyClosed.lean#L599). The attribute's comment: “all the assertions of the example together”.

> **Stacks 03KI.** Let `k'/k` be a degree two Galois extension and let `X` be the Galois twist
> of the affine line with zero doubled, the algebraic space of Stacks 03FN over `S = 𝔸¹_k`, with
> structure morphism `π : X ⟶ S`. Then:
>
> * `π` is quasi-compact and universally closed;
> * after base change along `𝔸¹_{k'} = S ×_{Spec k} Spec k' ⟶ S`, `π` is identified with the
>   affine line over `k'` with zero doubled over the affine line over `k'`, which is universally
>   closed;
> * `Spec k' ⟶ Spec k` is universally closed and surjective;
> * the point of `X` above the origin is a monomorphism `Spec k' ⟶ X`, the whole fibre of `π`
>   there;
> * the formal disc `Spec k⟦x⟧` over `S` carries no point of `X`, so the square of the example
>   (`AlgebraicGeometry.TwistedDoubledOrigin.formalDiskValuativeSquare`) has no dotted arrow;
> * `π` satisfies the existence part of the valuative criterion with finite separable extensions
>   of the fraction field, but not without extending it.

```lean
theorem quotientBaseMap_example :
    Space.IsQuasiCompact B (base k) hS (quotientBaseMap k K hdegree σ hσ B hS) ∧
      Space.UniversallyClosed B (base k) hS (quotientBaseMap k K hdegree σ hσ B hS) ∧
      (∃ χ : baseChangePresheaf k K B hS hdegree σ hσ ⟶
          (pointsFunctor k B hS).obj (doubledOverBase k K),
        IsIso χ ∧ χ ≫ (pointsFunctor k B hS).map (doubledProjOver k K) =
          pullback.fst (pointsCoverToBase k K B hS) (quotientBaseMap k K hdegree σ hσ B hS)) ∧
      UniversallyClosed (doubledProjOver k K).left ∧
      (UniversallyClosed (Spec.map (CommRingCat.ofHom (algebraMap k K))) ∧
        Surjective (Spec.map (CommRingCat.ofHom (algebraMap k K)))) ∧
      (∃ m : (pointsFunctor k B hS).obj (zeroCoverOverBase k K) ⟶
          (quadraticGaloisTwistedDoubledOrigin k K hdegree σ hσ B hS).obj,
        Mono m ∧ IsPullback m ((pointsFunctor k B hS).map (zeroCoverToZeroBase k K))
          (quotientBaseMap k K hdegree σ hσ B hS)
          ((pointsFunctor k B hS).map (zeroBaseToBase k))) ∧
      ¬ Nonempty
        (yoneda.obj (siteObject B (base k) hS (contains_powerSeries k B hS)
            (formalDiskBaseMap k)) ⟶
          (quadraticGaloisTwistedDoubledOrigin k K hdegree σ hσ B hS).obj) ∧
      IsEmpty (formalDiskValuativeSquare k K B hS hdegree σ hσ).Lift ∧
      Space.ExistenceFiniteSeparable (quotientBaseMap k K hdegree σ hσ B hS) ∧
      ¬ ∀ q : Space.ValuativeSquare (quotientBaseMap k K hdegree σ hσ B hS), Nonempty q.Lift
```

**`AlgebraicGeometry.TwistedDoubledOrigin.not_nonempty_hom_formalDisk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginValuativeLift.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginValuativeLift.lean#L129). The attribute's comment: “no_unextended_lift”.

> **Stacks 03KI**, third assertion of the example. For a quadratic Galois extension `K/k`,
> the formal disc over `k` has no point of the quadratic Galois twisted doubled origin lying
> over `AlgebraicGeometry.TwistedDoubledOrigin.formalDiskBaseMap`.
>
> So the solid valuative square over the valuation ring `k⟦x⟧` whose bottom edge is that
> coordinate map admits no dotted arrow, and a fortiori none compatible with the generic point
> coming from the isomorphism of Stacks 03FN away from the origin: a finite separable extension
> of the fraction field is genuinely needed in the existence part of Stacks 03IX.

```lean
theorem not_nonempty_hom_formalDisk
    [FiniteDimensional k K] [IsGalois k K] (hdegree : Module.finrank k K = 2)
    (σ : K ≃ₐ[k] K) (hσ : σ ≠ 1) (B : BigFppfSite.{u}) (hS : B.Contains (base k))
    (hDisk : B.Contains (Spec (.of (PowerSeries k))))
    [HasSheafify (BigFppfOver.topology B (base k) hS) (Type u)] :
    ¬ Nonempty
      (yoneda.obj (siteObject B (base k) hS hDisk (formalDiskBaseMap k)) ⟶
        (quadraticGaloisTwistedDoubledOrigin k K hdegree σ hσ B hS).obj)
```

## Tag 03IY, a lemma

[Tag 03IY](https://stacks.math.columbia.edu/tag/03IY) in the Stacks Project.

**`AlgebraicGeometry.Space.valuativeCriterion_uniqueness_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ValuativeCriteria.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ValuativeCriteria.lean#L219). The attribute's comment: “uniqueness part”.

> **Stacks 03IY, uniqueness part.** The base change of a morphism of algebraic spaces
> satisfying the uniqueness part of the valuative criterion satisfies it again.
>
> Two lifts of a valuative square for the base change `b` agree after composing with `a`, by
> uniqueness for `p` applied to the induced valuative square, and after composing with `b`,
> because both are lifts; so they agree.

```lean
theorem valuativeCriterion_uniqueness_of_isPullback
    {F G F' G' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {a : F ⟶ F'} {b : F ⟶ G} {p : F' ⟶ G'} {q : G ⟶ G'} (sq : IsPullback a b p q)
    (hp : ValuativeCriterion.Uniqueness p) : ValuativeCriterion.Uniqueness b
```

**`AlgebraicGeometry.Space.valuativeCriterion_existence_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ValuativeCriteria.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ValuativeCriteria.lean#L243). The attribute's comment: “existence part”.

> **Stacks 03IY, existence part.** The base change of a morphism of algebraic spaces
> satisfying the existence part of the valuative criterion satisfies it again.
>
> A valuative square for the base change `b` induces one for `p`; a dominating extension and a
> lift there, together with the bottom edge pushed along the extension, define a map into the
> fibre product by the universal property of the cartesian square, and that map is a lift of
> the dominating extension of the original square.

```lean
theorem valuativeCriterion_existence_of_isPullback
    {F G F' G' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {a : F ⟶ F'} {b : F ⟶ G} {p : F' ⟶ G'} {q : G ⟶ G'} (sq : IsPullback a b p q)
    (hp : ValuativeCriterion.Existence p) : ValuativeCriterion.Existence b
```

## Tag 03IZ, a lemma

[Tag 03IZ](https://stacks.math.columbia.edu/tag/03IZ) in the Stacks Project.

**`AlgebraicGeometry.Space.valuativeCriterionExistence_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Composition.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Composition.lean#L68). The attribute's comment: “composition_valuative_existence”.

> The existence part of the valuative criterion is preserved under composition.

```lean
public theorem valuativeCriterionExistence_comp
    (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : ValuativeCriterion.Existence f)
    (hg : ValuativeCriterion.Existence g) :
    ValuativeCriterion.Existence (f ≫ g)
```

**`AlgebraicGeometry.Space.valuativeCriterion_uniqueness_comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Composition.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Composition.lean#L130). The attribute's comment: “composition_valuative_uniqueness”.

> Uniqueness of lifts in valuative squares is stable under composition.

```lean
public lemma valuativeCriterion_uniqueness_comp (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : ValuativeCriterion.Uniqueness f)
    (hg : ValuativeCriterion.Uniqueness g) :
    ValuativeCriterion.Uniqueness (f ≫ g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.41, Tag 03IW](https://stacks.math.columbia.edu/tag/03IW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
