---
declaration: section
origin: cited
lean: Stacks.LocalCohomology.powerTorsionComplexInjectiveResolutionIso, Stacks.LocalCohomology.powerTorsionComplexComparison_comp_counit, Dualizing.localCohomologyRightAdjoint, Dualizing.localCohomologyFunctor, Stacks.LocalCohomology.CechFormula.localCohomologyCechIso, Stacks.LocalCohomology.CechFormula.localCohomologyCechIso_comp_augmentation, Stacks.LocalCohomology.powerTorsionRestrictScalarsData, Stacks.LocalCohomology.localCohomologyRestrictScalarsIso
statement: formalized
proof: formalized
---

# 47.9 Local cohomology

Section 47.9 of the Stacks Project, [Tag 0952](https://stacks.math.columbia.edu/tag/0952). 10 tags here are carried by 22 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0952, the section

[Tag 0952](https://stacks.math.columbia.edu/tag/0952) in the Stacks Project.

**`Stacks.LocalCohomology.powerTorsionComplexInjectiveResolutionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/ModelComparison/InjectiveResolution.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/ModelComparison/InjectiveResolution.lean#L200). The attribute's comment: “RΓ\_I(M) is the I-power-torsion subcomplex of an injective resolution”.

> **The `I`-power-torsion subcomplex of an injective resolution represents `RΓ_I(M)`.** Let `A`
> be a commutative ring, `I ⊆ A` a finitely generated ideal and `M` an `A`-module, and let
> `M → J^•` be a resolution of `M` by injective `A`-modules. Then the termwise `I`-power-torsion
> subcomplex `⋃_n J^•[I^n]` represents derived `I`-power torsion `RΓ_I(M)` in `D(A)`.
>
> This is the computation that [Stacks, Tag 0952] is cited for. No Noetherian hypothesis is
> needed: a bounded-below complex of injectives is K-injective, and a right derived functor is
> computed by a K-injective resolution.
>
> The isomorphism is the composite of: the identification of the two spellings of the termwise
> torsion subcomplex; the passage from the derived category to the homotopy category; the
> comparison of `Γ_I` on the homotopy category with its derived-category avatar; the unit of the
> total right derived functor `RΓ_I` at the K-injective complex `J^•`; the identification of
> `Q(J^•)` with `M⟦0⟧`; and the comparison functor of [Stacks, Tag 0A6N]. Every factor is
> invertible for formal reasons except the unit, which is invertible because `J^•` is
> K-injective.

```lean
def powerTorsionComplexInjectiveResolutionIso :
    DerivedCategory.Q.obj (Dualizing.powerTorsionComplex A I R.cocomplex) ≅
      derivedPowerTorsionObj.{u, u} A I hI M
```

**`Stacks.LocalCohomology.powerTorsionComplexComparison_comp_counit`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/ModelComparison/InjectiveResolution.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/ModelComparison/InjectiveResolution.lean#L248). The attribute's comment: “the representation is compatible with the structure maps onto M”.

> **The comparison carries the structure map of `RΓ_I(M)` to the degreewise inclusion.**
> Composing `Stacks.LocalCohomology.powerTorsionComplexComparison` with the structure map
> `Stacks.LocalCohomology.derivedPowerTorsionObjCounit` of `RΓ_I(M)` gives the degreewise
> inclusion `Γ_I(J^•) ⟶ J^•` of the termwise torsion subcomplex followed by the identification of
> `Q(J^•)` with `M⟦0⟧`.
>
> This is the normalization of the counit of [Stacks, Tag 0A6L] read on the K-injective complex
> `J^•`.

```lean
lemma powerTorsionComplexComparison_comp_counit :
    powerTorsionComplexComparison A I hI M R ≫ derivedPowerTorsionObjCounit.{u, u} A I hI M =
      DerivedCategory.Q.map (powerTorsionComplexι A I R.cocomplex) ≫
        (injectiveResolutionIso A M R).hom
```

Declarations registered for the tag:

- [`Dualizing.localCohomologyRightAdjoint`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/RightAdjoint.lean#L103), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/LocalCohomology/ModelComparison/InjectiveResolution.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/ModelComparison/InjectiveResolution.lean#L339) (StacksFrontier): “the functor (47.9.0.1), right adjoint to the inclusion”.

## Tag 0A6Q, an equation

[Tag 0A6Q](https://stacks.math.columbia.edu/tag/0A6Q) in the Stacks Project.

**`Dualizing.localCohomologyFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/Basic.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/Basic.lean#L42). The attribute's comment: “the functor”.

> **Stacks 0A6Q.** Local cohomology with support in `V(I)`, valued in the full subcategory of
> derived objects with `I`-power-torsion cohomology.

```lean
noncomputable def localCohomologyFunctor
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG) :
    DerivedCategory (ModuleCat.{v} A) ⥤
      PowerTorsionDerivedCategory A I hI
```

## Tag 0A6R, a lemma

[Tag 0A6R](https://stacks.math.columbia.edu/tag/0A6R) in the Stacks Project.

**`Dualizing.localCohomologyRightAdjoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/RightAdjoint.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/RightAdjoint.lean#L103). The attribute's comment: “local\_cohomology\_right\_adjoint”.

> **Stacks 0A6R, local cohomology right adjoint.** The inclusion of the derived category of
> objects with `I`-power-torsion cohomology has a right adjoint. This construction supplies the
> functor denoted `RΓ_Z` for `Z = V(I)`.

```lean
noncomputable def localCohomologyRightAdjoint
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG) :
    Σ F : DerivedCategory (ModuleCat.{v} A) ⥤
        PowerTorsionDerivedCategory A I hI,
      (derivedPowerTorsionProperty A I hI).ι ⊣ F
```

**`Stacks.LocalCohomology.CechFormula.localCohomologyCechIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CechFormula/Basic.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CechFormula/Basic.lean#L330). The attribute's comment: “the Čech formula, functorially in K ∈ D(A); module universe = ring universe”.

> **Stacks 0A6R, the Čech formula.** For a finitely generated ideal `I = (f₁, …, f_r)` of `A`,
> local cohomology `RΓ_Z` with `Z = V(I)` is, as a functor on `D(A)`, the derived tensor product
> with the extended alternating Čech complex of `f`. Normalized by
> `localCohomologyCechIso_comp_augmentation`.

```lean
def localCohomologyCechIso (I : Ideal A) (hI : I.FG) (f : Fin r → A)
    (hf : Ideal.span (Set.range f) = I) :
    Dualizing.localCohomologyFunctor A I hI ⋙
        (Dualizing.derivedPowerTorsionProperty A I hI).ι ≅
      (canonicalDerivedTensorProductFunctor A).obj (cechRegularObject.{u, u} f)
```

**`Stacks.LocalCohomology.CechFormula.localCohomologyCechIso_comp_augmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CechFormula/Basic.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CechFormula/Basic.lean#L343). The attribute's comment: “normalization of the Čech formula against the local-cohomology counit”.

> **Stacks 0A6R, the normalization of the Čech formula.** Composing it with the Čech comparison
> map gives the counit of the adjunction that defines local cohomology, which is what makes the
> isomorphism of `localCohomologyCechIso` the canonical one.

```lean
theorem localCohomologyCechIso_comp_augmentation (I : Ideal A) (hI : I.FG) (f : Fin r → A)
    (hf : Ideal.span (Set.range f) = I) :
    (localCohomologyCechIso A I hI f hf).hom ≫ cechTensorToId A f =
      (Dualizing.localCohomologyAdjunction A I hI).counit
```

## Tag 0BJB, a lemma

[Tag 0BJB](https://stacks.math.columbia.edu/tag/0BJB) in the Stacks Project.

**`Stacks.LocalCohomology.powerTorsionRestrictScalarsData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/RestrictScalars.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/RestrictScalars.lean#L104). The attribute's comment: “the torsion-valued restriction functor”.

> Restriction of scalars on power-torsion derived categories, together with its comparison to
> ordinary derived restriction after inclusion.

```lean
noncomputable def powerTorsionRestrictScalarsData
    {A : Type uA} {B : Type uB} [CommRing A] [CommRing B]
    (f : A →+* B) (I : Ideal A) (hI : I.FG) :
    Σ' F : Dualizing.PowerTorsionDerivedCategory B (I.map f) (hI.map f) ⥤
        Dualizing.PowerTorsionDerivedCategory A I hI,
      F ⋙ (Dualizing.derivedPowerTorsionProperty A I hI).ι ≅
        (Dualizing.derivedPowerTorsionProperty B (I.map f) (hI.map f)).ι ⋙
          (ModuleCat.restrictScalars.{max uA uB v} f).mapDerivedCategory
```

**`Stacks.LocalCohomology.localCohomologyRestrictScalarsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/RestrictScalars.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/RestrictScalars.lean#L184). The attribute's comment: “the local-cohomology isomorphism”.

> **Stacks Project, Tag 0BJB.** Local cohomology commutes with restriction of scalars,
> naturally in the derived `B`-module, as an isomorphism valued in the power-torsion derived
> category.
>
> Both functors are right adjoint to `K ↦ K ⊗ᴸ_A B` on `D_{I^∞-torsion}(A)`: for the left-hand
> side this is the composite of the local-cohomology adjunction over `A` with the
> extension–restriction adjunction, and for the right-hand side it is the composite of the
> local-cohomology adjunction over `B` with the restriction of the extension–restriction
> adjunction to the two power-torsion subcategories.

```lean
noncomputable def localCohomologyRestrictScalarsIso
    (f : A →+* B) (I : Ideal A) (hI : I.FG) :
    (ModuleCat.restrictScalars.{max uA uB v} f).mapDerivedCategory ⋙
        Dualizing.localCohomologyFunctor A I hI ≅
      Dualizing.localCohomologyFunctor B (I.map f) (hI.map f) ⋙
        powerTorsionRestrictScalars.{uA, uB, v} f I hI
```

## Tag 0ALZ, a lemma

[Tag 0ALZ](https://stacks.math.columbia.edu/tag/0ALZ) in the Stacks Project.

**`Stacks.LocalCohomology.localCohomologyBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/BaseChange.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/BaseChange.lean#L212).

> Local cohomology with support in a finitely generated ideal
> commutes naturally with arbitrary derived extension of scalars.

```lean
def localCohomologyBaseChangeIso :
    Dualizing.localCohomologyFunctor A I hI ⋙
          (Dualizing.derivedPowerTorsionProperty A I hI).ι ⋙
          (derivedExtensionScalarsGeneral f).functor ≅
      (derivedExtensionScalarsGeneral f).functor ⋙
          Dualizing.localCohomologyFunctor B (I.map f) (hI.map f) ⋙
          (Dualizing.derivedPowerTorsionProperty B (I.map f) (hI.map f)).ι
```

## Tag 0A6S, a lemma

[Tag 0A6S](https://stacks.math.columbia.edu/tag/0A6S) in the Stacks Project.

Declarations registered for the tag:

- [`Dualizing.localCohomology_isZero_of_isIso_smul`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DerivingTorsion/Vanishing.lean#L93), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/Vanishing.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/Vanishing.lean#L31) (StacksFrontier).

## Tag 0ALY, a lemma

[Tag 0ALY](https://stacks.math.columbia.edu/tag/0ALY) in the Stacks Project.

**`Stacks.LocalCohomology.CechFormula.localCohomology_derivedTensorProduct_right`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CechFormula/TensorCompatibility.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CechFormula/TensorCompatibility.lean#L189). The attribute's comment: “local cohomology on the right”.

> Local cohomology of a derived tensor product is naturally the tensor product
> with local cohomology in the right variable.

```lean
def localCohomology_derivedTensorProduct_right
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG) :
    derivedTensorProductBifunctor A ⋙ localCohomologyEndofunctor A I hI ≅
      (Functor.prod (𝟭 _) (localCohomologyEndofunctor A I hI)) ⋙
        derivedTensorProductBifunctor A
```

**`Stacks.LocalCohomology.CechFormula.localCohomology_derivedTensorProduct_left`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CechFormula/TensorCompatibility.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CechFormula/TensorCompatibility.lean#L199). The attribute's comment: “local cohomology on the left”.

> Tensoring local cohomology in the right variable is naturally isomorphic to
> tensoring it in the left variable.

```lean
def localCohomology_derivedTensorProduct_left
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG) :
    (Functor.prod (𝟭 _) (localCohomologyEndofunctor A I hI)) ⋙
        derivedTensorProductBifunctor A ≅
      (Functor.prod (localCohomologyEndofunctor A I hI) (𝟭 _)) ⋙
        derivedTensorProductBifunctor A
```

**`Stacks.LocalCohomology.CechFormula.localCohomology_derivedTensorProduct_both`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CechFormula/TensorCompatibility.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CechFormula/TensorCompatibility.lean#L212). The attribute's comment: “local cohomology in both factors”.

> Applying local cohomology in both tensor factors is naturally equivalent to
> applying it in just the left factor.

```lean
def localCohomology_derivedTensorProduct_both
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG) :
    (Functor.prod (localCohomologyEndofunctor A I hI) (𝟭 _)) ⋙
        derivedTensorProductBifunctor A ≅
      (Functor.prod (localCohomologyEndofunctor A I hI)
        (localCohomologyEndofunctor A I hI)) ⋙
        derivedTensorProductBifunctor A
```

**`Stacks.LocalCohomology.CechFormula.derivedTensorProduct_mem_powerTorsion_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CechFormula/TensorCompatibility.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CechFormula/TensorCompatibility.lean#L229). The attribute's comment: “torsion in the left factor”.

> Tensoring on the right preserves a complex with `I`-power-torsion
> cohomology.

```lean
theorem derivedTensorProduct_mem_powerTorsion_left
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    (K L : DerivedCategory (ModuleCat.{u} A))
    (hK : Dualizing.derivedPowerTorsionProperty A I hI K) :
    Dualizing.derivedPowerTorsionProperty A I hI
      ((derivedTensorProductBifunctor A).obj (K, L))
```

**`Stacks.LocalCohomology.CechFormula.derivedTensorProduct_mem_powerTorsion_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CechFormula/TensorCompatibility.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CechFormula/TensorCompatibility.lean#L243). The attribute's comment: “torsion in the right factor”.

> Tensoring on the left preserves a complex with `I`-power-torsion
> cohomology.

```lean
theorem derivedTensorProduct_mem_powerTorsion_right
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    (K L : DerivedCategory (ModuleCat.{u} A))
    (hL : Dualizing.derivedPowerTorsionProperty A I hI L) :
    Dualizing.derivedPowerTorsionProperty A I hI
      ((derivedTensorProductBifunctor A).obj (K, L))
```

## Tag 0BJC, a lemma

[Tag 0BJC](https://stacks.math.columbia.edu/tag/0BJC) in the Stacks Project.

**`Dualizing.localCohomology_comp_torsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/Composition.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/Composition.lean#L213). The attribute's comment: “the target of the composition of the local cohomology functors”.

> **[Stacks, Tag 0BJC].** Local cohomology supported on `V(J)` of an object with
> `I`-power-torsion cohomology has `(I + J)`-power-torsion cohomology, because
> `V(I + J) = V(I) ∩ V(J)`.

```lean
theorem localCohomology_comp_torsion (A : Type u) [CommRing A] (I J : Ideal A)
    (hI : I.FG) (hJ : J.FG) (K : PowerTorsionDerivedCategory A I hI) :
    derivedPowerTorsionProperty A (I + J) (Submodule.FG.sup hI hJ)
      (((derivedPowerTorsionProperty A I hI).ι ⋙ localCohomologyFunctor A J hJ ⋙
        (derivedPowerTorsionProperty A J hJ).ι).obj K)
```

**`Dualizing.localCohomologyCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/Composition.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/Composition.lean#L245). The attribute's comment: “the composition of the local cohomology functors”.

> **[Stacks, Tag 0BJC].** `RΓ_Y ∘ RΓ_Z = RΓ_{Y ∩ Z}` for `Z = V(I)` and `Y = V(J)`: iterated
> local cohomology is local cohomology supported on `V(I) ∩ V(J) = V(I + J)`. Both functors are
> right adjoint to the inclusion of the objects with `(I + J)`-power-torsion cohomology into those
> with `I`-power-torsion cohomology, so they agree.

```lean
noncomputable def localCohomologyCompIso (A : Type u) [CommRing A] (I J : Ideal A)
    (hI : I.FG) (hJ : J.FG) :
    localCohomologyFunctor.{u, v} A I hI ⋙ localCohomologyOnPowerTorsion A I J hI hJ ≅
      localCohomologyFunctor A (I + J) (Submodule.FG.sup hI hJ)
```

**`Dualizing.spectralSequencePageTwoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/CompositionSpectralSequence.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/CompositionSpectralSequence.lean#L246). The attribute's comment: “the second page of the spectral sequence”.

> **[Stacks, Tag 0BJC], the second page.** At `(p, q)` the second page of the spectral
> sequence is `H^p_Y(H^q_Z(K))`, naturally in `K`: the `q`-th local cohomology module of `K`
> supported on `Z = V(I)`, placed in degree zero, has its `p`-th local cohomology supported on
> `Y = V(J)` taken.
>
> This is `Stacks.Cohomology.LerayCard.pageTwoNatIsoDerived` for `Φ = RΓ_Y`, precomposed with
> `RΓ_Z`; no Noetherian hypothesis and no comparison of models of local cohomology is involved.

```lean
def spectralSequencePageTwoIso (p q : ℤ) :
    spectralSequence.{u, v} A I J hI hJ ⋙ SpectralSequence.pageFunctor _ _ 2 2 ⋙
        HomologicalComplex.eval _ _ (p, q) ≅
      localCohomologyFunctorPlus.{u, v} A I hI ⋙
        DerivedCategory.Plus.homologyFunctor (ModuleCat.{v} A) q ⋙
          DerivedCategory.Plus.singleFunctor (ModuleCat.{v} A) 0 ⋙
            localCohomologyFunctorPlus.{u, v} A J hJ ⋙
              DerivedCategory.Plus.homologyFunctor (ModuleCat.{v} A) p
```

**`Dualizing.abutsTo_spectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/CompositionSpectralSequence.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/CompositionSpectralSequence.lean#L269). The attribute's comment: “the convergence of the spectral sequence”.

> **[Stacks, Tag 0BJC], the convergence.** For `K` in `D⁺(A)` the spectral sequence has an
> infinity page at every bidegree and the terms `E_∞^{p, n-p}` are the successive quotients of a
> finite decreasing filtration of `H^n_{Y ∩ Z}(K)`.
>
> Boundedness of the spectral object comes from
> `Stacks.Cohomology.LerayTruncation.isBounded_cohomologySpectralObjectFunctor_obj`, whose
> hypothesis is left `t`-exactness of `RΓ_Y` — that is
> `Dualizing.isGE_localCohomologyFunctorPlus_obj`. The abutment the generic theorem produces is
> `H^n(RΓ_Y(RΓ_Z K))`, and `Dualizing.localCohomologyFunctorPlusCompIso` identifies it with
> `H^n_{Y ∩ Z}(K)`.

```lean
theorem abutsTo_spectralSequence (K : DerivedCategory.Plus (ModuleCat.{v} A)) :
    SpectralSequence.AbutsTo ((spectralSequence.{u, v} A I J hI hJ).obj K)
      (fun n : ℤ ↦ (DerivedCategory.Plus.homologyFunctor (ModuleCat.{v} A) n).obj
        ((localCohomologyFunctorPlus.{u, v} A (I + J) (Submodule.FG.sup hI hJ)).obj K))
```

**`Dualizing.localCohomology_comp_spectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomology/CompositionSpectralSequence.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology/CompositionSpectralSequence.lean#L305). The attribute's comment: “all five clauses conjoined; the two isomorphisms of functors appear as `Nonempty`, the isomorphisms themselves being the declarations that carry the tag for those clauses”.

> **Stacks 0BJC, all five clauses.** Let `A` be a ring, let `I, J ⊆ A` be finitely generated
> ideals and set `Z = V(I)`, `Y = V(J)`. Then
>
> 1. `Z ∩ Y = V(I + J)`;
> 2. `RΓ_Y` carries an object with `I`-power-torsion cohomology to one with
>    `(I + J)`-power-torsion cohomology, so that `RΓ_Y ∘ RΓ_Z` is a functor
>    `D(A) → D_{(I + J)^∞-torsion}(A)`;
> 3. `RΓ_Y ∘ RΓ_Z ≅ RΓ_{Y ∩ Z}` as functors `D(A) → D_{(I + J)^∞-torsion}(A)`;
> 4. for `K` in `D⁺(A)` the second page of the spectral sequence of the composition is
>    `E₂^{p, q} = H^p_Y(H^q_Z(K))`, naturally in `K`; and
> 5. that spectral sequence abuts to `H^{p + q}_{Y ∩ Z}(K)`.
>
> Clauses (3) and (4) are isomorphisms of functors, so they appear here as `Nonempty`; the
> isomorphisms themselves are `Dualizing.localCohomologyCompIso` and
> `Dualizing.spectralSequencePageTwoIso`, each of which carries the tag for its own clause, as do
> `PrimeSpectrum.zeroLocus_sup` for (1), `Dualizing.localCohomology_comp_torsion` for (2) and
> `Dualizing.abutsTo_spectralSequence` for (5). Nothing here is Noetherian and no comparison of
> the two models of local cohomology is involved: everything is the coreflection model `RΓ_{V(I)}`
> of [Stacks, Tag 0A6Q].

```lean
theorem localCohomology_comp_spectralSequence :
    PrimeSpectrum.zeroLocus (I : Set A) ∩ PrimeSpectrum.zeroLocus (J : Set A) =
        PrimeSpectrum.zeroLocus ((I + J : Ideal A) : Set A) ∧
      (∀ K : PowerTorsionDerivedCategory.{u, v} A I hI,
        derivedPowerTorsionProperty A (I + J) (Submodule.FG.sup hI hJ)
          (((derivedPowerTorsionProperty A I hI).ι ⋙ localCohomologyFunctor A J hJ ⋙
            (derivedPowerTorsionProperty A J hJ).ι).obj K)) ∧
      Nonempty (localCohomologyFunctor.{u, v} A I hI ⋙
          localCohomologyOnPowerTorsion A I J hI hJ ≅
        localCohomologyFunctor A (I + J) (Submodule.FG.sup hI hJ)) ∧
      (∀ p q : ℤ, Nonempty (spectralSequence.{u, v} A I J hI hJ ⋙
          SpectralSequence.pageFunctor _ _ 2 2 ⋙ HomologicalComplex.eval _ _ (p, q) ≅
        localCohomologyFunctorPlus.{u, v} A I hI ⋙
          DerivedCategory.Plus.homologyFunctor (ModuleCat.{v} A) q ⋙
            DerivedCategory.Plus.singleFunctor (ModuleCat.{v} A) 0 ⋙
              localCohomologyFunctorPlus.{u, v} A J hJ ⋙
                DerivedCategory.Plus.homologyFunctor (ModuleCat.{v} A) p)) ∧
      ∀ K : DerivedCategory.Plus (ModuleCat.{v} A),
        SpectralSequence.AbutsTo ((spectralSequence.{u, v} A I J hI hJ).obj K)
          (fun n : ℤ ↦ (DerivedCategory.Plus.homologyFunctor (ModuleCat.{v} A) n).obj
            ((localCohomologyFunctorPlus.{u, v} A (I + J) (Submodule.FG.sup hI hJ)).obj K))
```

Declarations registered for the tag:

- [`PrimeSpectrum.zeroLocus_sup`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.zeroLocus_sup#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Dualizing/LocalCohomology.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology.lean#L403) (StacksFrontier): “intersection\_of\_zero\_loci”. References: EGA I (1.1.2), “(iii), special case”; EGA I (1.1.5), “special case”.

## Tag 0AM0, a lemma

[Tag 0AM0](https://stacks.math.columbia.edu/tag/0AM0) in the Stacks Project.

**`Dualizing.powerTorsionDerivedEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomology.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomology.lean#L332).

> **Stacks 0AM0.** Flat base change and restriction of scalars are quasi-inverse on
> the derived categories of objects with power-torsion cohomology.

```lean
theorem powerTorsionDerivedEquivalence
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B]
    (I : Ideal A) (hI : I.FG) (hflat : Module.Flat A B)
    (hquot : Function.Bijective
      (Ideal.quotientMap (I.map (algebraMap A B)) (algebraMap A B)
        Ideal.le_comap_map)) :
    ∃ e : PowerTorsionDerivedCategory.{u, max u v w} A I hI ≌
        PowerTorsionDerivedCategory.{v, max u v w} B
          (I.map (algebraMap A B)) (Ideal.FG.map hI (algebraMap A B)),
      Nonempty (e.functor ⋙
          (derivedPowerTorsionProperty B (I.map (algebraMap A B))
            (Ideal.FG.map hI (algebraMap A B))).ι ≅
        (derivedPowerTorsionProperty A I hI).ι ⋙
          (CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, v, w}
            (algebraMap A B)).functor) ∧
      Nonempty (e.inverse ⋙ (derivedPowerTorsionProperty A I hI).ι ≅
        (derivedPowerTorsionProperty B (I.map (algebraMap A B))
          (Ideal.FG.map hI (algebraMap A B))).ι ⋙
          (ModuleCat.restrictScalars.{max u v w} (algebraMap A B)).mapDerivedCategory)
```

## Tag 05EH, a lemma

[Tag 05EH](https://stacks.math.columbia.edu/tag/05EH) in the Stacks Project.

**`Dualizing.PowerTorsionBaseChange.bijective_extBaseChange_of_powerTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Ext.lean, line 913](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Ext.lean#L913). The attribute's comment: “Ext”.

> **Stacks 05EH.** The canonical scalar-extension map on Ext groups from an
> `I`-power-torsion module is bijective in every degree.

```lean
theorem bijective_extBaseChange_of_powerTorsion
    (I : Ideal A) (hI : I.FG) (hflat : Module.Flat A B)
    (hquot : Function.Bijective
      (Ideal.quotientMap (I.map (algebraMap A B)) (algebraMap A B)
        Ideal.le_comap_map))
    (M N : ModuleCat.{max uA (max uR uM)} A) (hM : IsIPowerTorsion A M I) (i : ℕ) :
    let F := ModuleCat.extendScalars.{uR, uA, max uA (max uR uM)} (algebraMap A B)
    letI : F.IsLeftAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA}
        (algebraMap A B)).isLeftAdjoint
    letI : PreservesFiniteLimits F :=
      preservesFiniteLimits_extendScalars_of_flat.{uR, uA, uM} A B hflat
    letI : F.Additive := F.additive_of_preserves_binary_products
    letI := CategoryTheory.HasExt.standard (ModuleCat.{max uA (max uR uM)} A)
    letI := CategoryTheory.HasExt.standard (ModuleCat.{max uA (max uR uM)} B)
    Function.Bijective (F.mapExtAddHom M N i)
```

**`Dualizing.PowerTorsionBaseChange.isIso_derivedHomBaseChangeMate_of_powerTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/PowerTorsionDerivedHom.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/PowerTorsionDerivedHom.lean#L386). The attribute's comment: “derived Hom”.

> **Stacks 05EH.** Derived Hom from a complex with `I`-power-torsion cohomology is
> unchanged under flat base change which is an isomorphism modulo `I`.

```lean
theorem isIso_derivedHomBaseChangeMate_of_powerTorsion
    (A : Type uR) (B : Type uA) [CommRing A] [CommRing B] [Algebra A B]
    (I : Ideal A) (hI : I.FG) (hflat : Module.Flat A B)
    (hquot : Function.Bijective
      (Ideal.quotientMap (I.map (algebraMap A B)) (algebraMap A B)
        Ideal.le_comap_map))
    :
    letI : (ModuleCat.extendScalars.{uR, uA, max uA (max uR uM)} (algebraMap A B)).IsLeftAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA}
        (algebraMap A B)).isLeftAdjoint
    letI : (ModuleCat.restrictScalars.{max uA (max uR uM), uR, uA}
        (algebraMap A B)).IsRightAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA}
        (algebraMap A B)).isRightAdjoint
    letI : (ModuleCat.restrictScalars.{max uA (max uR uM), uR, uA}
        (algebraMap A B)).IsLeftAdjoint :=
      (ModuleCat.restrictCoextendScalarsAdj.{max uR uM, uR, uA}
        (algebraMap A B)).isLeftAdjoint
    ∀ (F : DerivedCategory (ModuleCat.{max uA (max uR uM)} A) ⥤
      DerivedCategory (ModuleCat.{max uA (max uR uM)} B))
    (comparison : DerivedCategory.Q ⋙ F ⟶
      (ModuleCat.extendScalars.{uR, uA, max uA (max uR uM)} (algebraMap A B)).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    [F.IsLeftDerivedFunctor comparison
      (HomologicalComplex.quasiIso (ModuleCat.{max uA (max uR uM)} A) (ComplexShape.up ℤ))]
    (K L : DerivedCategory (ModuleCat.{max uA (max uR uM)} A)),
    Dualizing.derivedPowerTorsionProperty A I hI K →
    IsIso ((Stacks.DerivedHom.ExtensionOfScalars.derivedHomBaseChangeMate.{uR, uA, uM}
      (algebraMap A B) F comparison).app (Opposite.op K, L))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.9, Tag 0952](https://stacks.math.columbia.edu/tag/0952)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
