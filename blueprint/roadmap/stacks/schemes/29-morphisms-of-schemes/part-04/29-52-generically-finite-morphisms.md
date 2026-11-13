---
declaration: section
origin: cited
lean: AlgebraicGeometry.finite_preimage_singleton_iff_exists_affine_cover_isFinite, AlgebraicGeometry.finite_preimage_singleton_iff_exists_affine_opens_isFinite, AlgebraicGeometry.finite_preimage_singleton_iff_exists_affine_open_isFinite_restrict, AlgebraicGeometry.coordinatePoint_injective, AlgebraicGeometry.doubledPoint, AlgebraicGeometry.doubledPoint_genericPoint, AlgebraicGeometry.doubledPoint_quasiCompact, AlgebraicGeometry.doubledPoint_locallyOfFiniteType
statement: formalized
proof: formalized
---

# 29.52 Generically finite morphisms

Section 29.52 of the Stacks Project, [Tag 02NV](https://stacks.math.columbia.edu/tag/02NV). 11 tags here are carried by 28 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02NW, a lemma

[Tag 02NW](https://stacks.math.columbia.edu/tag/02NW) in the Stacks Project.

**`AlgebraicGeometry.finite_preimage_singleton_iff_exists_affine_cover_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFinite.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFinite.lean#L478). The attribute's comment: “conditions (1) and (2)”.

> **Stacks Project, Tag 02NW, conditions (1) and (2).** For a morphism locally of finite
> type, the fibre over a generic point of an irreducible component is finite exactly when it is
> covered by finitely many affine opens which are finite over a common affine neighbourhood of
> that generic point.

```lean
theorem finite_preimage_singleton_iff_exists_affine_cover_isFinite
    {X Y : Scheme.{u}} (f : X ⟶ Y) [LocallyOfFiniteType f]
    (η : Y) (hη : η ∈ genericPoints Y) :
    (f ⁻¹' {η}).Finite ↔
      ∃ (n : ℕ) (U : Fin n → X.affineOpens) (V : Y.affineOpens),
        (η ∈ V.1) ∧
          (f ⁻¹' {η} ⊆ ⋃ i, (U i).1) ∧
            ∀ i, ∃ hUi : (U i).1 ≤ f ⁻¹ᵁ V.1, IsFinite (f.resLE V.1 (U i).1 hUi)
```

**`AlgebraicGeometry.finite_preimage_singleton_iff_exists_affine_opens_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFinite.lean, line 495](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFinite.lean#L495). The attribute's comment: “condition (3)”.

> **Stacks Project, Tag 02NW, condition (3).** For a quasi-separated morphism locally of
> finite type, the fibre over a generic point of an irreducible component is finite exactly when
> one affine open containing the fibre is finite over an affine neighbourhood of that point.

```lean
theorem finite_preimage_singleton_iff_exists_affine_opens_isFinite
    {X Y : Scheme.{u}} (f : X ⟶ Y) [LocallyOfFiniteType f] [QuasiSeparated f]
    (η : Y) (hη : η ∈ genericPoints Y) :
    (f ⁻¹' {η}).Finite ↔
      ∃ (V : Y.affineOpens) (U : X.affineOpens)
        (hUV : U.1 ≤ f ⁻¹ᵁ V.1),
        (η ∈ V.1) ∧ (f ⁻¹' {η} ⊆ U.1) ∧ IsFinite (f.resLE V.1 U.1 hUV)
```

**`AlgebraicGeometry.finite_preimage_singleton_iff_exists_affine_open_isFinite_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFinite.lean, line 513](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFinite.lean#L513). The attribute's comment: “condition (4)”.

> **Stacks Project, Tag 02NW, condition (4).** For a quasi-compact and quasi-separated
> morphism locally of finite type, finiteness of the fibre over a generic point of an
> irreducible component is equivalent to finiteness over some affine neighbourhood of the
> point.

```lean
theorem finite_preimage_singleton_iff_exists_affine_open_isFinite_restrict
    {X Y : Scheme.{u}} (f : X ⟶ Y) [LocallyOfFiniteType f] [QuasiCompact f]
    [QuasiSeparated f] (η : Y) (hη : η ∈ genericPoints Y) :
    (f ⁻¹' {η}).Finite ↔
      ∃ V : Y.affineOpens, (η ∈ V.1) ∧ IsFinite (f ∣_ V.1)
```

## Tag 03HY, an example

[Tag 03HY](https://stacks.math.columbia.edu/tag/03HY) in the Stacks Project.

**`AlgebraicGeometry.coordinatePoint_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L79). The attribute's comment: “distinctness of coordinate points”.

> Distinct coordinate projections induce distinct points of the spectrum of a countable product
> of copies of a field.

```lean
theorem coordinatePoint_injective (k : Type*) [Field k] :
    Function.Injective fun n : ℕ ↦ (coordinate k n).base (default : base k)
```

**`AlgebraicGeometry.doubledPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L223). The attribute's comment: “the doubled-point construction”.

> The spectrum of `∏ n : ℕ, 𝔽₂` with a closed, non-open point doubled, together with its
> canonical projection and chart identifications.

```lean
noncomputable def doubledPoint : DoubledPoint
```

**`AlgebraicGeometry.doubledPoint_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L291). The attribute's comment: “generic point of an irreducible component”.

> The doubled point is the generic point of an irreducible component of the spectrum.

```lean
theorem doubledPoint_genericPoint :
    doubledPoint.point ∈ genericPoints (space (ZMod 2))
```

**`AlgebraicGeometry.doubledPoint_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L301). The attribute's comment: “quasi-compactness”.

> The canonical projection is quasi-compact.

```lean
theorem doubledPoint_quasiCompact : QuasiCompact doubledPoint.projection
```

**`AlgebraicGeometry.doubledPoint_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L311). The attribute's comment: “finite type”.

> The canonical projection is locally of finite type.

```lean
theorem doubledPoint_locallyOfFiniteType : LocallyOfFiniteType doubledPoint.projection
```

**`AlgebraicGeometry.doubledPoint_finiteFibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L329). The attribute's comment: “finite fibres”.

> Every fibre of the canonical projection is finite.

```lean
theorem doubledPoint_finiteFibres (y : space (ZMod 2)) :
    (doubledPoint.projection ⁻¹' {y}).Finite
```

**`AlgebraicGeometry.doubledPoint_noAffinePreimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L386). The attribute's comment: “failure of conditions (3) and (4) of Tag 02NW”.

> The inverse image of every open neighbourhood of the doubled point is non-affine.

```lean
theorem doubledPoint_noAffinePreimage (U : (space (ZMod 2)).Opens)
    (hU : doubledPoint.point ∈ U) :
    ¬ IsAffine ((doubledPoint.projection ⁻¹ᵁ U).toScheme)
```

**`AlgebraicGeometry.doubledPoint_notQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 422](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L422). The attribute's comment: “failure of quasi-separatedness”.

> The canonical projection is not quasi-separated.

```lean
theorem doubledPoint_notQuasiSeparated : ¬ QuasiSeparated doubledPoint.projection
```

**`AlgebraicGeometry.doubledPoint_noAffineOpenContainingFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L448). The attribute's comment: “failure of condition (3) of Tag 02NW”.

> There is no affine open neighbourhood `V` of the doubled point together with an affine open
> `U` over `V` containing the whole fibre over the doubled point such that the restriction
> `U ⟶ V` of the canonical projection is finite.

```lean
theorem doubledPoint_noAffineOpenContainingFibre :
    ¬ ∃ (V : (space (ZMod 2)).affineOpens) (U : doubledPoint.source.affineOpens)
      (hUV : U.1 ≤ doubledPoint.projection ⁻¹ᵁ V.1),
        doubledPoint.point ∈ V.1 ∧
        doubledPoint.projection ⁻¹' {doubledPoint.point} ⊆ U.1 ∧
        IsFinite (doubledPoint.projection.resLE V.1 U.1 hUV)
```

**`AlgebraicGeometry.doubledPoint_noFiniteRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 500](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L500). The attribute's comment: “failure of condition (4) of Tag 02NW”.

> There is no affine open neighbourhood of the doubled point above which the canonical
> projection is finite.

```lean
theorem doubledPoint_noFiniteRestriction :
    ¬ ∃ V : (space (ZMod 2)).affineOpens, doubledPoint.point ∈ V.1 ∧
      IsFinite (doubledPoint.projection ∣_ V.1)
```

Declarations registered for the tag:

- [`PrimeSpectrum.compactSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.compactSpace#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L62) (StacksFrontier): “quasi-compactness of the affine spectrum”. References: EGA I (1.1.10), “more general”.
- [`AlgebraicGeometry.Space.InfiniteProduct.pow_card_eq_self`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean#L171), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L63) (StacksFrontier): “idempotence of the product ring”.
- [`AlgebraicGeometry.Space.InfiniteProduct.isClosed_singleton`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean#L243), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L65) (StacksFrontier): “closed points of the spectrum”.
- [`AlgebraicGeometry.Space.InfiniteProduct.nonempty_algEquiv_residueField`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean#L231), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L67) (StacksFrontier): “residue fields”.
- [`AlgebraicGeometry.Space.InfiniteProduct.isOpen_singleton_iff_coordinate`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean#L363), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L69) (StacksFrontier): “open coordinate points”.
- [`AlgebraicGeometry.Space.InfiniteProduct.not_discreteTopology`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean#L411), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L71) (StacksFrontier): “existence of a non-open point”.
- [`AlgebraicGeometry.Space.InfiniteProduct.instTotallyDisconnectedSpace`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean#L337), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/DoubledPoint.lean#L73) (StacksFrontier): “total disconnectedness”.

## Tag 03HZ, a remark

[Tag 03HZ](https://stacks.math.columbia.edu/tag/03HZ) in the Stacks Project.

**`AlgebraicGeometry.exists_dense_open_isFinite_of_quasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FiniteOverDenseOpen.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FiniteOverDenseOpen.lean#L208). The attribute's comment: “the whole content of the remark: the alternative to Tag 02NW that it states, namely that a quasi-finite morphism is finite over a dense open of the target, whose proof the remark defers to Tag 03I1”.

> **Stacks Project, Tag 03I1.** A quasi-finite morphism of schemes is finite over a dense open
> subscheme of its target. This is also the statement of [Stacks Project, Tag 03HZ], the remark
> offering it as an alternative to [Stacks Project, Tag 02NW] and deferring its proof to here.

```lean
theorem exists_dense_open_isFinite_of_quasiFinite {Y X : Scheme.{u}} (f : Y ⟶ X)
    [LocallyOfFiniteType f] [LocallyQuasiFinite f] [QuasiCompact f] :
    ∃ U : X.Opens, Dense (U : Set X) ∧ IsFinite (f ∣_ U)
```

## Tag 0BAH, a lemma

[Tag 0BAH](https://stacks.math.columbia.edu/tag/0BAH) in the Stacks Project.

**`AlgebraicGeometry.quasiFiniteAt_over_genericPoint_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Fibre.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Fibre.lean#L104).

> For a locally finite type morphism, the fibre over a generic point consists of generic
> points if and only if the morphism is quasi-finite at every point of the fibre, equivalently
> if it is quasi-finite at every generic point of the fibre.

```lean
public theorem quasiFiniteAt_over_genericPoint_tfae {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] (η : Y) (hη : η ∈ genericPoints Y) :
    List.TFAE [
      f ⁻¹' {η} ⊆ genericPoints X,
      ∀ x : X, f x = η → quasiFiniteAt f x,
      ∀ ξ : X, ξ ∈ genericPoints X → f ξ = η → quasiFiniteAt f ξ]
```

## Tag 0BAI, a lemma

[Tag 0BAI](https://stacks.math.columbia.edu/tag/0BAI) in the Stacks Project.

**`AlgebraicGeometry.exists_dense_open_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FiniteOverDenseOpen.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FiniteOverDenseOpen.lean#L448).

> **Stacks 0BAI.** A locally finite type morphism carrying precisely the generic points of its
> source to the generic points of its target is finite over a dense open of the target, if it is
> quasi-compact or separated.

```lean
theorem exists_dense_open_isFinite {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] (hX : (genericPoints X).Finite) (hY : (genericPoints Y).Finite)
    (hgeneric : f ⁻¹' genericPoints Y = genericPoints X)
    (hqc_or_sep : QuasiCompact f ∨ IsSeparated f) :
    ∃ V : Y.Opens, Dense (V : Set Y) ∧ IsFinite (f ∣_ V)
```

## Tag 0BAJ, a lemma

[Tag 0BAJ](https://stacks.math.columbia.edu/tag/0BAJ) in the Stacks Project.

**`AlgebraicGeometry.exists_dense_open_isIso_morphismRestrict_of_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/IsoOverDenseOpen.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/IsoOverDenseOpen.lean#L79).

> **Stacks Project, Tag 0BAJ.** A birational morphism between schemes with finitely many
> irreducible components is an isomorphism over a dense open subscheme of its target, provided it
> is quasi-compact or separated and provided it is locally of finite type with reduced target or
> locally of finite presentation.

```lean
theorem exists_dense_open_isIso_morphismRestrict_of_isBirational
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    [Finite (irreducibleComponents X)] [Finite (irreducibleComponents Y)]
    (hf : IsBirational f) (hqc_or_sep : QuasiCompact f ∨ IsSeparated f)
    (hfin : (LocallyOfFiniteType f ∧ IsReduced Y) ∨ LocallyOfFinitePresentation f) :
    ∃ V : Y.Opens, Dense (V : Set Y) ∧ IsIso (f ∣_ V)
```

## Tag 02NX, a lemma

[Tag 02NX](https://stacks.math.columbia.edu/tag/02NX) in the Stacks Project.

**`AlgebraicGeometry.eq_genericPoint_iff_finite_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFiniteDominant.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFiniteDominant.lean#L233). The attribute's comment: “condition (4), restated as finiteness of the fibre over the generic point of the target, which is the hypothesis of Tag 02NW”.

> **Stacks Project, Tag 02NX, condition (4) as finiteness of the generic fibre.** For a
> morphism locally of finite type between integral schemes, the generic point of the source is the
> only point above the generic point of the target exactly when that fibre is finite.

```lean
theorem eq_genericPoint_iff_finite_fibre :
    (∀ x : X, f x = genericPoint Y → x = genericPoint X) ↔
      (f ⁻¹' {genericPoint Y}).Finite
```

**`AlgebraicGeometry.exists_affineOpens_isFinite_iff_eq_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFiniteDominant.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFiniteDominant.lean#L257). The attribute's comment: “conditions (3) and (4)”.

> **Stacks Project, Tag 02NX, conditions (3) and (4).** For a dominant morphism locally of
> finite type between integral schemes, finiteness on some pair of nonempty affine opens of the
> source and target is equivalent to the generic point of the source being the only point above
> the generic point of the target.

```lean
theorem exists_affineOpens_isFinite_iff_eq_genericPoint :
    (∃ (U : X.affineOpens) (V : Y.affineOpens) (hUV : U.1 ≤ f ⁻¹ᵁ V.1),
        (U.1 : Set X).Nonempty ∧ (V.1 : Set Y).Nonempty ∧
          IsFinite (f.resLE V.1 U.1 hUV)) ↔
      (∀ x : X, f x = genericPoint Y → x = genericPoint X)
```

**`AlgebraicGeometry.exists_affineOpen_isFinite_restrict_iff_eq_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFiniteDominant.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFiniteDominant.lean#L298). The attribute's comment: “condition (5)”.

> **Stacks Project, Tag 02NX, condition (5).** For a dominant morphism locally of finite type
> between integral schemes which is separated or quasi-compact, finiteness over some nonempty
> affine open of the target is equivalent to the generic point of the source being the only point
> above the generic point of the target.

```lean
theorem exists_affineOpen_isFinite_restrict_iff_eq_genericPoint
    (hsep_or_qc : IsSeparated f ∨ QuasiCompact f) :
    (∃ V : Y.affineOpens, (V.1 : Set Y).Nonempty ∧ IsFinite (f ∣_ V.1)) ↔
      (∀ x : X, f x = genericPoint Y → x = genericPoint X)
```

**`AlgebraicGeometry.trdeg_functionField_eq_zero_of_eq_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFiniteDominant.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFiniteDominant.lean#L338). The attribute's comment: “the implication from condition (4) -- equivalently (3), or (5) -- to condition (1)”.

> **Stacks Project, Tag 02NX, the implication to condition (1).** If the generic point of the
> source is the only point above the generic point of the target, then the induced extension of
> function fields has transcendence degree zero.

```lean
theorem trdeg_functionField_eq_zero_of_eq_genericPoint
    (h : ∀ x : X, f x = genericPoint Y → x = genericPoint X) :
    letI : Algebra Y.functionField X.functionField := (dominantFunctionFieldMap f).toAlgebra
    Algebra.trdeg Y.functionField X.functionField = 0
```

**`AlgebraicGeometry.trdeg_functionField_eq_zero_iff_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFiniteDominant.lean, line 400](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFiniteDominant.lean#L400). The attribute's comment: “conditions (1) and (2): the extension of function fields has transcendence degree zero if and only if it is finite”.

> **Stacks Project, Tag 02NX, conditions (1) and (2).** For a dominant morphism locally of
> finite type between integral schemes, the extension of function fields `R(Y) ⊆ R(X)` has
> transcendence degree zero exactly when it is finite.

```lean
theorem trdeg_functionField_eq_zero_iff_finite :
    letI : Algebra Y.functionField X.functionField := (dominantFunctionFieldMap f).toAlgebra
    Algebra.trdeg Y.functionField X.functionField = 0 ↔
      Module.Finite Y.functionField X.functionField
```

**`AlgebraicGeometry.eq_genericPoint_of_trdeg_functionField_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFiniteDominant.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFiniteDominant.lean#L416). The attribute's comment: “the implication from condition (1) to condition (4)”.

> **Stacks Project, Tag 02NX, the implication from condition (1) to condition (4).** If the
> extension of function fields has transcendence degree zero, then the generic point of the source
> is the only point above the generic point of the target: on a pair of affine opens the point in
> question cuts out a prime contracting to the zero ideal, and over an algebraic extension of
> fraction fields such a prime is zero, which is the prime cut out by the generic point.

```lean
theorem eq_genericPoint_of_trdeg_functionField_eq_zero
    (h : letI : Algebra Y.functionField X.functionField :=
        (dominantFunctionFieldMap f).toAlgebra
      Algebra.trdeg Y.functionField X.functionField = 0) :
    ∀ x : X, f x = genericPoint Y → x = genericPoint X
```

**`AlgebraicGeometry.tfae_trdeg_functionField_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFiniteDominant.lean, line 444](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFiniteDominant.lean#L444). The attribute's comment: “the equivalence of conditions (1), (2), (3) and (4)”. References: EGA II (6.1.8), “more general”.

> **Stacks Project, Tag 02NX, conditions (1)–(4).** For a dominant morphism locally of finite
> type between integral schemes the following are equivalent: the extension of function fields
> `R(Y) ⊆ R(X)` has transcendence degree zero; that extension is finite; `f` is finite on some
> pair of nonempty affine opens `U ⊆ X`, `V ⊆ Y` with `f(U) ⊆ V`; the generic point of `X` is the
> only point of `X` above the generic point of `Y`.

```lean
theorem tfae_trdeg_functionField_eq_zero :
    letI : Algebra Y.functionField X.functionField := (dominantFunctionFieldMap f).toAlgebra
    List.TFAE
      [Algebra.trdeg Y.functionField X.functionField = 0,
        Module.Finite Y.functionField X.functionField,
        ∃ (U : X.affineOpens) (V : Y.affineOpens) (hUV : U.1 ≤ f ⁻¹ᵁ V.1),
          (U.1 : Set X).Nonempty ∧ (V.1 : Set Y).Nonempty ∧ IsFinite (f.resLE V.1 U.1 hUV),
        ∀ x : X, f x = genericPoint Y → x = genericPoint X]
```

## Tag 02NY, a definition

[Tag 02NY](https://stacks.math.columbia.edu/tag/02NY) in the Stacks Project.

**`AlgebraicGeometry.degreeOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FunctionFieldDegree.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FunctionFieldDegree.lean#L88).

> **Stacks Project, Tag 02NY.** The *degree of `X` over `Y`* for a morphism `f : X ⟶ Y` of
> integral schemes which is locally of finite type and dominant: the degree
> `deg(X/Y) = [R(X) : R(Y)]` of the extension of function fields induced by `f`.
>
> This is a positive integer whenever that extension is finite, which is the case the source
> defines it in; see `AlgebraicGeometry.degreeOver_pos`.

```lean
noncomputable def degreeOver (f : X ⟶ Y) [IsIntegral X] [IsIntegral Y]
    [LocallyOfFiniteType f] [IsDominant f] : ℕ
```

## Tag 02NZ, a lemma

[Tag 02NZ](https://stacks.math.columbia.edu/tag/02NZ) in the Stacks Project.

**`AlgebraicGeometry.finrank_functionField_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FunctionFieldDegree.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FunctionFieldDegree.lean#L140).

> **Stacks Project, Tag 02NZ.** The degree of a tower of dominant morphisms of integral
> schemes is the product of the two degrees: if the function field of `X` is finite over that of
> `Y` and the function field of `Y` is finite over that of `Z`, then
> `[R(X) : R(Z)] = [R(X) : R(Y)] * [R(Y) : R(Z)]`.

```lean
theorem finrank_functionField_comp
    [FiniteDimensional Y.functionField X.functionField]
    [FiniteDimensional Z.functionField Y.functionField]
    (hf : algebraMap Y.functionField X.functionField = dominantFunctionFieldMap f)
    (hg : algebraMap Z.functionField Y.functionField = dominantFunctionFieldMap g)
    (hfg : algebraMap Z.functionField X.functionField = dominantFunctionFieldMap (f ≫ g)) :
    Module.finrank Z.functionField X.functionField =
      Module.finrank Y.functionField X.functionField *
        Module.finrank Z.functionField Y.functionField
```

## Tag 0AAZ, a definition

[Tag 0AAZ](https://stacks.math.columbia.edu/tag/0AAZ) in the Stacks Project.

**`AlgebraicGeometry.IsModification`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/Modification.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/Modification.lean#L45).

> A morphism `f : X' ⟶ X` to an integral scheme is a **modification** if `X'` is
> integral and `f` is birational and proper.

```lean
public abbrev IsModification {X X' : Scheme.{u}} [IsIntegral X] (f : X' ⟶ X) : Prop
```

## Tag 0AB0, a definition

[Tag 0AB0](https://stacks.math.columbia.edu/tag/0AB0) in the Stacks Project.

**`AlgebraicGeometry.IsAlteration`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/Alteration.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/Alteration.lean#L33).

> A morphism to an integral scheme is an alteration if it is proper and dominant, its
> source is integral, and its restriction over some nonempty open of the target is finite.

```lean
public abbrev IsAlteration {Y X : Scheme.{u}} [IsIntegral X] (f : Y ⟶ X) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.52, Tag 02NV](https://stacks.math.columbia.edu/tag/02NV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
