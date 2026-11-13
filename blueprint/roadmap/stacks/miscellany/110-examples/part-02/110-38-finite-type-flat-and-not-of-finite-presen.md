---
declaration: section
origin: cited
lean: Stacks.Examples.exists_flat_finiteType_not_finitePresentation_of_curve_fibers, Stacks.Examples.exists_proper_flat_not_finitePresentation_with_nodal_or_line_fibers, Stacks.Examples.exists_proper_flat_not_finitePresentation_with_projectiveSpace_fibers, Stacks.Examples.exists_flat_finiteType_not_finitePresentation_with_completeIntersection_fibers
statement: formalized
proof: formalized
---

# 110.38 Finite type, flat and not of finite presentation

Section 110.38 of the Stacks Project, [Tag 05LB](https://stacks.math.columbia.edu/tag/05LB). 1 tag here is carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05LC, a lemma

[Tag 05LC](https://stacks.math.columbia.edu/tag/05LC) in the Stacks Project.

**`Stacks.Examples.exists_flat_finiteType_not_finitePresentation_of_curve_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/AffineCurveNotFinitePresentation.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Flatness/AffineCurveNotFinitePresentation.lean#L226). The attribute's comment: “(2)”.

> A flat algebra of finite type with geometrically
> connected and geometrically reduced one-dimensional complete-intersection fibres need not be
> of finite presentation.

```lean
theorem exists_flat_finiteType_not_finitePresentation_of_curve_fibers :
    ∃ (R : Type u) (A : Type v) (_ : CommRing R) (_ : CommRing A)
      (_ : Algebra R A),
      Module.Flat R A ∧ Algebra.FiniteType R A ∧ ¬ Algebra.FinitePresentation R A ∧
        (∀ (p : Ideal R) [p.IsPrime],
          Algebra.IsGeometricallyConnected p.ResidueField (p.Fiber A) ∧
          Algebra.IsGeometricallyReduced p.ResidueField (p.Fiber A) ∧
          ringKrullDim (p.Fiber A) = 1 ∧
          IsGlobalCompleteIntersection p.ResidueField (p.Fiber A))
```

**`Stacks.Examples.exists_proper_flat_not_finitePresentation_with_nodal_or_line_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/ProjFamilyNotFinitePresentation.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Flatness/ProjFamilyNotFinitePresentation.lean#L338). The attribute's comment: “(3)”.

> There is a proper flat morphism of schemes, not locally of finite presentation, each of whose
> fibres is either a projective line or the vanishing locus of `X₁X₂` in the projective plane over
> the residue field of its point.

```lean
theorem exists_proper_flat_not_finitePresentation_with_nodal_or_line_fibers :
    ∃ (R : Type u) (_ : CommRing R) (X : Scheme.{u}) (f : X ⟶ Spec (CommRingCat.of R)),
      IsProper f ∧ AlgebraicGeometry.Flat f ∧ ¬ LocallyOfFinitePresentation f ∧
        ∀ (p : Ideal R) [p.IsPrime],
          (∃ g : projectiveSpaceOverRing 1 (CommRingCat.of p.ResidueField) ⟶ X,
            IsPullback g
              (projectiveSpaceOverRing 1 (CommRingCat.of p.ResidueField) ↘
                Spec (CommRingCat.of p.ResidueField))
              f (Spec.map (CommRingCat.ofHom (algebraMap R p.ResidueField)))) ∨
          (∃ g : monomialPairLocus p.ResidueField 2 1 (Fin.last 2) ⟶ X,
            IsPullback g (monomialPairLocusToSpec p.ResidueField 2 1 (Fin.last 2)) f
              (Spec.map (CommRingCat.ofHom (algebraMap R p.ResidueField))))
```

**`Stacks.Examples.exists_proper_flat_not_finitePresentation_with_projectiveSpace_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/ProjFamilyNotFinitePresentation.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Flatness/ProjFamilyNotFinitePresentation.lean#L370). The attribute's comment: “(4)”.

> There is a proper flat morphism of schemes, not locally of finite presentation, each of whose
> fibres is either a projective line or a projective plane over the residue field of its point.

```lean
theorem exists_proper_flat_not_finitePresentation_with_projectiveSpace_fibers :
    ∃ (R : Type u) (_ : CommRing R) (X : Scheme.{u}) (f : X ⟶ Spec (CommRingCat.of R)),
      IsProper f ∧ AlgebraicGeometry.Flat f ∧ ¬ LocallyOfFinitePresentation f ∧
        ∀ (p : Ideal R) [p.IsPrime],
          (∃ g : projectiveSpaceOverRing 1 (CommRingCat.of p.ResidueField) ⟶ X,
            IsPullback g
              (projectiveSpaceOverRing 1 (CommRingCat.of p.ResidueField) ↘
                Spec (CommRingCat.of p.ResidueField))
              f (Spec.map (CommRingCat.ofHom (algebraMap R p.ResidueField)))) ∨
          (∃ g : projectiveSpaceOverRing 2 (CommRingCat.of p.ResidueField) ⟶ X,
            IsPullback g
              (projectiveSpaceOverRing 2 (CommRingCat.of p.ResidueField) ↘
                Spec (CommRingCat.of p.ResidueField))
              f (Spec.map (CommRingCat.ofHom (algebraMap R p.ResidueField))))
```

**`Stacks.Examples.exists_flat_finiteType_not_finitePresentation_with_completeIntersection_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/SquareZeroNotFinitePresentation.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Flatness/SquareZeroNotFinitePresentation.lean#L219). The attribute's comment: “(1)”.

> A flat ring map of finite type can have geometrically irreducible complete-intersection
> fibres without being of finite presentation.

```lean
theorem exists_flat_finiteType_not_finitePresentation_with_completeIntersection_fibers :
    ∃ (R S : Type u) (_ : CommRing R) (_ : CommRing S) (f : R →+* S),
      f.Flat ∧ f.FiniteType ∧ ¬ f.FinitePresentation ∧
        (letI := f.toAlgebra
         ∀ (p : Ideal R) [p.IsPrime],
           letI : Algebra p.ResidueField (S ⊗[R] p.ResidueField) :=
             Algebra.TensorProduct.rightAlgebra
           Algebra.IsGeometricallyIrreducible p.ResidueField
               (S ⊗[R] p.ResidueField) ∧
             IsGlobalCompleteIntersection p.ResidueField
               (S ⊗[R] p.ResidueField))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.38, Tag 05LB](https://stacks.math.columbia.edu/tag/05LB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
