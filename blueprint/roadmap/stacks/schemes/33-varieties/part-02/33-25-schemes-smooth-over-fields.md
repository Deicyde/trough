---
declaration: section
origin: cited
lean: AlgebraicGeometry.smooth_of_isLocallyFree_relativeDifferentials_of_charZero, AlgebraicGeometry.smooth_of_isLocallyFree_relativeDifferentials_of_perfectField, AlgebraicGeometry.isRegular_of_smooth_over_field, AlgebraicGeometry.isGeometricallyRegular_of_smooth, AlgebraicGeometry.isGeometricallyNormal_of_smooth, AlgebraicGeometry.geometricallyReduced_of_smooth, AlgebraicGeometry.exists_closedPoint_finite_separable_residueField, AlgebraicGeometry.dense_closedPoints_with_finite_separable_residueField_of_smooth
statement: formalized
proof: formalized
---

# 33.25 Schemes smooth over fields

Section 33.25 of the Stacks Project, [Tag 04QM](https://stacks.math.columbia.edu/tag/04QM). 11 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04QN, a lemma

[Tag 04QN](https://stacks.math.columbia.edu/tag/04QN) in the Stacks Project.

**`AlgebraicGeometry.smooth_of_isLocallyFree_relativeDifferentials_of_charZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/LocallyFreeDifferentials.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/LocallyFreeDifferentials.lean#L133). References: EGA IV (17.15.6), “characteristic zero”; EGA IV (16.12.2), “base field, finite type”; EGA IV (17.15.7), “free ⇒ smooth”.

> **Stacks Project, Tag 04QN.** A scheme locally of finite type over a field of
> characteristic zero is smooth if its sheaf of relative differentials is locally free.

```lean
theorem smooth_of_isLocallyFree_relativeDifferentials_of_charZero
    {k : Type u} [Field k] [CharZero k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f]
    (hΩ : _root_.SheafOfModules.IsLocallyFree.{u, u, u} f.relativeDifferentials) :
    Smooth f
```

## Tag 04QP, a lemma

[Tag 04QP](https://stacks.math.columbia.edu/tag/04QP) in the Stacks Project.

**`AlgebraicGeometry.smooth_of_isLocallyFree_relativeDifferentials_of_perfectField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/LocallyFreeDifferentialsPerfectField.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/LocallyFreeDifferentialsPerfectField.lean#L230). References: EGA IV (17.15.6), “perfect k, reduced X”; SGA 1 II (5.7), “k perfect, X reduced”; SGA 1 II (5.5), “(ii)=>(i), X reduced”.

> **Stacks Project, Tag 04QP.** A reduced scheme locally of finite type over a perfect field
> is smooth if its sheaf of relative differentials is locally free.

```lean
theorem smooth_of_isLocallyFree_relativeDifferentials_of_perfectField
    {k : Type u} [Field k] [PerfectField k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [IsReduced X] [LocallyOfFiniteType f]
    (hΩ : _root_.SheafOfModules.IsLocallyFree.{u, u, u} f.relativeDifferentials) :
    Smooth f
```

## Tag 056S, a lemma

[Tag 056S](https://stacks.math.columbia.edu/tag/056S) in the Stacks Project.

**`AlgebraicGeometry.isRegular_of_smooth_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Smooth/Regular.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Smooth/Regular.lean#L42). References: EGA IV (17.15.2), “smooth ⇒ regular”.

> **Stacks Project, Tag 056S.** A scheme smooth over a field is regular.

```lean
public theorem isRegular_of_smooth_over_field
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [Smooth f] :
    IsRegular X
```

## Tag 056T, a lemma

[Tag 056T](https://stacks.math.columbia.edu/tag/056T) in the Stacks Project.

**`AlgebraicGeometry.isGeometricallyRegular_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Smooth/GeometricallyRegularNormal.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Smooth/GeometricallyRegularNormal.lean#L83). The attribute's comment: “geometrically regular”. References: EGA IV (17.15.2), “necessity”; EGA IV (17.5.2), “field base, smooth⇒reg”; SGA 1 II (3.1), “base a field, regular”; SGA 3 XI (1.2), “Proposition 1.2(i)”.

> **Stacks Project, Tag 056T**, the geometric-regularity conclusion: a scheme smooth over a
> field `k` is geometrically regular over `k`.
>
> Proved at every point of the base change, not only at the points lying over the given point.

```lean
public theorem isGeometricallyRegular_of_smooth {k : Type u} [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [Smooth f] : IsGeometricallyRegular f
```

**`AlgebraicGeometry.isGeometricallyNormal_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Smooth/GeometricallyRegularNormal.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Smooth/GeometricallyRegularNormal.lean#L94). The attribute's comment: “geometrically normal”. References: EGA IV (7.3.9), “special case”; SGA 1 II (3.1), “base a field, normal”.

> **Stacks Project, Tag 056T**, the geometric-normality conclusion: a scheme smooth over a
> field `k` is geometrically normal over `k`.

```lean
public theorem isGeometricallyNormal_of_smooth {k : Type u} [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [Smooth f] : IsGeometricallyNormal f
```

**`AlgebraicGeometry.geometricallyReduced_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/GeometricallyReducedFibres.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/GeometricallyReducedFibres.lean#L82). The attribute's comment: “geometrically reduced”. References: EGA IV (17.15.2), “smooth ⇒ reduced”; EGA IV (7.3.9), “special case”; SGA 1 II (3.1), “base a field, reduced”.

> **Stacks Project, Tag 056T**, the geometric-reducedness conclusion: a smooth morphism of
> schemes is geometrically reduced, that is, its base change to every field-valued point of the
> target is a reduced scheme.
>
> The source fixes a field `k` as the base; no base field is needed, a morphism `Spec K ⟶ Spec k`
> being the same thing as a field extension of `k`.

```lean
public theorem geometricallyReduced_of_smooth {X Y : Scheme.{u}} (f : X ⟶ Y) [Smooth f] :
    GeometricallyReduced f
```

## Tag 055T, a lemma

[Tag 055T](https://stacks.math.columbia.edu/tag/055T) in the Stacks Project.

**`AlgebraicGeometry.exists_closedPoint_finite_separable_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/SeparableClosedPoints.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/SeparableClosedPoints.lean#L54).

> **Stacks Project, Tag 055T.** A nonempty open subset of affine space over a field contains
> a closed point whose residue field is a finite separable extension of the field.

```lean
theorem exists_closedPoint_finite_separable_residueField
    {k : Type u} [Field k] {d : ℕ}
    (W : Set (AffineSpace (ULift.{u} (Fin d)) (Spec (.of k))))
    (hWopen : IsOpen W) (hWnonempty : W.Nonempty) :
    ∃ w : AffineSpace (ULift.{u} (Fin d)) (Spec (.of k)),
      w ∈ W ∧ w ∈ closedPoints (AffineSpace (ULift.{u} (Fin d)) (Spec (.of k))) ∧
        let X := AffineSpace (ULift.{u} (Fin d)) (Spec (.of k))
        let f := X ↘ Spec (.of k)
        letI := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation w).hom.toAlgebra
        Module.Finite k (X.residueField w) ∧
          Algebra.IsSeparable k (X.residueField w)
```

## Tag 056U, a lemma

[Tag 056U](https://stacks.math.columbia.edu/tag/056U) in the Stacks Project.

**`AlgebraicGeometry.dense_closedPoints_with_finite_separable_residueField_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/DenseSeparableClosedPoints.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/DenseSeparableClosedPoints.lean#L142).

> **Stacks Project, Tag 056U.** If `X` is smooth over a field `k`, then the closed points of
> `X` whose residue fields are finite separable extensions of `k` are dense in `X`.

```lean
theorem dense_closedPoints_with_finite_separable_residueField_of_smooth
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [Smooth f] :
    Dense {x : X | x ∈ closedPoints X ∧
      letI := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x).hom.toAlgebra
      Module.Finite k (X.residueField x) ∧
        Algebra.IsSeparable k (X.residueField x)}
```

## Tag 056V, a lemma

[Tag 056V](https://stacks.math.columbia.edu/tag/056V) in the Stacks Project.

**`AlgebraicGeometry.geometricallyReduced_iff_exists_dense_open_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Smooth/DenseSmoothOpen.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Smooth/DenseSmoothOpen.lean#L88). References: EGA IV (17.15.12), “X reduced, 1st equiv”.

> A reduced scheme locally of finite type over a field is geometrically reduced if and only if
> it contains a dense open subscheme smooth over that field.

```lean
public theorem geometricallyReduced_iff_exists_dense_open_smooth
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [IsReduced X] [LocallyOfFiniteType f] :
    GeometricallyReduced f ↔
      ∃ U : X.Opens, Dense (U : Set X) ∧ Smooth (U.ι ≫ f)
```

## Tag 0B8X, a lemma

[Tag 0B8X](https://stacks.math.columbia.edu/tag/0B8X) in the Stacks Project.

**`AlgebraicGeometry.smoothAt_locus_eq_regular_locus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Smooth/SmoothLocus.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Smooth/SmoothLocus.lean#L64). The attribute's comment: “equality of the smooth and regular loci”. References: EGA IV (17.15.2), “k perfect case”; EGA 0 (19.0.2), “more general”; EGA IV (17.15.5), “special case”; SGA 1 II (5.4), “perfect k”; SGA 6 XIV (4.2), “Clause”.

> Over a perfect field, the points where a locally finite type scheme is smooth are exactly
> the points whose local rings are regular.

```lean
public theorem smoothAt_locus_eq_regular_locus
    (k : Type u) [Field k] [PerfectField k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] :
    {x : X | InfinitesimalLifting.SmoothAt f x} =
      {x : X | IsRegularLocalRing (X.presheaf.stalk x)}
```

**`AlgebraicGeometry.isOpen_smoothAt_locus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Smooth/SmoothLocus.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Smooth/SmoothLocus.lean#L103). The attribute's comment: “openness of the smooth locus”.

> The locus where a morphism of schemes is smooth is open.

```lean
public theorem isOpen_smoothAt_locus
    {X S : Scheme.{u}} (f : X ⟶ S) :
    IsOpen {x : X | InfinitesimalLifting.SmoothAt f x}
```

**`AlgebraicGeometry.dense_smoothAt_locus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Smooth/SmoothLocus.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Smooth/SmoothLocus.lean#L121). The attribute's comment: “density of the smooth locus”. References: SGA 4½ Th finitude (2.7), “Perfect-field clause”.

> Over a perfect field, the points where a reduced scheme locally of finite type is smooth are
> dense.

```lean
public theorem dense_smoothAt_locus
    (k : Type u) [Field k] [PerfectField k] {X : Scheme.{u}} [IsReduced X]
    (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] :
    Dense {x : X | InfinitesimalLifting.SmoothAt f x}
```

**`AlgebraicGeometry.smoothAt_locus_eq_regular_locus_and_isOpen_and_dense`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Smooth/SmoothLocus.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Smooth/SmoothLocus.lean#L142). References: EGA 0 (19.0.2), “IV, special case”; EGA IV (17.15.12), “special case”; EGA IV (6.12.5), “special case”; EGA IV (6.8.7), “special case”; EGA IV (7.8.3), “(iv), openness of Reg(X)”; EGA IV (7.8.6), “(iii), special case”; SGA 1 II (4.14), “special case”; SGA 1 II (5.4), “more general”; SGA 4½ Th finitude (2.7), “Perfect-field clause”; SGA 6 XIV (4.2), “Clause”.

> Let `k` be a perfect field and let `X` be a reduced scheme locally of finite type over `k`.
> Then the set of points at which `X` is smooth over `k` is the set of points whose local ring is
> regular, and that set is a dense open subset of `X`.

```lean
public theorem smoothAt_locus_eq_regular_locus_and_isOpen_and_dense
    (k : Type u) [Field k] [PerfectField k] {X : Scheme.{u}} [IsReduced X]
    (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] :
    {x : X | InfinitesimalLifting.SmoothAt f x} =
        {x : X | IsRegularLocalRing (X.presheaf.stalk x)} ∧
      IsOpen {x : X | InfinitesimalLifting.SmoothAt f x} ∧
      Dense {x : X | InfinitesimalLifting.SmoothAt f x}
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Hom.dense_smoothLocus_of_perfectField`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.dense_smoothLocus_of_perfectField#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/Smooth/SmoothLocus.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Smooth/SmoothLocus.lean#L38) (StacksFrontier): “density of the smooth locus”. References: EGA IV (17.15.12), “special case”; EGA IV (17.15.13), “special case”; SGA 4½ Th finitude (2.7), “Perfect-field clause”.

## Tag 05AX, a lemma

[Tag 05AX](https://stacks.math.columbia.edu/tag/05AX) in the Stacks Project.

**`AlgebraicGeometry.smoothAt_of_flatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Smooth/FlatDescent.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Smooth/FlatDescent.lean#L44). The attribute's comment: “pointwise statement”.

> Smoothness over a field descends at a point through a morphism which is flat there, provided
> both schemes are locally of finite type over the field.

```lean
public theorem smoothAt_of_flatAt
    {k : Type u} [Field k] {X Y : Scheme.{u}} (f : X ⟶ Y)
    (p : Y ⟶ Spec (.of k)) [LocallyOfFiniteType (f ≫ p)] [LocallyOfFiniteType p]
    (x : X) (hX : InfinitesimalLifting.SmoothAt (f ≫ p) x)
    (hf : AlgebraicGeometry.IsFlatAt f.toLRSHom.toShHom x) :
    InfinitesimalLifting.SmoothAt p (f x)
```

**`AlgebraicGeometry.smooth_of_flat_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Smooth/FlatDescent.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Smooth/FlatDescent.lean#L59). The attribute's comment: “global consequence”.

> A flat surjective image of a scheme smooth over a field is smooth, when both schemes are
> locally of finite type over that field.

```lean
public theorem smooth_of_flat_of_surjective
    {k : Type u} [Field k] {X Y : Scheme.{u}} (f : X ⟶ Y)
    (p : Y ⟶ Spec (.of k)) [LocallyOfFiniteType p] [Smooth (f ≫ p)]
    [Flat f] [Surjective f] : Smooth p
```

## Tag 0CDW, a lemma

[Tag 0CDW](https://stacks.math.columbia.edu/tag/0CDW) in the Stacks Project.

**`AlgebraicGeometry.geometricallyIntegral_of_isVariety_of_smoothAt_rationalPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/SmoothRationalPoint.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/SmoothRationalPoint.lean#L81).

> **Stacks Project, Tag 0CDW.** A variety over a field with a rational point at which its
> structure morphism is smooth is geometrically integral.

```lean
theorem geometricallyIntegral_of_isVariety_of_smoothAt_rationalPoint
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsVariety k f]
    (s : Spec (.of k) ⟶ X) (hs : s ≫ f = 𝟙 _)
    (hsm : InfinitesimalLifting.SmoothAt f (s.base (genericPoint (Spec (.of k))))) :
    GeometricallyIntegral f
```

## Tag 0H3W, a lemma

[Tag 0H3W](https://stacks.math.columbia.edu/tag/0H3W) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_purelyInseparable_extension_smooth_stratification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/SmoothStratification.lean, line 728](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/SmoothStratification.lean#L728). References: EGA IV (17.15.13).

> A finite-type scheme over a field has a finite smooth stratification after a finite purely
> inseparable extension of the field.

```lean
theorem exists_finite_purelyInseparable_extension_smooth_stratification
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [QuasiCompact f] :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k k')
      (_ : Module.Finite k k') (_ : IsPurelyInseparable k k'),
      let g : Spec (.of k') ⟶ Spec (.of k) :=
        Spec.map (CommRingCat.ofHom (algebraMap k k'))
      let Y : Scheme.{u} := pullback f g
      let p : Y ⟶ Spec (.of k') := pullback.snd f g
      ∃ (t : ℕ) (Z : Fin (t + 1) → Y.IdealSheafData),
        Z 0 = Scheme.IdealSheafData.vanishingIdeal (⊤ : Closeds Y) ∧
        Z ⟨t, Nat.lt_succ_self t⟩ = ⊤ ∧
        (∀ i : Fin t, Z i.castSucc ≤ Z i.succ) ∧
        (∀ i : Fin t, ∃ U : (Z i.castSucc).subscheme.Opens,
          (U : Set (Z i.castSucc).subscheme) =
            {x | (Z i.castSucc).subschemeι x ∉ (Z i.succ).support} ∧
          Smooth (U.ι ≫ (Z i.castSucc).subschemeι ≫ p))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.25, Tag 04QM](https://stacks.math.columbia.edu/tag/04QM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
