---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.ReflexiveModules.reflexiveHull, Stacks.AlgebraicGeometry.ReflexiveModules.toReflexiveHull, Stacks.AlgebraicGeometry.ReflexiveModules.isReflexive_iff_isIso, AlgebraicGeometry.isReflexive_iff_sections_isReflexive, Stacks.AlgebraicGeometry.ReflexiveModules.isTorsionFree_of_isReflexive, Stacks.AlgebraicGeometry.ReflexiveModules.mono_toDoubleDual_iff_isTorsionFree, Stacks.AlgebraicGeometry.ReflexiveModules.isReflexive_tfae, AlgebraicGeometry.isCoherent_pullback
statement: formalized
proof: formalized
---

# 31.13 Reflexive modules

Section 31.13 of the Stacks Project, [Tag 0AVT](https://stacks.math.columbia.edu/tag/0AVT). 14 tags here are carried by 36 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AVU, a definition

[Tag 0AVU](https://stacks.math.columbia.edu/tag/0AVU) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ReflexiveModules.reflexiveHull`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ReflexiveHull/Hull.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ReflexiveHull/Hull.lean#L64). The attribute's comment: “reflexive hull”. References: SGA 3 VIB (13.1).

> The reflexive hull `F⁎⁎` of a module on a scheme: the dual of its dual.

```lean
public noncomputable abbrev reflexiveHull (F : X.Modules) : X.Modules
```

**`Stacks.AlgebraicGeometry.ReflexiveModules.toReflexiveHull`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ReflexiveHull/Hull.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ReflexiveHull/Hull.lean#L71). The attribute's comment: “canonical map to the reflexive hull”.

> The canonical map `F ⟶ F⁎⁎` to the reflexive hull, bundled with the formula that
> characterizes it: over an open `U` it sends a local section `f` to the functional on `F^∨|_U`
> whose component at the terminal object of the slice site over `U` is evaluation at `f`.

```lean
public noncomputable def toReflexiveHull (F : X.Modules) :
    { j : F ⟶ reflexiveHull F //
      ∀ (U : X.Opens) (f : Γ(F, U)) (lam : Γ(dualSheaf F, U)),
        (((j.val.app (op U)).hom f).app (op (Over.mk (𝟙 U)))).hom lam =
          (lam.app (op (Over.mk (𝟙 U)))).hom f }
```

**`Stacks.AlgebraicGeometry.ReflexiveModules.isReflexive_iff_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ReflexiveHull/Hull.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ReflexiveHull/Hull.lean#L124). The attribute's comment: “reflexive predicate”.

> Reflexivity of `F` is invertibility of any morphism `F ⟶ F⁎⁎` satisfying the defining formula
> of the canonical map.

```lean
public theorem isReflexive_iff_isIso (F : X.Modules) (j : F ⟶ reflexiveHull F)
    (hj : ∀ (U : X.Opens) (f : Γ(F, U)) (lam : Γ(dualSheaf F, U)),
      (((j.val.app (op U)).hom f).app (op (Over.mk (𝟙 U)))).hom lam =
        (lam.app (op (Over.mk (𝟙 U)))).hom f) :
    IsReflexive F ↔ IsIso j
```

## Tag 0AY0, a lemma

[Tag 0AY0](https://stacks.math.columbia.edu/tag/0AY0) in the Stacks Project.

**`AlgebraicGeometry.isReflexive_iff_sections_isReflexive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/AffineLocalCriterion.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/AffineLocalCriterion.lean#L131).

> A coherent module on an integral locally Noetherian scheme is reflexive if and only if its
> module of sections over every affine open is reflexive.

```lean
theorem isReflexive_iff_sections_isReflexive (X : Scheme.{u}) [IsIntegral X]
    [IsLocallyNoetherian X] (F : X.Modules) [_root_.SheafOfModules.IsCoherent F] :
    IsReflexive F ↔ ∀ (U : X.Opens), IsAffineOpen U → Module.IsReflexive Γ(X, U) Γ(F, U)
```

## Tag 0AY2, a lemma

[Tag 0AY2](https://stacks.math.columbia.edu/tag/0AY2) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ReflexiveModules.isTorsionFree_of_isReflexive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Reflexive/DoubleDual.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Reflexive/DoubleDual.lean#L212). The attribute's comment: “part (1)”.

> A reflexive module on an integral scheme is torsion free.

```lean
public theorem isTorsionFree_of_isReflexive [IsIntegral X] (F : X.Modules)
    (hF : IsReflexive F) : IsTorsionFree F
```

**`Stacks.AlgebraicGeometry.ReflexiveModules.mono_toDoubleDual_iff_isTorsionFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ReflexiveTorsionFree/Converse.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ReflexiveTorsionFree/Converse.lean#L135). The attribute's comment: “part (2)”.

> On an integral scheme, the canonical map of a coherent module to its double dual is a
> monomorphism if and only if the module is torsion free.

```lean
public theorem mono_toDoubleDual_iff_isTorsionFree [IsIntegral X] (F : X.Modules)
    [F.IsCoherent] : Mono (toDoubleDual F) ↔ IsTorsionFree F
```

## Tag 0AY3, a lemma

[Tag 0AY3](https://stacks.math.columbia.edu/tag/0AY3) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ReflexiveModules.isReflexive_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ReflexiveStalk/ClosedPoints.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ReflexiveStalk/ClosedPoints.lean#L238).

> **Stacks Project, Tag 0AY3.**  For a coherent module `F` on a locally Noetherian scheme
> `X`, the following are equivalent:
>
> 1. `F` is reflexive, that is, the canonical map `F ⟶ F^∨∨` is an isomorphism;
> 2. for every point `x` of `X` the stalk `F_x` is a reflexive `𝒪_{X,x}`-module;
> 3. the same for every *closed* point `x` of `X`.
>
> Integrality of `X` is not needed: reflexivity of a module of finite presentation is detected on
> stalks over an arbitrary commutative local ring.

```lean
public theorem isReflexive_tfae (X : Scheme.{u}) [IsLocallyNoetherian X] (F : X.Modules)
    [F.IsCoherent] :
    [IsReflexive F,
      ∀ x : X, Module.IsReflexive (ringStalk X.sheaf x) (modStalk F x),
      ∀ x : X, x ∈ closedPoints X →
        Module.IsReflexive (ringStalk X.sheaf x) (modStalk F x)].TFAE
```

## Tag 0EBF, a lemma

[Tag 0EBF](https://stacks.math.columbia.edu/tag/0EBF) in the Stacks Project.

**`AlgebraicGeometry.isCoherent_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentPullback/Basic.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentPullback/Basic.lean#L48). The attribute's comment: “coherence of the pullback”.

> **Stacks Project, Tag 0EBF.** The pullback of a coherent module along a morphism of schemes
> with locally Noetherian source is coherent.

```lean
public theorem isCoherent_pullback
    {X Y : Scheme.{u}} [IsLocallyNoetherian X]
    (f : X ⟶ Y) (G : Y.Modules) [G.IsCoherent] :
    ((Scheme.Modules.pullback f).obj G).IsCoherent
```

**`Stacks.AlgebraicGeometry.ReflexiveModules.isReflexive_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentPullback/Reflexive.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentPullback/Reflexive.lean#L114). The attribute's comment: “reflexivity of the pullback”.

> **The reflexivity clause of Stacks, Tag 0EBF**: the pullback of a coherent reflexive module
> along a flat morphism of integral locally Noetherian schemes is reflexive.
>
> Reflexivity is checked on stalks by Tag 0AY3, on the target to read off reflexivity of the
> stalks of `G` and on the source to put reflexivity of the stalks of `f^*G` back together;
> coherence of `f^*G`, which the source half needs, is `AlgebraicGeometry.isCoherent_pullback`,
> and that declaration carries the coherence clause of the tag.

```lean
public theorem isReflexive_pullback {X Y : Scheme.{u}}
    [IsIntegral X] [IsIntegral Y] [IsLocallyNoetherian X] [IsLocallyNoetherian Y]
    (f : X ⟶ Y) [Flat f] (G : Y.Modules) [G.IsCoherent] (hG : IsReflexive G) :
    IsReflexive ((Scheme.Modules.pullback f).obj G)
```

## Tag 0EBG, a lemma

[Tag 0EBG](https://stacks.math.columbia.edu/tag/0EBG) in the Stacks Project.

**`AlgebraicGeometry.isReflexive_of_exact_of_isReflexive_of_isTorsionFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/ExactSequence.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/ExactSequence.lean#L54).

> In an exact sequence `0 → ℱ → ℱ' → ℱ''` of coherent modules on an integral locally
> Noetherian scheme, if `ℱ'` is reflexive and `ℱ''` is torsion free then `ℱ` is reflexive.

```lean
theorem isReflexive_of_exact_of_isReflexive_of_isTorsionFree {X : Scheme.{u}} [IsIntegral X]
    [IsLocallyNoetherian X] {F F' F'' : X.Modules} [_root_.SheafOfModules.IsCoherent F]
    [_root_.SheafOfModules.IsCoherent F'] [_root_.SheafOfModules.IsCoherent F'']
    (f : F ⟶ F') (g : F' ⟶ F'') [Mono f] (hfg : f ≫ g = 0)
    (hexact : (ShortComplex.mk f g hfg).Exact) (hF' : IsReflexive F')
    (hF'' : (letI : F''.IsQuasicoherent := _root_.isQuasicoherent_of_isCoherent F'';
      IsTorsionFree F'')) :
    IsReflexive F
```

## Tag 0AY4, a lemma

[Tag 0AY4](https://stacks.math.columbia.edu/tag/0AY4) in the Stacks Project.

**`AlgebraicGeometry.sheafHom_isReflexive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/SheafHomReflexive.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/SheafHomReflexive.lean#L39).

> On an integral locally Noetherian scheme, the internal Hom `SheafHom(ℱ, 𝒢)` of coherent modules
> is reflexive as soon as `𝒢` is.

```lean
theorem sheafHom_isReflexive (X : Scheme.{u}) [IsIntegral X] [IsLocallyNoetherian X]
    (F G : X.Modules) [_root_.SheafOfModules.IsCoherent F] [_root_.SheafOfModules.IsCoherent G]
    (hG : IsReflexive G) :
    IsReflexive (sheafInternalHom (spaceRingedSite X.sheaf) F G)
```

## Tag 0EBH, a remark

[Tag 0EBH](https://stacks.math.columbia.edu/tag/0EBH) in the Stacks Project.

**`AlgebraicGeometry.hullReflectionAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentCategory.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentCategory.lean#L82). The attribute's comment: “adjunction”.

> On an integral locally Noetherian scheme, taking reflexive hulls is a left adjoint of the
> inclusion of the coherent reflexive modules into the coherent modules.

```lean
noncomputable def hullReflectionAdjunction : hullReflection X ⊣ inclusion X
```

**`AlgebraicGeometry.coherentReflexiveModules_hasFiniteBiproducts`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentCategory.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentCategory.lean#L122). The attribute's comment: “additive”.

> The coherent reflexive modules on an integral locally Noetherian scheme form an additive
> category: they have finite direct sums.

```lean
noncomputable instance coherentReflexiveModules_hasFiniteBiproducts :
    HasFiniteBiproducts (CoherentReflexiveModules X)
```

**`AlgebraicGeometry.CoherentReflexive.internalHomObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentInternalHom.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentInternalHom.lean#L80). The attribute's comment: “internal\_hom”.

> **Stacks Project, Tag 0EBH.**  The sheaf Hom of two coherent reflexive modules, as a
> coherent reflexive module: it is coherent by [Stacks, Tag 01Y2] and reflexive by
> [Stacks, Tag 0AY4].

```lean
noncomputable def internalHomObj (G H : CoherentReflexiveModules X) :
    CoherentReflexiveModules X
```

**`AlgebraicGeometry.CoherentReflexive.dualObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentInternalHom.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentInternalHom.lean#L99). The attribute's comment: “dual”.

> **Stacks Project, Tag 0EBH.**  Every coherent reflexive module has a dual object in the
> category of coherent reflexive modules, namely `ℋom_{𝒪_X}(ℱ, 𝒪_X)`.

```lean
noncomputable def dualObj (F : CoherentReflexiveModules X) : CoherentReflexiveModules X
```

**`AlgebraicGeometry.CoherentReflexive.isReflexive_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentKernels.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentKernels.lean#L92). The attribute's comment: “kernels”.

> **Stacks Project, Tag 0EBH.**  The ordinary kernel of a morphism of coherent reflexive
> modules is reflexive: it is the kernel of a map into the reflexive, hence torsion-free, module
> `𝒢`.

```lean
theorem isReflexive_kernel (f : F ⟶ G) : IsReflexive (kernel f.hom.hom)
```

**`AlgebraicGeometry.CoherentReflexive.kernelIsKernel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentKernels.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentKernels.lean#L123). The attribute's comment: “kernels”.

> **Stacks Project, Tag 0EBH.**  The ordinary kernel, with its ordinary inclusion, is a
> kernel in the category of coherent reflexive modules.

```lean
noncomputable def kernelIsKernel (f : F ⟶ G) :
    IsLimit (KernelFork.ofι (f := f) (kernelι f) (kernelι_comp f))
```

**`AlgebraicGeometry.CoherentReflexive.cokernelIsCokernel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentKernels.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentKernels.lean#L179). The attribute's comment: “cokernels”.

> **Stacks Project, Tag 0EBH.**  The reflexive hull of the ordinary cokernel, with the
> ordinary projection followed by the canonical map to the double dual, is a cokernel in the
> category of coherent reflexive modules.

```lean
noncomputable def cokernelIsCokernel (f : F ⟶ G) :
    IsColimit (CokernelCofork.ofπ (f := f) (cokernelπ f) (comp_cokernelπ f))
```

**`AlgebraicGeometry.CoherentReflexive.tensorObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentTensor.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentTensor.lean#L139). The attribute's comment: “tensor”.

> **Stacks Project, Tag 0EBH.**  The tensor product of the category of coherent reflexive
> modules: the reflexive hull of the ordinary tensor product.

```lean
noncomputable def tensorObj (F G : CoherentReflexiveModules X) : CoherentReflexiveModules X
```

**`AlgebraicGeometry.CoherentReflexive.tensorObjComm`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentTensor.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentTensor.lean#L154). The attribute's comment: “symmetry”.

> **Stacks Project, Tag 0EBH.**  The tensor product of the category of coherent reflexive
> modules is symmetric: the hull of the braiding of the ordinary tensor product.

```lean
noncomputable def tensorObjComm (F G : CoherentReflexiveModules X) :
    tensorObj F G ≅ tensorObj G F
```

**`AlgebraicGeometry.CoherentReflexive.tensorHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentTensor.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentTensor.lean#L187). The attribute's comment: “internal\_hom”.

> **Stacks Project, Tag 0EBH.**  The internal-Hom adjunction of the category of coherent
> reflexive modules: morphisms out of the hull tensor product `ℱ ⊗_𝒞 𝒢` are morphisms of `ℱ` into
> the internal Hom `ℋom_{𝒪_X}(𝒢, ℋ)`.

```lean
noncomputable def tensorHomEquiv (F G H : CoherentReflexiveModules X) :
    (tensorObj F G ⟶ H) ≃ (F ⟶ internalHomObj G H)
```

**`AlgebraicGeometry.CoherentReflexive.tensorHomEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentTensor.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentTensor.lean#L198). The attribute's comment: “internal\_hom”.

> **Stacks Project, Tag 0EBH.**  The adjunction bijection is the currying map of
> [Stacks, Tag 01CN], applied after restricting along the canonical map from the ordinary tensor
> product to its double dual.  This pins the bijection down.

```lean
theorem tensorHomEquiv_apply (F G H : CoherentReflexiveModules X)
    (f : tensorObj F G ⟶ H) :
    (tensorHomEquiv F G H f).hom.hom =
      Stacks.SheafOfModules.tensorHomEquiv X.toRingedSpace F.obj.obj G.obj.obj H.obj.obj
        (toDoubleDual ((((Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
          ⟨((X.toRingedSpace)).presheaf, ((X.toRingedSpace)).IsSheaf⟩).obj (F.obj.obj)).obj
            (G.obj.obj))) ≫ f.hom.hom)
```

**`AlgebraicGeometry.CoherentReflexive.tensorObjAssoc`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentTensorAssoc.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/CoherentTensorAssoc.lean#L211). The attribute's comment: “associativity”.

> **Stacks Project, Tag 0EBH.**  The tensor product of the category of coherent reflexive
> modules is associative.

```lean
noncomputable def tensorObjAssoc (F G K : CoherentReflexiveModules X) :
    tensorObj (tensorObj F G) K ≅ tensorObj F (tensorObj G K)
```

**`AlgebraicGeometry.isReflexive_reflexiveHull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/HullCoherentReflexive.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/HullCoherentReflexive.lean#L48). The attribute's comment: “hull”.

> The reflexive hull `F^∨∨` of a coherent module on an integral locally Noetherian scheme is
> reflexive: it is the dual of the coherent module `F^∨`, and duals of coherent modules are
> reflexive.

```lean
theorem isReflexive_reflexiveHull (X : Scheme.{u}) [IsIntegral X] [IsLocallyNoetherian X]
    (F : X.Modules) [_root_.SheafOfModules.IsCoherent F] : IsReflexive (reflexiveHull F)
```

**`AlgebraicGeometry.not_forall_fiberRank_one_tensorObj_dualObj_iso_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/RankOneNotInvertible.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/RankOneNotInvertible.lean#L209). The attribute's comment: “unit\_failure”.

> On an integral locally Noetherian scheme a coherent reflexive module of rank one at the
> generic point need not have its dual as a tensor inverse for the hull tensor product.

```lean
theorem not_forall_fiberRank_one_tensorObj_dualObj_iso_unit :
    ¬ ∀ (X : Scheme.{u}) [IsIntegral X] [IsLocallyNoetherian X]
        (F : CoherentReflexiveModules X),
        Scheme.Modules.fiberRank (F.obj.obj : X.Modules) (genericPoint X) = 1 →
        Nonempty ((tensorObj F (dualObj F)).obj.obj ≅ unitModule X)
```

**`AlgebraicGeometry.not_forall_rank_one_sheafHom_iso_dualObj_tensorObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/RankOneNotInvertible.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/RankOneNotInvertible.lean#L224). The attribute's comment: “hom\_failure”.

> On an integral locally Noetherian scheme the sheaf Hom of two coherent reflexive modules of
> rank one at every point need not be the hull tensor product of the dual of the first with the
> second.

```lean
theorem not_forall_rank_one_sheafHom_iso_dualObj_tensorObj :
    ¬ ∀ (X : Scheme.{u}) [IsIntegral X] [IsLocallyNoetherian X]
        (F G : CoherentReflexiveModules X),
        (∀ x : X, Module.rank (X.presheaf.stalk x)
          ((show X.Modules from F.obj.obj).presheaf.stalk x) = 1) →
        (∀ x : X, Module.rank (X.presheaf.stalk x)
          ((show X.Modules from G.obj.obj).presheaf.stalk x) = 1) →
        Nonempty (Stacks.SheafOfModules.sheafHomSpace X.toRingedSpace F.obj.obj G.obj.obj ≅
          (tensorObj (dualObj F) G).obj.obj)
```

**`Stacks.AlgebraicGeometry.ReflexiveEquivalence.isCoherent_doubleDual`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/ReflexiveEquivalence/StalkDescent.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/ReflexiveEquivalence/StalkDescent.lean#L154). The attribute's comment: “hull”.

> **[Stacks, Tag 01Y2] for the double dual.** The reflexive hull `F^∨∨` of a coherent module
> on a locally Noetherian scheme is coherent.  This is the coherence half of the hull assertion of
> [Stacks, Tag 0EBH].

```lean
public lemma isCoherent_doubleDual [IsLocallyNoetherian X] (F : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] :
    _root_.SheafOfModules.IsCoherent (dualSheaf (dualSheaf F))
```

**`Stacks.AlgebraicGeometry.InternalHomLocalKernel.reflexiveHullAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InternalHomLocalKernel/Basic.lean, line 453](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/InternalHomLocalKernel/Basic.lean#L453). The attribute's comment: “adjunction”.

> **Stacks Tag 0EBH.** On an integral locally Noetherian scheme the double-dual functor is
> left adjoint to the inclusion of coherent reflexive modules into coherent modules, with the
> canonical bidual map as its unit.
>
> This is `reflexiveHullAdjunction_of_isLocallyStructureKernel` with its standing hypothesis
> discharged by `isLocallyStructureKernel_dualSheaf_of_isCoherent`.

```lean
noncomputable def reflexiveHullAdjunction (X : Scheme.{u})
    [IsIntegral X] [IsLocallyNoetherian X] :
    { p : (Σ L : ReflexiveHull.CoherentModules X ⥤ ReflexiveHull.CoherentReflexiveModules X,
        L ⊣ ReflexiveHull.inclusion X) //
      ∀ F : ReflexiveHull.CoherentModules X,
        ∃ e : (p.1.obj F).obj.obj = ReflexiveModules.reflexiveHull F.obj,
          (p.2.unit.app F).hom ≫ eqToHom e =
            (ReflexiveModules.toReflexiveHull F.obj).1 }
```

## Tag 0AY5, a lemma

[Tag 0AY5](https://stacks.math.columbia.edu/tag/0AY5) in the Stacks Project.

**`AlgebraicGeometry.isReflexive_iff_stalk_isReflexive_or_depth_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/StalkDepthCriterion.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/StalkDepthCriterion.lean#L122).

> **Stacks Project, Tag 0AY5.** A coherent module on an integral locally Noetherian scheme is
> reflexive if and only if at every point its stalk is either a reflexive module over the local
> ring there or has depth at least two.

```lean
theorem isReflexive_iff_stalk_isReflexive_or_depth_two (X : Scheme.{u}) [IsIntegral X]
    [IsLocallyNoetherian X] (F : X.Modules) [_root_.SheafOfModules.IsCoherent F] :
    IsReflexive F ↔
      ∀ x : X, Module.IsReflexive (X.presheaf.stalk x) (F.presheaf.stalk x) ∨
        (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
          (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (F.presheaf.stalk x)
```

## Tag 0EBI, a lemma

[Tag 0EBI](https://stacks.math.columbia.edu/tag/0EBI) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ReflexiveModules.depth_stalk_ge_two_of_isReflexive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Reflexive/ExtensionChain/Depth.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Reflexive/ExtensionChain/Depth.lean#L169). The attribute's comment: “part (1)”.

> **[Stacks, Tag 0EBI], part (1).** A coherent reflexive module on a locally Noetherian
> scheme has depth at least two at every point where the local ring does.

```lean
public theorem depth_stalk_ge_two_of_isReflexive [IsLocallyNoetherian X] (F : X.Modules)
    [_root_.SheafOfModules.IsCoherent F]
    (hF : IsReflexive F) (x : X)
    (hx : (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
      (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) :
    (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
      (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (F.presheaf.stalk x)
```

**`Stacks.AlgebraicGeometry.ReflexiveModules.sheafHasPropertySk_two_of_isReflexive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Reflexive/ExtensionChain/Depth.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Reflexive/ExtensionChain/Depth.lean#L240). The attribute's comment: “part (2)”.

> **[Stacks, Tag 0EBI], part (2).** On a locally Noetherian scheme satisfying Serre's
> condition `(S₂)`, every coherent reflexive module satisfies `(S₂)`.

```lean
public theorem sheafHasPropertySk_two_of_isReflexive [IsLocallyNoetherian X] (F : X.Modules)
    [_root_.SheafOfModules.IsCoherent F]
    (hF : IsReflexive F) (hX : HasPropertySk X 2) :
    SheafHasPropertySk X F 2
```

**`Stacks.AlgebraicGeometry.ReflexiveStalkDepthTwo.two_le_depth_stalk_of_isCoherent_of_isReflexive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ReflexiveStalkDepthTwo/Basic.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ReflexiveStalkDepthTwo/Basic.lean#L57). The attribute's comment: “part (1)”.

> On a locally Noetherian scheme, a coherent reflexive module has depth at least two at every
> point at which the structure sheaf has depth at least two.

```lean
theorem two_le_depth_stalk_of_isCoherent_of_isReflexive [IsLocallyNoetherian X]
    (G : X.Modules) (hc : G.IsCoherent) (hr : IsReflexive G) (x : X)
    (hx : (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
      (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) :
    (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
      (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
      (TopCat.Presheaf.stalk (C := Ab.{u}) G.val.presheaf x)
```

## Tag 0EBJ, a lemma

[Tag 0EBJ](https://stacks.math.columbia.edu/tag/0EBJ) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ReflexiveModules.reflexiveCoherentEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ReflexiveOpenEquivalence/Pushforward.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ReflexiveOpenEquivalence/Pushforward.lean#L158).

> **Stacks Project, Tag 0EBJ.** Restriction to an open subscheme whose complement
> has structure-sheaf depth at least two is an equivalence on coherent reflexive modules;
> its inverse is direct image. Both identifications are natural.
>
> This is `reflexiveCoherentEquivalenceOfPushforward` with its one hypothesis discharged by
> `isCoherent_and_isReflexive_pushforward`.

```lean
public noncomputable def reflexiveCoherentEquivalence (X : Scheme.{u})
    [AlgebraicGeometry.IsIntegral X] [IsLocallyNoetherian X] (U : X.Opens)
    (hdepth : ∀ x : X, x ∉ (U : Set X) →
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) :
    Σ e : ReflexiveCoherentModules X ≌ ReflexiveCoherentModules U.toScheme,
      (e.functor ⋙ ObjectProperty.ι
          (fun F : U.toScheme.Modules =>
            F.IsCoherent ∧ IsReflexive F) ≅
        ObjectProperty.ι
          (fun F : X.Modules => F.IsCoherent ∧ IsReflexive F) ⋙
          Scheme.Modules.pullback U.ι) ×
      (e.inverse ⋙ ObjectProperty.ι
          (fun F : X.Modules => F.IsCoherent ∧ IsReflexive F) ≅
        ObjectProperty.ι
          (fun F : U.toScheme.Modules =>
            F.IsCoherent ∧ IsReflexive F) ⋙
          Scheme.Modules.pushforward U.ι)
```

## Tag 0AY6, a lemma

[Tag 0AY6](https://stacks.math.columbia.edu/tag/0AY6) in the Stacks Project.

**`AlgebraicGeometry.isReflexive_isTorsionFree_propertyS2_extension_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/NormalCriterion.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/NormalCriterion.lean#L345).

> Let `X` be an integral locally Noetherian normal scheme and let `F` be a coherent
> `𝒪_X`-module. The following are equivalent:
>
> 1. `F` is reflexive;
> 2. `F` is torsion free and satisfies Serre's condition `(S₂)`;
> 3. there is an open subscheme `j : U → X` whose complement has codimension at least two at
>    every point, such that `j^*F` is finite locally free and the canonical map `F → j_*j^*F` is
>    an isomorphism.

```lean
theorem isReflexive_isTorsionFree_propertyS2_extension_tfae (X : Scheme.{u}) [IsIntegral X]
    [IsLocallyNoetherian X] [IsNormal X] (F : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] :
    List.TFAE [
      IsReflexive F,
      IsTorsionFree F ∧ SheafHasPropertySk X F 2,
      ∃ U : X.Opens,
        (∀ x : X, x ∉ U →
          (2 : ℕ∞) ≤ codimension (IrreducibleCloseds.closureSingleton x)) ∧
        SheafOfModules.IsFiniteLocallyFree (F.restrict U.ι) ∧
        IsIso ((Scheme.Modules.pullbackPushforwardAdjunction U.ι).unit.app F)]
```

## Tag 0AY7, a lemma

[Tag 0AY7](https://stacks.math.columbia.edu/tag/0AY7) in the Stacks Project.

**`AlgebraicGeometry.exists_lift_toReflexiveHull_iff_codimension_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/HullExtension.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/HullExtension.lean#L414).

> On an integral locally Noetherian normal scheme, a linear map of generic stalks extends to a
> map into the reflexive hull of its target if and only if, at every point whose local ring has
> dimension one, it carries the image of the source stalk into the image of the target stalk.

```lean
theorem exists_lift_toReflexiveHull_iff_codimension_one (X : Scheme.{u}) [IsIntegral X]
    [IsLocallyNoetherian X] [IsNormal X] (F G : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] [_root_.SheafOfModules.IsCoherent G]
    (T : (G.presheaf.stalk (genericPoint X)) →ₗ[X.functionField]
      (F.presheaf.stalk (genericPoint X))) :
    (∃ e : G ⟶ reflexiveHull F,
      ∀ m : G.presheaf.stalk (genericPoint X),
        ((TopCat.Presheaf.stalkFunctor Ab (genericPoint X)).map
          (Scheme.Modules.Hom.mapPresheaf (X := X) e)) m =
          ((TopCat.Presheaf.stalkFunctor Ab (genericPoint X)).map
            (Scheme.Modules.Hom.mapPresheaf (X := X)
              (toReflexiveHull F).1)) (T m)) ↔
      ∀ x : X, ringKrullDim (X.presheaf.stalk x) = 1 →
        let h : genericPoint X ⤳ x := (genericPoint_spec X).specializes trivial
        Set.MapsTo T (Set.range (G.presheaf.stalkSpecializes h))
          (Set.range (F.presheaf.stalkSpecializes h))
```

## Tag 0B3N, a lemma

[Tag 0B3N](https://stacks.math.columbia.edu/tag/0B3N) in the Stacks Project.

**`AlgebraicGeometry.isReflexive_iff_isFiniteLocallyFree_of_isRegular_of_dim_le_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/RegularDimensionTwo.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/RegularDimensionTwo.lean#L155).

> **Stacks Project, Tag 0B3N.** A coherent module on a regular scheme of dimension at most
> two is reflexive precisely when it is finite locally free.

```lean
theorem isReflexive_iff_isFiniteLocallyFree_of_isRegular_of_dim_le_two (X : Scheme.{u})
    (hX : IsRegular X) (hXdim : topologicalKrullDim X ≤ 2) (F : X.Modules)
    [_root_.SheafOfModules.IsCoherent F] :
    IsReflexive F ↔ SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.13, Tag 0AVT](https://stacks.math.columbia.edu/tag/0AVT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
