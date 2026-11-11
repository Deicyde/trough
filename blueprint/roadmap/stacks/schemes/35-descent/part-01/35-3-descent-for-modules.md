---
declaration: section
origin: cited
lean: ModuleCat.DescentData, ModuleCat.DescentData.Hom, ModuleCat.exists_descentCosimplicialModuleFunctor, ModuleCat.descentCosimplicialModuleFunctor, ModuleCat.cechTensorModule, ModuleCat.canonicalDescent_cosimplicialModule, ModuleCat.DescentData.IsEffective, Stacks.Descent.augmentedDescentComplex
statement: formalized
proof: formalized
---

# 35.3 Descent for modules

Section 35.3 of the Stacks Project, [Tag 023F](https://stacks.math.columbia.edu/tag/023F). 12 tags here are carried by 27 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 023G, a definition

[Tag 023G](https://stacks.math.columbia.edu/tag/023G) in the Stacks Project.

**`ModuleCat.DescentData`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/DescentData.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/DescentData.lean#L244). The attribute's comment: “descent data”.

> A descent datum for modules for an `R`-algebra `A`.
>
> The transition is bundled as an `A ⊗[R] A`-linear equivalence, and `cocycle` is the equality
> `φ₁₂ ∘ φ₀₁ = φ₀₂`.

```lean
structure DescentData
```

**`ModuleCat.DescentData.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/DescentData.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/DescentData.lean#L271). The attribute's comment: “morphisms”.

> A morphism of module descent data is an `A`-linear map commuting with the transition
> isomorphisms.

```lean
structure Hom (D E : DescentData.{u, v, w} R A)
```

## Tag 023H, a lemma

[Tag 023H](https://stacks.math.columbia.edu/tag/023H) in the Stacks Project.

**`ModuleCat.exists_descentCosimplicialModuleFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/CechCosimplicialModule.lean, line 1103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/CechCosimplicialModule.lean#L1103).

> **Stacks Lemma 023H.** To a descent datum `(N, φ)` one can associate a
> cosimplicial module over the Čech algebra `(A / R)_•` by the rules
> `N_n = N_{n, n}` and `N_•(β) = φᵐ_{β(n), m} ∘ N_{β, n}`, functorially in the
> descent datum.

```lean
public theorem exists_descentCosimplicialModuleFunctor :
    ∃ F : DescentData.{u, v, w} R A ⥤ CechModule.{u, v, w} R A,
      IsDescentCosimplicialModuleFunctor R A F
```

**`ModuleCat.descentCosimplicialModuleFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/CechCosimplicialModule.lean, line 1120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/CechCosimplicialModule.lean#L1120).

> The functor which associates to a descent datum `(N, φ)` its cosimplicial
> module over the Čech algebra `(A / R)_•`.  It is characterised by
> `descentCosimplicialModuleFunctor_obj` and
> `descentCosimplicialModuleFunctor_map`.

```lean
public noncomputable def descentCosimplicialModuleFunctor :
    DescentData.{u, v, w} R A ⥤ CechModule.{u, v, w} R A
```

## Tag 023I, a lemma

[Tag 023I](https://stacks.math.columbia.edu/tag/023I) in the Stacks Project.

**`ModuleCat.cechTensorModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/CanonicalCechTensorModule.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/CanonicalCechTensorModule.lean#L246). The attribute's comment: “tensor cosimplicial module”.

> The Čech cosimplicial algebra tensored with `M`, together with its
> degreewise and cosimplicial-map specification.

```lean
public noncomputable def cechTensorModule (M : ModuleCat.{w} R) :
    {T : CechModule.{u, v, w} R A // IsCechTensorModule R A M T}
```

**`ModuleCat.canonicalDescent_cosimplicialModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/CanonicalCechTensorModule.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/CanonicalCechTensorModule.lean#L560). The attribute's comment: “canonical isomorphism”.

> The cosimplicial module associated to a canonical descent datum is
> isomorphic to the Čech cosimplicial algebra tensored with its base module.

```lean
public theorem canonicalDescent_cosimplicialModule
    (M : ModuleCat.{w} R)
    (D : DescentData.{u, v, w} R A)
    (e : (A ⊗[R] M) ≃ₗ[A] D.module)
    (he : ∀ (a b : A) (m : M),
      D.transition ((e (a ⊗ₜ[R] m)) ⊗ₜ[R] b) =
        a ⊗ₜ[R] (show restrictModule R A D.module from
          e (b ⊗ₜ[R] m))) :
    Nonempty (((descentCosimplicialModuleFunctor R A).obj D) ≅
      (cechTensorModule R A M).1)
```

## Tag 023J, a definition

[Tag 023J](https://stacks.math.columbia.edu/tag/023J) in the Stacks Project.

**`ModuleCat.DescentData.IsEffective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/DescentData.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/DescentData.lean#L310).

> A module descent datum is effective if it is isomorphic to the canonical descent datum
> obtained by extending scalars from an `R`-module.

```lean
abbrev DescentData.IsEffective (R : Type u) (A : Type v) [CommRing R] [CommRing A]
    [Algebra R A] (D : DescentData.{u, v, w} R A) : Prop
```

## Tag 023K, an equation

[Tag 023K](https://stacks.math.columbia.edu/tag/023K) in the Stacks Project.

**`Stacks.Descent.augmentedDescentComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/AugmentedDescentComplex.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/AugmentedDescentComplex.lean#L368). The attribute's comment: “the augmented complex 0 → M → A ⊗ M → A ⊗ A ⊗ M → ⋯”.

> **Equation 023K: the augmented descent complex** `0 → M → A ⊗[R] M → A ⊗[R] A ⊗[R] M → ⋯`
> of the ring map `R → A` with coefficients in `M`. It is the alternating coface map complex of
> `(A/R)• ⊗[R] M`, augmented by `M` along `m ↦ 1 ⊗ₜ m`.

```lean
noncomputable def augmentedDescentComplex : CochainComplex (ModuleCat.{max u v} R) ℕ
```

**`Stacks.Descent.augmentedDescentComplexXIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/AugmentedDescentComplex.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/AugmentedDescentComplex.lean#L387). The attribute's comment: “its degree-(n+1) term is A^\{⊗(n+1)} ⊗\_R M”.

> **The degree-`(n + 1)` term of the augmented descent complex is `A^{⊗(n + 1)} ⊗[R] M`.**

```lean
noncomputable def augmentedDescentComplexXIso (n : ℕ) :
    ModuleCat.of R ((tensorPowerAlg R A n : Type u) ⊗[R] M) ≅
      (augmentedDescentComplex R A M).X (n + 1)
```

## Tag 023L, a lemma

[Tag 023L](https://stacks.math.columbia.edu/tag/023L) in the Stacks Project.

**`AlgebraicTopology.amitsurExtendedCochainComplex_acyclic_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/Amitsur.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/Amitsur.lean#L151).

> **Stacks Lemma 023L.** If `R → A` admits a section, then the extended Amitsur
> cochain complex with coefficients in any `R`-module `M` is exact.

```lean
theorem amitsurExtendedCochainComplex_acyclic_of_section
    (h : Nonempty (A →ₐ[R] R)) :
    (amitsurExtendedCochainComplex R A M).Acyclic
```

## Tag 023M, a lemma

[Tag 023M](https://stacks.math.columbia.edu/tag/023M) in the Stacks Project.

**`Stacks.Descent.amitsurExtendedCochainComplex_acyclic_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/AmitsurAcyclic.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/AmitsurAcyclic.lean#L435). References: SGA 1 VIII (1.7), “affine case”.

> **Stacks Lemma 023M.** For a faithfully flat algebra `A` over a commutative ring `R` and an
> arbitrary `R`-module `M`, the extended Amitsur cochain complex
> `M → A ⊗[R] M → (A ⊗[R] A) ⊗[R] M → ⋯`
> is exact in every degree.

```lean
theorem amitsurExtendedCochainComplex_acyclic_of_faithfullyFlat [Module.FaithfullyFlat R A] :
    (amitsurExtendedCochainComplex R A M).Acyclic
```

**`AlgebraicTopology.amitsurExtendedCochainComplex_acyclic_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/ModuleEquivalence/FaithfullyFlatAmitsur.lean, line 1259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/ModuleEquivalence/FaithfullyFlatAmitsur.lean#L1259). References: SGA 1 VIII (1.7), “affine case”.

> **Stacks Lemma 023M**, and **Stacks Lemma 03OA**.  The extended Amitsur cochain complex of a
> faithfully flat algebra is exact for every module of coefficients.  Exactness of the extended
> complex `M → A ⊗[R] M → A ⊗[R] A ⊗[R] M → ⋯` says both that the unaugmented complex is exact in
> positive degrees and that its degree-zero cohomology is `M`, which is the form 03OA states.

```lean
theorem amitsurExtendedCochainComplex_acyclic_of_faithfullyFlat
    (R : Type u) (A : Type v) (M : Type w) [CommRing R] [CommRing A] [Algebra R A]
    [AddCommGroup M] [Module R M] [Module.FaithfullyFlat R A] :
    (amitsurExtendedCochainComplex R A M).Acyclic
```

**`ModuleCat.baseExtensionUnitEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/EffectiveDescent.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/EffectiveDescent.lean#L364). The attribute's comment: “degrees −1 and 0”. References: SGA 1 VIII (1.7), “affine case”.

> **Stacks Project, Tag 023M in degrees `−1` and `0`.** For a universally injective ring map
> the unit `m ↦ 1 ⊗ m` of the base-extension adjunction is an isomorphism of `M` onto the
> invariants of the base-extended descent datum.
>
> Exactness of the extended cochain complex `0 → M → A ⊗[R] M → A ⊗[R] A ⊗[R] M → ⋯` at `M` is
> injectivity of the unit, and exactness at `A ⊗[R] M` says that the kernel of the next
> differential — which is `ModuleCat.invariantSubmodule R A` of the canonical descent datum on
> `A ⊗[R] M` — is the image of the unit. Together they are bijectivity of the unit onto the
> invariants. The source assumes `R → A` faithfully flat; faithful flatness is used only through
> universal injectivity (Tag 08WL), which is the hypothesis here.

```lean
noncomputable def baseExtensionUnitEquiv
    (h : Algebra.UniversallyInjective R A) (M : ModuleCat.{max u w} R) :
    M ≃ₗ[R] invariantSubmodule R A
      ((baseExtension.{u, u, w} R A).functor.obj M)
```

## Tag 039W, a lemma

[Tag 039W](https://stacks.math.columbia.edu/tag/039W) in the Stacks Project.

**`ModuleCat.DescentData.isEffective_iff_canonicalMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/EffectiveCriterion.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/EffectiveCriterion.lean#L560).

> A module descent datum is effective if and only if its canonical map from the base change
> of its zeroth cohomology is an isomorphism.

```lean
public theorem isEffective_iff_canonicalMap_bijective
    [Module.FaithfullyFlat R A] :
    IsEffective R A D ↔
      Function.Bijective (canonicalMap R A D)
```

## Tag 039X, a lemma

[Tag 039X](https://stacks.math.columbia.edu/tag/039X) in the Stacks Project.

**`ModuleCat.all_isEffective_of_faithfullyFlat_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/BaseChangeEffective.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/BaseChangeEffective.lean#L49).

> **Stacks Project, Tag 039X.** Let `R → A` be a faithfully flat ring map and let `R → R'` be
> faithfully flat, and set `A' = R' ⊗[R] A`. If all descent data for `R' → A'` are effective,
> then so are all descent data for `R → A`.

```lean
public theorem all_isEffective_of_faithfullyFlat_baseChange
    (R A R' : Type u) [CommRing R] [CommRing A] [CommRing R']
    [Algebra R A] [Algebra R R']
    (hA : (algebraMap R A).FaithfullyFlat)
    (_hR' : (algebraMap R R').FaithfullyFlat)
    (_h : ∀ D : DescentData.{u, u, w} R' (R' ⊗[R] A), D.IsEffective R' (R' ⊗[R] A)) :
    ∀ D : DescentData.{u, u, x} R A, D.IsEffective R A
```

## Tag 023N, a proposition

[Tag 023N](https://stacks.math.columbia.edu/tag/023N) in the Stacks Project.

**`ModuleCat.isEffectiveDescentMorphismForModules_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/FaithfullyFlatEffective.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/FaithfullyFlatEffective.lean#L95). The attribute's comment: “(2)”. References: SGA 1 VIII (1.6), “effectivity”; SGA 1 VIII (1.1), “affine case”; SGA 4½ Arcata (1.4.5), “affine case”; SGA 4½ Arcata (1.4), “module equivalence”.

> **Stacks 023N, part (2).** For a faithfully flat ring map `R → A`, base extension
> `M ↦ (A ⊗[R] M, can)` is an equivalence from `R`-modules onto the category of descent data for
> modules along `R → A`.

```lean
theorem isEffectiveDescentMorphismForModules_of_faithfullyFlat :
    IsEffectiveDescentMorphismForModules.{u, u, w} R A
```

**`ModuleCat.baseExtension_essSurj_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/FaithfullyFlatEffective.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/FaithfullyFlatEffective.lean#L106). The attribute's comment: “(1)”. References: SGA 1 VIII (1.6), “effectivity”; SGA 1 VIII (1.1), “affine case, effectivity”; SGA 4½ Arcata (1.4.5), “ess. surj. (affine)”.

> **Stacks 023N, part (1).** Every descent datum on modules along a faithfully flat ring map
> `R → A` is effective, that is, lies in the essential image of base extension.

```lean
theorem baseExtension_essSurj_of_faithfullyFlat :
    (baseExtension.{u, u, w} R A).functor.EssSurj
```

**`ModuleCat.DescentData.isEffective_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/FaithfullyFlatEffectiveDescent.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/FaithfullyFlatEffectiveDescent.lean#L84). The attribute's comment: “effectivity of descent data”. References: SGA 1 VIII (1.1), “affine case”; SGA 1 VIII (1.6), “effectivity”; SGA 4½ Arcata (1.4.5), “ess. surj. (affine)”; SGA 4½ Arcata (1.4), “module case”.

> **Stacks 023N, part (1).** Every descent datum for modules along a faithfully flat ring map
> `R → A` is effective: it is isomorphic, as a descent datum, to the canonical datum on the
> extension of scalars of an `R`-module.

```lean
public theorem DescentData.isEffective_of_faithfullyFlat
    (D : DescentData.{u, u, max u w} R A) : D.IsEffective R A
```

**`Stacks.Descent.faithfullyFlatInvariantsEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/InvariantsInverseFunctor.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/InvariantsInverseFunctor.lean#L283). The attribute's comment: “(3)”. References: SGA 1 VIII (1.6), “more general”.

> **Stacks 023N, part (3).** For a faithfully flat ring map `R → A` the functor
> `M ↦ (A ⊗[R] M, can)` from `R`-modules to descent data for modules along `R → A` is an
> equivalence whose inverse functor is `(N, φ) ↦ H⁰(s(N_•))`, the kernel of the descent complex.
> Only part (3) is registered here; part (2), that the functor is an equivalence, is
> `ModuleCat.isEffectiveDescentMorphismForModules_of_faithfullyFlat`.

```lean
def faithfullyFlatInvariantsEquivalence [Module.FaithfullyFlat R A] :
    ModuleCat.{max u w} R ≌ DescentData.{u, u, max u w} R A
```

**`Stacks.Descent.faithfullyFlatInvariantsEquivalence_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/InvariantsInverseFunctor.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Modules/InvariantsInverseFunctor.lean#L295). The attribute's comment: “(3)”.

> **Stacks 023N, part (3).** The inverse functor of the equivalence of Stacks 023N is
> `ModuleCat.pushforward`, that is `(N, φ) ↦ H⁰(s(N_•))`.

```lean
theorem faithfullyFlatInvariantsEquivalence_inverse [Module.FaithfullyFlat R A] :
    (faithfullyFlatInvariantsEquivalence.{u, w} R A).inverse = pushforward R A
```

## Tag 023O, a remark

[Tag 023O](https://stacks.math.columbia.edu/tag/023O) in the Stacks Project.

**`PrimeSpectrum.faithfullyFlat_standardCoverAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/StandardCoverAlgebra.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/StandardCoverAlgebra.lean#L230). The attribute's comment: “faithfully flat product”.

> The product of the principal localizations of a standard cover is faithfully flat.

```lean
public theorem faithfullyFlat_standardCoverAlgebra
    (hf : PrimeSpectrum.IsStandardOpenCoverOfSpectrum f) :
    Module.FaithfullyFlat R (∀ i : Fin m, Localization.Away (f i))
```

**`PrimeSpectrum.standardCoverCechDegreeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/StandardCoverAlgebra.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/StandardCoverAlgebra.lean#L332). The attribute's comment: “degree-wise Čech algebra”.

> In degree `d`, the Čech algebra of a standard cover is the product of the
> localizations at all `(d + 1)`-fold products of its covering elements.

```lean
public noncomputable def standardCoverCechDegreeEquiv (d : ℕ) :
    ((Arrow.mk (CommAlgCat.ofHom
      (Algebra.ofId R (∀ i : Fin m, Localization.Away (f i))))).cechConerve).obj
        (SimplexCategory.mk d) ≃ₐ[R]
      (∀ i : Fin (d + 1) → Fin m, Localization.Away (∏ j, f (i j)))
```

Declarations registered for the tag:

- [`Stacks.Cohomology.Cech.isZero_cechCohomology_of_isStandardOpenCover`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Cech/StandardCoverVanishing.lean#L424), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/StandardCoverAlgebra.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/StandardCoverAlgebra.lean#L341) (StacksFrontier): “Čech cohomology vanishing”.

## Tag 039Y, a remark

[Tag 039Y](https://stacks.math.columbia.edu/tag/039Y) in the Stacks Project.

**`ModuleCat.descentDataEquivCartesianCechModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/CartesianCechEquivalence.lean, line 1274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/CartesianCechEquivalence.lean#L1274). The attribute's comment: “(2): descent data for `A / R` correspond to cartesian `(A / R)_•`-modules, through the cosimplicial module of a descent datum of Stacks 023H”.

> Let `A` be an `R`-algebra.  Descent data for `A / R` correspond to cartesian
> `(A / R)_•`-modules: the functor `(N, φ) ↦ N_•`, sending a descent datum to its cosimplicial
> module over the Čech algebra `(A / R)_•` (`N_n = N_{n, n}`, `N_•(β) = φᵐ_{β(n), m} ∘ N_{β, n}`),
> is an equivalence of categories between descent data and cartesian `(A / R)_•`-modules.  Its
> inverse sends a cartesian module `M` to `M_0` with the transition `M_0 ⊗_R A ≅ M_1 ≅ A ⊗_R M_0`
> read off from the cartesian isomorphisms along the two cofaces `⦋0⦌ ⟶ ⦋1⦌`
> (`ModuleCat.cartesianDescentDataFunctor`).  No flatness is assumed.

```lean
noncomputable def descentDataEquivCartesianCechModule :
    DescentData.{u, u, max u w} R A ≌ CartesianCechModule.{u, u, max u w} R A
```

**`CategoryTheory.Arrow.cechConerve_homotopyEquivalent_const_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/CechConerve.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/CechConerve.lean#L118). The attribute's comment: “split\_cech\_homotopy”.

> A split Čech conerve is homotopy equivalent to the constant cosimplicial object on the base.
> For commutative `R`-algebras this is the split Čech algebra `(A/R)•` and the constant algebra
> `R`.

```lean
theorem cechConerve_homotopyEquivalent_const_of_section
    {C : Type u} [Category.{v} C] (f : Arrow C)
    [∀ n : ℕ, HasWidePushout f.left (fun _ : Fin (n + 1) => f.right) fun _ => f.hom]
    (h : ∃ s : f.right ⟶ f.left, f.hom ≫ s = 𝟙 f.left) :
    ∃ a : f.cechConerve.op ⟶ ((CosimplicialObject.const C).obj f.left).op,
      SimplicialObject.homotopyEquivalences Cᵒᵖ a
```

**`CategoryTheory.CosimplicialModule.Cartesian`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/Cosimplicial.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/Cosimplicial.lean#L74). The attribute's comment: “cartesian\_module”.

> A cosimplicial module is cartesian when every cosimplicial transition map
> induces an isomorphism after extension of scalars.

```lean
abbrev Cartesian (M : CosimplicialModule A) : Prop
```

**`CategoryTheory.CosimplicialModule.isEquivalence_cartesianBaseChange_of_homotopyEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/CosimplicialCartesian.lean, line 651](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Module/CosimplicialCartesian.lean#L651). The attribute's comment: “(4): base change along a homotopy equivalence of cosimplicial algebras is an equivalence of the categories of cartesian modules”.

> **Stacks 039Y (4).**  If `α : A_• ⟶ B_•` is a homotopy equivalence of cosimplicial
> `R`-algebras, then the functor `M_• ↦ M_• ⊗_{A_•} B_•` is an equivalence of categories between
> the cartesian `A_•`-modules and the cartesian `B_•`-modules.
>
> A homotopy equivalence is taken in the sense of Simplicial, Definition 019N, through the opposite
> category (cosimplicial homotopies being simplicial homotopies of the opposite objects,
> Simplicial, Lemma 019X), exactly as in Stacks 039Y (3) here
> (`CategoryTheory.Arrow.cechConerve_homotopyEquivalent_const_of_section`).  The proof is the
> source's "triviality": base change along homotopic morphisms gives isomorphic functors
> (`CategoryTheory.CosimplicialModule.nonempty_iso_cartesianBaseChange_of_homotopic`), so a homotopy
> inverse `β` makes base change along `α ≫ β` and along `β ≫ α` isomorphic to the identities, and
> base change is functorial (`CategoryTheory.CosimplicialModule.cartesianBaseChangeCompIso`).

```lean
theorem isEquivalence_cartesianBaseChange_of_homotopyEquivalence (α : A ⟶ B)
    (hα : SimplicialObject.homotopyEquivalences (CommAlgCat.{v, u} R)ᵒᵖ (NatTrans.op α)) :
    (cartesianBaseChange.{u, v, w} α).IsEquivalence
```

**`ModuleCat.all_isEffective_of_faithfullyFlat_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/BaseChangeEffective.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/BaseChangeEffective.lean#L49). The attribute's comment: “(1): descent data for `A / R` are effective once those for `(R' ⊗ A) / R'` are”.

> **Stacks Project, Tag 039X.** Let `R → A` be a faithfully flat ring map and let `R → R'` be
> faithfully flat, and set `A' = R' ⊗[R] A`. If all descent data for `R' → A'` are effective,
> then so are all descent data for `R → A`.

```lean
public theorem all_isEffective_of_faithfullyFlat_baseChange
    (R A R' : Type u) [CommRing R] [CommRing A] [CommRing R']
    [Algebra R A] [Algebra R R']
    (hA : (algebraMap R A).FaithfullyFlat)
    (_hR' : (algebraMap R R').FaithfullyFlat)
    (_h : ∀ D : DescentData.{u, u, w} R' (R' ⊗[R] A), D.IsEffective R' (R' ⊗[R] A)) :
    ∀ D : DescentData.{u, u, x} R A, D.IsEffective R A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.3, Tag 023F](https://stacks.math.columbia.edu/tag/023F)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
