---
declaration: section
origin: cited
lean: AlgebraicGeometry.universallyOpen_iff_forall_isOpenMap_pullback_snd, AlgebraicGeometry.universallyOpen_iff_forall_isOpenMap_affineSpaceMap, AlgebraicGeometry.universallyOpen_of_locallyQuasiFinite_of_dominant_components, AlgebraicGeometry.universallyOpen_iff_isOpen_image_basicOpen_linearCombination, AlgebraicGeometry.exists_locallyQuasiFinite_universallyOpen_baseChange_of_limitBaseChange, AlgebraicGeometry.geometricIrreducibleComponentCount_eq_numGeometricConnectedComponents, AlgebraicGeometry.exists_forall_geometricIrreducibleComponentCount_le, AlgebraicGeometry.exists_isGreatest_range_geometricIrreducibleComponentCount
statement: formalized
proof: formalized
---

# 37.74 Universally open morphisms

Section 37.74 of the Stacks Project, [Tag 0F30](https://stacks.math.columbia.edu/tag/0F30). 7 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F31, a lemma

[Tag 0F31](https://stacks.math.columbia.edu/tag/0F31) in the Stacks Project.

**`AlgebraicGeometry.universallyOpen_iff_forall_isOpenMap_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyOpen/Criteria.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyOpen/Criteria.lean#L314). The attribute's comment: “parts (1) and (2)”.

> A morphism of schemes is universally open if and only if its base change along every
> morphism locally of finite presentation is an open map.

```lean
theorem universallyOpen_iff_forall_isOpenMap_pullback_snd {X S : Scheme.{u}} (f : X ⟶ S) :
    UniversallyOpen f ↔
      ∀ (S' : Scheme.{u}) (g : S' ⟶ S),
        LocallyOfFinitePresentation g → IsOpenMap (pullback.snd f g)
```

**`AlgebraicGeometry.universallyOpen_iff_forall_isOpenMap_affineSpaceMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyOpen/Criteria.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyOpen/Criteria.lean#L325). The attribute's comment: “parts (1) and (3)”.

> A morphism of schemes is universally open if and only if the induced morphism of affine
> `n`-spaces is an open map for every `n`.

```lean
theorem universallyOpen_iff_forall_isOpenMap_affineSpaceMap {X S : Scheme.{u}} (f : X ⟶ S) :
    UniversallyOpen f ↔
      ∀ n : ℕ, IsOpenMap (AffineSpace.map (ULift.{u} (Fin n)) f)
```

## Tag 0F32, a lemma

[Tag 0F32](https://stacks.math.columbia.edu/tag/0F32) in the Stacks Project.

**`AlgebraicGeometry.universallyOpen_of_locallyQuasiFinite_of_dominant_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyOpen/QuasiFiniteDominant.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyOpen/QuasiFiniteDominant.lean#L417). References: EGA IV (14.4.5), “quasi-finite case”; EGA IV (14.4.2), “quasi-finite, b)=>a)”; EGA IV (14.4.4), “loc. quasi-finite case”; EGA IV (14.5.6), “(d) ⇒ (b)”; EGA IV (14.5.9), “(d) ⇒ (a), special case”; EGA IV (18.10.2), “special case”; SGA 3 VIB (5.6.0), “(i), (ii), special case”.

> **Stacks Project, Tag 0F32.** A locally quasi-finite morphism to a geometrically unibranch,
> locally Noetherian scheme is universally open as soon as every irreducible component of its
> source dominates an irreducible component of its target.

```lean
theorem universallyOpen_of_locallyQuasiFinite_of_dominant_components
    {X Y : Scheme.{u}} (f : X ⟶ Y) [LocallyOfFiniteType f] [LocallyQuasiFinite f]
    [IsLocallyNoetherian Y] (hY : IsGeometricallyUnibranch Y)
    (hcomponents : ∀ C : irreducibleComponents X,
      ∃ D : irreducibleComponents Y, closure (f '' (C : Set X)) = (D : Set Y)) :
    UniversallyOpen f
```

## Tag 0F33, a lemma

[Tag 0F33](https://stacks.math.columbia.edu/tag/0F33) in the Stacks Project.

**`AlgebraicGeometry.universallyOpen_iff_isOpen_image_basicOpen_linearCombination`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/UniversallyOpenFinite.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/UniversallyOpenFinite.lean#L162).

> Universal openness of a finite algebra is detected by the image of the
> principal open defined by a universal linear combination of module generators.

```lean
theorem universallyOpen_iff_isOpen_image_basicOpen_linearCombination
    (A B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (d : ℕ) (b : Fin d → B) (hb : Submodule.span A (Set.range b) = ⊤) :
    UniversallyOpen (Spec.map (CommRingCat.ofHom (algebraMap A B))) ↔
      IsOpen (PrimeSpectrum.comap (MvPolynomial.map (σ := Fin d) (algebraMap A B)) ''
        (PrimeSpectrum.basicOpen
          (∑ i : Fin d, MvPolynomial.C (b i) * MvPolynomial.X i) :
            Set (PrimeSpectrum (MvPolynomial (Fin d) B))))
```

## Tag 0F34, a lemma

[Tag 0F34](https://stacks.math.columbia.edu/tag/0F34) in the Stacks Project.

**`AlgebraicGeometry.exists_locallyQuasiFinite_universallyOpen_baseChange_of_limitBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/UniversallyOpen.lean, line 829](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/UniversallyOpen.lean#L829).

> Let `S` be the limit of a cofiltered system of schemes with affine transition morphisms and
> `f₀ : X₀ ⟶ Y₀` a locally finitely presented morphism over a quasi-compact quasi-separated stage
> `S i₀`, with `X₀`, `Y₀` quasi-compact and quasi-separated. If the base change of `f₀` to the limit
> is locally of finite type, locally quasi-finite and universally open, then so is its base change
> to some stage `S i`.

```lean
public theorem exists_locallyQuasiFinite_universallyOpen_baseChange_of_limitBaseChange
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    (S : I ⥤ Scheme.{u})
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (S.map g)]
    (c : Cone S) (hc : IsLimit c) (i₀ : I)
    (X₀ Y₀ : Over (S.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [CompactSpace (S.obj i₀)] [QuasiSeparatedSpace (S.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFinitePresentation f₀.left]
    [LocallyOfFiniteType ((Over.pullback (c.π.app i₀)).map f₀).left]
    [LocallyQuasiFinite ((Over.pullback (c.π.app i₀)).map f₀).left]
    [UniversallyOpen ((Over.pullback (c.π.app i₀)).map f₀).left] :
    ∃ (i : I) (g : i ⟶ i₀),
      (LocallyOfFiniteType ((Over.pullback (S.map g)).map f₀).left ∧
        LocallyQuasiFinite ((Over.pullback (S.map g)).map f₀).left) ∧
          UniversallyOpen ((Over.pullback (S.map g)).map f₀).left
```

## Tag 0F35, a lemma

[Tag 0F35](https://stacks.math.columbia.edu/tag/0F35) in the Stacks Project.

**`AlgebraicGeometry.geometricIrreducibleComponentCount_eq_numGeometricConnectedComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/GeometricFibreCount.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/GeometricFibreCount.lean#L112). The attribute's comment: “agreement”.

> For a locally quasi-finite morphism, the functions counting geometrically irreducible and
> geometrically connected components of its fibres agree.

```lean
theorem geometricIrreducibleComponentCount_eq_numGeometricConnectedComponents
    {X Y : Scheme.{u}} (f : X ⟶ Y) [LocallyQuasiFinite f] :
    geometricIrreducibleComponentCount f =
      numGeometricConnectedComponents f
```

**`AlgebraicGeometry.exists_forall_geometricIrreducibleComponentCount_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/GeometricFibreCount.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/GeometricFibreCount.lean#L162). The attribute's comment: “boundedness”.

> The geometric fibre count of a locally quasi-finite morphism whose source is quasi-compact
> is bounded by a natural number.

```lean
theorem exists_forall_geometricIrreducibleComponentCount_le {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [LocallyQuasiFinite f] [CompactSpace X] :
    ∃ d : ℕ, ∀ y : Y, geometricIrreducibleComponentCount f y ≤ (d : ℕ∞)
```

**`AlgebraicGeometry.exists_isGreatest_range_geometricIrreducibleComponentCount`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/GeometricFibreCount.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/GeometricFibreCount.lean#L176). The attribute's comment: “maximum, the target is assumed nonempty”.

> The geometric fibre count of a locally quasi-finite morphism whose source is quasi-compact
> and whose target is nonempty attains a finite maximum: its set of values has a greatest element.

```lean
theorem exists_isGreatest_range_geometricIrreducibleComponentCount {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [LocallyQuasiFinite f] [CompactSpace X] [Nonempty Y] :
    ∃ d : ℕ, IsGreatest (Set.range (geometricIrreducibleComponentCount f)) (d : ℕ∞)
```

## Tag 0F36, a lemma

[Tag 0F36](https://stacks.math.columbia.edu/tag/0F36) in the Stacks Project.

**`AlgebraicGeometry.isOpen_geometricIrreducibleComponentCount_ge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyOpen/FibreCountLowerBound.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyOpen/FibreCountLowerBound.lean#L414). References: EGA IV (18.10.17.1), “globally univ. open”; SGA 1 I (10.7), “more general”.

> **Stacks Project, Tag 0F36.** For a separated, locally quasi-finite and universally open
> morphism of schemes, the locus where the number of geometric components of the fibre is at least
> a fixed natural number is open.

```lean
theorem isOpen_geometricIrreducibleComponentCount_ge {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsSeparated f] [LocallyOfFiniteType f] [LocallyQuasiFinite f] [UniversallyOpen f] (d : ℕ) :
    IsOpen {y : Y | (d : ℕ∞) ≤ geometricIrreducibleComponentCount f y}
```

## Tag 0F37, a lemma

[Tag 0F37](https://stacks.math.columbia.edu/tag/0F37) in the Stacks Project.

**`AlgebraicGeometry.isOpen_geometricIrreducibleComponentCount_maxLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyOpen/MaximalFibreCount.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyOpen/MaximalFibreCount.lean#L350). The attribute's comment: “openness”.

> **Stacks Project, Tag 0F37.** For a separated, locally quasi-finite and universally open
> morphism whose geometric fibre count attains the finite maximum `d`, the locus where the count
> equals `d` is open.

```lean
theorem isOpen_geometricIrreducibleComponentCount_maxLocus
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsSeparated f] [LocallyOfFiniteType f]
    [LocallyQuasiFinite f] [UniversallyOpen f] (d : ℕ)
    (hmax : IsGreatest (Set.range (geometricIrreducibleComponentCount f)) (d : ℕ∞)) :
    IsOpen {y : Y | geometricIrreducibleComponentCount f y = (d : ℕ∞)}
```

**`AlgebraicGeometry.isFinite_restrict_geometricIrreducibleComponentCount_maxLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyOpen/MaximalFibreCount.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyOpen/MaximalFibreCount.lean#L362). The attribute's comment: “finiteness”.

> **Stacks Project, Tag 0F37.** The morphism is finite over the open locus where its geometric
> fibre count attains the finite maximum.

```lean
theorem isFinite_restrict_geometricIrreducibleComponentCount_maxLocus
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsSeparated f] [LocallyOfFiniteType f]
    [LocallyQuasiFinite f] [UniversallyOpen f] (d : ℕ)
    (hmax : IsGreatest (Set.range (geometricIrreducibleComponentCount f)) (d : ℕ∞)) :
    IsFinite (f ∣_ ⟨{y : Y | geometricIrreducibleComponentCount f y = (d : ℕ∞)},
      isOpen_geometricIrreducibleComponentCount_maxLocus f d hmax⟩)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.74, Tag 0F30](https://stacks.math.columbia.edu/tag/0F30)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
