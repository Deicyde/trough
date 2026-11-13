---
declaration: section
origin: cited
lean: SheafOfModules.gradedExtendHomEquiv, SheafOfModules.gradedExtensionByZeroAdjunction, SheafOfModules.gradedHomOfDegreeExtendEquiv, SheafOfModules.gradedHomOfDegreeExtendEquiv_naturality_left, SheafOfModules.gradedHomOfDegreeExtendEquiv_naturality_right, SheafOfModules.extendTensorIso, SheafOfModules.extendTensorHom_naturality_right, SheafOfModules.extendTensorHom_naturality_left
statement: formalized
proof: formalized
---

# 24.10 Localization and sheaves of graded modules

Section 24.10 of the Stacks Project, [Tag 0FR9](https://stacks.math.columbia.edu/tag/0FR9). 2 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FRA, a lemma

[Tag 0FRA](https://stacks.math.columbia.edu/tag/0FRA) in the Stacks Project.

**`SheafOfModules.gradedExtendHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedExtensionByZero.lean, line 425](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedExtensionByZero.lean#L425). The attribute's comment: “Hom(j\_! M, N) = Hom(M, j^* N)”.

> **Tag 0FRA.** The homomorphisms `j_!M ⟶ N` of right graded `A`-modules are the
> homomorphisms `M ⟶ j^*N` of right graded `A_U`-modules. The bijection is the degreewise
> adjunction `j_{U!} ⊣ j_U^*` of ordinary sheaves of modules; the content is that it matches the
> `A`-linear maps with the `A_U`-linear maps.

```lean
noncomputable def gradedExtendHomEquiv
    (M : GradedModule.{w, max u v m, max u v m} (A.over U))
    (N : GradedModule.{w, max u v m, max u v m} A) :
    (gradedExtensionByZero.{m} O U A M ⟶ N) ≃ (M ⟶ N.over U)
```

**`SheafOfModules.gradedExtensionByZeroAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedExtensionByZero.lean, line 451](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedExtensionByZero.lean#L451). The attribute's comment: “the identification is an adjunction `j_! ⊣ j^*` of graded modules”.

> **Tag 0FRA, as an adjunction.** `j_! : Mod^gr(A_U) ⥤ Mod^gr(A)` is left adjoint to
> `j^* : Mod^gr(A) ⥤ Mod^gr(A_U)`.

```lean
noncomputable def gradedExtensionByZeroAdjunction :
    gradedExtensionByZeroFunctor.{m} O U A ⊣ GradedModule.overFunctor A U
```

**`SheafOfModules.gradedHomOfDegreeExtendEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedExtensionByZero.lean, line 524](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedExtensionByZero.lean#L524). The attribute's comment: “Hom(j\_! M, N) = Hom(M, j^* N), in each degree”.

> **Tag 0FRA.** In every degree `d` the homogeneous homomorphisms `j_!M ⟶ N` of right graded
> `A`-modules are the homogeneous homomorphisms `M ⟶ j^*N` of right graded `A_U`-modules. The
> bijection is the degreewise adjunction `j_{U!} ⊣ j_U^*` of ordinary sheaves of modules; the
> content is that it matches the `A`-linear maps with the `A_U`-linear maps. In degree `0`, read
> together with the naturality below, this is the adjunction `j_! ⊣ j^*` of the source.

```lean
noncomputable def gradedHomOfDegreeExtendEquiv (d : ℤ) :
    GradedHomOfDegree (gradedExtensionByZero.{m} O U A M) N d ≃
      GradedHomOfDegree M (N.over U) d
```

**`SheafOfModules.gradedHomOfDegreeExtendEquiv_naturality_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedExtensionByZero.lean, line 547](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedExtensionByZero.lean#L547). The attribute's comment: “naturality of Hom(j\_! M, N) = Hom(M, j^* N) in M”.

> **Tag 0FRA, naturality in the source.**

```lean
theorem gradedHomOfDegreeExtendEquiv_naturality_left
    {M' : GradedModule.{w, max u v m, max u v m} (A.over U)} (g : M' ⟶ M) (d : ℤ)
    (f : GradedHomOfDegree (gradedExtensionByZero.{m} O U A M) N d) :
    gradedHomOfDegreeExtendEquiv.{m} O U A d
        (GradedHomOfDegree.compLeft (gradedExtensionByZeroMap.{m} O U A g) f) =
      GradedHomOfDegree.compLeft g (gradedHomOfDegreeExtendEquiv.{m} O U A d f)
```

**`SheafOfModules.gradedHomOfDegreeExtendEquiv_naturality_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedExtensionByZero.lean, line 558](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedExtensionByZero.lean#L558). The attribute's comment: “naturality of Hom(j\_! M, N) = Hom(M, j^* N) in N”.

> **Tag 0FRA, naturality in the target.**

```lean
theorem gradedHomOfDegreeExtendEquiv_naturality_right
    {N' : GradedModule.{w, max u v m, max u v m} A} (k : N ⟶ N') (d : ℤ)
    (f : GradedHomOfDegree (gradedExtensionByZero.{m} O U A M) N d) :
    gradedHomOfDegreeExtendEquiv.{m} O U A d (f.compRight k) =
      (gradedHomOfDegreeExtendEquiv.{m} O U A d f).compRight
        (GradedModule.overMap k U)
```

## Tag 0FRB, a lemma

[Tag 0FRB](https://stacks.math.columbia.edu/tag/0FRB) in the Stacks Project.

**`SheafOfModules.extendTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedExtensionByZeroTensor.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedExtensionByZeroTensor.lean#L299). The attribute's comment: “j\_! M ⊗\_A N = j\_!(M ⊗\_\{A\_U} N|\_U) as graded O-modules”.

> **Tag 0FRB.** In every degree `n` the relative tensor product of the extension by zero of
> a right graded `A_U`-module `M` with a left graded `A`-module `N` is the extension by zero of
> the relative tensor product of `M` with the restriction of `N`:
> `j_!M ⊗_A N = j_!(M ⊗_{A_U} N|_U)` as sheaves of `O`-modules. The isomorphism sends the local
> section `j_!x ⊗ y` to `j_!(x ⊗ y)`, and it is natural in `M` and in `N` by
> `SheafOfModules.extendTensorHom_naturality_left` and `..._naturality_right`.

```lean
noncomputable def extendTensorIso (n : ℤ) :
    extendTensor.{m} O U A M N n ≅
      (extendSheaf.{m} O U).obj (sliceTensor.{m} O U A M N n)
```

**`SheafOfModules.extendTensorHom_naturality_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedExtensionByZeroTensor.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedExtensionByZeroTensor.lean#L311). The attribute's comment: “functoriality of j\_! M ⊗\_A N = j\_!(M ⊗\_\{A\_U} N|\_U) in N”.

> **Tag 0FRB, functoriality in the left graded module.** The identification
> `j_!M ⊗_A N = j_!(M ⊗_{A_U} N|_U)` commutes with a homomorphism `N ⟶ N'` of left graded
> `A`-modules.

```lean
theorem extendTensorHom_naturality_right {N' : LeftGradedModule.{w, max u v m, max u v m} A}
    (f : N ⟶ N') (n : ℤ) :
    RelativeTensor.gradedTensorMap (gradedExtensionByZero.{m} O U A M) f n ≫
        extendTensorHom.{m} O U A M N' n =
      extendTensorHom.{m} O U A M N n ≫ (extendSheaf.{m} O U).map
        (RelativeTensor.gradedTensorMap (J := J.over U) (Osharp := O.over U) M
          (LeftGradedModule.overMap f U) n)
```

**`SheafOfModules.extendTensorHom_naturality_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedExtensionByZeroTensor.lean, line 368](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedExtensionByZeroTensor.lean#L368). The attribute's comment: “functoriality of j\_! M ⊗\_A N = j\_!(M ⊗\_\{A\_U} N|\_U) in M”.

> **Tag 0FRB, functoriality in the right graded module.** The identification
> `j_!M ⊗_A N = j_!(M ⊗_{A_U} N|_U)` commutes with a homomorphism `M ⟶ M'` of right graded
> `A_U`-modules.

```lean
theorem extendTensorHom_naturality_left {M' : GradedModule.{w, max u v m, max u v m} (A.over U)}
    (h : M ⟶ M') (n : ℤ) :
    RelativeTensor.gradedTensorMapRight (gradedExtensionByZeroMap.{m} O U A h) N n ≫
        extendTensorHom.{m} O U A M' N n =
      extendTensorHom.{m} O U A M N n ≫ (extendSheaf.{m} O U).map
        (RelativeTensor.gradedTensorMapRight (J := J.over U) (Osharp := O.over U) h
          (N.over U) n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.10, Tag 0FR9](https://stacks.math.columbia.edu/tag/0FR9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
