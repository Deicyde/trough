---
declaration: section
origin: cited
lean: Stacks.Sheaves.GradedModuleInverseImage.inverseImageGradedModule, Stacks.Sheaves.GradedModuleInverseImage.inverseImageGradedModuleFunctor, Stacks.Sheaves.GradedModuleInverseImage.inverseImageGradedHomOfDegree, SheafOfModules.GradedModule.semilinearHomOfDegreeEquiv, Stacks.Sheaves.GradedModuleToposPullback.tensorAlgebra, Stacks.Sheaves.GradedModuleToposPullback.pullbackObj, Stacks.Sheaves.GradedModuleToposPullback.pullbackFunctor, Stacks.Sheaves.GradedModuleToposPullback.tensorAlgebraHomOfDegree
statement: formalized
proof: formalized
---

# 24.9 Pull and push for sheaves of graded modules

Section 24.9 of the Stacks Project, [Tag 0FR7](https://stacks.math.columbia.edu/tag/0FR7). 2 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FR7, the section

[Tag 0FR7](https://stacks.math.columbia.edu/tag/0FR7) in the Stacks Project.

**`Stacks.Sheaves.GradedModuleInverseImage.inverseImageGradedModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleInverseImage.lean, line 531](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleInverseImage.lean#L531). The attribute's comment: “the graded f⁻¹B-module f⁻¹N, with degree-n piece f⁻¹N^n and multiplication f⁻¹ν\_\{n,m}”.

> **The inverse image `f⁻¹N` of a right graded `B`-module** along a morphism of topoi, a right
> graded `f⁻¹B`-module. Its degree-`n` piece is the inverse image `f⁻¹N^n` of the degree-`n` piece
> of `N`, and its multiplication `f⁻¹N^n × f⁻¹B^m ⟶ f⁻¹N^{n+m}` is the inverse image `f⁻¹ν_{n,m}`
> of the multiplication `ν_{n,m}` of `N`, which uses that `f⁻¹` commutes with products.

```lean
public noncomputable def inverseImageGradedModule
    (N : SheafOfModules.GradedModule.{w', w', w'} B) :
    SheafOfModules.GradedModule.{w, w, w} (inverseImageGradedAlgebra f O B)
```

**`Stacks.Sheaves.GradedModuleInverseImage.inverseImageGradedModuleFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleInverseImage.lean, line 547](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleInverseImage.lean#L547). The attribute's comment: “the functor f⁻¹ : Mod(B) ⥤ Mod(f⁻¹B)”.

> **The inverse image functor `f⁻¹ : Mod(B) ⥤ Mod(f⁻¹B)`** on right graded modules. Its
> degreewise components are the inverse images of the degreewise components.

```lean
public noncomputable def inverseImageGradedModuleFunctor :
    SheafOfModules.GradedModule.{w', w', w'} B ⥤
      SheafOfModules.GradedModule.{w, w, w} (inverseImageGradedAlgebra f O B)
```

**`Stacks.Sheaves.GradedModuleInverseImage.inverseImageGradedHomOfDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleInverseImage.lean, line 561](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleInverseImage.lean#L561). The attribute's comment: “f⁻¹ on homogeneous morphisms of degree n”.

> **The inverse image of a homomorphism homogeneous of degree `d`**, again homogeneous of
> degree `d`: the action on morphisms of `f⁻¹ : Mod^gr(B) ⥤ Mod^gr(f⁻¹B)`.

```lean
public noncomputable def inverseImageGradedHomOfDegree
    {N N' : SheafOfModules.GradedModule.{w', w', w'} B} {d : ℤ}
    (g : SheafOfModules.GradedHomOfDegree N N' d) :
    SheafOfModules.GradedHomOfDegree (inverseImageGradedModule f O N)
      (inverseImageGradedModule f O N') d
```

**`SheafOfModules.GradedModule.semilinearHomOfDegreeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModulePullback.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModulePullback.lean#L446). The attribute's comment: “f\_*M corepresents the φ-semilinear homomorphisms into M homogeneous of degree n, the morphisms of the graded category Mod^gr”.

> **`f_*M` corepresents the `φ`-semilinear homomorphisms into `M` homogeneous of degree `n`**:
> such a homomorphism out of `N` is exactly a homomorphism `N ⟶ f_*M` of right graded `B`-modules
> homogeneous of degree `n`.

```lean
noncomputable def semilinearHomOfDegreeEquiv (N : GradedModule.{t, a', m} B)
    (M : GradedModule.{t, a, m} A) (n : ℤ) :
    SemilinearHomOfDegree φ N M n ≃ GradedHomOfDegree N (pushforwardObj φ M) n
```

**`Stacks.Sheaves.GradedModuleToposPullback.tensorAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleToposPullback.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleToposPullback.lean#L299). The attribute's comment: “the functor - ⊗\_\{f⁻¹B} A : Mod(f⁻¹B) ⥤ Mod(A) of Section 0FR4, A a graded (f⁻¹B, A)-bimodule through φ : f⁻¹B → A”.

> **The functor `- ⊗_{f⁻¹B, φ} A : Mod(f⁻¹B) ⥤ Mod(A)`**, for a homomorphism
> `φ : f⁻¹B ⟶ A` of sheaves of graded `f⁻¹O_D`-algebras: the graded tensor product with `A`, read
> as a graded `(f⁻¹B, A)`-bimodule through `φ`, a right graded `A`-module.

```lean
def tensorAlgebra
    (φ : SheafOfModules.GradedAlgebra.UnitalHom (inverseImageAlgebra f B) (restrictedAlgebra f A)) :
    SheafOfModules.GradedModule.{max u v z, max u v z, max u v z} (inverseImageAlgebra f B) ⥤
      SheafOfModules.GradedModule.{max u v z, max u v z, max u v z} A
```

**`Stacks.Sheaves.GradedModuleToposPullback.pullbackObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleToposPullback.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleToposPullback.lean#L311). The attribute's comment: “f^*N = f⁻¹N ⊗\_\{f⁻¹B, φ} A”.

> **The pullback `f^*N = f⁻¹N ⊗_{f⁻¹B, φ} A` of a right graded `B`-module** along a morphism of
> ringed topoi `f` and a homomorphism `φ : f⁻¹B ⟶ A` of sheaves of graded `f⁻¹O_D`-algebras: the
> graded tensor product of the inverse image `f⁻¹N`, a right graded `f⁻¹B`-module, with `A`, a
> graded `(f⁻¹B, A)`-bimodule through `φ`.

```lean
def pullbackObj
    (φ : SheafOfModules.GradedAlgebra.UnitalHom (inverseImageAlgebra f B) (restrictedAlgebra f A))
    (N : SheafOfModules.GradedModule.{w', w', w'} B) :
    SheafOfModules.GradedModule.{max u v z, max u v z, max u v z} A
```

**`Stacks.Sheaves.GradedModuleToposPullback.pullbackFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleToposPullback.lean, line 334](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleToposPullback.lean#L334). The attribute's comment: “f^* : Mod(B) ⥤ Mod(A), the composite of f⁻¹ and - ⊗\_\{f⁻¹B, φ} A”.

> **The pullback functor `f^* : Mod(B) ⥤ Mod(A)`** of right graded modules along a morphism of
> ringed topoi and a homomorphism `φ : f⁻¹B ⟶ A`: the inverse image `f⁻¹ : Mod(B) ⥤ Mod(f⁻¹B)`
> followed by `- ⊗_{f⁻¹B, φ} A : Mod(f⁻¹B) ⥤ Mod(A)`.

```lean
def pullbackFunctor
    (φ : SheafOfModules.GradedAlgebra.UnitalHom (inverseImageAlgebra f B) (restrictedAlgebra f A)) :
    SheafOfModules.GradedModule.{w', w', w'} B ⥤
      SheafOfModules.GradedModule.{max u v z, max u v z, max u v z} A
```

**`Stacks.Sheaves.GradedModuleToposPullback.tensorAlgebraHomOfDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleToposPullback.lean, line 350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleToposPullback.lean#L350). The attribute's comment: “- ⊗\_\{f⁻¹B} A on homogeneous morphisms of degree n”.

> **`- ⊗_{f⁻¹B, φ} A` on homomorphisms homogeneous of degree `d`.**

```lean
def tensorAlgebraHomOfDegree
    (φ : SheafOfModules.GradedAlgebra.UnitalHom (inverseImageAlgebra f B) (restrictedAlgebra f A))
    {M M' : SheafOfModules.GradedModule.{max u v z, max u v z, max u v z}
      (inverseImageAlgebra f B)} {d : ℤ}
    (g : SheafOfModules.GradedHomOfDegree M M' d) :
    SheafOfModules.GradedHomOfDegree ((tensorAlgebra f φ).obj M) ((tensorAlgebra f φ).obj M') d
```

**`Stacks.Sheaves.GradedModuleToposPullback.pullbackHomOfDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleToposPullback.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleToposPullback.lean#L363). The attribute's comment: “f^* as a functor of graded categories, on homogeneous morphisms of degree n”.

> **`f^*` as a functor of graded categories `Mod^gr(B) ⥤ Mod^gr(A)`, on homogeneous morphisms
> of degree `d`**: the inverse image of a homomorphism homogeneous of degree `d`, followed by
> `- ⊗_{f⁻¹B, φ} A`. On objects it is `pullbackObj`.

```lean
def pullbackHomOfDegree
    (φ : SheafOfModules.GradedAlgebra.UnitalHom (inverseImageAlgebra f B) (restrictedAlgebra f A))
    {N N' : SheafOfModules.GradedModule.{w', w', w'} B} {d : ℤ}
    (g : SheafOfModules.GradedHomOfDegree N N' d) :
    SheafOfModules.GradedHomOfDegree (pullbackObj f φ N) (pullbackObj f φ N') d
```

**`SheafOfModules.GradedModule.pushforwardObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean#L193). The attribute's comment: “the direct image f\_*M of a graded module, with multiplication f\_*μ ∘ (id, φ)”.

> The direct image `f_*M` of a right graded `A`-module along a morphism of ringed sites and a
> homomorphism `φ : B ⟶ f_*A` of sheaves of graded algebras: its degree-`n` piece is the direct
> image of the degree-`n` piece of `M`, and a homogeneous section `b` of `B` acts through
> `φ b`.

```lean
noncomputable def pushforwardObj (φ : GradedAlgebra.SemilinearHom u σ B A)
    (M : GradedModule.{t, a, m} A) : GradedModule.{t, a', m} B
```

**`SheafOfModules.GradedModule.pushforwardMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean#L234). The attribute's comment: “the direct image is functorial in the graded module”.

> The direct image of a homomorphism of right graded `A`-modules is its degreewise direct
> image.

```lean
noncomputable def pushforwardMap (φ : GradedAlgebra.SemilinearHom u σ B A)
    {M N : GradedModule.{t, a, m} A} (g : M ⟶ N) :
    pushforwardObj φ M ⟶ pushforwardObj φ N
```

**`SheafOfModules.GradedModule.pushforwardFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean#L250). The attribute's comment: “the functor f\_* : Mod(A) ⥤ Mod(B)”.

> The direct image functor `f_* : Mod(A) ⥤ Mod(B)` on sheaves of graded modules.

```lean
noncomputable def pushforwardFunctor (φ : GradedAlgebra.SemilinearHom u σ B A) :
    GradedModule.{t, a, m} A ⥤ GradedModule.{t, a', m} B
```

**`SheafOfModules.GradedModule.pushforwardHomOfDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean#L279). The attribute's comment: “f\_* as a functor of graded categories, on homogeneous morphisms of degree n”.

> The direct image of a homomorphism of right graded `A`-modules homogeneous of degree `n`:
> the degreewise direct image again, which is homogeneous of degree `n`. This is the action on
> morphisms of the induced functor `f_* : Mod^gr(A) ⥤ Mod^gr(B)` of graded categories, whose
> action on objects is `SheafOfModules.GradedModule.pushforwardObj`.

```lean
noncomputable def pushforwardHomOfDegree (φ : GradedAlgebra.SemilinearHom u σ B A)
    {M L : GradedModule.{t, a, m} A} {n : ℤ} (g : GradedHomOfDegree M L n) :
    GradedHomOfDegree (pushforwardObj φ M) (pushforwardObj φ L) n
```

**`SheafOfModules.GradedModule.semilinearHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedPushforward.lean#L356). The attribute's comment: “f\_*M corepresents the φ-semilinear homomorphisms into M”.

> **A `φ`-semilinear homomorphism `P ⟶ M` is exactly a homomorphism `P ⟶ f_*M` of right graded
> `B`-modules.**

```lean
noncomputable def semilinearHomEquiv (φ : GradedAlgebra.SemilinearHom u σ B A)
    (P : GradedModule.{t, a', m} B) (M : GradedModule.{t, a, m} A) :
    SemilinearHom φ P M ≃ (P ⟶ pushforwardObj φ M)
```

## Tag 0FR8, a lemma

[Tag 0FR8](https://stacks.math.columbia.edu/tag/0FR8) in the Stacks Project.

**`SheafOfModules.GradedTensorPullback.tensorPullbackHomOfDegreeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModulePullbackTensor.lean, line 422](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModulePullbackTensor.lean#L422). The attribute's comment: “Hom\_\{Mod^gr(B)}(N, f\_*M) = Hom\_\{Mod^gr(A)}(f^*N, M) in every homogeneous degree, for the explicit pullback f^*N = f^\{-1}N ⊗\_\{f^\{-1}B, φ} A”.

> **Tag 0FR8**: for a morphism of ringed sites `f`, a sheaf of graded `O_C`-algebras `B` on the
> target, a sheaf of graded `O_D`-algebras `A` on the source and a homomorphism `φ : f⁻¹B ⟶ A` of
> sheaves of graded algebras, the homomorphisms `f^*N ⟶ M` of right graded `A`-modules homogeneous
> of degree `n`, for the pullback `f^*N = f⁻¹N ⊗_{f⁻¹B, φ} A` (`tensorPullbackObj`), are exactly
> the homomorphisms `N ⟶ f_*M` of right graded `B`-modules homogeneous of degree `n`:
>
> `Hom_{Mod^gr(B)}(N, f_*M) = Hom_{Mod^gr(A)}(f^*N, M)`.
>
> Here `f_*M` is the direct image of `M`, degreewise, with `B` acting through `φ` read as a
> homomorphism `B ⟶ f_*A` (`structureSemilinearHom`).

```lean
noncomputable def tensorPullbackHomOfDegreeEquiv {B : GradedAlgebra.{u, u} (toRingCat J Osharp)}
    {A : GradedAlgebra.{u, u} (toRingCat K Psharp)}
    (φ : GradedAlgebra.UnitalHom (gradedInverseImageAlgebra α hO hP B) A)
    (N : GradedModule.{u, u, u} B) (M : GradedModule.{u, u, u} A) (n : ℤ) :
    GradedHomOfDegree (tensorPullbackObj α hO hP φ N) M n ≃
      GradedHomOfDegree N (GradedModule.pushforwardObj (structureSemilinearHom α hO hP φ) M) n
```

**`SheafOfModules.GradedTensorPullback.tensorPullbackPushforwardAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModulePullbackTensor.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModulePullbackTensor.lean#L435). The attribute's comment: “the adjunction f^* ⊣ f\_*, for the explicit pullback f^*N = f^\{-1}N ⊗\_\{f^\{-1}B, φ} A”.

> **The pullback `f^*N = f⁻¹N ⊗_{f⁻¹B, φ} A` is left adjoint to the direct image** on sheaves
> of graded modules: the degree-zero case of Tag 0FR8, read as an adjunction `f^* ⊣ f_*`, so
> natural in both `N` and `M`.

```lean
noncomputable def tensorPullbackPushforwardAdjunction
    {B : GradedAlgebra.{u, u} (toRingCat J Osharp)}
    {A : GradedAlgebra.{u, u} (toRingCat K Psharp)}
    (φ : GradedAlgebra.UnitalHom (gradedInverseImageAlgebra α hO hP B) A) :
    tensorPullbackFunctor α hO hP φ ⊣
      GradedModule.pushforwardFunctor (structureSemilinearHom α hO hP φ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.9, Tag 0FR7](https://stacks.math.columbia.edu/tag/0FR7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
