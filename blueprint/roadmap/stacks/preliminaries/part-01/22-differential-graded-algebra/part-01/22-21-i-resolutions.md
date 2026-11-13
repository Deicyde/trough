---
declaration: section
origin: cited
lean: DifferentialGradedModule.exists_isAdmissibleShortExact_uliftProduct, DifferentialGradedModule.rightOrthogonal_acyclic_of_propertyI, DifferentialGradedModule.exists_dual_injection, DifferentialGradedModule.exists_propertyI_resolution
statement: formalized
proof: formalized
---

# 22.21 I-resolutions

Section 22.21 of the Stacks Project, [Tag 09KQ](https://stacks.math.columbia.edu/tag/09KQ). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09KR, a lemma

[Tag 09KR](https://stacks.math.columbia.edu/tag/09KR) in the Stacks Project.

**`DifferentialGradedModule.exists_isAdmissibleShortExact_uliftProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DualTelescopeProduct.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DualTelescopeProduct.lean#L81).

> **Stacks 09KR.** *"Let `(A, d)` be a differential graded algebra. Let `I` be a differential
> graded `A`-module. If `F_•` is a filtration as in property (I), then we obtain an admissible
> short exact sequence `0 → I → ∏ I/F_iI → ∏ I/F_iI → 0` of differential graded `A`-modules."*
>
> The filtration enters only through the tower of quotients `Q i = I/F_iI` it determines, together
> with conditions (1) and (2) of property (I): the quotient maps `p i : I ⟶ Q i` are compatible
> with the transitions `t i : Q (i + 1) ⟶ Q i` (`hp`), the transitions are admissible
> epimorphisms (`hadm`, condition (2)), and `I = lim Q i`, which is injectivity of
> `I → lim Q i` (`hsep`) together with its surjectivity in each degree (`hcomplete`, the limit
> being formed in differential graded modules and hence degreewise).
>
> The product is `DifferentialGradedModule.uliftProduct Q`, the first map is the family of
> quotient maps and the second is the identity minus the map induced by the transitions; each is
> pinned down by what it does on the projections.

```lean
theorem exists_isAdmissibleShortExact_uliftProduct {I : DifferentialGradedModule A}
    (Q : ℕ → DifferentialGradedModule A) (p : ∀ i, I ⟶ Q i) (t : ∀ i, Q (i + 1) ⟶ Q i)
    (hp : ∀ (i : ℕ) (x : I.M), (t i).toFun ((p (i + 1)).toFun x) = (p i).toFun x)
    (hadm : ∀ i, IsAdmissibleEpi (t i))
    (hsep : ∀ x : I.M, (∀ i, (p i).toFun x = 0) → x = 0)
    (hcomplete : ∀ (n : ℤ) (q : ∀ i, (Q i).M), (∀ i, q i ∈ (Q i).grading n) →
      (∀ i, (t i).toFun (q (i + 1)) = q i) → ∃ y ∈ I.grading n, ∀ i, (p i).toFun y = q i) :
    ∃ (α : I ⟶ uliftProduct Q) (β : uliftProduct Q ⟶ uliftProduct Q),
      (∀ (i : ℕ) (x : I.M), (uliftProduct.π Q i).toFun (α.toFun x) = (p i).toFun x) ∧
      (∀ (i : ℕ) (y : (uliftProduct Q).M), (uliftProduct.π Q i).toFun (β.toFun y)
        = (uliftProduct.π Q i).toFun y - (t i).toFun ((uliftProduct.π Q (i + 1)).toFun y)) ∧
      IsAdmissibleShortExact α β
```

## Tag 09KS, a lemma

[Tag 09KS](https://stacks.math.columbia.edu/tag/09KS) in the Stacks Project.

**`DifferentialGradedModule.rightOrthogonal_acyclic_of_propertyI`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/RightOrthogonalAcyclic.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/RightOrthogonalAcyclic.lean#L266).

> **Stacks 09KS.** A right differential graded module with property (I) is orthogonal on the
> right to the acyclic objects of the homotopy category: every morphism of `K(A, d)` from an
> acyclic differential graded module into it vanishes.

```lean
theorem rightOrthogonal_acyclic_of_propertyI {I : DifferentialGradedModule A}
    (F : PropertyIFiltration I) :
    (acyclic' A).rightOrthogonal ((toHomotopyCategory A).obj I)
```

## Tag 09KT, a lemma

[Tag 09KT](https://stacks.math.columbia.edu/tag/09KT) in the Stacks Project.

**`DifferentialGradedModule.exists_dual_injection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DualCover.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DualCover.lean#L327).

> **Stacks 09KT.** Every right differential graded `A`-module `M` admits an injection `φ` into
> the graded dual `I` of a direct sum of cells of left modules, such that
> `Coker(d_M) → Coker(d_I)` is injective, and `I` sits in an admissible short exact sequence whose
> two ends are the products of shifts of `A^∨`
>
> `∏ᵢ A^∨[kᵢ]` and `∏ᵢ A^∨[kᵢ + 1]`.

```lean
theorem exists_dual_injection (A : DifferentialGradedAlgebra R)
    (M : DifferentialGradedModule A) :
    ∃ (ι : Type u) (_ : DecidableEq ι) (k : ι → ℤ) (b : ι → Bool)
      (φ : M ⟶ Ldual (DifferentialGraded.LeftModule.twoCellSum A k b)),
      Function.Injective φ.toFun ∧
      (∀ x : M.M,
        (∃ w : (Ldual (DifferentialGraded.LeftModule.twoCellSum A k b)).M,
          (Ldual (DifferentialGraded.LeftModule.twoCellSum A k b)).d w = φ.toFun x) →
        ∃ y : M.M, M.d y = x) ∧
      ∃ (i : productDualShifts A k ⟶ Ldual (DifferentialGraded.LeftModule.twoCellSum A k b))
        (p : Ldual (DifferentialGraded.LeftModule.twoCellSum A k b) ⟶
          productDualShifts A (fun c => k c + 1)),
        IsAdmissibleShortExact i p
```

## Tag 09KU, a lemma

[Tag 09KU](https://stacks.math.columbia.edu/tag/09KU) in the Stacks Project.

**`DifferentialGradedModule.exists_propertyI_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/PropertyIResolutionExists.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/PropertyIResolutionExists.lean#L71).

> **Property-(I) resolutions exist** (Tag 09KU). Every right differential graded module `M`
> over a differential graded algebra `(A, d)` admits a quasi-isomorphism into a differential
> graded `A`-module `I` carrying a property-(I) filtration: an exhaustive decreasing filtration by
> differential graded submodules with admissible inclusions whose successive quotients are
> products of shifts of the graded dual `A^∨`.
>
> The resolution is the one of the Stacks proof: `I` is the totalization
> `∏_{j ≥ 0} Iⱼ[-j]` of the tower `I₀ → I₁ → ⋯` built from Stacks 09KT, and the map is its
> augmentation.

```lean
theorem exists_propertyI_resolution (A : DifferentialGradedAlgebra R)
    (M : DifferentialGradedModule A) :
    ∃ (I : DifferentialGradedModule A) (f : M ⟶ I),
      QuasiIso ((forgetToCochainComplex A).map f) ∧ Nonempty (PropertyIFiltration I)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.21, Tag 09KQ](https://stacks.math.columbia.edu/tag/09KQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
