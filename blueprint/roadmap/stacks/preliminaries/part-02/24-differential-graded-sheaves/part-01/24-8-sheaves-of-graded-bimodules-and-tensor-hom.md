---
declaration: section
origin: cited
lean: SheafOfModules.GradedLocalHom.actRight, SheafOfModules.IsGradedInternalHom, SheafOfModules.balancedEquiv, SheafOfModules.GradedBimodule, SheafOfModules.GradedBimodule.Hom, SheafOfModules.tensorHomEquiv, SheafOfModules.isGradedSheafHom_tensor
statement: formalized
proof: formalized
---

# 24.8 Sheaves of graded bimodules and tensor-hom adjunction

Section 24.8 of the Stacks Project, [Tag 0FR4](https://stacks.math.columbia.edu/tag/0FR4). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FR4, the section

[Tag 0FR4](https://stacks.math.columbia.edu/tag/0FR4) in the Stacks Project.

**`SheafOfModules.GradedLocalHom.actRight`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHom.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHom.lean#L243). The attribute's comment: “the right A-action on the local sections of the graded internal hom”.

> Right multiplication of a local section `f` of `SheafHom^n_B(N, L)` over `U` by a section
> `a` of `A^m` over `U`, defined by `(f a)(y) = f (a y)`. This involves no signs.

```lean
noncomputable def GradedLocalHom.actRight {N : GradedBimodule.{t, a, z} A B}
    {L : GradedModule.{t, a, s} B} {n : ℤ} {U : C}
    (f : GradedLocalHom N.toGradedModule L n U) (m : ℤ)
    (a : (A.piece m).val.obj (Opposite.op U)) :
    GradedLocalHom N.toGradedModule L (n + m) U
```

**`SheafOfModules.IsGradedInternalHom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHom.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHom.lean#L503). The attribute's comment: “SheafHom^gr\_B(N, L) as a right graded A-module”.

> A right graded `A`-module `H` is the graded internal hom `SheafHom^gr_B(N, L)` of a graded
> `(A, B)`-bimodule `N` and a right graded `B`-module `L` when its underlying graded sheaf of
> `R`-modules is that internal hom and its right `A`-action is `(f a)(y) = f (a y)`.

```lean
structure IsGradedInternalHom (N : GradedBimodule.{t, a, z} A B) (L : GradedModule.{t, a, s} B)
    (H : GradedModule.{t, a, h} A) extends IsGradedSheafHom N.toGradedModule L H.piece
```

**`SheafOfModules.balancedEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomAdjunction.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomAdjunction.lean#L361). The attribute's comment: “local homomorphisms into the internal hom are balanced bilinear families”.

> The degree-`n` local homomorphisms `M|_U → SheafHom^gr_B(N, L)|_U` of right graded
> `A`-modules are the `A`-balanced bilinear families of degree `n` over `U`. This is the local
> form of the tensor-hom adjunction.

```lean
noncomputable def balancedEquiv (hH : IsGradedInternalHom N L H)
    (M : GradedModule.{t, a, w} A) (n : ℤ) (U : C) :
    GradedLocalHom M H n U ≃ GradedLocalBalanced M N L n U
```

## Tag 0FR5, a definition

[Tag 0FR5](https://stacks.math.columbia.edu/tag/0FR5) in the Stacks Project.

**`SheafOfModules.GradedBimodule`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedBimodule.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedBimodule.lean#L59). The attribute's comment: “graded bimodules”.

> A graded `(A, B)`-bimodule is a family of sheaves of modules indexed by `ℤ` carrying
> commuting unital left `A`- and right `B`-actions.

```lean
structure GradedBimodule (A B : GradedAlgebra.{t, a} R)
```

**`SheafOfModules.GradedBimodule.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedBimodule.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedBimodule.lean#L95). The attribute's comment: “homomorphisms of graded bimodules”.

> A homomorphism of graded `(A, B)`-bimodules is a degreewise morphism of sheaves of modules
> which respects both actions.

```lean
structure Hom (M N : GradedBimodule.{t, a, m} A B)
```

## Tag 0FR6, a lemma

[Tag 0FR6](https://stacks.math.columbia.edu/tag/0FR6) in the Stacks Project.

**`SheafOfModules.tensorHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomAdjunction.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomAdjunction.lean#L390). The attribute's comment: “Hom\_\{Mod^gr(B)}(M ⊗\_A N, L) = Hom\_\{Mod^gr(A)}(M, SheafHom^gr\_B(N, L))”.

> **Tensor-hom adjunction for sheaves of graded modules**, first identity: the degree-`n`
> homomorphisms `M ⊗_A N → L` of right graded `B`-modules are the degree-`n` homomorphisms
> `M → SheafHom^gr_B(N, L)` of right graded `A`-modules.

```lean
noncomputable def tensorHomEquiv (hT : IsGradedTensorProduct M N T)
    (hH : IsGradedInternalHom N L H) (n : ℤ) :
    GradedHomOfDegree T L n ≃ GradedHomOfDegree M H n
```

**`SheafOfModules.isGradedSheafHom_tensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomAdjunction.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomAdjunction.lean#L423). The attribute's comment: “SheafHom^gr\_B(M ⊗\_A N, L) = SheafHom^gr\_A(M, SheafHom^gr\_B(N, L))”.

> **Tensor-hom adjunction for sheaves of graded modules**, second identity: a graded sheaf of
> `R`-modules which is the internal hom `SheafHom^gr_B(M ⊗_A N, L)` is also the internal hom
> `SheafHom^gr_A(M, SheafHom^gr_B(N, L))`.

```lean
noncomputable def isGradedSheafHom_tensor (hT : IsGradedTensorProduct M N T)
    (hH : IsGradedInternalHom N L H) {G : ℤ → SheafOfModules.{g} R}
    (hG : IsGradedSheafHom T L G) : IsGradedSheafHom M H G
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.8, Tag 0FR4](https://stacks.math.columbia.edu/tag/0FR4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
