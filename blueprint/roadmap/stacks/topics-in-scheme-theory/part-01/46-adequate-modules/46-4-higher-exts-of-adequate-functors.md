---
declaration: section
origin: cited
lean: AdequateFunctor.exists_adequate_homEquiv, AdequateFunctor.moduleValuedFunctor_enoughInjectives, AdequateFunctor.fullyFaithful_adequateInclusion, AdequateFunctor.preservesFiniteLimits_adequateInclusion, AdequateFunctor.preservesFiniteColimits_adequateInclusion, AdequateFunctor.adequateCoreflectionAdjunction, AdequateFunctor.preservesFiniteLimits_adequateCoreflection, AdequateFunctor.preservesInjectiveObjects_adequateCoreflection
statement: formalized
proof: formalized
---

# 46.4 Higher exts of adequate functors

Section 46.4 of the Stacks Project, [Tag 06Z5](https://stacks.math.columbia.edu/tag/06Z5). 11 tags here are carried by 44 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06Z6, a lemma

[Tag 06Z6](https://stacks.math.columbia.edu/tag/06Z6) in the Stacks Project.

**`AdequateFunctor.exists_adequate_homEquiv`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/Coreflection.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/Coreflection.lean#L264).

> **Stacks Project, Tag 06Z6.** For every module-valued functor `F` there is an adequate
> functor `Q F` and a morphism `Q F ⟶ F` of module-valued functors such that every morphism to `F`
> from an adequate functor factors uniquely through it.

```lean
public lemma exists_adequate_homEquiv
    (F : ModuleValuedFunctor.{max (u + 1) (v + 1) w, v} A) :
    ∃ (QF : ModuleValuedFunctor.{max (u + 1) (v + 1) w, v} A)
      (_ : IsAdequate (𝟭 _) QF) (q : QF ⟶ F),
      ∀ (G : ModuleValuedFunctor.{max (u + 1) (v + 1) w, v} A), IsAdequate (𝟭 _) G →
        ∀ φ : G ⟶ F, ∃! ψ : G ⟶ QF, ψ ≫ q = φ
```

## Tag 06Z7, a lemma

[Tag 06Z7](https://stacks.math.columbia.edu/tag/06Z7) in the Stacks Project.

**`AdequateFunctor.moduleValuedFunctor_enoughInjectives`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/Basic.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/Basic.lean#L49). The attribute's comment: “module\_valued\_functors\_enough\_injectives”.

> **Stacks Project, Tag 06Z7.** Module-valued functors on any category of algebras, in
> particular the algebras admitted by a big site, have enough injectives.

```lean
instance moduleValuedFunctor_enoughInjectives (C : Type u) [Category.{v} C]
    (R : Cᵒᵖ ⥤ RingCat.{w}) :
    EnoughInjectives (PresheafOfModules.{max u v w t} R)
```

**`AdequateFunctor.fullyFaithful_adequateInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/Coreflection.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/Coreflection.lean#L93). The attribute's comment: “part (1), i is fully faithful”.

> **Stacks Project, Tag 06Z7**, part (1), the full faithfulness of `i`. The adequate functors
> form a full subcategory of the module-valued functors, so their inclusion is fully faithful.

```lean
public noncomputable def fullyFaithful_adequateInclusion :
    (adequate.{u, v, max u v w} A).ι.FullyFaithful
```

**`AdequateFunctor.preservesFiniteLimits_adequateInclusion`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/Coreflection.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/Coreflection.lean#L101). The attribute's comment: “part (1), i is left exact”.

> **Stacks Project, Tag 06Z7**, part (1), the left exactness of `i`. The adequate functors are
> closed under kernels, so a kernel of adequate functors is already the kernel of the underlying
> module-valued functors.

```lean
public lemma preservesFiniteLimits_adequateInclusion :
    PreservesFiniteLimits (adequate.{u, v, max u v w} A).ι
```

**`AdequateFunctor.preservesFiniteColimits_adequateInclusion`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/Coreflection.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/Coreflection.lean#L111). The attribute's comment: “part (1), i is right exact”.

> **Stacks Project, Tag 06Z7**, part (1), the right exactness of `i`. The adequate functors are
> closed under cokernels, so a cokernel of adequate functors is already the cokernel of the
> underlying module-valued functors.

```lean
public lemma preservesFiniteColimits_adequateInclusion :
    PreservesFiniteColimits (adequate.{u, v, max u v w} A).ι
```

**`AdequateFunctor.adequateCoreflectionAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/Coreflection.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/Coreflection.lean#L255). The attribute's comment: “part (3), Q is a right adjoint to i”.

> **Stacks Project, Tag 06Z7**, part (3), the adjunction itself: the functor `Q` of
> [Stacks, Tag 06Z6] is a right adjoint to the inclusion `i` of the adequate module-valued
> functors into all module-valued functors.

```lean
public noncomputable def adequateCoreflectionAdjunction :
    (adequate.{u, v, max (u + 1) (v + 1) w} A).ι ⊣ adequateCoreflection.{u, v, w} A
```

**`AdequateFunctor.preservesFiniteLimits_adequateCoreflection`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/Coreflection.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/Coreflection.lean#L292). The attribute's comment: “part (3), Q is left exact”.

> **Stacks Project, Tag 06Z7**, part (3), the left exactness: a right adjoint preserves all
> limits, in particular the finite ones.

```lean
public lemma preservesFiniteLimits_adequateCoreflection :
    PreservesFiniteLimits (adequateCoreflection.{u, v, w} A)
```

**`AdequateFunctor.preservesInjectiveObjects_adequateCoreflection`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/Coreflection.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/Coreflection.lean#L301). The attribute's comment: “part (4)”.

> **Stacks Project, Tag 06Z7**, part (4). The functor `Q` transforms injectives into
> injectives: it is right adjoint to the exact functor `i`, so [Stacks, Tag 015Z] applies.

```lean
public lemma preservesInjectiveObjects_adequateCoreflection :
    (adequateCoreflection.{u, v, w} A).PreservesInjectiveObjects
```

**`AdequateFunctor.adequateFunctor_enoughInjectives`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/EnoughInjectives.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/EnoughInjectives.lean#L91). The attribute's comment: “adequate\_functors\_enough\_injectives”.

> **Stacks Project, Tag 06Z7.** The adequate module-valued functors on the commutative
> `A`-algebras have enough injectives: every one of them embeds into the extension of a pure
> injective `A`-module, and such an extension is an injective object.

```lean
public instance adequateFunctor_enoughInjectives {A : Type u} [CommRing A] :
    EnoughInjectives ((adequate.{u, v, max u v w} A).FullSubcategory)
```

**`AdequateFunctor.adequate_isWeakSerreClass`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/WeakSerre.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/WeakSerre.lean#L79). The attribute's comment: “part (1), the image of i is a weak Serre subcategory”.

> **Stacks Project, Tag 06Z7**, part (1), the image of `i` is a weak Serre subcategory. The
> adequate module-valued functors are a strictly full subcategory containing the zero functor and
> closed under kernels, cokernels and extensions, which is the characterisation of a weak Serre
> subcategory of [Stacks, Tag 0754].

```lean
public instance adequate_isWeakSerreClass :
    (adequate.{u, u, u} A).IsWeakSerreClass
```

**`AdequateFunctor.adequateInclusion_fullyFaithful_exact_isWeakSerreClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/WeakSerre.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/WeakSerre.lean#L95). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 06Z7**, part (1), in full and at one instantiation: the inclusion `i`
> of the adequate module-valued functors into all module-valued functors on `Alg_A` is fully
> faithful and exact, and its image is a weak Serre subcategory.
>
> The three conjuncts other than the last are instantiations of
> `AdequateFunctor.fullyFaithful_adequateInclusion`,
> `AdequateFunctor.preservesFiniteLimits_adequateInclusion` and
> `AdequateFunctor.preservesFiniteColimits_adequateInclusion`, which hold at the wider
> `adequate.{u, v, max u v w}`; the last holds at the universes of
> `AdequateFunctor.isAdequate_of_shortExact`. This conjunction records that all four are
> simultaneously available for one and the same category, namely the module-valued functors on the
> `A`-algebras whose carriers lie in the universe of `A`.

```lean
public theorem adequateInclusion_fullyFaithful_exact_isWeakSerreClass :
    (adequate.{u, u, u} A).ι.Full ∧ (adequate.{u, u, u} A).ι.Faithful ∧
      PreservesFiniteLimits (adequate.{u, u, u} A).ι ∧
      PreservesFiniteColimits (adequate.{u, u, u} A).ι ∧
      (adequate.{u, u, u} A).IsWeakSerreClass
```

## Tag 06Z8, a lemma

[Tag 06Z8](https://stacks.math.columbia.edu/tag/06Z8) in the Stacks Project.

**`AdequateFunctor.tangentKernel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean#L213). The attribute's comment: “parts (1) and (2): the kernel with its restricted module structure”.

> The tangent kernel, with scalars restricted along the zero section `B → B[N]`.

```lean
noncomputable def tangentKernel (X : AlgebraModulePair.{v} A) :
    Submodule X.algebra (extensionValue A F X)
```

**`AdequateFunctor.tangentFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean#L269). The attribute's comment: “part (3): the canonical tangent functor”.

> The canonical tangent functor on pairs of algebras and modules.

```lean
noncomputable def tangentFunctor : TangentFunctorData A F
```

**`AdequateFunctor.tangentDecompositionData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean#L327). The attribute's comment: “the canonical direct-sum decomposition”.

> The canonical decomposition, specified by the sum of the zero section and the kernel
> inclusion as its inverse.

```lean
noncomputable def tangentDecompositionData (X : AlgebraModulePair.{v} A) :
    TangentDecompositionData A F X
```

**`AdequateFunctor.tangentMultiplicationData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean#L404). The attribute's comment: “part (4): the canonical multiplication map”.

> Multiplication by the square-zero ideal, specified on pure tensors.

```lean
noncomputable def tangentMultiplicationData (X : AlgebraModulePair.{v} A) :
    {μ : TensorProduct X.algebra X.module (moduleValue A F X.algebra) →ₗ[X.algebra]
        tangentModule A F X //
      ∀ (n : X.module) (y : moduleValue A F X.algebra),
        (μ (TensorProduct.tmul X.algebra n y) : extensionValue A F X) =
          squareZeroInr A X n •
            moduleValueMap A F (squareZeroSection A X) y}
```

**`AdequateFunctor.tangentDecomposition_fst`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean#L478). The attribute's comment: “the augmentation coordinate of the decomposition”.

> The first coordinate of the canonical decomposition is the augmentation.

```lean
lemma tangentDecomposition_fst (X : AlgebraModulePair.{v} A) (x : extensionValue A F X) :
    (tangentDecomposition A F X x).1 =
      moduleValueMap A F (squareZeroAugmentation A X) x
```

**`AdequateFunctor.tangentDecomposition_naturality`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean, line 493](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean#L493). The attribute's comment: “naturality of the decomposition”.

> The decomposition is natural for morphisms of pairs, including changes of base algebra.

```lean
lemma tangentDecomposition_naturality {X Y : AlgebraModulePair.{v} A} (f : X ⟶ Y)
    (x : extensionValue A F X) :
    tangentDecomposition A F Y (moduleValueMap A F (squareZeroMap A f) x) =
      (moduleValueMap A F f.base (tangentDecomposition A F X x).1,
        (tangentFunctor A F).map f (tangentDecomposition A F X x).2)
```

**`AdequateFunctor.tangentMultiplication_naturality`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean, line 520](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean#L520). The attribute's comment: “part (4): naturality of multiplication”.

> The multiplication maps form a natural transformation on the category of pairs.

```lean
lemma tangentMultiplication_naturality {X Y : AlgebraModulePair.{v} A} (f : X ⟶ Y)
    (t : TensorProduct X.algebra X.module (moduleValue A F X.algebra)) :
    (tangentFunctor A F).map f (tangentMultiplication A F X t) =
      tangentMultiplication A F Y
        (TensorProduct.map f.linear (moduleValueMap A F f.base) t)
```

**`AdequateFunctor.tangentModule_subsingleton`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean, line 546](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean#L546). The attribute's comment: “part (5): vanishing at the zero module”.

> The tangent module of a zero module is zero.

```lean
lemma tangentModule_subsingleton (X : AlgebraModulePair.{v} A) [Subsingleton X.module] :
    Subsingleton (tangentModule A F X)
```

**`AdequateFunctor.tangentFunctor_map_eq_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean, line 581](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean#L581). The attribute's comment: “part (5): zero module maps induce zero tangent maps”.

> A morphism of pairs whose module map is zero induces the zero tangent map.

```lean
lemma tangentFunctor_map_eq_zero {X Y : AlgebraModulePair.{v} A} (f : X ⟶ Y)
    (hf : f.linear = 0) : (tangentFunctor A F).map f = 0
```

## Tag 06ZA, a lemma

[Tag 06ZA](https://stacks.math.columbia.edu/tag/06ZA) in the Stacks Project.

**`AdequateFunctor.map_comp_eq_zero_and_epi_tangentFunctorAt_map_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/InjectiveTangentSurjective.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/InjectiveTangentSurjective.lean#L236). The attribute's comment: “Stacks erratum, corrected statement: the tangent sequence `TI(B,N₁) → TI(B,N) → TI(B,N₂) → 0` of an injective module-valued functor is a complex and is exact at `TI(B,N₂)`. Exactness at `TI(B,N)`, also asserted by the source, is false: its negation is `AdequateFunctor.not_forall_exact_map_tangentFunctorAt_of_injective`. The module universe of `I` is the universe of the algebras.”.

> **Tag 06ZA, corrected.  Stacks erratum.**  Let `I` be an injective object of the category
> of module-valued functors on `Alg_A`.  For every `A`-algebra `B` and every short exact
> sequence `0 → N₁ → N → N₂ → 0` of `B`-modules, the sequence
> `TI(B, N₁) → TI(B, N) → TI(B, N₂) → 0` is a complex and is exact at `TI(B, N₂)`: the
> composite `TI(B, N₁) → TI(B, N₂)` is zero and `TI(B, N) → TI(B, N₂)` is an epimorphism.
>
> The source asserts that the sequence is exact.  **Exactness at `TI(B, N)` is false**, and is
> refuted by `AdequateFunctor.not_forall_exact_map_tangentFunctorAt_of_injective`: the
> counterexample takes the field `k = ℚ`, the algebra `C = k[ε]/(ε²)`, the injective `C`-module
> `J = Hom_k(C, k)` and the coinduced functor `I(D) = ∏_{α : D →ₐ C} J`, whose tangent module
> `TI(k, V)` is the functions `V^* → J` vanishing at `0`; on `0 → k → k² → k → 0` the function
> sending the first-coordinate functional to `0 ≠ j ∈ J` and everything else to `0` is killed
> by `TI(k, k²) → TI(k, k)` and is not in the image of `TI(k, k) → TI(k, k²)`, every element of
> which takes equal values at `(1, 0)` and `(1, 1)`.
>
> Surjectivity at `TI(B, N₂)` is unaffected: its proof does not use the coequalizer step that
> the counterexample refutes.

```lean
theorem map_comp_eq_zero_and_epi_tangentFunctorAt_map_of_injective
    (I : PresheafOfModules.{v} (algebraStructurePresheaf.{v} A)) [Injective I]
    (B : Type v) [CommRing B] [Algebra A B] (S : ShortComplex (ModuleCat.{v} B))
    (hS : S.ShortExact) :
    (tangentFunctorAt A I B).map S.f ≫ (tangentFunctorAt A I B).map S.g = 0 ∧
      Epi ((tangentFunctorAt A I B).map S.g)
```

**`AdequateFunctor.not_forall_exact_map_tangentFunctorAt_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/InjectiveTangentNotRightExact.lean, line 440](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Algebra/InjectiveTangentNotRightExact.lean#L440). The attribute's comment: “Stacks erratum: the negation of the exactness at `TI(B,N)` asserted by the source, witnessed by the injective functor coinduced from `ℚ[ε]` and the sequence `0 → ℚ → ℚ² → ℚ → 0`. The corrected statement is `AdequateFunctor.map_comp_eq_zero_and_epi_tangentFunctorAt_map_of_injective`.”.

> **Exactness at `TI(B, N)` in Tag 06ZA is false.  Stacks erratum.**
> The source asserts that for every ring `A`, every injective object `I` of the category of
> module-valued functors on `Alg_A`, every `A`-algebra `B` and every short exact sequence
> `0 → N₁ → N → N₂ → 0` of `B`-modules, the sequence `TI(B, N₁) → TI(B, N) → TI(B, N₂) → 0` is
> exact.  This is the negation of its exactness at the middle term `TI(B, N)`.
>
> The witness is the one of
> `AdequateFunctor.not_forall_hasRightExactTangentFunctor_of_injective`: the injective functor
> `AdequateFunctor.coinducedDualNum` and `0 → ℚ → ℚ² → ℚ → 0`.  Since the other conjunct,
> exactness at `TI(B, N₂)`, does hold for every injective functor
> (`AdequateFunctor.epi_tangentFunctorAt_map_of_injective`), middle exactness is exactly the
> part that fails.  The corrected statement is
> `AdequateFunctor.map_comp_eq_zero_and_epi_tangentFunctorAt_map_of_injective`.

```lean
theorem not_forall_exact_map_tangentFunctorAt_of_injective :
    ¬ ∀ (A : Type) [CommRing A]
        (I : PresheafOfModules.{0} (algebraStructurePresheaf.{0} A)), Injective I →
        ∀ (B : Type) [CommRing B] [Algebra A B] (S : ShortComplex (ModuleCat.{0} B)),
          S.ShortExact → (S.map (tangentFunctorAt A I B)).Exact
```

## Tag 06ZB, a lemma

[Tag 06ZB](https://stacks.math.columbia.edu/tag/06ZB) in the Stacks Project.

**`AdequateFunctor.tangentTensorEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/FinitelyPresentedTangent.lean, line 761](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/FinitelyPresentedTangent.lean#L761). The attribute's comment: “tensor\_finitely\_presented”.

> The canonical tensor-product description of the tangent module of a
> finitely presented module, using the second action on both tangent modules.

```lean
noncomputable def tangentTensorEquiv
    (S : RightExactTangentFunctor.{u, v, w})
    (B : Type v) [CommRing B] [Algebra S.A B]
    (N : Type v) [AddCommGroup N] [Module B N]
    [Module.FinitePresentation B N] :
    let X : AlgebraModulePair.{v} S.A := { algebra := B, module := B }
    let Y : AlgebraModulePair.{v} S.A := { algebra := B, module := N }
    letI : Module B (tangentModule S.A S.F X) :=
      (secondModuleStructure S X).1
    letI : Module B (tangentModule S.A S.F Y) :=
      (secondModuleStructure S Y).1
    { e : TensorProduct B (tangentModule S.A S.F X) N ≃ₗ[B]
        tangentModule S.A S.F Y //
      ∀ (x : tangentModule S.A S.F X) (n : N),
        e (TensorProduct.tmul B x n) =
          (tangentFunctor S.A S.F).map
            ({ base := AlgHom.id S.A B
               linear := (LinearMap.id : B →ₗ[B] B).smulRight n } : X ⟶ Y) x }
```

**`AdequateFunctor.tangentModule_prod_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/SecondModuleStructure.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/SecondModuleStructure.lean#L62). The attribute's comment: “direct\_sum”.

> A right exact tangent functor carries a binary direct sum of modules to
> the direct sum of their tangent modules, via the two projections.

```lean
theorem tangentModule_prod_bijective
    (T : RightExactTangentFunctor.{u, v, w})
    (B : Type v) [CommRing B] [Algebra T.A B]
    (N₁ N₂ : Type v) [AddCommGroup N₁] [Module B N₁]
    [AddCommGroup N₂] [Module B N₂] :
    Function.Bijective
      (fun x : tangentModule T.A T.F
          ({ algebra := B, module := N₁ × N₂ } : AlgebraModulePair.{v} T.A) =>
        ((tangentFunctor T.A T.F).map
            ({ base := AlgHom.id T.A B
               linear := LinearMap.fst B N₁ N₂ } :
              ({ algebra := B, module := N₁ × N₂ } : AlgebraModulePair.{v} T.A) ⟶
              ({ algebra := B, module := N₁ } : AlgebraModulePair.{v} T.A)) x,
         (tangentFunctor T.A T.F).map
            ({ base := AlgHom.id T.A B
               linear := LinearMap.snd B N₁ N₂ } :
              ({ algebra := B, module := N₁ × N₂ } : AlgebraModulePair.{v} T.A) ⟶
              ({ algebra := B, module := N₂ } : AlgebraModulePair.{v} T.A)) x))
```

**`AdequateFunctor.secondModuleStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/SecondModuleStructure.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/SecondModuleStructure.lean#L299). The attribute's comment: “second\_module\_structure”.

> The second module structure on a tangent module, characterized by the
> action induced by multiplication on the module variable.

```lean
noncomputable def secondModuleStructure (X : AlgebraModulePair.{v} S.A) :
    { m : Module X.algebra (tangentModule S.A S.F X) //
      ∀ (b : X.algebra) (x : tangentModule S.A S.F X),
        m.toDistribMulAction.toSMul.smul b x =
          secondScalarAction S.A S.F X x b }
```

**`AdequateFunctor.secondScalarAction_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/SecondModuleStructure.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/SecondModuleStructure.lean#L403). The attribute's comment: “second\_module\_structure”.

> Tangent maps commute with the second scalar action, semilinearly over
> their maps of base algebras.

```lean
theorem secondScalarAction_naturality {X Y : AlgebraModulePair.{v} S.A}
    (f : X ⟶ Y) (x : tangentModule S.A S.F X) (b : X.algebra) :
    (tangentFunctor S.A S.F).map f (secondScalarAction S.A S.F X x b) =
      secondScalarAction S.A S.F Y ((tangentFunctor S.A S.F).map f x) (f.base b)
```

**`AdequateFunctor.tangentMultiplication_smul_second`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/SecondModuleStructure.lean, line 455](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/SecondModuleStructure.lean#L455). The attribute's comment: “multiplication\_map\_linear”.

> The canonical tangent multiplication map is linear for the second
> `B`-module structure on the tangent module.

```lean
theorem tangentMultiplication_smul_second (S : RightExactTangentFunctor.{u, v, w})
    (X : AlgebraModulePair.{v} S.A) (b : X.algebra)
    (t : TensorProduct X.algebra X.module (moduleValue S.A S.F X.algebra)) :
    (secondModuleStructure S X).val.toDistribMulAction.toSMul.smul b
        (tangentMultiplication S.A S.F X t) =
      tangentMultiplication S.A S.F X (b • t)
```

**`AdequateFunctor.secondScalarAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean, line 616](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean#L616). The attribute's comment: “second\_scalar\_action”.

> The second scalar operation on a tangent module, induced by multiplication
> on the module variable.

```lean
noncomputable def secondScalarAction (X : AlgebraModulePair.{v} A)
    (x : tangentModule A F X) (b : X.algebra) : tangentModule A F X
```

## Tag 06ZC, an item

[Tag 06ZC](https://stacks.math.columbia.edu/tag/06ZC) in the Stacks Project.

**`AdequateFunctor.tangentMultiplication_smul_second`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/SecondModuleStructure.lean, line 455](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/SecondModuleStructure.lean#L455).

> The canonical tangent multiplication map is linear for the second
> `B`-module structure on the tangent module.

```lean
theorem tangentMultiplication_smul_second (S : RightExactTangentFunctor.{u, v, w})
    (X : AlgebraModulePair.{v} S.A) (b : X.algebra)
    (t : TensorProduct X.algebra X.module (moduleValue S.A S.F X.algebra)) :
    (secondModuleStructure S X).val.toDistribMulAction.toSMul.smul b
        (tangentMultiplication S.A S.F X t) =
      tangentMultiplication S.A S.F X (b • t)
```

## Tag 06ZD, an item

[Tag 06ZD](https://stacks.math.columbia.edu/tag/06ZD) in the Stacks Project.

**`AdequateFunctor.tangentTensorEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/FinitelyPresentedTangent.lean, line 761](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/FinitelyPresentedTangent.lean#L761).

> The canonical tensor-product description of the tangent module of a
> finitely presented module, using the second action on both tangent modules.

```lean
noncomputable def tangentTensorEquiv
    (S : RightExactTangentFunctor.{u, v, w})
    (B : Type v) [CommRing B] [Algebra S.A B]
    (N : Type v) [AddCommGroup N] [Module B N]
    [Module.FinitePresentation B N] :
    let X : AlgebraModulePair.{v} S.A := { algebra := B, module := B }
    let Y : AlgebraModulePair.{v} S.A := { algebra := B, module := N }
    letI : Module B (tangentModule S.A S.F X) :=
      (secondModuleStructure S X).1
    letI : Module B (tangentModule S.A S.F Y) :=
      (secondModuleStructure S Y).1
    { e : TensorProduct B (tangentModule S.A S.F X) N ≃ₗ[B]
        tangentModule S.A S.F Y //
      ∀ (x : tangentModule S.A S.F X) (n : N),
        e (TensorProduct.tmul B x n) =
          (tangentFunctor S.A S.F).map
            ({ base := AlgHom.id S.A B
               linear := (LinearMap.id : B →ₗ[B] B).smulRight n } : X ⟶ Y) x }
```

## Tag 06ZF, a lemma

[Tag 06ZF](https://stacks.math.columbia.edu/tag/06ZF) in the Stacks Project.

**`AdequateFunctor.rightExactTangentFunctor_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/RightExactPermanence.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/RightExactPermanence.lean#L260). The attribute's comment: “extension\_permanence”.

> Property `(*)` is stable under extensions of module-valued functors.

```lean
theorem rightExactTangentFunctor_of_shortExact
    (S : ShortComplex (PresheafOfModules.{w} (algebraStructurePresheaf.{v} A)))
    (hS : S.ShortExact)
    (hF : HasRightExactTangentFunctor A S.X₁)
    (hH : HasRightExactTangentFunctor A S.X₃) :
    HasRightExactTangentFunctor A S.X₂
```

**`AdequateFunctor.hasRightExactTangentFunctor_of_shortExact`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/RightExactPermanence.lean, line 372](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/RightExactPermanence.lean#L372). The attribute's comment: “quotient\_permanence”.

> Property `(*)` passes to the quotient in a short exact sequence of
> module-valued functors.

```lean
public lemma hasRightExactTangentFunctor_of_shortExact
    (A : Type u) [CommRing A]
    (S : ShortComplex (PresheafOfModules.{w} (AdequateFunctor.algebraStructurePresheaf.{v} A)))
    (hS : S.ShortExact)
    (hF : AdequateFunctor.HasRightExactTangentFunctor A S.X₁)
    (hG : AdequateFunctor.HasRightExactTangentFunctor A S.X₂) :
    AdequateFunctor.HasRightExactTangentFunctor A S.X₃
```

**`AdequateFunctor.hasRightExactTangentFunctor_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/RightExactPermanence.lean, line 508](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/RightExactPermanence.lean#L508). The attribute's comment: “pullback\_permanence”.

> Property `(*)` passes to a pullback of a short exact sequence of
> module-valued functors.

```lean
public theorem hasRightExactTangentFunctor_pullback
    {A : Type u} [CommRing A]
    (S : ShortComplex (PresheafOfModules.{w} (algebraStructurePresheaf.{v} A)))
    (hS : S.ShortExact)
    {H' : PresheafOfModules.{w} (algebraStructurePresheaf.{v} A)}
    (f : H' ⟶ S.X₃)
    (hF : HasRightExactTangentFunctor A S.X₁)
    (hH' : HasRightExactTangentFunctor A H') :
    HasRightExactTangentFunctor A (pullback S.g f)
```

**`AdequateFunctor.HasRightExactTangentFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean, line 680](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Adequate/Tangent/TangentFunctor.lean#L680). The attribute's comment: “property”.

> Property `(*)`: over every `A`-algebra, the tangent functor sends a short exact
> sequence of modules to an exact sequence ending in an epimorphism.

```lean
abbrev HasRightExactTangentFunctor : Prop
```

## Tag 06ZG, a lemma

[Tag 06ZG](https://stacks.math.columbia.edu/tag/06ZG) in the Stacks Project.

**`AdequateFunctor.subsingleton_zExt_moduleExtension_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/FinitelyPresentedExtAll.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/FinitelyPresentedExtAll.lean#L152). The attribute's comment: “every degree i > 0; the published proof via Tag 06ZA is replaced by the transfer along phi\_N^* -| psi\_N^* and a dual-number scaling argument”.

> **Stacks Project, Tag 06ZG.** For `A`-modules `M` and `P` with `P` of finite presentation,
> `Ext^i(P̲, M̲) = 0` for every `i > 0` in the category of module-valued functors on the commutative
> `A`-algebras, where `X̲` is `B ↦ B ⊗[A] X`.

```lean
theorem subsingleton_zExt_moduleExtension_of_finitePresentation
    (M P : ModuleCat.{max (u + 1) (v + 1) w} A) [Module.FinitePresentation A P]
    (i : ℤ) (hi : 0 < i) :
    Subsingleton (Abelian.zExt (moduleExtension.{max (u + 1) (v + 1) w, v} A P)
      (moduleExtension.{max (u + 1) (v + 1) w, v} A M) i)
```

**`AdequateFunctor.subsingleton_zExt_moduleExtension_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/FinitelyPresentedExtHigher.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/FinitelyPresentedExtHigher.lean#L130). The attribute's comment: “degree 3, by a double dimension shift to Ext¹ out of a linearly adequate functor, which vanishes by Tag 06V7”.

> **Stacks Project, Tag 06ZG in degree three.** For an `A`-module `P` of finite
> presentation, `Ext³` from the module-valued functor `B ↦ B ⊗[A] P` to `B ↦ B ⊗[A] M` vanishes
> in the category of module-valued functors on the commutative `A`-algebras.

```lean
theorem subsingleton_zExt_moduleExtension_three [Module.FinitePresentation A P] :
    Subsingleton (Abelian.zExt (moduleExtension.{max u v w, v} A P)
      (moduleExtension.{max u v w, v} A M) 3)
```

**`AdequateFunctor.subsingleton_zExt_moduleExtension_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/FinitelyPresentedExtTwo.lean, line 829](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/FinitelyPresentedExtTwo.lean#L829). The attribute's comment: “degree 1, via the universal section over the square-zero extension by the cokernel of the transpose of a presentation”.

> **Stacks Project, Tag 06ZG in degree one.**  For an `A`-module `P` of finite
> presentation, `Ext¹` from the module-valued functor `B ↦ B ⊗[A] P` to `B ↦ B ⊗[A] M` vanishes
> in the category of module-valued functors on the commutative `A`-algebras.

```lean
theorem subsingleton_zExt_moduleExtension_one [Module.FinitePresentation A P] :
    Subsingleton (Abelian.zExt (moduleExtension.{max u v w, v} A P)
      (moduleExtension.{max u v w, v} A M) 1)
```

**`AdequateFunctor.subsingleton_zExt_moduleExtension_two_large`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/FinitelyPresentedExtTwo.lean, line 840](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/FinitelyPresentedExtTwo.lean#L840). The attribute's comment: “degree 2, via Tag 06V0 and projectivity of the free module functors”.

> **Stacks Project, Tag 06ZG in degree two.**  For an `A`-module `P` of finite presentation,
> `Ext²` from the module-valued functor `B ↦ B ⊗[A] P` to `B ↦ B ⊗[A] M` vanishes in the
> category of module-valued functors on the commutative `A`-algebras.

```lean
theorem subsingleton_zExt_moduleExtension_two_large [Module.FinitePresentation A P] :
    Subsingleton (Abelian.zExt (moduleExtension.{max u v w, v} A P)
      (moduleExtension.{max u v w, v} A M) 2)
```

**`AdequateFunctor.subsingleton_zExt_moduleExtension_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/FinitelyPresentedExtTwo.lean, line 870](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/FinitelyPresentedExtTwo.lean#L870). The attribute's comment: “degree 2, via Tag 06V0 and projectivity of the free module functors”.

> **Stacks Project, Tag 06ZG in degree two.**  For an `A`-module `P` of finite presentation,
> `Ext²` from the module-valued functor `B ↦ B ⊗[A] P` to `B ↦ B ⊗[A] M` vanishes in the
> category of module-valued functors on the commutative `A`-algebras.

```lean
theorem subsingleton_zExt_moduleExtension_two [Module.FinitePresentation A P] :
    Subsingleton (Abelian.zExt (moduleExtension.{max u v, v} A P)
      (moduleExtension.{max u v, v} A M) 2)
```

## Tag 06ZH, a lemma

[Tag 06ZH](https://stacks.math.columbia.edu/tag/06ZH) in the Stacks Project.

**`AdequateFunctor.subsingleton_zExt_isLinearlyAdequate_moduleExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/FinitelyPresentedExtAll.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/FinitelyPresentedExtAll.lean#L177). The attribute's comment: “every degree i > 0, by the source's two dimension shifts from Tag 06ZG”.

> **Stacks Project, Tag 06ZH.** Let `A` be a ring, `M` an `A`-module and `L` a linearly adequate
> module-valued functor on the commutative `A`-algebras. Then `Ext^i(L, M̲) = 0` for every `i > 0`,
> where `M̲` is `B ↦ B ⊗[A] M`.

```lean
theorem subsingleton_zExt_isLinearlyAdequate_moduleExtension
    (L : ModuleValuedFunctor.{max (u + 1) (v + 1) w, v} A) (hL : IsLinearlyAdequate (𝟭 _) L)
    (M : ModuleCat.{max (u + 1) (v + 1) w} A) (i : ℤ) (hi : 0 < i) :
    Subsingleton (Abelian.zExt L (moduleExtension.{max (u + 1) (v + 1) w, v} A M) i)
```

**`AdequateFunctor.subsingleton_zExt_of_isLinearlyAdequate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/LinearlyAdequate.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/LinearlyAdequate.lean#L183). The attribute's comment: “The positive-degree vanishing for the functor of a finitely presented module, Tag 06ZG, is a hypothesis. Only its degree-two case is proved in this library, in `AdequateFunctor.subsingleton_zExt_moduleExtension_two`, while this proof needs degrees at least three: both short exact sequences used here are flanked by projective objects, so the degree shift along them is an isomorphism and those degrees of Tag 06ZG carry the content of this tag itself. The source derives Tag 06ZG from Tag 06ZA, which is false as stated and is refuted by `AdequateFunctor.not_forall_hasRightExactTangentFunctor_of_injective`.”.

> Let `A` be a commutative ring, `M` an `A`-module and `L` a linearly adequate module-valued
> functor on the commutative `A`-algebras. Then `Ext^i(L, M̲)` vanishes for `i > 0`, where `M̲`
> is the module-valued functor `B ↦ B ⊗[A] M`.

```lean
public theorem subsingleton_zExt_of_isLinearlyAdequate {A : Type u} [CommRing A]
    (L : ModuleValuedFunctor.{max u v w, v} A) (hL : IsLinearlyAdequate (𝟭 _) L)
    (M : ModuleCat.{max u v w} A)
    (hM : ∀ P : ModuleCat.{max u v w} A, Module.FinitePresentation A P → ∀ j : ℤ, 0 < j →
      Subsingleton (Abelian.zExt (moduleExtension.{max u v w, v} A P)
        (moduleExtension.{max u v w, v} A M) j))
    (i : ℤ) (hi : 0 < i) :
    Subsingleton (Abelian.zExt L (moduleExtension.{max u v w, v} A M) i)
```

## Tag 06ZI, a lemma

[Tag 06ZI](https://stacks.math.columbia.edu/tag/06ZI) in the Stacks Project.

**`AdequateFunctor.isZero_rightDerivedPlus_adequateCoreflection_of_isAdequate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/FinitelyPresentedExtAll.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/FinitelyPresentedExtAll.lean#L188). The attribute's comment: “every degree p > 0 and every adequate F”.

> **Stacks Project, Tag 06ZI.** The higher right derived functors of the coreflection `Q` onto
> the adequate module-valued functors vanish: `R^p Q(F) = 0` for every `p > 0` and every adequate
> functor `F`.

```lean
theorem isZero_rightDerivedPlus_adequateCoreflection_of_isAdequate
    (F : ModuleValuedFunctor.{max (u + 1) (v + 1) w, v} A) (hF : IsAdequate (𝟭 _) F)
    (p : ℤ) (hp : 0 < p) :
    IsZero (((adequateCoreflection.{u, v, w} A).rightDerivedPlus p).obj F)
```

**`AdequateFunctor.isZero_rightDerivedPlus_one_adequateCoreflection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/Vanishing.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/Vanishing.lean#L273). The attribute's comment: “degree 1, from Tag 06V7 and the covering of Tag 06UX”.

> **Stacks Project, Tag 06ZI in degree one.** The first right derived functor of the
> coreflection `Q` onto the adequate module-valued functors vanishes on every adequate functor `F`.
> On an injective resolution `F → I ⁎`, a degree-one cycle of `Q(I ⁎)` restricted along a linearly
> adequate functor `L` is a boundary, because `Ext¹(L, F)` vanishes by Tag 06V7; the linearly
> adequate functors cover every adequate functor by Tag 06UX.

```lean
public theorem isZero_rightDerivedPlus_one_adequateCoreflection
    (F : ModuleValuedFunctor.{max (u + 1) (v + 1) w, v} A) (hF : IsAdequate (𝟭 _) F) :
    IsZero (((adequateCoreflection.{u, v, w} A).rightDerivedPlus 1).obj F)
```

**`AdequateFunctor.isZero_rightDerivedPlus_adequateCoreflection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/Vanishing.lean, line 334](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/Vanishing.lean#L334). The attribute's comment: “the positive-degree vanishing of the extension groups between extensions of modules, one finitely presented, is a hypothesis: that is Tag 06ZG, which is absent from this library.”.

> **Stacks Project, Tag 06ZI.** The higher right derived functors of the coreflection `Q` onto
> the adequate module-valued functors vanish in positive degrees on every adequate functor.

```lean
public theorem isZero_rightDerivedPlus_adequateCoreflection
    (hFP : ∀ M P : ModuleCat.{max (u + 1) (v + 1) w} A, Module.FinitePresentation A P →
      ∀ j : ℤ, 0 < j → Subsingleton (Abelian.zExt
        (moduleExtension.{max (u + 1) (v + 1) w, v} A P)
        (moduleExtension.{max (u + 1) (v + 1) w, v} A M) j))
    (F : ModuleValuedFunctor.{max (u + 1) (v + 1) w, v} A) (hF : IsAdequate (𝟭 _) F)
    (p : ℤ) (hp : 0 < p) :
    IsZero (((adequateCoreflection.{u, v, w} A).rightDerivedPlus p).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 46.4, Tag 06Z5](https://stacks.math.columbia.edu/tag/06Z5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
