---
declaration: section
origin: cited
lean: SheafOfModules.GradedModule.semilinearHomOfDegreeEquiv, SheafOfModules.GradedModule.pushforwardObj, SheafOfModules.GradedModule.pushforwardMap, SheafOfModules.GradedModule.pushforwardFunctor, SheafOfModules.GradedModule.pushforwardHomOfDegree, SheafOfModules.GradedModule.semilinearHomEquiv, SheafOfModules.GradedModule.pullbackHomOfDegreeEquiv
statement: formalized
proof: formalized
---

# 24.9 Pull and push for sheaves of graded modules

Section 24.9 of the Stacks Project, [Tag 0FR7](https://stacks.math.columbia.edu/tag/0FR7). 2 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FR7, the section

[Tag 0FR7](https://stacks.math.columbia.edu/tag/0FR7) in the Stacks Project.

**`SheafOfModules.GradedModule.semilinearHomOfDegreeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModulePullback.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModulePullback.lean#L442). The attribute's comment: “f\_*M corepresents the φ-semilinear homomorphisms into M homogeneous of degree n, the morphisms of the graded category Mod^gr”.

> **`f_*M` corepresents the `φ`-semilinear homomorphisms into `M` homogeneous of degree `n`**:
> such a homomorphism out of `N` is exactly a homomorphism `N ⟶ f_*M` of right graded `B`-modules
> homogeneous of degree `n`.

```lean
noncomputable def semilinearHomOfDegreeEquiv (N : GradedModule.{t, a', m} B)
    (M : GradedModule.{t, a, m} A) (n : ℤ) :
    SemilinearHomOfDegree φ N M n ≃ GradedHomOfDegree N (pushforwardObj φ M) n
```

**`SheafOfModules.GradedModule.pushforwardObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean#L187). The attribute's comment: “the direct image f\_*M of a graded module, with multiplication f\_*μ ∘ (id, φ)”.

> The direct image `f_*M` of a right graded `A`-module along a morphism of ringed sites and a
> homomorphism `φ : B ⟶ f_*A` of sheaves of graded algebras: its degree-`n` piece is the direct
> image of the degree-`n` piece of `M`, and a homogeneous section `b` of `B` acts through
> `φ b`.

```lean
noncomputable def pushforwardObj (φ : GradedAlgebra.SemilinearHom u σ B A)
    (M : GradedModule.{t, a, m} A) : GradedModule.{t, a', m} B
```

**`SheafOfModules.GradedModule.pushforwardMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean#L228). The attribute's comment: “the direct image is functorial in the graded module”.

> The direct image of a homomorphism of right graded `A`-modules is its degreewise direct
> image.

```lean
noncomputable def pushforwardMap (φ : GradedAlgebra.SemilinearHom u σ B A)
    {M N : GradedModule.{t, a, m} A} (g : M ⟶ N) :
    pushforwardObj φ M ⟶ pushforwardObj φ N
```

**`SheafOfModules.GradedModule.pushforwardFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean#L244). The attribute's comment: “the functor f\_* : Mod(A) ⥤ Mod(B)”.

> The direct image functor `f_* : Mod(A) ⥤ Mod(B)` on sheaves of graded modules.

```lean
noncomputable def pushforwardFunctor (φ : GradedAlgebra.SemilinearHom u σ B A) :
    GradedModule.{t, a, m} A ⥤ GradedModule.{t, a', m} B
```

**`SheafOfModules.GradedModule.pushforwardHomOfDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean#L273). The attribute's comment: “f\_* as a functor of graded categories, on homogeneous morphisms of degree n”.

> The direct image of a homomorphism of right graded `A`-modules homogeneous of degree `n`:
> the degreewise direct image again, which is homogeneous of degree `n`. This is the action on
> morphisms of the induced functor `f_* : Mod^gr(A) ⥤ Mod^gr(B)` of graded categories, whose
> action on objects is `SheafOfModules.GradedModule.pushforwardObj`.

```lean
noncomputable def pushforwardHomOfDegree (φ : GradedAlgebra.SemilinearHom u σ B A)
    {M L : GradedModule.{t, a, m} A} {n : ℤ} (g : GradedHomOfDegree M L n) :
    GradedHomOfDegree (pushforwardObj φ M) (pushforwardObj φ L) n
```

**`SheafOfModules.GradedModule.semilinearHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean#L350). The attribute's comment: “f\_*M corepresents the φ-semilinear homomorphisms into M”.

> **A `φ`-semilinear homomorphism `P ⟶ M` is exactly a homomorphism `P ⟶ f_*M` of right graded
> `B`-modules.**

```lean
noncomputable def semilinearHomEquiv (φ : GradedAlgebra.SemilinearHom u σ B A)
    (P : GradedModule.{t, a', m} B) (M : GradedModule.{t, a, m} A) :
    SemilinearHom φ P M ≃ (P ⟶ pushforwardObj φ M)
```

## Tag 0FR8, a lemma

[Tag 0FR8](https://stacks.math.columbia.edu/tag/0FR8) in the Stacks Project.

**`SheafOfModules.GradedModule.pullbackHomOfDegreeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModulePullbackConstruction.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModulePullbackConstruction.lean#L217). The attribute's comment: “Hom\_\{Mod^gr(B)}(N, f\_*M) = Hom\_\{Mod^gr(A)}(f^*N, M), in every homogeneous degree, for the pullback f^* of sheaves of graded modules obtained as the left adjoint of the direct image”.

> **Tag 0FR8**: for a morphism of ringed sites `f`, a sheaf of graded `R`-algebras `A` on the
> source, a sheaf of graded `R'`-algebras `B` on the target and a homomorphism `φ : B ⟶ f_*A` of
> sheaves of graded algebras, the homomorphisms `f^*N ⟶ M` of right graded `A`-modules homogeneous
> of degree `n` are exactly the homomorphisms `N ⟶ f_*M` of right graded `B`-modules homogeneous
> of degree `n`:
>
> `Hom_{Mod^gr(B)}(N, f_*M) = Hom_{Mod^gr(A)}(f^*N, M)`
>
> Both sides of the source's identification are taken in the graded categories, so the statement
> is the identification in every homogeneous degree at once.

```lean
noncomputable def pullbackHomOfDegreeEquiv (φ : GradedAlgebra.SemilinearHom u σ B A)
    (N : GradedModule.{t, a', max u v a u' v' a' w} B)
    (M : GradedModule.{t, a, max u v a u' v' a' w} A) (n : ℤ) :
    GradedHomOfDegree ((pullbackFunctor.{t, a, w, v, u, a', v', u'} φ).obj N) M n ≃
      GradedHomOfDegree N (pushforwardObj φ M) n
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.9, Tag 0FR7](https://stacks.math.columbia.edu/tag/0FR7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
