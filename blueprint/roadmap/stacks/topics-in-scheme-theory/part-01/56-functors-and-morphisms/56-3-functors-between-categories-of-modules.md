---
declaration: section
origin: cited
lean: ModuleCat.tfae_iso_tensorFunctor_preserves_colimits_isLeftAdjoint, ModuleCat.tensorFunctor, ModuleCat.tensorFunctor_linear, ModuleCat.tensorFunctor_preservesFiniteColimits, ModuleCat.tensorFunctor_preservesDirectSums, ModuleCat.tensorFunctor_preservesColimits, ModuleCat.tensorFunctor_isLeftAdjoint, ModuleCat.tensorFunctorEquivalence
statement: formalized
proof: formalized
---

# 56.3 Functors between categories of modules

Section 56.3 of the Stacks Project, [Tag 0GNR](https://stacks.math.columbia.edu/tag/0GNR). 8 tags here are carried by 24 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GNS, a lemma

[Tag 0GNS](https://stacks.math.columbia.edu/tag/0GNS) in the Stacks Project.

**`ModuleCat.tfae_iso_tensorFunctor_preserves_colimits_isLeftAdjoint`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/BimoduleTensor.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/BimoduleTensor.lean#L311). References: EGA III (7.3.1), “(a) <=> (e)”; EGA III (7.2.6), “(1) <=> (2)”; EGA III (7.2.5), “(a) <=> (c)”.

> A functor between module categories is tensoring with a bimodule iff it is right exact and
> commutes with arbitrary direct sums; these are also equivalent to preserving all colimits and
> to having a right adjoint.

```lean
public lemma tfae_iso_tensorFunctor_preserves_colimits_isLeftAdjoint
    (F : ModuleCat.{u} A ⥤ ModuleCat.{u} B) :
    List.TFAE
      [ ∃ K : ModuleCat.{u} (A ⊗[ℤ] B),
          Nonempty (tensorFunctorOverInt A B K ≅ F),
        PreservesFiniteColimits F ∧
          ∀ J : Type u, PreservesColimitsOfShape (Discrete J) F,
        PreservesColimits F,
        F.IsLeftAdjoint ]
```

## Tag 0GNT, an example

[Tag 0GNT](https://stacks.math.columbia.edu/tag/0GNT) in the Stacks Project.

**`ModuleCat.tensorFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/TensorFunctor.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/TensorFunctor.lean#L72). The attribute's comment: “the functor”.

> Tensoring with an `A ⊗[R] B`-module, regarded as a functor from `A`-modules to
> `B`-modules.

```lean
public noncomputable def tensorFunctor
    (K : ModuleCat.{u} (A ⊗[R] B)) : ModuleCat.{u} A ⥤ ModuleCat.{u} B
```

**`ModuleCat.tensorFunctor_linear`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/TensorFunctor.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/TensorFunctor.lean#L82). The attribute's comment: “R-linearity”.

> Tensoring with an `A ⊗[R] B`-module is `R`-linear.

```lean
public lemma tensorFunctor_linear (K : ModuleCat.{u} (A ⊗[R] B)) :
    (tensorFunctor R A B K).Linear R
```

**`ModuleCat.tensorFunctor_preservesFiniteColimits`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/TensorFunctor.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/TensorFunctor.lean#L95). The attribute's comment: “right exactness”.

> Tensoring with an `A ⊗[R] B`-module is right exact.

```lean
public lemma tensorFunctor_preservesFiniteColimits (K : ModuleCat.{u} (A ⊗[R] B)) :
    PreservesFiniteColimits (tensorFunctor R A B K)
```

**`ModuleCat.tensorFunctor_preservesDirectSums`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/TensorFunctor.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/TensorFunctor.lean#L100). The attribute's comment: “arbitrary direct sums”.

> Tensoring with an `A ⊗[R] B`-module commutes with arbitrary direct sums.

```lean
public lemma tensorFunctor_preservesDirectSums (K : ModuleCat.{u} (A ⊗[R] B))
    (J : Type u) :
    PreservesColimitsOfShape (Discrete J) (tensorFunctor R A B K)
```

**`ModuleCat.tensorFunctor_preservesColimits`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/TensorFunctor.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/TensorFunctor.lean#L107). The attribute's comment: “all colimits”.

> Tensoring with an `A ⊗[R] B`-module commutes with all colimits.

```lean
public lemma tensorFunctor_preservesColimits (K : ModuleCat.{u} (A ⊗[R] B)) :
    PreservesColimits (tensorFunctor R A B K)
```

**`ModuleCat.tensorFunctor_isLeftAdjoint`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/TensorFunctor.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/TensorFunctor.lean#L112). The attribute's comment: “right adjoint”.

> Tensoring with an `A ⊗[R] B`-module has a right adjoint.

```lean
public lemma tensorFunctor_isLeftAdjoint (K : ModuleCat.{u} (A ⊗[R] B)) :
    (tensorFunctor R A B K).IsLeftAdjoint
```

## Tag 0GNV, a lemma

[Tag 0GNV](https://stacks.math.columbia.edu/tag/0GNV) in the Stacks Project.

**`ModuleCat.tensorFunctorEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/LinearTensorEquivalence.lean, line 782](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/LinearTensorEquivalence.lean#L782). The attribute's comment: “the equivalence”. References: EGA III (7.2.6), “commutative rings”.

> Modules over `A ⊗[R] B` are equivalent to `R`-linear right exact functors from
> `A`-modules to `B`-modules which preserve arbitrary direct sums.

```lean
public noncomputable def tensorFunctorEquivalence :
    ModuleCat.{u} (A ⊗[R] B) ≌
      ObjectProperty.FullSubcategory
        (IsLinearRightExactAndPreservesDirectSums R A B)
```

**`ModuleCat.tensorFunctorEquivalence_functorIso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/LinearTensorEquivalence.lean, line 793](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/LinearTensorEquivalence.lean#L793). The attribute's comment: “given by tensoring”. References: EGA III (7.2.6), “N ↦ T_N”.

> The functor underlying `tensorFunctorEquivalence` is naturally isomorphic to the functor
> which sends a module `K` to tensoring with `K`.

```lean
public lemma tensorFunctorEquivalence_functorIso :
    Nonempty
      ((tensorFunctorEquivalence R A B).functor ≅ moduleTensorFunctorLift R A B)
```

## Tag 0GNW, a remark

[Tag 0GNW](https://stacks.math.columbia.edu/tag/0GNW) in the Stacks Project.

**`ModuleCat.moduleTensorFunctor_comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/TensorComposition.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/TensorComposition.lean#L254).

> The tensor product over the middle algebra represents the composite of two tensor functors. The
> equation on pure tensors records the canonical action of `A ⊗[R] C`, and the functor isomorphism
> includes naturality in the input `A`-module.

```lean
public lemma moduleTensorFunctor_comp
    (K : ModuleCat.{u} (A ⊗[R] B)) (K' : ModuleCat.{u} (B ⊗[R] C)) :
    letI : Module A K := Module.compHom K
      (Algebra.TensorProduct.includeLeftRingHom (R := R) (A := A) (B := B))
    letI : Module B K := Module.compHom K
      (Algebra.TensorProduct.includeRight (R := R) (A := A) (B := B)).toRingHom
    letI : Module B K' := Module.compHom K'
      (Algebra.TensorProduct.includeLeftRingHom (R := R) (A := B) (B := C))
    letI : Module C K' := Module.compHom K'
      (Algebra.TensorProduct.includeRight (R := R) (A := B) (B := C)).toRingHom
    ∃ inst : Module (A ⊗[R] C) (K ⊗[B] K'),
      letI : Module (A ⊗[R] C) (K ⊗[B] K') := inst
      (∀ (a : A) (c : C) (k : K) (k' : K'),
        (a ⊗ₜ[R] c) • (k ⊗ₜ[B] k') = (a • k) ⊗ₜ[B] (c • k')) ∧
      Nonempty
        ((moduleTensorFunctor R A C).obj
            (ModuleCat.of (A ⊗[R] C) (K ⊗[B] K')) ≅
          ((moduleTensorFunctor R A B).obj K ⋙
            (moduleTensorFunctor R B C).obj K'))
```

## Tag 0GNX, a remark

[Tag 0GNX](https://stacks.math.columbia.edu/tag/0GNX) in the Stacks Project.

**`ModuleCat.tensorFunctor_exact_iff_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/TensorFunctorExactness.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/TensorFunctorExactness.lean#L139). References: EGA 0 (6.1.1), “more general”.

> Tensoring with an `A ⊗[R] B`-module `K` is an exact functor from `A`-modules to `B`-modules if
> and only if `K` is flat as an `A`-module.

```lean
public theorem tensorFunctor_exact_iff_flat
    (R A B : Type u) [CommRing R] [CommRing A] [CommRing B] [Algebra R A] [Algebra R B]
    (K : ModuleCat.{u} (A ⊗[R] B)) :
    exactFunctor (ModuleCat.{u} A) (ModuleCat.{u} B) (tensorFunctor R A B K) ↔
      Module.Flat A ((restrictScalars
        (Algebra.TensorProduct.includeLeftRingHom (R := R) (A := A) (B := B))).obj K)
```

## Tag 0GP0, a lemma

[Tag 0GP0](https://stacks.math.columbia.edu/tag/0GP0) in the Stacks Project.

**`ModuleCat.exists_ringEquiv_invertible_iso_extensionTensorFunctor`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/ModuleEquivalences.lean, line 627](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/ModuleEquivalences.lean#L627).

> **Stacks Project, Tag 0GP0.** Every equivalence between categories of modules is extension
> of scalars along an isomorphism of the rings, followed by tensoring with an invertible module.

```lean
public lemma exists_ringEquiv_invertible_iso_extensionTensorFunctor
    (A B : Type u) [CommRing A] [CommRing B]
    (F : ModuleCat.{u} A ⥤ ModuleCat.{u} B) [F.IsEquivalence] :
    ∃ (e : A ≃+* B) (L : ModuleCat.{u} B),
      Module.Invertible B L ∧ Nonempty (F ≅ extensionTensorFunctor A B e L)
```

## Tag 0GP1, a lemma

[Tag 0GP1](https://stacks.math.columbia.edu/tag/0GP1) in the Stacks Project.

**`ModuleCat.exists_algEquiv_invertible_iso_extensionTensorFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/LinearModuleEquivalences.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/LinearModuleEquivalences.lean#L89).

> **Stacks Project, Tag 0GP1.** An equivalence of module categories linear over the base
> ring is extension of scalars along an algebra isomorphism, followed by tensoring with an
> invertible module.

```lean
public theorem exists_algEquiv_invertible_iso_extensionTensorFunctor
    (R : Type v) (A B : Type u) [CommRing R] [CommRing A] [CommRing B]
    [Algebra R A] [Algebra R B]
    (F : ModuleCat.{u} A ⥤ ModuleCat.{u} B) [F.IsEquivalence]
    [F.Linear R] :
    ∃ (e : A ≃ₐ[R] B) (L : ModuleCat.{u} B),
      Module.Invertible B L ∧
        Nonempty (F ≅ extensionTensorFunctor A B e.toRingEquiv L)
```

## Tag 0GP2, a remark

[Tag 0GP2](https://stacks.math.columbia.edu/tag/0GP2) in the Stacks Project.

**`ModuleCat.monoidHomOfMonoidal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean#L101). The attribute's comment: “part (2): multiplicative scalar map”.

> A monoidal functor canonically induces a multiplicative map on scalars.

```lean
public noncomputable def monoidHomOfMonoidal
    (F : ModuleCat.{u} A ⥤ ModuleCat.{u} B) [F.Monoidal] :
    { φ : A →* B // ∀ a, φ a = scalarValue F a }
```

**`ModuleCat.scalarValue_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean#L147). The attribute's comment: “part (4): additive scalar map”.

> The scalar map of an additive monoidal functor preserves addition.

```lean
public theorem scalarValue_add (F : ModuleCat.{u} A ⥤ ModuleCat.{u} B)
    [F.Monoidal] [F.Additive] (a b : A) :
    scalarValue F (a + b) = scalarValue F a + scalarValue F b
```

**`ModuleCat.ringHomOfAdditive`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean#L172). The attribute's comment: “part (4): ring homomorphism”.

> An additive monoidal functor induces a ring homomorphism.

```lean
public noncomputable def ringHomOfAdditive
    (F : ModuleCat.{u} A ⥤ ModuleCat.{u} B) [F.Monoidal] [F.Additive] :
    { φ : A →+* B // ∀ a, φ a = scalarValue F a }
```

**`ModuleCat.tensorSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean#L185). The attribute's comment: “part (3): tensor-square example”.

> Tensor squaring is a monoidal functor whose scalar map is squaring.

```lean
public theorem tensorSquare (A : Type u) [CommRing A] :
    ∃ h : (tensorSquareFunctor A).Monoidal,
      ∀ a : A, letI : (tensorSquareFunctor A).Monoidal := h
        scalarValue (tensorSquareFunctor A) a = a ^ 2
```

**`ModuleCat.torsionFreeQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean#L302). The attribute's comment: “part (5): monoidal torsion-free quotient”.

> Quotienting abelian groups by torsion is monoidal.

```lean
public theorem torsionFreeQuotient :
    Nonempty torsionFreeQuotientFunctor.{u}.Monoidal
```

**`ModuleCat.torsionFreeQuotient_scalarValue`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean#L383). The attribute's comment: “part (5): induced scalar map is the identity”.

> For any monoidal structure on torsion-free quotient, conjugating the image of
> each scalar endomorphism of the monoidal unit gives that same scalar endomorphism.
> This expresses that the induced scalar map is the identity in every module universe.

```lean
public theorem torsionFreeQuotient_scalarValue
    (h : torsionFreeQuotientFunctor.{u}.Monoidal) (a : ℤ) :
    letI : torsionFreeQuotientFunctor.{u}.Monoidal := h
    (Functor.Monoidal.εIso torsionFreeQuotientFunctor.{u}).hom ≫
      torsionFreeQuotientFunctor.{u}.map
        (a • (𝟙 (𝟙_ (ModuleCat.{u} ℤ)))) ≫
      (Functor.Monoidal.εIso torsionFreeQuotientFunctor.{u}).inv =
        a • (𝟙 (𝟙_ (ModuleCat.{u} ℤ)))
```

**`ModuleCat.torsionFreeQuotient_scalar_action`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean#L409). The attribute's comment: “part (5): scalar endomorphisms on all modules”.

> Torsion-free quotient preserves multiplication by every integer on every module.

```lean
public theorem torsionFreeQuotient_scalar_action (M : ModuleCat.{u} ℤ) (a : ℤ) :
    torsionFreeQuotientFunctor.{u}.map
        (ModuleCat.ofHom (a • (LinearMap.id : M →ₗ[ℤ] M))) =
      ModuleCat.ofHom (a • (LinearMap.id :
        torsionFreeQuotientFunctor.{u}.obj M →ₗ[ℤ]
          torsionFreeQuotientFunctor.{u}.obj M))
```

**`ModuleCat.torsionFreeQuotient_not_iso_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean#L419). The attribute's comment: “part (5): nonidentity example”.

> Torsion-free quotient is not naturally isomorphic to the identity functor.

```lean
public theorem torsionFreeQuotient_not_iso_id :
    ¬ Nonempty (torsionFreeQuotientFunctor.{u} ≅ 𝟭 (ModuleCat.{u} ℤ))
```

**`ModuleCat.iso_extendScalars_of_rightExact_preservesDirectSums`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean, line 634](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean#L634). The attribute's comment: “part (6): extension of scalars”.

> A right-exact monoidal functor commuting with direct sums is extension of
> scalars along its induced ring map, compatibly with the monoidal structures.

```lean
public theorem iso_extendScalars_of_rightExact_preservesDirectSums
    (F : ModuleCat.{u} A ⥤ ModuleCat.{u} B) [F.Monoidal]
    [PreservesFiniteColimits F]
    (hF : ∀ J : Type u, PreservesColimitsOfShape (Discrete J) F) :
    ∃ φ : A →+* B,
      (∀ a, φ a = scalarValue F a) ∧
        ∃ i : F ≅ ModuleCat.extendScalars φ,
          NatTrans.IsMonoidal i.hom
```

**`ModuleCat.extendScalars_injective_up_to_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean, line 672](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean#L672). The attribute's comment: “classification: uniqueness”.

> Ring maps are uniquely determined by the corresponding monoidal extension-of-scalars
> functors, up to natural isomorphism.

```lean
public theorem extendScalars_injective_up_to_iso (φ ψ : A →+* B)
    (h : Nonempty (ModuleCat.extendScalars.{u, u, u} φ ≅
      ModuleCat.extendScalars.{u, u, u} ψ)) :
    φ = ψ
```

**`ModuleCat.extendScalars_monoidal_preservesColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean, line 694](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean#L694). The attribute's comment: “classification: existence”.

> Every ring map gives a cocontinuous monoidal extension-of-scalars functor.

```lean
public theorem extendScalars_monoidal_preservesColimits (φ : A →+* B) :
    Nonempty (ModuleCat.extendScalars.{u, u, u} φ).Monoidal ∧
      PreservesColimits (ModuleCat.extendScalars.{u, u, u} φ)
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.Monoidal.εIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.Monoidal.εIso#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsBetweenCategories/MonoidalFunctors.lean#L97) (StacksFrontier): “part (1): the unit isomorphism”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 56.3, Tag 0GNR](https://stacks.math.columbia.edu/tag/0GNR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
