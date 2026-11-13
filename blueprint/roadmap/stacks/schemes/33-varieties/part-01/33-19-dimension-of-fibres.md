---
declaration: section
origin: cited
lean: AlgebraicGeometry.topologicalKrullDimAt_fiber_eq_of_target_dim_le_one, AlgebraicGeometry.specialFiber_equidimensional, AlgebraicGeometry.topologicalKrullDim_specialFiber_eq_genericFiber, AlgebraicGeometry.topologicalKrullDimAt_fiber_add_one_le_of_genericPoints
statement: formalized
proof: formalized
---

# 33.19 Dimension of fibres

Section 33.19 of the Stacks Project, [Tag 0B2H](https://stacks.math.columbia.edu/tag/0B2H). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B2I, a lemma

[Tag 0B2I](https://stacks.math.columbia.edu/tag/0B2I) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDimAt_fiber_eq_of_target_dim_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/HigherCodimension.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/HigherCodimension.lean#L366). References: EGA IV (7.1.13).

> **Stacks Project, Tag 0B2I.** If the local ring of the target at `y` is Noetherian of
> dimension at most one, and the fibre dimension at every generic point of an irreducible
> component of `X` through `x` is `d`, then the fibre dimension at `x` is `d`.

```lean
theorem topologicalKrullDimAt_fiber_eq_of_target_dim_le_one (f : X ⟶ Y) [LocallyOfFiniteType f]
    (x : X) (hY : IsNoetherianRing (Y.presheaf.stalk (f x)))
    (hYdim : ringKrullDim (Y.presheaf.stalk (f x)) ≤ 1) (d : ℕ)
    (hgeneric : ∀ η : X, closure {η} ∈ irreducibleComponents X → x ∈ closure {η} →
      topologicalKrullDimAt (f.fiber (f η)) (f.asFiber η) = d) :
    topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) = d
```

## Tag 0B2J, a lemma

[Tag 0B2J](https://stacks.math.columbia.edu/tag/0B2J) in the Stacks Project.

**`AlgebraicGeometry.specialFiber_equidimensional`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ValuationFibreDimension.lean, line 498](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ValuationFibreDimension.lean#L498). The attribute's comment: “equidimensionality”.

> **Stacks Project, Tag 0B2J (equidimensionality).** The special fibre of a surjective,
> locally finite type morphism from an irreducible scheme to the spectrum of a valuation ring is
> equidimensional.

```lean
lemma specialFiber_equidimensional {R : Type u} [CommRing R] [IsDomain R] [ValuationRing R]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of R)) [IrreducibleSpace X]
    [LocallyOfFiniteType f] [Surjective f] :
    TopologicalSpace.Equidimensional
      (f.fiber (⟨IsLocalRing.maximalIdeal R, inferInstance⟩ : PrimeSpectrum R))
```

**`AlgebraicGeometry.topologicalKrullDim_specialFiber_eq_genericFiber`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ValuationFibreDimension.lean, line 527](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ValuationFibreDimension.lean#L527). The attribute's comment: “equality of fibre dimensions”. References: EGA IV (14.3.10), “surjective f”; SGA 3 XXV (4.3), “special case”.

> **Stacks Project, Tag 0B2J (dimension).** The special and generic fibres of a surjective,
> locally finite type morphism from an irreducible scheme to the spectrum of a valuation ring
> have the same dimension.

```lean
lemma topologicalKrullDim_specialFiber_eq_genericFiber
    {R : Type u} [CommRing R] [IsDomain R] [ValuationRing R]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of R)) [IrreducibleSpace X]
    [LocallyOfFiniteType f] [Surjective f] :
    topologicalKrullDim
        (f.fiber (⟨IsLocalRing.maximalIdeal R, inferInstance⟩ : PrimeSpectrum R)) =
      topologicalKrullDim (f.fiber (⟨⊥, inferInstance⟩ : PrimeSpectrum R))
```

## Tag 0B2K, a lemma

[Tag 0B2K](https://stacks.math.columbia.edu/tag/0B2K) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDimAt_fiber_add_one_le_of_genericPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/HigherCodimension.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/HigherCodimension.lean#L216).

> **Stacks Project, Tag 0B2K.** The dimension at a point of a fibre is bounded by the
> generic fibre dimension plus the dimension of the base local ring minus one, provided every
> irreducible component through the point dominates a nonclosed generalization of its image.

```lean
theorem topologicalKrullDimAt_fiber_add_one_le_of_genericPoints (f : X ⟶ Y)
    [LocallyOfFiniteType f] (x : X) [IsNoetherianRing (Y.presheaf.stalk (f x))] (d : ℕ)
    (h : ∀ Z ∈ irreducibleComponents X, x ∈ Z → ∀ η : X, IsGenericPoint η Z →
      (f η ≠ f x ∧
        topologicalKrullDimAt (f.fiber (f η)) (f.asFiber η) = (d : WithBot ℕ∞))) :
    topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) + 1 ≤
      (d : WithBot ℕ∞) + ringKrullDim (Y.presheaf.stalk (f x))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.19, Tag 0B2H](https://stacks.math.columbia.edu/tag/0B2H)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
