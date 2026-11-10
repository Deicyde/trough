---
declaration: section
origin: cited
lean: CategoryTheory.FilteredDerived.PerfectHomotopyCategory, CategoryTheory.FilteredDerived.perfectComplexFunctor, CategoryTheory.FilteredDerived.perfectComplexFunctorFullyFaithful, CategoryTheory.FilteredDerived.isPerfect_iff, CategoryTheory.FilteredDerived.PerfectDerivedCategory, CategoryTheory.FilteredDerived.perfectDerivedTrace_eq_alternatingTrace
statement: formalized
proof: formalized
---

# 64.10 Perfectness

Section 64.10 of the Stacks Project, [Tag 03TG](https://stacks.math.columbia.edu/tag/03TG). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03TH, a definition

[Tag 03TH](https://stacks.math.columbia.edu/tag/03TH) in the Stacks Project.

**`CategoryTheory.FilteredDerived.PerfectHomotopyCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Perfectness/Basic.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Perfectness/Basic.lean#L73). The attribute's comment: “the category K_perf”. References: SGA 4½ Rapport (4.3), “K_parf(Λ)”.

> The category `K_perf(R)` of bounded complexes of finite projective `R`-modules, with
> morphisms up to homotopy.

```lean
public abbrev PerfectHomotopyCategory (R : Type u) [Ring R]
```

**`CategoryTheory.FilteredDerived.perfectComplexFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Perfectness/Basic.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Perfectness/Basic.lean#L78). The attribute's comment: “the functor to D(R)”.

> The canonical functor from `K_perf(R)` to `D(R)`.

```lean
public def perfectComplexFunctor (R : Type u) [Ring R] :
    PerfectHomotopyCategory.{u, v} R ⥤ DerivedCategory (ModuleCat.{v} R)
```

**`CategoryTheory.FilteredDerived.perfectComplexFunctorFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Perfectness/Basic.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Perfectness/Basic.lean#L111). The attribute's comment: “full faithfulness”. References: SGA 4 XVII (5.5.6.3), “more general”; SGA 4½ Rapport (4.3); SGA 6 I (4.10), “Clause (i), special case”; SGA 6 I (4.12.2), “Case C = R-modules”; SGA 6 II (1.1), “c), special case”.

> The canonical functor from perfect complexes up to homotopy to the derived category is fully
> faithful.

```lean
public def perfectComplexFunctorFullyFaithful (R : Type u) [Ring R] :
    (perfectComplexFunctor.{u, v} R).FullyFaithful
```

**`CategoryTheory.FilteredDerived.isPerfect_iff`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Perfectness/Basic.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Perfectness/Basic.lean#L142). The attribute's comment: “perfect objects”. References: SGA 4½ Rapport (4.3), “D_parf(Λ)”.

> A derived object is perfect exactly when it is isomorphic to the image of a bounded
> complex of finite projective modules.

```lean
public lemma isPerfect_iff (R : Type u) [Ring R]
    (X : DerivedCategory (ModuleCat.{v} R)) :
    StacksDraft.Perfect.IsPerfect X ↔
      ∃ K : CochainComplex (ModuleCat.{v} R) ℤ,
        finiteProjectiveComplex.{u, v} R K ∧ Nonempty (DerivedCategory.Q.obj K ≅ X)
```

**`CategoryTheory.FilteredDerived.PerfectDerivedCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Perfectness/Basic.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Perfectness/Basic.lean#L178). The attribute's comment: “the category D_perf”. References: SGA 4½ Rapport (4.3), “D_parf(Λ)”.

> The full subcategory `D_perf(R)` of perfect derived objects.

```lean
public abbrev PerfectDerivedCategory (R : Type u) [Ring R]
```

## Tag 03TI, a proposition

[Tag 03TI](https://stacks.math.columbia.edu/tag/03TI) in the Stacks Project.

**`CategoryTheory.FilteredDerived.perfectDerivedTrace_eq_alternatingTrace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Perfectness/Trace.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Perfectness/Trace.lean#L276).

> The trace of an endomorphism of a perfect derived object is computed on any bounded
> finite-projective representative, and hence is independent of the representative, the chosen
> isomorphism, and the cochain map representing the endomorphism.

```lean
public theorem perfectDerivedTrace_eq_alternatingTrace (R : Type u) [Ring R]
    (K : PerfectDerivedCategory.{u, v} R) (f : K.obj ⟶ K.obj)
    (P : CochainComplex (ModuleCat.{v} R) ℤ)
    (hP : finiteProjectiveComplex R P)
    (e : DerivedCategory.Q.obj P ≅ K.obj) (g : P ⟶ P)
    (hg : DerivedCategory.Q.map g = e.hom ≫ f ≫ e.inv) :
    perfectDerivedTrace R K f = alternatingTrace R P hP g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.10, Tag 03TG](https://stacks.math.columbia.edu/tag/03TG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
