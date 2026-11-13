---
declaration: section
origin: cited
lean: RingFibreProduct.Situation, RingFibreProduct.Situation.pullbackCone, RingFibreProduct.Situation.pullbackConeIsLimit, RingFibreProduct.primeSpectrum_isPushout, RingFibreProduct.pullback_snd_isIntegral_of_surjective, ModuleGlueing.extensionOfScalarsToPullback, MilnorPatching.compatiblePairsRightAdjoint_counit_isIso, MilnorPatching.compatiblePairs_adjunctionMap_surjective_and_not_injective_in_general
statement: formalized
proof: formalized
---

# 15.6 Fibre products of rings, II

Section 15.6 of the Stacks Project, [Tag 0D2G](https://stacks.math.columbia.edu/tag/0D2G). 10 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08KH, a situation

[Tag 08KH](https://stacks.math.columbia.edu/tag/08KH) in the Stacks Project.

**`RingFibreProduct.Situation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FibreProduct.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FibreProduct.lean#L75).

> The setup for a ring fibre product `B ×_A A'` in which `A' → A` is surjective and
> has the specified ideal `I` as its kernel.

```lean
public structure Situation (toBase : B →+* A) (surjection : A' →+* A)
    (I : Ideal A') : Prop
```

**`RingFibreProduct.Situation.pullbackCone`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FibreProduct.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FibreProduct.lean#L91).

> The canonical cone whose point is `B ×_A A'` and whose legs are the two projections.

```lean
public abbrev pullbackCone {toBase : B →+* A} {surjection : A' →+* A} {I : Ideal A'}
    (_s : Situation toBase surjection I) :
    PullbackCone (CommRingCat.ofHom toBase) (CommRingCat.ofHom surjection)
```

**`RingFibreProduct.Situation.pullbackConeIsLimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FibreProduct.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FibreProduct.lean#L98).

> The canonical square defining `B ×_A A'` is cartesian.

```lean
public def pullbackConeIsLimit {toBase : B →+* A} {surjection : A' →+* A}
    {I : Ideal A'} (s : Situation toBase surjection I) :
    IsLimit s.pullbackCone
```

## Tag 0B7J, a lemma

[Tag 0B7J](https://stacks.math.columbia.edu/tag/0B7J) in the Stacks Project.

**`RingFibreProduct.primeSpectrum_isPushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FibreProduct/Spectrum.lean, line 459](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FibreProduct/Spectrum.lean#L459).

> **Stacks 0B7J.** The prime spectrum of `B ×_A A'`, where `A' → A` is surjective,
> is the pushout of `Spec(B)` and `Spec(A')` over `Spec(A)` as a topological space.

```lean
public theorem primeSpectrum_isPushout
    {A A' B : Type u} [CommRing A] [CommRing A'] [CommRing B]
    {toBase : B →+* A} {surjection : A' →+* A} {I : Ideal A'}
    (s : Situation toBase surjection I) :
    IsPushout
      (TopCat.ofHom ⟨PrimeSpectrum.comap toBase, PrimeSpectrum.continuous_comap toBase⟩)
      (TopCat.ofHom ⟨PrimeSpectrum.comap surjection, PrimeSpectrum.continuous_comap surjection⟩)
      (TopCat.ofHom ⟨PrimeSpectrum.comap s.pullbackCone.fst.hom,
        PrimeSpectrum.continuous_comap s.pullbackCone.fst.hom⟩)
      (TopCat.ofHom ⟨PrimeSpectrum.comap s.pullbackCone.snd.hom,
        PrimeSpectrum.continuous_comap s.pullbackCone.snd.hom⟩)
```

## Tag 0E1S, a lemma

[Tag 0E1S](https://stacks.math.columbia.edu/tag/0E1S) in the Stacks Project.

**`RingFibreProduct.pullback_snd_isIntegral_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FibreProduct.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FibreProduct.lean#L315).

> The second projection `B ×_A A' → A'` is integral when `B → A` is integral and
> `A' → A` is surjective.

```lean
public theorem pullback_snd_isIntegral_of_surjective (toBase : B →+* A) (surjection : A' →+* A)
    (hSurjective : Function.Surjective surjection) (hIntegral : toBase.IsIntegral) :
    (CommRingCat.pullbackCone (CommRingCat.ofHom toBase)
      (CommRingCat.ofHom surjection)).snd.hom.IsIntegral
```

## Tag 08KI, an equation

[Tag 08KI](https://stacks.math.columbia.edu/tag/08KI) in the Stacks Project.

**`ModuleGlueing.extensionOfScalarsToPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/CategoricalPullback.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Localization/Glueing/CategoricalPullback.lean#L96).

> A commutative square of commutative rings induces the
> extension-of-scalars functor
> `Mod B' ⟶ Mod B ×_(Mod A) Mod A'`. Its value at `L'` consists of the two scalar
> extensions of `L'` and their canonical identification after extending scalars to `A`.

```lean
noncomputable def extensionOfScalarsToPullback.{u, uB', uB, uA', uA}
    {B' : Type uB'} {B : Type uB} {A' : Type uA'} {A : Type uA}
    [CommRing B'] [CommRing B] [CommRing A'] [CommRing A]
    (toB : B' →+* B) (toA' : B' →+* A') (BtoA : B →+* A) (A'toA : A' →+* A)
    (comm : BtoA.comp toB = A'toA.comp toA') :
    ModuleCat.{max u uB uA' uA} B' ⥤
      CategoricalPullback (ModuleCat.extendScalars.{uB, uA, max u uB uA' uA} BtoA)
        (ModuleCat.extendScalars.{uA', uA, max u uB uA' uA} A'toA)
```

## Tag 07RU, a lemma

[Tag 07RU](https://stacks.math.columbia.edu/tag/07RU) in the Stacks Project.

**`MilnorPatching.compatiblePairsRightAdjoint_counit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MilnorPatching/Adjunction.lean, line 483](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/MilnorPatching/Adjunction.lean#L483).

> **Stacks Project, Tag 07RU.** For a fibre product `B' = B ×_A A'` with `A' → A`
> surjective, the compatible-pairs construction is right adjoint to extension of scalars from
> `B'`.  The counit is an isomorphism, so scalar extension of the compatible-pairs module to
> `B` and to `A'` canonically recovers the original two modules.

```lean
public theorem compatiblePairsRightAdjoint_counit_isIso
    {A A' B : Type u} [CommRing A] [CommRing A'] [CommRing B]
    (toBase : B →+* A) (surjection : A' →+* A) (I : Ideal A')
    (s : RingFibreProduct.Situation toBase surjection I) :
    let toB : s.fibreProduct →+* B := s.pullbackCone.fst.hom
    let toA' : s.fibreProduct →+* A' := s.pullbackCone.snd.hom
    let comm : toBase.comp toB = surjection.comp toA' := by
      exact congrArg CommRingCat.Hom.hom s.pullbackCone.condition
    ∃ (F : CategoricalPullback (ModuleCat.extendScalars.{u, u, u} toBase)
          (ModuleCat.extendScalars.{u, u, u} surjection) ⥤ ModuleCat.{u} s.fibreProduct)
      (e : ∀ X, F.obj X ≃ CompatiblePairs toBase surjection X)
      (adj : extensionOfScalarsToPullback toB toA' toBase surjection comm ⊣ F),
      (∀ (L : ModuleCat.{u} s.fibreProduct) (X) (h : L ⟶ F.obj X) (l : L),
          (e X (h l)).1.1 =
              ((adj.homEquiv L X).symm h).fst
                ((1 : B) ⊗ₜ[s.fibreProduct,toB] l) ∧
            (e X (h l)).1.2 =
              ((adj.homEquiv L X).symm h).snd
                ((1 : A') ⊗ₜ[s.fibreProduct,toA'] l)) ∧
        IsIso adj.counit
```

## Tag 08IG, a lemma

[Tag 08IG](https://stacks.math.columbia.edu/tag/08IG) in the Stacks Project.

**`MilnorPatching.compatiblePairs_adjunctionMap_surjective_and_not_injective_in_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MilnorPatching/AdjunctionUnit.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/MilnorPatching/AdjunctionUnit.lean#L352).

> **Stacks Project, Tag 08IG.** For a fibre product `B' = B ×_A A'` with `A' → A`
> surjective, the adjunction map from any `B'`-module to the compatible pairs of its scalar
> extensions to `B` and `A'` is surjective. In general this map is not injective.

```lean
public theorem compatiblePairs_adjunctionMap_surjective_and_not_injective_in_general :
    (∀ (A A' B : Type u) [CommRing A] [CommRing A'] [CommRing B]
      (toBase : B →+* A) (surjection : A' →+* A) (I : Ideal A')
      (s : RingFibreProduct.Situation toBase surjection I),
      let toB : s.fibreProduct →+* B := s.pullbackCone.fst.hom
      let toA' : s.fibreProduct →+* A' := s.pullbackCone.snd.hom
      let comm : toBase.comp toB = surjection.comp toA' := by
        exact congrArg CommRingCat.Hom.hom s.pullbackCone.condition
      ∃ (F : CategoricalPullback (ModuleCat.extendScalars.{u, u, u} toBase)
            (ModuleCat.extendScalars.{u, u, u} surjection) ⥤ ModuleCat.{u} s.fibreProduct)
        (e : ∀ X, F.obj X ≃ CompatiblePairs toBase surjection X)
        (adj : extensionOfScalarsToPullback toB toA' toBase surjection comm ⊣ F),
        (∀ (L : ModuleCat.{u} s.fibreProduct) (X) (h : L ⟶ F.obj X) (l : L),
          (e X (h l)).1.1 =
              ((adj.homEquiv L X).symm h).fst
                ((1 : B) ⊗ₜ[s.fibreProduct,toB] l) ∧
            (e X (h l)).1.2 =
              ((adj.homEquiv L X).symm h).snd
                ((1 : A') ⊗ₜ[s.fibreProduct,toA'] l)) ∧
          IsIso adj.counit ∧ ∀ L, Function.Surjective (adj.unit.app L)) ∧
      ∃ (A A' B : Type u) (_ : CommRing A) (_ : CommRing A') (_ : CommRing B)
        (toBase : B →+* A) (surjection : A' →+* A) (I : Ideal A')
        (s : RingFibreProduct.Situation toBase surjection I),
        let toB : s.fibreProduct →+* B := s.pullbackCone.fst.hom
        let toA' : s.fibreProduct →+* A' := s.pullbackCone.snd.hom
        let comm : toBase.comp toB = surjection.comp toA' := by
          exact congrArg CommRingCat.Hom.hom s.pullbackCone.condition
        ∃ (F : CategoricalPullback (ModuleCat.extendScalars.{u, u, u} toBase)
              (ModuleCat.extendScalars.{u, u, u} surjection) ⥤ ModuleCat.{u} s.fibreProduct)
          (e : ∀ X, F.obj X ≃ CompatiblePairs toBase surjection X)
          (adj : extensionOfScalarsToPullback toB toA' toBase surjection comm ⊣ F)
          (L : ModuleCat.{u} s.fibreProduct),
          (∀ (N : ModuleCat.{u} s.fibreProduct) (X) (h : N ⟶ F.obj X) (l : N),
            (e X (h l)).1.1 =
                ((adj.homEquiv N X).symm h).fst
                  ((1 : B) ⊗ₜ[s.fibreProduct,toB] l) ∧
              (e X (h l)).1.2 =
                ((adj.homEquiv N X).symm h).snd
                  ((1 : A') ⊗ₜ[s.fibreProduct,toA'] l)) ∧
            IsIso adj.counit ∧ ¬ Function.Injective (adj.unit.app L)
```

## Tag 08KJ, a lemma

[Tag 08KJ](https://stacks.math.columbia.edu/tag/08KJ) in the Stacks Project.

**`MilnorPatching.fibreProdMap_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MilnorPatching.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/MilnorPatching.lean#L230).

> **Theorem (Stacks Tag `08KJ`, Lemma 15.6.6).**  If both component maps
> `a : N₁ → N₂` and `b : M'₁ → M'₂` of a morphism in the fibre product category are
> surjective, then the induced `B'`-linear map `F(a, b)` is surjective.

```lean
theorem fibreProdMap_surjective
    (φ₁ : StructIso π B N₁ M₁') (φ₂ : StructIso π B N₂ M₂')
    (a : N₁ →ₗ[B] N₂) (b : M₁' →ₗ[A'] M₂') (hab : IsMorphism π B N₁ N₂ M₁' M₂' φ₁ φ₂ a b)
    (ha : Function.Surjective a) (hb : Function.Surjective b) :
    Function.Surjective (Fmor π B N₁ N₂ M₁' M₂' φ₁ φ₂ a b hab)
```

## Tag 0D2H, a lemma

[Tag 0D2H](https://stacks.math.columbia.edu/tag/0D2H) in the Stacks Project.

**`MilnorPatching.finite_rightAdjoint_obj_of_finite_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MilnorPatching/ModuleProperties.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/MilnorPatching/ModuleProperties.lean#L69).

> **Stacks Project, Tag 0D2H.** Let `B' = B ×_A A'`, with `A' → A` surjective.
> For the compatible-pairs right adjoint of Tag 07RU, if both component modules are finite,
> then their compatible-pairs module is finite over `B'`.

```lean
public theorem finite_rightAdjoint_obj_of_finite_components
    {A A' B : Type u} [CommRing A] [CommRing A'] [CommRing B]
    (toBase : B →+* A) (surjection : A' →+* A) (I : Ideal A')
    (s : RingFibreProduct.Situation toBase surjection I) :
    let toB : s.fibreProduct →+* B := s.pullbackCone.fst.hom
    let toA' : s.fibreProduct →+* A' := s.pullbackCone.snd.hom
    let comm : toBase.comp toB = surjection.comp toA' := by
      exact congrArg CommRingCat.Hom.hom s.pullbackCone.condition
    ∀ (F : CategoricalPullback (ModuleCat.extendScalars.{u, u, u} toBase)
          (ModuleCat.extendScalars.{u, u, u} surjection) ⥤ ModuleCat.{u} s.fibreProduct)
        (adj : extensionOfScalarsToPullback toB toA' toBase surjection comm ⊣ F)
        (_ : IsIso adj.counit)
        (X : CategoricalPullback (ModuleCat.extendScalars.{u, u, u} toBase)
          (ModuleCat.extendScalars.{u, u, u} surjection)),
      Module.Finite B X.fst → Module.Finite A' X.snd →
        Module.Finite s.fibreProduct (F.obj X)
```

## Tag 0D2I, a lemma

[Tag 0D2I](https://stacks.math.columbia.edu/tag/0D2I) in the Stacks Project.

**`MilnorPatching.flatModulesEquivalenceOverFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MilnorPatching/ModuleProperties.lean, line 1025](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/MilnorPatching/ModuleProperties.lean#L1025).

> **Stacks Project, Tag 0D2I.** Over a fibre product `B' = B ×_A A'` with `A' → A`
> surjective, compatible pairs of flat modules are flat, every flat `B'`-module is canonically
> reconstructed from its scalar extensions, and these operations induce an equivalence between
> the full subcategory of flat `B'`-modules and the full subcategory of compatible pairs whose
> two components are flat.

```lean
public theorem flatModulesEquivalenceOverFibreProduct
    {A A' B : Type u} [CommRing A] [CommRing A'] [CommRing B]
    (toBase : B →+* A) (surjection : A' →+* A) (I : Ideal A')
    (s : RingFibreProduct.Situation toBase surjection I) :
    let toB : s.fibreProduct →+* B := s.pullbackCone.fst.hom
    let toA' : s.fibreProduct →+* A' := s.pullbackCone.snd.hom
    let comm : toBase.comp toB = surjection.comp toA' := by
      exact congrArg CommRingCat.Hom.hom s.pullbackCone.condition
    let E := extensionOfScalarsToPullback toB toA' toBase surjection comm
    let flatSource : ObjectProperty (ModuleCat.{u} s.fibreProduct) :=
      fun L ↦ Module.Flat s.fibreProduct L
    let flatTarget : ObjectProperty
        (CategoricalPullback (ModuleCat.extendScalars.{u, u, u} toBase)
          (ModuleCat.extendScalars.{u, u, u} surjection)) :=
      fun X ↦ Module.Flat B X.fst ∧ Module.Flat A' X.snd
    ∃ (F : CategoricalPullback (ModuleCat.extendScalars.{u, u, u} toBase)
          (ModuleCat.extendScalars.{u, u, u} surjection) ⥤ ModuleCat.{u} s.fibreProduct)
      (e : ∀ X, F.obj X ≃ CompatiblePairs toBase surjection X)
      (adj : E ⊣ F),
      (∀ (L : ModuleCat.{u} s.fibreProduct) (X) (h : L ⟶ F.obj X) (l : L),
          (e X (h l)).1.1 =
              ((adj.homEquiv L X).symm h).fst
                ((1 : B) ⊗ₜ[s.fibreProduct,toB] l) ∧
            (e X (h l)).1.2 =
              ((adj.homEquiv L X).symm h).snd
                ((1 : A') ⊗ₜ[s.fibreProduct,toA'] l)) ∧
        IsIso adj.counit ∧
        (∀ X, flatTarget X → flatSource (F.obj X)) ∧
        (∀ L, flatSource L → IsIso (adj.unit.app L)) ∧
        ∃ q : flatSource.FullSubcategory ≌ flatTarget.FullSubcategory,
          Nonempty (flatSource.ι ⋙ E ≅ q.functor ⋙ flatTarget.ι) ∧
            Nonempty (flatTarget.ι ⋙ F ≅ q.inverse ⋙ flatSource.ι)
```

## Tag 0D2J, a lemma

[Tag 0D2J](https://stacks.math.columbia.edu/tag/0D2J) in the Stacks Project.

**`MilnorPatching.finiteProjectiveModulesEquivalenceOverFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MilnorPatching/ProjectiveModules.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/MilnorPatching/ProjectiveModules.lean#L274).

> **Stacks Project, Tag 0D2J.** Over a fibre product `B' = B ×_A A'` with `A' → A`
> surjective, extension of scalars gives an equivalence from finite projective `B'`-modules to
> compatible pairs whose `B`- and `A'`-components are finite projective.

```lean
public theorem finiteProjectiveModulesEquivalenceOverFibreProduct
    {A A' B : Type u} [CommRing A] [CommRing A'] [CommRing B]
    (toBase : B →+* A) (surjection : A' →+* A) (I : Ideal A')
    (s : RingFibreProduct.Situation toBase surjection I) :
    let toB : s.fibreProduct →+* B := s.pullbackCone.fst.hom
    let toA' : s.fibreProduct →+* A' := s.pullbackCone.snd.hom
    let comm : toBase.comp toB = surjection.comp toA' := by
      change toBase.comp s.pullbackCone.fst.hom =
        surjection.comp s.pullbackCone.snd.hom
      exact congrArg CommRingCat.Hom.hom s.pullbackCone.condition
    let E := extensionOfScalarsToPullback toB toA' toBase surjection comm
    let finiteProjectiveSource : ObjectProperty (ModuleCat.{u} s.fibreProduct) :=
      fun L ↦ Module.Finite s.fibreProduct L ∧ Module.Projective s.fibreProduct L
    let finiteProjectiveTarget : ObjectProperty
        (CategoricalPullback (ModuleCat.extendScalars.{u, u, u} toBase)
          (ModuleCat.extendScalars.{u, u, u} surjection)) :=
      fun X ↦ (Module.Finite B X.fst ∧ Module.Projective B X.fst) ∧
        (Module.Finite A' X.snd ∧ Module.Projective A' X.snd)
    ∃ q : finiteProjectiveSource.FullSubcategory ≌
        finiteProjectiveTarget.FullSubcategory,
      Nonempty (finiteProjectiveSource.ι ⋙ E ≅ q.functor ⋙ finiteProjectiveTarget.ι)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.6, Tag 0D2G](https://stacks.math.columbia.edu/tag/0D2G)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
