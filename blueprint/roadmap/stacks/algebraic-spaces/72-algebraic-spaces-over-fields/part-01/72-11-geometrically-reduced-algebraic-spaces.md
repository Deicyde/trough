---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsGeometricallyReducedAt, AlgebraicGeometry.Space.IsGeometricallyReduced, AlgebraicGeometry.Space.isGeometricallyReducedAt_iff_exists_etaleChart, AlgebraicGeometry.Space.isGeometricallyReducedAt_iff_forall_etaleChart, AlgebraicGeometry.Space.isGeometricallyReduced_iff_exists_surjective_etaleChart, AlgebraicGeometry.Space.isGeometricallyReduced_iff_forall_etaleChart, AlgebraicGeometry.Space.isGeometricallyReduced_of_isReduced, AlgebraicGeometry.Space.isGeometricallyReducedAt_of_isReduced_etaleLocalRing
statement: formalized
proof: formalized
---

# 72.11 Geometrically reduced algebraic spaces

Section 72.11 of the Stacks Project, [Tag 0DMP](https://stacks.math.columbia.edu/tag/0DMP). 7 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DMQ, a definition

[Tag 0DMQ](https://stacks.math.columbia.edu/tag/0DMQ) in the Stacks Project.

**`AlgebraicGeometry.Space.IsGeometricallyReducedAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReduced.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReduced.lean#L204). The attribute's comment: “part (1): at a point”.

> **Stacks 0DMQ, part (1).** An algebraic space `X` over a field `k` is *geometrically
> reduced at* a point `x` of `X` when the étale local ring of `X` at every geometric point
> above `x` is geometrically reduced as a `k`-algebra.

```lean
abbrev IsGeometricallyReducedAt (k : Type u) [Field k] (B : BigFppfSite.{u})
    (hk : B.Contains (Spec (.of k)))
    (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (x : points B (Spec (.of k)) hk X) : Prop
```

**`AlgebraicGeometry.Space.IsGeometricallyReduced`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReduced.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReduced.lean#L217). The attribute's comment: “part (2): over the field”.

> **Stacks 0DMQ, part (2).** An algebraic space over a field `k` is *geometrically
> reduced* when it is geometrically reduced at every one of its points.

```lean
abbrev IsGeometricallyReduced (k : Type u) [Field k] (B : BigFppfSite.{u})
    (hk : B.Contains (Spec (.of k)))
    (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X) : Prop
```

## Tag 0DMR, a lemma

[Tag 0DMR](https://stacks.math.columbia.edu/tag/0DMR) in the Stacks Project.

**`AlgebraicGeometry.Space.isGeometricallyReducedAt_iff_exists_etaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReduced.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReduced.lean#L510). The attribute's comment: “conditions (1) and (2): some étale neighbourhood”.

> **Stacks 0DMR, conditions (1) and (2).** An algebraic space over a field `k` is
> geometrically reduced at a point `x` exactly when *some* étale neighbourhood `(U, u) → (X, x)`
> with `U` a scheme is geometrically reduced at `u`.

```lean
theorem isGeometricallyReducedAt_iff_exists_etaleChart
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X) (x : points B (Spec (.of k)) hk X) :
    IsGeometricallyReducedAt k B hk X hX x ↔
      ∃ (U : BigFppfOver B (Spec (.of k)) hk) (a : yoneda.obj U ⟶ X),
        IsEtale B (Spec (.of k)) hk a ∧
          ∃ p : FieldValuedPoint B (Spec (.of k)) hk (yoneda.obj U),
            pointsMap B (Spec (.of k)) hk (yoneda.obj U) a
                (p.class B (Spec (.of k)) hk (yoneda.obj U)) = x ∧
              _root_.AlgebraicGeometry.IsGeometricallyReducedAt (B.inclusion.map U.hom)
                (schemePoint B (Spec (.of k)) hk U p)
```

**`AlgebraicGeometry.Space.isGeometricallyReducedAt_iff_forall_etaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReduced.lean, line 533](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReduced.lean#L533). The attribute's comment: “conditions (1) and (3): every étale neighbourhood”.

> **Stacks 0DMR, conditions (1) and (3).** An algebraic space over a field `k` is
> geometrically reduced at a point `x` exactly when *every* étale neighbourhood `(U, u) → (X, x)`
> with `U` a scheme is geometrically reduced at `u`.

```lean
theorem isGeometricallyReducedAt_iff_forall_etaleChart
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X) (x : points B (Spec (.of k)) hk X) :
    IsGeometricallyReducedAt k B hk X hX x ↔
      ∀ (U : BigFppfOver B (Spec (.of k)) hk) (a : yoneda.obj U ⟶ X),
        IsEtale B (Spec (.of k)) hk a →
          ∀ p : FieldValuedPoint B (Spec (.of k)) hk (yoneda.obj U),
            pointsMap B (Spec (.of k)) hk (yoneda.obj U) a
                (p.class B (Spec (.of k)) hk (yoneda.obj U)) = x →
              _root_.AlgebraicGeometry.IsGeometricallyReducedAt (B.inclusion.map U.hom)
                (schemePoint B (Spec (.of k)) hk U p)
```

## Tag 0DMS, a lemma

[Tag 0DMS](https://stacks.math.columbia.edu/tag/0DMS) in the Stacks Project.

**`AlgebraicGeometry.Space.isGeometricallyReduced_iff_exists_surjective_etaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReduced.lean, line 579](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReduced.lean#L579). The attribute's comment: “conditions (1) and (2): some surjective étale chart”.

> **Stacks 0DMS, conditions (1) and (2).** An algebraic space over a field `k` is
> geometrically reduced exactly when *some* surjective étale morphism `U → X` with `U` a scheme
> has `U` geometrically reduced over `k`.

```lean
theorem isGeometricallyReduced_iff_exists_surjective_etaleChart
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X) :
    IsGeometricallyReduced k B hk X hX ↔
      ∃ (U : BigFppfOver B (Spec (.of k)) hk) (a : yoneda.obj U ⟶ X),
        IsSurjective B (Spec (.of k)) hk a ∧ IsEtale B (Spec (.of k)) hk a ∧
          _root_.AlgebraicGeometry.GeometricallyReduced (B.inclusion.map U.hom)
```

**`AlgebraicGeometry.Space.isGeometricallyReduced_iff_forall_etaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReduced.lean, line 600](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReduced.lean#L600). The attribute's comment: “conditions (1) and (3): every étale chart”.

> **Stacks 0DMS, conditions (1) and (3).** An algebraic space over a field `k` is
> geometrically reduced exactly when *every* étale morphism `U → X` with `U` a scheme has `U`
> geometrically reduced over `k`.

```lean
theorem isGeometricallyReduced_iff_forall_etaleChart
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X) :
    IsGeometricallyReduced k B hk X hX ↔
      ∀ (U : BigFppfOver B (Spec (.of k)) hk) (a : yoneda.obj U ⟶ X),
        IsEtale B (Spec (.of k)) hk a →
          _root_.AlgebraicGeometry.GeometricallyReduced (B.inclusion.map U.hom)
```

## Tag 0E02, a lemma

[Tag 0E02](https://stacks.math.columbia.edu/tag/0E02) in the Stacks Project.

**`AlgebraicGeometry.Space.isGeometricallyReduced_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReducedFieldExtension.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReducedFieldExtension.lean#L435). The attribute's comment: “part (2)”.

> **Stacks 0E02, part (2).** Over a perfect field a reduced algebraic space is geometrically
> reduced: by Stacks 0DMS it suffices that every étale scheme chart is geometrically reduced,
> which over a perfect field is Stacks 020I.

```lean
theorem isGeometricallyReduced_of_isReduced [PerfectField k]
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (hred : HasEtaleLocalProperty B (Spec (.of k)) hk X (fun Y : Scheme.{u} => IsReduced Y)) :
    IsGeometricallyReduced k B hk X hX
```

**`AlgebraicGeometry.Space.isGeometricallyReducedAt_of_isReduced_etaleLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReducedPerfectField.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReducedPerfectField.lean#L112). The attribute's comment: “part (1)”.

> **Stacks 0E02, part (1).** Let `X` be an algebraic space over a perfect field `k`, for
> example a field of characteristic zero. If the étale local ring `𝒪_{X, x̄}` at a geometric
> point `x̄` above `x` is reduced, then `X` is geometrically reduced at `x`.

```lean
theorem isGeometricallyReducedAt_of_isReduced_etaleLocalRing
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (x : points B (Spec (.of k)) hk X)
    (xbar : GeometricPoint B (Spec (.of k)) hk X) (hxbar : xbar.LiesOver x)
    (hred : _root_.IsReduced (etaleLocalRing B (Spec (.of k)) hk X xbar)) :
    IsGeometricallyReducedAt k B hk X hX x
```

## Tag 0E03, a lemma

[Tag 0E03](https://stacks.math.columbia.edu/tag/0E03) in the Stacks Project.

**`AlgebraicGeometry.Space.isGeometricallyReduced_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReducedFieldExtension.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReducedFieldExtension.lean#L83).

> **Stacks 0E03.** Let `k` be a field of exponential characteristic `p` and let `X` be an
> algebraic space over `k`. Then `X` is geometrically reduced over `k` if and only if `X_{k'}`
> is reduced for every field extension `k'/k`, if and only if `X_{k'}` is reduced for every
> finite purely inseparable extension `k'/k`, if and only if each of `X_{k^{1/p}}`,
> `X_{k^{perf}}` and `X_{k̄}` is reduced.

```lean
theorem isGeometricallyReduced_tfae (k : Type u) [Field k] (p : ℕ) [ExpChar k p]
    (B : BigFppfSite.{u}) (hk : B.Contains (Spec (.of k)))
    (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (kperf : Type u) [Field kperf] [Algebra k kperf] [ExpChar kperf p] [PerfectRing kperf p]
    [IsPerfectClosure (algebraMap k kperf) p]
    (kbar : Type u) [Field kbar] [Algebra k kbar] [IsAlgClosure k kbar] :
    let isReducedBaseChange := fun (k' : Type u) [Field k'] [Algebra k k'] ↦
      ∀ (U : BigFppfOver B (Spec (.of k)) hk) (a : yoneda.obj U ⟶ X),
        IsEtale B (Spec (.of k)) hk a →
          IsReduced (pullback (B.inclusion.map U.hom)
            (Spec.map (CommRingCat.ofHom (algebraMap k k'))))
    List.TFAE
      [ IsGeometricallyReduced k B hk X hX,
        ∀ (k' : Type u) [Field k'] [Algebra k k'], isReducedBaseChange k',
        ∀ (k' : Type u) [Field k'] [Algebra k k'] [FiniteDimensional k k']
          [IsPurelyInseparable k k'], isReducedBaseChange k',
        isReducedBaseChange (AdjoinPthRoots k),
        isReducedBaseChange kperf,
        isReducedBaseChange kbar ]
```

## Tag 0E04, a lemma

[Tag 0E04](https://stacks.math.columbia.edu/tag/0E04) in the Stacks Project.

**`AlgebraicGeometry.Space.isGeometricallyReducedAt_relocalizeRestrict_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReducedFieldExtension.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReducedFieldExtension.lean#L342). The attribute's comment: “pointwise equivalence”.

> **Stacks 0E04, pointwise statement.** An algebraic space over a field `k` is geometrically
> reduced at a point `x` exactly when its base change to a field extension `k'/k` is
> geometrically reduced at any point `x'` lying over `x`.

```lean
theorem isGeometricallyReducedAt_relocalizeRestrict_iff
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (x : points B (Spec (.of k)) hk X)
    (x' : points B (Spec (.of k')) hk'
      ((OverShriek.relocalizeRestrict (fieldExtensionMap B k k' hk hk')).obj X))
    (hx : pointsOfRelocalizeRestrict B (Spec (.of k')) (Spec (.of k)) hk' hk
      (fieldExtensionMap B k k' hk hk') X x' = x) :
    IsGeometricallyReducedAt k B hk X hX x ↔
      IsGeometricallyReducedAt k' B hk'
        ((OverShriek.relocalizeRestrict (fieldExtensionMap B k k' hk hk')).obj X)
        (isAlgebraicSpace_relocalizeRestrict B (Spec (.of k')) (Spec (.of k)) hk' hk
          (fieldExtensionMap B k k' hk hk') X hX) x'
```

**`AlgebraicGeometry.Space.isGeometricallyReduced_relocalizeRestrict_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReducedFieldExtension.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReducedFieldExtension.lean#L388). The attribute's comment: “global equivalence”.

> **Stacks 0E04, global statement.** An algebraic space over a field `k` is geometrically
> reduced over `k` exactly when its base change to a field extension `k'/k` is geometrically
> reduced over `k'`.

```lean
theorem isGeometricallyReduced_relocalizeRestrict_iff
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X) :
    IsGeometricallyReduced k B hk X hX ↔
      IsGeometricallyReduced k' B hk'
        ((OverShriek.relocalizeRestrict (fieldExtensionMap B k k' hk hk')).obj X)
        (isAlgebraicSpace_relocalizeRestrict B (Spec (.of k')) (Spec (.of k)) hk' hk
          (fieldExtensionMap B k k' hk hk') X hX)
```

## Tag 0E05, a lemma

[Tag 0E05](https://stacks.math.columbia.edu/tag/0E05) in the Stacks Project.

**`AlgebraicGeometry.Space.isGeometricallyReducedAt_iff_of_isEtaleAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReducedEtaleLocal.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReducedEtaleLocal.lean#L93). The attribute's comment: “part (1)”.

> **Stacks 0E05, part (1).** Let `f : X ⟶ Y` be a morphism of algebraic spaces over a field
> `k` and let `x` be a point of `X` with image `y`. If `f` is étale at `x`, then `X` is
> geometrically reduced at `x` if and only if `Y` is geometrically reduced at `y`.

```lean
theorem isGeometricallyReducedAt_iff_of_isEtaleAt
    {X Y : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (hY : IsAlgebraicSpace B (Spec (.of k)) hk Y)
    (f : X ⟶ Y) (x : points B (Spec (.of k)) hk X)
    (hf : IsEtaleAt B (Spec (.of k)) hk f x) :
    IsGeometricallyReducedAt k B hk X hX x ↔
      IsGeometricallyReducedAt k B hk Y hY (pointsMap B (Spec (.of k)) hk X f x)
```

**`AlgebraicGeometry.Space.isGeometricallyReduced_iff_of_surjective_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReducedEtaleLocal.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyReducedEtaleLocal.lean#L112). The attribute's comment: “part (2)”.

> **Stacks 0E05, part (2).** Let `f : X ⟶ Y` be a surjective étale morphism of algebraic
> spaces over a field `k`. Then `X` is geometrically reduced if and only if `Y` is.

```lean
theorem isGeometricallyReduced_iff_of_surjective_isEtale
    {X Y : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (hY : IsAlgebraicSpace B (Spec (.of k)) hk Y)
    (f : X ⟶ Y) (hf : IsEtale B (Spec (.of k)) hk f)
    (hs : IsSurjective B (Spec (.of k)) hk f) :
    IsGeometricallyReduced k B hk X hX ↔ IsGeometricallyReduced k B hk Y hY
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 72.11, Tag 0DMP](https://stacks.math.columbia.edu/tag/0DMP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
