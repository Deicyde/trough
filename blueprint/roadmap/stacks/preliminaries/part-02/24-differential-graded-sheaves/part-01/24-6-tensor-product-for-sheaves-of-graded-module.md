---
declaration: section
origin: cited
lean: SheafOfModules.RelativeTensor.balanceMap, SheafOfModules.RelativeTensor.gradedTensor, SheafOfModules.RelativeTensor.gradedTensorFunctor, SheafOfModules.RelativeTensor.gradedTensorMapRightOfDegree, SheafOfModules.RelativeTensor.gradedTensorMapRightOfDegree_comp, SheafOfModules.RelativeTensor.unitorIso, SheafOfModules.RelativeTensor.isGradedFlat_regularModule, SheafOfModules.GradedLocalBalanced
statement: formalized
proof: formalized
---

# 24.6 Tensor product for sheaves of graded modules

Section 24.6 of the Stacks Project, [Tag 0FR2](https://stacks.math.columbia.edu/tag/0FR2). 1 tag here is carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FR2, the section

[Tag 0FR2](https://stacks.math.columbia.edu/tag/0FR2) in the Stacks Project.

**`SheafOfModules.RelativeTensor.balanceMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedRelativeTensor.lean, line 734](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedRelativeTensor.lean#L734). The attribute's comment: “the map of the presentation, sending `x ⊗ a ⊗ y` to `xa ⊗ y - x ⊗ ay`”.

> The balance map `⨁_{r+s+t=n} P^r ⊗_O A^s ⊗_O N^t ⟶ ⨁_{p+q=n} P^p ⊗_O N^q` of degree `n`,
> sending `x ⊗ a ⊗ y` to `xa ⊗ y - x ⊗ ay`.

```lean
noncomputable def balanceMap (n : ℤ) : relationSum P N n ⟶ tensorSum P N n
```

**`SheafOfModules.RelativeTensor.gradedTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedRelativeTensor.lean, line 761](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedRelativeTensor.lean#L761). The attribute's comment: “degree `n` of the graded tensor product, as the cokernel of the balance map”.

> Degree `n` of the relative tensor product `P ⊗_A N` of a right graded `A`-module with a left
> graded `A`-module: the associated sheaf of the cokernel of the balance map.

```lean
noncomputable def gradedTensor (n : ℤ) : SheafOfModules.{m} (toRingCat J Osharp)
```

**`SheafOfModules.RelativeTensor.gradedTensorFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedRelativeTensor.lean, line 1031](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedRelativeTensor.lean#L1031). The attribute's comment: “the functor `- ⊗_A N` on right graded modules”.

> The functor `- ⊗_A N` from right graded `A`-modules to graded `O`-modules, for a fixed left
> graded `A`-module `N`.

```lean
noncomputable def gradedTensorFunctor :
    GradedModule.{t, m, m} A ⥤ GradedObject ℤ (SheafOfModules.{m} (toRingCat J Osharp))
```

**`SheafOfModules.RelativeTensor.gradedTensorMapRightOfDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedRelativeTensorOfDegree.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedRelativeTensorOfDegree.lean#L132). The attribute's comment: “`- ⊗_A N` as a functor of graded categories: the map of degree `d` induced by a homomorphism of degree `d`”.

> **`- ⊗_A N` on homomorphisms of degree `d`.** The component `(P ⊗_A N)^n → (P' ⊗_A N)^k`,
> for `n + d = k`, of the map of degree `d` induced by a homomorphism `f : P → P'` of right graded
> `A`-modules homogeneous of degree `d`; it sends `x ⊗ y` to `f(x) ⊗ y`.

```lean
noncomputable def gradedTensorMapRightOfDegree {n k : ℤ} (hk : n + d = k) :
    gradedTensor P N n ⟶ gradedTensor P' N k
```

**`SheafOfModules.RelativeTensor.gradedTensorMapRightOfDegree_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedRelativeTensorOfDegree.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedRelativeTensorOfDegree.lean#L171). The attribute's comment: “`- ⊗_A N` as a functor of graded categories: compatibility with composition”.

> **`- ⊗_A N` preserves composition of the graded category.** For `f : P → P'` homogeneous of
> degree `d` and `g : P' → P''` homogeneous of degree `e`, the map of degree `d + e` induced by the
> composite `g ∘ f` is the composite of the maps induced by `f` and by `g`.

```lean
theorem gradedTensorMapRightOfDegree_comp {P P' P'' : GradedModule.{t, m, m} A} {d e : ℤ}
    (f : GradedHomOfDegree P P' d) (g : GradedHomOfDegree P' P'' e)
    (N : LeftGradedModule.{t, m, m} A) {n j k : ℤ} (hj : n + d = j) (hk : j + e = k) :
    gradedTensorMapRightOfDegree (g.comp f) N (show n + (d + e) = k by omega) =
      gradedTensorMapRightOfDegree f N hj ≫ gradedTensorMapRightOfDegree g N hk
```

**`SheafOfModules.RelativeTensor.unitorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedRelativeTensorUnitor.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedRelativeTensorUnitor.lean#L298). The attribute's comment: “the unit isomorphism A ⊗\_A N ≅ N of the relative tensor product, in degree n”.

> **The unit isomorphism of the relative tensor product**: `A ⊗_A N ≅ N` in degree `n`, for `A`
> a sheaf of graded algebras acting on itself on the right and `N` a left graded `A`-module.

```lean
noncomputable def unitorIso (n : ℤ) :
    gradedTensor (GradedModule.regularModule A) N n ≅ N.piece n
```

**`SheafOfModules.RelativeTensor.isGradedFlat_regularModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedRelativeTensorUnitor.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedRelativeTensorUnitor.lean#L337). The attribute's comment: “the regular right graded module is flat, by the unit isomorphism”.

> **A sheaf of graded algebras is flat as a right graded module over itself.** The functor
> `N ↦ A ⊗_A N` is isomorphic to the identity by `SheafOfModules.RelativeTensor.unitorIso`, so it
> carries a degreewise short exact sequence to a degreewise short exact sequence.

```lean
theorem isGradedFlat_regularModule (A : GradedAlgebra.{t, m} (toRingCat J Osharp)) :
    IsGradedFlat (GradedModule.regularModule A)
```

**`SheafOfModules.GradedLocalBalanced`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorProduct.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorProduct.lean#L89). The attribute's comment: “local balanced bilinear families out of a graded module and a bimodule”.

> An `A`-balanced bilinear family of degree `n` over an object `U` of the site, from a right
> graded `A`-module `M` and a graded `(A, B)`-bimodule `N` to a right graded `B`-module `L`: maps
> `M^i|_U × N^j|_U → L^{i + j + n}|_U` which are bilinear over the sheaf of rings, compatible with
> restriction, `A`-balanced and `B`-linear in the second variable.

```lean
structure GradedLocalBalanced (M : GradedModule.{t, a, w} A) (N : GradedBimodule.{t, a, z} A B)
    (L : GradedModule.{t, a, s} B) (n : ℤ) (U : C)
```

**`SheafOfModules.GradedGlobalBalanced`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorProduct.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorProduct.lean#L208). The attribute's comment: “balanced bilinear families out of a graded module and a bimodule”.

> An `A`-balanced bilinear family of degree `n` over the whole site: maps
> `M^i × N^j → L^{i + j + n}` on sections which are bilinear over the sheaf of rings, compatible
> with restriction, `A`-balanced and `B`-linear in the second variable.

```lean
structure GradedGlobalBalanced (M : GradedModule.{t, a, w} A) (N : GradedBimodule.{t, a, z} A B)
    (L : GradedModule.{t, a, s} B) (n : ℤ)
```

**`SheafOfModules.IsGradedTensorProduct`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorProduct.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorProduct.lean#L292). The attribute's comment: “the graded tensor product, by its universal property”.

> A right graded `B`-module `T` is the tensor product `M ⊗_A N` of a right graded `A`-module
> `M` with a graded `(A, B)`-bimodule `N` when it carries an `A`-balanced bilinear map `tmul` of
> degree zero whose right `B`-action is `(x ⊗ y) b = x ⊗ y b` and which is universal: composing a
> degree-`n` local homomorphism out of `T` with `tmul` is a bijection onto the `A`-balanced
> bilinear families of degree `n`.

```lean
structure IsGradedTensorProduct (M : GradedModule.{t, a, w} A)
    (N : GradedBimodule.{t, a, z} A B) (T : GradedModule.{t, a, s} B)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.6, Tag 0FR2](https://stacks.math.columbia.edu/tag/0FR2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
