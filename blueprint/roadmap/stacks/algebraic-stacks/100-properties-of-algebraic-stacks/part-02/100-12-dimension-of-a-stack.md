---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.dimensionSubNat_eq_dimensionSubNat_of_isSmooth, AlgebraicGeometry.Stack.exists_dimensionSubNat_eq_dimensionSubNat_of_isSmooth, AlgebraicGeometry.Stack.dimensionAtPoint, AlgebraicGeometry.Stack.dimensionAtPoint_eq_dimensionSubNat_zero_of_representing, AlgebraicGeometry.Stack.dimension, AlgebraicGeometry.Stack.exists_dimension_classifyingStack_additiveGroup_eq_neg_one, AlgebraicGeometry.Stack.exists_algebraicStack_dimension_lt_zero, AlgebraicGeometry.Stack.dimension_quotientStack_le
statement: formalized
proof: formalized
---

# 100.12 Dimension of a stack

Section 100.12 of the Stacks Project, [Tag 0AFL](https://stacks.math.columbia.edu/tag/0AFL). 4 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AFM, a lemma

[Tag 0AFM](https://stacks.math.columbia.edu/tag/0AFM) in the Stacks Project.

**`AlgebraicGeometry.Stack.dimensionSubNat_eq_dimensionSubNat_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DimensionChartIndependence.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DimensionChartIndependence.lean#L416).

> Let `𝒳` be a locally Noetherian algebraic stack over `S`, and let `f : T ⟶ 𝒳` and
> `f' : T' ⟶ 𝒳` be two smooth, locally-of-finite-type 1-morphisms from algebraic spaces, with
> points `t ∈ |T|` and `t' ∈ |T'|` with the same image in `|𝒳|`. If the relative dimensions of
> Stacks 0DRG of `f` at `t` and of `f'` at `t'` are the natural numbers `d` and `d'`, then
> `dim_t(T) - d = dim_{t'}(T') - d'`.

```lean
theorem dimensionSubNat_eq_dimensionSubNat_of_isSmooth
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    {T T' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hT : IsAlgebraicSpace B S hS T) (hT' : IsAlgebraicSpace B S hS T')
    (f : algebraicSpaceStack.{u, w} B S hS T hT ⟶ 𝒳)
    (f' : algebraicSpaceStack.{u, w} B S hS T' hT' ⟶ 𝒳)
    (hsm : AlgebraicStacks.IsSmooth B S hS f) (hsm' : AlgebraicStacks.IsSmooth B S hS f')
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (hf' : AlgebraicStacks.IsLocallyOfFiniteType B S hS f')
    (t : Space.points B S hS T) (t' : Space.points B S hS T')
    (hx : pointsMap B S hS (fibredCategory B S hS T).val
        (fibredCategory B S hS T).property 𝒳.val.property f.hom.hom
        (stackPointOfSpacePoint B S hS T t) =
      pointsMap B S hS (fibredCategory B S hS T').val
        (fibredCategory B S hS T').property 𝒳.val.property f'.hom.hom
        (stackPointOfSpacePoint B S hS T' t'))
    (d d' : ℕ)
    (hd : relativeDimensionAt.{u, w} B S hS T hT 𝒳 f hf t = (d : WithBot ℕ∞))
    (hd' : relativeDimensionAt.{u, w} B S hS T' hT' 𝒳 f' hf' t' = (d' : WithBot ℕ∞)) :
    dimensionSubNat (Space.dimensionAtPoint B S hS T hT t) d =
      dimensionSubNat (Space.dimensionAtPoint B S hS T' hT' t') d'
```

**`AlgebraicGeometry.Stack.exists_dimensionSubNat_eq_dimensionSubNat_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionFiniteness.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionFiniteness.lean#L136).

> Let `𝒳` be a locally Noetherian algebraic stack over `S`, let `f : T ⟶ 𝒳` and
> `f' : T' ⟶ 𝒳` be smooth, locally-of-finite-type 1-morphisms from algebraic spaces, and let
> `t ∈ |T|` and `t' ∈ |T'|` have the same image `x ∈ |𝒳|`. Then the relative dimensions of
> Stacks 0DRG of `f` at `t` and of `f'` at `t'` are natural numbers `d` and `d'`, and the two values
> of the formula of Stacks 0AFN agree: `dim_t(T) - d = dim_{t'}(T') - d'` in `ℤ ∪ {±∞}`.
>
> So the quantity `dim_u(U) - dim_{e(u)}(R_u)` of the source is defined — its subtrahend is
> finite — and does not depend on the presentation or on the point above `x` used to read it.
> A presentation `[U/R] → 𝒳` enters through the smooth, locally of finite type 1-morphism
> `U ⟶ 𝒳` it induces: the fibre `R_u` of the source map `s : R = U ×_𝒳 U ⟶ U` at the identity
> arrow `e(u)` is the fibre of that 1-morphism over a field-valued point representing `x`, so its
> local dimension there is the relative dimension of Stacks 0DRG subtracted here.

```lean
theorem exists_dimensionSubNat_eq_dimensionSubNat_of_isSmooth
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    {T T' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hT : IsAlgebraicSpace B S hS T) (hT' : IsAlgebraicSpace B S hS T')
    (f : algebraicSpaceStack.{u, w} B S hS T hT ⟶ 𝒳)
    (f' : algebraicSpaceStack.{u, w} B S hS T' hT' ⟶ 𝒳)
    (hsm : AlgebraicStacks.IsSmooth B S hS f) (hsm' : AlgebraicStacks.IsSmooth B S hS f')
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (hf' : AlgebraicStacks.IsLocallyOfFiniteType B S hS f')
    (t : Space.points B S hS T) (t' : Space.points B S hS T')
    (hx : pointsMap B S hS (fibredCategory B S hS T).val
        (fibredCategory B S hS T).property 𝒳.val.property f.hom.hom
        (stackPointOfSpacePoint B S hS T t) =
      pointsMap B S hS (fibredCategory B S hS T').val
        (fibredCategory B S hS T').property 𝒳.val.property f'.hom.hom
        (stackPointOfSpacePoint B S hS T' t')) :
    ∃ d d' : ℕ, relativeDimensionAt.{u, w} B S hS T hT 𝒳 f hf t = (d : WithBot ℕ∞) ∧
      relativeDimensionAt.{u, w} B S hS T' hT' 𝒳 f' hf' t' = (d' : WithBot ℕ∞) ∧
        dimensionSubNat (Space.dimensionAtPoint B S hS T hT t) d =
          dimensionSubNat (Space.dimensionAtPoint B S hS T' hT' t') d'
```

## Tag 0AFN, a definition

[Tag 0AFN](https://stacks.math.columbia.edu/tag/0AFN) in the Stacks Project.

**`AlgebraicGeometry.Stack.dimensionAtPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Dimension.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Dimension.lean#L124).

> **Stacks 0AFN.** The dimension of a locally Noetherian algebraic stack `𝒳` at a point `x`:
> the infimum of `dim_t(T) - dim_t(T_x)` over the 1-morphisms `T ⟶ 𝒳` from an algebraic space
> that are smooth and locally of finite type and the points `t ∈ |T|` above `x`.

```lean
noncomputable def dimensionAtPoint (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (_h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (x : points B S hS 𝒳.val.val 𝒳.val.property) : EInt
```

**`AlgebraicGeometry.Stack.dimensionAtPoint_eq_dimensionSubNat_zero_of_representing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DimensionRepresentable.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DimensionRepresentable.lean#L68). The attribute's comment: “agreement with the dimension of an algebraic space”.

> **Stacks 0AFN, agreement with the dimension of an algebraic space.** Let `𝒵` be a locally
> Noetherian algebraic stack over `S` represented by an algebraic space `W`, and let `x ∈ |W|`
> have image `z ∈ |𝒵|`. Then the dimension of `𝒵` at `z` is the dimension of `W` at `x`.
>
> The chart of the representing equivalence is smooth, locally of finite type and of relative
> dimension `0`, so the formula of Stacks 0DRJ computes the left-hand side as
> `dim_x(W) - 0`.

```lean
theorem dimensionAtPoint_eq_dimensionSubNat_zero_of_representing
    (𝒵 : AlgebraicStacks.{u, w} B S hS)
    (h𝒵 : IsLocallyNoetherianStack.{u, w} B S hS 𝒵)
    (W : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hW : IsAlgebraicSpace B S hS W)
    (eW : StacksRepresentableCFG.EquivalenceOver 𝒵.val.val.p
      (presheafOfCategories (W ⋙ typeToCat)).p)
    (x : Space.points B S hS W) (z : points B S hS 𝒵.val.val 𝒵.val.property)
    (hz : spacePointMap B S hS W 𝒵.val
      (representingEquivalence B S hS W 𝒵.val eW).functor x = z) :
    dimensionAtPoint B S hS 𝒵 h𝒵 z =
      dimensionSubNat (Space.dimensionAtPoint B S hS W hW x) 0
```

## Tag 0AFP, a definition

[Tag 0AFP](https://stacks.math.columbia.edu/tag/0AFP) in the Stacks Project.

**`AlgebraicGeometry.Stack.dimension`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Dimension.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Dimension.lean#L155).

> **Stacks 0AFP.** The dimension of a locally Noetherian algebraic stack: the supremum, over
> the points of the stack, of its dimension at that point, as an extended integer.

```lean
noncomputable abbrev dimension (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳) : EInt
```

## Tag 0AFR, an example

[Tag 0AFR](https://stacks.math.columbia.edu/tag/0AFR) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_dimension_classifyingStack_additiveGroup_eq_neg_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NegativeDimensionExample.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/NegativeDimensionExample.lean#L134). The attribute's comment: “the dimension of an algebraic stack can be a negative integer: over every field the classifying stack of the additive group is constructed and has dimension `-1`”.

> **Stacks 0AFR: the classifying stack of `𝐆ₐ` has dimension `-1`.** Over every field `k`, the
> classifying stack `B𝐆ₐ = [Spec k/𝐆ₐ]` has a model in the 2-category of algebraic stacks, and every
> model is locally Noetherian of dimension `-1`.

```lean
theorem exists_dimension_classifyingStack_additiveGroup_eq_neg_one :
    (∃ 𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk,
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (classifyingStack C hk (Space.additiveGroupOverField C hk)).val.p 𝒬.val.val.p)) ∧
      ∀ (𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
        (_ : StacksRepresentableCFG.EquivalenceOver
          (classifyingStack C hk (Space.additiveGroupOverField C hk)).val.p 𝒬.val.val.p),
        ∃ hN : IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒬,
          dimension C (Spec (.of k)) hk 𝒬 hN = ((-1 : ℤ) : EInt)
```

**`AlgebraicGeometry.Stack.exists_algebraicStack_dimension_lt_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NegativeDimensionExample.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/NegativeDimensionExample.lean#L154). The attribute's comment: “the dimension of an algebraic stack can be a negative integer: a locally Noetherian algebraic stack of dimension `-1` exists over every field”.

> **Stacks 0AFR: the dimension of an algebraic stack can be a negative integer.** Over every
> field `k` there is a locally Noetherian algebraic stack of dimension `-1`, namely a model of the
> classifying stack of the additive group.

```lean
theorem exists_algebraicStack_dimension_lt_zero :
    ∃ (𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
      (hN : IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒬),
      dimension C (Spec (.of k)) hk 𝒬 hN = ((-1 : ℤ) : EInt) ∧
        dimension C (Spec (.of k)) hk 𝒬 hN < 0
```

**`AlgebraicGeometry.Stack.dimension_quotientStack_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimension.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimension.lean#L143). The attribute's comment: “upper bound `dim [X/G] ≤ dim X - dim G`, carrying the algebraicity of the quotient (Stacks 04WZ and 04TB) and the tautological chart `X ⟶ [X/G]` as hypotheses; the matching lower bound needs the independence of the chart, Stacks 0AFM”.

> **Stacks 0AFR**, the upper bound. Let `G` act on `X` over the base algebraic space `A`, let
> `𝒬` be an algebraic stack equivalent over the site to the quotient stack `[X/G]`, and let
> `f : X ⟶ 𝒬` be the tautological chart, of relative dimension `dim(G)` at every point. Then
> `dim [X/G] ≤ dim(X) - dim(G)`.

```lean
theorem dimension_quotientStack_le (A : AlgebraicSpaces B S hS) (G X : Over A.obj)
    [GrpObj G] [ModObj G X] (hG : IsAlgebraicSpace B S hS G.left)
    (hX : IsAlgebraicSpace B S hS X.left) (𝒬 : AlgebraicStacks.{u, w} B S hS)
    (_h𝒬 : Nonempty (StacksRepresentableCFG.EquivalenceOver 𝒬.val.val.p
      (quotientStack (Space.groupoidOfAction A G X hG hX).groupoid).p))
    (hN : IsLocallyNoetherianStack.{u, w} B S hS 𝒬)
    (f : algebraicSpaceStack.{u, w} B S hS X.left hX ⟶ 𝒬)
    (hsm : AlgebraicStacks.IsSmooth B S hS f)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (hsurj : ∀ x : points B S hS 𝒬.val.val 𝒬.val.property,
      ∃ t : Space.points B S hS X.left,
        pointsMap B S hS (fibredCategory B S hS X.left).val
          (fibredCategory B S hS X.left).property 𝒬.val.property f.hom.hom
          (stackPointOfSpacePoint B S hS X.left t) = x)
    (dG : ℕ) (hdG : ∀ t : Space.points B S hS X.left,
      relativeDimensionAt.{u, w} B S hS X.left hX 𝒬 f hf t = (dG : WithBot ℕ∞))
    (hGdim : Space.dimension B S hS G.left hG = (dG : WithBot ℕ∞)) :
    ∃ m : ℕ, Space.dimension B S hS G.left hG = (m : WithBot ℕ∞) ∧
      dimension B S hS 𝒬 hN ≤ dimensionSubNat (Space.dimension B S hS X.left hX) m
```

**`AlgebraicGeometry.Stack.dimension_classifyingStack_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimension.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimension.lean#L180). The attribute's comment: “upper bound `dim BG ≤ -dim G` for the classifying stack, carrying the algebraicity of `BG` (Stacks 04WZ and 04TB), the tautological chart `Spec k ⟶ BG` and `dim (Spec k) = 0` as hypotheses; the matching lower bound needs Stacks 0AFM”.

> **Stacks 0AFR**, the upper bound for the classifying stack `BG = [Spec k/G]` of a group `G`
> over a field `k`, whose tautological chart is `Spec k ⟶ BG`: `dim BG ≤ -dim(G)`.

```lean
theorem dimension_classifyingStack_le
    (_h𝒬 : Nonempty (StacksRepresentableCFG.EquivalenceOver 𝒬.val.val.p
      (classifyingStack C hk G).val.p))
    (hN : IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒬)
    (f : algebraicSpaceStack.{u, w} C (Spec (.of k)) hk
      (Space.terminalSpace C (Spec (.of k)) hk).obj
      (Space.terminalSpace C (Spec (.of k)) hk).property ⟶ 𝒬)
    (hsm : AlgebraicStacks.IsSmooth C (Spec (.of k)) hk f)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType C (Spec (.of k)) hk f)
    (hsurj : ∀ x : points C (Spec (.of k)) hk 𝒬.val.val 𝒬.val.property,
      ∃ t : Space.points C (Spec (.of k)) hk
        (Space.terminalSpace C (Spec (.of k)) hk).obj,
        pointsMap C (Spec (.of k)) hk
          (fibredCategory C (Spec (.of k)) hk
            (Space.terminalSpace C (Spec (.of k)) hk).obj).val
          (fibredCategory C (Spec (.of k)) hk
            (Space.terminalSpace C (Spec (.of k)) hk).obj).property 𝒬.val.property f.hom.hom
          (stackPointOfSpacePoint C (Spec (.of k)) hk
            (Space.terminalSpace C (Spec (.of k)) hk).obj t) = x)
    (dG : ℕ) (hdG : ∀ t : Space.points C (Spec (.of k)) hk
        (Space.terminalSpace C (Spec (.of k)) hk).obj,
      relativeDimensionAt.{u, w} C (Spec (.of k)) hk
        (Space.terminalSpace C (Spec (.of k)) hk).obj
        (Space.terminalSpace C (Spec (.of k)) hk).property 𝒬 f hf t = (dG : WithBot ℕ∞))
    (hGdim : Space.dimension C (Spec (.of k)) hk G.obj.X.left G.property =
      (dG : WithBot ℕ∞))
    (hk0 : Space.dimension C (Spec (.of k)) hk
      (Space.terminalSpace C (Spec (.of k)) hk).obj
      (Space.terminalSpace C (Spec (.of k)) hk).property = ((0 : ℕ) : WithBot ℕ∞)) :
    ∃ m : ℕ, Space.dimension C (Spec (.of k)) hk G.obj.X.left G.property =
      (m : WithBot ℕ∞) ∧ dimension C (Spec (.of k)) hk 𝒬 hN ≤ ((-(m : ℤ) : ℤ) : EInt)
```

**`AlgebraicGeometry.Stack.dimension_classifyingStack_lt_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimension.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimension.lean#L224). The attribute's comment: “the dimension of an algebraic stack can be a negative integer, carrying the algebraicity of `BG` (Stacks 04WZ and 04TB), the tautological chart `Spec k ⟶ BG` and `dim (Spec k) = 0` as hypotheses”.

> **Stacks 0AFR.** The dimension of an algebraic stack can be a negative integer: the
> classifying stack of a group of positive dimension over a field has negative dimension.

```lean
theorem dimension_classifyingStack_lt_zero
    (_h𝒬 : Nonempty (StacksRepresentableCFG.EquivalenceOver 𝒬.val.val.p
      (classifyingStack C hk G).val.p))
    (hN : IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒬)
    (f : algebraicSpaceStack.{u, w} C (Spec (.of k)) hk
      (Space.terminalSpace C (Spec (.of k)) hk).obj
      (Space.terminalSpace C (Spec (.of k)) hk).property ⟶ 𝒬)
    (hsm : AlgebraicStacks.IsSmooth C (Spec (.of k)) hk f)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType C (Spec (.of k)) hk f)
    (hsurj : ∀ x : points C (Spec (.of k)) hk 𝒬.val.val 𝒬.val.property,
      ∃ t : Space.points C (Spec (.of k)) hk
        (Space.terminalSpace C (Spec (.of k)) hk).obj,
        pointsMap C (Spec (.of k)) hk
          (fibredCategory C (Spec (.of k)) hk
            (Space.terminalSpace C (Spec (.of k)) hk).obj).val
          (fibredCategory C (Spec (.of k)) hk
            (Space.terminalSpace C (Spec (.of k)) hk).obj).property 𝒬.val.property f.hom.hom
          (stackPointOfSpacePoint C (Spec (.of k)) hk
            (Space.terminalSpace C (Spec (.of k)) hk).obj t) = x)
    (dG : ℕ) (hdG : ∀ t : Space.points C (Spec (.of k)) hk
        (Space.terminalSpace C (Spec (.of k)) hk).obj,
      relativeDimensionAt.{u, w} C (Spec (.of k)) hk
        (Space.terminalSpace C (Spec (.of k)) hk).obj
        (Space.terminalSpace C (Spec (.of k)) hk).property 𝒬 f hf t = (dG : WithBot ℕ∞))
    (_hGdim : Space.dimension C (Spec (.of k)) hk G.obj.X.left G.property =
      (dG : WithBot ℕ∞))
    (hk0 : Space.dimension C (Spec (.of k)) hk
      (Space.terminalSpace C (Spec (.of k)) hk).obj
      (Space.terminalSpace C (Spec (.of k)) hk).property = ((0 : ℕ) : WithBot ℕ∞))
    (hpos : 0 < dG) :
    dimension C (Spec (.of k)) hk 𝒬 hN < 0
```

**`AlgebraicGeometry.Stack.dimension_quotientStack_eq_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionField.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionField.lean#L441). The attribute's comment: “`dim [X/G] = dim X - dim G` for a group smooth over the field; the quotient stack is constructed, and every model of it has this dimension”.

> **The dimension of a quotient stack by a smooth group.** Let `X` be an algebraic space locally
> of finite type over a field `k` and let `G` be a group algebraic space smooth over `k` acting on
> `X`. Then the quotient stack `[X/G]` is an algebraic stack — it has a model `𝒬` in the 2-category
> of algebraic stacks — and every such model is locally Noetherian of dimension
> `dim [X/G] = dim(X) - dim(G)`, the dimension of `G` being a natural number.

```lean
theorem dimension_quotientStack_eq_of_isSmooth
    (X : Over (Space.terminalSpace C (Spec (.of k)) hk).obj) [ModObj G.obj.X X]
    (hX : IsAlgebraicSpace C (Spec (.of k)) hk X.left)
    (hXft : Space.IsLocallyOfFiniteType C (Spec (.of k)) hk X.hom)
    (hGsm : Space.IsSmooth C (Spec (.of k)) hk G.obj.X.hom) :
    ∃ m : ℕ, Space.dimension C (Spec (.of k)) hk G.obj.X.left G.property = (m : WithBot ℕ∞) ∧
      (∃ 𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk,
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (quotientStack (Space.groupoidOfAction (Space.terminalSpace C (Spec (.of k)) hk)
            G.obj.X X G.property hX).groupoid).p 𝒬.val.val.p)) ∧
      ∀ (𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
        (_ : StacksRepresentableCFG.EquivalenceOver
          (quotientStack (Space.groupoidOfAction (Space.terminalSpace C (Spec (.of k)) hk)
            G.obj.X X G.property hX).groupoid).p 𝒬.val.val.p),
        ∃ hN : IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒬,
          dimension C (Spec (.of k)) hk 𝒬 hN =
            dimensionSubNat (Space.dimension C (Spec (.of k)) hk X.left hX) m
```

**`AlgebraicGeometry.Stack.dimension_classifyingStack_eq_neg_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionField.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionField.lean#L475). The attribute's comment: “`dim BG = -dim G` for the classifying stack of a group smooth over the field; the classifying stack is constructed, and every model of it has this dimension”.

> **The dimension of the classifying stack of a smooth group.** Let `G` be a group algebraic
> space smooth over a field `k`. Then the classifying stack `BG = [Spec k/G]` is an algebraic stack
> — it has a model `𝒬` in the 2-category of algebraic stacks — and every such model is locally
> Noetherian of dimension `dim BG = -dim(G)`, the dimension of `G` being a natural number.

```lean
theorem dimension_classifyingStack_eq_neg_of_isSmooth
    (hGsm : Space.IsSmooth C (Spec (.of k)) hk G.obj.X.hom) :
    ∃ m : ℕ, Space.dimension C (Spec (.of k)) hk G.obj.X.left G.property = (m : WithBot ℕ∞) ∧
      (∃ 𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk,
        Nonempty (StacksRepresentableCFG.EquivalenceOver (classifyingStack C hk G).val.p
          𝒬.val.val.p)) ∧
      ∀ (𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
        (_ : StacksRepresentableCFG.EquivalenceOver (classifyingStack C hk G).val.p
          𝒬.val.val.p),
        ∃ hN : IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒬,
          dimension C (Spec (.of k)) hk 𝒬 hN = ((-(m : ℤ) : ℤ) : EInt)
```

**`AlgebraicGeometry.Stack.dimension_classifyingStack_lt_zero_of_isSmooth_of_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionField.lean, line 502](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionField.lean#L502). The attribute's comment: “the dimension of an algebraic stack can be a negative integer: `dim BG < 0` for a group of positive dimension smooth over the field”.

> **The dimension of an algebraic stack can be a negative integer.** Let `G` be a group algebraic
> space of positive dimension, smooth over a field `k`. Then the classifying stack `BG` is an
> algebraic stack, and every model of it is a locally Noetherian algebraic stack of negative
> dimension.

```lean
theorem dimension_classifyingStack_lt_zero_of_isSmooth_of_pos
    (hGsm : Space.IsSmooth C (Spec (.of k)) hk G.obj.X.hom)
    (hpos : 0 < Space.dimension C (Spec (.of k)) hk G.obj.X.left G.property) :
    (∃ 𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk,
        Nonempty (StacksRepresentableCFG.EquivalenceOver (classifyingStack C hk G).val.p
          𝒬.val.val.p)) ∧
      ∀ (𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
        (_ : StacksRepresentableCFG.EquivalenceOver (classifyingStack C hk G).val.p
          𝒬.val.val.p),
        ∃ hN : IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒬,
          dimension C (Spec (.of k)) hk 𝒬 hN < 0
```

**`AlgebraicGeometry.Stack.dimension_quotientStack_eq_of_charZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionField.lean, line 759](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionField.lean#L759). The attribute's comment: “`dim [X/G] = dim X - dim G` over a field of characteristic zero, for every group scheme locally of finite type; the quotient stack is constructed”.

> **The dimension of a quotient stack in characteristic zero.** Let `X` be an algebraic space
> locally of finite type over a field `k` of characteristic `0`, and let `G` be a group scheme
> locally of finite type over `k` acting on `X`. Then `[X/G]` is an algebraic stack, and every model
> of it is locally Noetherian of dimension `dim(X) - dim(G)`, the dimension of `G` being a natural
> number.

```lean
theorem dimension_quotientStack_eq_of_charZero [CharZero k]
    [G.obj.X.left.IsRepresentable]
    (hGft : Space.IsLocallyOfFiniteType C (Spec (.of k)) hk G.obj.X.hom)
    (X : Over (Space.terminalSpace C (Spec (.of k)) hk).obj) [ModObj G.obj.X X]
    (hX : IsAlgebraicSpace C (Spec (.of k)) hk X.left)
    (hXft : Space.IsLocallyOfFiniteType C (Spec (.of k)) hk X.hom) :
    ∃ m : ℕ, Space.dimension C (Spec (.of k)) hk G.obj.X.left G.property = (m : WithBot ℕ∞) ∧
      (∃ 𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk,
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (quotientStack (Space.groupoidOfAction (Space.terminalSpace C (Spec (.of k)) hk)
            G.obj.X X G.property hX).groupoid).p 𝒬.val.val.p)) ∧
      ∀ (𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
        (_ : StacksRepresentableCFG.EquivalenceOver
          (quotientStack (Space.groupoidOfAction (Space.terminalSpace C (Spec (.of k)) hk)
            G.obj.X X G.property hX).groupoid).p 𝒬.val.val.p),
        ∃ hN : IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒬,
          dimension C (Spec (.of k)) hk 𝒬 hN =
            dimensionSubNat (Space.dimension C (Spec (.of k)) hk X.left hX) m
```

**`AlgebraicGeometry.Stack.dimension_classifyingStack_eq_neg_of_charZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionField.lean, line 785](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionField.lean#L785). The attribute's comment: “`dim BG = -dim G` over a field of characteristic zero, for every group scheme locally of finite type; the classifying stack is constructed”.

> **The dimension of the classifying stack in characteristic zero.** For a group scheme `G`
> locally of finite type over a field `k` of characteristic `0`, the classifying stack `BG` is an
> algebraic stack and every model of it is locally Noetherian of dimension `-dim(G)`.

```lean
theorem dimension_classifyingStack_eq_neg_of_charZero [CharZero k]
    [G.obj.X.left.IsRepresentable]
    (hGft : Space.IsLocallyOfFiniteType C (Spec (.of k)) hk G.obj.X.hom) :
    ∃ m : ℕ, Space.dimension C (Spec (.of k)) hk G.obj.X.left G.property = (m : WithBot ℕ∞) ∧
      (∃ 𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk,
        Nonempty (StacksRepresentableCFG.EquivalenceOver (classifyingStack C hk G).val.p
          𝒬.val.val.p)) ∧
      ∀ (𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
        (_ : StacksRepresentableCFG.EquivalenceOver (classifyingStack C hk G).val.p
          𝒬.val.val.p),
        ∃ hN : IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒬,
          dimension C (Spec (.of k)) hk 𝒬 hN = ((-(m : ℤ) : ℤ) : EInt)
```

**`AlgebraicGeometry.Stack.dimension_classifyingStack_lt_zero_of_charZero_of_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionField.lean, line 805](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionField.lean#L805). The attribute's comment: “the dimension of an algebraic stack can be a negative integer: `dim BG < 0` over a field of characteristic zero, for every group scheme of positive dimension locally of finite type”.

> **The dimension of an algebraic stack can be a negative integer, in characteristic zero.** For
> a group scheme `G` of positive dimension, locally of finite type over a field of characteristic
> `0`, the classifying stack `BG` is an algebraic stack of negative dimension.

```lean
theorem dimension_classifyingStack_lt_zero_of_charZero_of_pos [CharZero k]
    [G.obj.X.left.IsRepresentable]
    (hGft : Space.IsLocallyOfFiniteType C (Spec (.of k)) hk G.obj.X.hom)
    (hpos : 0 < Space.dimension C (Spec (.of k)) hk G.obj.X.left G.property) :
    (∃ 𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk,
        Nonempty (StacksRepresentableCFG.EquivalenceOver (classifyingStack C hk G).val.p
          𝒬.val.val.p)) ∧
      ∀ (𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
        (_ : StacksRepresentableCFG.EquivalenceOver (classifyingStack C hk G).val.p
          𝒬.val.val.p),
        ∃ hN : IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒬,
          dimension C (Spec (.of k)) hk 𝒬 hN < 0
```

**`AlgebraicGeometry.Stack.dimension_quotientStack_eq_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionFiniteType.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionFiniteType.lean#L54). The attribute's comment: “`dim [X/G] = dim X - dim G` for every group algebraic space locally of finite type over the field, smooth or not, acting on an algebraic space locally of finite type; the quotient stack is constructed”.

> Let `X` be an algebraic space locally of finite type over a field `k`, and let
> `G` be a group algebraic space locally of finite type over `k`, not necessarily smooth, acting on
> `X`. Then the quotient stack `[X/G]` is an algebraic stack — it has a model `𝒬` in the 2-category
> of algebraic stacks — the dimension of `G` is a natural number `m`, and every model of `[X/G]` is
> locally Noetherian of dimension `dim(X) - m`.

```lean
theorem dimension_quotientStack_eq_of_isLocallyOfFiniteType
    (hGft : Space.IsLocallyOfFiniteType C (Spec (.of k)) hk G.obj.X.hom)
    (X : Over (Space.terminalSpace C (Spec (.of k)) hk).obj) [ModObj G.obj.X X]
    (hX : IsAlgebraicSpace C (Spec (.of k)) hk X.left)
    (hXft : Space.IsLocallyOfFiniteType C (Spec (.of k)) hk X.hom) :
    ∃ m : ℕ, Space.dimension C (Spec (.of k)) hk G.obj.X.left G.property = (m : WithBot ℕ∞) ∧
      (∃ 𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk,
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (quotientStack (Space.groupoidOfAction (Space.terminalSpace C (Spec (.of k)) hk)
            G.obj.X X G.property hX).groupoid).p 𝒬.val.val.p)) ∧
      ∀ (𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
        (_ : StacksRepresentableCFG.EquivalenceOver
          (quotientStack (Space.groupoidOfAction (Space.terminalSpace C (Spec (.of k)) hk)
            G.obj.X X G.property hX).groupoid).p 𝒬.val.val.p),
        ∃ hN : IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒬,
          dimension C (Spec (.of k)) hk 𝒬 hN =
            dimensionSubNat (Space.dimension C (Spec (.of k)) hk X.left hX) m
```

**`AlgebraicGeometry.Stack.dimension_classifyingStack_eq_neg_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionFiniteType.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionFiniteType.lean#L79). The attribute's comment: “`dim BG = -dim G` for every group algebraic space locally of finite type over the field, smooth or not; the classifying stack is constructed”.

> For a group algebraic space `G` locally of finite type over a field `k`, not necessarily
> smooth, the classifying stack `BG` is an algebraic stack, the dimension of `G` is a natural number
> `m`, and every model of `BG` is locally Noetherian of dimension `-m`.

```lean
theorem dimension_classifyingStack_eq_neg_of_isLocallyOfFiniteType
    (hGft : Space.IsLocallyOfFiniteType C (Spec (.of k)) hk G.obj.X.hom) :
    ∃ m : ℕ, Space.dimension C (Spec (.of k)) hk G.obj.X.left G.property = (m : WithBot ℕ∞) ∧
      (∃ 𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk,
        Nonempty (StacksRepresentableCFG.EquivalenceOver (classifyingStack C hk G).val.p
          𝒬.val.val.p)) ∧
      ∀ (𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
        (_ : StacksRepresentableCFG.EquivalenceOver (classifyingStack C hk G).val.p
          𝒬.val.val.p),
        ∃ hN : IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒬,
          dimension C (Spec (.of k)) hk 𝒬 hN = ((-(m : ℤ) : ℤ) : EInt)
```

**`AlgebraicGeometry.Stack.dimension_classifyingStack_lt_zero_of_isLocallyOfFiniteType_of_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionFiniteType.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDimensionFiniteType.lean#L99). The attribute's comment: “the dimension of an algebraic stack can be a negative integer: `dim BG < 0` for every group algebraic space of positive dimension locally of finite type over the field, smooth or not”.

> For a group algebraic space `G` of positive dimension, locally of finite type over a field `k`
> and not necessarily smooth, the classifying stack `BG` is an algebraic stack, and every model of
> it is locally Noetherian of negative dimension.

```lean
theorem dimension_classifyingStack_lt_zero_of_isLocallyOfFiniteType_of_pos
    (hGft : Space.IsLocallyOfFiniteType C (Spec (.of k)) hk G.obj.X.hom)
    (hpos : 0 < Space.dimension C (Spec (.of k)) hk G.obj.X.left G.property) :
    (∃ 𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk,
        Nonempty (StacksRepresentableCFG.EquivalenceOver (classifyingStack C hk G).val.p
          𝒬.val.val.p)) ∧
      ∀ (𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
        (_ : StacksRepresentableCFG.EquivalenceOver (classifyingStack C hk G).val.p
          𝒬.val.val.p),
        ∃ hN : IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒬,
          dimension C (Spec (.of k)) hk 𝒬 hN < 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 100.12, Tag 0AFL](https://stacks.math.columbia.edu/tag/0AFL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
