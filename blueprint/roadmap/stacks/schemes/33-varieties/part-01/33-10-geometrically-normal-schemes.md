---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsGeometricallyNormalAt, AlgebraicGeometry.IsGeometricallyNormal, AlgebraicGeometry.geometricallyNormalAt_tfae, AlgebraicGeometry.geometricallyNormal_tfae, AlgebraicGeometry.isGeometricallyNormal_iff_baseChange, AlgebraicGeometry.isGeometricallyNormalAt_iff_baseChange, AlgebraicGeometry.isGeometricallyNormal_iff_baseChange_of_isGeometricallyNormalAt, AlgebraicGeometry.isNormal_pullback_of_isGeometricallyNormal
statement: formalized
proof: formalized
---

# 33.10 Geometrically normal schemes

Section 33.10 of the Stacks Project, [Tag 038L](https://stacks.math.columbia.edu/tag/038L). 7 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 038M, a definition

[Tag 038M](https://stacks.math.columbia.edu/tag/038M) in the Stacks Project.

**`AlgebraicGeometry.IsGeometricallyNormalAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Normal.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Normal.lean#L53). The attribute's comment: “part (1)”. References: EGA IV (6.7.6); EGA IV (6.7.8).

> A scheme `X ⟶ Spec k` is geometrically normal at `x` if, after every field extension
> `K / k`, the local ring at every point of the base change lying over `x` is normal.

```lean
public def IsGeometricallyNormalAt (f : X ⟶ Spec (.of k)) (x : X) : Prop
```

**`AlgebraicGeometry.IsGeometricallyNormal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Normal.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/Normal.lean#L62). The attribute's comment: “part (2)”. References: EGA IV (6.7.6).

> A scheme over `k` is geometrically normal if it is geometrically normal at every point.

```lean
public def IsGeometricallyNormal (f : X ⟶ Spec (.of k)) : Prop
```

## Tag 038N, a lemma

[Tag 038N](https://stacks.math.columbia.edu/tag/038N) in the Stacks Project.

**`AlgebraicGeometry.geometricallyNormalAt_tfae`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/Normal.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/Normal.lean#L133).

> Geometric normality at a point is equivalent both to normality at every point above it after
> every finite purely inseparable field extension and to geometric normality of its local ring over
> the ground field.

```lean
lemma geometricallyNormalAt_tfae
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) (x : X) :
    List.TFAE [
      IsGeometricallyNormalAt f x,
      ∀ (K : Type u) [Field K] [Algebra k K] [Module.Finite k K]
        [IsPurelyInseparable k K],
        ∀ (x' : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u})),
          pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K))) x' = x →
            IsNormalRing
              ((pullback f
                (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}).presheaf.stalk x'),
      letI : Algebra k (X.presheaf.stalk x) :=
        letI : Algebra k ((Spec (.of k)).presheaf.stalk (f.base x)) :=
          StructureSheaf.stalkAlgebra k (f.base x)
        ((f.stalkMap x).hom.comp
          (algebraMap k ((Spec (.of k)).presheaf.stalk (f.base x)))).toAlgebra
      Algebra.IsGeometricallyNormal k (X.presheaf.stalk x)]
```

## Tag 038O, a lemma

[Tag 038O](https://stacks.math.columbia.edu/tag/038O) in the Stacks Project.

**`AlgebraicGeometry.geometricallyNormal_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/NormalTFAE.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/NormalTFAE.lean#L211).

> **Stacks Project, Tag 038O.** The six standard characterizations of geometric normality for
> a scheme over a field are equivalent.

```lean
public theorem geometricallyNormal_tfae
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) :
    let geometricallyNormalSections := fun U : X.Opens ↦
      letI : Algebra k Γ(X, U) :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appLE ⊤ U (by simp)).hom.toAlgebra
      Algebra.IsGeometricallyNormal k Γ(X, U)
    List.TFAE
      [ IsGeometricallyNormal f,
        ∀ (k' : Type u) [Field k'] [Algebra k k'],
          IsNormal (pullback f (Spec.map (ofHom (algebraMap k k')))),
        ∀ (k' : Type u) [Field k'] [Algebra k k'] [Algebra.EssFiniteType k k'],
          IsNormal (pullback f (Spec.map (ofHom (algebraMap k k')))),
        ∀ (k' : Type u) [Field k'] [Algebra k k'] [Module.Finite k k']
          [IsPurelyInseparable k k'],
          IsNormal (pullback f (Spec.map (ofHom (algebraMap k k')))),
        ∀ U : X.affineOpens, geometricallyNormalSections U.1,
        IsNormal (pullback f (Spec.map
          (ofHom (algebraMap k (perfectClosure k (AlgebraicClosure k)))))) ]
```

## Tag 038P, a lemma

[Tag 038P](https://stacks.math.columbia.edu/tag/038P) in the Stacks Project.

**`AlgebraicGeometry.isGeometricallyNormal_iff_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NormalMorphism/BaseFieldExtension.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NormalMorphism/BaseFieldExtension.lean#L93). The attribute's comment: “global equivalence”. References: EGA IV (6.7.8), “(vi) global”.

> **Stacks Project, Tag 038P.** Geometric normality of a scheme over a field is invariant
> under extension of the ground field.

```lean
public theorem isGeometricallyNormal_iff_baseChange (k K : Type u) [Field k] [Field K]
    [Algebra k K] (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) :
    IsGeometricallyNormal f ↔
      IsGeometricallyNormal (pullback.snd f (Spec.map (ofHom (algebraMap k K))))
```

**`AlgebraicGeometry.isGeometricallyNormalAt_iff_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/Normal.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/Normal.lean#L292). The attribute's comment: “pointwise equivalence”. References: EGA IV (6.7.8), “(vi)”.

> Geometric normality at a point is invariant under extension of the base field.

```lean
theorem isGeometricallyNormalAt_iff_baseChange
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    (K : Type u) [Field K] [Algebra k K]
    (x : X) (x' : (pullback f (Spec.map (ofHom (algebraMap k K))) : Scheme.{u}))
    (hx' : (pullback.fst f (Spec.map (ofHom (algebraMap k K)))).base x' = x) :
    IsGeometricallyNormalAt f x ↔
      IsGeometricallyNormalAt
        (pullback.snd f (Spec.map (ofHom (algebraMap k K)))) x'
```

**`AlgebraicGeometry.isGeometricallyNormal_iff_baseChange_of_isGeometricallyNormalAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/Normal.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/Normal.lean#L323). The attribute's comment: “global equivalence”. References: EGA IV (6.7.8), “(vi) global”; EGA IV (7.3.8), “partial”.

> A scheme is geometrically normal exactly when any base field extension is.

```lean
theorem isGeometricallyNormal_iff_baseChange_of_isGeometricallyNormalAt
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    (K : Type u) [Field K] [Algebra k K] :
    IsGeometricallyNormal f ↔
      IsGeometricallyNormal
        (pullback.snd f (Spec.map (ofHom (algebraMap k K))))
```

## Tag 06DG, a lemma

[Tag 06DG](https://stacks.math.columbia.edu/tag/06DG) in the Stacks Project.

**`AlgebraicGeometry.isNormal_pullback_of_isGeometricallyNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcDescentProperties/PullbackNormal.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FpqcDescentProperties/PullbackNormal.lean#L177). References: EGA IV (6.14.1), “base = Spec of a field”; EGA IV (21.14.4), “more general”; EGA IV (7.3.9), “more general”.

> **Stacks Project, Tag 06DG.** The fibre product over a field of a geometrically normal
> scheme and a normal scheme is normal.

```lean
public theorem isNormal_pullback_of_isGeometricallyNormal {k : Type u} [Field k]
    {X Y : Scheme.{u}} (f : X ⟶ Spec (.of k)) (g : Y ⟶ Spec (.of k))
    (hX : IsGeometricallyNormal f) [IsNormal Y] :
    IsNormal (pullback f g : Scheme.{u})
```

## Tag 0C3M, a lemma

[Tag 0C3M](https://stacks.math.columbia.edu/tag/0C3M) in the Stacks Project.

**`AlgebraicGeometry.isNormal_pullback_of_isSeparableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Normal.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Normal.lean#L399). References: EGA IV (6.14.2); EGA IV (6.14.3), “Y = Spec K”; EGA IV (4.6.4), “Case where X is normal”; EGA IV (6.7.4), “c), special case”.

> **Stacks Project, Tag 0C3M.** A normal scheme over a field stays normal after base change
> along a separable extension of the ground field.
>
> Affine-locally the base change is `Spec (Γ(N, U) ⊗[k] K)`, and the ring-level statement
> `IsNormalRing.tensorProduct_of_isSeparableExtension` applies.

```lean
theorem isNormal_pullback_of_isSeparableExtension
    (k K : Type u) [Field k] [Field K] [Algebra k K] [Algebra.IsSeparableExtension k K]
    {N : Scheme.{u}} (p : N ⟶ Spec (.of k)) [IsNormal N] :
    IsNormal (pullback p (Spec.map (CommRingCat.ofHom (algebraMap k K))))
```

## Tag 0FD3, a lemma

[Tag 0FD3](https://stacks.math.columbia.edu/tag/0FD3) in the Stacks Project.

**`AlgebraicGeometry.isIso_globalSections_tfae_geometricallyConnected_irreducible_integral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ProperGlobalSections.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometrically/ProperGlobalSections.lean#L117).

> For a proper geometrically normal scheme over a field, having only constant global
> functions, geometric connectedness, geometric irreducibility, and geometric integrality are
> equivalent.

```lean
theorem isIso_globalSections_tfae_geometricallyConnected_irreducible_integral
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [IsProper f] (hnormal : IsGeometricallyNormal f) :
    List.TFAE [
      IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop),
      GeometricallyConnected f,
      GeometricallyIrreducible f,
      GeometricallyIntegral f]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.10, Tag 038L](https://stacks.math.columbia.edu/tag/038L)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
