---
declaration: section
origin: cited
lean: AlgebraicGeometry.isOpenImmersion_curvesSubstackInclusion_and_factors_iff
statement: formalized
proof: formalized
---

# 109.6 Open substacks of the stack of curves

Section 109.6 of the Stacks Project, [Tag 0E0E](https://stacks.math.columbia.edu/tag/0E0E). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E0E, the section

[Tag 0E0E](https://stacks.math.columbia.edu/tag/0E0E) in the Stacks Project.

**`AlgebraicGeometry.isOpenImmersion_curvesSubstackInclusion_and_factors_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesOpenSubstack.lean, line 376](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesOpenSubstack.lean#L376). The attribute's comment: “the open substack Curves^P cut out by a property P with condition (o), and its universal property (1); part (2) is the special case of (1) at the family of a proper scheme of dimension at most one over a field”.

> **Stacks 0E0E.** For a property `P` of families of curves satisfying condition (o):
> `Curves^P ⊂ Curves` is an open substack — `P` is invariant under isomorphism, and the inclusion
> is representable by algebraic spaces and an open immersion — and the classifying morphism of a
> family factors through `Curves^P` exactly when the family has `P`.

```lean
theorem isOpenImmersion_curvesSubstackInclusion_and_factors_iff
    (hP : IsOpenCurvesLocus B hZ P) :
    (P.IsClosedUnderIsomorphisms ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ P hP.prop_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ (curvesSubstackInclusion B hZ P hP.prop_of_hom)) ∧
    ∀ (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤ P.FullSubcategory, z ⋙ P.ι = y) ↔
        P (y.obj (Over.mk (𝟙 U.left))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.6, Tag 0E0E](https://stacks.math.columbia.edu/tag/0E0E)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
