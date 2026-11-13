---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsGeometricallyRegularAt, AlgebraicGeometry.IsGeometricallyRegular, AlgebraicGeometry.geometricallyRegularAt_tfae, AlgebraicGeometry.geometricallyRegular_tfae, AlgebraicGeometry.geometricallyRegularAt_baseChange_iff, AlgebraicGeometry.geometricallyRegular_baseChange_iff, AlgebraicGeometry.isGeometricallyRegularAt_baseChange_iff, AlgebraicGeometry.isGeometricallyRegular_baseChange_iff
statement: formalized
proof: formalized
---

# 33.12 Geometrically regular schemes

Section 33.12 of the Stacks Project, [Tag 038S](https://stacks.math.columbia.edu/tag/038S). 7 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 038T, a definition

[Tag 038T](https://stacks.math.columbia.edu/tag/038T) in the Stacks Project.

**`AlgebraicGeometry.IsGeometricallyRegularAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Regular.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Regular.lean#L67). The attribute's comment: “part (1)”. References: EGA IV (6.7.6), “geom. regular at x”; EGA IV (6.7.8).

> **Stacks Project, Tag 038T, part (1).** A scheme `X` over a field `k` is geometrically
> regular at `x` if, after every finitely generated field extension `K/k`, every point above `x`
> has a regular local ring.

```lean
public abbrev IsGeometricallyRegularAt {k : Type u} [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) (x : X) : Prop
```

**`AlgebraicGeometry.IsGeometricallyRegular`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Regular.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Regular.lean#L82). The attribute's comment: “part (2)”. References: EGA IV (6.7.6), “geometrically regular”.

> **Stacks Project, Tag 038T, part (2).** A scheme over a field is geometrically regular if it
> is geometrically regular at every point.

```lean
public abbrev IsGeometricallyRegular {k : Type u} [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) : Prop
```

## Tag 038U, a lemma

[Tag 038U](https://stacks.math.columbia.edu/tag/038U) in the Stacks Project.

**`AlgebraicGeometry.geometricallyRegularAt_tfae`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Regular.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Regular.lean#L275).

> For a locally Noetherian scheme over a field, geometric regularity at a point is equivalent
> both to regularity at every point above it after every finite purely inseparable field extension,
> and to geometric regularity of its local ring over the ground field.

```lean
public lemma geometricallyRegularAt_tfae
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [IsLocallyNoetherian X] (x : X) :
    List.TFAE [
      IsGeometricallyRegularAt f x,
      ∀ (K : Type u) [Field K] [Algebra k K] [Module.Finite k K]
        [IsPurelyInseparable k K],
        ∀ (x' : (pullback f
            (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u})),
          pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K))) x' = x →
            IsRegularLocalRing
              ((pullback f
                (Spec.map
                  (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}).presheaf.stalk x'),
      let : Algebra k (X.presheaf.stalk x) :=
        let : Algebra k ((Spec (.of k)).presheaf.stalk (f.base x)) :=
          StructureSheaf.stalkAlgebra k (f.base x)
        ((f.stalkMap x).hom.comp
          (algebraMap k ((Spec (.of k)).presheaf.stalk (f.base x)))).toAlgebra
      Algebra.IsGeometricallyRegular k (X.presheaf.stalk x)]
```

## Tag 038V, a lemma

[Tag 038V](https://stacks.math.columbia.edu/tag/038V) in the Stacks Project.

**`AlgebraicGeometry.geometricallyRegular_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/Regular.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/Regular.lean#L162).

> **Stacks Project, Tag 038V.** The five standard characterizations of geometric regularity
> for a locally Noetherian scheme over a field are equivalent.

```lean
theorem geometricallyRegular_tfae
    (k : Type u) [Field k] (X : Scheme.{u}) [IsLocallyNoetherian X]
    (f : X ⟶ Spec (.of k)) :
    let geometricallyRegularSections := fun U : X.Opens ↦
      letI : Algebra k Γ(X, U) :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appLE ⊤ U (by simp)).hom.toAlgebra
      Algebra.IsGeometricallyRegular k Γ(X, U)
    List.TFAE
      [ IsGeometricallyRegular f,
        ∀ (k' : Type u) [Field k'] [Algebra k k'] [Algebra.EssFiniteType k k'],
          IsRegular
            (pullback f (Spec.map (ofHom (algebraMap k k')))),
        ∀ (k' : Type u) [Field k'] [Algebra k k'] [Module.Finite k k']
          [IsPurelyInseparable k k'],
          IsRegular
            (pullback f (Spec.map (ofHom (algebraMap k k')))),
        ∀ U : X.affineOpens, geometricallyRegularSections U.1,
        ∃ (I : Type u) (U : I → X.affineOpens),
          (⨆ i, (U i).1) = ⊤ ∧ ∀ i, geometricallyRegularSections (U i).1 ]
```

## Tag 038W, a lemma

[Tag 038W](https://stacks.math.columbia.edu/tag/038W) in the Stacks Project.

**`AlgebraicGeometry.geometricallyRegularAt_baseChange_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/RegularBaseChange.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/RegularBaseChange.lean#L148). The attribute's comment: “pointwise equivalence”.

> **Stacks Project, Tag 038W, pointwise assertion.** Geometric regularity at a point
> is equivalent to geometric regularity at any point above it after a finitely generated
> extension of the ground field.

```lean
public theorem geometricallyRegularAt_baseChange_iff
    (k k' : Type u) [Field k] [Field k'] [Algebra k k']
    [Algebra.EssFiniteType k k']
    (X : Scheme.{u}) [IsLocallyNoetherian X]
    (f : X ⟶ Spec (.of k)) (x : X) :
    let g : Spec (.of k') ⟶ Spec (.of k) :=
      Spec.map (ofHom (algebraMap k k'))
    ∀ (x' : (pullback f g : Scheme.{u})),
      pullback.fst f g x' = x →
        (IsGeometricallyRegularAt f x ↔
          IsGeometricallyRegularAt (pullback.snd f g) x')
```

**`AlgebraicGeometry.geometricallyRegular_baseChange_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/RegularBaseChange.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/RegularBaseChange.lean#L166). The attribute's comment: “global equivalence”.

> **Stacks Project, Tag 038W, global assertion.** Geometric regularity is invariant
> under finitely generated extension of the ground field.

```lean
public theorem geometricallyRegular_baseChange_iff
    (k k' : Type u) [Field k] [Field k'] [Algebra k k']
    [Algebra.EssFiniteType k k']
    (X : Scheme.{u}) [IsLocallyNoetherian X]
    (f : X ⟶ Spec (.of k)) :
    let g : Spec (.of k') ⟶ Spec (.of k) :=
      Spec.map (ofHom (algebraMap k k'))
    IsGeometricallyRegular f ↔
      IsGeometricallyRegular (pullback.snd f g)
```

**`AlgebraicGeometry.isGeometricallyRegularAt_baseChange_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/RegularUpstairs.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/RegularUpstairs.lean#L233). The attribute's comment: “the equivalence of (1) and (2), for any scheme over k”. References: EGA IV (6.7.8), “clause (iv)”.

> **Stacks Project, Tag 038W, the equivalence.** Let `k` be a field, `X` a scheme over `k`,
> `k'/k` a finitely generated field extension, `x ∈ X`, and `x' ∈ X_{k'}` a point lying over `x`.
> Then `X` is geometrically regular at `x` over `k` if and only if `X_{k'}` is geometrically
> regular at `x'` over `k'`.

```lean
public theorem isGeometricallyRegularAt_baseChange_iff
    (k k' : Type u) [Field k] [Field k'] [Algebra k k'] [Algebra.EssFiniteType k k']
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) (x : X)
    (x' : (pullback f (Spec.map (ofHom (algebraMap k k'))) : Scheme.{u}))
    (hx' : pullback.fst f (Spec.map (ofHom (algebraMap k k'))) x' = x) :
    IsGeometricallyRegularAt f x ↔
      IsGeometricallyRegularAt (pullback.snd f (Spec.map (ofHom (algebraMap k k')))) x'
```

**`AlgebraicGeometry.isGeometricallyRegular_baseChange_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/RegularUpstairs.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/RegularUpstairs.lean#L249). The attribute's comment: “in particular: X geometrically regular over k iff X\_\{k'} is over k'”. References: EGA IV (7.3.10), “special case”; EGA IV (7.3.8), “partial”.

> **Stacks Project, Tag 038W, the consequence for schemes.** Let `k` be a field, `X` a scheme
> over `k` and `k'/k` a finitely generated field extension. Then `X` is geometrically regular
> over `k` if and only if `X_{k'}` is geometrically regular over `k'`.

```lean
public theorem isGeometricallyRegular_baseChange_iff
    (k k' : Type u) [Field k] [Field k'] [Algebra k k'] [Algebra.EssFiniteType k k']
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) :
    IsGeometricallyRegular f ↔
      IsGeometricallyRegular (pullback.snd f (Spec.map (ofHom (algebraMap k k'))))
```

## Tag 05AW, a lemma

[Tag 05AW](https://stacks.math.columbia.edu/tag/05AW) in the Stacks Project.

**`AlgebraicGeometry.isGeometricallyRegularAt_of_flatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/RegularDescent.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/RegularDescent.lean#L40). The attribute's comment: “pointwise statement”.

> **Stacks Project, Tag 05AW (pointwise statement).** Geometric regularity at a point
> descends along a morphism which is flat at that point.

```lean
public theorem isGeometricallyRegularAt_of_flatAt {k : Type u} [Field k]
    {X Y : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Spec (.of k))
    [IsLocallyNoetherian X] [IsLocallyNoetherian Y] (x : X)
    (hX : IsGeometricallyRegularAt (f ≫ g) x)
    (hf : AlgebraicGeometry.IsFlatAt f.toLRSHom.toShHom x) :
    IsGeometricallyRegularAt g (f x)
```

**`AlgebraicGeometry.isGeometricallyRegular_of_flat_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/RegularDescent.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/RegularDescent.lean#L75). The attribute's comment: “global statement”.

> **Stacks Project, Tag 05AW (global statement).** A flat surjective image of a
> geometrically regular scheme over a field is geometrically regular.

```lean
public theorem isGeometricallyRegular_of_flat_surjective {k : Type u} [Field k]
    {X Y : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Spec (.of k))
    [IsLocallyNoetherian X] [IsLocallyNoetherian Y] [Flat f] [Surjective f]
    (hX : IsGeometricallyRegular (f ≫ g)) :
    IsGeometricallyRegular g
```

## Tag 038X, a lemma

[Tag 038X](https://stacks.math.columbia.edu/tag/038X) in the Stacks Project.

**`AlgebraicGeometry.isGeometricallyRegularAt_iff_smoothAt`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/RegularSmooth.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/RegularSmooth.lean#L140). References: EGA IV (17.5.2), “base a field, pointwise”; EGA IV (17.5.5), “base = Spec k”; EGA IV (17.15.2), “more general”; SGA 1 II (5.4), “more general”.

> **Stacks Project, Tag 038X.** For a scheme locally of finite type over a field, geometric
> regularity at a point is equivalent to smoothness of the structure morphism at that point.

```lean
public lemma isGeometricallyRegularAt_iff_smoothAt
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] (x : X) :
    IsGeometricallyRegularAt f x ↔ InfinitesimalLifting.SmoothAt f x
```

## Tag 038Y, an example

[Tag 038Y](https://stacks.math.columbia.edu/tag/038Y) in the Stacks Project.

**`AlgebraicGeometry.curve_isVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/CuspidalCurve.lean, line 322](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/CuspidalCurve.lean#L322). The attribute's comment: “geometrically\_reduced\_not\_geometrically\_normal”. References: EGA IV (6.7.5), “(i) X integral curve”.

> **Stacks Project, Tag 038Y.** The curve is a variety over `𝔽ₚ(t)`.

```lean
theorem curve_isVariety (hp : 2 < p) :
    IsVariety (RatFunc (ZMod p)) (curveToBase p)
```

**`AlgebraicGeometry.curve_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/CuspidalCurve.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/CuspidalCurve.lean#L336). The attribute's comment: “geometrically\_reduced\_not\_geometrically\_normal”. References: EGA IV (6.7.5), “(i) X regular”.

> **Stacks Project, Tag 038Y.** The curve is regular.

```lean
theorem curve_isRegular (_hp : 2 < p) :
    IsRegular (curve p)
```

**`AlgebraicGeometry.curve_geometricallyReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/CuspidalCurve.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/CuspidalCurve.lean#L348). The attribute's comment: “geometrically\_reduced\_not\_geometrically\_normal”. References: EGA IV (6.7.5), “(i) X geom. integral”.

> **Stacks Project, Tag 038Y.** The curve is geometrically reduced.

```lean
theorem curve_geometricallyReduced (hp : 2 < p) :
    GeometricallyReduced (curveToBase p)
```

**`AlgebraicGeometry.curve_not_isGeometricallyNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/CuspidalCurve.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/CuspidalCurve.lean#L448). The attribute's comment: “geometrically\_reduced\_not\_geometrically\_normal”.

> **Stacks Project, Tag 038Y.** The curve is not geometrically normal.

```lean
theorem curve_not_isGeometricallyNormal (hp : 2 < p) :
    ¬ IsGeometricallyNormal (curveToBase p)
```

**`AlgebraicGeometry.hypersurface_isVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/InseparableHypersurface.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/InseparableHypersurface.lean#L114). The attribute's comment: “regular\_not\_geometrically\_reduced”.

> **Stacks Project, Tag 038Y.** The hypersurface is a variety over `𝔽ₚ(t)`.

```lean
theorem hypersurface_isVariety :
    IsVariety (RatFunc (ZMod p)) (hypersurfaceToBase p)
```

**`AlgebraicGeometry.hypersurface_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/InseparableHypersurface.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/InseparableHypersurface.lean#L127). The attribute's comment: “regular\_not\_geometrically\_reduced”.

> **Stacks Project, Tag 038Y.** The hypersurface is regular.

```lean
theorem hypersurface_isRegular :
    IsRegular (hypersurface p)
```

**`AlgebraicGeometry.hypersurface_not_geometricallyReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/InseparableHypersurface.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/InseparableHypersurface.lean#L141). The attribute's comment: “regular\_not\_geometrically\_reduced”.

> **Stacks Project, Tag 038Y.** The hypersurface is not geometrically reduced.

```lean
theorem hypersurface_not_geometricallyReduced :
    ¬ GeometricallyReduced (hypersurfaceToBase p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.12, Tag 038S](https://stacks.math.columbia.edu/tag/038S)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
