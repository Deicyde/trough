---
declaration: section
origin: cited
lean: DifferentialGradedModule.homHomotopyDescent, DifferentialGradedModule.homDGFunctorData, DifferentialGradedModule.homModuleFunctor, DifferentialGradedModule.homHomotopyCategoryFunctor, DifferentialGradedModule.shiftHomIso, DifferentialGradedModule.shiftHomModuleIso, Bimod.tensorHomEquiv, Bimod.tensorHomEquiv_apply
statement: formalized
proof: formalized
---

# 22.30 Bimodules and internal hom

Section 22.30 of the Stacks Project, [Tag 0FQP](https://stacks.math.columbia.edu/tag/0FQP). 3 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FQQ, a lemma

[Tag 0FQQ](https://stacks.math.columbia.edu/tag/0FQQ) in the Stacks Project.

**`DifferentialGradedModule.homHomotopyDescent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean, line 561](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean#L561). The attribute's comment: “descent of the functor on DG modules”.

> The internal hom functor on homotopy categories is the descent of the internal hom functor on
> differential graded modules: both send `P` to the chosen presentation of `Hom^•_B(N, P)` and a
> homotopy class to the class of the postcomposition.

```lean
def homHomotopyDescent (N : DifferentialGradedModule B) (L : BimoduleStructure A B N) :
    toHomotopyCategory B ⋙ homHomotopyCategoryFunctor A B N L ≅
      homModuleFunctor A B N L ⋙ toHomotopyCategory A
```

**`DifferentialGradedModule.homDGFunctorData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/InternalHomFunctor.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/InternalHomFunctor.lean#L315). The attribute's comment: “the DG functor”.

> **Stacks 0FQQ.** The internal hom functor of a differential graded bimodule, as a functor of
> differential graded categories.

```lean
noncomputable def homDGFunctorData : HomDGFunctorData A B N L
```

**`DifferentialGradedModule.homModuleFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/InternalHomFunctor.lean, line 477](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/InternalHomFunctor.lean#L477). The attribute's comment: “the functor on DG modules”.

> **Stacks 0FQQ.** The internal hom functor on the categories of differential graded
> modules.

```lean
noncomputable def homModuleFunctor :
    DifferentialGradedModule B ⥤ DifferentialGradedModule A
```

**`DifferentialGradedModule.homHomotopyCategoryFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/InternalHomFunctor.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/InternalHomFunctor.lean#L485). The attribute's comment: “the functor on homotopy categories”.

> **Stacks 0FQQ.** The internal hom functor on the homotopy categories of differential graded
> modules.

```lean
noncomputable def homHomotopyCategoryFunctor :
    HomotopyCategory B ⥤ HomotopyCategory A
```

## Tag 0FQR, a remark

[Tag 0FQR](https://stacks.math.columbia.edu/tag/0FQR) in the Stacks Project.

**`DifferentialGradedModule.shiftHomIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/BimoduleHomShift.lean, line 1116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/BimoduleHomShift.lean#L1116).

> The canonical, sign-free isomorphism
> `Hom_B^gr(N,P)[k] ≅ Hom_B^gr(N,P[k])` of right DG `A`-modules.
> The equality says that the associated homogeneous maps have the same value
> on each homogeneous element of `N`.

```lean
public theorem shiftHomIso (k : ℤ) :
    ∃ (H : HomDGModulePresentation A B N P L)
      (Hk : HomDGModulePresentation A B N (DifferentialGradedModule.shift P k) L)
      (e : DifferentialGradedModule.shift H.module k ≅ Hk.module),
      ∀ (n p : ℤ) (f : (DifferentialGradedModule.shift H.module k).grading n)
        (x : N.grading p),
        ((Hk.homogeneousEquiv n (e.hom.gradedMap n f)).1 x : P.M) =
          (H.homogeneousEquiv (n + k)
            ⟨(f.1 : H.module.M), by
              simpa only [DifferentialGradedModule.shift_grading] using f.property⟩).1 x
```

**`DifferentialGradedModule.shiftHomModuleIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/InternalHom.lean, line 515](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/InternalHom.lean#L515).

> **Stacks 0FQR.** The canonical, sign-free isomorphism `Hom^•_B(N, P)[k] ≅ Hom^•_B(N, P[k])`
> of right differential graded `A`-modules. The displayed equation says that the homogeneous maps
> associated with corresponding elements take the same value on every homogeneous element of `N`.

```lean
theorem shiftHomModuleIso (k : ℤ) :
    ∃ (H : HomModuleData A B N P L)
      (Hk : HomModuleData A B N (shift P k) L)
      (e : shift H.module k ≅ Hk.module),
      ∀ (n p : ℤ) (f : (shift H.module k).grading n) (x : N.grading p),
        ((Hk.homogeneousEquiv n (e.hom.gradedMap n f)).1 x : P.M) =
          (H.homogeneousEquiv (n + k)
            ⟨(f.1 : H.module.M), by
              simpa only [shift_grading] using f.property⟩).1 x
```

## Tag 09LN, a lemma

[Tag 09LN](https://stacks.math.columbia.edu/tag/09LN) in the Stacks Project.

**`Bimod.tensorHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Bimod/TensorHom.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Bimod/TensorHom.lean#L132). The attribute's comment: “ordinary\_tensor\_hom”. References: SGA 4 IV (12.14), “punctual topos”.

> **Stacks 09LN, ordinary tensor--hom.**  For a right `A`-module `M`, an `(A,B)`-bimodule
> `N`, and a right `B`-module `P`, `B`-linear maps from `M ⊗_A N` to `P` are canonically the
> same as `A`-balanced maps from `M` into the `B`-linear maps from `N` to `P`.

```lean
public noncomputable def tensorHomEquiv {A B : Mon (ModuleCat.{u} R)}
    (M : Bimod (𝟙_ (Mon (ModuleCat.{u} R))) A) (N : Bimod A B)
    (P : Bimod (𝟙_ (Mon (ModuleCat.{u} R))) B) :
    rightLinearMaps (M.tensorBimod N) P ≃ₗ[R] balancedRightLinearMaps M N P
```

**`Bimod.tensorHomEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Bimod/TensorHom.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Bimod/TensorHom.lean#L248). The attribute's comment: “ordinary\_tensor\_hom”.

> The forward tensor-hom correspondence is evaluation on pure tensors.

```lean
public theorem tensorHomEquiv_apply {A B : Mon (ModuleCat.{u} R)}
    (M : Bimod (𝟙_ (Mon (ModuleCat.{u} R))) A) (N : Bimod A B)
    (P : Bimod (𝟙_ (Mon (ModuleCat.{u} R))) B)
    (f : rightLinearMaps (M.tensorBimod N) P) (m : M.X) (n : N.X) :
    (tensorHomEquiv M N P f).1 m n =
      f.1 (CategoryTheory.Limits.coequalizer.π
        (M.actRight ▷ N.X) ((α_ M.X A.X N.X).hom ≫ (M.X ◁ N.actLeft)) |>.hom
        (m ⊗ₜ[R] n))
```

**`DifferentialGraded.Bimodule.tensorCompFunctor_adj_homModuleFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorHom.lean, line 535](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorHom.lean#L535). The attribute's comment: “the differential graded case in degree zero”.

> **Stacks 09LN, the differential graded case.** Tensoring with a differential graded
> `(A, B)`-bimodule `N` is left adjoint to the internal hom out of `N`, as functors between the
> categories of differential graded modules:
> `Hom_{Mod^{dg}_{(B,d)}}(M ⊗_A N, P) = Hom_{Mod^{dg}_{(A,d)}}(M, Hom^•_B(N, P))`,
> naturally in `M` and `P`.
>
> This is the degree-zero part of the source's isomorphism of Hom complexes — the bijection of the
> morphism groups of the two categories of differential graded modules — which is why the tag is
> part-qualified.

```lean
def tensorCompFunctor_adj_homModuleFunctor (N : Bimodule A B) :
    tensorCompFunctor N ⊣ homModuleFunctor A B N.rightModule N.leftAction
```

**`DifferentialGraded.Bimodule.tensorHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorHom.lean, line 550](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorHom.lean#L550). The attribute's comment: “the differential graded case in degree zero, as a bijection”.

> **Stacks 09LN, the differential graded case**, as the bijection of morphism groups
> `Hom_{Mod^{dg}_{(B,d)}}(M ⊗_A N, P) = Hom_{Mod^{dg}_{(A,d)}}(M, Hom^•_B(N, P))`. It is natural
> in `M` and `P`, being the hom-set bijection of
> `DifferentialGraded.Bimodule.tensorCompFunctor_adj_homModuleFunctor`.

```lean
def tensorHomEquiv (N : Bimodule A B) (M : DifferentialGradedModule A)
    (P : DifferentialGradedModule B) :
    ((tensorCompFunctor N).obj M ⟶ P) ≃
      (M ⟶ (homModuleFunctor A B N.rightModule N.leftAction).obj P)
```

**`DifferentialGraded.Bimodule.tensorHomotopyFunctor_adj_homHomotopyCategoryFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorHom.lean, line 569](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorHom.lean#L569). The attribute's comment: “the differential graded case in degree zero, on the homotopy categories”. References: SGA 5 IIIB (5.2), “partial”.

> **Stacks 09LN for differential graded modules, on the homotopy categories.** Tensoring with a
> differential graded `(A, B)`-bimodule `N` is left adjoint to the internal hom out of `N` as
> functors `K(A, d) ⥤ K(B, d)` and `K(B, d) ⥤ K(A, d)`.
>
> This is the adjunction on the categories of differential graded modules, descended along the
> passage to homotopy classes: both functors are compatible with it, by Tag 09LM
> (`DifferentialGraded.Bimodule.tensorCompFunctor_quotient`) and Tag 0FQQ
> (`DifferentialGradedModule.homHomotopyDescent`), and an adjunction descends to a quotient
> category by `CategoryTheory.Quotient.adjunctionOfSquares`.

```lean
def tensorHomotopyFunctor_adj_homHomotopyCategoryFunctor (N : Bimodule A B) :
    tensorHomotopyFunctor N ⊣ homHomotopyCategoryFunctor A B N.rightModule N.leftAction
```

**`DifferentialGraded.Bimodule.exists_tensorHomComplexIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorHom.lean, line 981](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorHom.lean#L981). The attribute's comment: “the differential graded case in every degree, as an isomorphism of Hom complexes”.

> **Stacks 09LN, in every degree.** For a right differential graded `A`-module `M`, a
> differential graded `(A, B)`-bimodule `N` and a right differential graded `B`-module `P` the two
> Hom complexes
>
> `Hom^•_{Mod^{dg}_{(B, d)}}(M ⊗_A N, P)`  and  `Hom^•_{Mod^{dg}_{(A, d)}}(M, Hom^•_B(N, P))`
>
> are isomorphic as complexes of `R`-modules: in each degree `n` the homogeneous right-`B`-linear
> maps `M ⊗_A N → P` of degree `n` correspond `R`-linearly to the homogeneous right-`A`-linear maps
> `M → Hom^•_B(N, P)` of degree `n`, by restriction to the pure tensors, and the correspondence
> commutes with the differentials of the two Hom complexes.
>
> The correspondence is pinned by its value on pure tensors, which is what the first displayed
> property says: the homogeneous map that the image of `ψ` at a homogeneous `x` presents sends `y`
> to `ψ (x ⊗ y)`. That property determines it, since the pure tensors generate `M ⊗_A N`.
>
> The degree-zero part is `DifferentialGraded.Bimodule.tensorHomEquiv`, which is the bijection of
> morphism groups of the two categories of differential graded modules; the statement here is the
> isomorphism of Hom complexes that the source asserts, of which that bijection is the part given
> by the closed elements of degree zero.

```lean
theorem exists_tensorHomComplexIso (N : Bimodule A B) (M : DifferentialGradedModule A)
    (P : DifferentialGradedModule B) :
    ∃ e : ∀ n : ℤ, HomogeneousMap B (tensorObj N M) P n ≃ₗ[R]
        HomogeneousMap A M (homPresentation N P).module n,
      (∀ (n p : ℤ) (ψ : HomogeneousMap B (tensorObj N M) P n) (x : M.M)
          (hx : x ∈ M.grading p) (y : N.rightModule.M),
        ((homPresentation N P).homogeneousEquiv (p + n)
            ⟨(e n ψ).1 x, (e n ψ).2.1 p x hx⟩).1 y =
          ψ.1 (((tensorDGFunctor N).pure M).toLinearMap x y)) ∧
        ∀ (n : ℤ) (ψ : HomogeneousMap B (tensorObj N M) P n),
          e (n + 1) (homogeneousMapDifferential B ψ) =
            homogeneousMapDifferential A (e n ψ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.30, Tag 0FQP](https://stacks.math.columbia.edu/tag/0FQP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
