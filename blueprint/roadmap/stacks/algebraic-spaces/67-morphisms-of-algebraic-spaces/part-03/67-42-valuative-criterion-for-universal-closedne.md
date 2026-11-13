---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.universallyClosed_of_isQuasiCompact_of_valuativeCriterion_existence, AlgebraicGeometry.Space.valuativeCriterion_existence_of_isQuasiSeparated_of_universallyClosed, AlgebraicGeometry.Space.universallyClosed_iff_valuativeCriterion_existence_of_isQuasiCompact_of_isQuasiSeparated, AlgebraicGeometry.Space.universallyClosed_tfae_of_isQuasiCompact_of_isSeparated, AlgebraicGeometry.Space.exists_valuationRing_extension_lift_of_isFlat, AlgebraicGeometry.Space.universallyClosed_of_refinedValuativeCriterion, AlgebraicGeometry.Space.isSeparated_of_refinedValuativeCriterion
statement: formalized
proof: formalized
---

# 67.42 Valuative criterion for universal closedness

Section 67.42 of the Stacks Project, [Tag 03K9](https://stacks.math.columbia.edu/tag/03K9). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03KA, a lemma

[Tag 03KA](https://stacks.math.columbia.edu/tag/03KA) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyClosed_of_isQuasiCompact_of_valuativeCriterion_existence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ValuativeCriteria.lean, line 769](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ValuativeCriteria.lean#L769).

> **Stacks 03KA.** A quasi-compact morphism of algebraic spaces over `S` which satisfies the
> existence part of the valuative criterion is universally closed.
>
> By Stacks 03IT it is enough to check that the base change along every morphism from a
> represented presheaf with affine scheme is closed on points; such a base change is again
> quasi-compact (Stacks 03HF) and again satisfies the existence part (Stacks 03IY), so
> `isClosedMap_pointsMap_of_isAffine_target` applies.

```lean
theorem universallyClosed_of_isQuasiCompact_of_valuativeCriterion_existence
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsQuasiCompact B S hS f) (hval : ValuativeCriterion.Existence f) :
    UniversallyClosed B S hS f
```

## Tag 0A3X, a lemma

[Tag 0A3X](https://stacks.math.columbia.edu/tag/0A3X) in the Stacks Project.

**`AlgebraicGeometry.Space.valuativeCriterion_existence_of_isQuasiSeparated_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ValuativeCriteria.lean, line 827](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ValuativeCriteria.lean#L827). The attribute's comment: “part (1)”.

> **Stacks 0A3X, part (1).** A quasi-separated universally closed morphism of algebraic spaces
> over `S` satisfies the existence part of the valuative criterion.
>
> A valuative square for `f` presents the generic point of its valuation ring `A` as a point of
> the base change `P = X ×_Y Spec A`, through a section `g : Spec K ⟶ P`. Quasi-separatedness of
> `P ⟶ Spec A` makes `g` quasi-compact (Stacks 03KS), the morphism `Spec K ⟶ Spec A` being
> affine, so the points of the scheme-theoretic image `Z ⊆ P` of `g` are the closure of the
> image of `g` (Stacks 082Z). Universal closedness makes the image of that closed set in
> `|Spec A|` closed, and it contains the generic point, hence everything; so some point of `|Z|`
> lies over the closed point of `Spec A`. Stacks 089B realizes that point by a valuation ring
> `A'` with fraction field `K'` and a square `Spec K' ⟶ Spec K`, `Spec A' ⟶ Z`; composing with
> `Z ⟶ P ⟶ X` gives the lift, and `A'` dominates `A` because the closed point of `Spec A'` maps
> to the closed point of `Spec A`.

```lean
theorem valuativeCriterion_existence_of_isQuasiSeparated_of_universallyClosed
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hqs : IsQuasiSeparated B S hS f) (huc : UniversallyClosed B S hS f) :
    ValuativeCriterion.Existence f
```

**`AlgebraicGeometry.Space.universallyClosed_iff_valuativeCriterion_existence_of_isQuasiCompact_of_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ValuativeCriteria.lean, line 1025](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ValuativeCriteria.lean#L1025). The attribute's comment: “part (2)”.

> **Stacks 0A3X, part (2).** A quasi-compact quasi-separated morphism of algebraic spaces over
> `S` is universally closed exactly when it satisfies the existence part of the valuative
> criterion.
>
> One direction is Stacks 03KA, the other is part (1).

```lean
theorem universallyClosed_iff_valuativeCriterion_existence_of_isQuasiCompact_of_isQuasiSeparated
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hqc : IsQuasiCompact B S hS f) (hqs : IsQuasiSeparated B S hS f) :
    UniversallyClosed B S hS f ↔ ValuativeCriterion.Existence f
```

## Tag 0A3Y, a lemma

[Tag 0A3Y](https://stacks.math.columbia.edu/tag/0A3Y) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyClosed_tfae_of_isQuasiCompact_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Valuative/UniversallyClosedValuative.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/UniversallyClosedValuative.lean#L46).

> For a quasi-compact separated morphism `f : X ⟶ Y` of algebraic spaces over `S`, universal
> closedness, the existence part of the valuative criterion of Stacks 03IX, and the existence of a
> lift in every valuative square for `f` over the valuation ring itself are equivalent.

```lean
public theorem universallyClosed_tfae_of_isQuasiCompact_of_isSeparated
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hqc : IsQuasiCompact B S hS f) (hsep : IsSeparated B S hS f) :
    List.TFAE
      [UniversallyClosed B S hS f,
        ValuativeCriterion.Existence f,
        ∀ q : ValuativeSquare f, Nonempty q.Lift]
```

## Tag 089F, a lemma

[Tag 089F](https://stacks.math.columbia.edu/tag/089F) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_valuationRing_extension_lift_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ValuativeCriteria.lean, line 1190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ValuativeCriteria.lean#L1190).

> **Stacks 089F.** Let `f : X ⟶ Y` be a flat morphism of algebraic spaces over `S` and let
> `Spec A ⟶ Y` be a morphism with `A` a valuation ring. If the closed point of `Spec A` maps to
> a point of `|Y|` in the image of `|X| → |Y|`, then there is an extension of valuation rings
> `A ⟶ A'` and a commutative square filling in `Spec A' ⟶ X` over `Spec A ⟶ Y`.
>
> The point of `|X|` above the closed point is produced by a chart `U ⟶ X ×_Y Spec A` of the
> fibre product (Stacks 03H4, 03H5). The chart is flat over `Spec A` because flatness is stable
> under base change (Stacks 03MO) and may be read on étale charts, so the induced homomorphism
> `A ⟶ 𝒪_{U, u}` is flat and local, hence faithfully flat; a prime of the stalk contracting to
> the zero ideal of `A` therefore exists, and factoring the resulting map to its fraction field
> through a valuation subring gives `A'`.

```lean
theorem exists_valuationRing_extension_lift_of_isFlat
    (A : Type u) [CommRing A] [IsDomain A] [ValuationRing A]
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (hf : IsFlat B S hS f)
    (V : BigFppfOver B S hS)
    (e : (BigFppfOver.toScheme B S hS).obj V ≅ Spec (.of A))
    (g : yoneda.obj V ⟶ Y)
    (p : FieldValuedPoint B S hS (yoneda.obj V))
    (hp : e.hom ((BigFppfOver.toScheme B S hS).map p.value
      (IsLocalRing.closedPoint p.carrier)) = IsLocalRing.closedPoint A)
    (himage : ∃ x : points B S hS X, pointsMap B S hS X f x =
      pointsMap B S hS (yoneda.obj V) g (p.class B S hS (yoneda.obj V))) :
    ∃ (A' : Type u) (_ : CommRing A') (_ : IsDomain A') (_ : ValuationRing A') (ι : A →+* A'),
      ValuationRing.IsExtension ι ∧
      ∃ (V' : BigFppfOver B S hS)
        (e' : (BigFppfOver.toScheme B S hS).obj V' ≅ Spec (.of A'))
        (j : V' ⟶ V) (lift : yoneda.obj V' ⟶ X),
        (BigFppfOver.toScheme B S hS).map j ≫ e.hom =
          e'.hom ≫ Spec.map (CommRingCat.ofHom ι) ∧
        lift ≫ f = yoneda.map j ≫ g
```

## Tag 089G, a lemma

[Tag 089G](https://stacks.math.columbia.edu/tag/089G) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyClosed_of_refinedValuativeCriterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RefinedValuativeCriterion.lean, line 1810](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RefinedValuativeCriterion.lean#L1810). The attribute's comment: “universally closed conclusion”.

> The refined valuative criterion makes `f` universally closed when the quasi-compact map `h`
> has dense image.

```lean
public theorem universallyClosed_of_refinedValuativeCriterion
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {U X Y : (AlgebraicGeometry.BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hU : AlgebraicGeometry.IsAlgebraicSpace B S hS U)
    (hX : AlgebraicGeometry.IsAlgebraicSpace B S hS X)
    (hY : AlgebraicGeometry.IsAlgebraicSpace B S hS Y)
    (h : U ⟶ X) (f : X ⟶ Y)
    (hf : AlgebraicGeometry.Space.IsQuasiCompact B S hS f)
    (hh : AlgebraicGeometry.Space.IsQuasiCompact B S hS h)
    (hdense : letI : TopologicalSpace (AlgebraicGeometry.Space.points B S hS X) :=
        pointTopology B S hS X
      DenseRange (pointsMap B S hS U h))
    (hunique : ∀ (q : ValuativeSquare f)
      (g : yoneda.obj (siteObject B S hS q.field_mem
        (Spec.map (CommRingCat.ofHom (algebraMap q.R q.K)) ≫ q.base)) ⟶ U),
      g ≫ h = q.generic → Subsingleton q.Lift)
    (hexists : ∀ (q : ValuativeSquare f)
      (g : yoneda.obj (siteObject B S hS q.field_mem
        (Spec.map (CommRingCat.ofHom (algebraMap q.R q.K)) ≫ q.base)) ⟶ U),
      g ≫ h = q.generic →
        ∃ e : q.DominatingExtension, Nonempty e.square.Lift) :
    UniversallyClosed B S hS f
```

**`AlgebraicGeometry.Space.isSeparated_of_refinedValuativeCriterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RefinedValuativeCriterion.lean, line 1984](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RefinedValuativeCriterion.lean#L1984). The attribute's comment: “separated conclusion”.

> With quasi-separatedness, the same refined valuative criterion makes `f` separated.

```lean
public theorem isSeparated_of_refinedValuativeCriterion
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {U X Y : (AlgebraicGeometry.BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hU : AlgebraicGeometry.IsAlgebraicSpace B S hS U)
    (hX : AlgebraicGeometry.IsAlgebraicSpace B S hS X)
    (hY : AlgebraicGeometry.IsAlgebraicSpace B S hS Y)
    (h : U ⟶ X) (f : X ⟶ Y)
    (hh : AlgebraicGeometry.Space.IsQuasiCompact B S hS h)
    (hqs : AlgebraicGeometry.Space.IsQuasiSeparated B S hS f)
    (hdense : letI : TopologicalSpace (AlgebraicGeometry.Space.points B S hS X) :=
        pointTopology B S hS X
      DenseRange (pointsMap B S hS U h))
    (hunique : ∀ (q : ValuativeSquare f)
      (g : yoneda.obj (siteObject B S hS q.field_mem
        (Spec.map (CommRingCat.ofHom (algebraMap q.R q.K)) ≫ q.base)) ⟶ U),
      g ≫ h = q.generic → Subsingleton q.Lift)
    (hexists : ∀ (q : ValuativeSquare f)
      (g : yoneda.obj (siteObject B S hS q.field_mem
        (Spec.map (CommRingCat.ofHom (algebraMap q.R q.K)) ≫ q.base)) ⟶ U),
      g ≫ h = q.generic →
        ∃ e : q.DominatingExtension, Nonempty e.square.Lift) :
    AlgebraicGeometry.Space.IsSeparated B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.42, Tag 03K9](https://stacks.math.columbia.edu/tag/03K9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
