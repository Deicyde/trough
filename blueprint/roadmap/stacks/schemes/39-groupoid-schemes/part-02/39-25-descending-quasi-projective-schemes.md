---
declaration: section
origin: cited
lean: AlgebraicGeometry.DescentDatum.isEffective_of_cardinalMk_geometricFibre_le, AlgebraicGeometry.DescentDatum.isEffective_of_forall_exists_isAffineOpen, AlgebraicGeometry.DescentDatum.isEffective_of_isAmple, AlgebraicGeometry.DescentDatum.isEffective_of_isRelativelyAmple, AlgebraicGeometry.DescentDatum.isEffective_of_isQuasiProjective, AlgebraicGeometry.DescentDatum.isEffective_of_isProjectiveMorphism, AlgebraicGeometry.DescentDatum.isEffective_of_isProjective, AlgebraicGeometry.DescentDatum.isEffective_of_isRelativelyVeryAmple
statement: formalized
proof: formalized
---

# 39.25 Descending quasi-projective schemes

Section 39.25 of the Stacks Project, [Tag 0CCH](https://stacks.math.columbia.edu/tag/0CCH). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0H8K, a lemma

[Tag 0H8K](https://stacks.math.columbia.edu/tag/0H8K) in the Stacks Project.

**`AlgebraicGeometry.DescentDatum.isEffective_of_cardinalMk_geometricFibre_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/Effective.lean, line 511](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/Effective.lean#L511). References: SGA 1 VIII (7.6), “sufficiency, fibres ≤ d”.

> **Stacks Project, Tag 0H8K.** Let `f : X ⟶ Y` be a surjective finite locally free morphism
> of schemes and let `d` be a positive integer such that every geometric fibre of `f` has at most
> `d` points. Let `D` be a descent datum relative to `f` whose underlying scheme `V` has the
> property that any `d` points of `V` lying over one point of `Y` have a common affine open
> neighbourhood. Then `D` is effective.

```lean
theorem isEffective_of_cardinalMk_geometricFibre_le
    {X Y : Scheme.{u}} {f : X ⟶ Y} [Surjective f] [IsFiniteLocallyFree f]
    (d : ℕ) (hd : 0 < d)
    (hfib : ∀ p : GeometricPoint Y,
      Cardinal.mk (pullback p.hom f : Scheme.{u}) ≤ (d : Cardinal.{u}))
    (D : DescentDatum f)
    (hV : ∀ (y : Y) (v : Fin d → D.over.left),
      (∀ i, (D.over.hom ≫ f) (v i) = y) →
        ∃ U : D.over.left.Opens, IsAffineOpen U ∧ ∀ i, v i ∈ U) :
    DescentData.IsEffective D
```

## Tag 0CCI, a lemma

[Tag 0CCI](https://stacks.math.columbia.edu/tag/0CCI) in the Stacks Project.

**`AlgebraicGeometry.DescentDatum.isEffective_of_forall_exists_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/Effective.lean, line 597](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/Effective.lean#L597).

> **Stacks Project, Tag 0CCI.** Let `f : X ⟶ Y` be a surjective finite locally free morphism
> of schemes and let `D` be a descent datum relative to `f` whose underlying scheme `V` has the
> property that any finite nonempty collection of points of `V` lying over one point of `Y` has a
> common affine open neighbourhood. Then `D` is effective.

```lean
theorem isEffective_of_forall_exists_isAffineOpen
    {X Y : Scheme.{u}} {f : X ⟶ Y} [Surjective f] [IsFiniteLocallyFree f] (D : DescentDatum f)
    (hV : ∀ (n : ℕ) (y : Y) (v : Fin (n + 1) → D.over.left),
      (∀ i, (D.over.hom ≫ f) (v i) = y) →
        ∃ U : D.over.left.Opens, IsAffineOpen U ∧ ∀ i, v i ∈ U) :
    DescentData.IsEffective D
```

## Tag 0CCJ, a lemma

[Tag 0CCJ](https://stacks.math.columbia.edu/tag/0CCJ) in the Stacks Project.

**`AlgebraicGeometry.DescentDatum.isEffective_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/QuasiProjective.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/QuasiProjective.lean#L173). The attribute's comment: “condition (3), an ample invertible sheaf on V”. References: SGA 1 VIII (7.6), “special case”; SGA 1 VIII (7.7), “special case”.

> **Stacks Project, Tag 0CCJ, condition (3).** Let `f : X ⟶ Y` be a surjective finite locally
> free morphism. A descent datum on `V/X/Y` whose scheme `V` carries an ample invertible
> `𝒪_V`-module is effective.

```lean
theorem isEffective_of_isAmple {X Y : Scheme.{u}} {f : X ⟶ Y} [Surjective f]
    [IsFiniteLocallyFree f] (D : DescentDatum f) (L : D.over.left.Modules)
    [Stacks.Ample.IsInvertibleModule D.over.left L]
    (hL : Stacks.Ample.IsAmple D.over.left L) :
    DescentData.IsEffective D
```

**`AlgebraicGeometry.DescentDatum.isEffective_of_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/QuasiProjective.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/QuasiProjective.lean#L192). The attribute's comment: “condition (4), an X-ample invertible sheaf on V”. References: SGA 1 VIII (7.6), “more general”; SGA 1 VIII (7.7), “more general”; SGA 1 VIII (7.8), “partial”; SGA 1 XI (4.6), “partial”.

> **Stacks Project, Tag 0CCJ, condition (4).** Let `f : X ⟶ Y` be a surjective finite locally
> free morphism. A descent datum on `V/X/Y` whose scheme `V` carries an invertible `𝒪_V`-module
> ample relative to `V ⟶ X` is effective.

```lean
theorem isEffective_of_isRelativelyAmple {X Y : Scheme.{u}} {f : X ⟶ Y} [Surjective f]
    [IsFiniteLocallyFree f] (D : DescentDatum f) (L : D.over.left.Modules)
    [Stacks.Ample.IsInvertibleModule D.over.left L]
    (hL : Stacks.RelativeAmple.IsRelativelyAmple D.over.hom L) :
    DescentData.IsEffective D
```

**`AlgebraicGeometry.DescentDatum.isEffective_of_isQuasiProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/QuasiProjective.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/QuasiProjective.lean#L207). The attribute's comment: “condition (2), V ⟶ X quasi-projective”. References: SGA 1 VIII (7.6); SGA 1 VIII (7.7), “Effectivity clause”; SGA 1 XI (4.6), “partial”.

> **Stacks Project, Tag 0CCJ, condition (2).** Let `f : X ⟶ Y` be a surjective finite locally
> free morphism. A descent datum on `V/X/Y` whose scheme `V` is quasi-projective over `X` is
> effective.

```lean
theorem isEffective_of_isQuasiProjective {X Y : Scheme.{u}} {f : X ⟶ Y} [Surjective f]
    [IsFiniteLocallyFree f] (D : DescentDatum f) (hV : IsQuasiProjective D.over.hom) :
    DescentData.IsEffective D
```

**`AlgebraicGeometry.DescentDatum.isEffective_of_isProjectiveMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/QuasiProjective.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/QuasiProjective.lean#L222). The attribute's comment: “condition (1), V ⟶ X H-projective”. References: SGA 1 VIII (7.6), “special case”; SGA 1 VIII (7.7), “special case”; SGA 1 XI (4.6), “partial”.

> **Stacks Project, Tag 0CCJ, condition (1), H-projective case.** Let `f : X ⟶ Y` be a
> surjective finite locally free morphism. A descent datum on `V/X/Y` whose scheme `V` is
> H-projective over `X` is effective.

```lean
theorem isEffective_of_isProjectiveMorphism {X Y : Scheme.{u}} {f : X ⟶ Y} [Surjective f]
    [IsFiniteLocallyFree f] (D : DescentDatum f) (hV : IsProjectiveMorphism D.over.hom) :
    DescentData.IsEffective D
```

**`AlgebraicGeometry.DescentDatum.isEffective_of_isProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/QuasiProjective.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/QuasiProjective.lean#L273). The attribute's comment: “condition (1), V ⟶ X projective”. References: SGA 1 VIII (7.6), “special case”; SGA 1 VIII (7.7), “special case”; SGA 1 XI (4.6), “partial”.

> **Stacks Project, Tag 0CCJ, condition (1).** Let `f : X ⟶ Y` be a surjective finite locally
> free morphism. A descent datum on `V/X/Y` whose scheme `V` is projective over `X` — in the sense
> of clause (1) of [Stacks, Tag 01W8], a closed immersion over `X` into the projective bundle of a
> quasi-coherent `𝒪_X`-module of finite type — is effective.

```lean
theorem isEffective_of_isProjective {X Y : Scheme.{u}} {f : X ⟶ Y} [Surjective f]
    [IsFiniteLocallyFree f] (D : DescentDatum f) (hV : IsProjective D.over.hom) :
    DescentData.IsEffective D
```

**`AlgebraicGeometry.DescentDatum.isEffective_of_isRelativelyVeryAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/QuasiProjective.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/QuasiProjective.lean#L304). The attribute's comment: “condition (5), an X-very ample invertible sheaf on V”. References: SGA 1 VIII (7.6), “special case”; SGA 1 VIII (7.7), “special case”; SGA 1 VIII (7.8), “partial”.

> **Stacks Project, Tag 0CCJ, condition (5).** Let `f : X ⟶ Y` be a surjective finite locally
> free morphism. A descent datum on `V/X/Y` whose scheme `V` carries an invertible `𝒪_V`-module
> very ample relative to `V ⟶ X` is effective.

```lean
theorem isEffective_of_isRelativelyVeryAmple {X Y : Scheme.{u}} {f : X ⟶ Y} [Surjective f]
    [IsFiniteLocallyFree f] (D : DescentDatum f) (L : D.over.left.Modules)
    [Stacks.Ample.IsInvertibleModule D.over.left L]
    (hL : Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple D.over.hom L) :
    DescentData.IsEffective D
```

## Tag 0H8L, a lemma

[Tag 0H8L](https://stacks.math.columbia.edu/tag/0H8L) in the Stacks Project.

**`AlgebraicGeometry.DescentDatum.isEffective_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/Effective.lean, line 624](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BoundedFibreDescent/Effective.lean#L624).

> **Stacks Project, Tag 0H8L.** Every descent datum relative to a surjective finite locally
> free radicial morphism of schemes is effective: such a morphism is universally injective, so
> each of its geometric fibres is a single point.

```lean
theorem isEffective_of_universallyInjective
    {X Y : Scheme.{u}} {f : X ⟶ Y} [Surjective f] [IsFiniteLocallyFree f]
    [UniversallyInjective f] (D : DescentDatum f) : DescentData.IsEffective D
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.25, Tag 0CCH](https://stacks.math.columbia.edu/tag/0CCH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
