---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_open_ncard_irreducibleComponents_fiber_ge, AlgebraicGeometry.geometricallyIrreducibleFiberLocus_baseChange, AlgebraicGeometry.geometricallyIrreducibleFiberLocus_eq_preimage_of_isPullback, AlgebraicGeometry.geometricIrreducibleComponentCount, AlgebraicGeometry.encard_irreducibleComponents_geometricFiber, AlgebraicGeometry.geometricIrreducibleComponentCount_pullback, MvPolynomial.exists_away_irreducible_map, AlgebraicGeometry.geometricallyIrreducibleAfterShrinking
statement: formalized
proof: formalized
---

# 37.27 Irreducible components of fibres

Section 37.27 of the Stacks Project, [Tag 0553](https://stacks.math.columbia.edu/tag/0553). 7 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0554, a lemma

[Tag 0554](https://stacks.math.columbia.edu/tag/0554) in the Stacks Project.

**`AlgebraicGeometry.exists_open_ncard_irreducibleComponents_fiber_ge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NowhereDenseFibres/ComponentCount.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NowhereDenseFibres/ComponentCount.lean#L257). References: EGA IV (9.7.1), “irreducible components”.

> **Stacks Project, Tag 0554.** For a finite type morphism to a scheme with a chosen dense
> generic point, the number of irreducible components of the fibres is at least the number for
> the generic fibre over a nonempty open subset of the base.

```lean
theorem exists_open_ncard_irreducibleComponents_fiber_ge {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [QuasiCompact f] (η : Y) (hη : IsGenericPoint η Set.univ)
    (n : ℕ) (hcomp : (irreducibleComponents (f.fiber η)).ncard = n) :
    ∃ V : Set Y, IsOpen V ∧ V.Nonempty ∧
      ∀ y ∈ V, n ≤ (irreducibleComponents (f.fiber y)).ncard
```

## Tag 0555, a lemma

[Tag 0555](https://stacks.math.columbia.edu/tag/0555) in the Stacks Project.

**`AlgebraicGeometry.geometricallyIrreducibleFiberLocus_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/IrreducibleComponents.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/IrreducibleComponents.lean#L193). The attribute's comment: “the locus pulls back under the chosen fibre product”.

> **Stacks Project, Tag 0555.** The points with geometrically irreducible fibre pull back
> exactly under an arbitrary base change.

```lean
theorem geometricallyIrreducibleFiberLocus_baseChange
    {X Y Y' : Scheme.{u}} (f : X ⟶ Y) (g : Y' ⟶ Y) :
    {y' : Y' | GeometricallyIrreducible
      ((pullback.snd f g).fiberToSpecResidueField y')} =
      g ⁻¹' {y : Y | GeometricallyIrreducible (f.fiberToSpecResidueField y)}
```

**`AlgebraicGeometry.geometricallyIrreducibleFiberLocus_eq_preimage_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/IrreducibleComponents.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/IrreducibleComponents.lean#L205). The attribute's comment: “the locus pulls back under an arbitrary cartesian square”.

> **Stacks Project, Tag 0555.** The points with geometrically irreducible fibre pull back
> exactly under an arbitrary cartesian square, not only under the chosen fibre product.

```lean
theorem geometricallyIrreducibleFiberLocus_eq_preimage_of_isPullback
    {X Y X' Y' : Scheme.{u}} (f : X ⟶ Y) (f' : X' ⟶ Y') (i : X' ⟶ X) (g : Y' ⟶ Y)
    (h : IsPullback i f' f g) :
    {y' : Y' | GeometricallyIrreducible (f'.fiberToSpecResidueField y')} =
      g ⁻¹' {y : Y | GeometricallyIrreducible (f.fiberToSpecResidueField y)}
```

## Tag 0556, a lemma

[Tag 0556](https://stacks.math.columbia.edu/tag/0556) in the Stacks Project.

**`AlgebraicGeometry.geometricIrreducibleComponentCount`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/IrreducibleComponents.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/IrreducibleComponents.lean#L114). The attribute's comment: “the function”. References: EGA IV (4.5.2), “more general”; EGA IV (4.7.4), “more general”.

> The number, as an extended natural number, of geometrically irreducible components of each
> fibre of a morphism of schemes.

```lean
def geometricIrreducibleComponentCount {X Y : Scheme.{u}} (f : X ⟶ Y) : Y → ℕ∞
```

**`AlgebraicGeometry.encard_irreducibleComponents_geometricFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/IrreducibleComponents.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/IrreducibleComponents.lean#L121). The attribute's comment: “well-definedness”. References: EGA IV (4.5.1), “partial”.

> The number of irreducible components of the geometric fibre can be computed after extension
> to any separably closed field containing the residue field.

```lean
theorem encard_irreducibleComponents_geometricFiber {X Y : Scheme.{u}} (f : X ⟶ Y)
    (y : Y) (K : Type u) [Field K] [Algebra (Y.residueField y) K] [IsSepClosed K] :
    (irreducibleComponents (geometricFiber f y K)).encard =
      geometricIrreducibleComponentCount f y
```

**`AlgebraicGeometry.geometricIrreducibleComponentCount_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/IrreducibleComponents.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/IrreducibleComponents.lean#L158). The attribute's comment: “base change”.

> Formation of the function counting geometrically irreducible components of fibres commutes
> with arbitrary base change.

```lean
theorem geometricIrreducibleComponentCount_pullback {X Y Y' : Scheme.{u}}
    (f : X ⟶ Y) (g : Y' ⟶ Y) :
    geometricIrreducibleComponentCount (pullback.snd f g) =
      geometricIrreducibleComponentCount f ∘ g
```

## Tag 0557, a lemma

[Tag 0557](https://stacks.math.columbia.edu/tag/0557) in the Stacks Project.

**`MvPolynomial.exists_away_irreducible_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/PolynomialIrreducibility.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/PolynomialIrreducibility.lean#L313). References: EGA IV (9.7.5); EGA IV (9.7.4), “c ⇒ b”.

> **Stacks Project, Tag 0557.** An absolutely irreducible polynomial over a domain
> remains irreducible under every specialization to a field after restricting to a
> nonempty principal open subset.

```lean
theorem exists_away_irreducible_map
    (A : Type u) [CommRing A] [IsDomain A]
    (K : Type v) [Field K] [Algebra A K] [IsFractionRing A K]
    (Kbar : Type w) [Field Kbar] [Algebra K Kbar] [IsAlgClosed Kbar]
    (ι : Type x) [Finite ι] (P : MvPolynomial ι A)
    (hP : Irreducible (P.map ((algebraMap K Kbar).comp (algebraMap A K)))) :
    ∃ f : A, f ≠ 0 ∧
      ∀ (κ : Type y) [Field κ] (φ : Localization.Away f →+* κ),
        Irreducible (P.map (φ.comp (algebraMap A (Localization.Away f))))
```

## Tag 0559, a lemma

[Tag 0559](https://stacks.math.columbia.edu/tag/0559) in the Stacks Project.

**`AlgebraicGeometry.geometricallyIrreducibleAfterShrinking`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/GenericResidueField.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/GenericResidueField.lean#L336).

> **Stacks Project, Tag 0559.** A morphism of finite type onto an irreducible base whose
> fibre over the generic point is geometrically irreducible has geometrically irreducible fibres
> over a nonempty open subscheme of the base.

```lean
theorem geometricallyIrreducibleAfterShrinking :
    GeometricallyIrreducibleAfterShrinking.{u}
```

## Tag 055A, a lemma

[Tag 055A](https://stacks.math.columbia.edu/tag/055A) in the Stacks Project.

**`AlgebraicGeometry.exists_open_geometricIrreducibleComponentCount_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean#L60).

> **Stacks Project, Tag 055A.** The number of geometrically irreducible components of the
> fibres of a finite type morphism is constant on a nonempty open subset of the closure of any
> point of the target.

```lean
theorem exists_open_geometricIrreducibleComponentCount_constant {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [QuasiCompact f] (y : Y) :
    ∃ V : Opens (↑(closure ({y} : Set Y))), Nonempty V ∧
      ∃ n : ℕ∞, ∀ z : V, geometricIrreducibleComponentCount f z.1.1 = n
```

## Tag 055B, a lemma

[Tag 055B](https://stacks.math.columbia.edu/tag/055B) in the Stacks Project.

**`AlgebraicGeometry.isLocallyConstructible_level_geometricIrreducibleComponentCount`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean#L70). References: EGA IV (9.7.9), “n(s) (irreducible)”; SGA 4 XIV (1.11), “special case”.

> **Stacks Project, Tag 055B.** Every level set of the number of geometrically irreducible
> components of the fibres of a morphism of finite presentation is locally constructible.

```lean
theorem isLocallyConstructible_level_geometricIrreducibleComponentCount {X Y : Scheme.{u}}
    (f : X ⟶ Y) (hf : FinitePresentation f) (n : ℕ∞) :
    IsLocallyConstructible {y : Y | geometricIrreducibleComponentCount f y = n}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.27, Tag 0553](https://stacks.math.columbia.edu/tag/0553)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
