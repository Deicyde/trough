---
declaration: section
origin: cited
lean: Stacks.DifferentialGradedModule.DeltaFunctor.exists_deltaFunctorStructure_δ_eq, DifferentialGradedModule.canonicalDeltaFunctorStructure, DifferentialGradedModule.canonicalDeltaFunctorStructure_δ_eq, DifferentialGradedModule.isHomotopyColimit_toDerivedCategory_obj_colimit
statement: formalized
proof: formalized
---

# 22.23 The canonical delta-functor

Section 22.23 of the Stacks Project, [Tag 09KZ](https://stacks.math.columbia.edu/tag/09KZ). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09L0, a lemma

[Tag 09L0](https://stacks.math.columbia.edu/tag/09L0) in the Stacks Project.

**`Stacks.DifferentialGradedModule.DeltaFunctor.exists_deltaFunctorStructure_δ_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/DeltaFunctor.lean, line 506](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/DeltaFunctor.lean#L506).

> **Stacks Project, Tag 09L0.** The canonical functor from differential graded modules to
> their derived category is a `δ`-functor, with connecting arrow the third arrow of the cone
> triangle read after inverting the cone-to-quotient quasi-isomorphism.

```lean
theorem exists_deltaFunctorStructure_δ_eq :
    ∃ h : (canonicalFunctor.{u, v, w} A).DeltaFunctorStructure
        (DifferentialGradedModule.{u, v, w} A) (derivedCategory.{u, v, w} A),
      ∀ (S : ShortComplex (DifferentialGradedModule.{u, v, w} A)) (hS : S.ShortExact),
        ∃ q : coneModule S.f ⟶ S.X₃,
          (∀ x : (coneModule S.f).M,
            q.toFun x = S.g.toFun ((cone S.f).coordinates x).1) ∧
          (coneInclusion S.f ≫ q = S.g) ∧
          quasiIsomorphisms A ((toHomotopyCategory A).map q) ∧
          ∃ _ : IsIso ((canonicalFunctor A).map q),
            h.δ hS =
              inv ((canonicalFunctor A).map q) ≫
                (quasiIsomorphisms A).Q.map (coneTriangle S.f).mor₃ ≫
                  ((quasiIsomorphisms A).Q.commShiftIso (1 : ℤ)).hom.app
                    ((toHomotopyCategory A).obj S.X₁)
```

**`DifferentialGradedModule.canonicalDeltaFunctorStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CanonicalDeltaFunctor.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/CanonicalDeltaFunctor.lean#L304). The attribute's comment: “the delta-functor structure”.

> *"Let `(A, d)` be a differential graded algebra. The functor `Mod_{(A, d)} → D(A, d)` has the
> natural structure of a `δ`-functor."* The connecting morphism is
> `DifferentialGradedModule.shortExactδ`, identified with `- p ∘ q⁻¹` in
> `DifferentialGradedModule.canonicalDeltaFunctorStructure_δ_eq`.

```lean
def canonicalDeltaFunctorStructure (A : DifferentialGradedAlgebra R) :
    (toDerivedCategory A).DeltaFunctorStructure (DifferentialGradedModule A)
      (derivedCategory A)
```

**`DifferentialGradedModule.canonicalDeltaFunctorStructure_δ_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CanonicalDeltaFunctor.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/CanonicalDeltaFunctor.lean#L372). The attribute's comment: “the connecting morphism”.

> The formula for the connecting morphism of the canonical `δ`-functor structure:
> *"`δ_{K → L → M} = - p ∘ q⁻¹` with `p` and `q` as explained above"*. Here `q` is the comparison
> `C(f) ⟶ M`, which on the underlying module `L × K` is `(l, k) ↦ g l` and restricts along the
> inclusion of `L` to `g`, and which is invertible in `D(A, d)`; and `- p` is the third morphism of
> the cone triangle, the *signed* cone projection `C(f) ⟶ K[1]`.

```lean
theorem canonicalDeltaFunctorStructure_δ_eq
    {S : ShortComplex (DifferentialGradedModule A)} (hS : S.ShortExact) :
    (∀ x : (coneObject S.f).M, (coneDescShortComplex S).toFun x = S.g.toFun x.1) ∧
      coneIncl S.f ≫ coneDescShortComplex S = S.g ∧
      ∃ _ : IsIso ((toDerivedCategory A).map (coneDescShortComplex S)),
        (canonicalDeltaFunctorStructure A).δ hS =
          inv ((toDerivedCategory A).map (coneDescShortComplex S)) ≫
            (quasiIsomorphisms A).Q.map (coneTriangle S.f).mor₃ ≫
              ((quasiIsomorphisms A).Q.commShiftIso (1 : ℤ)).hom.app
                ((toHomotopyCategory A).obj S.X₁)
```

## Tag 0CRL, a lemma

[Tag 0CRL](https://stacks.math.columbia.edu/tag/0CRL) in the Stacks Project.

**`DifferentialGradedModule.isHomotopyColimit_toDerivedCategory_obj_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedColimits.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedColimits.lean#L298).

> Let `(A, d)` be a differential graded algebra and `Mₙ` a system of differential graded
> modules. Then the derived colimit `hocolim Mₙ` in `D(A, d)` is represented by the differential
> graded module `colim Mₙ`.

```lean
theorem isHomotopyColimit_toDerivedCategory_obj_colimit
    (A : DifferentialGradedAlgebra.{u, u} R) (F : ℕ ⥤ DifferentialGradedModule.{u, u, u} A) :
    IsHomotopyColimit (F ⋙ toDerivedCategory A) ((toDerivedCategory A).obj (colimit F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.23, Tag 09KZ](https://stacks.math.columbia.edu/tag/09KZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
