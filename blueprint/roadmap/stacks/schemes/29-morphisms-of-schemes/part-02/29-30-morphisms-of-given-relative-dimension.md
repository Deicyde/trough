---
declaration: section
origin: cited
lean: AlgebraicGeometry.RelativeDimensionLEAt, AlgebraicGeometry.RelativeDimensionLE, AlgebraicGeometry.RelativeDimension, AlgebraicGeometry.equidimensional_and_topologicalKrullDim_of_relativeDimension, AlgebraicGeometry.RelativeDimension.of_isPullback, AlgebraicGeometry.RelativeDimensionLE.of_isPullback, AlgebraicGeometry.RelativeDimensionLE.comp, AlgebraicGeometry.RelativeDimension.comp_of_flat
statement: formalized
proof: formalized
---

# 29.30 Morphisms of given relative dimension

Section 29.30 of the Stacks Project, [Tag 02NI](https://stacks.math.columbia.edu/tag/02NI). 6 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02NJ, a definition

[Tag 02NJ](https://stacks.math.columbia.edu/tag/02NJ) in the Stacks Project.

**`AlgebraicGeometry.RelativeDimensionLEAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/RelativeDimension.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/RelativeDimension.lean#L55). The attribute's comment: “part (1)”.

> A locally finite type morphism `f : X ⟶ S` has relative dimension at most `d` at
> `x : X` if the local Krull dimension of the fibre over `f x` at its point corresponding to `x`
> is at most `d`.

```lean
public def RelativeDimensionLEAt {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (d : ℕ) (x : X) : Prop
```

**`AlgebraicGeometry.RelativeDimensionLE`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/RelativeDimension.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/RelativeDimension.lean#L62). The attribute's comment: “part (2)”.

> A locally finite type morphism has relative dimension at most `d` if it does so at every
> point of its source.

```lean
public abbrev RelativeDimensionLE {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (d : ℕ) : Prop
```

**`AlgebraicGeometry.RelativeDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/RelativeDimension.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/RelativeDimension.lean#L69). The attribute's comment: “part (3)”.

> A locally finite type morphism has relative dimension `d` if every nonempty fibre is
> equidimensional and has topological Krull dimension `d`.

```lean
public def RelativeDimension {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (d : ℕ) : Prop
```

**`AlgebraicGeometry.equidimensional_and_topologicalKrullDim_of_relativeDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphCodimension.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphCodimension.lean#L88). The attribute's comment: “over a field”.

> **Over a field, constant fibre dimension `d` is equidimensionality of dimension `d`.** The
> spectrum of a field has a single point whose residue field is the field itself, so the only
> nonempty fibre is the scheme itself.

```lean
theorem equidimensional_and_topologicalKrullDim_of_relativeDimension (k : Type u) [Field k]
    {T : Scheme.{u}} (q : T ⟶ Spec (.of k)) [LocallyOfFiniteType q] [Nonempty T] (d : ℕ)
    (h : AlgebraicGeometry.RelativeDimension q d) :
    TopologicalSpace.Equidimensional T ∧ topologicalKrullDim T = (d : WithBot ℕ∞)
```

## Tag 02NK, a lemma

[Tag 02NK](https://stacks.math.columbia.edu/tag/02NK) in the Stacks Project.

**`AlgebraicGeometry.RelativeDimension.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/BaseChange.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/BaseChange.lean#L74). The attribute's comment: “relative dimension d”.

> **Stacks Project, Tag 02NK.** Relative dimension `d` in the sense of Tag 02NJ is preserved by
> an arbitrary base change: every nonempty fibre of the base change has local dimension `d` at each
> of its points, hence is equidimensional of dimension `d`.

```lean
public theorem RelativeDimension.of_isPullback {X' X S' S : Scheme.{u}} {g' : X' ⟶ X}
    {f' : X' ⟶ S'} {f : X ⟶ S} {g : S' ⟶ S} (hsq : IsPullback g' f' f g)
    [LocallyOfFiniteType f] {d : ℕ} (hf : RelativeDimension f d) :
    letI : LocallyOfFiniteType f' := MorphismProperty.of_isPullback hsq inferInstance
    RelativeDimension f' d
```

**`AlgebraicGeometry.RelativeDimensionLE.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/BaseChange.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/BaseChange.lean#L98). The attribute's comment: “relative dimension at most d”.

> **Stacks Project, Tag 02NK.** A bound `≤ d` on the relative dimension in the sense of
> Tag 02NJ is preserved by an arbitrary base change, because the local dimension of a fibre is
> unchanged along the square.

```lean
public theorem RelativeDimensionLE.of_isPullback {X' X S' S : Scheme.{u}} {g' : X' ⟶ X}
    {f' : X' ⟶ S'} {f : X ⟶ S} {g : S' ⟶ S} (hsq : IsPullback g' f' f g)
    [LocallyOfFiniteType f] {d : ℕ} (hf : RelativeDimensionLE f d) :
    letI : LocallyOfFiniteType f' := MorphismProperty.of_isPullback hsq inferInstance
    RelativeDimensionLE f' d
```

## Tag 02NL, a lemma

[Tag 02NL](https://stacks.math.columbia.edu/tag/02NL) in the Stacks Project.

**`AlgebraicGeometry.RelativeDimensionLE.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Composition.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Composition.lean#L66). The attribute's comment: “the inequality”.

> **Stacks Project, Tag 02NL.** If `f` has relative dimension at most `d` and `g` has relative
> dimension at most `e`, then `f ≫ g` has relative dimension at most `d + e`.

```lean
public theorem RelativeDimensionLE.comp (f : X ⟶ Y) (g : Y ⟶ S) [LocallyOfFiniteType f]
    [LocallyOfFiniteType g] {d e : ℕ} (hf : RelativeDimensionLE f d)
    (hg : RelativeDimensionLE g e) : RelativeDimensionLE (f ≫ g) (d + e)
```

**`AlgebraicGeometry.RelativeDimension.comp_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Composition.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Composition.lean#L79). The attribute's comment: “the exact relative dimension of a flat composition”.

> **Stacks Project, Tag 02NL.** If `f` has relative dimension `d`, `g` has relative dimension
> `e` and `f` is flat, then `f ≫ g` has relative dimension `d + e`.

```lean
public theorem RelativeDimension.comp_of_flat (f : X ⟶ Y) (g : Y ⟶ S) [LocallyOfFiniteType f]
    [LocallyOfFiniteType g] [Flat f] {d e : ℕ} (hf : RelativeDimension f d)
    (hg : RelativeDimension g e) : RelativeDimension (f ≫ g) (d + e)
```

## Tag 02NM, a lemma

[Tag 02NM](https://stacks.math.columbia.edu/tag/02NM) in the Stacks Project.

**`AlgebraicGeometry.relativeDimensionFunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayRelativeDimension.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayRelativeDimension.lean#L370). The attribute's comment: “relative dimension function”.

> The locally constant function giving the relative dimension of a flat, locally finitely
> presented morphism with Cohen–Macaulay fibres.

```lean
public noncomputable def relativeDimensionFunction
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f]
    (hCM : ∀ s : S, IsCohenMacaulay (f.fiber s)) : LocallyConstant X ℕ
```

**`AlgebraicGeometry.relativeDimensionFunction_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayRelativeDimension.lean, line 462](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayRelativeDimension.lean#L462). The attribute's comment: “pointwise relative dimension”.

> At a point, the relative dimension function is the local Krull dimension of its fibre.

```lean
public theorem relativeDimensionFunction_apply
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f]
    (hCM : ∀ s : S, IsCohenMacaulay (f.fiber s)) (x : X) :
    topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) =
      ((relativeDimensionFunction f hCM x : ℕ) : WithBot ℕ∞)
```

**`AlgebraicGeometry.relativeDimensionOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayRelativeDimension.lean, line 474](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayRelativeDimension.lean#L474). The attribute's comment: “canonical dimension pieces”.

> The canonical open subscheme where the relative dimension is `d`.

```lean
public def relativeDimensionOpen
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f]
    (hCM : ∀ s : S, IsCohenMacaulay (f.fiber s)) (d : ℕ) : X.Opens
```

**`AlgebraicGeometry.relativeDimensionOpen_isClopen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayRelativeDimension.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayRelativeDimension.lean#L482). The attribute's comment: “canonical pieces are clopen”.

> Every canonical relative-dimension piece is open and closed.

```lean
public theorem relativeDimensionOpen_isClopen
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f]
    (hCM : ∀ s : S, IsCohenMacaulay (f.fiber s)) (d : ℕ) :
    IsClopen (relativeDimensionOpen f hCM d : Set X)
```

**`AlgebraicGeometry.iSup_relativeDimensionOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayRelativeDimension.lean, line 502](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayRelativeDimension.lean#L502). The attribute's comment: “canonical pieces cover”.

> The canonical relative-dimension pieces cover the source.

```lean
public theorem iSup_relativeDimensionOpen
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f]
    (hCM : ∀ s : S, IsCohenMacaulay (f.fiber s)) :
    ⨆ d : ℕ, relativeDimensionOpen f hCM d = ⊤
```

**`AlgebraicGeometry.pairwise_disjoint_relativeDimensionOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayRelativeDimension.lean, line 517](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayRelativeDimension.lean#L517). The attribute's comment: “canonical pieces are disjoint”.

> Distinct canonical relative-dimension pieces are disjoint.

```lean
public theorem pairwise_disjoint_relativeDimensionOpen
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f]
    (hCM : ∀ s : S, IsCohenMacaulay (f.fiber s)) :
    Pairwise (Disjoint on relativeDimensionOpen f hCM)
```

**`AlgebraicGeometry.relativeDimensionOpen_relativeDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayRelativeDimension.lean, line 532](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayRelativeDimension.lean#L532). The attribute's comment: “canonical pieces have pure relative dimension”.

> The restriction of the morphism to its `d`-dimensional locus has relative dimension `d`.

```lean
public theorem relativeDimensionOpen_relativeDimension
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f]
    (hCM : ∀ s : S, IsCohenMacaulay (f.fiber s)) (d : ℕ) :
    RelativeDimension ((relativeDimensionOpen f hCM d).ι ≫ f) d
```

**`AlgebraicGeometry.exists_clopen_relativeDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayRelativeDimension.lean, line 581](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayRelativeDimension.lean#L581).

> **Stacks Project, Tag 02NM.** A flat morphism locally of finite presentation with
> Cohen–Macaulay fibres is the disjoint union of clopen subschemes of pure relative dimension.

```lean
public theorem exists_clopen_relativeDimension
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f]
    (hCM : ∀ s : S, IsCohenMacaulay (f.fiber s)) :
    ∃ U : ℕ → X.Opens,
      (∀ d : ℕ, IsClopen (U d : Set X)) ∧
      (iSup U = ⊤) ∧
      Pairwise (Disjoint on U) ∧
      (∀ d : ℕ, RelativeDimension ((U d).ι ≫ f) d)
```

## Tag 0397, a lemma

[Tag 0397](https://stacks.math.columbia.edu/tag/0397) in the Stacks Project.

**`AlgebraicGeometry.quasiFiniteAt_of_fiberDimensionAt_le_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/MaxSliceQuasiFinite.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/MaxSliceQuasiFinite.lean#L63). The attribute's comment: “a zero-dimensional fibre point is a quasi-finite point”.

> A morphism locally of finite type is quasi-finite at a point whose fibre has local dimension
> at most zero there: local dimensions are nonnegative, so the bound makes the dimension zero.

```lean
public theorem quasiFiniteAt_of_fiberDimensionAt_le_zero {X S : Scheme.{u}}
    (f : X ⟶ S) [LocallyOfFiniteType f] (x : X)
    (hx : topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) ≤ 0) :
    f.QuasiFiniteAt x
```

**`AlgebraicGeometry.locallyQuasiFinite_of_relativeDimensionLE_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/MaxSliceQuasiFinite.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/MaxSliceQuasiFinite.lean#L73). The attribute's comment: “relative dimension at most zero implies locally quasi-finite”.

> A morphism locally of finite type of relative dimension at most zero is locally
> quasi-finite.

```lean
public theorem locallyQuasiFinite_of_relativeDimensionLE_zero {X S : Scheme.{u}}
    (f : X ⟶ S) [LocallyOfFiniteType f] (hf : RelativeDimensionLE f 0) :
    LocallyQuasiFinite f
```

**`AlgebraicGeometry.quasiFiniteAt_iff_fiberDimensionAt_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/QuasiFinite.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/QuasiFinite.lean#L65). The attribute's comment: “pointwise characterization”.

> A morphism locally of finite type is quasi-finite at a point if and only if the local
> dimension of its fibre at that point is zero.

```lean
public theorem quasiFiniteAt_iff_fiberDimensionAt_eq_zero
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] (x : X) :
    quasiFiniteAt f x ↔
      topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) = 0
```

**`AlgebraicGeometry.locallyQuasiFinite_iff_relativeDimension_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/QuasiFinite.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/QuasiFinite.lean#L76). The attribute's comment: “global characterization”.

> A morphism locally of finite type is locally quasi-finite if and only if it has relative
> dimension zero.

```lean
public theorem locallyQuasiFinite_iff_relativeDimension_zero
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] :
    LocallyQuasiFinite f ↔ RelativeDimension f 0
```

## Tag 0AFE, a lemma

[Tag 0AFE](https://stacks.math.columbia.edu/tag/0AFE) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDimAt_eq_add_of_relativeDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayDimensionFormula.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayDimensionFormula.lean#L187).

> **Stacks Project, Tag 0AFE.** A flat morphism locally of finite type of relative dimension
> `d` between locally Noetherian schemes raises the local dimension by `d`:
> `dim_x(X) = dim_{f x}(Y) + d`.
>
> This is also the input to the dimension formula for a Cohen-Macaulay morphism.

```lean
public theorem topologicalKrullDimAt_eq_add_of_relativeDimension {X Y : Scheme.{u}}
    [IsLocallyNoetherian X] [IsLocallyNoetherian Y] (f : X ⟶ Y) [Flat f] [LocallyOfFiniteType f]
    {d : ℕ} (hf : RelativeDimension f d) (x : X) :
    topologicalKrullDimAt X x = topologicalKrullDimAt Y (f x) + (d : WithBot ℕ∞)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.30, Tag 02NI](https://stacks.math.columbia.edu/tag/02NI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
