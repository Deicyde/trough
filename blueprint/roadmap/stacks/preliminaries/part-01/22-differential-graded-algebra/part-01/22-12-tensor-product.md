---
declaration: section
origin: cited
lean: DifferentialGraded.tensorComplex, DifferentialGraded.tensorTmul, DifferentialGraded.tensorHomEquiv, DifferentialGraded.tensorDegEquivCoker, DifferentialGraded.balancedTensorGradedEquiv, DifferentialGraded.balancedTensorGradedEquiv_lof_tmul, DifferentialGraded.gradedTensorHomEquiv, StacksDraft.BalancedTensorProduct
statement: formalized
proof: formalized
---

# 22.12 Tensor product

Section 22.12 of the Stacks Project, [Tag 09LL](https://stacks.math.columbia.edu/tag/09LL). 1 tag here is carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09LL, the section

[Tag 09LL](https://stacks.math.columbia.edu/tag/09LL) in the Stacks Project.

**`DifferentialGraded.tensorComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BalancedTensor.lean, line 375](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BalancedTensor.lean#L375). The attribute's comment: “M ⊗\_A N is a differential graded R-module”.

> The tensor product `M' ⊗_A M` of a right and a left differential graded `A`-module, as a
> complex of `R`-modules with differential `d (x ⊗ y) = d x ⊗ y + (-1)^p x ⊗ d y`. Its degree-`n`
> term is the degree-`n` piece of the balanced tensor product of the underlying modules
> (`DifferentialGraded.balancedTensorGradedEquiv`).

```lean
noncomputable def tensorComplex : CochainComplex (ModuleCat.{u} R) ℤ
```

**`DifferentialGraded.tensorTmul`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BalancedTensor.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BalancedTensor.lean#L390). The attribute's comment: “the map M × N → M ⊗\_A N in the differential graded case”.

> The universal balanced bilinear map `(x, y) ↦ x ⊗ y` into `M' ⊗_A M`: it is `A`-balanced,
> compatible with the gradings and compatible with the differentials.

```lean
noncomputable def tensorTmul : BalancedBilinear M' M (tensorComplex M' M)
```

**`DifferentialGraded.tensorHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BalancedTensor.lean, line 506](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BalancedTensor.lean#L506). The attribute's comment: “DifferentialGradedBilinear\_A(M × N, Q) = Hom\_\{Comp(R)}(M ⊗\_A N, Q)”.

> **The universal property of `M' ⊗_A M`.** Maps of complexes of `R`-modules out of
> `M' ⊗_A M` are the balanced bilinear maps out of `M'` and `M`:
> `DifferentialGradedBilinear_A(M' × M, Q) = Hom_{Comp(R)}(M' ⊗_A M, Q)`.

```lean
noncomputable def tensorHomEquiv (Q : CochainComplex (ModuleCat.{u} R) ℤ) :
    (tensorComplex M' M ⟶ Q) ≃ BalancedBilinear M' M Q
```

**`DifferentialGraded.tensorDegEquivCoker`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BalancedTensorGraded.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BalancedTensorGraded.lean#L201). The attribute's comment: “the n-th graded piece of M ⊗\_A N is the cokernel”.

> The degree-`n` piece of `M' ⊗_A M` is the cokernel of `tensorRelMap`, the map
> `⨁_{r + t + s = n} (M')^r ⊗_R A^t ⊗_R M^s → ⨁_{p + q = n} (M')^p ⊗_R M^q` sending
> `x ⊗ a ⊗ y` to `x ⊗ a y - x a ⊗ y`.

```lean
noncomputable def tensorDegEquivCoker (n : ℤ) :
    tensorDeg M' M n ≃ₗ[R] tensorRaw M' M n ⧸ LinearMap.range (tensorRelMap M' M n)
```

**`DifferentialGraded.balancedTensorGradedEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BalancedTensorGraded.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BalancedTensorGraded.lean#L318). The attribute's comment: “M ⊗\_A N is a graded R-module”.

> **`M' ⊗_A M` is a graded `R`-module.** The balanced tensor product `M' ⊗_A M` of the
> underlying modules is the direct sum of the pieces `tensorDeg M' M n`, the degree-`n` piece
> being the cokernel of `tensorRelMap` (`tensorDegEquivCoker`).

```lean
noncomputable def balancedTensorGradedEquiv :
    (⨁ n : ℤ, tensorDeg M' M n) ≃ₗ[R] StacksDraft.BalancedTensorProduct R A.A M'.M M.M
```

**`DifferentialGraded.balancedTensorGradedEquiv_lof_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BalancedTensorGraded.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BalancedTensorGraded.lean#L352). The attribute's comment: “the map M × N → M ⊗\_A N is compatible with gradings”.

> Under `balancedTensorGradedEquiv`, the class of a homogeneous `x ⊗ y` in degree `p + q` is
> the symbol `x ⊗ y` of `M' ⊗_A M`: the universal map `M' × M → M' ⊗_A M` is compatible with the
> gradings.

```lean
theorem balancedTensorGradedEquiv_lof_tmul (p q n : ℤ) (h : p + q = n) (x : M'.grading p)
    (y : M.grading q) :
    balancedTensorGradedEquiv M' M (DirectSum.lof R ℤ (fun n => tensorDeg M' M n) n
        ((tensorRel M' M n).mkQ (tensorMk M' M n p q h x y))) =
      StacksDraft.BalancedTensorProduct.tmul R A.A M'.M M.M x y
```

**`DifferentialGraded.gradedTensorHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BalancedTensorGraded.lean, line 442](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BalancedTensorGraded.lean#L442). The attribute's comment: “GradedBilinear\_A(M × N, Q) = Hom\_\{graded R-modules}(M ⊗\_A N, Q)”.

> **The universal property of the graded tensor product.** Maps of graded `R`-modules from
> `M' ⊗_A M` (with the pieces `tensorDeg M' M n` of `balancedTensorGradedEquiv`) to a graded
> `R`-module with pieces `Q n` are the graded `A`-balanced bilinear maps `M' × M → Q`:
> `GradedBilinear_A(M' × M, Q) = Hom_{graded R-modules}(M' ⊗_A M, Q)`.

```lean
noncomputable def gradedTensorHomEquiv (Q : ℤ → Type u) [∀ n, AddCommGroup (Q n)]
    [∀ n, Module R (Q n)] :
    (∀ n : ℤ, tensorDeg M' M n →ₗ[R] Q n) ≃ GradedBalancedBilinear M' M Q
```

**`StacksDraft.BalancedTensorProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/BalancedTensorProduct.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/BalancedTensorProduct.lean#L104). The attribute's comment: “the tensor product”.

> The tensor product `M ⊗_A N` of a right `A`-module `M` and a left `A`-module `N`: the quotient
> of `M ⊗_R N` by the balancing relations `x a ⊗ y - x ⊗ a y`.

```lean
def BalancedTensorProduct : Type (max w w')
```

**`StacksDraft.BalancedTensorProduct.tmul`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/BalancedTensorProduct.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/BalancedTensorProduct.lean#L123). The attribute's comment: “the universal bilinear map”.

> The universal `A`-balanced bilinear map `(x, y) ↦ x ⊗ y` of `M ⊗_A N`.

```lean
def tmul : M →ₗ[R] N →ₗ[R] BalancedTensorProduct R A M N
```

**`StacksDraft.BalancedTensorProduct.tmul_balanced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/BalancedTensorProduct.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/BalancedTensorProduct.lean#L134). The attribute's comment: “the balancing relation”.

> The universal map is `A`-balanced: `x a ⊗ y = x ⊗ a y`. This is the balancing relation the
> tensor product is defined by.

```lean
theorem tmul_balanced : IsBalancedBilinear A (tmul R A M N)
```

**`StacksDraft.BalancedTensorProduct.span_tmul_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/BalancedTensorProduct.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/BalancedTensorProduct.lean#L155). The attribute's comment: “generated by the symbols x ⊗ y”.

> As an `R`-module, `M ⊗_A N` is generated by the symbols `x ⊗ y`.

```lean
theorem span_tmul_eq_top :
    Submodule.span R (Set.range fun p : M × N => tmul R A M N p.1 p.2) = ⊤
```

**`StacksDraft.BalancedTensorProduct.liftEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/BalancedTensorProduct.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/BalancedTensorProduct.lean#L266). The attribute's comment: “Bilinear\_A(M × N, Q) = Hom\_R(M ⊗\_A N, Q)”. References: EGA III (7.2.1).

> The identification `Bilinear_A(M × N, Q) = Hom_R(M ⊗_A N, Q)`: composing with the universal
> map `(x, y) ↦ x ⊗ y` is an `R`-linear bijection from the `R`-linear maps out of `M ⊗_A N` onto the
> `A`-balanced `R`-bilinear maps `M × N → Q`.

```lean
def liftEquiv (Q : Type t) [AddCommGroup Q] [Module R Q] :
    balancedBilinearMaps R A M N Q ≃ₗ[R] (BalancedTensorProduct R A M N →ₗ[R] Q)
```

**`StacksDraft.Perfect.preservesColimits_balancedTensorFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/BalancedDerivedTensor.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/BalancedDerivedTensor.lean#L436). The attribute's comment: “right exactness and commutation with colimits in the left-module variable”.

> Balanced tensoring with a fixed right `Λ`-module commutes with arbitrary colimits; in
> particular it is right exact. This is because it is a left adjoint, its right adjoint being
> `Q ↦ Hom_ℤ(N, Q)`. Colimits of `R`-modules are computed on the underlying abelian groups, so
> this is also the statement for the `R`-module `N ⊗_Λ M` when `Λ` is an `R`-algebra.

```lean
theorem preservesColimits_balancedTensorFunctor_obj (N : ModuleCat.{v} (MulOpposite Λ)) :
    PreservesColimits ((balancedTensorFunctor Λ).obj N)
```

**`StacksDraft.Perfect.preservesColimits_balancedTensorFunctor_flip_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/BalancedDerivedTensor.lean, line 568](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/BalancedDerivedTensor.lean#L568). The attribute's comment: “right exactness and commutation with colimits in the right-module variable”.

> Balanced tensoring with a fixed left `Λ`-module commutes with arbitrary colimits; in
> particular it is right exact. This is because it is a left adjoint, its right adjoint being
> `Q ↦ Hom_ℤ(M, Q)`. Together with `preservesColimits_balancedTensorFunctor_obj` this is the
> statement in each variable.

```lean
theorem preservesColimits_balancedTensorFunctor_flip_obj (M : ModuleCat.{v} Λ) :
    PreservesColimits ((balancedTensorFunctor Λ).flip.obj M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.12, Tag 09LL](https://stacks.math.columbia.edu/tag/09LL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
