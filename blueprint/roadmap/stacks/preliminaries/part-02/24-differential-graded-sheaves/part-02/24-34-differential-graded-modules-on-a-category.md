---
declaration: section
origin: cited
lean: SheafOfModules.DifferentialGradedModule.ChaoticExtension.isEquivalence_qcRestriction, SheafOfModules.DifferentialGradedModule.Chaotic.qc_derivedExtension_iff_and_isEquivalence
statement: formalized
proof: formalized
---

# 24.34 Differential graded modules on a category, bis

Section 24.34 of the Stacks Project, [Tag 0GZD](https://stacks.math.columbia.edu/tag/0GZD). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GZE, a lemma

[Tag 0GZE](https://stacks.math.columbia.edu/tag/0GZE) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.ChaoticExtension.isEquivalence_qcRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedChaoticRestrictionEquivalence.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedChaoticRestrictionEquivalence.lean#L404).

> *Let `C, O, A` be as in Section 0GZ8. Let `C' ⊂ C` be a full subcategory with the following
> property: for every `U ∈ Ob(C)` the category `U/C'` of arrows `U → U'` is cofiltered. Denote
> `O', A'` the restrictions of `O, A` to `C'`. Then restriction induces an equivalence
> `QC(A, d) → QC(A', d)`.*
>
> Here `C` carries the chaotic topology, `O` is a sheaf of commutative rings and `A` a sheaf of
> differential graded `O`-algebras on it; the full subcategory `C'` is `P.FullSubcategory` for a
> property `P` of objects, `U/C'` is `StructuredArrow U P.ι`, `O'` is
> `SheafOfModules.restrictRingSheaf P.ι O` and `A'` is `A.restrict P.ι`. `QC(A, d)` is the full
> subcategory `Chaotic.QC A` of `D(A, d)` of Definition 0GZ9, and the functor is restriction
> `D(A, d) ⥤ D(A', d)`, the functor induced by restriction of differential graded modules, which is
> exact. That functor is the literal restriction up to the canonical isomorphism
> `restriction_sectionModuleIso : (M|_{C'})(U') ≅ M(F U')` (read over `A'(U') = A(F U')`), natural
> in `M` by `restriction_sectionModuleIso_naturality`.

```lean
theorem isEquivalence_qcRestriction [∀ U : C, IsCofiltered (StructuredArrow U P.ι)] :
    (qcRestriction P.ι A).IsEquivalence
```

## Tag 0GZF, a lemma

[Tag 0GZF](https://stacks.math.columbia.edu/tag/0GZF) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.Chaotic.qc_derivedExtension_iff_and_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedChaoticQuasiCoherentQuasiIso.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedChaoticQuasiCoherentQuasiIso.lean#L160).

> **Stacks 0GZF.** Let `C` be a category with the chaotic topology, `O` a sheaf of rings on it
> and `φ : A ⟶ B` a homomorphism of sheaves of differential graded `O`-algebras which induces an
> isomorphism on cohomology sheaves. Then the equivalence `D(A, d) ⥤ D(B, d)`, `M ↦ M ⊗^𝐋_A B`, of
> Tag 0FTZ induces an equivalence `QC(A, d) ⥤ QC(B, d)`.
>
> The three conjuncts are: an object `M` of `D(A, d)` lies in `QC(A, d)` exactly when `M ⊗^𝐋_A B`
> lies in `QC(B, d)`, so that the functor induces a functor `QC(A, d) ⥤ QC(B, d)`; that functor
> lies over derived extension of scalars; and it is an equivalence.
>
> The source's functor `M ↦ M ⊗^𝐋_A B` is defined only for a homomorphism `φ` preserving `1`,
> since `B` is made a left `A`-module through `φ`; so `PreservesOne` is implicit in the
> statement.

```lean
theorem qc_derivedExtension_iff_and_isEquivalence :
    (∀ M : derivedCategory.{u, u, u} A, QC B ((derivedExtension φ hφ).obj M) ↔ QC A M) ∧
      qcDerivedExtension φ hφ hqis ⋙ QCι B = QCι A ⋙ derivedExtension φ hφ ∧
      (qcDerivedExtension φ hφ hqis).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.34, Tag 0GZD](https://stacks.math.columbia.edu/tag/0GZD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
