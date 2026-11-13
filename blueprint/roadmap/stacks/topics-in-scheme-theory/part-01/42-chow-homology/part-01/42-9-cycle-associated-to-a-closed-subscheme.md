---
declaration: section
origin: cited
lean: Stacks.Chow.isGenericPoint_component_of_relativeDimension_eq, AlgebraicGeometry.isFiniteLength_stalk_of_isGenericPoint_component, Stacks.Chow.componentMultiplicity, Stacks.Chow.cycleAssociatedToClosedSubscheme, Stacks.Chow.cycleAssociatedToClosedSubscheme_apply, Stacks.Chow.cycleAssociatedToClosedSubscheme_apply_eq_zero
statement: formalized
proof: formalized
---

# 42.9 Cycle associated to a closed subscheme

Section 42.9 of the Stacks Project, [Tag 02QS](https://stacks.math.columbia.edu/tag/02QS). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02QT, a lemma

[Tag 02QT](https://stacks.math.columbia.edu/tag/02QT) in the Stacks Project.

**`Stacks.Chow.isGenericPoint_component_of_relativeDimension_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/MaximalDeltaDimension.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/CoherentCycle/MaximalDeltaDimension.lean#L118). The attribute's comment: “maximal\_delta\_component”.

> A point of a closed subscheme `i : Z ⟶ X` attaining an upper bound for the delta-dimension
> of `Z` is the generic point of an irreducible component of `Z`.

```lean
theorem isGenericPoint_component_of_relativeDimension_eq (C : ChowSituation.{u})
    {X Z : Scheme.{u}} (f : X ⟶ C.S) [LocallyOfFiniteType f] (i : Z ⟶ X) [IsClosedImmersion i]
    {k : ℤ} (hZ : schemeDeltaDimension C (i ≫ f) ≤ (k : EInt)) (ξ : Z)
    (hξ : relativeDimension C.dimensionFunction f (i ξ) = k) :
    ∃ W : irreducibleComponents Z, IsGenericPoint ξ (W : Set Z)
```

**`AlgebraicGeometry.isFiniteLength_stalk_of_isGenericPoint_component`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CycleAssociatedClosed/Basic.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/CycleAssociatedClosed/Basic.lean#L48). The attribute's comment: “finite\_multiplicity”.

> **Stacks Project, Tag 02QT.** At the generic point of an irreducible component of a closed
> subscheme, its local ring has finite length over the ambient local ring.

```lean
lemma isFiniteLength_stalk_of_isGenericPoint_component
    (C : Stacks.Chow.ChowSituation.{u}) {X Z : Scheme.{u}}
    (f : X ⟶ C.S) [LocallyOfFiniteType f]
    (i : Z ⟶ X) [IsClosedImmersion i]
    (Z' : Set Z) (hZ' : Z' ∈ irreducibleComponents Z)
    (ξ : Z) (hξ : IsGenericPoint ξ Z') :
    letI : Module (X.presheaf.stalk (i ξ)) (Z.presheaf.stalk ξ) :=
      Module.compHom (Z.presheaf.stalk ξ) (i.stalkMap ξ).hom
    IsFiniteLength (X.presheaf.stalk (i ξ)) (Z.presheaf.stalk ξ)
```

## Tag 02QU, a definition

[Tag 02QU](https://stacks.math.columbia.edu/tag/02QU) in the Stacks Project.

**`Stacks.Chow.componentMultiplicity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean#L77). The attribute's comment: “part (1): multiplicity”.

> **Stacks 02QU.** The multiplicity of an irreducible component of a closed subscheme,
> computed at its generic point as the length of the stalk of the subscheme over the stalk of the
> ambient scheme.

```lean
def componentMultiplicity {X Z : Scheme.{u}} (i : Z ⟶ X) [IsClosedImmersion i]
    (ξ : genericPoints Z) : ℤ
```

**`Stacks.Chow.cycleAssociatedToClosedSubscheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean#L137). The attribute's comment: “part (2): associated cycle”.

> **Stacks 02QU.** The `k`-cycle `[Z]_k` associated to a closed subscheme `i : Z ⟶ X`: the
> coefficient of each irreducible component of delta-dimension `k` is its multiplicity.

```lean
def cycleAssociatedToClosedSubscheme (C : ChowSituation.{u}) {X Z : Scheme.{u}} (f : X ⟶ C.S)
    [LocallyOfFiniteType f] (i : Z ⟶ X) [IsClosedImmersion i] (k : ℤ) : CycleGroup C f k
```

**`Stacks.Chow.cycleAssociatedToClosedSubscheme_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean#L144). The attribute's comment: “coefficient formula”.

> **Stacks 02QU.** At the image of the generic point of a component of delta-dimension `k`,
> the associated cycle has that component's multiplicity as coefficient.

```lean
theorem cycleAssociatedToClosedSubscheme_apply (C : ChowSituation.{u}) {X Z : Scheme.{u}}
    (f : X ⟶ C.S) [LocallyOfFiniteType f] (i : Z ⟶ X) [IsClosedImmersion i] (k : ℤ)
    (ξ : genericPoints Z)
    (hξ : relativeDimension C.dimensionFunction f (i ξ.1) = k) :
    (cycleAssociatedToClosedSubscheme C f i k).1 (i ξ.1) = componentMultiplicity i ξ
```

**`Stacks.Chow.cycleAssociatedToClosedSubscheme_apply_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean#L161). The attribute's comment: “zero coefficients”.

> **Stacks 02QU.** A point that is not the image of the generic point of a component of
> delta-dimension `k` has coefficient zero in the associated cycle.

```lean
theorem cycleAssociatedToClosedSubscheme_apply_eq_zero (C : ChowSituation.{u})
    {X Z : Scheme.{u}} (f : X ⟶ C.S) [LocallyOfFiniteType f] (i : Z ⟶ X)
    [IsClosedImmersion i] (k : ℤ) (x : X)
    (hx : ¬ ∃ ξ : genericPoints Z,
      i ξ.1 = x ∧ relativeDimension C.dimensionFunction f x = k) :
    (cycleAssociatedToClosedSubscheme C f i k).1 x = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.9, Tag 02QS](https://stacks.math.columbia.edu/tag/02QS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
