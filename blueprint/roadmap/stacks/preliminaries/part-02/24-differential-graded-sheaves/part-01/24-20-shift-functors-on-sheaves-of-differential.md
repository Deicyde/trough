---
declaration: section
origin: cited
lean: SheafOfModules.DifferentialGradedModule.dgShiftFunctor, SheafOfModules.DifferentialGradedModule.dgShiftFunctor_complex, SheafOfModules.DifferentialGradedModule.dgShiftFunctor_map_v, SheafOfModules.DifferentialGradedModule.dgShiftFunctor_map_v_of_degree_zero, SheafOfModules.DifferentialGradedModule.dgShiftFunctor_zero_obj, SheafOfModules.DifferentialGradedModule.dgShiftFunctor_add_obj, SheafOfModules.DifferentialGradedModule.dgShiftFunctor_add_map, SheafOfModules.DifferentialGradedModule.dgShiftHomEquiv
statement: formalized
proof: formalized
---

# 24.20 Shift functors on sheaves of differential graded modules

Section 24.20 of the Stacks Project, [Tag 0FRY](https://stacks.math.columbia.edu/tag/0FRY). 1 tag here is carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FRY, the section

[Tag 0FRY](https://stacks.math.columbia.edu/tag/0FRY) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.dgShiftFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean#L105). The attribute's comment: “the shift functor [k] on Mod^dg(A, d)”.

> **Stacks Project, Tag 0FRY.** The `k`-th shift functor `[k]` on the differential graded
> category `Mod^dg(A, d)` of right differential graded `A`-modules: a functor of differential
> graded categories, so additive and linear on `Hom` modules and compatible with the differential,
> the composition and the identities.

```lean
noncomputable def dgShiftFunctor (k : ℤ) :
    DGCategory.DGFunctor (dgCategoryData.{u, v, w} A).category
      (dgCategoryData.{u, v, w} A).category
```

**`SheafOfModules.DifferentialGradedModule.dgShiftFunctor_complex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean#L113). The attribute's comment: “clauses (1) and (2): the underlying complex of M[k]”.

> **Stacks Project, Tag 0FRY, clauses (1) and (2).** The complex of sheaves of modules
> underlying `M[k]` is the `k`-th shift of the complex underlying `M`.

```lean
theorem dgShiftFunctor_complex (k : ℤ) (M : DifferentialGradedModule.{u, v, w} A) :
    (asModule A ((dgShiftFunctor.{u, v, w} A k).obj (asObject A M))).complex =
      (CochainComplex.shiftFunctor
        (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) k).obj M.complex
```

**`SheafOfModules.DifferentialGradedModule.dgShiftFunctor_map_v`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean#L149). The attribute's comment: “the components of f[k]”.

> **Stacks Project, Tag 0FRY.** The components of the shift `f[k]` of a homogeneous morphism
> `f` of degree `n` are those of `f`, multiplied by `(-1)^{k n}`. See the implementation notes:
> the sign is forced by the requirement that `[k]` be a functor of differential graded
> categories, and it is `+1` in the degree the source's clause is about.

```lean
theorem dgShiftFunctor_map_v (k n : ℤ) (M N : DifferentialGradedModule.{u, v, w} A)
    (f : (dgCategoryData.{u, v, w} A).category.Hom (asObject A M) (asObject A N) n)
    (p q : ℤ) (h : p + n = q) :
    HEq ((asCochain A ((dgShiftFunctor.{u, v, w} A k).map f)).v p q h)
      ((Int.negOnePow (k * n) : ℤ) • (asCochain A f).v (p + k) (q + k) (by omega))
```

**`SheafOfModules.DifferentialGradedModule.dgShiftFunctor_map_v_of_degree_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean#L160). The attribute's comment: “f[k] has the same component maps as f in degree zero”.

> **Stacks Project, Tag 0FRY.** On a homogeneous morphism of degree zero — in particular on a
> morphism of `Mod(A, d)` — the shift `f[k]` has literally the same component maps as `f`, which
> is the source's formulation.

```lean
theorem dgShiftFunctor_map_v_of_degree_zero (k : ℤ)
    (M N : DifferentialGradedModule.{u, v, w} A)
    (f : (dgCategoryData.{u, v, w} A).category.Hom (asObject A M) (asObject A N) 0)
    (p q : ℤ) (h : p + 0 = q) :
    HEq ((asCochain A ((dgShiftFunctor.{u, v, w} A k).map f)).v p q h)
      ((asCochain A f).v (p + k) (q + k) (by omega))
```

**`SheafOfModules.DifferentialGradedModule.dgShiftFunctor_zero_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean#L174). The attribute's comment: “[0] is the identity”.

> **Stacks Project, Tag 0FRY.** The zeroth shift is the identity on objects.

```lean
theorem dgShiftFunctor_zero_obj (M : (dgCategoryData.{u, v, w} A).category.Obj) :
    (dgShiftFunctor.{u, v, w} A 0).obj M = M
```

**`SheafOfModules.DifferentialGradedModule.dgShiftFunctor_add_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean#L186). The attribute's comment: “[k + l] = [k] ∘ [l]”.

> **Stacks Project, Tag 0FRY.** `[k + l] = [k] ∘ [l]` on objects.

```lean
theorem dgShiftFunctor_add_obj (k l : ℤ) (M : (dgCategoryData.{u, v, w} A).category.Obj) :
    (dgShiftFunctor.{u, v, w} A (k + l)).obj M =
      (dgShiftFunctor.{u, v, w} A k).obj ((dgShiftFunctor.{u, v, w} A l).obj M)
```

**`SheafOfModules.DifferentialGradedModule.dgShiftFunctor_add_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean#L193). The attribute's comment: “[k + l] = [k] ∘ [l] on morphisms”.

> **Stacks Project, Tag 0FRY.** `[k + l] = [k] ∘ [l]` on homogeneous morphisms.

```lean
theorem dgShiftFunctor_add_map (k l : ℤ) {M N : (dgCategoryData.{u, v, w} A).category.Obj}
    {n : ℤ} (f : (dgCategoryData.{u, v, w} A).category.Hom M N n) :
    HEq ((dgShiftFunctor.{u, v, w} A (k + l)).map f)
      ((dgShiftFunctor.{u, v, w} A k).map ((dgShiftFunctor.{u, v, w} A l).map f))
```

**`SheafOfModules.DifferentialGradedModule.dgShiftHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean#L204). The attribute's comment: “Hom(L, M[k]) = Hom(L, M)[k]”.

> **Stacks Project, Tag 0FRY.** The identification `Hom(L, M[k])^n = Hom(L, M)^{n + k}`, as
> modules over the global sections of the structure sheaf.

```lean
noncomputable def dgShiftHomEquiv (k : ℤ) (L M : (dgCategoryData.{u, v, w} A).category.Obj)
    (n : ℤ) :
    (dgCategoryData.{u, v, w} A).category.Hom L M (n + k) ≃ₗ[(limit X.O.obj : CommRingCat.{u})]
      (dgCategoryData.{u, v, w} A).category.Hom L ((dgShiftFunctor.{u, v, w} A k).obj M) n
```

**`SheafOfModules.DifferentialGradedModule.dgShiftHomEquiv_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedShiftFunctor.lean#L214). The attribute's comment: “Hom(L, M[k]) = Hom(L, M)[k] is compatible with the differentials”.

> **Stacks Project, Tag 0FRY.** The identification `Hom(L, M[k]) = Hom(L, M)[k]` is compatible
> with the differentials: on the right hand side the differential of a shifted complex carries the
> sign `(-1)^k`.

```lean
theorem dgShiftHomEquiv_d (k : ℤ) (L M : (dgCategoryData.{u, v, w} A).category.Obj) (n : ℤ)
    (f : (dgCategoryData.{u, v, w} A).category.Hom L M (n + k)) :
    dgShiftHomEquiv.{u, v, w} A k L M (n + 1)
        ((dgCategoryData.{u, v, w} A).category.d' (by omega : (n + k) + 1 = (n + 1) + k) f) =
      (-1 : (limit X.O.obj : CommRingCat.{u})) ^ k.natAbs •
        (dgCategoryData.{u, v, w} A).category.d (dgShiftHomEquiv.{u, v, w} A k L M n f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.20, Tag 0FRY](https://stacks.math.columbia.edu/tag/0FRY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
