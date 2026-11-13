---
declaration: section
origin: cited
lean: SheafOfModules.GradedBimodule.smulCommClass_sections, SheafOfModules.RelativeTensor.gradedTensorRight, SheafOfModules.RelativeTensor.gradedTensorRightHomOfDegreeLinear, SheafOfModules.gradedSheafHomModule, SheafOfModules.isGradedInternalHom_gradedSheafHomModule, SheafOfModules.gradedSheafHomFunctor, SheafOfModules.gradedSheafHomMapOfDegree, SheafOfModules.gradedSheafHomMapOfDegreeLinear
statement: formalized
proof: formalized
---

# 24.8 Sheaves of graded bimodules and tensor-hom adjunction

Section 24.8 of the Stacks Project, [Tag 0FR4](https://stacks.math.columbia.edu/tag/0FR4). 3 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FR4, the section

[Tag 0FR4](https://stacks.math.columbia.edu/tag/0FR4) in the Stacks Project.

**`SheafOfModules.GradedBimodule.smulCommClass_sections`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedBimoduleSections.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedBimoduleSections.lean#L176). The attribute's comment: “N(U) = ⨁ N^n(U) is a graded (A(U), B(U))-bimodule”.

> **Stacks 0FR4: the two actions on the sections of a graded bimodule commute**,
> `a (x b) = (a x) b`. Together with `leftModuleSections` and `rightModuleSections` this makes
> `N(U) = ⨁_n N^n(U)` an `(A(U), B(U))`-bimodule, graded by `incl_smul_incl` and
> `op_incl_smul_incl`, and bilinear over `O(U)` by `isScalarTower_left_sections`,
> `smulCommClass_base_left_sections`, `isScalarTower_right_sections` and
> `smulCommClass_base_right_sections`.

```lean
instance smulCommClass_sections :
    SMulCommClass (A.toPresheafGradedAlgebra.Total X) (B.toPresheafGradedAlgebra.Total X)ᵐᵒᵖ
      (N.Sections X)
```

**`SheafOfModules.RelativeTensor.gradedTensorRight`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedBimoduleTensorAction.lean, line 972](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedBimoduleTensorAction.lean#L972). The attribute's comment: “M ⊗\_A N is a right graded B-module, with (x ⊗ y) b = x ⊗ (y b)”.

> **Stacks 0FR4: the right graded `B`-module `M ⊗_A N`**, for `M` a right graded `A`-module and
> `N` a graded `(A, B)`-bimodule: degree `n` is degree `n` of the graded tensor product of Stacks
> 0FR2, and a homogeneous section `b` of `B` acts on `x ⊗ y` by `x ⊗ (y b)`
> (`SheafOfModules.RelativeTensor.gradedTensorRight_smul_tmul`). The functors `- ⊗_A N` are
> `SheafOfModules.RelativeTensor.gradedTensorRightFunctor` and
> `SheafOfModules.RelativeTensor.gradedTensorRightHomOfDegree`, with the laws of a functor of graded
> categories in `StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedBimoduleTensorFunctor.lean`.

```lean
noncomputable def gradedTensorRight : GradedModule.{t, max u v z, max u v z} B
```

**`SheafOfModules.RelativeTensor.gradedTensorRightHomOfDegreeLinear`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedBimoduleTensorFunctor.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedBimoduleTensorFunctor.lean#L237). The attribute's comment: “- ⊗\_A N is Γ(C, O)-linear on Hom^n, as a functor of graded categories”.

> **Stacks 0FR4: `- ⊗_A N` is a functor of graded categories over `Γ(C, O)`, on the morphisms
> of degree `n`**: the map `Hom^n(M, M') → Hom^n(M ⊗_A N, M' ⊗_A N)` is `Γ(C, O)`-linear. Its
> compatibility with composition is
> `SheafOfModules.RelativeTensor.gradedTensorRightHomOfDegree_comp`, and with identities
> `SheafOfModules.RelativeTensor.gradedTensorRightHomOfDegree_ofHom`.

```lean
noncomputable def gradedTensorRightHomOfDegreeLinear
    (M M' : GradedModule.{t, max u v z, max u v z} A) (n : ℤ) :
    GradedHomOfDegree M M' n →ₗ[Stacks.Cohomology.SiteModules.GlobalSectionRing
        (toRingCat J Osharp)]
      GradedHomOfDegree (gradedTensorRight M N) (gradedTensorRight M' N) n
```

**`SheafOfModules.gradedSheafHomModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomModule.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomModule.lean#L232). The attribute's comment: “SheafHom^gr\_B(N, L) is a right graded A-module, with (f a)(y) = f(a y)”.

> **Stacks 0FR4: `SheafHom^gr_B(N, L)` is a right graded `A`-module.** For a graded
> `(A, B)`-bimodule `N` and a right graded `B`-module `L`, the graded `O`-module
> `SheafHom^gr_B(N, L)` of [Stacks, Tag 0FR3] with the multiplication maps
> `SheafHom^n_B(N, L) × A^m → SheafHom^{n + m}_B(N, L)` sending `(f, a)` to the local
> homomorphism `(f a)(y) = f (a y)`, which involves no signs.

```lean
noncomputable def gradedSheafHomModule (N : GradedBimodule.{t, a, z} A B)
    (L : GradedModule.{t, a, s} B) : GradedModule.{t, a, max u v z s} A
```

**`SheafOfModules.isGradedInternalHom_gradedSheafHomModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomModule.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomModule.lean#L261). The attribute's comment: “the right graded A-module SheafHom^gr\_B(N, L), as the internal hom with its right A-action”.

> **The constructed module is the internal hom with its right `A`-action**, in the sense of
> `SheafOfModules.IsGradedInternalHom`.

```lean
noncomputable def isGradedInternalHom_gradedSheafHomModule :
    IsGradedInternalHom N L (gradedSheafHomModule N L)
```

**`SheafOfModules.gradedSheafHomFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomModule.lean, line 375](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomModule.lean#L375). The attribute's comment: “the functor SheafHom^gr\_B(N, -) : Mod(B) → Mod(A)”.

> **Stacks 0FR4: the functor `SheafHom^gr_B(N, -) : Mod(B) ⥤ Mod(A)`**, from right graded
> `B`-modules to right graded `A`-modules, sending `L` to `SheafHom^gr_B(N, L)` and a homomorphism
> to postcomposition with it.

```lean
noncomputable def gradedSheafHomFunctor (N : GradedBimodule.{t, a, z} A B) :
    GradedModule.{t, a, s} B ⥤ GradedModule.{t, a, max u v z s} A
```

**`SheafOfModules.gradedSheafHomMapOfDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomModule.lean, line 420](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomModule.lean#L420). The attribute's comment: “SheafHom^gr\_B(N, -) : Mod^gr(B) → Mod^gr(A) on homogeneous homomorphisms of degree k”.

> **Stacks 0FR4, the functor of graded categories `SheafHom^gr_B(N, -)`, on morphisms.** A
> homomorphism `g : L → L'` of right graded `B`-modules homogeneous of degree `k` induces the
> homomorphism `SheafHom^gr_B(N, L) → SheafHom^gr_B(N, L')` of right graded `A`-modules
> homogeneous of degree `k` given by postcomposition with `g`.

```lean
noncomputable def gradedSheafHomMapOfDegree (g : GradedHomOfDegree L L' k) :
    GradedHomOfDegree (gradedSheafHomModule N L) (gradedSheafHomModule N L') k
```

**`SheafOfModules.gradedSheafHomMapOfDegreeLinear`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomModule.lean, line 496](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHomModule.lean#L496). The attribute's comment: “SheafHom^gr\_B(N, -) is Γ(C, O)-linear on Hom^k, as a functor of graded categories”.

> **Stacks 0FR4: `SheafHom^gr_B(N, -)` is a functor of graded categories over `Γ(C, O)`, on
> the morphisms of degree `k`**: the map
> `Hom^k(L, L') → Hom^k(SheafHom^gr_B(N, L), SheafHom^gr_B(N, L'))` is `Γ(C, O)`-linear. Its
> compatibility with composition is `SheafOfModules.gradedSheafHomMapOfDegree_comp`, and with
> identities `SheafOfModules.gradedSheafHomMapOfDegree_ofHom`.

```lean
noncomputable def gradedSheafHomMapOfDegreeLinear (L L' : GradedModule.{t, a, s} B) (k : ℤ) :
    GradedHomOfDegree L L' k →ₗ[Stacks.Cohomology.SiteModules.GlobalSectionRing R]
      GradedHomOfDegree (gradedSheafHomModule N L) (gradedSheafHomModule N L') k
```

**`SheafOfModules.RelativeTensor.gradedTensorRightFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleToposPullback.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleToposPullback.lean#L185). The attribute's comment: “the functor - ⊗\_A N : Mod(A) → Mod(B)”.

> **The functor `- ⊗_A N : Mod(A) ⥤ Mod(B)`** of right graded modules, for a graded
> `(A, B)`-bimodule `N`.

```lean
def gradedTensorRightFunctor :
    GradedModule.{t, max u v z, max u v z} A ⥤ GradedModule.{t, max u v z, max u v z} B
```

**`SheafOfModules.RelativeTensor.gradedTensorRightHomOfDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleToposPullback.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleToposPullback.lean#L244). The attribute's comment: “- ⊗\_A N : Mod^gr(A) → Mod^gr(B) on homogeneous homomorphisms of degree n”.

> **The homomorphism `M ⊗_A N ⟶ M' ⊗_A N` homogeneous of degree `d`** induced by a homomorphism
> `g : M ⟶ M'` homogeneous of degree `d`: the action of `- ⊗_A N` on homogeneous morphisms,
> determined by `x ⊗ y ↦ (g x) ⊗ y`.

```lean
def gradedTensorRightHomOfDegree {d : ℤ} (g : GradedHomOfDegree M M' d) :
    GradedHomOfDegree (gradedTensorRight M N) (gradedTensorRight M' N) d
```

## Tag 0FR5, a definition

[Tag 0FR5](https://stacks.math.columbia.edu/tag/0FR5) in the Stacks Project.

**`SheafOfModules.GradedBimodule`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedBimodule.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedBimodule.lean#L59). The attribute's comment: “graded bimodules”.

> A graded `(A, B)`-bimodule is a family of sheaves of modules indexed by `ℤ` carrying
> commuting unital left `A`- and right `B`-actions.

```lean
structure GradedBimodule (A B : GradedAlgebra.{t, a} R)
```

**`SheafOfModules.GradedBimodule.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedBimodule.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedBimodule.lean#L95). The attribute's comment: “homomorphisms of graded bimodules”.

> A homomorphism of graded `(A, B)`-bimodules is a degreewise morphism of sheaves of modules
> which respects both actions.

```lean
structure Hom (M N : GradedBimodule.{t, a, m} A B)
```

## Tag 0FR6, a lemma

[Tag 0FR6](https://stacks.math.columbia.edu/tag/0FR6) in the Stacks Project.

**`SheafOfModules.balancedEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomAdjunction.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomAdjunction.lean#L367). The attribute's comment: “proof: local homomorphisms into the internal hom are balanced bilinear families”.

> The degree-`n` local homomorphisms `M|_U → SheafHom^gr_B(N, L)|_U` of right graded
> `A`-modules are the `A`-balanced bilinear families of degree `n` over `U`. This is the local
> form of the tensor-hom adjunction, and the hint of the proof of Stacks 0FR6.

```lean
noncomputable def balancedEquiv (hH : IsGradedInternalHom N L H)
    (M : GradedModule.{t, a, w} A) (n : ℤ) (U : C) :
    GradedLocalHom M H n U ≃ GradedLocalBalanced M N L n U
```

**`SheafOfModules.tensorHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomAdjunction.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomAdjunction.lean#L396). The attribute's comment: “Hom\_\{Mod^gr(B)}(M ⊗\_A N, L) = Hom\_\{Mod^gr(A)}(M, SheafHom^gr\_B(N, L))”.

> **Tensor-hom adjunction for sheaves of graded modules**, first identity: the degree-`n`
> homomorphisms `M ⊗_A N → L` of right graded `B`-modules are the degree-`n` homomorphisms
> `M → SheafHom^gr_B(N, L)` of right graded `A`-modules.

```lean
noncomputable def tensorHomEquiv (hT : IsGradedTensorProduct M N T)
    (hH : IsGradedInternalHom N L H) (n : ℤ) :
    GradedHomOfDegree T L n ≃ GradedHomOfDegree M H n
```

**`SheafOfModules.isGradedSheafHom_tensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomAdjunction.lean, line 429](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomAdjunction.lean#L429). The attribute's comment: “SheafHom^gr\_B(M ⊗\_A N, L) = SheafHom^gr\_A(M, SheafHom^gr\_B(N, L))”.

> **Tensor-hom adjunction for sheaves of graded modules**, second identity: a graded sheaf of
> `R`-modules which is the internal hom `SheafHom^gr_B(M ⊗_A N, L)` is also the internal hom
> `SheafHom^gr_A(M, SheafHom^gr_B(N, L))`.

```lean
noncomputable def isGradedSheafHom_tensor (hT : IsGradedTensorProduct M N T)
    (hH : IsGradedInternalHom N L H) {G : ℤ → SheafOfModules.{g} R}
    (hG : IsGradedSheafHom T L G) : IsGradedSheafHom M H G
```

**`SheafOfModules.tensorHomEquiv_naturality_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomNaturality.lean, line 346](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomNaturality.lean#L346). The attribute's comment: “first identity, natural in M”.

> **Tensor-hom adjunction for sheaves of graded modules**, first identity, functoriality in
> `M`: for a morphism `u : M' ⟶ M` of right graded `A`-modules, precomposition with the induced
> `u ⊗ 1 : M' ⊗_A N ⟶ M ⊗_A N` corresponds to precomposition with `u`.

```lean
theorem tensorHomEquiv_naturality_left (hT : IsGradedTensorProduct M N T)
    (hT' : IsGradedTensorProduct M' N T') (hH : IsGradedInternalHom N L H) (u : M' ⟶ M) {n : ℤ}
    (φ : GradedHomOfDegree T L n) :
    tensorHomEquiv hT' hH n (GradedHomOfDegree.compLeft (hT'.map hT u (𝟙 N)) φ) =
      GradedHomOfDegree.compLeft u (tensorHomEquiv hT hH n φ)
```

**`SheafOfModules.tensorHomEquiv_naturality_bimodule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomNaturality.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomNaturality.lean#L366). The attribute's comment: “first identity, natural in N”.

> **Tensor-hom adjunction for sheaves of graded modules**, first identity, functoriality in
> `N`: for a morphism `σ : N ⟶ N'` of graded `(A, B)`-bimodules, precomposition with the induced
> `1 ⊗ σ : M ⊗_A N ⟶ M ⊗_A N'` corresponds to postcomposition with the induced
> `SheafHom^gr_B(N', L) ⟶ SheafHom^gr_B(N, L)`.

```lean
theorem tensorHomEquiv_naturality_bimodule (hT : IsGradedTensorProduct M N T)
    (hT' : IsGradedTensorProduct M N' T') (hH : IsGradedInternalHom N L H)
    (hH' : IsGradedInternalHom N' L H') (σ : N ⟶ N') {n : ℤ} (φ : GradedHomOfDegree T' L n) :
    tensorHomEquiv hT hH n (GradedHomOfDegree.compLeft (hT.map hT' (𝟙 M) σ) φ) =
      (tensorHomEquiv hT' hH' n φ).compRight (hH'.map hH σ (𝟙 L))
```

**`SheafOfModules.tensorHomEquiv_naturality_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomNaturality.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomNaturality.lean#L386). The attribute's comment: “first identity, natural in L”.

> **Tensor-hom adjunction for sheaves of graded modules**, first identity, functoriality in
> `L`: for a morphism `k : L ⟶ L'` of right graded `B`-modules, postcomposition with `k`
> corresponds to postcomposition with the induced `SheafHom^gr_B(N, L) ⟶ SheafHom^gr_B(N, L')`.

```lean
theorem tensorHomEquiv_naturality_right (hT : IsGradedTensorProduct M N T)
    (hH : IsGradedInternalHom N L H) (hH' : IsGradedInternalHom N L' H') (k : L ⟶ L') {n : ℤ}
    (φ : GradedHomOfDegree T L n) :
    tensorHomEquiv hT hH' n (φ.compRight k) =
      (tensorHomEquiv hT hH n φ).compRight (hH.map hH' (𝟙 N) k)
```

**`SheafOfModules.isGradedSheafHom_tensor_map_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomNaturality.lean, line 444](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomNaturality.lean#L444). The attribute's comment: “second identity, natural in M”.

> **Tensor-hom adjunction for sheaves of graded modules**, second identity, functoriality in
> `M`: for a morphism `u : M' ⟶ M` of right graded `A`-modules, the morphism
> `SheafHom^gr_B(M ⊗_A N, L) ⟶ SheafHom^gr_B(M' ⊗_A N, L)` induced by `u ⊗ 1` is the morphism
> `SheafHom^gr_A(M, SheafHom^gr_B(N, L)) ⟶ SheafHom^gr_A(M', SheafHom^gr_B(N, L))` induced by
> `u`.

```lean
theorem isGradedSheafHom_tensor_map_left (hT : IsGradedTensorProduct M N T)
    (hT' : IsGradedTensorProduct M' N T') (hH : IsGradedInternalHom N L H)
    (hG : IsGradedSheafHom T L G) (hG' : IsGradedSheafHom T' L G') (u : M' ⟶ M) (n : ℤ) :
    hG.map hG' (hT'.map hT u (𝟙 N)) (𝟙 L) n =
      (isGradedSheafHom_tensor hT hH hG).map (isGradedSheafHom_tensor hT' hH hG') u (𝟙 H) n
```

**`SheafOfModules.isGradedSheafHom_tensor_map_bimodule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomNaturality.lean, line 471](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomNaturality.lean#L471). The attribute's comment: “second identity, natural in N”.

> **Tensor-hom adjunction for sheaves of graded modules**, second identity, functoriality in
> `N`: for a morphism `σ : N ⟶ N'` of graded `(A, B)`-bimodules, the morphism
> `SheafHom^gr_B(M ⊗_A N', L) ⟶ SheafHom^gr_B(M ⊗_A N, L)` induced by `1 ⊗ σ` is the morphism
> `SheafHom^gr_A(M, SheafHom^gr_B(N', L)) ⟶ SheafHom^gr_A(M, SheafHom^gr_B(N, L))` induced by the
> morphism `SheafHom^gr_B(N', L) ⟶ SheafHom^gr_B(N, L)` which `σ` induces.

```lean
theorem isGradedSheafHom_tensor_map_bimodule (hT : IsGradedTensorProduct M N T)
    (hT' : IsGradedTensorProduct M N' T') (hH : IsGradedInternalHom N L H)
    (hH' : IsGradedInternalHom N' L H') (hG : IsGradedSheafHom T L G)
    (hG' : IsGradedSheafHom T' L G') (σ : N ⟶ N') (n : ℤ) :
    hG'.map hG (hT.map hT' (𝟙 M) σ) (𝟙 L) n =
      (isGradedSheafHom_tensor hT' hH' hG').map (isGradedSheafHom_tensor hT hH hG) (𝟙 M)
        (hH'.map hH σ (𝟙 L)) n
```

**`SheafOfModules.isGradedSheafHom_tensor_map_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomNaturality.lean, line 501](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedTensorHomNaturality.lean#L501). The attribute's comment: “second identity, natural in L”.

> **Tensor-hom adjunction for sheaves of graded modules**, second identity, functoriality in
> `L`: for a morphism `k : L ⟶ L'` of right graded `B`-modules, the morphism
> `SheafHom^gr_B(M ⊗_A N, L) ⟶ SheafHom^gr_B(M ⊗_A N, L')` induced by `k` is the morphism
> `SheafHom^gr_A(M, SheafHom^gr_B(N, L)) ⟶ SheafHom^gr_A(M, SheafHom^gr_B(N, L'))` induced by the
> morphism `SheafHom^gr_B(N, L) ⟶ SheafHom^gr_B(N, L')` which `k` induces.

```lean
theorem isGradedSheafHom_tensor_map_right (hT : IsGradedTensorProduct M N T)
    (hH : IsGradedInternalHom N L H) (hH' : IsGradedInternalHom N L' H')
    (hG : IsGradedSheafHom T L G) (hG' : IsGradedSheafHom T L' G') (k : L ⟶ L') (n : ℤ) :
    hG.map hG' (𝟙 T) k n =
      (isGradedSheafHom_tensor hT hH hG).map (isGradedSheafHom_tensor hT hH' hG') (𝟙 M)
        (hH.map hH' (𝟙 N) k) n
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.8, Tag 0FR4](https://stacks.math.columbia.edu/tag/0FR4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
