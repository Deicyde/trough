---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsGeometricallyReducedOver, AlgebraicGeometry.isGeometricallyReducedAt_iff_isGeometricallyReduced_stalk, AlgebraicGeometry.isGeometricallyReducedAt_of_isReduced, AlgebraicGeometry.geometricallyReduced_of_isReduced, AlgebraicGeometry.geometricallyReduced_tfae, AlgebraicGeometry.isGeometricallyReducedAt_tfae, AlgebraicGeometry.isGeometricallyReducedAt_iff_baseChange_fieldExtension, AlgebraicGeometry.geometricallyReduced_iff_baseChange_fieldExtension
statement: formalized
proof: formalized
---

# 33.6 Geometrically reduced schemes

Section 33.6 of the Stacks Project, [Tag 035U](https://stacks.math.columbia.edu/tag/035U). 11 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 035V, a definition

[Tag 035V](https://stacks.math.columbia.edu/tag/035V) in the Stacks Project.

**`AlgebraicGeometry.IsGeometricallyReducedOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Reduced.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Reduced.lean#L107).

> **[Stacks, Tag 035V].** Let `k` be a field and let `X` be a scheme over `k`, given by its
> structure morphism `f : X ⟶ Spec k`.
>
> 1. `X` is *geometrically reduced at* a point `x ∈ X` if for any field extension `k'/k` and any
>    point `x'` of `X_{k'}` lying over `x` the local ring `𝒪_{X_{k'}, x'}` is reduced. That
>    pointwise condition is `AlgebraicGeometry.IsGeometricallyReducedAt f x`, the body of this
>    definition under its quantifier: the base change `X_{k'}` is the pullback of `f` along
>    `Spec k' ⟶ Spec k`, and `x'` lies over `x` when the first projection sends it to `x`.
> 2. `X` is *geometrically reduced over `k`* if it is geometrically reduced at every point of
>    `X`, which is exactly what this definition says.
>
> Mathlib's `AlgebraicGeometry.GeometricallyReduced` is the notion of part (2) for an arbitrary
> base, defined by reducedness of every field-valued base change rather than pointwise; over a
> field the two agree by
> `AlgebraicGeometry.geometricallyReduced_iff_forall_isGeometricallyReducedAt`, so the results
> stated for it — such as `AlgebraicGeometry.geometricallyReduced_of_isReduced` over a perfect
> field — apply to this predicate as well.

```lean
public abbrev IsGeometricallyReducedOver {k : Type u} [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) : Prop
```

## Tag 035W, a lemma

[Tag 035W](https://stacks.math.columbia.edu/tag/035W) in the Stacks Project.

**`AlgebraicGeometry.isGeometricallyReducedAt_iff_isGeometricallyReduced_stalk`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Reduced.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Reduced.lean#L255).

> A scheme over a field is geometrically reduced at a point if and only if its local ring at
> that point is geometrically reduced over the field.

```lean
public lemma isGeometricallyReducedAt_iff_isGeometricallyReduced_stalk
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) (x : X) :
    IsGeometricallyReducedAt f x ↔
      let : Algebra k (X.presheaf.stalk x) :=
        let : Algebra k ((Spec (.of k)).presheaf.stalk (f.base x)) :=
          StructureSheaf.stalkAlgebra k (f.base x)
        ((f.stalkMap x).hom.comp
          (algebraMap k ((Spec (.of k)).presheaf.stalk (f.base x)))).toAlgebra
      Algebra.IsGeometricallyReduced k (X.presheaf.stalk x)
```

## Tag 020I, a lemma

[Tag 020I](https://stacks.math.columbia.edu/tag/020I) in the Stacks Project.

**`AlgebraicGeometry.isGeometricallyReducedAt_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Reduced.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Reduced.lean#L291). The attribute's comment: “part (1)”. References: EGA IV (4.6.11), “partial”; EGA IV (4.6.12), “special case”.

> A reduced local ring of a scheme over a perfect field is geometrically reduced at the
> corresponding point.

```lean
public theorem isGeometricallyReducedAt_of_isReduced
    {k : Type u} [Field k] [PerfectField k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) (x : X) [_root_.IsReduced (X.presheaf.stalk x)] :
    IsGeometricallyReducedAt f x
```

**`AlgebraicGeometry.geometricallyReduced_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Reduced.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Reduced.lean#L311). The attribute's comment: “part (2)”. References: EGA IV (4.6.1), “(c) ⇒ (b), special case”; EGA IV (4.6.12), “(b) ⇒ (a), special case”.

> A reduced scheme over a perfect field is geometrically reduced over that field.

```lean
public theorem geometricallyReduced_of_isReduced
    {k : Type u} [Field k] [PerfectField k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsReduced X] :
    GeometricallyReduced f
```

## Tag 035X, a lemma

[Tag 035X](https://stacks.math.columbia.edu/tag/035X) in the Stacks Project.

**`AlgebraicGeometry.geometricallyReduced_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometric/ReducedTFAE.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometric/ReducedTFAE.lean#L124).

> **Stacks Project, Tag 035X.** The seven standard characterizations of geometric reducedness
> for a scheme over a field are equivalent.

```lean
public theorem geometricallyReduced_tfae
    (k : Type u) [Field k] (p : ℕ) [ExpChar k p] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k))
    (kperf : Type u) [Field kperf] [Algebra k kperf] [ExpChar kperf p]
    [PerfectRing kperf p] [IsPerfectClosure (algebraMap k kperf) p]
    (K : Type u) [Field K] [Algebra k K] [IsAlgClosure k K] :
    let isReducedAfterBaseChange := fun (k' : Type u) [Field k'] [Algebra k k'] ↦
      IsReduced (pullback f (Spec.map (ofHom (algebraMap k k'))))
    let geometricallyReducedSections := fun U : X.Opens ↦
      letI : Algebra k Γ(X, U) :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appLE ⊤ U (by simp)).hom.toAlgebra
      Algebra.IsGeometricallyReduced k Γ(X, U)
    List.TFAE
      [ GeometricallyReduced f,
        ∀ (k' : Type u) [Field k'] [Algebra k k'], isReducedAfterBaseChange k',
        ∀ (k' : Type u) [Field k'] [Algebra k k'] [FiniteDimensional k k']
          [IsPurelyInseparable k k'], isReducedAfterBaseChange k',
        isReducedAfterBaseChange (AdjoinPthRoots k),
        isReducedAfterBaseChange kperf,
        isReducedAfterBaseChange K,
        ∀ U : X.affineOpens, geometricallyReducedSections U.1 ]
```

## Tag 035Y, a lemma

[Tag 035Y](https://stacks.math.columbia.edu/tag/035Y) in the Stacks Project.

**`AlgebraicGeometry.isGeometricallyReducedAt_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedPurelyInseparable.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedPurelyInseparable.lean#L51). References: EGA IV (6.7.7), “reduced: b), e), f)”; EGA IV (4.6.1), “special case”; EGA IV (4.6.12), “special case”.

> **Stacks Project, Tag 035Y.** For a scheme over a field of positive characteristic,
> geometric reducedness at a point is equivalent to reducedness of the local rings above that
> point after every finite purely inseparable extension, after adjoining all `p`-th roots, or
> after passing to a perfect closure.

```lean
public theorem isGeometricallyReducedAt_tfae
    {k : Type u} [Field k] (p : ℕ) [CharP k p] (hp : p ≠ 0)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) (x : X) :
    [IsGeometricallyReducedAt f x,
      ∀ (k' : Type u) [Field k'] [Algebra k k'] [FiniteDimensional k k']
          [IsPurelyInseparable k k'],
        let g : Spec (.of k') ⟶ Spec (.of k) :=
          Spec.map (CommRingCat.ofHom (algebraMap k k'))
        ∀ x' : (pullback f g : Scheme), pullback.fst f g x' = x →
          _root_.IsReduced ((pullback f g).presheaf.stalk x'),
      let g : Spec (.of (AdjoinPthRoots k)) ⟶ Spec (.of k) :=
        Spec.map (CommRingCat.ofHom (algebraMap k (AdjoinPthRoots k)))
      ∀ x' : (pullback f g : Scheme), pullback.fst f g x' = x →
        _root_.IsReduced ((pullback f g).presheaf.stalk x'),
      let g : Spec (.of (perfectClosure k (AlgebraicClosure k))) ⟶ Spec (.of k) :=
        Spec.map (CommRingCat.ofHom
          (algebraMap k (perfectClosure k (AlgebraicClosure k))))
      ∀ x' : (pullback f g : Scheme), pullback.fst f g x' = x →
        _root_.IsReduced ((pullback f g).presheaf.stalk x')].TFAE
```

## Tag 0384, a lemma

[Tag 0384](https://stacks.math.columbia.edu/tag/0384) in the Stacks Project.

**`AlgebraicGeometry.isGeometricallyReducedAt_iff_baseChange_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedBaseChange.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedBaseChange.lean#L215). The attribute's comment: “pointwise equivalence”. References: EGA IV (4.6.10).

> **Stacks Project, Tag 0384, pointwise statement.** Geometric reducedness at a point is
> preserved and reflected after extending the base field and choosing a point above it.

```lean
public theorem isGeometricallyReducedAt_iff_baseChange_fieldExtension
    (k k' : Type u) [Field k] [Field k'] [Algebra k k'] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) (x : X)
    (x' : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k k'))) : Scheme))
    (hx' : pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k k'))) x' = x) :
    IsGeometricallyReducedAt f x ↔
      IsGeometricallyReducedAt
        (pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap k k')))) x'
```

**`AlgebraicGeometry.geometricallyReduced_iff_baseChange_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedBaseChange.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedBaseChange.lean#L234). The attribute's comment: “global equivalence”.

> **Stacks Project, Tag 0384, global statement.** A scheme over a field is geometrically
> reduced if and only if its base change along a field extension is geometrically reduced.

```lean
public theorem geometricallyReduced_iff_baseChange_fieldExtension
    (k k' : Type u) [Field k] [Field k'] [Algebra k k'] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) :
    GeometricallyReduced f ↔
      GeometricallyReduced
        (pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap k k'))))
```

## Tag 035Z, a lemma

[Tag 035Z](https://stacks.math.columbia.edu/tag/035Z) in the Stacks Project.

**`AlgebraicGeometry.isReduced_stalk_pullback_of_isGeometricallyReducedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedProduct.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedProduct.lean#L52). The attribute's comment: “reduced\_at\_points\_over\_x”. References: EGA IV (4.6.1), “more general”; EGA IV (4.6.12), “partial”.

> A product with a reduced scheme is reduced at every point above a geometrically reduced
> point of the other factor.

```lean
public theorem isReduced_stalk_pullback_of_isGeometricallyReducedAt
    {k : Type u} [Field k] {X Y : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) (g : Y ⟶ Spec (.of k)) (x : X)
    (hX : IsGeometricallyReducedAt f x) [IsReduced Y]
    (z : (pullback f g : Scheme)) (hz : pullback.fst f g z = x) :
    _root_.IsReduced ((pullback f g).presheaf.stalk z)
```

**`AlgebraicGeometry.isReduced_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedProduct.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedProduct.lean#L120). The attribute's comment: “reduced\_product”. References: EGA IV (4.6.1), “(b) ⇒ (a)”.

> The fibre product of a geometrically reduced scheme and a reduced scheme over a field is
> reduced.

```lean
public theorem isReduced_pullback
    {k : Type u} [Field k] {X Y : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) (g : Y ⟶ Spec (.of k))
    [GeometricallyReduced f] [IsReduced Y] :
    IsReduced (pullback f g)
```

**`AlgebraicGeometry.geometricallyReduced_pullback_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedProduct.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedProduct.lean#L142). The attribute's comment: “geometrically\_reduced\_product”. References: EGA IV (4.6.5).

> The fibre product over a field of two geometrically reduced schemes is geometrically
> reduced.

```lean
public theorem geometricallyReduced_pullback_over_field
    {k : Type u} [Field k] {X Y : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) (g : Y ⟶ Spec (.of k))
    [GeometricallyReduced f] [GeometricallyReduced g] :
    GeometricallyReduced (pullback.fst f g ≫ f)
```

**`AlgebraicGeometry.isReduced_pullback_over_perfectField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedProduct.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedProduct.lean#L163). The attribute's comment: “perfect\_field\_reduced\_product”. References: EGA IV (4.6.1), “special case”; SGA 3 VIA (0.2), “partial”.

> The fibre product of two reduced schemes over a perfect field is reduced.

```lean
public theorem isReduced_pullback_over_perfectField
    {k : Type u} [Field k] [PerfectField k]
    {X Y : Scheme.{u}} (f : X ⟶ Spec (.of k)) (g : Y ⟶ Spec (.of k))
    [IsReduced X] [IsReduced Y] :
    IsReduced (pullback f g)
```

## Tag 04KS, a lemma

[Tag 04KS](https://stacks.math.columbia.edu/tag/04KS) in the Stacks Project.

**`AlgebraicGeometry.isGeometricallyReducedAt_of_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedGenericPoints.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedGenericPoints.lean#L87). The attribute's comment: “geometric\_reducedness\_at\_generalization”.

> **Stacks Project, Tag 04KS.** Geometric reducedness at a point of a scheme over a field is
> preserved on passing to a generalization of that point.

```lean
public theorem isGeometricallyReducedAt_of_specializes
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) {x' x : X}
    (hsp : x' ⤳ x) (hx : IsGeometricallyReducedAt f x) :
    IsGeometricallyReducedAt f x'
```

**`AlgebraicGeometry.isGeometricallyReducedAt_of_isReduced_stalk_of_genericPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedGenericPoints.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedGenericPoints.lean#L272). The attribute's comment: “geometric\_reducedness\_at\_point\_of\_generic\_points”.

> **Stacks Project, Tag 04KS.** A scheme over a field is geometrically reduced at a point
> whose local ring is reduced if it is geometrically reduced at every generic point of an
> irreducible component specializing to that point.

```lean
public theorem isGeometricallyReducedAt_of_isReduced_stalk_of_genericPoints
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) (x : X)
    (hx : _root_.IsReduced (X.presheaf.stalk x))
    (hgeneric : ∀ x' : X, x' ∈ genericPoints X → x' ⤳ x →
      IsGeometricallyReducedAt f x') :
    IsGeometricallyReducedAt f x
```

**`AlgebraicGeometry.geometricallyReduced_of_isGeometricallyReducedAt_genericPoints`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedGenericPoints.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedGenericPoints.lean#L317). The attribute's comment: “geometric\_reducedness\_of\_generic\_points”.

> A reduced scheme over a field which is geometrically reduced at the generic points of all
> its irreducible components is geometrically reduced.

```lean
public lemma geometricallyReduced_of_isGeometricallyReducedAt_genericPoints
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsReduced X]
    (h : ∀ x : X, x ∈ genericPoints X → IsGeometricallyReducedAt f x) :
    GeometricallyReduced f
```

**`AlgebraicGeometry.geometricallyReduced_iff_isSeparableExtension_functionField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedGenericPoints.lean, line 339](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedGenericPoints.lean#L339). The attribute's comment: “geometric\_reducedness\_iff\_separable\_function\_field”. References: EGA IV (4.2.4), “(ii), special case”; EGA IV (4.6.1), “(b) ⇔ (e), special case”; EGA IV (4.6.3); EGA IV (6.7.5), “partial”; SGA 1 X (1.1), “special case”.

> **Stacks Project, Tag 04KS.** An integral scheme over a field is geometrically reduced if and
> only if its function field is a separable extension of the base field.

```lean
public theorem geometricallyReduced_iff_isSeparableExtension_functionField
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsIntegral X] :
    letI : Nonempty (⊤ : X.Opens) := ⟨⟨genericPoint X, trivial⟩⟩
    letI : Algebra k X.functionField :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫
        X.germToFunctionField ⊤).hom.toAlgebra
    GeometricallyReduced f ↔ Algebra.IsSeparableExtension k X.functionField
```

## Tag 0360, a lemma

[Tag 0360](https://stacks.math.columbia.edu/tag/0360) in the Stacks Project.

**`AlgebraicGeometry.exists_open_geometricallyReduced_of_isGeometricallyReducedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedNoetherian.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedNoetherian.lean#L66). References: EGA IV (4.6.13), “(a) ⇒ (f)”.

> **Stacks Project, Tag 0360.** A locally Noetherian scheme that is geometrically reduced at a
> point has a geometrically reduced open neighbourhood of that point.

```lean
public theorem exists_open_geometricallyReduced_of_isGeometricallyReducedAt
    {k : Type u} [Field k] {X : Scheme.{u}} [IsLocallyNoetherian X]
    (f : X ⟶ Spec (.of k)) (x : X) (hx : IsGeometricallyReducedAt f x) :
    ∃ U : X.Opens, x ∈ U ∧ GeometricallyReduced (U.ι ≫ f)
```

## Tag 020F, an example

[Tag 020F](https://stacks.math.columbia.edu/tag/020F) in the Stacks Project.

**`AlgebraicGeometry.InseparableHypersurface.nilpotentElement_pow_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedCounterexample.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedCounterexample.lean#L121). The attribute's comment: “the displayed element has p-th power zero”.

> **Stacks Project, Tag 020F.** The displayed element is nilpotent.

```lean
public theorem nilpotentElement_pow_eq_zero (K : Type*) [Field K]
    [Algebra (rationalFunctionField p) K] (a b : K)
    (ha : a ^ p = algebraMap (rationalFunctionField p) K (transcendentalGenerator p 0))
    (hb : b ^ p = algebraMap (rationalFunctionField p) K (transcendentalGenerator p 1)) :
    nilpotentElement p K a b ^ p = 0
```

**`AlgebraicGeometry.InseparableHypersurface.hypersurface_isVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedCounterexample.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedCounterexample.lean#L312). The attribute's comment: “the original scheme is a variety”.

> **Stacks Project, Tag 020F.** The hypersurface over `𝔽ₚ(s,t)` is a variety.

```lean
public theorem hypersurface_isVariety :
    IsVariety (rationalFunctionField p) (hypersurfaceToSpec p)
```

**`AlgebraicGeometry.InseparableHypersurface.nilpotentElement_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedCounterexample.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedCounterexample.lean#L423). The attribute's comment: “the displayed element is nonzero”.

> **Stacks Project, Tag 020F.** The displayed element is nonzero.

```lean
public theorem nilpotentElement_ne_zero (K : Type*) [Field K]
    [Algebra (rationalFunctionField p) K] (a b : K) :
    nilpotentElement p K a b ≠ 0
```

**`AlgebraicGeometry.InseparableHypersurface.baseChange_not_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedCounterexample.lean, line 464](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ReducedCounterexample.lean#L464). The attribute's comment: “the base change is not reduced”.

> **Stacks Project, Tag 020F.** The base change to a field containing both roots is
> not reduced.

```lean
public theorem baseChange_not_isReduced (K : Type) [Field K]
    [Algebra (rationalFunctionField p) K] (a b : K)
    (ha : a ^ p = algebraMap (rationalFunctionField p) K (transcendentalGenerator p 0))
    (hb : b ^ p = algebraMap (rationalFunctionField p) K (transcendentalGenerator p 1)) :
    ¬ IsReduced (pullback (hypersurfaceToSpec p)
      (Spec.map (CommRingCat.ofHom (algebraMap (rationalFunctionField p) K))))
```

## Tag 04KT, a lemma

[Tag 04KT](https://stacks.math.columbia.edu/tag/04KT) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_purelyInseparable_extension_geometricallyReduced_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometric/ReducedReduction.lean, line 647](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometric/ReducedReduction.lean#L647). References: EGA IV (17.15.14.2), “geom. reduced reduction”; EGA IV (4.6.6), “more general”; EGA IV (4.6.8), “First clause”.

> **Stacks Project, Tag 04KT.** After a finite purely inseparable extension of the ground
> field, the reduction of the base change of a scheme with finitely many irreducible components
> is geometrically reduced.

```lean
public theorem exists_finite_purelyInseparable_extension_geometricallyReduced_reduction
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] (hX : (irreducibleComponents X).Finite) :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k k')
      (_ : Module.Finite k k') (_ : IsPurelyInseparable k k'),
      let g : Spec (.of k') ⟶ Spec (.of k) :=
        Spec.map (CommRingCat.ofHom (algebraMap k k'))
      let p : pullback f g ⟶ Spec (.of k') := pullback.snd f g
      let I := Scheme.IdealSheafData.vanishingIdeal
        (X := (pullback f g : Scheme.{u})) (⊤ : Closeds (pullback f g : Scheme.{u}))
      GeometricallyReduced (I.subschemeι ≫ p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.6, Tag 035U](https://stacks.math.columbia.edu/tag/035U)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
