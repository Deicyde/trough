---
declaration: section
origin: cited
lean: AlgebraicGeometry.topologicalKrullDimAt_fiber_eq_krullDimOfRing_stalk_add_trdeg, AlgebraicGeometry.topologicalKrullDimAt_fiber_eq_ringKrullDim_stalk_add_trdeg, AlgebraicGeometry.topologicalKrullDimAt_fiber_comp_le_add, AlgebraicGeometry.topologicalKrullDimAt_fiber_comp_eq_add_of_isFlatAt_fiberMapOfComp, AlgebraicGeometry.topologicalKrullDimAt_fiber_comp_eq_add_of_isFlatAt, AlgebraicGeometry.topologicalKrullDimAt_fiber_eq_of_isPullback, AlgebraicGeometry.fiberMap_ringKrullDim_stalk_add_eq, AlgebraicGeometry.fiberMap_ringKrullDim_stalk_add_trdeg_eq
statement: formalized
proof: formalized
---

# 29.29 Morphisms and dimensions of fibres

Section 29.29 of the Stacks Project, [Tag 02FW](https://stacks.math.columbia.edu/tag/02FW). 7 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02FX, a lemma

[Tag 02FX](https://stacks.math.columbia.edu/tag/02FX) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDimAt_fiber_eq_krullDimOfRing_stalk_add_trdeg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/F6Rank128/FiberDimension.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/F6Rank128/FiberDimension.lean#L50).

> **Stacks Project, Tag 02FX.** For a morphism locally of finite type, the dimension of the
> fibre at a point is the dimension of the local ring of the fibre there plus the transcendence
> degree of the residue-field extension.

```lean
theorem topologicalKrullDimAt_fiber_eq_krullDimOfRing_stalk_add_trdeg
    (f : X ⟶ S) [LocallyOfFiniteType f] (x : X) :
    letI := (f.residueFieldMap x).hom.toAlgebra
    topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) =
      ringKrullDim ((f.fiber (f x)).presheaf.stalk (f.asFiber x)) +
        (Cardinal.toENat (Algebra.trdeg (S.residueField (f x)) (X.residueField x)) :
          WithBot ℕ∞)
```

**`AlgebraicGeometry.topologicalKrullDimAt_fiber_eq_ringKrullDim_stalk_add_trdeg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FiniteOverSmoothInputs/FibreDimensionFormula.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FiniteOverSmoothInputs/FibreDimensionFormula.lean#L97). References: EGA IV (17.15.8), “more general”; SGA 1 II (5.8), “n = p + trdeg_k κ(x)”.

> For a morphism locally of finite type, the dimension of the fibre at a point is the Krull
> dimension of the local ring of the fibre there plus the transcendence degree of the residue field
> extension.

```lean
theorem topologicalKrullDimAt_fiber_eq_ringKrullDim_stalk_add_trdeg
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] (x : X) :
    letI := (f.residueFieldMap x).hom.toAlgebra
    topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) =
      ringKrullDim ((f.fiber (f x)).presheaf.stalk (f.asFiber x)) +
        (Cardinal.toENat (Algebra.trdeg (S.residueField (f x)) (X.residueField x)) :
          WithBot ℕ∞)
```

## Tag 02JS, a lemma

[Tag 02JS](https://stacks.math.columbia.edu/tag/02JS) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDimAt_fiber_comp_le_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/Composite.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/Composite.lean#L153). The attribute's comment: “the inequality”.

> For two morphisms locally of finite type, the dimension at a point of a fibre of their
> composition is at most the sum of the dimensions, at the corresponding points, of the two
> successive fibres.

```lean
theorem topologicalKrullDimAt_fiber_comp_le_add (f : X ⟶ Y) (g : Y ⟶ S)
    [LocallyOfFiniteType f] [LocallyOfFiniteType g] (x : X) :
    topologicalKrullDimAt ((f ≫ g).fiber ((f ≫ g) x)) ((f ≫ g).asFiber x) ≤
      topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) +
        topologicalKrullDimAt (g.fiber (g (f x))) (g.asFiber (f x))
```

**`AlgebraicGeometry.topologicalKrullDimAt_fiber_comp_eq_add_of_isFlatAt_fiberMapOfComp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/Composite.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/Composite.lean#L256). The attribute's comment: “equality for a flat morphism of fibres”.

> The dimension inequality for a composition is an equality as soon as the induced morphism
> between the fibres is flat at the point.

```lean
theorem topologicalKrullDimAt_fiber_comp_eq_add_of_isFlatAt_fiberMapOfComp (f : X ⟶ Y)
    (g : Y ⟶ S) [LocallyOfFiniteType f] [LocallyOfFiniteType g] (x : X)
    (hflat : IsFlatAt (fiberMapOfComp f g ((f ≫ g) x)).toLRSHom.toShHom
      ((f ≫ g).asFiber x)) :
    topologicalKrullDimAt ((f ≫ g).fiber ((f ≫ g) x)) ((f ≫ g).asFiber x) =
      topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) +
        topologicalKrullDimAt (g.fiber (g (f x))) (g.asFiber (f x))
```

**`AlgebraicGeometry.topologicalKrullDimAt_fiber_comp_eq_add_of_isFlatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/Composite.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/Composite.lean#L310). The attribute's comment: “equality when the first morphism is flat”.

> The dimension inequality for a composition is an equality as soon as the first morphism is
> flat at the point.

```lean
theorem topologicalKrullDimAt_fiber_comp_eq_add_of_isFlatAt (f : X ⟶ Y) (g : Y ⟶ S)
    [LocallyOfFiniteType f] [LocallyOfFiniteType g] (x : X)
    (hflat : IsFlatAt f.toLRSHom.toShHom x) :
    topologicalKrullDimAt ((f ≫ g).fiber ((f ≫ g) x)) ((f ≫ g).asFiber x) =
      topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) +
        topologicalKrullDimAt (g.fiber (g (f x))) (g.asFiber (f x))
```

## Tag 02FY, a lemma

[Tag 02FY](https://stacks.math.columbia.edu/tag/02FY) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDimAt_fiber_eq_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/Basic.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/Basic.lean#L235). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 02FY part (1).** In a fibre product diagram with `f` locally of finite
> type, the fibre of the base change `f'` has the same dimension at `x'` as the fibre of `f` has
> at the image of `x'`.

```lean
public theorem topologicalKrullDimAt_fiber_eq_of_isPullback {X' X S' S : Scheme.{u}}
    {g' : X' ⟶ X} {f' : X' ⟶ S'} {f : X ⟶ S} {g : S' ⟶ S}
    (hsq : IsPullback g' f' f g) [LocallyOfFiniteType f] (x' : X') :
    topologicalKrullDimAt ↥(f'.fiber (f' x')) (f'.asFiber x') =
      topologicalKrullDimAt ↥(f.fiber (f (g' x'))) (f.asFiber (g' x'))
```

**`AlgebraicGeometry.fiberMap_ringKrullDim_stalk_add_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/LocalRing.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/LocalRing.lean#L208). The attribute's comment: “local_ring_differences”.

> **Stacks Project, Tag 02FY part (2).** In a fibre product diagram with `f` locally of finite
> type, the dimension of the local ring at `x'` of the fibre of the induced morphism of fibres, plus
> the dimension of the local ring of `X_s` at `x = g' x'`, is the dimension of the local ring of
> `X'_{s'}` at `x'`.

```lean
public theorem fiberMap_ringKrullDim_stalk_add_eq (hsq : IsPullback g' f' f g)
    [LocallyOfFiniteType f] (x' : X') :
    ringKrullDim (((fiberMap f' g' g f hsq.w (f' x')).fiber
            (fiberMap f' g' g f hsq.w (f' x') (f'.asFiber x'))).presheaf.stalk
          ((fiberMap f' g' g f hsq.w (f' x')).asFiber (f'.asFiber x'))) +
        ringKrullDim ((f.fiber (g (f' x'))).presheaf.stalk
          (fiberMap f' g' g f hsq.w (f' x') (f'.asFiber x'))) =
      ringKrullDim ((f'.fiber (f' x')).presheaf.stalk (f'.asFiber x'))
```

**`AlgebraicGeometry.fiberMap_ringKrullDim_stalk_add_trdeg_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/LocalRing.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/LocalRing.lean#L229). The attribute's comment: “local_ring_differences”.

> **Stacks Project, Tag 02FY part (2).** The same dimension is the loss of residue-field
> transcendence degree: the dimension of the local ring at `x'` of the fibre of the induced
> morphism of fibres, plus `trdeg_{κ(s')} κ(x')`, is `trdeg_{κ(s)} κ(x)`.

```lean
public theorem fiberMap_ringKrullDim_stalk_add_trdeg_eq (hsq : IsPullback g' f' f g)
    [LocallyOfFiniteType f] (x' : X') :
    letI := (f.residueFieldMap (g' x')).hom.toAlgebra
    letI := (f'.residueFieldMap x').hom.toAlgebra
    ringKrullDim (((fiberMap f' g' g f hsq.w (f' x')).fiber
            (fiberMap f' g' g f hsq.w (f' x') (f'.asFiber x'))).presheaf.stalk
          ((fiberMap f' g' g f hsq.w (f' x')).asFiber (f'.asFiber x'))) +
        (Cardinal.toENat (Algebra.trdeg ↥(S'.residueField (f' x')) ↥(X'.residueField x')) :
          WithBot ℕ∞) =
      (Cardinal.toENat (Algebra.trdeg ↥(S.residueField (f (g' x'))) ↥(X.residueField (g' x'))) :
        WithBot ℕ∞)
```

**`AlgebraicGeometry.ringKrullDim_stalk_fiber_le_of_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/LocalRing.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/LocalRing.lean#L267). The attribute's comment: “local_ring_differences”.

> **Stacks Project, Tag 02FY part (2).** The dimension of the local ring of a fibre cannot drop
> under base change.

```lean
public theorem ringKrullDim_stalk_fiber_le_of_baseChange (hsq : IsPullback g' f' f g)
    [LocallyOfFiniteType f] (x' : X') :
    ringKrullDim ((f.fiber (g (f' x'))).presheaf.stalk
        (fiberMap f' g' g f hsq.w (f' x') (f'.asFiber x'))) ≤
      ringKrullDim ((f'.fiber (f' x')).presheaf.stalk (f'.asFiber x'))
```

**`AlgebraicGeometry.trdeg_residueField_le_of_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/LocalRing.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/LocalRing.lean#L278). The attribute's comment: “local_ring_differences”.

> **Stacks Project, Tag 02FY part (2).** The transcendence degree of the residue-field
> extension cannot grow under base change.

```lean
public theorem trdeg_residueField_le_of_baseChange (hsq : IsPullback g' f' f g)
    [LocallyOfFiniteType f] (x' : X') :
    letI := (f.residueFieldMap (g' x')).hom.toAlgebra
    letI := (f'.residueFieldMap x').hom.toAlgebra
    Algebra.trdeg ↥(S'.residueField (f' x')) ↥(X'.residueField x') ≤
      Algebra.trdeg ↥(S.residueField (f (g' x'))) ↥(X.residueField (g' x'))
```

**`AlgebraicGeometry.exists_pullback_point_preserving_fibre_dimension_and_trdeg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/LocalRing.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/LocalRing.lean#L358). The attribute's comment: “zero_difference_lift”.

> **Stacks Project, Tag 02FY part (3).** In a fibre product diagram with `f` locally of finite
> type, let `s'` be a point of `S'` and `x` a point of `X` with the same image `s` in `S`. Then
> there is a common lift `x'` of `x` and `s'` to `X'` at which neither the dimension of the local
> ring of the fibre nor the transcendence degree of the residue-field extension changes.

```lean
public theorem exists_pullback_point_preserving_fibre_dimension_and_trdeg
    (hpb : IsPullback g' f' f g) [LocallyOfFiniteType f] (s' : S') (x : X) (h : f x = g s') :
    ∃ (x' : X') (_hx : g' x' = x) (hs' : f' x' = s'),
      ringKrullDim ((f'.fiber s').presheaf.stalk ((f'.fiberHomeo s').symm ⟨x', hs'⟩)) =
          ringKrullDim ((f.fiber (g s')).presheaf.stalk
            ((f.fiberHomeo (g s')).symm ⟨x, h⟩)) ∧
        (letI := ((S.residueFieldCongr h).inv ≫ f.residueFieldMap x).hom.toAlgebra
         letI := ((S'.residueFieldCongr hs').inv ≫ f'.residueFieldMap x').hom.toAlgebra
         Algebra.trdeg ↥(S.residueField (g s')) ↥(X.residueField x) =
           Algebra.trdeg ↥(S'.residueField s') ↥(X'.residueField x'))
```

## Tag 02FZ, a lemma

[Tag 02FZ](https://stacks.math.columbia.edu/tag/02FZ) in the Stacks Project.

**`AlgebraicGeometry.isOpen_setOf_fiberDimensionAt_le`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Openness.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Openness.lean#L78). References: EGA IV (13.1.3).

> **Stacks Project, Tag 02FZ.** For a locally finite type morphism of schemes, the locus where
> the local dimension of the fibre is at most `n` is open.

```lean
public lemma isOpen_setOf_fiberDimensionAt_le {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (n : ℕ) :
    IsOpen {x : X |
      topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) ≤ (n : WithBot ℕ∞)}
```

## Tag 0A3V, a lemma

[Tag 0A3V](https://stacks.math.columbia.edu/tag/0A3V) in the Stacks Project.

**`AlgebraicGeometry.exists_topologicalKrullDim_fiber_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Bounded.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Bounded.lean#L78).

> **Stacks Project, Tag 0A3V.** The dimensions of the fibres of a finite-type morphism to a
> quasi-compact scheme are bounded by a single natural number.

```lean
public theorem exists_topologicalKrullDim_fiber_le
    {X Y : Scheme.{u}} (f : X ⟶ Y) [LocallyOfFiniteType f] [QuasiCompact f]
    [CompactSpace Y] :
    ∃ n : ℕ, ∀ y : Y, topologicalKrullDim (f.fiber y) ≤ n
```

## Tag 02G0, a lemma

[Tag 02G0](https://stacks.math.columbia.edu/tag/02G0) in the Stacks Project.

**`AlgebraicGeometry.isRetrocompact_setOf_fiberDimensionAt_le`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Openness.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Openness.lean#L160).

> **Stacks Project, Tag 02G0.** For a morphism of schemes locally of finite presentation, the
> locus where the local dimension of the fibre is at most `n` is retrocompact.

```lean
public lemma isRetrocompact_setOf_fiberDimensionAt_le {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFinitePresentation f] (n : ℕ) :
    IsRetrocompact {x : X |
      topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) ≤ (n : WithBot ℕ∞)}
```

## Tag 06RU, a lemma

[Tag 06RU](https://stacks.math.columbia.edu/tag/06RU) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDimAt_fiber_le_of_specialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Specialization.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Specialization.lean#L49). The attribute's comment: “fiber_dimension_monotone”.

> Local dimension in a fibre is monotone along a specialization of points with a common
> image in the base.

```lean
public theorem topologicalKrullDimAt_fiber_le_of_specialization {X S : Scheme.{u}}
    (f : X ⟶ S) {x x' : X} (hxx' : x ⤳ x') {s : S}
    (hx : f x = s) (hx' : f x' = s) :
    topologicalKrullDimAt (f.fiber s) ((f.fiberHomeo s).symm ⟨x, hx⟩) ≤
      topologicalKrullDimAt (f.fiber s) ((f.fiberHomeo s).symm ⟨x', hx'⟩)
```

**`AlgebraicGeometry.ringKrullDim_fiber_stalk_lt_of_specialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Specialization.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Specialization.lean#L61). The attribute's comment: “fiber_local_dimension_strict”.

> A strict specialization inside a fibre of a locally finite type morphism strictly
> increases the dimension of the fibre's local ring.

```lean
public theorem ringKrullDim_fiber_stalk_lt_of_specialization
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    {x x' : X} (hxx' : x ⤳ x') (hne : x ≠ x')
    {s : S} (hx : f x = s) (hx' : f x' = s) :
    ringKrullDim ((f.fiber s).presheaf.stalk ((f.fiberHomeo s).symm ⟨x, hx⟩)) <
      ringKrullDim ((f.fiber s).presheaf.stalk ((f.fiberHomeo s).symm ⟨x', hx'⟩))
```

**`AlgebraicGeometry.trdeg_residueField_fiber_lt_of_specialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/SpecializationTrdeg.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/SpecializationTrdeg.lean#L172). The attribute's comment: “part (3): the strict inequality of transcendence degrees `trdeg_{κ(s)} κ(x) > trdeg_{κ(s)} κ(x')` along a nontrivial specialization `x ⤳ x'` inside a fibre, for `f` locally of finite type. Each residue field is a `κ(s)`-algebra through `AlgebraicGeometry.Scheme.Hom.residueFieldMap`, and the comparison is between Mathlib's cardinal-valued `Algebra.trdeg`. Parts (1) and (2) are `AlgebraicGeometry.topologicalKrullDimAt_fiber_le_of_specialization` and `AlgebraicGeometry.ringKrullDim_fiber_stalk_lt_of_specialization`.”.

> **Stacks 06RU, part (3).** Let `f : X ⟶ S` be locally of finite type and let `x ⤳ x'` be a
> nontrivial specialization of points of `X` lying over the same point `s` of `S`. Then the
> transcendence degree of `κ(x)` over `κ(s)` is strictly larger than that of `κ(x')`.

```lean
public theorem trdeg_residueField_fiber_lt_of_specialization (f : X ⟶ S)
    [LocallyOfFiniteType f] {x x' : X} (hxx' : x ⤳ x') (hne : x ≠ x')
    {s : S} (hx : f x = s) (hx' : f x' = s) :
    letI : Algebra (S.residueField s) (X.residueField x) :=
      ((S.residueFieldCongr hx).inv ≫ f.residueFieldMap x).hom.toAlgebra
    letI : Algebra (S.residueField s) (X.residueField x') :=
      ((S.residueFieldCongr hx').inv ≫ f.residueFieldMap x').hom.toAlgebra
    Algebra.trdeg (S.residueField s) (X.residueField x') <
      Algebra.trdeg (S.residueField s) (X.residueField x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.29, Tag 02FW](https://stacks.math.columbia.edu/tag/02FW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
