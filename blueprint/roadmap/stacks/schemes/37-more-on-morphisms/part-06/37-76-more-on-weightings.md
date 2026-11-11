---
declaration: section
origin: cited
lean: AlgebraicGeometry.isLocallyConstructible_weighting_levelSet, AlgebraicGeometry.isLocallyConstructible_separableDegreeWeightedFiberSum_levelSet, AlgebraicGeometry.IsWeighting.upperSemicontinuous, AlgebraicGeometry.lowerSemicontinuous_separableDegreeWeightedFiberSum, AlgebraicGeometry.exists_isGreatest_range_separableDegreeWeightedFiberSum, AlgebraicGeometry.exists_isFinite_restrict_separableDegreeWeightedFiberSum_maxLocus, Algebra.exists_finitePresentation_algebra_universal_for_idempotents, AlgebraicGeometry.exists_universal_finite_open_subscheme
statement: formalized
proof: formalized
---

# 37.76 More on weightings

Section 37.76 of the Stacks Project, [Tag 0F3F](https://stacks.math.columbia.edu/tag/0F3F). 9 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F3G, a lemma

[Tag 0F3G](https://stacks.math.columbia.edu/tag/0F3G) in the Stacks Project.

**`AlgebraicGeometry.isLocallyConstructible_weighting_levelSet`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/LevelSetConstructible.lean, line 657](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/LevelSetConstructible.lean#L657).

> **Stacks Project, Tag 0F3G.** The level sets of a weighting of a locally quasi-finite
> morphism are locally constructible in the source.
>
> Quasi-finiteness being local, the hypothesis is `AlgebraicGeometry.LocallyQuasiFinite` together
> with `AlgebraicGeometry.LocallyOfFiniteType`, which is Stacks 01TD's pointwise characterization
> of a locally quasi-finite morphism.

```lean
theorem isLocallyConstructible_weighting_levelSet
    {X Y : Scheme.{u}} {f : X ⟶ Y} [LocallyOfFiniteType f] [LocallyQuasiFinite f]
    {w : X → ℤ} (hw : IsWeighting f w) (n : ℤ) :
    IsLocallyConstructible {x : X | w x = n}
```

## Tag 0F3H, a lemma

[Tag 0F3H](https://stacks.math.columbia.edu/tag/0F3H) in the Stacks Project.

**`AlgebraicGeometry.isLocallyConstructible_separableDegreeWeightedFiberSum_levelSet`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FibreSumLevelSetConstructible.lean, line 618](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FibreSumLevelSetConstructible.lean#L618).

> **Stacks Project, Tag 0F3H.** Each level set of the weighted fibre sum of a weighting of a
> locally quasi-finite morphism of finite presentation is locally constructible on the target.
>
> The statement is local on the target, so one restricts to an affine open of it; the restricted
> morphism is again locally quasi-finite of finite presentation and the restricted weight is again
> a weighting, by [Stacks, Tag 0F3B], while the weighted fibre sum commutes with the restriction by
> [Stacks, Tag 0F39].

```lean
theorem isLocallyConstructible_separableDegreeWeightedFiberSum_levelSet
    {X Y : Scheme.{u}} (f : X ⟶ Y) [LocallyQuasiFinite f] (hf : FinitePresentation f)
    (w : X → ℤ) (hw : IsWeighting f w) (n : ℤ) :
    Topology.IsLocallyConstructible
      {y : Y | separableDegreeWeightedFiberSum f w y = n}
```

## Tag 0F3I, a lemma

[Tag 0F3I](https://stacks.math.columbia.edu/tag/0F3I) in the Stacks Project.

**`AlgebraicGeometry.IsWeighting.upperSemicontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/Semicontinuity.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/Semicontinuity.lean#L111).

> **Stacks Project, Tag 0F3I.** A positive weighting of a locally quasi-finite morphism is
> upper semicontinuous on its source.

```lean
theorem IsWeighting.upperSemicontinuous
    {X Y : Scheme.{u}} {f : X ⟶ Y} [LocallyOfFiniteType f]
    [LocallyQuasiFinite f] {w : X → ℤ}
    (hw : IsWeighting f w) (hpos : ∀ x, 0 < w x) :
    UpperSemicontinuous w
```

## Tag 0F3J, a lemma

[Tag 0F3J](https://stacks.math.columbia.edu/tag/0F3J) in the Stacks Project.

**`AlgebraicGeometry.lowerSemicontinuous_separableDegreeWeightedFiberSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/Semicontinuity.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/Semicontinuity.lean#L125). References: EGA IV (18.2.8), “semicontinuity of n(y)”.

> **Stacks Project, Tag 0F3J.** The weighted fibre sum of a positive weighting of a
> separated, locally quasi-finite morphism with finite fibres is lower semicontinuous.

```lean
theorem lowerSemicontinuous_separableDegreeWeightedFiberSum
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsSeparated f]
    [LocallyOfFiniteType f] [LocallyQuasiFinite f]
    (hfinite : ∀ y, (f ⁻¹' {y}).Finite) (w : X → ℤ)
    (hw : IsWeighting f w) (hpos : ∀ x, 0 < w x) :
    LowerSemicontinuous (separableDegreeWeightedFiberSum f w)
```

## Tag 0F3K, a lemma

[Tag 0F3K](https://stacks.math.columbia.edu/tag/0F3K) in the Stacks Project.

**`AlgebraicGeometry.exists_isGreatest_range_separableDegreeWeightedFiberSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FibreSumMaximum.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FibreSumMaximum.lean#L376). The attribute's comment: “the target is assumed nonempty”.

> **Stacks Project, Tag 0F3K.** The weighted fibre sum of a weighting of a locally quasi-finite
> morphism with quasi-compact source attains its maximum: its set of values has a greatest
> element.
>
> The target is assumed nonempty, which the source does not say and without which the set of
> values is empty and has no greatest element.

```lean
public theorem exists_isGreatest_range_separableDegreeWeightedFiberSum
    {X Y : Scheme.{u}} (f : X ⟶ Y) [LocallyOfFiniteType f] [LocallyQuasiFinite f]
    [CompactSpace X] [Nonempty Y] {w : X → ℤ} (hw : IsWeighting f w) :
    ∃ d : ℤ, IsGreatest (Set.range (separableDegreeWeightedFiberSum f w)) d
```

## Tag 0F3L, a lemma

[Tag 0F3L](https://stacks.math.columbia.edu/tag/0F3L) in the Stacks Project.

**`AlgebraicGeometry.exists_isFinite_restrict_separableDegreeWeightedFiberSum_maxLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/MaximalLocus.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/MaximalLocus.lean#L309).

> **Stacks Project, Tag 0F3L.** A separated locally quasi-finite morphism with finite fibres
> and a positive weighting is finite over the open locus where its weighted fibre sum attains its
> global maximum.

```lean
theorem exists_isFinite_restrict_separableDegreeWeightedFiberSum_maxLocus
    {X Y : Scheme.{u}} (f : X ⟶ Y) [LocallyOfFiniteType f]
    [LocallyQuasiFinite f] [IsSeparated f]
    (hfinite : ∀ y : Y, (f ⁻¹' {y}).Finite)
    (w : X → ℤ) (hw : IsWeighting f w)
    (hpositive : ∀ x : X, 0 < w x)
    (d : ℤ)
    (hmax : IsGreatest (Set.range (separableDegreeWeightedFiberSum f w)) d) :
    ∃ U : Y.Opens,
      (U : Set Y) = {y | separableDegreeWeightedFiberSum f w y = d} ∧
        IsFinite (f ∣_ U)
```

## Tag 0F3M, a lemma

[Tag 0F3M](https://stacks.math.columbia.edu/tag/0F3M) in the Stacks Project.

**`Algebra.exists_finitePresentation_algebra_universal_for_idempotents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/IdempotentUniversalAlgebra.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/IdempotentUniversalAlgebra.lean#L91).

> **Stacks Project, Tag 0F3M.** A finite, finitely presented algebra has a finitely
> presented weakly universal base change equipped with an idempotent: every idempotent after an
> arbitrary base change is the image of the universal one under some specialization.

```lean
theorem Algebra.exists_finitePresentation_algebra_universal_for_idempotents
    (A : Type u) [CommRing A] (B : Type v) [CommRing B] [Algebra A B]
    [Module.Finite A B] [Algebra.FinitePresentation A B] :
    ∃ (Auniv : Type (max u v)) (_ : CommRing Auniv) (_ : Algebra A Auniv)
      (_ : Algebra.FinitePresentation A Auniv)
      (euniv : B ⊗[A] Auniv),
      IsIdempotentElem euniv ∧
        ∀ (A' : Type w) [CommRing A'] [Algebra A A'] (e : B ⊗[A] A'),
          IsIdempotentElem e →
            ∃ f : Auniv →ₐ[A] A',
              Algebra.TensorProduct.map (AlgHom.id A B) f euniv = e
```

## Tag 0F3N, a lemma

[Tag 0F3N](https://stacks.math.columbia.edu/tag/0F3N) in the Stacks Project.

**`AlgebraicGeometry.exists_universal_finite_open_subscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/UniversalFiniteOpen.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/UniversalFiniteOpen.lean#L242).

> **Stacks Project, Tag 0F3N.** A quasi-finite morphism of finite presentation between affine
> schemes admits a base change of finite presentation carrying a universal finite open subscheme:
> every open subscheme of a base change along a morphism of affine schemes that is finite over the
> new base is the inverse image of this one.

```lean
theorem exists_universal_finite_open_subscheme
    {X Y : Scheme.{u}} [IsAffine X] [IsAffine Y] (f : X ⟶ Y)
    [LocallyQuasiFinite f] (hfp : FinitePresentation f) :
    ∃ (Yuniv : Scheme.{u}) (g : Yuniv ⟶ Y)
      (Uuniv : (pullback f g).Opens),
      FinitePresentation g ∧
        IsFinite (Uuniv.ι ≫ pullback.snd f g) ∧
      ∀ (Y' : Scheme.{u}) [IsAffine Y'] (g' : Y' ⟶ Y)
          (U' : (pullback f g').Opens),
          IsFinite (U'.ι ≫ pullback.snd f g') →
            ∃ (h : Y' ⟶ Yuniv) (hh : h ≫ g = g'),
              (pullback.lift (pullback.fst f g')
                (pullback.snd f g' ≫ h)
                (by rw [Category.assoc, hh]; exact pullback.condition)) ⁻¹ᵁ Uuniv = U'
```

## Tag 0F3P, a lemma

[Tag 0F3P](https://stacks.math.columbia.edu/tag/0F3P) in the Stacks Project.

**`AlgebraicGeometry.eventually_exists_weighting_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/LimitDescent/FiniteStage.lean, line 495](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/LimitDescent/FiniteStage.lean#L495).

> A weighting on the limit base change of a quasi-finite finitely presented
> morphism of affine schemes comes from a weighting at every sufficiently late
> stage of the directed inverse system.

```lean
theorem eventually_exists_weighting_baseChange
    {I : Type v} [Small.{u} I] [Preorder I] [IsDirected I (· ≤ ·)]
    (D : Iᵒᵖ ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    [∀ i : I, IsAffine (D.obj (op i))]
    (i₀ : I) (X₀ : Scheme.{u}) [IsAffine X₀]
    (f₀ : X₀ ⟶ D.obj (op i₀))
    (hfp : FinitePresentation f₀)
    [LocallyQuasiFinite f₀]
    (w : (pullback f₀ (c.π.app (op i₀)) : Scheme.{u}) → ℤ)
    (hw : IsWeighting
      (pullback.snd f₀ (c.π.app (op i₀))) w) :
    ∀ᶠ i in Filter.atTop, ∀ hi : i₀ ≤ i,
      ∃ wᵢ : (pullback f₀ (D.map (homOfLE hi).op) : Scheme.{u}) → ℤ,
        IsWeighting
          (pullback.snd f₀ (D.map (homOfLE hi).op)) wᵢ ∧
        w = wᵢ ∘ pullback.lift
          (pullback.fst f₀ (c.π.app (op i₀)))
          (pullback.snd f₀ (c.π.app (op i₀)) ≫ c.π.app (op i))
          (by
            rw [Category.assoc, c.w (homOfLE hi).op]
            exact pullback.condition)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.76, Tag 0F3F](https://stacks.math.columbia.edu/tag/0F3F)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
