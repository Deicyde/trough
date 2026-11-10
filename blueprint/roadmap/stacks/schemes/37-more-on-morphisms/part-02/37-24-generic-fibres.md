---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_open_preimage_eq_bot_of_isEmpty_generic_fiber, AlgebraicGeometry.exists_nonempty_open_surjective_baseChange, AlgebraicGeometry.exists_open_isNowhereDense_fiber, AlgebraicGeometry.exists_open_isSchemeTheoreticallyDense_fiber, AlgebraicGeometry.exists_open_fiber_covered_by_closures, AlgebraicGeometry.comap_nilradical_fiberι, AlgebraicGeometry.exists_finiteUniversalHomeomorphism_geometricallyReduced_genericFiber, AlgebraicGeometry.exists_nonemptyOpen_finiteEtale_cover_geometricallyIrreducible_genericFiber
statement: formalized
proof: formalized
---

# 37.24 Generic fibres

Section 37.24 of the Stacks Project, [Tag 054V](https://stacks.math.columbia.edu/tag/054V). 8 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 054W, a lemma

[Tag 054W](https://stacks.math.columbia.edu/tag/054W) in the Stacks Project.

**`AlgebraicGeometry.exists_open_preimage_eq_bot_of_isEmpty_generic_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ConnectedComponentSection/CoveringFibres.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ConnectedComponentSection/CoveringFibres.lean#L154).

> **Stacks Project, Tag 054W.** Let `f : X ⟶ Y` be a finite type morphism with `Y`
> irreducible with generic point `η`. If the fibre over `η` is empty, then the base change of `f`
> to some nonempty open subset `V` of `Y` is empty, that is, `f ⁻¹ᵁ V = ⊥`.

```lean
theorem exists_open_preimage_eq_bot_of_isEmpty_generic_fiber
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [QuasiCompact f]
    (η : Y) (hη : IsGenericPoint η Set.univ) (hempty : IsEmpty (f.fiber η)) :
    ∃ V : Y.Opens, Nonempty V ∧ f ⁻¹ᵁ V = ⊥
```

## Tag 05F5, a lemma

[Tag 05F5](https://stacks.math.columbia.edu/tag/05F5) in the Stacks Project.

**`AlgebraicGeometry.exists_nonempty_open_surjective_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/Surjective.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/Surjective.lean#L45). References: EGA IV (1.8.6), “first assertion”.

> **Stacks Project, Tag 05F5.** A finite type morphism to an irreducible scheme
> with nonempty generic fibre is surjective over some nonempty open subscheme of
> the target.

```lean
theorem exists_nonempty_open_surjective_baseChange
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IrreducibleSpace Y]
    [LocallyOfFiniteType f] [QuasiCompact f]
    (η : Y) (hη : IsGenericPoint η Set.univ) (h : Nonempty (f.fiber η)) :
    ∃ V : Y.Opens, (V : Set Y).Nonempty ∧ Surjective (pullback.snd f V.ι)
```

## Tag 054X, a lemma

[Tag 054X](https://stacks.math.columbia.edu/tag/054X) in the Stacks Project.

**`AlgebraicGeometry.exists_open_isNowhereDense_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIntegral/NowhereDenseGenericFibre.lean, line 444](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIntegral/NowhereDenseGenericFibre.lean#L444).

> **Stacks Project, Tag 054X.** A closed subset that is nowhere dense in the generic fibre of a
> finite type morphism remains nowhere dense in all fibres over a nonempty open subset of the
> irreducible base.
>
> The base is replaced by its reduction, which is a universal homeomorphism onto it (Stacks 054M),
> so the base change of `f` is a homeomorphism onto `X`; nowhere density in fibres is invariant
> under that, and the reduced base is handled by
> `AlgebraicGeometry.exists_open_isNowhereDense_fiber_of_isReduced`.

```lean
theorem exists_open_isNowhereDense_fiber {X Y : Scheme.{u}} (f : X ⟶ Y) [IrreducibleSpace Y]
    [LocallyOfFiniteType f] [QuasiCompact f] (Z : Set X) (hZ : IsClosed Z) (η : Y)
    (hη : IsGenericPoint η Set.univ) (hηZ : IsNowhereDense ((f.fiberι η) ⁻¹' Z)) :
    ∃ V : Set Y, IsOpen V ∧ V.Nonempty ∧
      ∀ y ∈ V, IsNowhereDense ((f.fiberι y) ⁻¹' Z)
```

## Tag 0573, a lemma

[Tag 0573](https://stacks.math.columbia.edu/tag/0573) in the Stacks Project.

**`AlgebraicGeometry.exists_open_isSchemeTheoreticallyDense_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/SchemeTheoreticDenseFibre.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/SchemeTheoreticDenseFibre.lean#L71).

> **Stacks Project, Tag 0573.** Let `f : X ⟶ Y` be a finite type morphism of schemes with `Y`
> irreducible with generic point `η`, and let `U ⊆ X` be an open subscheme whose trace on the fibre
> over `η` is scheme-theoretically dense there. Then there is a nonempty open `V ⊆ Y` such that the
> trace of `U` on the fibre over `y` is scheme-theoretically dense for every `y ∈ V`.

```lean
public theorem exists_open_isSchemeTheoreticallyDense_fiber {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IrreducibleSpace Y] [LocallyOfFiniteType f] [QuasiCompact f] (U : X.Opens) (η : Y)
    (hη : IsGenericPoint η Set.univ)
    (hηU : Scheme.Opens.IsSchemeTheoreticallyDense (f.fiberι η ⁻¹ᵁ U)) :
    ∃ V : Y.Opens, (V : Set Y).Nonempty ∧ ∀ y ∈ V,
      Scheme.Opens.IsSchemeTheoreticallyDense (f.fiberι y ⁻¹ᵁ U)
```

## Tag 054Y, a lemma

[Tag 054Y](https://stacks.math.columbia.edu/tag/054Y) in the Stacks Project.

**`AlgebraicGeometry.exists_open_fiber_covered_by_closures`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ConnectedComponentSection/CoveringFibres.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ConnectedComponentSection/CoveringFibres.lean#L117).

> **Stacks Project, Tag 054Y.** Let `f : X ⟶ Y` be a finite type morphism with `Y`
> irreducible with generic point `η`. If the subsets `Z i` cover the generic fibre, then over
> some nonempty open subset of `Y` the closures in `X` of their images cover every fibre.

```lean
theorem exists_open_fiber_covered_by_closures
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [QuasiCompact f]
    (η : Y) (hη : IsGenericPoint η Set.univ)
    {ι : Type v}
    (Z : ι → Set (f.fiber η))
    (hcover : ∀ x : f.fiber η, ∃ i, x ∈ Z i) :
    ∃ V : Set Y, IsOpen V ∧ V.Nonempty ∧
      ∀ y ∈ V, ∀ x : f.fiber y,
        ∃ i, f.fiberι y x ∈ closure (f.fiberι η '' Z i)
```

## Tag 054Z, a lemma

[Tag 054Z](https://stacks.math.columbia.edu/tag/054Z) in the Stacks Project.

**`AlgebraicGeometry.comap_nilradical_fiberι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/GenericFibreReduction.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/GenericFibreReduction.lean#L99).

> The reduction of the fibre over a generic point of an irreducible component is the
> base change of the reduction of the source.

```lean
theorem comap_nilradical_fiberι {X Y : Scheme.{u}} (f : X ⟶ Y)
    (η : Y) (hη : η ∈ genericPoints Y) :
    X.nilradical.comap (f.fiberι η) = (f.fiber η).nilradical
```

## Tag 0550, a lemma

[Tag 0550](https://stacks.math.columbia.edu/tag/0550) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteUniversalHomeomorphism_geometricallyReduced_genericFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/GeometricallyReducedGenericFibre.lean, line 978](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/GeometricallyReducedGenericFibre.lean#L978).

> **Stacks Project, Tag 0550.** A finite type morphism over an irreducible
> base admits, locally on the base, a finite universal homeomorphic cover whose
> reduced pullback is flat and finitely presented with geometrically reduced
> generic fibre.

```lean
public theorem exists_finiteUniversalHomeomorphism_geometricallyReduced_genericFiber
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IrreducibleSpace Y]
    [LocallyOfFiniteType f] [QuasiCompact f] :
    ∃ (V : Y.Opens) (_ : V.1.Nonempty)
      (Y' : Scheme.{u}) (g : Y' ⟶ V.toScheme)
      (_ : IsFinite g) (_ : UniversalHomeomorphism g)
      (_ : IsIntegral Y') (_ : IsAffine Y'),
      let X_V := pullback V.ι f
      let P := pullback (g ≫ V.ι) f
      let X' := P.nilradical.subscheme
      let r : X' ⟶ P := P.nilradical.subschemeι
      let f' : X' ⟶ Y' := r ≫ pullback.fst (g ≫ V.ι) f
      let g' : X' ⟶ X_V := pullback.lift
        (f' ≫ g) (r ≫ pullback.snd (g ≫ V.ι) f) (by
          dsimp [f']
          rw [Category.assoc, Category.assoc, pullback.condition]
          rfl)
      IsFinite g' ∧ UniversalHomeomorphism g' ∧ Flat f' ∧
        AlgebraicGeometry.FinitePresentation f' ∧
        ∀ η : Y', IsGenericPoint η Set.univ →
          GeometricallyReduced (f'.fiberToSpecResidueField η)
```

## Tag 0551, a lemma

[Tag 0551](https://stacks.math.columbia.edu/tag/0551) in the Stacks Project.

**`AlgebraicGeometry.exists_nonemptyOpen_finiteEtale_cover_geometricallyIrreducible_genericFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/GeometricallyIrreducible.lean, line 574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/GeometricallyIrreducible.lean#L574).

> **Stacks Project, Tag 0551.** After passing to a nonempty open of an irreducible base, a
> finite type morphism has a finite etale surjective base change from an irreducible affine
> scheme whose generic fibre has geometrically irreducible irreducible components.

```lean
theorem exists_nonemptyOpen_finiteEtale_cover_geometricallyIrreducible_genericFiber
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IrreducibleSpace Y]
    [LocallyOfFiniteType f] [QuasiCompact f] :
    ∃ (V : Y.Opens) (_ : V.1.Nonempty)
      (Y' : Scheme.{u}) (g : Y' ⟶ V.toScheme)
      (_ : Surjective g) (_ : IsFinite g) (_ : Etale g)
      (_ : IrreducibleSpace Y') (_ : IsAffine Y'),
      let X_V := pullback V.ι f
      let fV : X_V ⟶ V.toScheme := pullback.fst V.ι f
      let X' := pullback (g ≫ V.ι) f
      let f' : X' ⟶ Y' := pullback.fst (g ≫ V.ι) f
      let g' : X' ⟶ X_V := pullback.lift
        (pullback.fst (g ≫ V.ι) f ≫ g)
        (pullback.snd (g ≫ V.ι) f) (by
          rw [Category.assoc]
          exact pullback.condition)
      IsPullback g' f' fV g ∧
        Surjective g' ∧ IsFinite g' ∧ Etale g' ∧
        ∀ (η : Y'), IsGenericPoint η Set.univ →
          ∀ Z : irreducibleComponents (f'.fiber η),
            GeometricallyIrreducible
              ((Scheme.IdealSheafData.vanishingIdeal (X := f'.fiber η)
                  ⟨Z.1, isClosed_of_mem_irreducibleComponents Z.1 Z.2⟩).subschemeι ≫
                f'.fiberToSpecResidueField η)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.24, Tag 054V](https://stacks.math.columbia.edu/tag/054V)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
