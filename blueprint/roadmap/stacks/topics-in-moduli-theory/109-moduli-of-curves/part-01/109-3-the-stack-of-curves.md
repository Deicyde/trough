---
declaration: section
origin: cited
lean: AlgebraicGeometry.relativeCurvesMorphismsEquivalence, AlgebraicGeometry.curvesMorphismsEquivalence, AlgebraicGeometry.relativeCurvesMorphismsCurveFamilyEquivalence
statement: formalized
proof: formalized
---

# 109.3 The stack of curves

Section 109.3 of the Stacks Project, [Tag 0DMJ](https://stacks.math.columbia.edu/tag/0DMJ). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DMK, a lemma

[Tag 0DMK](https://stacks.math.columbia.edu/tag/0DMK) in the Stacks Project.

**`AlgebraicGeometry.relativeCurvesMorphismsEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesMorphismsFromSpace.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesMorphismsFromSpace.lean#L324). The attribute's comment: “the identification of Mor\_B(T, B-Curves) with Mor(T, Curves)”.

> **Stacks 0DMK, the identification `Mor_B(T, B-Curves) = Mor(T, Curves)`.** For a morphism
> `f : T → A` of algebraic spaces, the category of morphisms over `(Sch/A)` from `T` to the stack
> `A-Curves` is equivalent to the category of morphisms over the big fppf site from `T` to the stack
> of curves, by forgetting the morphisms of the bases to `A`.

```lean
def relativeCurvesMorphismsEquivalence {T A : AlgebraicSpaces B integerBase hZ} (f : T ⟶ A) :
    (schemesOverSpaceBasedOver B hZ f ⥤ᵇ curvesOverSpaceBased B hZ A) ≌
      (schemesOverSpaceBased B hZ T ⥤ᵇ (curvesFiberedCategory B hZ).val)
```

**`AlgebraicGeometry.curvesMorphismsEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesMorphismsFromSpace.lean, line 428](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesMorphismsFromSpace.lean#L428). The attribute's comment: “Mor(T, Curves) is the category of families of curves over the algebraic space T”.

> **Stacks 0DMK, `Mor(T, Curves)` is the category of families of curves over `T`.** For an
> algebraic space `T`, the category of morphisms over the big fppf site from `T` (read as the
> category `(Sch/T)` of schemes with a morphism to `T`) to the stack of curves is equivalent to the
> category of families of curves over `T`: morphisms of algebraic spaces `X ⟶ T` which are flat,
> proper, of finite presentation and of relative dimension at most one, with the isomorphisms over
> `T` as morphisms. A family `X ⟶ T` corresponds to the morphism sending `U ⟶ T` to the family of
> curves `U ×_T X ⟶ U`.

```lean
noncomputable def curvesMorphismsEquivalence (T : AlgebraicSpaces B integerBase hZ) :
    (schemesOverSpaceBased B hZ T ⥤ᵇ (curvesFiberedCategory B hZ).val) ≌
      CurveFamilyOnSpace B integerBase hZ T
```

**`AlgebraicGeometry.relativeCurvesMorphismsCurveFamilyEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesMorphismsFromSpace.lean, line 442](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesMorphismsFromSpace.lean#L442). The attribute's comment: “Mor\_B(T, B-Curves) = Mor(T, Curves) is the category of families of curves over T”.

> **Stacks 0DMK.** For a morphism `f : T ⟶ A` of algebraic spaces, the category
> `Mor_A(T, A-Curves)` of morphisms over `(Sch/A)` from `T` to the stack `A-Curves` is equivalent to
> `Mor(T, Curves)` (`AlgebraicGeometry.relativeCurvesMorphismsEquivalence`), and both are the
> category of families of curves over `T`.

```lean
noncomputable def relativeCurvesMorphismsCurveFamilyEquivalence
    {T A : AlgebraicSpaces B integerBase hZ} (f : T ⟶ A) :
    (schemesOverSpaceBasedOver B hZ f ⥤ᵇ curvesOverSpaceBased B hZ A) ≌
      CurveFamilyOnSpace B integerBase hZ T
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.3, Tag 0DMJ](https://stacks.math.columbia.edu/tag/0DMJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
