---
declaration: section
origin: cited
lean: SheafOfModules.dgExtendHomEquiv, SheafOfModules.dgExtensionByZeroAdjunction, SheafOfModules.dgHomOfDegreeExtendEquiv_isHomComplexDifferential, SheafOfModules.dgExtendTensorIso, SheafOfModules.dgExtendTensorIso_naturality_left, SheafOfModules.dgExtendTensorIso_naturality_right
statement: formalized
proof: formalized
---

# 24.19 Localization and sheaves of differential graded modules

Section 24.19 of the Stacks Project, [Tag 0FRV](https://stacks.math.columbia.edu/tag/0FRV). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FRW, a lemma

[Tag 0FRW](https://stacks.math.columbia.edu/tag/0FRW) in the Stacks Project.

**`SheafOfModules.dgExtendHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedExtensionByZero.lean, line 699](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedExtensionByZero.lean#L699). The attribute's comment: “Hom(j\_! M, N) = Hom(M, j^* N) in degree zero”.

> **Tag 0FRW in degree zero.** The homomorphisms `j_!M ⟶ N` of right differential graded
> `A`-modules are the homomorphisms `M ⟶ j^*N` of right differential graded `A_U`-modules. The
> bijection is the degreewise adjunction `j_{U!} ⊣ j_U^*` of ordinary sheaves of modules; the
> content is that it matches the `A`-linear chain maps with the `A_U`-linear ones. This is the
> degree-zero closed part of the hom-complex identification of the source; the identification in
> every degree is `SheafOfModules.dgHomOfDegreeExtendEquiv_isHomComplexDifferential`.

```lean
noncomputable def dgExtendHomEquiv (N : DifferentialGradedModule.{w, max u v m, max u v m} A) :
    (dgExtensionByZero.{m} O U A M ⟶ N) ≃ (M ⟶ N.over U)
```

**`SheafOfModules.dgExtensionByZeroAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedExtensionByZero.lean, line 716](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedExtensionByZero.lean#L716). The attribute's comment: “the identification is an adjunction `j_! ⊣ j^*` of differential graded modules”.

> **Tag 0FRW in degree zero, as an adjunction.** `j_! : Mod^dg(A_U, d) ⥤ Mod^dg(A, d)` is left
> adjoint to `j^* : Mod^dg(A, d) ⥤ Mod^dg(A_U, d)`, which is the displayed identification of
> Hom-sets of the source together with its naturality in both variables.

```lean
noncomputable def dgExtensionByZeroAdjunction :
    dgExtensionByZeroFunctor.{m} O U A ⊣ DifferentialGradedModule.overFunctor A U
```

**`SheafOfModules.dgHomOfDegreeExtendEquiv_isHomComplexDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedExtensionByZero.lean, line 767](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedExtensionByZero.lean#L767). The attribute's comment: “Hom(j\_! M, N) = Hom(M, j^* N) as complexes: compatibility with the differentials”.

> **Tag 0FRW.** The identification of Tag 0FRA of the homogeneous homomorphisms of degree `d`
> out of `j_!M` with those into `j^*N` matches the differentials of the two hom-complexes. Read in
> every degree together with `SheafOfModules.gradedHomOfDegreeExtendEquiv` and its naturality, this
> is the displayed identification
> `Hom_{Mod^dg(A, d)}(j_!M, N) = Hom_{Mod^dg(A_U, d)}(M, j^*N)`
> of complexes of abelian groups.

```lean
theorem dgHomOfDegreeExtendEquiv_isHomComplexDifferential
    (N : DifferentialGradedModule.{w, max u v m, max u v m} A) (d : ℤ)
    (f : GradedHomOfDegree (GradedModule.ofDifferentialGraded (dgExtensionByZero.{m} O U A M))
      (GradedModule.ofDifferentialGraded N) d)
    (g : GradedHomOfDegree (GradedModule.ofDifferentialGraded (dgExtensionByZero.{m} O U A M))
      (GradedModule.ofDifferentialGraded N) (d + 1)) :
    IsHomComplexDifferential f g ↔
      IsHomComplexDifferential (A := A.over U) (M := M) (N := N.over U) (d := d)
        (gradedHomOfDegreeExtendEquiv.{m} (M := GradedModule.ofDifferentialGraded M)
          (N := GradedModule.ofDifferentialGraded N) O U A.toGradedAlgebra d f)
        (gradedHomOfDegreeExtendEquiv.{m} (M := GradedModule.ofDifferentialGraded M)
          (N := GradedModule.ofDifferentialGraded N) O U A.toGradedAlgebra (d + 1) g)
```

## Tag 0FRX, a lemma

[Tag 0FRX](https://stacks.math.columbia.edu/tag/0FRX) in the Stacks Project.

**`SheafOfModules.dgExtendTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedExtensionByZeroTensor.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedExtensionByZeroTensor.lean#L332). The attribute's comment: “j\_! M ⊗\_A N = j\_!(M ⊗\_\{A\_U} N|\_U) as complexes of O-modules”.

> **Tag 0FRX.** The relative tensor product of the extension by zero of a right differential
> graded `A_U`-module `M` with a left differential graded `A`-module `N` is the extension by zero
> of the relative tensor product of `M` with the restriction of `N`:
> `j_!M ⊗_A N = j_!(M ⊗_{A_U} N|_U)` as complexes of `O`-modules. In each degree it is the
> isomorphism of Tag 0FRB, which sends the local section `j_!x ⊗ y` to `j_!(x ⊗ y)` and is natural
> in `M` and in `N`; what is proved here is that it commutes with the differentials.

```lean
noncomputable def dgExtendTensorIso :
    dgExtendTensor.{m} O U A M N ≅ dgExtendSliceTensor.{m} O U A M N
```

**`SheafOfModules.dgExtendTensorIso_naturality_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedExtensionByZeroTensor.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedExtensionByZeroTensor.lean#L362). The attribute's comment: “functoriality of j\_! M ⊗\_A N = j\_!(M ⊗\_\{A\_U} N|\_U) in M, in each degree”.

> **Tag 0FRX, functoriality in the right differential graded module.** In every degree the
> identification `j_!M ⊗_A N = j_!(M ⊗_{A_U} N|_U)` commutes with a homomorphism `M ⟶ M'` of right
> differential graded `A_U`-modules; its components are the degreewise maps of the relative tensor
> products induced by `j_!M ⟶ j_!M'`, respectively by `M ⟶ M'`.

```lean
theorem dgExtendTensorIso_naturality_left
    {M' : DifferentialGradedModule.{w, max u v m, max u v m} (A.over U)} (h : M ⟶ M') (n : ℤ) :
    RelativeTensor.gradedTensorMapRight (gradedExtensionByZeroMap.{m} O U A.toGradedAlgebra
          (GradedModule.ofDifferentialGradedMap h))
          (LeftGradedModule.ofDifferentialGraded N) n ≫
        (dgExtendTensorIso.{m} O U A M' N).hom.f n =
      (dgExtendTensorIso.{m} O U A M N).hom.f n ≫ (extendSheaf.{m} O U).map
        (RelativeTensor.gradedTensorMapRight (J := J.over U) (Osharp := O.over U)
          (GradedModule.ofDifferentialGradedMap h)
          ((LeftGradedModule.ofDifferentialGraded N).over U) n)
```

**`SheafOfModules.dgExtendTensorIso_naturality_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedExtensionByZeroTensor.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedExtensionByZeroTensor.lean#L380). The attribute's comment: “functoriality of j\_! M ⊗\_A N = j\_!(M ⊗\_\{A\_U} N|\_U) in N, in each degree”.

> **Tag 0FRX, functoriality in the left differential graded module.** In every degree the
> identification `j_!M ⊗_A N = j_!(M ⊗_{A_U} N|_U)` commutes with a homomorphism `N ⟶ N'` of left
> differential graded `A`-modules.

```lean
theorem dgExtendTensorIso_naturality_right
    {N' : LeftDifferentialGradedModule.{w, max u v m, max u v m} A} (f : N ⟶ N') (n : ℤ) :
    RelativeTensor.gradedTensorMap (gradedExtensionByZero.{m} O U A.toGradedAlgebra
          (GradedModule.ofDifferentialGraded M))
          (LeftGradedModule.ofDifferentialGradedMap f) n ≫
        (dgExtendTensorIso.{m} O U A M N').hom.f n =
      (dgExtendTensorIso.{m} O U A M N).hom.f n ≫ (extendSheaf.{m} O U).map
        (RelativeTensor.gradedTensorMap (J := J.over U) (Osharp := O.over U)
          (GradedModule.ofDifferentialGraded M)
          (LeftGradedModule.overMap (LeftGradedModule.ofDifferentialGradedMap f) U) n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.19, Tag 0FRV](https://stacks.math.columbia.edu/tag/0FRV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
