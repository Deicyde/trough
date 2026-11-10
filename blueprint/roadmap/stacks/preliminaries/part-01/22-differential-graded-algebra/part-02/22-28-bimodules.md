---
declaration: section
origin: cited
lean: DifferentialGraded.Bimodule, AlgebraBimodule, GradedBimodule, DifferentialGraded.Bimodule.toGradedBimodule, DifferentialGradedModule.bimoduleStructureEquivRightLinearEndomorphismHom, DifferentialGraded.Bimodule.tensorEquivalence, DifferentialGraded.Bimodule.exists_propertyP_resolution, DifferentialGraded.Bimodule.exists_admissible_telescope
statement: formalized
proof: formalized
---

# 22.28 Bimodules

Section 22.28 of the Stacks Project, [Tag 0FQG](https://stacks.math.columbia.edu/tag/0FQG). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FQH, a definition

[Tag 0FQH](https://stacks.math.columbia.edu/tag/0FQH) in the Stacks Project.

**`DifferentialGraded.Bimodule`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Endomorphism/BimoduleDefs.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Endomorphism/BimoduleDefs.lean#L51). The attribute's comment: “(3): a differential graded `(A, B)`-bimodule, presented as in Tag 0FQI by a right differential graded `B`-module together with a left differential graded `A`-action on its underlying complex whose homogeneous multiplications are right `B`-linear; the grading, the differential and the two Leibniz rules are those of the right module and of the left action. Its underlying graded bimodule, part (2), is `DifferentialGraded.Bimodule.toGradedBimodule`”.

> A differential graded `(A, B)`-bimodule, presented as a right differential graded `B`-module
> with a compatible left differential graded `A`-action.

```lean
structure Bimodule
```

**`AlgebraBimodule`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/GradedBimodule.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/GradedBimodule.lean#L99). The attribute's comment: “(1): an `(A, B)`-bimodule, bundled as a carrier together with the Mathlib classes that discharge the source's clauses — `Module A M` and `Module Bᵐᵒᵖ M` (clause (a) by `mul_smul`, clause (c) by `one_smul`), `SMulCommClass A Bᵐᵒᵖ M` (clause (b)), and `Module R M` with the two `IsScalarTower`s (`R`-bilinearity of the two actions)”.

> An `(A, B)`-bimodule over a commutative ring `R`, for `R`-algebras `A` and `B`: an `R`-module
> `M` with an `R`-bilinear left `A`-action and an `R`-bilinear right `B`-action which commute.
>
> All of the source's clauses are discharged by the Mathlib classes listed as fields, so the only
> data is the carrier: `mul_smul` of the two module structures is clause (a), `SMulCommClass` is
> clause (b), `one_smul` is clause (c), and the two `IsScalarTower` fields together with the
> `R`-module structure are the `R`-bilinearity of the two actions.

```lean
structure AlgebraBimodule (R : Type u) [CommRing R] (A : Type u) [Ring A] [Algebra R A]
    (B : Type u) [Ring B] [Algebra R B]
```

**`GradedBimodule`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/GradedBimodule.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/GradedBimodule.lean#L133). The attribute's comment: “(2): a graded `(A, B)`-bimodule, an `AlgebraBimodule` (part (1), the parent projection `toAlgebraBimodule`) together with a grading by `R`-submodules which decomposes the module and satisfies `Aⁿ Mᵐ ⊆ Mⁿ⁺ᵐ` and `Mⁿ Bᵐ ⊆ Mⁿ⁺ᵐ`”.

> A graded `(A, B)`-bimodule over a commutative ring `R`, for `ℤ`-graded `R`-algebras `𝒜` and
> `ℬ`: an `(A, B)`-bimodule `M` with a grading `M = ⨁ Mⁿ` such that `Aⁿ Mᵐ ⊆ Mⁿ⁺ᵐ` and
> `Mⁿ Bᵐ ⊆ Mⁿ⁺ᵐ`.
>
> The underlying `(A, B)`-bimodule of part (1) is the parent projection
> `GradedBimodule.toAlgebraBimodule`.

```lean
structure GradedBimodule {R : Type u} [CommRing R] {A : Type u} [Ring A] [Algebra R A]
    (𝒜 : ℤ → Submodule R A) [GradedAlgebra 𝒜] {B : Type u} [Ring B] [Algebra R B]
    (ℬ : ℤ → Submodule R B) [GradedAlgebra ℬ] extends AlgebraBimodule R A B
```

**`DifferentialGraded.Bimodule.toGradedBimodule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/GradedBimodule.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/GradedBimodule.lean#L176). The attribute's comment: “the graded (A, B)-bimodule underlying a differential graded one, which is what makes part (3) a refinement of part (2); the three parts themselves are tagged with stacks\_fixed, which plain @[stacks] cannot carry on a structure”.

> The graded `(A, B)`-bimodule underlying a differential graded `(A, B)`-bimodule: the right
> differential graded `B`-module with its grading, the left `A`-action totalized from the left
> differential graded action, and the differential forgotten.
>
> This is what makes the three parts of [Stacks, Tag 0FQH] one definition rather than three
> unrelated ones: part (3), `DifferentialGraded.Bimodule`, refines part (2), `GradedBimodule`,
> which in turn extends part (1), `AlgebraBimodule`.

```lean
noncomputable def Bimodule.toGradedBimodule (M : Bimodule.{u, u} A B) :
    GradedBimodule A.grading B.grading
```

## Tag 0FQI, a lemma

[Tag 0FQI](https://stacks.math.columbia.edu/tag/0FQI) in the Stacks Project.

**`DifferentialGradedModule.bimoduleStructureEquivRightLinearEndomorphismHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Endomorphism/Bimodule.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Endomorphism/Bimodule.lean#L82).

> Compatible left differential graded actions on a fixed right differential graded `B`-module
> correspond bijectively to homomorphisms into its right `B`-linear endomorphism differential graded
> algebra. The specified equation makes the correspondence canonical on every homogeneous element.

```lean
noncomputable def bimoduleStructureEquivRightLinearEndomorphismHom :
    { e : BimoduleStructure A B M ≃ RightLinearEndomorphismHom A B M //
      ∀ (L : BimoduleStructure A B M) (n : ℤ) (a : A.grading n),
        (endomorphismDGA M.toCochainComplex).cochainEquiv n
          ⟨(e L).1.toAlgebraHom a, (e L).1.map_grading n a a.property⟩ = L.1.action n a }
```

## Tag 0FQJ, a lemma

[Tag 0FQJ](https://stacks.math.columbia.edu/tag/0FQJ) in the Stacks Project.

**`DifferentialGraded.Bimodule.tensorEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Endomorphism/BimoduleTensorEquivalence.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Endomorphism/BimoduleTensorEquivalence.lean#L466).

> A differential graded `(A, B)`-bimodule is canonically a right differential graded module over
> the graded tensor product of the graded opposite of `A` with `B`, and this is an equivalence of
> categories.

```lean
noncomputable def tensorEquivalence : TensorEquivalence A B
```

## Tag 0FQK, a lemma

[Tag 0FQK](https://stacks.math.columbia.edu/tag/0FQK) in the Stacks Project.

**`DifferentialGraded.Bimodule.exists_propertyP_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Endomorphism/BimodulePropertyP.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Endomorphism/BimodulePropertyP.lean#L110).

> **Stacks 0FQK.** *"Let `R` be a ring. Let `(A, d)` and `(B, d)` be differential graded
> `R`-algebras. Let `M` be a differential graded `(A, B)`-bimodule. There exists a homomorphism
> `P → M` of differential graded `(A, B)`-bimodules which is a quasi-isomorphism such that `P`
> has property (P)."*
>
> Property (P) of the resolving bimodule is recorded as a property-(P) filtration of the right
> differential graded `Aᵒᵖ ⊗_R B`-module it is by Tag 0FQJ, and being a quasi-isomorphism is
> Mathlib's `QuasiIso` on the cochain complex underlying the homomorphism of right `B`-modules.

```lean
theorem exists_propertyP_resolution (A B : DifferentialGradedAlgebra.{u, u} R)
    (M : Bimodule A B) :
    ∃ (P : Bimodule A B) (f : P ⟶ M),
      QuasiIso ((DifferentialGradedModule.forgetToCochainComplex B).map f.rightHom) ∧
        Nonempty (DifferentialGradedModule.PropertyPFiltration (toTensorModule A B P))
```

## Tag 0FQL, a lemma

[Tag 0FQL](https://stacks.math.columbia.edu/tag/0FQL) in the Stacks Project.

**`DifferentialGraded.Bimodule.exists_admissible_telescope`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Endomorphism/BimoduleTelescope.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Endomorphism/BimoduleTelescope.lean#L117).

> **Stacks 0FQL.** *"Let `R` be a ring. Let `(A, d)` and `(B, d)` be differential graded
> `R`-algebras. Let `P` be a differential graded `(A, B)`-bimodule having property (P) with
> corresponding filtration `F_•`, then we obtain a short exact sequence
> `0 → ⨁ F_iP → ⨁ F_iP → P → 0` of differential graded `(A, B)`-bimodules which is split as a
> sequence of graded `(A, B)`-bimodules."*
>
> Property (P) is read on the right differential graded `Aᵒᵖ ⊗_R B`-module of Tag 0FQJ, and the
> stages of the filtration are brought back to bimodules through the same construction. The direct
> sum is recorded by its universal property, the second map is the sum of the inclusions
> `F_iP → P`, and the first map is, on the summand `F_iP`, the identity minus the inclusion
> `F_iP → F_{i+1}P`.

```lean
theorem exists_admissible_telescope (P : Bimodule A B)
    (F : DifferentialGradedModule.PropertyPFiltration (toTensorModule A B P)) :
    ∃ (S : Bimodule A B) (ι : ∀ i : ℕ, ofTensorModule A B (F.F i) ⟶ S) (α : S ⟶ S) (β : S ⟶ P),
      (∀ (T : Bimodule A B) (g : ∀ i : ℕ, ofTensorModule A B (F.F i) ⟶ T),
          ∃! h : S ⟶ T, ∀ i : ℕ, ι i ≫ h = g i) ∧
        (∀ (i : ℕ) (x : (F.F i).M),
          β.rightHom.toFun ((ι i).rightHom.toFun x) = (F.ι i).toFun x) ∧
        (∀ (i : ℕ) (x : (F.F i).M), α.rightHom.toFun ((ι i).rightHom.toFun x) =
          (ι i).rightHom.toFun x - (ι (i + 1)).rightHom.toFun ((F.incl i).toFun x)) ∧
        IsAdmissibleShortExact A B α β
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.28, Tag 0FQG](https://stacks.math.columbia.edu/tag/0FQG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
