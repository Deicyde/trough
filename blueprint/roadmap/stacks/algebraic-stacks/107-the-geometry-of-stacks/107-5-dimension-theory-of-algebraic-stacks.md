---
declaration: section
origin: cited
lean: Stacks.Examples.DimensionVersusPointSet.dimensionAtPoint_translationQuotient_eq_one, Stacks.Examples.DimensionVersusPointSet.topologicalKrullDim_points_translationQuotient_eq_zero, Stacks.Examples.DimensionVersusPointSet.dimensionAtPoint_ne_topologicalKrullDimAt_points, Stacks.Examples.DimensionVersusPointSet.dimensionAtPoint_infiniteProductQuotient_eq_zero, Stacks.Examples.DimensionVersusPointSet.isGenericPoint_quotientCoordinatePoint, Stacks.Examples.DimensionVersusPointSet.irreducibleSpace_points_infiniteProductQuotient, Stacks.Examples.DimensionVersusPointSet.topologicalKrullDim_points_infiniteProductQuotient_eq_one, Stacks.Examples.DimensionVersusPointSet.topologicalKrullDimAt_points_infiniteProductQuotient_eq_one
statement: formalized
proof: formalized
---

# 107.5 Dimension theory of algebraic stacks

Section 107.5 of the Stacks Project, [Tag 0DRE](https://stacks.math.columbia.edu/tag/0DRE). 24 tags here are carried by 56 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DRF, a remark

[Tag 0DRF](https://stacks.math.columbia.edu/tag/0DRF) in the Stacks Project.

**`Stacks.Examples.DimensionVersusPointSet.dimensionAtPoint_translationQuotient_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean#L373). The attribute's comment: “the first counterexample: 𝔸¹\_k/ℤ has dimension 1 at every point”.

> **Stacks 0DRF.** The dimension of `𝔸¹_k/ℤ` at each of its points is `1`: the affine line
> is a surjective étale chart and has local dimension `1` at every point.

```lean
theorem dimensionAtPoint_translationQuotient_eq_one
    (x : Space.points B (Spec (.of k)) hS
      (translationQuotient k B hS (contains_affineLine k B hS))) :
    Space.dimensionAtPoint B (Spec (.of k)) hS
        (translationQuotient k B hS (contains_affineLine k B hS))
        (isAlgebraicSpace_translationQuotient k B hS) x = 1
```

**`Stacks.Examples.DimensionVersusPointSet.topologicalKrullDim_points_translationQuotient_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean, line 489](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean#L489). The attribute's comment: “the first counterexample: the point space of 𝔸¹\_k/ℤ is of Krull dimension 0”.

> **Stacks 0DRF.** The point space of `𝔸¹_k/ℤ` is of Krull dimension `0`, being
> indiscrete.

```lean
theorem topologicalKrullDim_points_translationQuotient_eq_zero :
    topologicalKrullDim (Space.points B (Spec (.of k)) hS
      (translationQuotient k B hS (contains_affineLine k B hS))) = (0 : WithBot ℕ∞)
```

**`Stacks.Examples.DimensionVersusPointSet.dimensionAtPoint_ne_topologicalKrullDimAt_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean, line 513](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean#L513). The attribute's comment: “the dimension at a point differs from the local dimension of the point space”.

> **Stacks 0DRF.** The dimension of an algebraic space at a point need not coincide with the
> dimension of its point space at that point: for `𝔸¹_k/ℤ` over a field of characteristic zero
> the former is `1` while the latter is `0`.

```lean
theorem dimensionAtPoint_ne_topologicalKrullDimAt_points
    (x : Space.points B (Spec (.of k)) hS
      (translationQuotient k B hS (contains_affineLine k B hS))) :
    Space.dimensionAtPoint B (Spec (.of k)) hS
        (translationQuotient k B hS (contains_affineLine k B hS))
        (isAlgebraicSpace_translationQuotient k B hS) x ≠
      topologicalKrullDimAt (Space.points B (Spec (.of k)) hS
        (translationQuotient k B hS (contains_affineLine k B hS))) x
```

**`Stacks.Examples.DimensionVersusPointSet.dimensionAtPoint_infiniteProductQuotient_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean, line 599](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean#L599). The attribute's comment: “the second counterexample: the space X = U/R of Stacks 02Z8 has dimension 0 at every point”.

> **Stacks 0DRF.** The algebraic space `X = U/R` of Stacks 02Z8 has dimension `0` at each of
> its points: `U = Spec (∏ n : ℕ, K)` is an étale chart surjective on points, and its point space
> is `T₁` and sober, hence of local Krull dimension `0` at every one of its points.

```lean
theorem dimensionAtPoint_infiniteProductQuotient_eq_zero
    (x : Space.points B (base K) hS (quotient K B hS hU hR)) :
    Space.dimensionAtPoint B (base K) hS (quotient K B hS hU hR)
        (isAlgebraicSpace_quotient K B hS hU hR) x = 0
```

**`Stacks.Examples.DimensionVersusPointSet.isGenericPoint_quotientCoordinatePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean, line 641](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean#L641). The attribute's comment: “the second counterexample: |X| admits x₀ as a generic point”.

> **Stacks 0DRF.** The point `x₀` is a generic point of the point space of `X = U/R`: the
> coordinate points are dense in `|U|` and all of them map to `x₀`, which is Stacks 02Z8.

```lean
theorem isGenericPoint_quotientCoordinatePoint :
    IsGenericPoint (quotientCoordinatePoint K B hS hU hR)
      (Set.univ : Set (Space.points B (base K) hS (quotient K B hS hU hR)))
```

**`Stacks.Examples.DimensionVersusPointSet.irreducibleSpace_points_infiniteProductQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean, line 659](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean#L659). The attribute's comment: “the second counterexample: |X| is irreducible”.

> **Stacks 0DRF.** The point space of `X = U/R` is irreducible: the closure of `x₀` is all of
> it.

```lean
theorem irreducibleSpace_points_infiniteProductQuotient :
    IrreducibleSpace (Space.points B (base K) hS (quotient K B hS hU hR))
```

**`Stacks.Examples.DimensionVersusPointSet.topologicalKrullDim_points_infiniteProductQuotient_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean, line 853](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean#L853). The attribute's comment: “the second counterexample: |X| is of Krull dimension 1”.

> **Stacks 0DRF.** The point space of `X = U/R` is of Krull dimension `1`: it is irreducible
> with generic point `x₀`, and every irreducible closed subset of it is either all of it or a single
> point.

```lean
theorem topologicalKrullDim_points_infiniteProductQuotient_eq_one :
    topologicalKrullDim (Space.points B (base K) hS (quotient K B hS hU hR)) = 1
```

**`Stacks.Examples.DimensionVersusPointSet.topologicalKrullDimAt_points_infiniteProductQuotient_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean, line 871](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean#L871). The attribute's comment: “the second counterexample: the local dimension of |X| is 1 at each of its points other than x₀”.

> **Stacks 0DRF.** The local Krull dimension of the point space of `X = U/R` is `1` at every
> point other than `x₀`: every open neighbourhood of such a point contains `x₀` as well, whose
> closure is everything, so the point and the neighbourhood form a chain of length one.

```lean
theorem topologicalKrullDimAt_points_infiniteProductQuotient_eq_one
    (z : Space.points B (base K) hS (quotient K B hS hU hR))
    (hz : z ≠ quotientCoordinatePoint K B hS hU hR) :
    topologicalKrullDimAt (Space.points B (base K) hS (quotient K B hS hU hR)) z = 1
```

**`Stacks.Examples.DimensionVersusPointSet.dimensionAtPoint_ne_topologicalKrullDimAt_points_infiniteProductQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean, line 900](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean#L900). The attribute's comment: “the second counterexample: the dimension at a point is smaller than the local dimension of the point space”.

> **Stacks 0DRF.** The dimension of an algebraic space at a point can also be *smaller* than
> the dimension of its point space at that point: the space `X = U/R` of Stacks 02Z8 is of
> dimension `0` at each of its points, while the local Krull dimension of `|X|` is `1` at every
> point other than `x₀`.

```lean
theorem dimensionAtPoint_ne_topologicalKrullDimAt_points_infiniteProductQuotient
    (z : Space.points B (base K) hS (quotient K B hS hU hR))
    (hz : z ≠ quotientCoordinatePoint K B hS hU hR) :
    Space.dimensionAtPoint B (base K) hS (quotient K B hS hU hR)
        (isAlgebraicSpace_quotient K B hS hU hR) z ≠
      topologicalKrullDimAt (Space.points B (base K) hS (quotient K B hS hU hR)) z
```

**`Stacks.Examples.DimensionVersusPointSet.topologicalKrullDimAt_quotientCoordinatePoint_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean, line 918](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean#L918). The attribute's comment: “the second counterexample, corrected: at x₀ the local dimension of |X| is 0, not 1”.

> **Stacks 0DRF is inaccurate at the generic point.** The remark says of the example of
> Stacks 02Z8 that `|X|` admitting a generic point makes "the dimension of `|X|` at any of its
> points" equal to `1`. That fails at the generic point `x₀` itself: the coordinate points form an
> open subset of `|U|`, saturated for the relation, and `|U| → |X|` is open, so `{x₀}` is an open
> neighbourhood of `x₀` of Krull dimension `0`. At `x₀` the two dimensions compared by the remark
> therefore agree, both being `0`; the example separates them at every other point.

```lean
theorem topologicalKrullDimAt_quotientCoordinatePoint_eq_zero :
    topologicalKrullDimAt (Space.points B (base K) hS (quotient K B hS hU hR))
      (quotientCoordinatePoint K B hS hU hR) = 0
```

**`Stacks.Examples.DimensionVersusPointSet.exists_dimensionAtPoint_eq_zero_topologicalKrullDim_points_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean, line 965](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/DimensionVersusPointSet.lean#L965). The attribute's comment: “the second counterexample exists: an algebraic space of dimension 0 at each of its points whose point space is irreducible of Krull dimension 1 with a generic point”.

> **Stacks 0DRF.** There is an algebraic space over a field which is of dimension `0` at each
> of its points while its point space is irreducible of Krull dimension `1` and admits a generic
> point: the example of Stacks 02Z8 over the field with two elements, on a big fppf site
> containing the three schemes it is built from.

```lean
theorem exists_dimensionAtPoint_eq_zero_topologicalKrullDim_points_eq_one :
    ∃ (B : BigFppfSite.{u}) (hS : B.Contains (base (ULift.{u} (ZMod 2))))
      (F : (BigFppfOver B (base (ULift.{u} (ZMod 2))) hS)ᵒᵖ ⥤ Type u)
      (hF : IsAlgebraicSpace B (base (ULift.{u} (ZMod 2))) hS F),
      (∀ x, Space.dimensionAtPoint B (base (ULift.{u} (ZMod 2))) hS F hF x = 0) ∧
        IrreducibleSpace (Space.points B (base (ULift.{u} (ZMod 2))) hS F) ∧
        topologicalKrullDim (Space.points B (base (ULift.{u} (ZMod 2))) hS F) = 1 ∧
        ∃ x₀, IsGenericPoint x₀
          (Set.univ : Set (Space.points B (base (ULift.{u} (ZMod 2))) hS F))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.topologicalKrullDimAt_points_eq_dimensionAtPoint_of_isDecentSpace`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/Dimension.lean#L96), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/DimensionCoincidence.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/DimensionCoincidence.lean#L27) (StacksFrontier): “the remark's last assertion: for a decent space the two dimensions do coincide at every point”.

## Tag 0DRG, a definition

[Tag 0DRG](https://stacks.math.columbia.edu/tag/0DRG) in the Stacks Project.

**`AlgebraicGeometry.Stack.relativeDimensionAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionAtPoint.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionAtPoint.lean#L335). References: EGA IV (17.10.1).

> The relative dimension `dim_t(T_x)` at `t ∈ |T|` of a 1-morphism `f`, locally of finite type,
> from an algebraic space `T` to an algebraic stack `𝒳`: the dimension of the algebraic space
> `T ×_𝒳 Spec k` at a point above `t`, for a field-valued point `Spec k ⟶ 𝒳` representing the
> image `x` of `t`. The representative and the point above `t` are the choices the source makes;
> the point above `t` exists by Stacks 04XH.

```lean
noncomputable def relativeDimensionAt
    (_hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f) (t : Space.points B S hS T) :
    WithBot ℕ∞
```

## Tag 0DRH, a remark

[Tag 0DRH](https://stacks.math.columbia.edu/tag/0DRH) in the Stacks Project.

**`AlgebraicGeometry.Stack.relativeDimensionAt_eq_fieldFibreDimensionAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionAtPoint.lean, line 1189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionAtPoint.lean#L1189). The attribute's comment: “relative\_dimension\_well\_defined”.

> **The relative dimension `relativeDimensionAt` is well defined.** The value of the
> formula of Stacks 0DRG at *every* field-valued point `p` representing the image of `t` and every
> point `q` of the fibre `T ×_𝒳 Spec κ(p)` above `t` is `relativeDimensionAt`, the value at the two
> choices the definition makes. So any two admissible pairs of choices give the same value, which
> is what makes `relativeDimensionAt` an invariant of `(f, t)`.

```lean
theorem relativeDimensionAt_eq_fieldFibreDimensionAt
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f) (t : Space.points B S hS T)
    (p : FieldValuedPoint B S hS 𝒳.val.val)
    (q : points B S hS (fieldFibreSquare B S hS f.hom p).pt.val
      (fieldFibreSquare B S hS f.hom p).pt.property)
    (_hp : pointClass B S hS 𝒳.val.val 𝒳.val.property p =
      pointsMap B S hS (fibredCategory B S hS T).val
        (fibredCategory B S hS T).property 𝒳.val.property f.hom.hom
        (stackPointOfSpacePoint B S hS T t))
    (hq : pointsMap B S hS (fieldFibreSquare B S hS f.hom p).pt.val
        (fieldFibreSquare B S hS f.hom p).pt.property
        (fibredCategory B S hS T).property
        (fieldFibreSquare B S hS f.hom p).fst.hom q =
      stackPointOfSpacePoint B S hS T t) :
    relativeDimensionAt B S hS T hT 𝒳 f hf t =
      fieldFibreDimensionAt.{u, w} B S hS f.hom 𝒳.property
        (isRepresentableByAlgebraicSpace_fibredCategory B S hS T hT) p q
```

**`AlgebraicGeometry.Stack.relativeDimensionAt_eq_iff_hasRelativeDimensionAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionAtPoint.lean, line 1312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionAtPoint.lean#L1312). The attribute's comment: “relative\_dimension\_agrees\_with\_spaces”.

> **The relative dimension of Stacks 0DRG agrees with the relative dimension of a morphism of
> algebraic spaces.** For a morphism `g : T ⟶ G` of algebraic spaces over `S`, the relative
> dimension of Stacks 0DRG of the induced 1-morphism of algebraic stacks is, at every point
> `t ∈ |T|`, the relative dimension `d` of `g` at `t` in the sense of Stacks 04NM.

```lean
theorem relativeDimensionAt_eq_iff_hasRelativeDimensionAt
    {T G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hT : IsAlgebraicSpace B S hS T) (hG : IsAlgebraicSpace B S hS G) (g : T ⟶ G)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS
      (algebraicSpaceStackMap.{u, w} B S hS hT hG g))
    (t : Space.points B S hS T) (d : ℕ∞) :
    relativeDimensionAt.{u, w} B S hS T hT (algebraicSpaceStack.{u, w} B S hS G hG)
        (algebraicSpaceStackMap.{u, w} B S hS hT hG g) hf t = (d : WithBot ℕ∞) ↔
      Space.HasRelativeDimensionAt d B S hS g t
```

## Tag 0DRI, a lemma

[Tag 0DRI](https://stacks.math.columbia.edu/tag/0DRI) in the Stacks Project.

**`AlgebraicGeometry.Stack.dimensionAtPoint_eq_add_relativeDimensionAt_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionSmoothSpaces.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionSmoothSpaces.lean#L80).

> **Stacks 0DRI.** Let `g : U ⟶ X` be a smooth morphism of locally Noetherian algebraic spaces
> over `S` and let `u ∈ |U|` have image `x ∈ |X|`. Then `dim_u(U) = dim_x(X) + dim_u(U_x)`, where
> `dim_u(U_x)` is the relative dimension of Stacks 0DRG of the induced 1-morphism of algebraic
> stacks at `u`.

```lean
theorem dimensionAtPoint_eq_add_relativeDimensionAt_of_isSmooth
    {U X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hU : IsAlgebraicSpace B S hS U) (hX : IsAlgebraicSpace B S hS X)
    (hNU : Space.HasEtaleLocalProperty B S hS U
      (fun Z : Scheme.{u} => IsLocallyNoetherian Z))
    (hNX : Space.HasEtaleLocalProperty B S hS X
      (fun Z : Scheme.{u} => IsLocallyNoetherian Z))
    (g : U ⟶ X) (hg : Space.IsSmooth B S hS g) (u : Space.points B S hS U) :
    Space.dimensionAtPoint B S hS U hU u =
      Space.dimensionAtPoint B S hS X hX (Space.pointsMap B S hS U g u) +
        relativeDimensionAt.{u, w} B S hS U hU (algebraicSpaceStack.{u, w} B S hS X hX)
          (algebraicSpaceStackMap.{u, w} B S hS hU hX g)
          (isLocallyOfFiniteType_algebraicSpaceStackMap_of_isSmooth.{u, w} B S hS hU hX g hg)
          u
```

## Tag 0DRJ, a lemma

[Tag 0DRJ](https://stacks.math.columbia.edu/tag/0DRJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.dimensionAtPoint_eq_dimensionSubNat_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DimensionChartIndependence.lean, line 497](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DimensionChartIndependence.lean#L497). The attribute's comment: “dimension via a smooth algebraic space”.

> Let `𝒳` be a locally Noetherian algebraic stack over `S`, let `f : T ⟶ 𝒳` be a smooth,
> locally-of-finite-type 1-morphism from an algebraic space, and let `t ∈ |T|` lie above
> `x ∈ |𝒳|`. If the relative dimension of Stacks 0DRG of `f` at `t` is the natural number `d`, then
> `dim_x(𝒳) = dim_t(T) - d`.

```lean
theorem dimensionAtPoint_eq_dimensionSubNat_of_isSmooth
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (x : points B S hS 𝒳.val.val 𝒳.val.property)
    {T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hT : IsAlgebraicSpace B S hS T)
    (f : algebraicSpaceStack.{u, w} B S hS T hT ⟶ 𝒳)
    (hsm : AlgebraicStacks.IsSmooth B S hS f)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (t : Space.points B S hS T)
    (ht : pointsMap B S hS (fibredCategory B S hS T).val
      (fibredCategory B S hS T).property 𝒳.val.property f.hom.hom
      (stackPointOfSpacePoint B S hS T t) = x)
    (d : ℕ) (hd : relativeDimensionAt.{u, w} B S hS T hT 𝒳 f hf t = (d : WithBot ℕ∞)) :
    dimensionAtPoint B S hS 𝒳 h𝒳 x =
      dimensionSubNat (Space.dimensionAtPoint B S hS T hT t) d
```

**`AlgebraicGeometry.Stack.exists_dimensionAtPoint_eq_dimensionSubNat_of_isSmooth_schemeChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DimensionSchemeChart.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DimensionSchemeChart.lean#L164). The attribute's comment: “dimension via a smooth scheme chart”.

> **Stacks 0DRJ at a smooth chart by a scheme of the site.** Let `𝒳` be a locally Noetherian
> algebraic stack over `S`, let `f : U ⟶ 𝒳` be a smooth 1-morphism from the algebraic stack of a
> scheme `U` of the site, and let `u ∈ U`. Then the relative dimension of Stacks 0DRG at `u` is a
> natural number `d` and
>
> `dim_{f(u)}(𝒳) = dim_u(U) - d`,
>
> the first term being the dimension of Stacks 0AFN and the second the local Krull dimension of the
> scheme `U` at `u`.
>
> The two models of `U` as an algebraic stack are compared by
> `AlgebraicGeometry.Stack.exists_smooth_algebraicSpaceStack_hom_pointsMap_eq`, which turns `f`
> into a smooth chart by the algebraic space `yoneda.obj U` through the same point of `|𝒳|`; the
> formula is then `AlgebraicGeometry.Stack.exists_dimensionAtPoint_eq_dimensionSubNat_of_isSmooth`
> there, with the dimension of Stacks 04N5 of `yoneda.obj U` identified with the local Krull
> dimension of `U` by
> `AlgebraicGeometry.Stack.dimensionAtPoint_yoneda_eq_topologicalKrullDimAt`. Local finite type of
> the chart, which Stacks 0DRG needs to speak of its relative dimension, is a consequence of
> smoothness by **Stacks 06MH**.

```lean
theorem exists_dimensionAtPoint_eq_dimensionSubNat_of_isSmooth_schemeChart
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (U : BigFppfOver B S hS) (f : schemeStack.{u, w} B S hS U ⟶ 𝒳)
    (hf : AlgebraicStacks.IsSmooth B S hS f)
    (u : (BigFppfOver.toScheme B S hS).obj U) :
    ∃ d : ℕ,
      dimensionAtPoint B S hS 𝒳 h𝒳 (AlgebraicStacks.chartPointMap B S hS U 𝒳 f u) =
        dimensionSubNat (topologicalKrullDimAt ((BigFppfOver.toScheme B S hS).obj U) u) d
```

**`AlgebraicGeometry.Stack.dimensionAtPoint_eq_dimensionSubNat_relativeDimensionAt_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DimensionSmoothChart.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DimensionSmoothChart.lean#L67). The attribute's comment: “dimension via a smooth algebraic space, from smoothness alone”.

> **Stacks 0DRJ.** Let `𝒳` be a locally Noetherian algebraic stack over `S`, let
> `f : T ⟶ 𝒳` be a smooth 1-morphism from an algebraic space, and let `t ∈ |T|` lie above
> `x ∈ |𝒳|`. Then
>
> `dim_x(𝒳) = dim_t(T) - dim_t(T_x)`,
>
> the left-hand side being the dimension of Stacks 0AFN and `dim_t(T_x)` the relative dimension of
> Stacks 0DRG of `f` at `t`.
>
> The relative dimension is taken at the local finite type of `f` that smoothness gives
> (Stacks 06MH, `AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_of_isSmooth`). It is
> a natural number (`AlgebraicGeometry.Stack.exists_relativeDimensionAt_eq_natCast`), and it enters
> the subtraction as that natural number, `ENat.toNat (r.unbotD 0)`.

```lean
theorem dimensionAtPoint_eq_dimensionSubNat_relativeDimensionAt_of_isSmooth
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (x : points B S hS 𝒳.val.val 𝒳.val.property)
    {T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hT : IsAlgebraicSpace B S hS T)
    (f : algebraicSpaceStack.{u, w} B S hS T hT ⟶ 𝒳)
    (hsm : AlgebraicStacks.IsSmooth B S hS f)
    (t : Space.points B S hS T)
    (ht : pointsMap B S hS (fibredCategory B S hS T).val
      (fibredCategory B S hS T).property 𝒳.val.property f.hom.hom
      (stackPointOfSpacePoint B S hS T t) = x) :
    dimensionAtPoint B S hS 𝒳 h𝒳 x =
      dimensionSubNat (Space.dimensionAtPoint B S hS T hT t)
        (ENat.toNat ((relativeDimensionAt.{u, w} B S hS T hT 𝒳 f
          (AlgebraicStacks.isLocallyOfFiniteType_of_isSmooth B S hS f hsm) t).unbotD 0))
```

**`AlgebraicGeometry.Stack.exists_relativeDimensionAt_eq_natCast`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionFiniteness.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionFiniteness.lean#L89). The attribute's comment: “finiteness of the relative dimension”.

> **The relative dimension of Stacks 0DRG is a natural number.** For a 1-morphism
> `f : T ⟶ 𝒳` locally of finite type from an algebraic space to an algebraic stack and a point
> `t ∈ |T|`, the value `dim_t(T_x)` is finite.

```lean
theorem exists_relativeDimensionAt_eq_natCast
    (T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hT : IsAlgebraicSpace B S hS T)
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (f : algebraicSpaceStack.{u, w} B S hS T hT ⟶ 𝒳)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (t : Space.points B S hS T) :
    ∃ d : ℕ, relativeDimensionAt.{u, w} B S hS T hT 𝒳 f hf t = (d : WithBot ℕ∞)
```

## Tag 0DRK, a remark

[Tag 0DRK](https://stacks.math.columbia.edu/tag/0DRK) in the Stacks Project.

**`AlgebraicGeometry.Stack.dimensionAtPoint_eq_topologicalKrullDimAt_of_isDeligneMumfordStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DimensionDeligneMumford.lean, line 350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DimensionDeligneMumford.lean#L350). The attribute's comment: “Deligne-Mumford stacks which are decent: `dim_x(𝒳) = dim_x |𝒳|`”.

> **Stacks 0DRK, the Deligne-Mumford case.** Let `𝒳` be a locally Noetherian Deligne-Mumford
> algebraic stack over `S` which is decent. Then at every point `x ∈ |𝒳|` the dimension of `𝒳`
> (Stacks 0AFN) agrees with the local Krull dimension `dim_x |𝒳|` of its point space.
>
> An étale chart `c : W ⟶ 𝒳` by a scheme has relative dimension `0` everywhere, so by Stacks 0DRJ
> the dimension of `𝒳` at `x = c(t)` is the dimension of `W` at `t`, which is `dim_t |W|`. The map
> `|W| ⟶ |𝒳|` is continuous and open (Stacks 06R7), generizations lift along it (Stacks 0GVZ,
> decency supplying the quasi-compact representatives), and it collapses no specialization
> (`AlgebraicGeometry.Stack.eq_of_specializes_of_spacePointMap_eq_of_isRelativelyEtale`); `|W|` is
> sober and `|𝒳|` is sober by Stacks 0GW8, so the two local dimensions agree.

```lean
theorem dimensionAtPoint_eq_topologicalKrullDimAt_of_isDeligneMumfordStack
    (𝒳 : AlgebraicStacks.{u, w} B S hS) (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (hDM : IsDeligneMumfordStack.{u, w} B S hS 𝒳.val.val) (hdec : IsDecent B S hS 𝒳.val)
    (x : points B S hS 𝒳.val.val 𝒳.val.property) :
    dimensionAtPoint B S hS 𝒳 h𝒳 x =
      dimensionSubNat (topologicalKrullDimAt (points B S hS 𝒳.val.val 𝒳.val.property) x) 0
```

**`AlgebraicGeometry.Stack.dimensionAtPoint_eq_topologicalKrullDimAt_of_isDeligneMumfordStack_of_quasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DimensionDeligneMumford.lean, line 397](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DimensionDeligneMumford.lean#L397). The attribute's comment: “quasi-separated Deligne-Mumford stacks: `dim_x(𝒳) = dim_x |𝒳|`”.

> **Stacks 0DRK, the quasi-separated Deligne-Mumford case.** At every point of a locally
> Noetherian, quasi-separated Deligne-Mumford algebraic stack `𝒳` the dimension of `𝒳` agrees with
> the local Krull dimension of `|𝒳|`. A quasi-separated algebraic stack is decent (Stacks 0GW2).

```lean
theorem dimensionAtPoint_eq_topologicalKrullDimAt_of_isDeligneMumfordStack_of_quasiSeparated
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (𝒳 : AlgebraicStacks.{u, w} B S hS) (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (hDM : IsDeligneMumfordStack.{u, w} B S hS 𝒳.val.val)
    (hqs : AlgebraicStacks.IsAbsolutelyQuasiSeparated.{u, w} B S hS hZ 𝒳)
    (x : points B S hS 𝒳.val.val 𝒳.val.property) :
    dimensionAtPoint B S hS 𝒳 h𝒳 x =
      dimensionSubNat (topologicalKrullDimAt (points B S hS 𝒳.val.val 𝒳.val.property) x) 0
```

**`Stacks.Examples.AffineLineQuotient.affineLineQuotientStack_points_dimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/AffineLineQuotientDimension.lean, line 845](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Stacks/AffineLineQuotientDimension.lean#L845). The attribute's comment: “the example [A¹/Gₘ] over a field: |𝒳| has two points, one a specialisation of the other, |𝒳| has Krull dimension 1, and dim\_x(𝒳) = 0 at both points”.

> **Stacks 0DRK, the example `[𝔸¹/𝔾ₘ]`.** Over a field `k`, let `[𝔸¹/𝔾ₘ]` be the quotient stack
> of the multiplicative group acting on the affine line by multiplication. It is an algebraic stack,
> equivalent over the site to an object `𝒳` of the 2-category of algebraic stacks, and for every
> such `𝒳`:
> * `|𝒳|` has exactly two points `x₀ ≠ x₁`, and `x₀` is a specialisation of `x₁` (they are the
>   images of the two orbits `{0}` and `𝔸¹ ∖ {0}`);
> * `|𝒳|` has Krull dimension `1` as a topological space;
> * `𝒳` is locally Noetherian, and `dim_x(𝒳) = 0` (Stacks 0AFN) at both points `x`.

```lean
theorem affineLineQuotientStack_points_dimension {k : Type u} [Field k]
    (hk : C.Contains (Spec (.of k))) :
    (∃ 𝒳 : Stack.AlgebraicStacks.{u, w} C (Spec (.of k)) hk,
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (affineLineQuotientStack C (Spec (.of k)) hk).p 𝒳.val.val.p)) ∧
    ∀ (𝒳 : Stack.AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
      (_e : StacksRepresentableCFG.EquivalenceOver
        (affineLineQuotientStack C (Spec (.of k)) hk).p 𝒳.val.val.p),
      letI := Stack.pointTopology C (Spec (.of k)) hk 𝒳.val
      (∃ x₀ x₁ : Stack.points C (Spec (.of k)) hk 𝒳.val.val 𝒳.val.property,
        x₀ ≠ x₁ ∧ (∀ x, x = x₀ ∨ x = x₁) ∧ x₁ ⤳ x₀) ∧
      topologicalKrullDim (Stack.points C (Spec (.of k)) hk 𝒳.val.val 𝒳.val.property) = 1 ∧
      Stack.IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒳 ∧
      ∀ (h𝒳 : Stack.IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒳) x,
        Stack.dimensionAtPoint C (Spec (.of k)) hk 𝒳 h𝒳 x = 0
```

**`Stacks.Examples.AffineLineQuotient.classifyingStack_multiplicativeGroup_dimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/AffineLineQuotientDimension.lean, line 972](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Stacks/AffineLineQuotientDimension.lean#L972). The attribute's comment: “the example [Spec k/Gₘ]: the classifying stack has a unique point, at which its dimension is -1”.

> **Stacks 0DRK, the example `[Spec k/𝔾ₘ]`.** Over a field `k` the classifying stack
> `[Spec k/𝔾ₘ]` of the multiplicative group is an algebraic stack, equivalent over the site to an
> object `𝒳` of the 2-category of algebraic stacks, and for every such `𝒳`, which is locally
> Noetherian, `|𝒳|` has a unique point, at which `dim_x(𝒳) = -1` (Stacks 0AFN).

```lean
theorem classifyingStack_multiplicativeGroup_dimension {k : Type u} [Field k]
    (hk : C.Contains (Spec (.of k))) :
    (∃ 𝒳 : Stack.AlgebraicStacks.{u, w} C (Spec (.of k)) hk,
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (Stack.classifyingStack C hk (multiplicativeGroupOverField C hk)).val.p 𝒳.val.val.p)) ∧
    ∀ (𝒳 : Stack.AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
      (_e : StacksRepresentableCFG.EquivalenceOver
        (Stack.classifyingStack C hk (multiplicativeGroupOverField C hk)).val.p 𝒳.val.val.p),
      Stack.IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒳 ∧
      ∃ x : Stack.points C (Spec (.of k)) hk 𝒳.val.val 𝒳.val.property,
        (∀ y, y = x) ∧
        ∀ h𝒳 : Stack.IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒳,
          Stack.dimensionAtPoint C (Spec (.of k)) hk 𝒳 h𝒳 x = ((-1 : ℤ) : EInt)
```

**`Stacks.Examples.remark_0DRK`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/DimensionAtPointRemark.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Stacks/DimensionAtPointRemark.lean#L69). The attribute's comment: “the whole remark: dim\_x(𝒳) = dim\_x |𝒳| for decent (in particular quasi-separated) locally Noetherian Deligne-Mumford stacks; for [A¹/Gₘ] over a field |𝒳| has two points, one a specialisation of the other, |𝒳| has dimension 1 and dim\_x(𝒳) = 0 at both points, so the equality fails; [Spec k/Gₘ] has dimension -1 at its unique point”.

> **Stacks 0DRK.** The comparison of the dimension of an algebraic stack at a point (Stacks
> 0AFN) with the local Krull dimension of its space of points.
> 1. For a locally Noetherian Deligne-Mumford stack `𝒳` which is decent, `dim_x(𝒳) = dim_x |𝒳|`
>    at every point `x`.
> 2. The same holds when `𝒳` is quasi-separated.
> 3. Over a field `k`, the quotient stack `[𝔸¹/𝔾ₘ]` of the multiplication action is an algebraic
>    stack, and for every object `𝒳` of the 2-category of algebraic stacks equivalent to it, `|𝒳|`
>    has exactly two points, one a specialisation of the other, `|𝒳|` has Krull dimension `1`, and
>    `𝒳` is locally Noetherian with `dim_x(𝒳) = 0` at both points `x`.
> 4. Consequently the equality of 1 fails for such an `𝒳`: at some point `dim_x(𝒳) ≠ dim_x |𝒳|`.
> 5. Over a field `k`, the classifying stack `[Spec k/𝔾ₘ]` is an algebraic stack, and every object
>    `𝒳` equivalent to it is locally Noetherian, with a unique point `x`, at which
>    `dim_x(𝒳) = -1`.

```lean
theorem remark_0DRK :
    (∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
      (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS)
      (h𝒳 : Stack.IsLocallyNoetherianStack.{u, w} B S hS 𝒳),
      Stack.IsDeligneMumfordStack.{u, w} B S hS 𝒳.val.val → Stack.IsDecent B S hS 𝒳.val →
      ∀ x : Stack.points B S hS 𝒳.val.val 𝒳.val.property,
        Stack.dimensionAtPoint B S hS 𝒳 h𝒳 x =
          Stack.dimensionSubNat
            (topologicalKrullDimAt (Stack.points B S hS 𝒳.val.val 𝒳.val.property) x) 0) ∧
    (∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
      (hZ : B.Contains (⊤_ Scheme.{u}))
      (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS)
      (h𝒳 : Stack.IsLocallyNoetherianStack.{u, w} B S hS 𝒳),
      Stack.IsDeligneMumfordStack.{u, w} B S hS 𝒳.val.val →
      Stack.AlgebraicStacks.IsAbsolutelyQuasiSeparated.{u, w} B S hS hZ 𝒳 →
      ∀ x : Stack.points B S hS 𝒳.val.val 𝒳.val.property,
        Stack.dimensionAtPoint B S hS 𝒳 h𝒳 x =
          Stack.dimensionSubNat
            (topologicalKrullDimAt (Stack.points B S hS 𝒳.val.val 𝒳.val.property) x) 0) ∧
    (∀ (C : BigFppfSite.{u}) (k : Type u) [Field k] (hk : C.Contains (Spec (.of k))),
      (∃ 𝒳 : Stack.AlgebraicStacks.{u, w} C (Spec (.of k)) hk,
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (affineLineQuotientStack C (Spec (.of k)) hk).p 𝒳.val.val.p)) ∧
      ∀ (𝒳 : Stack.AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
        (_e : StacksRepresentableCFG.EquivalenceOver
          (affineLineQuotientStack C (Spec (.of k)) hk).p 𝒳.val.val.p),
        (∃ x₀ x₁ : Stack.points C (Spec (.of k)) hk 𝒳.val.val 𝒳.val.property,
          x₀ ≠ x₁ ∧ (∀ x, x = x₀ ∨ x = x₁) ∧ x₁ ⤳ x₀) ∧
        topologicalKrullDim (Stack.points C (Spec (.of k)) hk 𝒳.val.val 𝒳.val.property) = 1 ∧
        Stack.IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒳 ∧
        ∀ (h𝒳 : Stack.IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒳) x,
          Stack.dimensionAtPoint C (Spec (.of k)) hk 𝒳 h𝒳 x = 0) ∧
    (∀ (C : BigFppfSite.{u}) (k : Type u) [Field k] (hk : C.Contains (Spec (.of k)))
      (𝒳 : Stack.AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
      (_e : StacksRepresentableCFG.EquivalenceOver
        (affineLineQuotientStack C (Spec (.of k)) hk).p 𝒳.val.val.p)
      (h𝒳 : Stack.IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒳),
      ∃ x : Stack.points C (Spec (.of k)) hk 𝒳.val.val 𝒳.val.property,
        Stack.dimensionAtPoint C (Spec (.of k)) hk 𝒳 h𝒳 x ≠
          Stack.dimensionSubNat
            (topologicalKrullDimAt (Stack.points C (Spec (.of k)) hk 𝒳.val.val 𝒳.val.property)
              x) 0) ∧
    (∀ (C : BigFppfSite.{u}) (k : Type u) [Field k] (hk : C.Contains (Spec (.of k))),
      (∃ 𝒳 : Stack.AlgebraicStacks.{u, w} C (Spec (.of k)) hk,
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (Stack.classifyingStack C hk (multiplicativeGroupOverField C hk)).val.p 𝒳.val.val.p)) ∧
      ∀ (𝒳 : Stack.AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
        (_e : StacksRepresentableCFG.EquivalenceOver
          (Stack.classifyingStack C hk (multiplicativeGroupOverField C hk)).val.p 𝒳.val.val.p),
        Stack.IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒳 ∧
        ∃ x : Stack.points C (Spec (.of k)) hk 𝒳.val.val 𝒳.val.property,
          (∀ y, y = x) ∧
          ∀ h𝒳 : Stack.IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒳,
            Stack.dimensionAtPoint C (Spec (.of k)) hk 𝒳 h𝒳 x = ((-1 : ℤ) : EInt))
```

## Tag 0DRL, a definition

[Tag 0DRL](https://stacks.math.columbia.edu/tag/0DRL) in the Stacks Project.

**`AlgebraicGeometry.Stack.relativeStackDimensionAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackMorphism.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackMorphism.lean#L235).

> **Stacks 0DRL.** The relative dimension `dim_t(𝒯_x)` at `t ∈ |𝒯|` of a 1-morphism `f`,
> locally of finite type, of locally Noetherian algebraic stacks: the infimum of the dimensions of
> the locally Noetherian algebraic stack `𝒯 ×_𝒳 Spec k` at a point above `t`, over the
> field-valued points `Spec k ⟶ 𝒳` representing the image `x` of `t` and the points above `t`.
> Those are the two choices the source makes; a point above `t` exists by Stacks 04XH.

```lean
noncomputable def relativeStackDimensionAt (f : 𝒯 ⟶ 𝒳)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (_h𝒯 : IsLocallyNoetherianStack.{u, w} B S hS 𝒯)
    (_h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (t : points B S hS 𝒯.val.val 𝒯.val.property) : EInt
```

## Tag 0DRM, a remark

[Tag 0DRM](https://stacks.math.columbia.edu/tag/0DRM) in the Stacks Project.

**`AlgebraicGeometry.Stack.relativeStackDimensionAt_eq_fieldFibreStackDimensionAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackBaseChange.lean, line 543](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackBaseChange.lean#L543).

> **Stacks 0DRM.** The relative dimension `dim_t(𝒯_x)` of Stacks 0DRL is well defined: for a
> locally-of-finite-type 1-morphism `f : 𝒯 ⟶ 𝒳` of locally Noetherian algebraic stacks and a
> point `t ∈ |𝒯|`, it is the value of the formula of Stacks 0DRL at *every* admissible pair of
> choices — a field-valued point `p` of `𝒳` representing the image of `t` and a point of
> `𝒯 ×_𝒳 Spec κ(p)` above `t`. So the value depends on neither choice.
>
> Both sides are computed on one smooth chart of `𝒯` above `t` by
> `AlgebraicGeometry.Stack.relativeStackDimensionAt_eq_dimensionSubNat_of_isSmooth` and
> `AlgebraicGeometry.Stack.dimensionAtPoint_eq_dimensionSubNat_of_isTwoFibreProduct_fieldFibre`,
> and the chart exists by
> `AlgebraicGeometry.Stack.exists_isSmooth_algebraicSpaceStack_hom_pointsMap_eq`.

```lean
theorem relativeStackDimensionAt_eq_fieldFibreStackDimensionAt
    (f : 𝒯 ⟶ 𝒳) (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (h𝒯 : IsLocallyNoetherianStack.{u, w} B S hS 𝒯)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (t : points B S hS 𝒯.val.val 𝒯.val.property)
    (p : FieldValuedPoint B S hS 𝒳.val.val)
    (q : points B S hS (fieldFibreStackSquare B S hS f p).pt.val.val
      (fieldFibreStackSquare B S hS f p).pt.val.property)
    (hp : pointClass B S hS 𝒳.val.val 𝒳.val.property p =
      pointsMap B S hS 𝒯.val.val 𝒯.val.property 𝒳.val.property f.hom.hom t)
    (hq : pointsMap B S hS (fieldFibreStackSquare B S hS f p).pt.val.val
      (fieldFibreStackSquare B S hS f p).pt.val.property 𝒯.val.property
      (fieldFibreStackSquare B S hS f p).snd.hom.hom q = t) :
    relativeStackDimensionAt.{u, w} B S hS f hf h𝒯 h𝒳 t =
      fieldFibreStackDimensionAt.{u, w} B S hS f hf p q
```

**`AlgebraicGeometry.Stack.relativeStackDimensionAt_eq_fieldFibreStackDimensionAt_of_algebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackRepresentable.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackRepresentable.lean#L121). The attribute's comment: “the case of a source representable by an algebraic space”.

> Let `f : T ⟶ 𝒳` be a 1-morphism, locally of finite type, from the algebraic stack of an
> algebraic space to a locally Noetherian algebraic stack, and let `t ∈ |T|`. Then the relative
> dimension of Stacks 0DRL at `t` is the value of the formula of Stacks 0DRL at *every* admissible
> pair of choices — a field-valued point `p` of `𝒳` representing the image of `t` and a point `q` of
> `T ×_𝒳 Spec κ(p)` above `t`. So that value depends on neither choice.

```lean
theorem relativeStackDimensionAt_eq_fieldFibreStackDimensionAt_of_algebraicSpace
    (T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hT : IsAlgebraicSpace B S hS T)
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (f : algebraicSpaceStack.{u, w} B S hS T hT ⟶ 𝒳)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (h𝒯 : IsLocallyNoetherianStack.{u, w} B S hS (algebraicSpaceStack.{u, w} B S hS T hT))
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (t : points B S hS (fibredCategory B S hS T).val (fibredCategory B S hS T).property)
    (p : FieldValuedPoint B S hS 𝒳.val.val)
    (q : points B S hS (fieldFibreStackSquare B S hS f p).pt.val.val
      (fieldFibreStackSquare B S hS f p).pt.val.property)
    (hp : pointClass B S hS 𝒳.val.val 𝒳.val.property p =
      pointsMap B S hS (fibredCategory B S hS T).val (fibredCategory B S hS T).property
        𝒳.val.property f.hom.hom t)
    (hq : pointsMap B S hS (fieldFibreStackSquare B S hS f p).pt.val.val
      (fieldFibreStackSquare B S hS f p).pt.val.property
      (fibredCategory B S hS T).property
      (fieldFibreStackSquare B S hS f p).snd.hom.hom q = t) :
    relativeStackDimensionAt.{u, w} B S hS f hf h𝒯 h𝒳 t =
      fieldFibreStackDimensionAt.{u, w} B S hS f hf p q
```

## Tag 0DRN, a lemma

[Tag 0DRN](https://stacks.math.columbia.edu/tag/0DRN) in the Stacks Project.

**`AlgebraicGeometry.Stack.relativeStackDimensionAt_fst_eq_relativeStackDimensionAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackBaseChange.lean, line 696](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackBaseChange.lean#L696).

> **Stacks 0DRN.** Let
> ```text
>   𝒯' ⟶ 𝒯
>   |      |
>   v      v
>   𝒳' ⟶ 𝒳
> ```
> be a Cartesian square of 1-morphisms of locally Noetherian algebraic stacks over `S` in which
> the vertical 1-morphisms are locally of finite type. If `t' ∈ |𝒯'|` has images `t`, `x'` and `x`
> in `|𝒯|`, `|𝒳'|` and `|𝒳|`, then `dim_{t'}(𝒯'_{x'}) = dim_t(𝒯_x)`.
>
> Both sides are infima of sets of values of the formula of Stacks 0DRL, and the chart formula
> `AlgebraicGeometry.Stack.dimensionAtPoint_eq_dimensionSubNat_of_isTwoFibreProduct_fieldFibre`
> evaluates every member of either set at one and the same smooth chart `U ⟶ 𝒯` of `𝒯` above `t`:
> the fibre `𝒯' ×_{𝒳'} Spec κ(p')` over a field-valued point `p'` of `𝒳'` is, pasted with the
> Cartesian square and reindexed along
> `AlgebraicGeometry.Stack.fieldValuedPointMorphism_comp_iso`, a 2-fibre product of the vertical
> 1-morphism `𝒯 ⟶ 𝒳` with the 1-morphism of the image field-valued point of `𝒳`. So no
> field-valued point of `𝒳` has to be lifted to `𝒳'`, which is what the source's one-line proof
> elides.

```lean
theorem relativeStackDimensionAt_fst_eq_relativeStackDimensionAt
    {𝒳' 𝒯 𝒳 : AlgebraicStacks.{u, w} B S hS} (g : 𝒳' ⟶ 𝒳) (f : 𝒯 ⟶ 𝒳)
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (hfst : AlgebraicStacks.IsLocallyOfFiniteType B S hS P.fst)
    (h𝒯' : IsLocallyNoetherianStack.{u, w} B S hS P.pt)
    (h𝒯 : IsLocallyNoetherianStack.{u, w} B S hS 𝒯)
    (h𝒳' : IsLocallyNoetherianStack.{u, w} B S hS 𝒳')
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (t' : points B S hS P.pt.val.val P.pt.val.property) :
    relativeStackDimensionAt.{u, w} B S hS P.fst hfst h𝒯' h𝒳' t' =
      relativeStackDimensionAt.{u, w} B S hS f hf h𝒯 h𝒳
        (pointsMap B S hS P.pt.val.val P.pt.val.property 𝒯.val.property P.snd.hom.hom t')
```

## Tag 0DRP, a lemma

[Tag 0DRP](https://stacks.math.columbia.edu/tag/0DRP) in the Stacks Project.

**`AlgebraicGeometry.Stack.dimensionAtPoint_eq_add_relativeStackDimensionAt_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionSmoothStacks.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionSmoothStacks.lean#L84).

> If `f : 𝒰 ⟶ 𝒳` is a smooth 1-morphism, locally of finite type, of locally Noetherian
> algebraic stacks over `S` and `u ∈ |𝒰|` has image `x ∈ |𝒳|`, then
> `dim_u(𝒰) = dim_x(𝒳) + dim_u(𝒰_x)`,
> the relative dimension being that of Stacks 0DRL and the two dimensions those of Stacks 0AFN.

```lean
theorem dimensionAtPoint_eq_add_relativeStackDimensionAt_of_isSmooth
    {𝒰 𝒳 : AlgebraicStacks.{u, w} B S hS} (f : 𝒰 ⟶ 𝒳)
    (hsm : AlgebraicStacks.IsSmooth B S hS f)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (h𝒰 : IsLocallyNoetherianStack.{u, w} B S hS 𝒰)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (u : points B S hS 𝒰.val.val 𝒰.val.property) :
    dimensionAtPoint B S hS 𝒰 h𝒰 u =
      dimensionAtPoint B S hS 𝒳 h𝒳
          (pointsMap B S hS 𝒰.val.val 𝒰.val.property 𝒳.val.property f.hom.hom u) +
        relativeStackDimensionAt.{u, w} B S hS f hf h𝒰 h𝒳 u
```

**`AlgebraicGeometry.Stack.dimensionAtPoint_eq_dimensionAtPoint_add_relativeStackDimensionAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionSmoothStacks.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionSmoothStacks.lean#L126).

> If `f : 𝒰 ⟶ 𝒳` is a smooth 1-morphism of locally Noetherian algebraic stacks over `S` and
> `u ∈ |𝒰|` has image `x ∈ |𝒳|`, then
> `dim_u(𝒰) = dim_x(𝒳) + dim_u(𝒰_x)`,
> the relative dimension being that of Stacks 0DRL and the two dimensions those of Stacks 0AFN.
> Local finite type of `f`, which the relative dimension takes as an argument, is derived from
> smoothness by `AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_of_isSmooth`.

```lean
theorem dimensionAtPoint_eq_dimensionAtPoint_add_relativeStackDimensionAt
    {𝒰 𝒳 : AlgebraicStacks.{u, w} B S hS} (f : 𝒰 ⟶ 𝒳)
    (hsm : AlgebraicStacks.IsSmooth B S hS f)
    (h𝒰 : IsLocallyNoetherianStack.{u, w} B S hS 𝒰)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (u : points B S hS 𝒰.val.val 𝒰.val.property) :
    dimensionAtPoint B S hS 𝒰 h𝒰 u =
      dimensionAtPoint B S hS 𝒳 h𝒳
          (pointsMap B S hS 𝒰.val.val 𝒰.val.property 𝒳.val.property f.hom.hom u) +
        relativeStackDimensionAt.{u, w} B S hS f
          (AlgebraicStacks.isLocallyOfFiniteType_of_isSmooth B S hS f hsm) h𝒰 h𝒳 u
```

## Tag 0DRQ, a lemma

[Tag 0DRQ](https://stacks.math.columbia.edu/tag/0DRQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isOpen_setOf_relativeDimensionAt_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionLocalConstancy.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionLocalConstancy.lean#L146). The attribute's comment: “part (1) for a morphism of algebraic spaces”.

> For a morphism `g : T ⟶ G` of algebraic spaces over `S` which is locally of finite type, the
> locus of points of `|T|` at which the fibre dimension `dim_t(T_{g(t)})` of Stacks 0DRG is at most
> `n` is open.

```lean
theorem isOpen_setOf_relativeDimensionAt_le
    {T G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hT : IsAlgebraicSpace B S hS T) (hG : IsAlgebraicSpace B S hS G) (g : T ⟶ G)
    (hg : Space.IsLocallyOfFiniteType B S hS g)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS
      (algebraicSpaceStackMap.{u, w} B S hS hT hG g))
    (n : ℕ) :
    IsOpen {t : Space.points B S hS T |
      relativeDimensionAt.{u, w} B S hS T hT (algebraicSpaceStack.{u, w} B S hS G hG)
        (algebraicSpaceStackMap.{u, w} B S hS hT hG g) hf t ≤ (n : WithBot ℕ∞)}
```

**`AlgebraicGeometry.Stack.isLocallyConstant_relativeDimensionAt_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionLocalConstancy.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionLocalConstancy.lean#L176). The attribute's comment: “part (2) for a morphism of algebraic spaces”. References: EGA IV (17.10.2), “more general”.

> For a smooth morphism `g : T ⟶ G` of algebraic spaces over `S`, the fibre dimension
> `t ↦ dim_t(T_{g(t)})` of Stacks 0DRG is locally constant on `|T|`.

```lean
theorem isLocallyConstant_relativeDimensionAt_of_isSmooth
    {T G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hT : IsAlgebraicSpace B S hS T) (hG : IsAlgebraicSpace B S hS G) (g : T ⟶ G)
    (hg : Space.IsSmooth B S hS g) :
    IsLocallyConstant
      (relativeDimensionAt.{u, w} B S hS T hT (algebraicSpaceStack.{u, w} B S hS G hG)
        (algebraicSpaceStackMap.{u, w} B S hS hT hG g)
        (isLocallyOfFiniteType_algebraicSpaceStackMap_of_isSmooth.{u, w} B S hS hT hG g hg))
```

**`AlgebraicGeometry.Stack.upperSemicontinuous_relativeStackDimensionAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackLocalConstancy.lean, line 447](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackLocalConstancy.lean#L447). The attribute's comment: “part (1)”.

> For a locally-of-finite-type 1-morphism `f : 𝒯 ⟶ 𝒳` of locally Noetherian algebraic stacks,
> the function `t ↦ dim_t(𝒯_{f(t)})` of Stacks 0DRL is upper semi-continuous on `|𝒯|`.

```lean
theorem upperSemicontinuous_relativeStackDimensionAt :
    UpperSemicontinuous (relativeStackDimensionAt.{u, w} B S hS f hf h𝒯 h𝒳)
```

**`AlgebraicGeometry.Stack.isLocallyConstant_relativeStackDimensionAt_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackLocalConstancy.lean, line 463](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackLocalConstancy.lean#L463). The attribute's comment: “part (2)”. References: EGA IV (17.10.2), “special case”.

> For a smooth 1-morphism `f : 𝒯 ⟶ 𝒳` of locally Noetherian algebraic stacks, the function
> `t ↦ dim_t(𝒯_{f(t)})` of Stacks 0DRL is locally constant on `|𝒯|`.

```lean
theorem isLocallyConstant_relativeStackDimensionAt_of_isSmooth
    (hfsm : AlgebraicStacks.IsSmooth B S hS f) :
    IsLocallyConstant (relativeStackDimensionAt.{u, w} B S hS f hf h𝒯 h𝒳)
```

**`AlgebraicGeometry.Stack.isOpen_setOf_relativeStackDimension_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackUpperSemicontinuous.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackUpperSemicontinuous.lean#L261). The attribute's comment: “part (1), as openness of the sublevel sets”.

> Let `f : 𝒯 ⟶ 𝒳` be a locally-of-finite-type 1-morphism of algebraic stacks over `S`. Then
> every sublevel set of the function `t ↦ dim_t(𝒯_{f(t)})` of Stacks 0DRL is open in `|𝒯|`.

```lean
theorem isOpen_setOf_relativeStackDimension_le (c : EInt) :
    IsOpen {t : points B S hS 𝒯.val.val 𝒯.val.property |
      relativeStackDimension.{u, w} B S hS f hf t ≤ c}
```

**`AlgebraicGeometry.Stack.upperSemicontinuous_relativeStackDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackUpperSemicontinuous.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackUpperSemicontinuous.lean#L325). The attribute's comment: “part (1)”.

> For a locally-of-finite-type 1-morphism `f : 𝒯 ⟶ 𝒳` of algebraic stacks, the function
> `t ↦ dim_t(𝒯_{f(t)})` of Stacks 0DRL is upper semi-continuous on `|𝒯|`.

```lean
theorem upperSemicontinuous_relativeStackDimension :
    UpperSemicontinuous (relativeStackDimension.{u, w} B S hS f hf)
```

**`AlgebraicGeometry.Stack.isLocallyConstant_relativeStackDimension_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackUpperSemicontinuous.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDimensionStackUpperSemicontinuous.lean#L335). The attribute's comment: “part (2)”. References: EGA IV (17.10.2), “more general”.

> For a smooth, locally-of-finite-type 1-morphism `f : 𝒯 ⟶ 𝒳` of algebraic stacks, the function
> `t ↦ dim_t(𝒯_{f(t)})` of Stacks 0DRL is locally constant on `|𝒯|`.

```lean
theorem isLocallyConstant_relativeStackDimension_of_isSmooth
    (hfsm : AlgebraicStacks.IsSmooth B S hS f) :
    IsLocallyConstant (relativeStackDimension.{u, w} B S hS f hf)
```

## Tag 0DRR, a lemma

[Tag 0DRR](https://stacks.math.columbia.edu/tag/0DRR) in the Stacks Project.

**`AlgebraicGeometry.exists_isClosed_isFiniteTypePoint_dim_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Exercises/NonExercises/DimensionFiniteTypePoint.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Exercises/NonExercises/DimensionFiniteTypePoint.lean#L81).

> A finite-dimensional scheme has a closed finite type point at which its local dimension
> equals its dimension.

```lean
theorem exists_isClosed_isFiniteTypePoint_dim_eq
    (X : Scheme.{u}) (d : ℕ) (hX : topologicalKrullDim X = d) :
    ∃ x : X, IsClosed ({x} : Set X) ∧
      IsFiniteTypePoint x ∧
      topologicalKrullDimAt X x = topologicalKrullDim X
```

## Tag 0DRT, a lemma

[Tag 0DRT](https://stacks.math.columbia.edu/tag/0DRT) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDim_eq_of_isOpen_of_catenary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/ConstancyOfDimension.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/ConstancyOfDimension.lean#L227). The attribute's comment: “dimension of nonempty opens”. References: SGA 3 VIB (1.5), “more general”.

> A nonempty open subset of an irreducible, Jacobson, catenary, locally Noetherian scheme of
> finite dimension has the same dimension as the scheme.

```lean
theorem topologicalKrullDim_eq_of_isOpen_of_catenary
    (X : Scheme.{u}) [IrreducibleSpace X] [JacobsonSpace X]
    (hcat : IrreducibleClosedsCodim.IsCatenarySpace X) [IsLocallyNoetherian X]
    (d : ℕ) (hX : topologicalKrullDim X = d)
    (U : Set X) (hU : IsOpen U) (hne : U.Nonempty) :
    topologicalKrullDim X = topologicalKrullDim U
```

**`AlgebraicGeometry.isConstant_topologicalKrullDimAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/ConstancyOfDimension.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/ConstancyOfDimension.lean#L241). The attribute's comment: “constancy of local dimension”.

> On an irreducible, Jacobson, catenary, locally Noetherian scheme of finite dimension, the
> local Krull dimension is constant.

```lean
theorem isConstant_topologicalKrullDimAt
    (X : Scheme.{u}) [IrreducibleSpace X] [JacobsonSpace X]
    (hcat : IrreducibleClosedsCodim.IsCatenarySpace X) [IsLocallyNoetherian X]
    (d : ℕ) (hX : topologicalKrullDim X = d) :
    ∀ x y : X, topologicalKrullDimAt X x = topologicalKrullDimAt X y
```

## Tag 0DRU, a definition

[Tag 0DRU](https://stacks.math.columbia.edu/tag/0DRU) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsPseudoCatenary`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PseudoCatenaryAlgebraicStack.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/PseudoCatenaryAlgebraicStack.lean#L57).

> **Stacks 0DRU.** An algebraic stack over `S` is *pseudo-catenary* when it admits a smooth
> surjective 1-morphism from a scheme of the big fppf site over `S` whose underlying scheme is
> locally Noetherian and universally catenary.

```lean
abbrev IsPseudoCatenary (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS) : Prop
```

## Tag 0DRV, an example

[Tag 0DRV](https://stacks.math.columbia.edu/tag/0DRV) in the Stacks Project.

**`AlgebraicGeometry.Stack.isPseudoCatenary_of_isLocallyOfFiniteType_over_scheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PseudoCatenary.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/PseudoCatenary.lean#L226).

> **Stacks 0DRV.** An algebraic stack locally of finite type over a locally Noetherian
> universally catenary scheme `S` is pseudo-catenary.
>
> Any smooth surjective scheme atlas serves as the witness, its source being universally catenary
> by `AlgebraicGeometry.Stack.isUniversallyCatenary_of_isSmooth_schemeStack`.

```lean
theorem isPseudoCatenary_of_isLocallyOfFiniteType_over_scheme [IsLocallyNoetherian S]
    (hcat : Scheme.IsUniversallyCatenary S) (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : AlgebraicStacks.IsLocallyOfFiniteType B S hS (structureMorphism B S hS 𝒳)) :
    AlgebraicStacks.IsPseudoCatenary B S hS 𝒳
```

## Tag 0DRW, a lemma

[Tag 0DRW](https://stacks.math.columbia.edu/tag/0DRW) in the Stacks Project.

**`AlgebraicGeometry.Stack.isPseudoCatenary_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PseudoCatenary.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/PseudoCatenary.lean#L242).

> **Stacks 0DRW.** The source of a 1-morphism of algebraic stacks over `S` which is locally of
> finite type and whose target is pseudo-catenary is pseudo-catenary.
>
> For a universally catenary smooth surjective scheme atlas `U ⟶ 𝒳` and a smooth surjective scheme
> atlas `V ⟶ 𝒴 ×_𝒳 U`, the composite `V ⟶ 𝒴 ×_𝒳 U ⟶ 𝒴` is smooth and surjective while
> `V ⟶ 𝒴 ×_𝒳 U ⟶ U` is locally of finite type, so `V` is universally catenary by Stacks 02J9.

```lean
theorem isPseudoCatenary_of_isLocallyOfFiniteType {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒴 ⟶ 𝒳) (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (h𝒳 : AlgebraicStacks.IsPseudoCatenary B S hS 𝒳) :
    AlgebraicStacks.IsPseudoCatenary B S hS 𝒴
```

## Tag 0DRX, a lemma

[Tag 0DRX](https://stacks.math.columbia.edu/tag/0DRX) in the Stacks Project.

**`AlgebraicGeometry.Stack.isConstant_dimensionAtPoint_of_irreducibleSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ConstancyOfStackDimension.lean, line 457](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ConstancyOfStackDimension.lean#L457).

> **Stacks 0DRX.** On a Jacobson, pseudo-catenary, locally Noetherian algebraic stack `𝒳`
> over `S` whose space of points `|𝒳|` is irreducible, the dimension `dim_x(𝒳)` of Stacks 0AFN is
> the same at every point of `|𝒳|`.
>
> Pseudo-catenarity (Stacks 0DRU) provides a smooth surjective 1-morphism from the algebraic stack
> of a scheme `U` of the site which is locally Noetherian and universally catenary; `U` is then
> catenary, and Jacobson by the universal scheme criterion of Stacks 04YF. The dimension formula of
> Stacks 0DRJ holds along that chart, read as a chart by the algebraic space `U` represents, and the
> relative dimension occurring in it is locally constant by Stacks 0DRQ (2). Around each point of
> `U` the local dimension of `U` is then the dimension of a nonempty open irreducible subset, by
> Stacks 0DRT at the irreducible components, so `dim_x(𝒳)` takes on the image of that subset the
> single value it has at the given point; two such images meet in `|𝒳|`, which is irreducible, and
> that common point identifies any two values.

```lean
theorem isConstant_dimensionAtPoint_of_irreducibleSpace (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (h𝒳Jacobson : AlgebraicStacks.IsJacobson B S hS 𝒳)
    (h𝒳Catenary : AlgebraicStacks.IsPseudoCatenary B S hS 𝒳)
    (h𝒳Irreducible : @IrreducibleSpace _ (pointTopology B S hS 𝒳.val)) :
    ∀ x y : points B S hS 𝒳.val.val 𝒳.val.property,
      dimensionAtPoint B S hS 𝒳 h𝒳 x = dimensionAtPoint B S hS 𝒳 h𝒳 y
```

## Tag 0DRY, a lemma

[Tag 0DRY](https://stacks.math.columbia.edu/tag/0DRY) in the Stacks Project.

**`AlgebraicGeometry.Stack.dimensionAtPoint_le_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DimensionClosedImmersion.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DimensionClosedImmersion.lean#L138).

> If `i : 𝒵 ⟶ 𝒳` is a closed immersion of locally Noetherian algebraic stacks over `S` and
> `z ∈ |𝒵|` has image `x ∈ |𝒳|`, then `dim_z(𝒵) ≤ dim_x(𝒳)`, the dimensions being those of
> Stacks 0AFN.

```lean
theorem dimensionAtPoint_le_of_isClosedImmersion
    {𝒵 𝒳 : AlgebraicStacks.{u, w} B S hS} (i : 𝒵 ⟶ 𝒳)
    (hi : AlgebraicStacks.IsClosedImmersion B S hS i)
    (h𝒵 : IsLocallyNoetherianStack.{u, w} B S hS 𝒵)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (z : points B S hS 𝒵.val.val 𝒵.val.property) :
    dimensionAtPoint B S hS 𝒵 h𝒵 z ≤
      dimensionAtPoint B S hS 𝒳 h𝒳
        (pointsMap B S hS 𝒵.val.val 𝒵.val.property 𝒳.val.property i.hom.hom z)
```

## Tag 0DRZ, a lemma

[Tag 0DRZ](https://stacks.math.columbia.edu/tag/0DRZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.dimensionAtPoint_eq_sSup_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DimensionIrreducibleComponentsSupremum.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DimensionIrreducibleComponentsSupremum.lean#L399).

> **Stacks 0DRZ.** For a locally Noetherian algebraic stack `𝒳` over `S` and a point
> `x ∈ |𝒳|`, the dimension of Stacks 0AFN at `x` is the supremum of the dimensions at `x` of the
> irreducible components of `|𝒳|` through `x`, each endowed with its induced reduced structure:
>
> `dim_x(𝒳) = sup_𝒯 dim_x(𝒯)`.
>
> The inequality `sup_𝒯 dim_x(𝒯) ≤ dim_x(𝒳)` is Stacks 0DRY
> (`AlgebraicGeometry.Stack.sSup_componentDimensionsAt_le`). For the reverse inequality, the
> source's equation Stacks 0DS0, choose a smooth surjective chart `f : U ⟶ 𝒳` by a scheme and a
> point `u` over `x`; some irreducible component `T'` of `U` through `u` has `dim_u(T') = dim_u(U)`
> (`AlgebraicGeometry.Stack.exists_mem_irreducibleComponents_topologicalKrullDimAt_eq_of_isSmooth`).
> The closure `T` of its image is an irreducible component of `|𝒳|` through `x` (Stacks 0DR5), and it
> carries a reduced closed substack `𝒯` with `|𝒯| = T` (the existence half of Stacks 0509,
> `AlgebraicGeometry.Stack.exists_isClosedSubstack_isReducedStack_range_pointsMap_eq`). Then
> `AlgebraicGeometry.Stack.exists_dimensionAtPoint_le_of_isClosedImmersion_of_image_subset`, applied
> to `A = T'`, produces a point of `𝒯` over `x` at which `dim_x(𝒳) ≤ dim(𝒯)`.

```lean
theorem dimensionAtPoint_eq_sSup_irreducibleComponents (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (x : points B S hS 𝒳.val.val 𝒳.val.property) :
    dimensionAtPoint B S hS 𝒳 h𝒳 x = sSup (componentDimensionsAt B S hS 𝒳 x)
```

## Tag 0DS1, a lemma

[Tag 0DS1](https://stacks.math.columbia.edu/tag/0DS1) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isFiniteTypePoint_mem_pointSet_dimensionAtPoint_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DimensionAtFiniteTypePoint.lean, line 469](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DimensionAtFiniteTypePoint.lean#L469).

> **Stacks 0DS1.** Let `𝒳` be a locally Noetherian algebraic stack over `S`, let `𝒱` be an open
> substack of `𝒳` and let `x ∈ |𝒱|`. Then there is a finite type point `x₀ ∈ |𝒱|` — a finite type
> point both of `𝒱` and of `𝒳` — with `dim_{x₀}(𝒳) = dim_x(𝒱)`.
>
> The point `x` of `|𝒳|` lying in `|𝒱|` is given as a point of `|𝒱|`, which is what membership in
> `AlgebraicGeometry.Stack.OpenSubstack.pointSet` says, and `dim_x(𝒱)` is the dimension of
> Stacks 0AFN of the open substack read as an algebraic stack; that it is locally Noetherian is
> **Stacks 0CPM**, `AlgebraicGeometry.Stack.isLocallyNoetherianStack_toAlgebraicStack`.
>
> The source reduces to a smooth chart of `𝒱` and performs two shrinkings there, which is
> `AlgebraicGeometry.Stack.exists_isFiniteTypePoint_dimensionAtPoint_eq` applied to `𝒱`. What
> remains is to pass from `𝒱` back to `𝒳`: the inclusion of an open substack is locally of finite
> type, so it carries finite type points to finite type points (**Stacks 06G0**), and it leaves the
> dimension of Stacks 0AFN unchanged, which is
> `AlgebraicGeometry.Stack.dimensionAtPoint_pointsMap_eq_of_isOpenImmersion`.

```lean
theorem exists_isFiniteTypePoint_mem_pointSet_dimensionAtPoint_eq
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (𝒱 : OpenSubstack 𝒳)
    (x : points B S hS
      (fullSubcategoryAlgebraicStack 𝒳 𝒱.property 𝒱.isAlgebraic).val.val
      (fullSubcategoryAlgebraicStack 𝒳 𝒱.property 𝒱.isAlgebraic).val.property) :
    ∃ x₀ : points B S hS
        (fullSubcategoryAlgebraicStack 𝒳 𝒱.property 𝒱.isAlgebraic).val.val
        (fullSubcategoryAlgebraicStack 𝒳 𝒱.property 𝒱.isAlgebraic).val.property,
      IsFiniteTypePoint.{u, w} B S hS
          (fullSubcategoryAlgebraicStack 𝒳 𝒱.property 𝒱.isAlgebraic) x₀ ∧
        IsFiniteTypePoint.{u, w} B S hS 𝒳
            (AlgebraicStacks.pointsMap B S hS 𝒱.inclusion x₀) ∧
          AlgebraicStacks.pointsMap B S hS 𝒱.inclusion x₀ ∈ 𝒱.pointSet B S hS ∧
            dimensionAtPoint B S hS 𝒳 h𝒳
                (AlgebraicStacks.pointsMap B S hS 𝒱.inclusion x₀) =
              dimensionAtPoint B S hS
                (fullSubcategoryAlgebraicStack 𝒳 𝒱.property 𝒱.isAlgebraic)
                (isLocallyNoetherianStack_toAlgebraicStack B S hS 𝒱 h𝒳) x
```

## Tag 0DS2, a lemma

[Tag 0DS2](https://stacks.math.columbia.edu/tag/0DS2) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_openSubstack_isOpenImmersion_subset_irreducibleComponent'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismGenericOpenImmersion.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismGenericOpenImmersion.lean#L289).

> **Stacks 0DS2** (Morphisms of Algebraic Stacks, Lemma 107.5.21), with every input
> discharged. Let `m : 𝒯 ⟶ 𝒳` be a
> monomorphism of algebraic stacks over `S` which is locally of finite type, with `𝒳` Jacobson,
> pseudo-catenary and locally Noetherian, with `|𝒯|` irreducible and `𝒯` of dimension `d` in the
> sense of Stacks 0AFP, and with `𝒳` reduced of dimension at most `d`. Then there is a non-empty
> open substack `𝒱` of `𝒯`, in the sense of **Stacks 04YM**, such that `𝒱 ⟶ 𝒳` is an open
> immersion identifying `𝒱` with an open subset of an irreducible component of `|𝒳|`: its range
> on points lies in an irreducible component `Z` and is open in `|𝒳|`, hence open in the subspace
> `Z`, and the open immersion makes `|𝒱| → |𝒳|` a homeomorphism onto that range.
>
> The source derives the Jacobson, pseudo-catenary and locally Noetherian properties of `𝒯` from
> those of `𝒳`; of these only local Noetherianity is needed, and only so that the dimension of
> `𝒯` is defined, and it is supplied in the statement of `h𝒯dim` by **Stacks 06R6** rather than
> assumed.
>
> The dimension hypotheses enter the proof only through the chart-level conclusion
> `AlgebraicGeometry.Stack.exists_chart_openSubspace_isSmooth`: the source's argument on a smooth
> surjective chart `U ⟶ 𝒳` by a reduced algebraic space, its base change `U' = 𝒯 ×_𝒳 U`, and the
> étale-local structure of the unramified monomorphism `U' ⟶ U`, concludes that some non-empty open
> `W ⊆ U'` has `W ⟶ U` étale and hence `W ⟶ 𝒳` smooth. The module's "The chart" says where that is
> proved.
>
> The rest, and the content of this module, is the source's last step. Stacks 05UP
> turns the smooth 1-morphism `W ⟶ 𝒯` into the open substack `𝒱` of `𝒯` covered by `|W|` with a
> smooth surjective factorization `q : W ⟶ 𝒱` satisfying `q ≫ 𝒱.inclusion = W ⟶ 𝒯`; since
> `q ≫ (𝒱.inclusion ≫ m)` is the smooth 1-morphism `W ⟶ 𝒳`, source-side cancellation of
> smoothness along `q` gives `𝒱.inclusion ≫ m` smooth, and Stacks 04ZY makes it a monomorphism. A
> smooth monomorphism of algebraic stacks is an open immersion. Finally `|𝒱|` is a non-empty open
> subset of the irreducible `|𝒯|`, hence irreducible, so its continuous image in `|𝒳|` is
> irreducible and lies in an irreducible component, and that image is open because `𝒱 ⟶ 𝒳` is
> smooth.

```lean
theorem exists_openSubstack_isOpenImmersion_subset_irreducibleComponent'
    {𝒯 𝒳 : AlgebraicStacks.{u, w} B S hS} (m : 𝒯 ⟶ 𝒳)
    (hmono : AlgebraicStacks.IsMonomorphism B S hS m)
    (hft : AlgebraicStacks.IsLocallyOfFiniteType B S hS m)
    (h𝒳Jacobson : AlgebraicStacks.IsJacobson B S hS 𝒳)
    (h𝒳Catenary : AlgebraicStacks.IsPseudoCatenary B S hS 𝒳)
    (h𝒳N : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (h𝒯Irreducible : @IrreducibleSpace _ (pointTopology B S hS 𝒯.val))
    (d : ℕ) (h𝒯dim : dimension B S hS 𝒯
      (AlgebraicStacks.isLocallyNoetherian_of_isLocallyOfFiniteType.{u, w} B S hS m hft h𝒳N) =
      ((d : ℤ) : EInt))
    (h𝒳red : IsReducedStack B S hS 𝒳)
    (h𝒳dim : dimension B S hS 𝒳 h𝒳N ≤ ((d : ℤ) : EInt)) :
    ∃ 𝒱 : OpenSubstack 𝒯, (𝒱.pointSet B S hS).Nonempty ∧
      AlgebraicStacks.IsOpenImmersion B S hS (𝒱.inclusion ≫ m) ∧
        ∃ Z ∈ @irreducibleComponents _ (pointTopology B S hS 𝒳.val),
          Set.range (AlgebraicStacks.pointsMap B S hS (𝒱.inclusion ≫ m)) ⊆ Z ∧
            @IsOpen _ (pointTopology B S hS 𝒳.val)
              (Set.range (AlgebraicStacks.pointsMap B S hS (𝒱.inclusion ≫ m)))
```

## Tag 0DS4, a lemma

[Tag 0DS4](https://stacks.math.columbia.edu/tag/0DS4) in the Stacks Project.

**`AlgebraicGeometry.Stack.dimension_le_closedSubstackDimension_add_relativeStackDimensionAt_of_isQuasiCompactMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DimensionSchemeTheoreticImage.lean, line 980](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DimensionSchemeTheoreticImage.lean#L980). The attribute's comment: “the inequality at every point of 𝒯, for f quasi-compact as in the statement”.

> **The inequality of Stacks 0DS4 for a quasi-compact 1-morphism.** Under the hypotheses of
> `exists_isOpen_dimension_eq_add_relativeStackDimensionAt_of_isQuasiCompactMorphism`,
> `dim(𝒯) ≤ dim(𝒵) + dim_t(𝒯_{f(t)})` at *every* `t ∈ |𝒯|`.
>
> The generic equality implies it, by
> `AlgebraicGeometry.Stack.dimension_le_add_relativeStackDimensionAt_of_exists_isOpen` — the upper
> semi-continuity of Stacks 0DRQ (1) together with the constancy of Stacks 0DRX.

```lean
theorem dimension_le_closedSubstackDimension_add_relativeStackDimensionAt_of_isQuasiCompactMorphism
    {𝒯 𝒳 : AlgebraicStacks.{u, w} B S hS} (f : 𝒯 ⟶ 𝒳)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (hfQC : IsQuasiCompactMorphism B S hS f)
    (h𝒯 : IsLocallyNoetherianStack.{u, w} B S hS 𝒯)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (h𝒯Jacobson : AlgebraicStacks.IsJacobson B S hS 𝒯)
    (h𝒳Jacobson : AlgebraicStacks.IsJacobson B S hS 𝒳)
    (h𝒯Catenary : AlgebraicStacks.IsPseudoCatenary B S hS 𝒯)
    (h𝒳Catenary : AlgebraicStacks.IsPseudoCatenary B S hS 𝒳)
    (h𝒯Irreducible : @IrreducibleSpace _ (pointTopology B S hS 𝒯.val))
    (_h𝒳QuasiSeparated : IsQuasiSeparatedAbs.{u, w, w} B S hS 𝒳)
    {P : ObjectProperty 𝒳.val.val.obj} (hP : IsSchemeTheoreticImage f P)
    (t : points B S hS 𝒯.val.val 𝒯.val.property) :
    dimension B S hS 𝒯 h𝒯 ≤
      closedSubstackDimension B S hS 𝒳 P hP.1 hP.isAlgebraicStack h𝒳 +
        relativeStackDimensionAt.{u, w} B S hS f hf h𝒯 h𝒳 t
```

**`AlgebraicGeometry.Stack.dimension_le_add_and_exists_isOpen_dense_eq_add_relativeStackDimensionAt_of_isQuasiCompactMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DimensionSchemeTheoreticImage.lean, line 1010](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DimensionSchemeTheoreticImage.lean#L1010). The attribute's comment: “both clauses: the inequality at every point and the equality on a dense open subset, for f quasi-compact as in the statement”.

> **The content of Stacks 0DS4 for a quasi-compact 1-morphism.** Let `f : 𝒯 ⟶ 𝒳` be a
> quasi-compact 1-morphism locally of finite type of Jacobson, pseudo-catenary, locally Noetherian
> algebraic stacks over `S` with `|𝒯|` irreducible and `𝒳` quasi-separated, and let `P` cut out the
> scheme theoretic image `𝒵` of Stacks 0CMI. Then `dim(𝒯) ≤ dim(𝒵) + dim_t(𝒯_{f(t)})` at every
> `t ∈ |𝒯|`, and equality holds on an open subset of `|𝒯|` that is nonempty, equivalently dense,
> `|𝒯|` being irreducible.

```lean
theorem
  dimension_le_add_and_exists_isOpen_dense_eq_add_relativeStackDimensionAt_of_isQuasiCompactMorphism
    {𝒯 𝒳 : AlgebraicStacks.{u, w} B S hS} (f : 𝒯 ⟶ 𝒳)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (hfQC : IsQuasiCompactMorphism B S hS f)
    (h𝒯 : IsLocallyNoetherianStack.{u, w} B S hS 𝒯)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (h𝒯Jacobson : AlgebraicStacks.IsJacobson B S hS 𝒯)
    (h𝒳Jacobson : AlgebraicStacks.IsJacobson B S hS 𝒳)
    (h𝒯Catenary : AlgebraicStacks.IsPseudoCatenary B S hS 𝒯)
    (h𝒳Catenary : AlgebraicStacks.IsPseudoCatenary B S hS 𝒳)
    (h𝒯Irreducible : @IrreducibleSpace _ (pointTopology B S hS 𝒯.val))
    (h𝒳QuasiSeparated : IsQuasiSeparatedAbs.{u, w, w} B S hS 𝒳)
    {P : ObjectProperty 𝒳.val.val.obj} (hP : IsSchemeTheoreticImage f P) :
    (∀ t : points B S hS 𝒯.val.val 𝒯.val.property,
        dimension B S hS 𝒯 h𝒯 ≤
          closedSubstackDimension B S hS 𝒳 P hP.1 hP.isAlgebraicStack h𝒳 +
            relativeStackDimensionAt.{u, w} B S hS f hf h𝒯 h𝒳 t) ∧
      ∃ W : Set (points B S hS 𝒯.val.val 𝒯.val.property),
        @IsOpen _ (pointTopology B S hS 𝒯.val) W ∧ W.Nonempty ∧
          @Dense _ (pointTopology B S hS 𝒯.val) W ∧
          ∀ t ∈ W, dimension B S hS 𝒯 h𝒯 =
            closedSubstackDimension B S hS 𝒳 P hP.1 hP.isAlgebraicStack h𝒳 +
              relativeStackDimensionAt.{u, w} B S hS f hf h𝒯 h𝒳 t
```

**`AlgebraicGeometry.Stack.forall_dimension_le_closedSubstackDimension_add_relativeStackDimensionAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DimensionSchemeTheoreticImageInequality.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DimensionSchemeTheoreticImageInequality.lean#L123). The attribute's comment: “the inequality clause, for every f (no quasi-compactness), under the hypotheses of the statement in the Stacks Project other than quasi-compactness of f. The equality clause needs f quasi-compact and is registered on AlgebraicGeometry.Stack.dimension\_le\_add\_and\_exists\_isOpen\_dense\_eq\_add\_relativeStackDimensionAt\_of\_isQuasiCompactMorphism; without quasi-compactness it is refuted by AlgebraicGeometry.Stack.not\_forall\_dimension\_le\_add\_and\_exists\_isOpen\_dense\_eq”.

> **The inequality clause of Stacks 0DS4, for every 1-morphism.** Let `f : 𝒯 ⟶ 𝒳` be a
> 1-morphism locally of finite type of Jacobson, pseudo-catenary, locally Noetherian algebraic
> stacks over `S`, with `|𝒯|` irreducible and `𝒳` quasi-separated, and let `P` cut out the scheme
> theoretic image `𝒵` of `f` (Stacks 0CMI). Then `dim(𝒯) ≤ dim(𝒵) + dim_t(𝒯_{f(t)})` for every
> `t ∈ |𝒯|`, i.e. `dim_t(𝒯_{f(t)}) ≥ dim(𝒯) - dim(𝒵)`.
>
> No quasi-compactness of `f` is asked. A nonempty quasi-compact open substack `𝒰` of `𝒯` exists by
> `AlgebraicGeometry.Stack.exists_isOpenImmersion_isQuasiCompactStack_nonempty` (through
> Stacks 05UP); the restriction of `f` to it is quasi-compact by Stacks 075S, part (1), the target
> being quasi-separated; and
> `dimension_le_closedSubstackDimension_add_relativeStackDimensionAt_of_quasiCompactRestriction`
> concludes.

```lean
theorem forall_dimension_le_closedSubstackDimension_add_relativeStackDimensionAt
    {𝒯 𝒳 : AlgebraicStacks.{u, w} B S hS} (f : 𝒯 ⟶ 𝒳)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (h𝒯 : IsLocallyNoetherianStack.{u, w} B S hS 𝒯)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (h𝒯Jacobson : AlgebraicStacks.IsJacobson B S hS 𝒯)
    (h𝒳Jacobson : AlgebraicStacks.IsJacobson B S hS 𝒳)
    (h𝒯Catenary : AlgebraicStacks.IsPseudoCatenary B S hS 𝒯)
    (h𝒳Catenary : AlgebraicStacks.IsPseudoCatenary B S hS 𝒳)
    (h𝒯Irreducible : @IrreducibleSpace _ (pointTopology B S hS 𝒯.val))
    (h𝒳QuasiSeparated : IsQuasiSeparatedAbs.{u, w, w} B S hS 𝒳)
    {P : ObjectProperty 𝒳.val.val.obj} (hP : IsSchemeTheoreticImage f P) :
    ∀ t : points B S hS 𝒯.val.val 𝒯.val.property,
      dimension B S hS 𝒯 h𝒯 ≤
        closedSubstackDimension B S hS 𝒳 P hP.1 hP.isAlgebraicStack h𝒳 +
          relativeStackDimensionAt.{u, w} B S hS f hf h𝒯 h𝒳 t
```

## Tag 0DS5, a remark

[Tag 0DS5](https://stacks.math.columbia.edu/tag/0DS5) in the Stacks Project.

**`AlgebraicGeometry.Stack.classifyingStack_multiplicativeGroup_dimension_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ClassifyingStackMultiplicativeGroupExample.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ClassifyingStackMultiplicativeGroupExample.lean#L307). The attribute's comment: “the example [Spec k/G\_m] → Spec k: it need not be that dim T ≥ dim Z, the fibres having negative dimension”.

> **Stacks 0DS5**, the example `[Spec k/𝐆_m] ⟶ Spec k`. Let `k` be a field. The classifying
> stack `[Spec k/𝐆_m]` is an algebraic stack, of which a model `𝒬` in the 2-category of algebraic
> stacks over `Spec k` exists; and for every such model, the structure morphism `f : 𝒬 ⟶ Spec k`
> satisfies the hypotheses of Stacks 0DS4 — it is quasi-compact and locally of finite type, `𝒬` and
> `Spec k` are Jacobson, pseudo-catenary and locally Noetherian, `|𝒬|` is irreducible and `Spec k` is
> quasi-separated — its scheme theoretic image is all of `Spec k`, of dimension `0`, while
> `dim 𝒬 = -1`, so that `dim 𝒬 < dim 𝒵`; and the fibre dimension `dim_t(𝒬_{f(t)})` of Stacks 0DRL is
> `-1 < 0` at every point `t` of `𝒬`.

```lean
theorem classifyingStack_multiplicativeGroup_dimension_lt :
    IsAlgebraicStack.{u, w} C (Spec (.of k)) hk
        (classifyingStack C hk (multiplicativeGroupOverField C hk)).val ∧
      (∃ 𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk, Nonempty
        (StacksRepresentableCFG.EquivalenceOver
          (classifyingStack C hk (multiplicativeGroupOverField C hk)).val.p 𝒬.val.val.p)) ∧
      ∀ (𝒬 : AlgebraicStacks.{u, w} C (Spec (.of k)) hk)
        (_e : StacksRepresentableCFG.EquivalenceOver
          (classifyingStack C hk (multiplicativeGroupOverField C hk)).val.p 𝒬.val.val.p),
        ∃ (h𝒯 : IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk 𝒬)
          (h𝒳 : IsLocallyNoetherianStack.{u, w} C (Spec (.of k)) hk (specFieldStack.{u, w} C hk))
          (hf : AlgebraicStacks.IsLocallyOfFiniteType C (Spec (.of k)) hk (toSpecFieldStack C hk 𝒬))
          (hP : IsSchemeTheoreticImage (toSpecFieldStack C hk 𝒬) ⊤),
          IsQuasiCompactMorphism C (Spec (.of k)) hk (toSpecFieldStack C hk 𝒬) ∧
          AlgebraicStacks.IsJacobson C (Spec (.of k)) hk 𝒬 ∧
          AlgebraicStacks.IsJacobson C (Spec (.of k)) hk (specFieldStack.{u, w} C hk) ∧
          AlgebraicStacks.IsPseudoCatenary C (Spec (.of k)) hk 𝒬 ∧
          AlgebraicStacks.IsPseudoCatenary C (Spec (.of k)) hk (specFieldStack.{u, w} C hk) ∧
          @IrreducibleSpace _ (pointTopology C (Spec (.of k)) hk 𝒬.val) ∧
          IsQuasiSeparatedAbs.{u, w, w} C (Spec (.of k)) hk (specFieldStack.{u, w} C hk) ∧
          closedSubstackDimension C (Spec (.of k)) hk (specFieldStack.{u, w} C hk) ⊤ hP.1
            hP.isAlgebraicStack h𝒳 = 0 ∧
          dimension C (Spec (.of k)) hk 𝒬 h𝒯 = ((-1 : ℤ) : EInt) ∧
          dimension C (Spec (.of k)) hk 𝒬 h𝒯 <
            closedSubstackDimension C (Spec (.of k)) hk (specFieldStack.{u, w} C hk) ⊤ hP.1
              hP.isAlgebraicStack h𝒳 ∧
          ∀ t : points C (Spec (.of k)) hk 𝒬.val.val 𝒬.val.property,
            relativeStackDimensionAt.{u, w} C (Spec (.of k)) hk (toSpecFieldStack C hk 𝒬) hf h𝒯
                h𝒳 t =
              ((-1 : ℤ) : EInt)
```

**`AlgebraicGeometry.Stack.isQuasiDMAbs_and_zero_le_dimensionAtPoint_fieldFibreStackSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiDMFibreDimension.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiDMFibreDimension.lean#L70). The attribute's comment: “the fibres of a quasi-DM 1-morphism are quasi-DM algebraic stacks, hence of non-negative dimension”.

> Let `f : 𝒯 ⟶ 𝒳` be a quasi-DM 1-morphism of algebraic stacks over `S`, locally of finite type,
> and let `p` be a field-valued point of `𝒳` with field spectrum `Spec k`. Then the fibre
> `𝒯 ×_𝒳 Spec k` of `f` over `p` is a quasi-DM algebraic stack (Stacks 050D, part (6)), and hence has
> non-negative dimension at every one of its points; so, when it is nonempty, its dimension of Stacks
> 0AFP is non-negative.

```lean
theorem isQuasiDMAbs_and_zero_le_dimensionAtPoint_fieldFibreStackSquare
    {𝒯 𝒳 : AlgebraicStacks.{u, w} B S hS} (f : 𝒯 ⟶ 𝒳)
    (hqdm : AlgebraicStacks.IsQuasiDM B S hS f)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (p : FieldValuedPoint B S hS 𝒳.val.val) :
    IsQuasiDMAbs.{u, w, w} B S hS (fieldFibreStackSquare B S hS f p).pt ∧
      (∀ x : points B S hS (fieldFibreStackSquare B S hS f p).pt.val.val
          (fieldFibreStackSquare B S hS f p).pt.val.property,
        0 ≤ dimensionAtPoint B S hS (fieldFibreStackSquare B S hS f p).pt
          (isLocallyNoetherianStack_fieldFibreStackSquare.{u, w} B S hS f hf p) x) ∧
      (Nonempty (points B S hS (fieldFibreStackSquare B S hS f p).pt.val.val
          (fieldFibreStackSquare B S hS f p).pt.val.property) →
        0 ≤ dimension B S hS (fieldFibreStackSquare B S hS f p).pt
          (isLocallyNoetherianStack_fieldFibreStackSquare.{u, w} B S hS f hf p))
```

**`AlgebraicGeometry.Stack.zero_le_relativeStackDimensionAt_and_closedSubstackDimension_le_dimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiDMFibreDimension.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiDMFibreDimension.lean#L96). The attribute's comment: “in the quasi-DM case the lemma implies dim T ≥ dim Z”.

> Let `f : 𝒯 ⟶ 𝒳` be a quasi-compact, locally of finite type 1-morphism of Jacobson,
> pseudo-catenary, locally Noetherian algebraic stacks over `S`, whose source is irreducible and
> whose target is quasi-separated, and let `𝒵 ↪ 𝒳`, cut out by `P`, be the scheme theoretic image of
> `f` — the situation of Stacks 0DS4. If `f` is moreover quasi-DM, then its fibres have non-negative
> dimension, `dim_t(𝒯_{f(t)}) ≥ 0` at every `t ∈ |𝒯|`, and Stacks 0DS4 then gives `dim 𝒵 ≤ dim 𝒯`.

```lean
theorem zero_le_relativeStackDimensionAt_and_closedSubstackDimension_le_dimension
    {𝒯 𝒳 : AlgebraicStacks.{u, w} B S hS} (f : 𝒯 ⟶ 𝒳)
    (hfQC : IsQuasiCompactMorphism B S hS f)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (hDM : AlgebraicStacks.IsQuasiDM B S hS f)
    (h𝒯 : IsLocallyNoetherianStack.{u, w} B S hS 𝒯)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (h𝒯Jacobson : AlgebraicStacks.IsJacobson B S hS 𝒯)
    (h𝒳Jacobson : AlgebraicStacks.IsJacobson B S hS 𝒳)
    (h𝒯Catenary : AlgebraicStacks.IsPseudoCatenary B S hS 𝒯)
    (h𝒳Catenary : AlgebraicStacks.IsPseudoCatenary B S hS 𝒳)
    (h𝒯Irreducible : @IrreducibleSpace _ (pointTopology B S hS 𝒯.val))
    (h𝒳QuasiSeparated : IsQuasiSeparatedAbs.{u, w, w} B S hS 𝒳)
    {P : ObjectProperty 𝒳.val.val.obj} (hP : IsSchemeTheoreticImage f P) :
    (∀ t : points B S hS 𝒯.val.val 𝒯.val.property,
        0 ≤ relativeStackDimensionAt B S hS f hf h𝒯 h𝒳 t) ∧
      closedSubstackDimension B S hS 𝒳 P hP.1 hP.isAlgebraicStack h𝒳 ≤
        dimension B S hS 𝒯 h𝒯
```

## Tag 0DS6, a lemma

[Tag 0DS6](https://stacks.math.columbia.edu/tag/0DS6) in the Stacks Project.

**`AlgebraicGeometry.Stack.closedSubstackDimension_le_dimension_of_isQuasiCompactMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DimensionSchemeTheoreticImage.lean, line 1206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DimensionSchemeTheoreticImage.lean#L1206). The attribute's comment: “the first clause, dim Z ≤ dim T, under exactly the hypotheses of the source”. References: EGA IV (4.1.2), “(i)”.

> **The inequality of Stacks 0DS6.** For a quasi-compact, locally of finite type, quasi-DM
> 1-morphism `f : 𝒯 ⟶ 𝒳` of Jacobson, pseudo-catenary, locally Noetherian algebraic stacks over
> `S`, with `|𝒯|` irreducible and `𝒳` quasi-separated, and `P` cutting out the scheme theoretic
> image `𝒵` of `f`, one has `dim(𝒵) ≤ dim(𝒯)`.
>
> At a point of the nonempty open subset of `|𝒯|` on which
> `dim(𝒯) = dim(𝒵) + dim_t(𝒯_{f(t)})` (Stacks 0DS4 for a quasi-compact `f`), the fibre dimension
> is non-negative because `f` is quasi-DM.

```lean
theorem closedSubstackDimension_le_dimension_of_isQuasiCompactMorphism
    {𝒯 𝒳 : AlgebraicStacks.{u, w} B S hS} (f : 𝒯 ⟶ 𝒳)
    (hfQC : IsQuasiCompactMorphism B S hS f)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (hDM : AlgebraicStacks.IsQuasiDM B S hS f)
    (h𝒯 : IsLocallyNoetherianStack.{u, w} B S hS 𝒯)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (h𝒯Jacobson : AlgebraicStacks.IsJacobson B S hS 𝒯)
    (h𝒳Jacobson : AlgebraicStacks.IsJacobson B S hS 𝒳)
    (h𝒯Catenary : AlgebraicStacks.IsPseudoCatenary B S hS 𝒯)
    (h𝒳Catenary : AlgebraicStacks.IsPseudoCatenary B S hS 𝒳)
    (h𝒯Irreducible : @IrreducibleSpace _ (pointTopology B S hS 𝒯.val))
    (h𝒳QuasiSeparated : IsQuasiSeparatedAbs.{u, w, w} B S hS 𝒳)
    {P : ObjectProperty 𝒳.val.val.obj} (hP : IsSchemeTheoreticImage f P) :
    closedSubstackDimension B S hS 𝒳 P hP.1 hP.isAlgebraicStack h𝒳 ≤ dimension B S hS 𝒯 h𝒯
```

**`AlgebraicGeometry.Stack.closedSubstackDimension_le_dimension_and_xor_relativeDimension_pos_of_ne_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DimensionSchemeTheoreticImage.lean, line 1330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DimensionSchemeTheoreticImage.lean#L1330). The attribute's comment: “the exactly-one form under the added hypothesis that dim T is finite; erratum: false as written when dim T = dim Z = infinity, machine-checked as AlgebraicGeometry.Stack.not\_forall\_xor\_relativeDimension\_pos (the affine line over N`<`X>, N Nagata's ring; Fujita 1975, Brewer-Heinzer 1980), see the docstring”.

> **Stacks 0DS6**, for `𝒯` of finite dimension. Let `f : 𝒯 ⟶ 𝒳` be a quasi-compact, locally of
> finite type 1-morphism of Jacobson, pseudo-catenary, locally Noetherian algebraic stacks over `S`
> which is quasi-DM, whose source is irreducible and whose target is quasi-separated, and let
> `𝒵 ↪ 𝒳`, cut out by `P`, be the scheme theoretic image of `f`. Suppose `dim(𝒯) ≠ ∞`. Then
> `dim(𝒵) ≤ dim(𝒯)`, and exactly one of the following holds: (1) `dim_t(𝒯_{f(t)}) > 0` at every
> finite type point `t ∈ |𝒯|`, in which case `dim(𝒵) < dim(𝒯)`; or (2) `dim(𝒯) = dim(𝒵)`.
>
> **Erratum.** The source states the lemma without the hypothesis `dim(𝒯) ≠ ∞`, and as written
> it is false when `dim(𝒯) = dim(𝒵) = ∞`. Let `N` be Nagata's Noetherian ring of infinite dimension
> (Stacks, Examples, Tag 02JC), let `D = N⟨X⟩` be the localization of `N[X]` at the monic
> polynomials, and let `f : 𝔸¹_D ⟶ Spec D` be the projection.
> * Every hypothesis holds. `N` is regular, its local rings being localizations of polynomial rings,
>   so `D` is a Noetherian regular domain, hence Cohen–Macaulay and universally catenary
>   (Stacks 00NM), and `D[s]` is as well. `D` is Jacobson by J. W. Brewer and W. J. Heinzer,
>   *R Noetherian implies R⟨X⟩ is a Hilbert ring*, J. Algebra 67 (1980) 204–209,
>   doi:10.1016/0021-8693(80)90317-8; so is `D[s]`, being of finite type over `D`. `𝔸¹_D` is
>   irreducible, `f` is affine, hence quasi-compact and representable, hence quasi-DM, and of finite
>   type, and `Spec D` is affine, hence quasi-separated.
> * Both alternatives hold. `f` is faithfully flat, so its scheme theoretic image is `Spec D`. Every
>   fibre is an affine line over a field, so `dim_t(𝒯_{f(t)}) = 1 > 0` everywhere. The primes
>   `p_i N[X]` contain no monic polynomial and have unbounded height, so
>   `dim(𝒯) = dim(𝒵) = ∞`. Thus (1) and (2) hold together, and (1) does not force
>   `dim(𝒵) < dim(𝒯)`.
>
> This counterexample is machine-checked:
> `AlgebraicGeometry.Stack.not_forall_xor_relativeDimension_pos`, in
> `StacksFrontier/AlgebraicGeometry/Stacks/DimensionSchemeTheoreticImageCounterexample0DS6.lean`,
> proves that the statement below without `h𝒯Finite` is false, every hypothesis of the source
> (quasi-compactness of `f` included) being proved for this `f`.
>
> Infinite-dimensional Noetherian Hilbert domains were first constructed by K. Fujita, *Infinite
> dimensional Noetherian Hilbert domains*, Hiroshima Math. J. 5 (1975) 181–185,
> doi:10.32917/hmj/1206136627. The source's arithmetic presupposes finiteness: Stacks 0DS4, from
> which it derives this lemma, is stated as `dim_t(𝒯_{f(t)}) ≥ dim 𝒯 - dim 𝒵`, and the proof as
> `dim_t(𝒯_{f(t)}) = dim_t 𝒯 - dim_{f(t)} 𝒵`, differences that are undefined when both dimensions
> are infinite; Stacks 0DRT, on which Stacks 0DRX rests, assumes finite dimension explicitly. With
> no finiteness hypothesis, what holds is
> `AlgebraicGeometry.Stack.closedSubstackDimension_le_dimension_and_xor_relativeDimension_pos`:
> `dim(𝒵) ≤ dim(𝒯)` and `Xor ((1) ∧ dim(𝒵) < dim(𝒯)) (2)`.
>
> The proof: Stacks 0DS4 for a quasi-compact `f` gives `dim(𝒯) ≤ dim(𝒵) + dim_t(𝒯_{f(t)})` at
> every point, with equality on a nonempty open subset `W` of `|𝒯|`; the fibre dimensions are
> non-negative integers because `f` is quasi-DM. The open `W` contains a finite type point `t`,
> `𝒯` being Jacobson (`AlgebraicGeometry.Stack.exists_isFiniteTypePoint_mem_of_isOpen`). Under (1)
> the fibre dimension at `t` is a positive integer, so `dim(𝒵) < dim(𝒯)` because `dim(𝒯)` is finite
> — it is neither `∞`, by hypothesis, nor `-∞`, by
> `AlgebraicGeometry.Stack.dimensionAtPoint_ne_bot`; hence (1) excludes (2). If (2) fails, then
> (1) holds by
> `AlgebraicGeometry.Stack.closedSubstackDimension_le_dimension_and_xor_relativeDimension_pos`.

```lean
theorem closedSubstackDimension_le_dimension_and_xor_relativeDimension_pos_of_ne_top
    {𝒯 𝒳 : AlgebraicStacks.{u, w} B S hS} (f : 𝒯 ⟶ 𝒳)
    (hfQC : IsQuasiCompactMorphism B S hS f)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (hDM : AlgebraicStacks.IsQuasiDM B S hS f)
    (h𝒯 : IsLocallyNoetherianStack.{u, w} B S hS 𝒯)
    (h𝒳 : IsLocallyNoetherianStack.{u, w} B S hS 𝒳)
    (h𝒯Jacobson : AlgebraicStacks.IsJacobson B S hS 𝒯)
    (h𝒳Jacobson : AlgebraicStacks.IsJacobson B S hS 𝒳)
    (h𝒯Catenary : AlgebraicStacks.IsPseudoCatenary B S hS 𝒯)
    (h𝒳Catenary : AlgebraicStacks.IsPseudoCatenary B S hS 𝒳)
    (h𝒯Irreducible : @IrreducibleSpace _ (pointTopology B S hS 𝒯.val))
    (h𝒳QuasiSeparated : IsQuasiSeparatedAbs.{u, w, w} B S hS 𝒳)
    {P : ObjectProperty 𝒳.val.val.obj} (hP : IsSchemeTheoreticImage f P)
    (h𝒯Finite : dimension B S hS 𝒯 h𝒯 ≠ ⊤) :
    closedSubstackDimension B S hS 𝒳 P hP.1 hP.isAlgebraicStack h𝒳 ≤ dimension B S hS 𝒯 h𝒯 ∧
      Xor (∀ t, IsFiniteTypePoint.{u, w} B S hS 𝒯 t →
            0 < relativeStackDimensionAt B S hS f hf h𝒯 h𝒳 t)
        (dimension B S hS 𝒯 h𝒯 =
          closedSubstackDimension B S hS 𝒳 P hP.1 hP.isAlgebraicStack h𝒳) ∧
      ((∀ t, IsFiniteTypePoint.{u, w} B S hS 𝒯 t →
            0 < relativeStackDimensionAt B S hS f hf h𝒯 h𝒳 t) →
        closedSubstackDimension B S hS 𝒳 P hP.1 hP.isAlgebraicStack h𝒳 <
          dimension B S hS 𝒯 h𝒯)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 107.5, Tag 0DRE](https://stacks.math.columbia.edu/tag/0DRE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
