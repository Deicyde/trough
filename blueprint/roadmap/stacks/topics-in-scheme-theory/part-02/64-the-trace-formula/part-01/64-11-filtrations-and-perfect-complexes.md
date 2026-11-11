---
declaration: section
origin: cited
lean: CategoryTheory.FilteredDerived.perfectDerivedTrace_eq_sum_grDF, CategoryTheory.FilteredDerived.projectiveModuleTrace_eq_sum_grP
statement: formalized
proof: formalized
---

# 64.11 Filtrations and perfect complexes

Section 64.11 of the Stacks Project, [Tag 03TJ](https://stacks.math.columbia.edu/tag/03TJ). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03TK, a lemma

[Tag 03TK](https://stacks.math.columbia.edu/tag/03TK) in the Stacks Project.

**`CategoryTheory.FilteredDerived.perfectDerivedTrace_eq_sum_grDF`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Perfectness/FilteredTrace.lean, line 507](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Perfectness/FilteredTrace.lean#L507). References: SGA 4½ Rapport (4.4), “(4.4.1)”; SGA 5 IIIB (5.6), “(5.6.5), F = A”.

> **Stacks 03TK.** Trace is additive along the filtration of a perfect
> filtered derived complex.

```lean
public theorem perfectDerivedTrace_eq_sum_grDF (R : Type u) [Ring R]
    (K : FilteredPerfectData.{u, v} R) (f : K.obj ⟶ K.obj) :
    perfectDerivedTrace R
      ⟨(CochainComplex.FilteredDerivedCategory.forgetDF).obj K.obj,
        K.forgetPerfect R⟩
      ((CochainComplex.FilteredDerivedCategory.forgetDF).map f) =
      ∑ᶠ p : ℤ, perfectDerivedTrace R
        ⟨(CochainComplex.FilteredDerivedCategory.grDF p).obj K.obj,
          K.gradedPerfect R p⟩
        ((CochainComplex.FilteredDerivedCategory.grDF p).map f)
```

## Tag 03TL, a lemma

[Tag 03TL](https://stacks.math.columbia.edu/tag/03TL) in the Stacks Project.

**`CategoryTheory.FilteredDerived.projectiveModuleTrace_eq_sum_grP`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Perfectness/FilteredModuleTrace.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Perfectness/FilteredModuleTrace.lean#L132). References: SGA 4½ Rapport (4.2), “(4.2.2) ungraded”; SGA 5 IIIB (5.6), “special case”.

> The trace of a filtered endomorphism of a finite projective module is the sum of the traces on
> its associated graded pieces.

```lean
public theorem projectiveModuleTrace_eq_sum_grP (R : Type u) [Ring R]
    (P : FiniteFilteredObject (ModuleCat.{max u v} R))
    (hP : IsFilteredFiniteProjective P)
    (f : P ⟶ P) :
    (letI : Module.Finite R ((FiniteFilteredObject.forget
          (𝒜 := ModuleCat.{max u v} R)).obj P) :=
        hP.finite_projective_forget.1;
      letI : Module.Projective R ((FiniteFilteredObject.forget
          (𝒜 := ModuleCat.{max u v} R)).obj P) :=
        hP.finite_projective_forget.2;
      Stacks.Trace.projectiveModuleTrace R
        ((FiniteFilteredObject.forget (𝒜 := ModuleCat.{max u v} R)).obj P)
        ((FiniteFilteredObject.forget (𝒜 := ModuleCat.{max u v} R)).map f).hom) =
      ∑ᶠ p : ℤ,
        (letI : Projective ((FiniteFilteredObject.grP
            (𝒜 := ModuleCat.{max u v} R) p).obj P) := (hP p).2;
          letI : Module.Finite R ((FiniteFilteredObject.grP
              (𝒜 := ModuleCat.{max u v} R) p).obj P) := (hP p).1;
          letI : Module.Projective R ((FiniteFilteredObject.grP
              (𝒜 := ModuleCat.{max u v} R) p).obj P) := inferInstance;
          Stacks.Trace.projectiveModuleTrace R
            ((FiniteFilteredObject.grP (𝒜 := ModuleCat.{max u v} R) p).obj P)
            ((FiniteFilteredObject.grP (𝒜 := ModuleCat.{max u v} R) p).map f).hom)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.11, Tag 03TJ](https://stacks.math.columbia.edu/tag/03TJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
