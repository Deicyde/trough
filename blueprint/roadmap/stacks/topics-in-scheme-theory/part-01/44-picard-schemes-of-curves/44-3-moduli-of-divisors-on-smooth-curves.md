---
declaration: section
origin: cited
lean: Stacks.Hilbert.HilbertFamily.isRelativeEffectiveCartierDivisor, Stacks.Hilbert.hilbertFunctorOfRankIsoRelativeEffectiveCartierDivisorFunctorOfRank, AlgebraicGeometry.isRelativeEffectiveCartierDivisor_iff_locallyQuasiFinite_flat, AlgebraicGeometry.isRelativeEffectiveCartierDivisor_of_isFiniteLocallyFree, AlgebraicGeometry.locallyQuasiFinite_flat_of_locallyOfFinitePresentation, AlgebraicGeometry.isFiniteLocallyFree_iff_isRelativeEffectiveCartierDivisor_of_isProper, AlgebraicGeometry.locallyQuasiFinite_flat_locallyOfFinitePresentation_iff_of_isLocallyNoetherian, AlgebraicGeometry.isFiniteLocallyFreeOfRank_mul
statement: formalized
proof: formalized
---

# 44.3 Moduli of divisors on smooth curves

Section 44.3 of the Stacks Project, [Tag 0B9C](https://stacks.math.columbia.edu/tag/0B9C). 8 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B9C, the section

[Tag 0B9C](https://stacks.math.columbia.edu/tag/0B9C) in the Stacks Project.

**`Stacks.Hilbert.HilbertFamily.isRelativeEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFamilyDivisor.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/HilbertFamilyDivisor.lean#L80). The attribute's comment: “the forward inclusion of the section's identification: a degree-`d` Hilbert family on a smooth relative curve is a relative effective Cartier divisor. The identification itself, as a natural isomorphism of functors, is `Stacks.Hilbert.hilbertFunctorOfRankIsoRelativeEffectiveCartierDivisorFunctorOfRank`”.

> **Stacks Project, Section 0B9C, forward inclusion.** On a scheme smooth of relative dimension
> one over `S`, a degree-`d` Hilbert family in `X` over `T` is a relative effective Cartier divisor
> on `X ×_S T` over `T`.
>
> Smoothness of relative dimension one is stable under base change, so `X ×_S T ⟶ T` is again
> smooth of relative dimension one; the family is finite locally free of degree `d` over `T`,
> hence finite locally free, and a finite locally free closed subscheme of a smooth relative curve
> is a relative effective Cartier divisor.

```lean
theorem HilbertFamily.isRelativeEffectiveCartierDivisor {S : Scheme.{u}} {X T : Over S}
    [SmoothOfRelativeDimension 1 X.hom] {d : ℕ} (Z : HilbertFamily X T d) :
    Stacks.Divisors.IsRelativeEffectiveCartierDivisor
      ((Over.pullback T.hom).obj X).hom Z.ideal
```

**`Stacks.Hilbert.hilbertFunctorOfRankIsoRelativeEffectiveCartierDivisorFunctorOfRank`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFamilyDivisor.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/HilbertFamilyDivisor.lean#L187). The attribute's comment: “the section's assertion that `Hilb^d_{X/S}` parametrizes relative effective Cartier divisors, read as a natural isomorphism of functors on schemes over `S` between `Hilb^d_{X/S}` and the functor sending `T` to the relative effective Cartier divisors `D ⊂ X_T` over `T` which are finite locally free of degree `d` over `T`. This is the form in which the rest of the section uses it: 0B9E, 0B9F and the addition morphism on `Hilb^d` treat points of `Hilb^d` as divisors”.

> **Stacks Project, Section 0B9C.** For `X ⟶ S` smooth of relative dimension one, the
> degree-`d` Hilbert functor `Hilb^d_{X/S}` is the functor of degree-`d` relative effective Cartier
> divisors: for every `S`-scheme `T`, the closed subschemes of `X ×_S T` finite locally free of
> degree `d` over `T` are exactly the relative effective Cartier divisors on `X ×_S T` over `T`
> which are finite locally free of degree `d` over `T`, compatibly with base change in `T`.
>
> Both directions send an ideal sheaf to itself. A Hilbert family is a relative effective Cartier
> divisor by `Stacks.Hilbert.HilbertFamily.isRelativeEffectiveCartierDivisor` (Tag 0B9D,
> (1) implies (2), on `X ×_S T ⟶ T`), and a divisor of degree `d` is in particular a Hilbert
> family.

```lean
def hilbertFunctorOfRankIsoRelativeEffectiveCartierDivisorFunctorOfRank {S : Scheme.{u}}
    (X : Over S) [SmoothOfRelativeDimension 1 X.hom] (d : ℕ) :
    hilbertFunctorOfRank X d ≅ relativeEffectiveCartierDivisorFunctorOfRank X d
```

## Tag 0B9D, a lemma

[Tag 0B9D](https://stacks.math.columbia.edu/tag/0B9D) in the Stacks Project.

**`AlgebraicGeometry.isRelativeEffectiveCartierDivisor_iff_locallyQuasiFinite_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/DivisorsOnSmoothCurves.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/DivisorsOnSmoothCurves.lean#L288). The attribute's comment: “(2) iff (3)”.

> **Stacks Project, Tag 0B9D (2) iff (3).** On a scheme smooth of relative dimension one over
> a base, the relative effective Cartier divisors are exactly the closed subschemes that are
> locally quasi-finite, flat and locally of finite presentation over the base.
>
> Both directions are checked on the fibres, which are smooth curves over a field and hence
> regular of dimension one at every point. An effective Cartier divisor drops the local dimension,
> so its fibres are zero-dimensional, hence discrete, which is quasi-finiteness; conversely a
> discrete closed subscheme of a smooth curve meets each local ring, a discrete valuation ring, in
> a nonzero ideal, which is therefore generated by a nonzerodivisor.

```lean
theorem isRelativeEffectiveCartierDivisor_iff_locallyQuasiFinite_flat
    {X S : Scheme.{u}} (f : X ⟶ S) [SmoothOfRelativeDimension 1 f] (I : X.IdealSheafData) :
    IsRelativeEffectiveCartierDivisor f I ↔
      LocallyOfFiniteType (I.subschemeι ≫ f) ∧ LocallyQuasiFinite (I.subschemeι ≫ f) ∧
        Flat (I.subschemeι ≫ f) ∧ LocallyOfFinitePresentation (I.subschemeι ≫ f)
```

**`AlgebraicGeometry.isRelativeEffectiveCartierDivisor_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/DivisorsOnSmoothCurves.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/DivisorsOnSmoothCurves.lean#L301). The attribute's comment: “(1) implies (2)”.

> **Stacks Project, Tag 0B9D (1) implies (2).** A closed subscheme of a scheme smooth of
> relative dimension one over a base that is finite locally free over the base is a relative
> effective Cartier divisor: a finite locally free morphism is finite, flat and locally of finite
> presentation, hence in particular locally quasi-finite.

```lean
theorem isRelativeEffectiveCartierDivisor_of_isFiniteLocallyFree {X S : Scheme.{u}} (f : X ⟶ S)
    [SmoothOfRelativeDimension 1 f] (I : X.IdealSheafData)
    [Stacks.Morphisms.IsFiniteLocallyFree (I.subschemeι ≫ f)] :
    IsRelativeEffectiveCartierDivisor f I
```

**`AlgebraicGeometry.locallyQuasiFinite_flat_of_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/DivisorsOnSmoothCurves.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/DivisorsOnSmoothCurves.lean#L316). The attribute's comment: “(3) implies (4)”.

> **Stacks Project, Tag 0B9D (3) implies (4).** Dropping the local finite presentation
> conjunct from the third condition gives the fourth.

```lean
theorem locallyQuasiFinite_flat_of_locallyOfFinitePresentation {D S : Scheme.{u}} (g : D ⟶ S)
    (h : LocallyOfFiniteType g ∧ LocallyQuasiFinite g ∧ Flat g ∧
      LocallyOfFinitePresentation g) :
    LocallyOfFiniteType g ∧ LocallyQuasiFinite g ∧ Flat g
```

**`AlgebraicGeometry.isFiniteLocallyFree_iff_isRelativeEffectiveCartierDivisor_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/DivisorsOnSmoothCurves.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/DivisorsOnSmoothCurves.lean#L328). The attribute's comment: “(1) iff (2) when X over S is proper”. References: SGA 4 XVIII (1.5.10.3), “special case”.

> **Stacks Project, Tag 0B9D (1) iff (2) for a proper morphism.** On a proper scheme smooth of
> relative dimension one over a base, the relative effective Cartier divisors are exactly the
> closed subschemes that are finite locally free over the base. Such a divisor is quasi-finite
> over the base, and proper since it is a closed subscheme of a proper scheme, hence finite; being
> also flat and locally of finite presentation it is finite locally free.

```lean
theorem isFiniteLocallyFree_iff_isRelativeEffectiveCartierDivisor_of_isProper {X S : Scheme.{u}}
    (f : X ⟶ S) [SmoothOfRelativeDimension 1 f] [IsProper f] (I : X.IdealSheafData) :
    Stacks.Morphisms.IsFiniteLocallyFree (I.subschemeι ≫ f) ↔
      IsRelativeEffectiveCartierDivisor f I
```

**`AlgebraicGeometry.locallyQuasiFinite_flat_locallyOfFinitePresentation_iff_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/SmoothCurveLocalDimension.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/SmoothCurveLocalDimension.lean#L336). The attribute's comment: “(3) iff (4) when S is locally Noetherian”.

> **Stacks Project, Tag 0B9D (3) iff (4).** Over a locally Noetherian base, a morphism locally of
> finite type is automatically locally of finite presentation, so the finite presentation conjunct
> may be dropped from the characterization of relative effective Cartier divisors.

```lean
theorem locallyQuasiFinite_flat_locallyOfFinitePresentation_iff_of_isLocallyNoetherian
    {D S : Scheme.{u}} (g : D ⟶ S) [IsLocallyNoetherian S] :
    (LocallyOfFiniteType g ∧ LocallyQuasiFinite g ∧ Flat g ∧
      LocallyOfFinitePresentation g) ↔
    (LocallyOfFiniteType g ∧ LocallyQuasiFinite g ∧ Flat g)
```

## Tag 0B9E, a lemma

[Tag 0B9E](https://stacks.math.columbia.edu/tag/0B9E) in the Stacks Project.

**`AlgebraicGeometry.isFiniteLocallyFreeOfRank_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/DivisorDegreeSum.lean, line 655](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/DivisorDegreeSum.lean#L655).

> **Stacks Project, Tag 0B9E.** Let `f : X ⟶ S` be smooth of relative dimension one and let
> `I` and `J` be quasi-coherent sheaves of ideals on `X` whose closed subschemes are finite
> locally free over `S` of degrees `d₁` and `d₂`. The sum of the two divisors, cut out by the
> product `I * J`, is finite locally free over `S` of degree `d₁ + d₂`.

```lean
theorem isFiniteLocallyFreeOfRank_mul
    {X S : Scheme.{u}} (f : X ⟶ S) [SmoothOfRelativeDimension 1 f]
    (I J : X.IdealSheafData) (d₁ d₂ : ℕ)
    [Stacks.Morphisms.IsFiniteLocallyFreeOfRank (I.subschemeι ≫ f) d₁]
    [Stacks.Morphisms.IsFiniteLocallyFreeOfRank (J.subschemeι ≫ f) d₂] :
    Stacks.Morphisms.IsFiniteLocallyFreeOfRank ((I * J).subschemeι ≫ f) (d₁ + d₂)
```

## Tag 0B9F, a lemma

[Tag 0B9F](https://stacks.math.columbia.edu/tag/0B9F) in the Stacks Project.

**`AlgebraicGeometry.exists_isFiniteLocallyFreeOfRank_sub_mul_eq_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/DivisorDegreeDifference.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/DivisorDegreeDifference.lean#L112).

> **Stacks Project, Tag 0B9F.** Let `f : X ⟶ S` be smooth of relative dimension one and let
> `D₁` and `D₂` be quasi-coherent sheaves of ideals on `X` whose closed subschemes are finite
> locally free over `S` of degrees `d₁` and `d₂`. If the closed subscheme of `D₁` is contained in
> that of `D₂`, that is `D₂ ≤ D₁`, then there is a quasi-coherent sheaf of ideals `D` with
> `D₂ = D₁ * D`, the sum of the two divisors, whose closed subscheme is finite locally free over
> `S` of degree `d₂ - d₁`.

```lean
theorem exists_isFiniteLocallyFreeOfRank_sub_mul_eq_of_le
    {X S : Scheme.{u}} (f : X ⟶ S) [SmoothOfRelativeDimension 1 f]
    (D₁ D₂ : X.IdealSheafData) (d₁ d₂ : ℕ)
    [Stacks.Morphisms.IsFiniteLocallyFreeOfRank (D₁.subschemeι ≫ f) d₁]
    [Stacks.Morphisms.IsFiniteLocallyFreeOfRank (D₂.subschemeι ≫ f) d₂]
    (hle : D₂ ≤ D₁) :
    ∃ D : X.IdealSheafData, D₂ = D₁ * D ∧
      Stacks.Morphisms.IsFiniteLocallyFreeOfRank (D.subschemeι ≫ f) (d₂ - d₁)
```

## Tag 0B9G, a lemma

[Tag 0B9G](https://stacks.math.columbia.edu/tag/0B9G) in the Stacks Project.

**`Stacks.Hilbert.IsPointAddition.isFiniteLocallyFreeOfRank_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertPointAddition.lean, line 565](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/HilbertPointAddition.lean#L565).

> **Stacks Project, Tag 0B9G.** Let `X ⟶ S` be smooth of relative dimension one and suppose
> the Hilbert functors `Hilb^d_{X/S}` are representable, say by `H` in degree `d` and by `H'` in
> degree `d + 1`. The point-addition morphism `H ×_S X ⟶ H'` is finite locally free of degree
> `d + 1`.
>
> It factors as the incidence isomorphism `H ×_S X ≅ D_univ` onto the universal degree-`(d+1)`
> family followed by the structure morphism of `D_univ`, which is finite locally free of degree
> `d + 1` because `D_univ` is a degree-`(d+1)` family. The incidence morphism is an isomorphism
> because it is bijective on points: surjectivity is the subtraction of a point from a family
> (Stacks Tag 0B9F) and injectivity is the cancellation of the graph of the point from the sum.

```lean
theorem isFiniteLocallyFreeOfRank_left (hf : IsPointAddition hH hH' f) :
    Stacks.Morphisms.IsFiniteLocallyFreeOfRank f.left (d + 1)
```

## Tag 0B9H, a lemma

[Tag 0B9H](https://stacks.math.columbia.edu/tag/0B9H) in the Stacks Project.

**`Stacks.Hilbert.smoothOfRelativeDimension_of_represents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeSmoothness.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeSmoothness.lean#L425). The attribute's comment: “corrected statement: adds the hypothesis that X -> S is separated, which the printed statement omits and needs (the source uses it through Hilb^1 = X and Tag 0B9G; without it the statement is false, see Stacks.Hilbert.NonSeparated.not_smooth_hilbertScheme_doubledLine); representability is the tag's own hypothesis”.

> **Stacks Project, Tag 0B9H.** Let `X ⟶ S` be a smooth morphism of schemes of relative
> dimension one such that the functors `Hilb^d_{X/S}` are representable, say by `H d` over `S`.
> Then the schemes `H d` are smooth over `S` of relative dimension `d`.
>
> Representability is the tag's own hypothesis, carried here as the family `hH`. Separatedness of
> `X ⟶ S` is what makes the point-addition morphism of Tag 0B9G available, and by
> `Stacks.Hilbert.isSeparated_of_isPointAddition_zero` it is equivalent to the existence of that
> morphism in degree `0`, so the induction cannot be started without it. The form of the result
> which takes those morphisms as data instead is
> `Stacks.Hilbert.smoothOfRelativeDimension_of_isPointAddition`.
>
> *Correction.* The printed statement has no separatedness hypothesis and is false without one:
> `Stacks.Hilbert.NonSeparated.not_smooth_hilbertScheme_doubledLine` is a smooth non-separated
> relative curve all of whose Hilbert functors are representable, with no `Hilb^d` of positive
> degree smooth. Apart from `[IsSeparated X.hom]` the binders are exactly the tag's: `X ⟶ S` smooth
> of relative dimension one, and a representing scheme `H d` of `Hilb^d_{X/S}` for every `d`.

```lean
theorem smoothOfRelativeDimension_of_represents [IsSeparated X.hom] (H : ℕ → Over S)
    (hH : ∀ d : ℕ, RepresentsHilbertFunctorOfRank X (H d) d) (d : ℕ) :
    SmoothOfRelativeDimension d (H d).hom
```

**`Stacks.Hilbert.NonSeparated.not_forall_smoothOfRelativeDimension_of_represents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeSmoothnessCounterexample.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeSmoothnessCounterexample.lean#L232). The attribute's comment: “the statement as printed is false: without separatedness of X → S it fails (this is the negation of the printed statement); the separated case is Stacks.Hilbert.smoothOfRelativeDimension_of_represents”.

> **Stacks Project, Tag 0B9H, as printed, is false.** The statement "for a smooth morphism of
> schemes `X ⟶ S` of relative dimension `1` such that the functors `Hilb^d_{X/S}` are representable,
> the schemes `Hilb^d_{X/S}` are smooth over `S` of relative dimension `d`" fails without a
> separation hypothesis on `X ⟶ S`: for `S = Spec ∏_{n ∈ ℕ} 𝔽₂` and `X` two copies of `𝔸¹_S` glued
> along the inverse image of the dense open `⋃ₙ D(eₙ)`, every `Hilb^d_{X/S}` is representable and
> none with `d ≥ 1` is smooth. The tag holds for a separated `X ⟶ S`:
> `Stacks.Hilbert.smoothOfRelativeDimension_of_represents`.

```lean
theorem not_forall_smoothOfRelativeDimension_of_represents :
    ¬ ∀ (S : Scheme.{u}) (X : Over S) [SmoothOfRelativeDimension 1 X.hom] (H : ℕ → Over S),
      (∀ d, RepresentsHilbertFunctorOfRank X (H d) d) →
        ∀ d, SmoothOfRelativeDimension d (H d).hom
```

**`Stacks.Hilbert.NonSeparated.not_smooth_hilbertScheme_doubledLine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeSmoothnessCounterexample.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeSmoothnessCounterexample.lean#L288). The attribute's comment: “the statement as printed is false: this is an explicit counterexample, a smooth non-separated relative curve over Spec of a product of copies of F_2 with every Hilb^d representable and no Hilb^d with d >= 1 smooth. The source needs X -> S separated (it uses Hilb^1 = X and Tag 0B9G); the corrected statement is Stacks.Hilbert.smoothOfRelativeDimension_of_represents”.

> **Stacks Project, Tag 0B9H, as printed, is false: the concrete counterexample.**
>
> The tag reads: "Let `X → S` be a smooth morphism of schemes of relative dimension `1` such that
> the functors `Hilb^d_{X/S}` are representable. The schemes `Hilb^d_{X/S}` are smooth over `S` of
> relative dimension `d`." This theorem exhibits `S`, `X` and the failure, with every degree
> `d ≥ 1` failing.
>
> * `S = Spec A` with `A = ∏_{n ∈ ℕ} 𝔽₂` (the ring `ULift ℕ → ZMod 2`).
> * `S' = ⋃ₙ D(eₙ) ⊆ S`, where `eₙ = Pi.single n 1` is the `n`-th coordinate idempotent; `S'` is a
>   dense open whose complement `V((eₙ)ₙ)` is nonempty.
> * `X = Stacks.Hilbert.DoubledLine.doubledLine S'`: two copies of `𝔸¹_S` glued along `𝔸¹_{S'}`,
>   that is, the total space of `Stacks.Examples.doubleSectionCover 𝔸¹_S 𝔸¹_{S'}`, covered by two
>   open charts `𝔸¹_S ⟶ X` which agree exactly over `S'`, with structure map to `S` given on
>   each chart by the projection `𝔸¹_S ⟶ S`.
>
> The conclusion records, in this order: `X ⟶ S` is smooth of relative dimension `1` (the tag's
> hypothesis); `X ⟶ S` is *not* separated (the hypothesis the source uses implicitly, through
> `Hilb^1_{X/S} = X` and Tag 0B9G); for every `d` the functor `Hilb^d_{X/S}` is representable (the
> tag's other hypothesis); and for every `d ≥ 1`, *every* scheme representing `Hilb^d_{X/S}` fails
> to be smooth over `S`, so in particular is not smooth of relative dimension `d`.
>
> The definitions the statement relies on:
>
> * `Stacks.Hilbert.HilbertFamily X T d` (Stacks Section 0B94, the value `Hilb^d_{X/S}(T)`): an
>   ideal sheaf `ideal` on `X ×_S T` together with the proof that `ideal.subschemeι ≫ (X ×_S T ⟶ T)`
>   is `Stacks.Morphisms.IsFiniteLocallyFreeOfRank _ d`, i.e. affine with direct image of the
>   structure sheaf finite locally free of rank `d` (Stacks Tag 02KA). A closed subscheme is
>   recorded by its ideal sheaf, so two families are equal iff their ideals are.
> * `Stacks.Hilbert.RepresentsHilbertFunctorOfRank X H d` (`H` represents `Hilb^d_{X/S}`): a
>   bijection `family : (T ⟶ H) ≃ HilbertFamily X T d` for every `S`-scheme `T`, natural in `T`:
>   `(family (g ≫ f)).ideal = (family f).ideal.comap (X ×_S T' ⟶ X ×_S T)`, where `comap` is the
>   ideal of the scheme-theoretic inverse image (Mathlib `Scheme.IdealSheafData.comap`), i.e. the
>   base change of the closed subscheme.
> * `AlgebraicGeometry.SmoothOfRelativeDimension`, `AlgebraicGeometry.Smooth`,
>   `AlgebraicGeometry.IsSeparated`: Mathlib's.
>
> Why it fails: a family of positive degree splits any base `T` into the open and closed parts over
> `S'` and over `S ∖ S'`, and over the latter `T ⟶ S` factors through `Z = V((eₙ)ₙ)`; so
> `Hilb^d_{X/S} ≅ 𝔸^d_{S'} ⊔ ∐_{a + b = d} (𝔸^a × 𝔸^b)_Z`. The pieces over `Z` are open and map
> into `S ∖ S'`, which has empty interior, whereas a smooth morphism is open.
>
> The corrected statement, with `X ⟶ S` separated, is
> `Stacks.Hilbert.smoothOfRelativeDimension_of_represents`; the bare negation of the printed
> statement is `Stacks.Hilbert.NonSeparated.not_forall_smoothOfRelativeDimension_of_represents`.

```lean
theorem not_smooth_hilbertScheme_doubledLine :
    let S : Scheme.{u} := Spec (CommRingCat.of (ULift.{u} ℕ → ZMod 2))
    let S' : S.Opens :=
      ⨆ n : ULift.{u} ℕ, PrimeSpectrum.basicOpen (Pi.single n 1 : ULift.{u} ℕ → ZMod 2)
    let X : Over S := DoubledLine.doubledLine S'
    SmoothOfRelativeDimension 1 X.hom ∧ ¬ IsSeparated X.hom ∧
      (∀ d : ℕ, ∃ H : Over S, Nonempty (RepresentsHilbertFunctorOfRank X H d)) ∧
      ∀ d : ℕ, 0 < d → ∀ H : Over S, RepresentsHilbertFunctorOfRank X H d → ¬ Smooth H.hom
```

## Tag 0B9I, a proposition

[Tag 0B9I](https://stacks.math.columbia.edu/tag/0B9I) in the Stacks Project.

**`Stacks.Hilbert.smoothOfRelativeDimension_and_isProper_of_isCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeCurve.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeCurve.lean#L134). The attribute's comment: “(1), ingredient: every representing scheme is smooth of relative dimension d and proper. The whole of (1), with representability, is Stacks.Hilbert.exists_representsHilbertFunctorOfRank_isVariety_of_isCurve”.

> **Stacks Project, Tag 0B9I, (1), smoothness and properness.** Let `X` be a smooth proper
> curve over a field `k`. Every scheme representing the degree-`d` Hilbert functor of `X` is smooth
> of relative dimension `d` and proper over `k`.
>
> Smoothness is Tag 0B9H; properness follows by induction on `d` from the point-addition morphisms
> `H^d ×_k X ⟶ H^{d+1}` of Tag 0B9G, which are finite locally free of degree `d + 1`, hence
> surjective, so that `H^{d+1}` is universally closed over `k` (Tag 03GN), and separated by Tag
> 0B98.

```lean
theorem smoothOfRelativeDimension_and_isProper_of_isCurve [IsProper f] [IsCurve k f] [Smooth f]
    (d : ℕ) (H : Over (Spec (.of k))) (hH : RepresentsHilbertFunctorOfRank (Over.mk f) H d) :
    SmoothOfRelativeDimension d H.hom ∧ IsProper H.hom
```

**`Stacks.Hilbert.isVariety_and_topologicalKrullDim_of_isCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeCurve.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeCurve.lean#L189). The attribute's comment: “(1), ingredient: every representing scheme is a variety of dimension d. The whole of (1), with representability, is Stacks.Hilbert.exists_representsHilbertFunctorOfRank_isVariety_of_isCurve”.

> **Stacks Project, Tag 0B9I, (1), the varieties.** Let `X` be a geometrically irreducible
> smooth proper curve over a field `k`. Every scheme representing the degree-`d` Hilbert functor of
> `X` is a variety of dimension `d` over `k`.
>
> By induction on `d`: `H^0` is a point, and `H^{d+1}` is the image of the irreducible scheme
> `H^d ×_k X` (Tag 038F) under the surjective point-addition morphism of Tag 0B9G; smooth and
> connected over a field it is integral, and its dimension is its relative dimension `d`.

```lean
theorem isVariety_and_topologicalKrullDim_of_isCurve [IsProper f] [IsCurve k f] [Smooth f]
    [GeometricallyIrreducible f] (d : ℕ) (H : Over (Spec (.of k)))
    (hH : RepresentsHilbertFunctorOfRank (Over.mk f) H d) :
    IsVariety k H.hom ∧ topologicalKrullDim H.left = d
```

**`Stacks.Hilbert.rationalPointsEquivEffectiveCartierDivisors`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeCurve.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeCurve.lean#L232). The attribute's comment: “(2)”.

> **Stacks Project, Tag 0B9I, (2).** Let `X` be a smooth proper curve over a field `k` and `H`
> a scheme representing the degree-`d` Hilbert functor of `X`. For a field extension `k'/k`, the
> `k'`-rational points of `H` correspond bijectively to the effective Cartier divisors of degree
> `d` on `X_{k'}`: the closed subschemes of `X_{k'}` which are effective Cartier divisors, finite
> locally free of rank `d` over `k'`.
>
> The correspondence is representability; every degree-`d` family over `k'` is an effective
> Cartier divisor by Tag 0B9D.

```lean
def rationalPointsEquivEffectiveCartierDivisors [IsProper f] [IsCurve k f] [Smooth f] (d : ℕ)
    (H : Over (Spec (.of k))) (hH : RepresentsHilbertFunctorOfRank (Over.mk f) H d)
    (k' : Type u) [Field k'] [Algebra k k'] :
    (fieldExtOver k k' ⟶ H) ≃
      {I : ((Over.pullback (fieldExtOver k k').hom).obj (Over.mk f)).left.IdealSheafData //
        Stacks.Divisors.IsEffectiveCartierDivisor I ∧
          Stacks.Morphisms.IsFiniteLocallyFreeOfRank
            (I.subschemeι ≫ ((Over.pullback (fieldExtOver k k').hom).obj (Over.mk f)).hom) d}
```

**`Stacks.Hilbert.Curve.hilbertScheme_geometry`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeCurveGeometry.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeCurveGeometry.lean#L125). The attribute's comment: “(1)”. References: SGA 4 XVII (6.3.8), “special case”.

> **Stacks Project, Tag 0B9I, part (1).** Let `X` be a geometrically irreducible smooth proper
> curve over a field `k` and `d ≥ 0`. The degree-`d` Hilbert functor of points of `X` is
> representable, and every scheme representing it is a smooth proper variety of dimension `d`
> over `k`.

```lean
theorem hilbertScheme_geometry [IsCurve k f] [GeometricallyIrreducible f] [Smooth f] [IsProper f]
    (d : ℕ) :
    Nonempty (Σ H : Over (Spec (.of k)), RepresentsHilbertFunctorOfRank (Over.mk f) H d) ∧
    ∀ (H : Over (Spec (.of k))), RepresentsHilbertFunctorOfRank (Over.mk f) H d →
      Smooth H.hom ∧ IsProper H.hom ∧ IsVariety k H.hom ∧
        topologicalKrullDim H.left = (d : WithBot ℕ∞)
```

**`Stacks.Hilbert.Curve.rationalPointsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeCurveGeometry.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeCurveGeometry.lean#L156). The attribute's comment: “(2)”.

> **Stacks Project, Tag 0B9I, part (2).** Let `X` be a geometrically irreducible smooth proper
> curve over a field `k`, let `H` represent its degree-`d` Hilbert functor and let `k'/k` be a field
> extension. The `k'`-rational points of `H` are in bijection with the effective Cartier divisors of
> degree `d` on `X_{k'}`: the closed subschemes of `X_{k'}` which are effective Cartier divisors and
> finite locally free of degree `d` over `k'`.

```lean
def rationalPointsEquiv {k' : Type u} [Field k'] [Algebra k k'] [IsCurve k f]
    [GeometricallyIrreducible f] [Smooth f] [IsProper f] (d : ℕ) (H : Over (Spec (.of k)))
    (hH : RepresentsHilbertFunctorOfRank (Over.mk f) H d) :
    (Over.mk (Spec.map (CommRingCat.ofHom (algebraMap k k'))) ⟶ H) ≃
    {I : ((Over.pullback (Over.mk (Spec.map (CommRingCat.ofHom (algebraMap k k')))).hom).obj
          (Over.mk f)).left.IdealSheafData //
      Stacks.Divisors.IsEffectiveCartierDivisor I ∧
        Stacks.Morphisms.IsFiniteLocallyFreeOfRank (I.subschemeι ≫
          ((Over.pullback (Over.mk (Spec.map (CommRingCat.ofHom (algebraMap k k')))).hom).obj
            (Over.mk f)).hom) d}
```

**`Stacks.Hilbert.exists_representsHilbertFunctorOfRank_isVariety_of_isCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeProperCurve.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeProperCurve.lean#L70). The attribute's comment: “(1)”.

> **Stacks Project, Tag 0B9I (1).** Let `X` be a geometrically irreducible smooth proper curve
> over a field `k`. For every `d` the degree-`d` Hilbert functor of `X` is representable by a
> smooth proper variety of dimension `d` over `k`.

```lean
theorem exists_representsHilbertFunctorOfRank_isVariety_of_isCurve [IsProper f] [IsCurve k f]
    [Smooth f] [GeometricallyIrreducible f] (d : ℕ) :
    ∃ (H : Over (Spec (.of k))) (_ : RepresentsHilbertFunctorOfRank (Over.mk f) H d),
      IsVariety k H.hom ∧ SmoothOfRelativeDimension d H.hom ∧ IsProper H.hom ∧
        topologicalKrullDim H.left = d
```

**`Stacks.Hilbert.isFiniteLocallyFreeOfRank_addDivisors_of_isCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeProperCurve.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeProperCurve.lean#L84). The attribute's comment: “(3), for every choice of representing schemes; geometric irreducibility of X is not needed”.

> **Stacks Project, Tag 0B9I (3).** Let `X` be a smooth proper curve over a field `k`, and let
> `H₁`, `H₂` and `H` be any schemes representing the Hilbert functors of `X` of degrees `d₁`, `d₂`
> and `d₁ + d₂`. The addition morphism `H₁ ×_k H₂ ⟶ H`, `(D₁, D₂) ↦ D₁ + D₂`, classifies the sum of
> the two families, and is finite locally free of degree `(d₁ + d₂).choose d₁`.

```lean
theorem isFiniteLocallyFreeOfRank_addDivisors_of_isCurve [IsProper f] [IsCurve k f] [Smooth f]
    {d₁ d₂ : ℕ} {H₁ H₂ H : Over (Spec (.of k))}
    (h₁ : RepresentsHilbertFunctorOfRank (Over.mk f) H₁ d₁)
    (h₂ : RepresentsHilbertFunctorOfRank (Over.mk f) H₂ d₂)
    (h : RepresentsHilbertFunctorOfRank (Over.mk f) H (d₁ + d₂)) :
    haveI : SmoothOfRelativeDimension 1 (Over.mk f).hom :=
      smoothOfRelativeDimension_one_of_isCurve k f
    (∀ {T : Over (Spec (.of k))} (g : T ⟶ H₁ ⨯ H₂),
        h.family (g ≫ addDivisors h₁ h₂ h) =
          (h₁.family (g ≫ prod.fst)).add (h₂.family (g ≫ prod.snd))) ∧
      Morphisms.IsFiniteLocallyFreeOfRank (addDivisors h₁ h₂ h).left ((d₁ + d₂).choose d₁)
```

**`Stacks.Hilbert.exists_hilbertSchemes_of_isCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeProperCurve.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeProperCurve.lean#L111).

> **Stacks Project, Tag 0B9I.** Let `X` be a geometrically irreducible smooth proper curve over
> a field `k`. There are schemes `H d` representing the Hilbert functors `Hilb^d_{X/k}` such that
>
> 1. each `H d` is a smooth proper variety of dimension `d` over `k`;
> 2. for every field extension `k'/k`, the `k'`-rational points of `H d` are in bijection with the
>    effective Cartier divisors of degree `d` on `X_{k'}`, i.e. the closed subschemes of `X_{k'}`
>    which are effective Cartier divisors finite locally free of rank `d` over `k'`;
> 3. for `d₁, d₂ ≥ 0` the addition morphism `H d₁ ×_k H d₂ ⟶ H (d₁ + d₂)`,
>    `(D₁, D₂) ↦ D₁ + D₂`, is finite locally free of degree `(d₁ + d₂).choose d₁`.

```lean
theorem exists_hilbertSchemes_of_isCurve [IsProper f] [IsCurve k f] [Smooth f]
    [GeometricallyIrreducible f] :
    haveI : SmoothOfRelativeDimension 1 (Over.mk f).hom :=
      smoothOfRelativeDimension_one_of_isCurve k f
    ∃ (H : ℕ → Over (Spec (.of k)))
      (hH : ∀ d, RepresentsHilbertFunctorOfRank (Over.mk f) (H d) d),
      (∀ d, IsVariety k (H d).hom ∧ SmoothOfRelativeDimension d (H d).hom ∧
          IsProper (H d).hom ∧ topologicalKrullDim (H d).left = d) ∧
      (∀ (d : ℕ) (k' : Type u) [Field k'] [Algebra k k'],
        Nonempty ((fieldExtOver k k' ⟶ H d) ≃
          {I : ((Over.pullback (fieldExtOver k k').hom).obj (Over.mk f)).left.IdealSheafData //
            Stacks.Divisors.IsEffectiveCartierDivisor I ∧
              Stacks.Morphisms.IsFiniteLocallyFreeOfRank
                (I.subschemeι ≫ ((Over.pullback (fieldExtOver k k').hom).obj (Over.mk f)).hom)
                d})) ∧
      (∀ d₁ d₂ : ℕ,
        (∀ {T : Over (Spec (.of k))} (g : T ⟶ H d₁ ⨯ H d₂),
          (hH (d₁ + d₂)).family (g ≫ addDivisors (hH d₁) (hH d₂) (hH (d₁ + d₂))) =
            ((hH d₁).family (g ≫ prod.fst)).add ((hH d₂).family (g ≫ prod.snd))) ∧
        Morphisms.IsFiniteLocallyFreeOfRank
          (addDivisors (hH d₁) (hH d₂) (hH (d₁ + d₂))).left ((d₁ + d₂).choose d₁))
```

## Tag 0B9J, a remark

[Tag 0B9J](https://stacks.math.columbia.edu/tag/0B9J) in the Stacks Project.

**`Stacks.Hilbert.isRelativeEffectiveCartierDivisor_univ_iso_prod_and_restrict_picardClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeCurve.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/HilbertSchemeCurve.lean#L303).

> **Stacks Project, Tag 0B9J.** Let `X` be a smooth proper curve over a field `k`, let `d ≥ 0`,
> and let `H` and `H'` be schemes representing the Hilbert functors `Hilb^d_{X/k}` and
> `Hilb^{d+1}_{X/k}` (they exist by Tag 0B9I). Write `D_univ ⊆ X ×_k H'` for the universal closed
> subscheme. Then
>
> * `D_univ` is a relative effective Cartier divisor over `H'` (Tag 0B9D);
> * `D_univ` is isomorphic as a scheme to `H ×_k X`, by an isomorphism under which the inclusion
>   `D_univ ⊆ X ×_k H'` becomes `(D, x) ↦ (x, D + x)`, the point and point addition
>   `Stacks.Hilbert.addPoint` of Tag 0B9G (see the proof of Tag 0B9G);
> * in particular `D_univ` is an effective Cartier divisor on `X ×_k H'` and its sheaf
>   `𝒪(D_univ)` is invertible;
> * for a `k`-rational point `[D]` of `H'`, classifying the effective Cartier divisor `D` of degree
>   `d + 1` on the fibre `[D] × X = X ×_k k`, the restriction of `𝒪(D_univ)` to that fibre is
>   `𝒪_X(D)`, as classes in the Picard group of the fibre.
>
> The source assumes `X` geometrically irreducible, as in Tag 0B9I; that hypothesis is not used, and
> is dropped.

```lean
theorem isRelativeEffectiveCartierDivisor_univ_iso_prod_and_restrict_picardClass [IsProper f]
    [IsCurve k f] [Smooth f] (d : ℕ) (H H' : Over (Spec (.of k)))
    (hH : RepresentsHilbertFunctorOfRank (Over.mk f) H d)
    (hH' : RepresentsHilbertFunctorOfRank (Over.mk f) H' (d + 1)) :
    haveI : SmoothOfRelativeDimension 1 (Over.mk f).hom :=
      smoothOfRelativeDimension_one_of_isCurve k f
    haveI : IsSeparated (Over.mk f).hom := inferInstanceAs (IsSeparated f)
    Stacks.Divisors.IsRelativeEffectiveCartierDivisor ((Over.pullback H'.hom).obj (Over.mk f)).hom
        (hH'.family (𝟙 H')).ideal ∧
      (∃ e : (H ⨯ Over.mk f).left ≅ (hH'.family (𝟙 H')).ideal.subscheme,
        e.hom ≫ (hH'.family (𝟙 H')).ideal.subschemeι ≫ pullback.fst f H'.hom =
            (prod.snd : H ⨯ Over.mk f ⟶ Over.mk f).left ∧
          e.hom ≫ (hH'.family (𝟙 H')).ideal.subschemeι ≫ pullback.snd f H'.hom =
            (addPoint hH hH').left) ∧
      Stacks.Divisors.IsEffectiveCartierDivisor (hH'.family (𝟙 H')).ideal ∧
      AlgebraicGeometry.SheafOfModules.IsInvertible _
        (_root_.structureSheafRing
          ((Over.pullback H'.hom).obj (Over.mk f)).left.toRingedSpace).property
        (Stacks.Divisors.invertibleSheaf' (hH'.family (𝟙 H')).ideal) ∧
      ∀ x : Over.mk (𝟙 (Spec (.of k))) ⟶ H',
        Stacks.Picard.schemePullbackClass (familyBaseChangeMap (Over.mk f) x)
          (hH'.family (𝟙 H')).picardClass = (hH'.family x).picardClass
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 44.3, Tag 0B9C](https://stacks.math.columbia.edu/tag/0B9C)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
