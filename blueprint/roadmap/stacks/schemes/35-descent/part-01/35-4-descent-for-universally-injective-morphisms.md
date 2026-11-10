---
declaration: section
origin: cited
lean: Stacks.Descent.IsEqualizerDiagram, CategoryTheory.IsSplitEqualizer, CategoryTheory.Functor.reflectsMonomorphisms_of_preservesFiniteLimits_of_reflectsZeroObjects, CategoryTheory.Functor.reflectsEpimorphisms_of_preservesFiniteColimits_of_reflectsZeroObjects, ModuleCat.extendScalars_isZero_iff_of_faithfullyFlat, ModuleCat.extendScalars_reflectsMonomorphisms_of_faithfullyFlat, ModuleCat.extendScalars_reflectsEpimorphisms_of_faithfullyFlat, ModuleCat.preservesFiniteLimits_extendScalars_of_flat
statement: formalized
proof: formalized
---

# 35.4 Descent for universally injective morphisms

Section 35.4 of the Stacks Project, [Tag 08WE](https://stacks.math.columbia.edu/tag/08WE). 23 tags here are carried by 39 declarations of the repository (all in StacksFrontier) and 10 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08WG, an equation

[Tag 08WG](https://stacks.math.columbia.edu/tag/08WG) in the Stacks Project.

**`Stacks.Descent.IsEqualizerDiagram`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/EqualizerDiagram.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/EqualizerDiagram.lean#L60). The attribute's comment: “the displayed diagram is an equalizer”.

> The diagram `A ⟶ B ⇉ C` consisting of `f : A ⟶ B` and a parallel pair `g₁, g₂ : B ⟶ C`
> *is an equalizer*: the two composites `f ≫ g₁` and `f ≫ g₂` agree, and `f` is universal for
> that property, meaning that every `e : A' ⟶ B` equalizing `g₁` and `g₂` factors as `e = d ≫ f`
> for a unique `d : A' ⟶ A`.

```lean
structure IsEqualizerDiagram (f : A ⟶ B) (g₁ g₂ : B ⟶ C) : Prop
```

## Tag 08WH, a definition

[Tag 08WH](https://stacks.math.columbia.edu/tag/08WH) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.IsSplitEqualizer`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsSplitEqualizer#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch35.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch35.lean#L19) (StacksFrontier): “as a structure carrying `h` and `i`; 'is a split equalizer' is its `Nonempty`”.

## Tag 08WK, a remark

[Tag 08WK](https://stacks.math.columbia.edu/tag/08WK) in the Stacks Project.

**`CategoryTheory.Functor.reflectsMonomorphisms_of_preservesFiniteLimits_of_reflectsZeroObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Exactness.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Exactness.lean#L59). The attribute's comment: “monomorphisms”.

> A left exact functor between abelian categories which reflects zero objects reflects
> monomorphisms.

```lean
theorem reflectsMonomorphisms_of_preservesFiniteLimits_of_reflectsZeroObjects
    (F : A ⥤ B) [PreservesFiniteLimits F]
    (hF : ∀ X, IsZero (F.obj X) → IsZero X) : F.ReflectsMonomorphisms
```

**`CategoryTheory.Functor.reflectsEpimorphisms_of_preservesFiniteColimits_of_reflectsZeroObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Exactness.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Exactness.lean#L68). The attribute's comment: “epimorphisms”.

> A right exact functor between abelian categories which reflects zero objects reflects
> epimorphisms.

```lean
theorem reflectsEpimorphisms_of_preservesFiniteColimits_of_reflectsZeroObjects
    (F : A ⥤ B) [PreservesFiniteColimits F]
    (hF : ∀ X, IsZero (F.obj X) → IsZero X) : F.ReflectsEpimorphisms
```

**`ModuleCat.extendScalars_isZero_iff_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Exactness.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Exactness.lean#L83). The attribute's comment: “faithfully flat extension of scalars detects zero objects”. References: EGA IV (2.2.7), “special case”.

> Extension of scalars along a faithfully flat ring homomorphism detects zero modules.

```lean
theorem extendScalars_isZero_iff_of_faithfullyFlat (f : R →+* S)
    (hf : f.FaithfullyFlat) (M : ModuleCat.{u} R) :
    IsZero ((ModuleCat.extendScalars f).obj M) ↔ IsZero M
```

**`ModuleCat.extendScalars_reflectsMonomorphisms_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Exactness.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Exactness.lean#L95). The attribute's comment: “faithfully flat extension of scalars reflects monomorphisms”. References: SGA 1 IV (2.1), “special case”; SGA 4½ Arcata (1.4.2), “Clause (i), special case”.

> Extension of scalars along a faithfully flat ring homomorphism reflects monomorphisms.

```lean
theorem extendScalars_reflectsMonomorphisms_of_faithfullyFlat (f : R →+* S)
    (hf : f.FaithfullyFlat) :
    (ModuleCat.extendScalars.{u, u, u} f).ReflectsMonomorphisms
```

**`ModuleCat.extendScalars_reflectsEpimorphisms_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Exactness.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Exactness.lean#L105). The attribute's comment: “faithfully flat extension of scalars reflects epimorphisms”. References: SGA 1 IV (2.1), “special case”.

> Extension of scalars along a faithfully flat ring homomorphism reflects epimorphisms.

```lean
theorem extendScalars_reflectsEpimorphisms_of_faithfullyFlat (f : R →+* S)
    (hf : f.FaithfullyFlat) :
    (ModuleCat.extendScalars.{u, u, u} f).ReflectsEpimorphisms
```

Declarations registered for the tag:

- [`ModuleCat.preservesFiniteLimits_extendScalars_of_flat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ModuleCat.preservesFiniteLimits_extendScalars_of_flat#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Exactness.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Exactness.lean#L47) (StacksFrontier): “exactness of extension of scalars”. References: EGA 0 (20.6.21), “partial”.

## Tag 08WL, a definition

[Tag 08WL](https://stacks.math.columbia.edu/tag/08WL) in the Stacks Project.

**`Algebra.UniversallyInjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Defs.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Defs.lean#L45).

> A ring map `R → S` is universally injective as a map of `R`-modules: for every `R`-module
> `Q`, the map `(Algebra.linearMap R S) ⊗ id_Q` is injective.

```lean
def Algebra.UniversallyInjective (R : Type u) [CommRing R] (S : Type u) [CommRing S]
    [Algebra R S] : Prop
```

## Tag 08WM, an example

[Tag 08WM](https://stacks.math.columbia.edu/tag/08WM) in the Stacks Project.

**`UniversallyInjective.of_split`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Defs.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Defs.lean#L51). The attribute's comment: “module maps”.

> A split injection of modules is universally injective.

```lean
theorem UniversallyInjective.of_split
    {R : Type u} [CommRing R]
    {M N : Type v} [AddCommGroup M] [AddCommGroup N] [Module R M] [Module R N]
    (f : M →ₗ[R] N) (g : N →ₗ[R] M) (h : g.comp f = LinearMap.id) :
    UniversallyInjective f
```

**`Algebra.UniversallyInjective.of_split`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Defs.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Defs.lean#L62). The attribute's comment: “ring maps”.

> A split ring map is universally injective.

```lean
theorem Algebra.UniversallyInjective.of_split
    (R S : Type u) [CommRing R] [CommRing S] [Algebra R S]
    (g : S →+* R) (h : g.comp (algebraMap R S) = RingHom.id R) :
    Algebra.UniversallyInjective R S
```

## Tag 08WN, an example

[Tag 08WN](https://stacks.math.columbia.edu/tag/08WN) in the Stacks Project.

**`Algebra.UniversallyInjective.pi_localizationAway`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Localization.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Localization.lean#L107).

> A family of principal localizations covering `Spec R` yields a universally injective
> canonical map from `R` to their product.

```lean
theorem Algebra.UniversallyInjective.pi_localizationAway
    {R : Type u} [CommRing R] {ι : Type u} (f : ι → R)
    (hspan : Ideal.span (Set.range f) = ⊤) :
    Algebra.UniversallyInjective R (∀ i : ι, Localization.Away (f i))
```

## Tag 08WP, a lemma

[Tag 08WP](https://stacks.math.columbia.edu/tag/08WP) in the Stacks Project.

Declarations registered for the tag:

- [`faithfullyFlat_universallyInjective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjective.lean#L485), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Defs.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/Defs.lean#L73) (StacksFrontier).

## Tag 08WQ, a definition

[Tag 08WQ](https://stacks.math.columbia.edu/tag/08WQ) in the Stacks Project.

**`CharacterModule.dualFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/CharacterModule/Duality.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/CharacterModule/Duality.lean#L55).

> The contravariant functor `M ↦ M^∨ = Hom_ℤ(M, ℚ/ℤ)` on modules over a commutative ring,
> acting on a linear map by precomposition (`CharacterModule.dual`).

```lean
noncomputable def dualFunctor (R : Type u) [CommRing R] :
    (ModuleCat.{u} R)ᵒᵖ ⥤ ModuleCat.{u} R
```

## Tag 08WR, a lemma

[Tag 08WR](https://stacks.math.columbia.edu/tag/08WR) in the Stacks Project.

Declarations registered for the tag:

- [`CharacterModule.dual_exact`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/CharacterModule/Duality.lean#L88), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/CharacterModule.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/CharacterModule.lean#L61) (StacksFrontier): “exactness”.
- [`CharacterModule.dual_surjective_iff_injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CharacterModule.dual_surjective_iff_injective#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/CharacterModule.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/CharacterModule.lean#L63) (StacksFrontier): “reflection of injections”.
- [`CharacterModule.dual_injective_iff_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CharacterModule.dual_injective_iff_surjective#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/CharacterModule.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/CharacterModule.lean#L66) (StacksFrontier): “reflection of surjections”.

## Tag 08WS, a remark

[Tag 08WS](https://stacks.math.columbia.edu/tag/08WS) in the Stacks Project.

**`CharacterModule.dual_map_conj_homEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/TensorHomAdjunction.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/TensorHomAdjunction.lean#L74). The attribute's comment: “naturality of the adjunction isomorphism”.

> **Stacks 08WS.** The adjunction isomorphism `C(• ⊗_R •) ≅ Hom_R(•, C(•))` is natural in
> both variables: conjugating `C(f ⊗ g)` by it gives `φ ↦ C(g) ∘ φ ∘ f`.

```lean
theorem dual_map_conj_homEquiv (f : M₁ →ₗ[R] M₁') (g : M₂ →ₗ[R] M₂') :
    homEquiv.symm.toLinearMap ∘ₗ dual (TensorProduct.map f g) ∘ₗ homEquiv.toLinearMap =
      LinearMap.compRight R (dual g) ∘ₗ LinearMap.lcomp R (CharacterModule M₂') f
```

**`CharacterModule.isSplitCoequalizer_dual_rTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/TensorHomAdjunction.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/TensorHomAdjunction.lean#L178). The attribute's comment: “split coequalizers of character modules are preserved by tensoring inside C”.

> **Stacks 08WS**, the corollary of the adjunction. If
> `C(M) ⇉ C(N) → C(P)` is a split coequalizer diagram of `R`-modules, the arrows being the
> character-module duals of `u`, `v : N → M` and `w : P → N`, then so is
> `C(M ⊗_R Q) ⇉ C(N ⊗_R Q) → C(P ⊗_R Q)`, for any `R`-module `Q`.

```lean
noncomputable def isSplitCoequalizer_dual_rTensor (u v : N →ₗ[R] M) (w : P →ₗ[R] N)
    (q : IsSplitCoequalizer (ModuleCat.ofHom (dual u)) (ModuleCat.ofHom (dual v))
      (ModuleCat.ofHom (dual w))) :
    IsSplitCoequalizer (ModuleCat.ofHom (dual (u.rTensor Q)))
      (ModuleCat.ofHom (dual (v.rTensor Q))) (ModuleCat.ofHom (dual (w.rTensor Q)))
```

Declarations registered for the tag:

- [`CharacterModule.homEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CharacterModule.homEquiv#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/TensorHomAdjunction.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/TensorHomAdjunction.lean#L222) (StacksFrontier): “adjunction isomorphism”. References: SGA 5 IIIB (5.2), “5.2.1 with K = B = Z”.
- [`CharacterModule.homEquiv_symm_apply_apply_apply`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CharacterModule.homEquiv_symm_apply_apply_apply#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/TensorHomAdjunction.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/TensorHomAdjunction.lean#L225) (StacksFrontier): “the displayed formula for the isomorphism”.

## Tag 08WU, a lemma

[Tag 08WU](https://stacks.math.columbia.edu/tag/08WU) in the Stacks Project.

**`universallyInjective_iff_dual_splitSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/CharacterModule.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/CharacterModule.lean#L91).

> A module map is universally injective exactly when its character-module dual admits a
> linear section.

```lean
theorem universallyInjective_iff_dual_splitSurjective
    {R : Type u} [CommRing R]
    {M N : Type v} [AddCommGroup M] [AddCommGroup N] [Module R M] [Module R N]
    (f : M →ₗ[R] N) :
    UniversallyInjective f ↔
      ∃ s : CharacterModule M →ₗ[R] CharacterModule N,
        (CharacterModule.dual f).comp s = LinearMap.id
```

## Tag 08WV, a remark

[Tag 08WV](https://stacks.math.columbia.edu/tag/08WV) in the Stacks Project.

**`exists_functorialCharacterModuleSplitting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/CharacterModule.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjective/CharacterModule.lean#L128).

> A universally injective map admits a section after applying the character
> module functor, and the section obtained on `C(P ⊗ -)` by postcomposition is a splitting
> functorial in the module `P`.

```lean
theorem exists_functorialCharacterModuleSplitting
    {R : Type u} [CommRing R]
    {M N : Type v} [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N]
    (f : M →ₗ[R] N) (hf : UniversallyInjective f) :
    ∃ g : CharacterModule M →ₗ[R] CharacterModule N,
      CharacterModule.dual f ∘ₗ g = LinearMap.id ∧
      (∀ (P : Type v) [AddCommGroup P] [Module R P],
        CharacterModule.dual (LinearMap.lTensor P f) ∘ₗ
            functorialCharacterModuleSection g P =
          LinearMap.id) ∧
      ∀ (P Q : Type v) [AddCommGroup P] [Module R P]
        [AddCommGroup Q] [Module R Q] (h : P →ₗ[R] Q),
        functorialCharacterModuleSection g P ∘ₗ
            CharacterModule.dual (LinearMap.rTensor M h) =
          CharacterModule.dual (LinearMap.rTensor N h) ∘ₗ
            functorialCharacterModuleSection g Q
```

## Tag 08WX, an equation

[Tag 08WX](https://stacks.math.columbia.edu/tag/08WX) in the Stacks Project.

**`ModuleCat.DescentData`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/DescentData.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/DescentData.lean#L244). The attribute's comment: “the cocycle condition, as the cocycle field”.

> A descent datum for modules for an `R`-algebra `A`.
>
> The transition is bundled as an `A ⊗[R] A`-linear equivalence, and `cocycle` is the equality
> `φ₁₂ ∘ φ₀₁ = φ₀₂`.

```lean
structure DescentData
```

## Tag 08WY, a definition

[Tag 08WY](https://stacks.math.columbia.edu/tag/08WY) in the Stacks Project.

**`ModuleCat.baseExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/BaseExtension.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/BaseExtension.lean#L236). The attribute's comment: “the functor”.

> **Stacks Project, Tag 08WY.** The base-extension functor from `R`-modules to descent data
> for modules along `R → A`, bundled with its canonical objectwise description.

```lean
def baseExtension : BaseExtension.{u, v, w} R A
```

**`ModuleCat.IsDescentMorphismForModules`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/BaseExtension.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/BaseExtension.lean#L252). The attribute's comment: “descent morphism”.

> **Stacks Project, Tag 08WY.** An algebra map is a descent morphism for modules when its
> base-extension functor is fully faithful.

```lean
abbrev IsDescentMorphismForModules : Prop
```

**`ModuleCat.IsEffectiveDescentMorphismForModules`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/BaseExtension.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/BaseExtension.lean#L260). The attribute's comment: “effective descent morphism”. References: SGA 4 Vbis (2.4.10), “modules over a ring map”; SGA 4 Vbis (2.2.2), “modules over rings”.

> **Stacks Project, Tag 08WY.** An algebra map is an effective descent morphism for modules
> when its base-extension functor is an equivalence of categories.

```lean
abbrev IsEffectiveDescentMorphismForModules : Prop
```

## Tag 08WZ, a lemma

[Tag 08WZ](https://stacks.math.columbia.edu/tag/08WZ) in the Stacks Project.

**`ModuleCat.DescentData.isSplitEqualizer_descentComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/SplitEqualizer.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/SplitEqualizer.lean#L457).

> **Stacks Project, Tag 08WZ.** The canonically associated diagram is a split equalizer of
> `A`-modules.

```lean
theorem isSplitEqualizer_descentComparison
    (D : DescentData.{u, v, w} R A) :
    Nonempty (IsSplitEqualizer
      (ModuleCat.ofHom (transition12AfterUnitHom R A D))
      (ModuleCat.ofHom (rightUnitBaseChangeHom R A D))
      (ModuleCat.ofHom (descentComparisonHom R A D)))
```

**`ModuleCat.DescentData.isSplitEqualizer_inverseTransitionUnitHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/TransitionSplitEqualizer.lean, line 602](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/TransitionSplitEqualizer.lean#L602).

> **Stacks Project, Tag 08WZ.** For a descent datum `(M, θ)` relative to `R → S`, the diagram
> ```
>       θ ∘ (1 ⊗ δ₀¹)                    (θ ⊗ δ₂²) ∘ (1 ⊗ δ₀²)
>   M ---------------> M ⊗_{S, δ₁¹} S₂ ========================> M ⊗_{S, δ₁₂¹} S₃
>                                             1 ⊗ δ₁²
> ```
> is a split equalizer of `S`-modules. Here `M ⊗_{S, δ₁¹} S₂ = N ⊗[R] A` and
> `M ⊗_{S, δ₁₂¹} S₃ = (N ⊗[R] A) ⊗[R] A`, on which `S` acts through the last tensor factor, and
> `θ` is `inverseTransition`, the inverse of the transition isomorphism; see the module docstring
> for the identifications. The auxiliary maps are `1 ⊗ σ₀⁰` and `1 ⊗ σ₀¹`, see
> `inverseTransitionUnitSplitEqualizer`.

```lean
theorem isSplitEqualizer_inverseTransitionUnitHom (D : DescentData.{u, v, w} R A) :
    Nonempty (IsSplitEqualizer (inverseTransition01AfterUnitHom D) (middleUnitInsertionHom D)
      (inverseTransitionUnitHom D))
```

## Tag 08X1, a lemma

[Tag 08X1](https://stacks.math.columbia.edu/tag/08X1) in the Stacks Project.

**`ModuleCat.DescentData.isSplitCoequalizer_characterModule_descentComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/SplitEqualizer.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/SplitEqualizer.lean#L523).

> **Stacks Project, Tag 08X1.** Character duality turns the descent equalizer into a split
> coequalizer.

```lean
theorem isSplitCoequalizer_characterModule_descentComparison
    (D : DescentData.{u, v, w} R A) :
    Nonempty (IsSplitCoequalizer
      (ModuleCat.ofHom (CharacterModule.dual (transition12AfterUnitHom R A D)))
      (ModuleCat.ofHom (CharacterModule.dual (rightUnitBaseChangeHom R A D)))
      (ModuleCat.ofHom (CharacterModule.dual (descentComparisonHom R A D))))
```

## Tag 08X3, a lemma

[Tag 08X3](https://stacks.math.columbia.edu/tag/08X3) in the Stacks Project.

**`Stacks.Descent.isSplitEqualizerTensorInsertOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/TensorPowerSplitEqualizer.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/TensorPowerSplitEqualizer.lean#L83).

> **Stacks Project, Tag 08X3.** The diagram `S₁ --δ¹₁--> S₂ ⇉ S₃` of tensor powers of `A`
> over `R`, whose parallel arrows are `δ²₂` and `δ²₁`, is a split equalizer of commutative
> `R`-algebras. Its splittings are the codegeneracy maps `σ⁰₀` and `σ¹₀`.

```lean
noncomputable def isSplitEqualizerTensorInsertOne :
    IsSplitEqualizer (tensorInsertOne R A 1 2) (tensorInsertOne R A 1 1)
      (tensorInsertOne R A 0 1)
```

## Tag 08X5, a definition

[Tag 08X5](https://stacks.math.columbia.edu/tag/08X5) in the Stacks Project.

**`ModuleCat.pushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/Pushforward.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/Pushforward.lean#L78).

> Pushforward sends a module descent datum to the equalizer of its two pullbacks to
> `A ⊗[R] A`.

```lean
def pushforward : DescentData.{u, v, w} R A ⥤ ModuleCat.{w} R
```

## Tag 08X7, a lemma

[Tag 08X7](https://stacks.math.columbia.edu/tag/08X7) in the Stacks Project.

**`ModuleCat.tensorPushforwardComparison_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/TensorEqualizer/Comparison.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/TensorEqualizer/Comparison.lean#L302). The attribute's comment: “comparison formula”.

> Under tensor symmetry, the first arrow applies the descent transition to
> the unit pullback of the scalar multiple of an invariant section.

```lean
public theorem tensorPushforwardComparison_tmul
    (D : DescentData.{u, v, w} R A)
    (a : A) (m : invariantSubmodule R A D) :
    tensorPushforwardComparison R A D (a ⊗ₜ[R] m) =
      D.transitionRestrictScalars R A
        ((a • (m.1 : restrictModule R A D.module)) ⊗ₜ[R] (1 : A))
```

**`ModuleCat.tensorPushforwardComparison_condition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/TensorEqualizer/Comparison.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/TensorEqualizer/Comparison.lean#L320). The attribute's comment: “fork condition”.

> The base-changed inclusion equalizes the two pullbacks of a descent datum.

```lean
public theorem tensorPushforwardComparison_condition
    (D : DescentData.{u, v, w} R A) :
    ModuleCat.ofHom (tensorPushforwardComparison R A D) ≫
        ModuleCat.ofHom (DescentData.transition12AfterUnitHom R A D) =
      ModuleCat.ofHom (tensorPushforwardComparison R A D) ≫
        ModuleCat.ofHom (DescentData.rightUnitBaseChangeHom R A D)
```

**`ModuleCat.tensorPushforward_isEqualizer`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/TensorEqualizer/Equalizer.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/TensorEqualizer/Equalizer.lean#L536). The attribute's comment: “equalizer”.

> For a universally injective ring map, the displayed diagram of `A`-modules
> is an equalizer. The middle and right objects and both parallel arrows use the
> canonical identifications from the descent datum.

```lean
public noncomputable def tensorPushforward_isEqualizer
    (h : Stacks.UniversalInjectivity.LocalizationCriteria.UniversallyInjective.{u}
      (Algebra.linearMap R A))
    (D : DescentData.{u, v, w} R A) :
    CategoryTheory.Limits.IsLimit
      (CategoryTheory.Limits.Fork.ofι
        (ModuleCat.ofHom (tensorPushforwardComparison R A D))
        (tensorPushforwardComparison_condition R A D))
```

## Tag 08XA, a theorem

[Tag 08XA](https://stacks.math.columbia.edu/tag/08XA) in the Stacks Project.

**`ModuleCat.isDescentMorphismForModules_iff_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/EffectiveDescent.lean, line 689](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/EffectiveDescent.lean#L689). The attribute's comment: “descent morphism”.

> A ring map is a descent morphism for modules exactly when it is universally injective.

```lean
public theorem isDescentMorphismForModules_iff_universallyInjective :
    IsDescentMorphismForModules.{u, u, w} R A ↔
      Algebra.UniversallyInjective R A
```

**`ModuleCat.isEffectiveDescentMorphismForModules_iff_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/EffectiveDescent.lean, line 697](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/EffectiveDescent.lean#L697). The attribute's comment: “effective descent morphism”.

> A ring map is an effective descent morphism for modules exactly when it is universally
> injective.

```lean
public theorem isEffectiveDescentMorphismForModules_iff_universallyInjective :
    IsEffectiveDescentMorphismForModules.{u, u, w} R A ↔
      Algebra.UniversallyInjective R A
```

## Tag 08XC, a lemma

[Tag 08XC](https://stacks.math.columbia.edu/tag/08XC) in the Stacks Project.

Declarations registered for the tag:

- [`Module.Flat.iff_characterModule_injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat.iff_characterModule_injective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch35.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch35.lean#L24) (StacksFrontier): “Mathlib proves the equivalence, under `[Small.{v} R]`”. References: SGA 4 V (1.2), “(ii) ⇒ (i)”.
- [`Module.Flat.iff_characterModule_baer`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat.iff_characterModule_baer#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch35.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch35.lean#L26) (StacksFrontier): “universe-free form, with `Module.Baer.injective`”. References: SGA 4 V (1.2), “(ii) ⇒ (i)”.

## Tag 08XD, a theorem

[Tag 08XD](https://stacks.math.columbia.edu/tag/08XD) in the Stacks Project.

**`Module.finite_iff_baseChange_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/BaseChangeFiniteness.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/BaseChangeFiniteness.lean#L53). The attribute's comment: “finite”. References: EGA IV (2.5.2), “(i), affine case”; EGA IV (2.5.4), “(i), affine case”; SGA 1 VIII (1.11), “finite type”; SGA 4½ Arcata (1.4.2), “(ii) finite type”.

> Finite generation descends and ascends along a universally injective ring map.

```lean
theorem finite_iff_baseChange_of_universallyInjective
    {R : Type u} [CommRing R] {S : Type u} [CommRing S] [Algebra R S]
    (hRS : Algebra.UniversallyInjective R S)
    (M : Type v) [AddCommGroup M] [Module R M] :
    Module.Finite R M ↔ Module.Finite S (TensorProduct R S M)
```

**`Module.finitePresentation_iff_baseChange_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/BaseChangeFiniteness.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/BaseChangeFiniteness.lean#L213). The attribute's comment: “finite_presentation”. References: EGA IV (2.5.2), “(ii), affine case”; EGA IV (2.5.4), “(ii), affine case”; SGA 1 VIII (1.11), “finite presentation”; SGA 4½ Arcata (1.4.2), “(ii) finite presentation”.

> Finite presentation descends and ascends along a universally injective ring map.

```lean
theorem finitePresentation_iff_baseChange_of_universallyInjective
    {R : Type u} [CommRing R] {S : Type u} [CommRing S] [Algebra R S]
    (hRS : Algebra.UniversallyInjective R S)
    (M : Type v) [AddCommGroup M] [Module R M] :
    Module.FinitePresentation R M ↔
    Module.FinitePresentation S (TensorProduct R S M)
```

**`Module.flat_iff_baseChange_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/BaseChangeFlat.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/BaseChangeFlat.lean#L204). The attribute's comment: “flat”.

> Flatness descends and ascends along a universally injective ring map.

```lean
theorem flat_iff_baseChange_of_universallyInjective
    {R : Type u} [CommRing R] {S : Type u} [CommRing S] [Algebra R S]
    (hRS : Algebra.UniversallyInjective R S)
    (M : Type v) [AddCommGroup M] [Module R M] :
    Module.Flat R M ↔ Module.Flat S (TensorProduct R S M)
```

**`Module.faithfullyFlat_iff_baseChange_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/BaseChangeFlat.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/BaseChangeFlat.lean#L238). The attribute's comment: “faithfully_flat”. References: EGA 0 (6.6.3), “more general”.

> Faithful flatness descends and ascends along a universally injective ring map.

```lean
theorem faithfullyFlat_iff_baseChange_of_universallyInjective
    {R : Type u} [CommRing R] {S : Type u} [CommRing S] [Algebra R S]
    (hRS : Algebra.UniversallyInjective R S)
    (M : Type v) [AddCommGroup M] [Module R M] :
    Module.FaithfullyFlat R M ↔ Module.FaithfullyFlat S (TensorProduct R S M)
```

**`Module.finite_projective_iff_baseChange_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/BaseChangeProjective.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/BaseChangeProjective.lean#L40). The attribute's comment: “finite_projective”.

> Finite projectivity descends and ascends along a universally injective ring map.

```lean
theorem finite_projective_iff_baseChange_of_universallyInjective
    {R : Type u} [CommRing R] {S : Type u} [CommRing S] [Algebra R S]
    (hRS : Algebra.UniversallyInjective R S)
    (M : Type v) [AddCommGroup M] [Module R M] :
    (Module.Finite R M ∧ Module.Projective R M) ↔
      (Module.Finite S (TensorProduct R S M) ∧
        Module.Projective S (TensorProduct R S M))
```

## Tag 08XE, a theorem

[Tag 08XE](https://stacks.math.columbia.edu/tag/08XE) in the Stacks Project.

**`Algebra.finiteType_iff_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/AlgebraBaseChangeFiniteness.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/AlgebraBaseChangeFiniteness.lean#L53). The attribute's comment: “finite_type”. References: EGA IV (1.3.1), “special case”.

> **Stacks Project, Tag 08XE (finite type).** Finite type descends along a
> universally injective ring map and is preserved by base change.

```lean
theorem finiteType_iff_tensorProduct
    (R S A : Type u) [CommRing R] [CommRing S] [CommRing A]
    [Algebra R S] [Algebra R A] (h : Algebra.UniversallyInjective R S) :
    Algebra.FiniteType R A ↔ Algebra.FiniteType S (A ⊗[R] S)
```

**`Algebra.finitePresentation_iff_baseChange_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/AlgebraBaseChangeFiniteness.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/AlgebraBaseChangeFiniteness.lean#L146). The attribute's comment: “finite_presentation”.

> Finite presentation of an algebra descends and ascends along a universally injective
> ring map.

```lean
theorem finitePresentation_iff_baseChange_of_universallyInjective
    {R : Type u} [CommRing R] {S : Type u} [CommRing S] [Algebra R S]
    (hRS : Algebra.UniversallyInjective R S)
    (A : Type u) [CommRing A] [Algebra R A] :
    Algebra.FinitePresentation R A ↔
      Algebra.FinitePresentation S (TensorProduct R S A)
```

**`Algebra.formallyUnramified_iff_tensorProduct_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/AlgebraBaseChangeUnramified.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/AlgebraBaseChangeUnramified.lean#L52). The attribute's comment: “formally_unramified”.

> Formal unramifiedness descends and ascends along a universally injective base-ring map.

```lean
theorem formallyUnramified_iff_tensorProduct_of_universallyInjective
    (R S A : Type u) [CommRing R] [CommRing S] [CommRing A]
    [Algebra R S] [Algebra R A] (hRS : Algebra.UniversallyInjective R S) :
    Algebra.FormallyUnramified R A ↔
      Algebra.FormallyUnramified S (TensorProduct R A S)
```

**`Algebra.unramified_iff_baseChange_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/AlgebraBaseChangeUnramified.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/AlgebraBaseChangeUnramified.lean#L72). The attribute's comment: “unramified”.

> Unramifiedness descends and ascends along a universally injective ring map.

```lean
theorem unramified_iff_baseChange_of_universallyInjective
    {R : Type u} [CommRing R] {S : Type u} [CommRing S] [Algebra R S]
    (hRS : Algebra.UniversallyInjective R S)
    (A : Type u) [CommRing A] [Algebra R A] :
    Algebra.Unramified R A ↔ Algebra.Unramified S (A ⊗[R] S)
```

**`Algebra.etale_iff_baseChange_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/AlgebraBaseChangeUnramified.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/AlgebraBaseChangeUnramified.lean#L91). The attribute's comment: “etale”.

> Étaleness descends and ascends along a universally injective ring map.

```lean
theorem etale_iff_baseChange_of_universallyInjective
    {R : Type u} [CommRing R] {S : Type u} [CommRing S] [Algebra R S]
    (hRS : Algebra.UniversallyInjective R S)
    (A : Type u) [CommRing A] [Algebra R A] :
    Algebra.Etale R A ↔ Algebra.Etale S (TensorProduct R S A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.4, Tag 08WE](https://stacks.math.columbia.edu/tag/08WE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
