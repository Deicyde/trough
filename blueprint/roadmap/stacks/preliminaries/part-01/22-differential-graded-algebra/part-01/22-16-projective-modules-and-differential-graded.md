---
declaration: section
origin: cited
lean: Stacks.DifferentialGraded.DGModule.isAdmissibleEpi_of_surjective_of_isProjectiveAsGradedModule, Stacks.DifferentialGraded.HomComplex.DGModule.hom_shift_equiv_cocycles, Stacks.DifferentialGraded.HomComplex.DGModule.homotopyClasses_shift_equiv_cohomology, DifferentialGradedModule.isZero_hom_toHomotopyCategory_shift_regularModule, DifferentialGradedModule.leftOrthogonal_acyclic_toHomotopyCategory_shift_regularModule, DifferentialGradedModule.isZero_hom_shift_regularModule, DifferentialGradedModule.leftOrthogonal_shift_regularModule
statement: formalized
proof: formalized
---

# 22.16 Projective modules and differential graded algebras

Section 22.16 of the Stacks Project, [Tag 0FQB](https://stacks.math.columbia.edu/tag/0FQB). 2 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09K0, a lemma

[Tag 09K0](https://stacks.math.columbia.edu/tag/09K0) in the Stacks Project.

**`Stacks.DifferentialGraded.DGModule.isAdmissibleEpi_of_surjective_of_isProjectiveAsGradedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DifferentialGraded/GradedProjective.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DifferentialGraded/GradedProjective.lean#L75).

> A surjective homomorphism of lawful differential graded modules whose target is
> projective as a graded module is an admissible epimorphism.
>
> The lawfulness of `A` and of `P` is part of the setting of the statement but is not
> needed to produce the splitting.

```lean
theorem isAdmissibleEpi_of_surjective_of_isProjectiveAsGradedModule
    (_hA : A.IsLawful) {M : DGModule.{u, w', v} A} {P : DGModule.{u, w, v} A}
    (hM : M.IsLawful) (_hP : P.IsLawful) (f : DGModule.Hom M P)
    (hf : Function.Surjective f.toFun)
    (hPProjective : IsProjectiveAsGradedModule.{u, v, w, w'} P) :
    DGModule.IsAdmissibleEpi f
```

## Tag 09K1, a lemma

[Tag 09K1](https://stacks.math.columbia.edu/tag/09K1) in the Stacks Project.

**`Stacks.DifferentialGraded.HomComplex.DGModule.hom_shift_equiv_cocycles`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/HomCohomology.lean, line 683](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/HomCohomology.lean#L683).

> **Statement 1.**  Evaluation at the generator `1` gives a natural
> `R`-linear isomorphism
> `Hom_{Mod_{(A,d)}}(A[k], M) ≃ₗ[R] ker(d_M : M^{-k} → M^{-k+1}) = Z^{-k}(M)`,
> sending `f` to `f(1)`.  The first conjunct records that the underlying map is
> `f ↦ f(1)`; the second records naturality in `M`: for any morphism
> `g : M → N`, the square with `cocyclesMap g` commutes.

```lean
theorem hom_shift_equiv_cocycles (M : DGModule A) (k : ℤ) :
    ∃ e : Hom ((A.toDGModule).shift k) M ≃ₗ[R] ↥(M.cocyclesM (-k)),
      (∀ f : Hom ((A.toDGModule).shift k) M, ((e f : M.carrier)) = f.toFun (1 : A.carrier))
      ∧ (∀ (N : DGModule A) (g : Hom M N)
          (eN : Hom ((A.toDGModule).shift k) N ≃ₗ[R] ↥(N.cocyclesM (-k)))
          (_ : ∀ f', ((eN f' : N.carrier)) = f'.toFun (1 : A.carrier))
          (f : Hom ((A.toDGModule).shift k) M),
          eN (g.comp f) = cocyclesMap g (-k) (e f))
```

**`Stacks.DifferentialGraded.HomComplex.DGModule.homotopyClasses_shift_equiv_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/HomCohomology.lean, line 758](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/HomCohomology.lean#L758).

> **Statement 2.**  Passing to homotopy classes, the isomorphism of
> Statement 1 descends to a natural `R`-linear isomorphism
> `Hom_{K(Mod_{(A,d)})}(A[k], M) ≃ₗ[R] H^{-k}(M)`, sending the homotopy class
> `[f]` to the cohomology class of `f(1)`.  Here `hf` is the membership
> `f(1) ∈ Z^{-k}(M)` provided by Statement 1.  The second conjunct records
> naturality in `M`: for any morphism `g : M → N`, the square with the induced
> map `cohomologyMap g` commutes (where the action on homotopy classes is
> `[f] ↦ [g ∘ f]`).

```lean
theorem homotopyClasses_shift_equiv_cohomology (M : DGModule A) (k : ℤ) :
    ∃ e : HomotopyClass ((A.toDGModule).shift k) M ≃ₗ[R] M.cohomology (-k),
      (∀ (f : Hom ((A.toDGModule).shift k) M) (hf : f.toFun (1 : A.carrier) ∈ M.cocyclesM (-k)),
        e (Submodule.Quotient.mk f)
          = Submodule.Quotient.mk (⟨f.toFun (1 : A.carrier), hf⟩ : ↥(M.cocyclesM (-k))))
      ∧ (∀ (N : DGModule A) (g : Hom M N)
          (eN : HomotopyClass ((A.toDGModule).shift k) N ≃ₗ[R] N.cohomology (-k))
          (_ : ∀ (f' : Hom ((A.toDGModule).shift k) N)
                (hf' : f'.toFun (1 : A.carrier) ∈ N.cocyclesM (-k)),
              eN (Submodule.Quotient.mk f')
                = Submodule.Quotient.mk (⟨f'.toFun (1 : A.carrier), hf'⟩ : ↥(N.cocyclesM (-k))))
          (f : Hom ((A.toDGModule).shift k) M),
          eN (Submodule.Quotient.mk (g.comp f))
            = cohomologyMap g (-k) (e (Submodule.Quotient.mk f)))
```

**`DifferentialGradedModule.isZero_hom_toHomotopyCategory_shift_regularModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/RegularModuleHom.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/RegularModuleHom.lean#L168). The attribute's comment: “vanishing of the homotopy classes”.

> Every morphism of the homotopy category from the image of a shift of the regular module to
> an acyclic object is zero.

```lean
theorem isZero_hom_toHomotopyCategory_shift_regularModule (A : DifferentialGradedAlgebra R)
    (k : ℤ) {N : HomotopyCategory A} (hN : acyclic' A N) :
    ∀ f : (toHomotopyCategory A).obj (shift (regularModule A) k) ⟶ N, f = 0
```

**`DifferentialGradedModule.leftOrthogonal_acyclic_toHomotopyCategory_shift_regularModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/RegularModuleHom.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/RegularModuleHom.lean#L182). The attribute's comment: “left orthogonality of the shifted regular module”.

> The image of a shift of the regular module lies in the left orthogonal of the acyclic
> objects of the homotopy category.

```lean
theorem leftOrthogonal_acyclic_toHomotopyCategory_shift_regularModule
    (A : DifferentialGradedAlgebra R) (k : ℤ) :
    (acyclic' A).leftOrthogonal ((toHomotopyCategory A).obj (shift (regularModule A) k))
```

**`DifferentialGradedModule.isZero_hom_shift_regularModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/RegularModuleHom.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/RegularModuleHom.lean#L190).

> Every morphism of the homotopy category from the `k`-th shift, taken in `K(A, d)`, of the
> regular module to an acyclic object is zero.

```lean
theorem isZero_hom_shift_regularModule (A : DifferentialGradedAlgebra R) (k : ℤ)
    {N : HomotopyCategory A} (hN : acyclic' A N) :
    ∀ f : ((toHomotopyCategory A).obj (regularModule A))⟦k⟧ ⟶ N, f = 0
```

**`DifferentialGradedModule.leftOrthogonal_shift_regularModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/RegularModuleHom.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/RegularModuleHom.lean#L204). The attribute's comment: “left orthogonality, with the shift taken in the homotopy category”.

> The `k`-th shift, taken in `K(A, d)`, of the regular module lies in the left orthogonal of
> the acyclic objects.

```lean
theorem leftOrthogonal_shift_regularModule (A : DifferentialGradedAlgebra R) (k : ℤ) :
    (acyclic' A).leftOrthogonal (((toHomotopyCategory A).obj (regularModule A))⟦k⟧)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.16, Tag 0FQB](https://stacks.math.columbia.edu/tag/0FQB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
