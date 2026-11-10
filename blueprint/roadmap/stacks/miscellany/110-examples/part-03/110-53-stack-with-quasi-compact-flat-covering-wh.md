---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isFiniteType_of_smoothSchemeCovering_classifyingStack
statement: formalized
proof: formalized
---

# 110.53 Stack with quasi-compact flat covering which is not algebraic

Section 110.53 of the Stacks Project, [Tag 04AG](https://stacks.math.columbia.edu/tag/04AG). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04AH, a lemma

[Tag 04AH](https://stacks.math.columbia.edu/tag/04AH) in the Stacks Project.

**`AlgebraicGeometry.Stack.isFiniteType_of_smoothSchemeCovering_classifyingStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/ClassifyingStackSmoothCovering.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Stacks/ClassifyingStackSmoothCovering.lean#L125). The attribute's comment: “conditional on Stacks 04WZ, that the diagonal of a quotient stack is representable by algebraic spaces, and on the implication of Stacks 06PL that an algebraic classifying stack has a group locally of finite presentation over the base”.

> **Stacks 04AH.** Let `k` be a field and let `G` be an affine group scheme over `k`. If the
> classifying stack `[Spec(k)/G]` has a smooth surjective covering by a scheme, then `G` is of
> finite type over `k`.
>
> The covering hypothesis is the third clause of Stacks 026O for the classifying stack. The
> hypotheses `hdiag` and `hfp` are Stacks 04WZ and the forward implication of Stacks 06PL, which
> this library does not have.

```lean
theorem isFiniteType_of_smoothSchemeCovering_classifyingStack
    (G : Space.GroupAlgebraicSpace C (Spec (.of k)) hk
      (Space.terminalSpace C (Spec (.of k)) hk).obj
      (Space.terminalSpace C (Spec (.of k)) hk).property)
    (hAffine : Space.IsAffineHom C (Spec (.of k)) hk G.obj.X.hom)
    (hdiag : HasRepresentableDiagonal C (Spec (.of k)) hk (classifyingStack C hk G))
    (hfp : IsAlgebraicStack.{u, u} C (Spec (.of k)) hk (classifyingStack C hk G).val →
      Space.IsLocallyOfFinitePresentation C (Spec (.of k)) hk G.obj.X.hom)
    (hcov :
      ∃ (U : BigFppfOver C (Spec (.of k)) hk)
        (f : (schemeFibredCategory C (Spec (.of k)) hk U).val ⥤ᵇ
          (classifyingStack C hk G).val),
        IsRepresentableByAlgebraicSpaces C (Spec (.of k)) hk f ∧
          ∀ (V : BigFppfOver C (Spec (.of k)) hk)
            (y : BigFppfOver C V.left.1 V.left.2 ⥤ (classifyingStack C hk G).val.obj)
            (_hy : y ⋙ (classifyingStack C hk G).val.p = Over.map V.hom)
            (F : (BigFppfOver C V.left.1 V.left.2)ᵒᵖ ⥤ Type u)
            (hF : IsAlgebraicSpace C V.left.1 V.left.2 F),
            Nonempty (StacksRepresentableCFG.EquivalenceOver
              (TwoFibreProductOver.fst (Over.map V.hom)
                (schemeFibredCategory C (Spec (.of k)) hk U).val.p
                (classifyingStack C hk G).val.p y f.toFunctor)
              (presheafOfCategories (F ⋙ typeToCat)).p) →
              (let g := (algebraicSpaceMap C (Spec (.of k)) hk V
                ((spacesOverSmallerBaseFunctor C V.left.1 (Spec (.of k)) V.left.2 hk
                  V.hom).obj ⟨F, hF⟩)).hom
               Space.IsSurjective C (Spec (.of k)) hk g ∧
                 Space.IsSmooth C (Spec (.of k)) hk g)) :
    Space.IsFiniteType C (Spec (.of k)) hk G.obj.X.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.53, Tag 04AG](https://stacks.math.columbia.edu/tag/04AG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
