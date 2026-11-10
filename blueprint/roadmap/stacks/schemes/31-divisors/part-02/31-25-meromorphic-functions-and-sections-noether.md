---
declaration: section
origin: cited
lean: AlgebraicGeometry.pow_mul_eq_zero_of_res_basicOpen_eq_zero, AlgebraicGeometry.pow_mul_eq_zero_of_restrict_basicOpen_eq_zero, AlgebraicGeometry.stalk_totalQuotientSheaf_isFractionRing_of_isLocallyNoetherian, AlgebraicGeometry.isLocalization_totalQuotientSheaf_obj_of_isLocallyNoetherian, AlgebraicGeometry.isLocalization_totalQuotientPresheaf_obj_of_isAffineOpen, AlgebraicGeometry.regularSectionGerms_eq_nonZeroDivisors_of_isLocallyNoetherian, AlgebraicGeometry.stalk_totalQuotientPresheaf_isFractionRing_of_isLocallyNoetherian, Stacks.AlgebraicGeometry.GenericPointCoproduct.meromorphicFunctions_iso_coproduct_of_noEmbeddedPoints
statement: formalized
proof: formalized
---

# 31.25 Meromorphic functions and sections; Noetherian case

Section 31.25 of the Stacks Project, [Tag 0EMG](https://stacks.math.columbia.edu/tag/0EMG). 5 tags here are carried by 34 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08I7, a lemma

[Tag 08I7](https://stacks.math.columbia.edu/tag/08I7) in the Stacks Project.

**`AlgebraicGeometry.pow_mul_eq_zero_of_res_basicOpen_eq_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/BasicOpenVanishing.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/BasicOpenVanishing.lean#L148).

> A meromorphic function on a quasi-compact open which vanishes on the basic open of a
> regular function there is annihilated by a power of that regular function.

```lean
lemma pow_mul_eq_zero_of_res_basicOpen_eq_zero
    (X : Scheme.{u}) {W : X.Opens} (hW : IsCompact (W : Set X)) (h : Γ(X, W))
    (f : X.totalQuotientSheaf.presheaf.obj (op W))
    (hf : X.totalQuotientSheaf.presheaf.map
      (homOfLE (X.basicOpen_le h)).op f = 0) :
    ∃ n : ℕ,
      (X.toTotalQuotientSheaf.hom.app (op W)).hom h ^ n * f = 0
```

**`AlgebraicGeometry.pow_mul_eq_zero_of_restrict_basicOpen_eq_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/BasicOpenVanishing.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/BasicOpenVanishing.lean#L174).

> A meromorphic function vanishing on the basic open of a global regular function is
> annihilated by a power of that regular function.

```lean
lemma pow_mul_eq_zero_of_restrict_basicOpen_eq_zero
    (X : Scheme.{u}) [CompactSpace X] (h : Γ(X, ⊤))
    (f : X.totalQuotientSheaf.presheaf.obj (op ⊤))
    (hf : X.totalQuotientSheaf.presheaf.map
      (homOfLE (X.basicOpen_le h)).op f = 0) :
    ∃ n : ℕ,
      (X.toTotalQuotientSheaf.hom.app (op ⊤)).hom h ^ n * f = 0
```

## Tag 02OV, a lemma

[Tag 02OV](https://stacks.math.columbia.edu/tag/02OV) in the Stacks Project.

**`AlgebraicGeometry.stalk_totalQuotientSheaf_isFractionRing_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/NoetherianSheafSections.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/NoetherianSheafSections.lean#L144). The attribute's comment: “part (1), for the sheaf”. References: EGA IV (21.6.7), “partial”.

> At every point of a locally Noetherian scheme the stalk of the sheaf of meromorphic
> functions is the total quotient ring of the local ring.

```lean
theorem stalk_totalQuotientSheaf_isFractionRing_of_isLocallyNoetherian
    (X : Scheme.{u}) [IsLocallyNoetherian X] (x : X) :
    letI : Algebra (X.presheaf.stalk x) (X.totalQuotientSheaf.presheaf.stalk x) :=
      ((TopCat.Presheaf.stalkFunctor CommRingCat x).map
        X.toTotalQuotientSheaf.hom).hom.toAlgebra
    IsFractionRing (X.presheaf.stalk x) (X.totalQuotientSheaf.presheaf.stalk x)
```

**`AlgebraicGeometry.isLocalization_totalQuotientSheaf_obj_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/NoetherianSheafSections.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/NoetherianSheafSections.lean#L240). The attribute's comment: “part (2)”.

> **The sheaf of meromorphic functions on an affine open of a locally Noetherian scheme.**
> The sections of `K_X` over an affine open `U` form the total quotient ring of `Γ(X, U)`.

```lean
theorem isLocalization_totalQuotientSheaf_obj_of_isLocallyNoetherian
    (X : Scheme.{u}) [IsLocallyNoetherian X] (U : X.Opens) (hU : IsAffineOpen U) :
    letI : Algebra Γ(X, U) (X.totalQuotientSheaf.presheaf.obj (op U)) :=
      (X.toTotalQuotientSheaf.hom.app (op U)).hom.toAlgebra
    IsLocalization Γ(X, U)⁰ (X.totalQuotientSheaf.presheaf.obj (op U))
```

**`AlgebraicGeometry.isLocalization_totalQuotientPresheaf_obj_of_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/Stalks.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/Stalks.lean#L57). The attribute's comment: “affine_total_quotient”.

> On an affine open of a scheme, meromorphic functions form the total quotient ring of the
> ring of regular functions. No Noetherian hypothesis is needed: the denominator submonoid of
> the total quotient presheaf on an affine open is already all of `nonZeroDivisors Γ(X, U)`.

```lean
theorem isLocalization_totalQuotientPresheaf_obj_of_isAffineOpen
    (X : Scheme.{u}) (U : X.Opens)
    (hU : IsAffineOpen U) :
    letI : Algebra Γ(X, U)
        ((X.presheaf.totalQuotientPresheaf).obj (Opposite.op U)) :=
      (X.presheaf.toTotalQuotientPresheaf.app (Opposite.op U)).hom.toAlgebra
    IsLocalization (nonZeroDivisors Γ(X, U))
      ((X.presheaf.totalQuotientPresheaf).obj (Opposite.op U))
```

**`AlgebraicGeometry.regularSectionGerms_eq_nonZeroDivisors_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/Stalks.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/Stalks.lean#L200). The attribute's comment: “regular_stalk”.

> At a point of a locally Noetherian scheme, the germs of regular local
> sections are exactly the non-zero-divisors in the local ring.

```lean
theorem regularSectionGerms_eq_nonZeroDivisors_of_isLocallyNoetherian
    (X : Scheme.{u}) [IsLocallyNoetherian X] (x : X) :
    (⨆ (U : Opens X) (hx : x ∈ U),
      ((X.presheaf.submonoidPresheafOfStalk
        (fun y ↦ nonZeroDivisors (X.presheaf.stalk y))).obj (Opposite.op U)).map
          (X.presheaf.germ U x hx).hom) =
      nonZeroDivisors (X.presheaf.stalk x)
```

**`AlgebraicGeometry.stalk_totalQuotientPresheaf_isFractionRing_of_isLocallyNoetherian`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/Stalks.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/Stalks.lean#L227). The attribute's comment: “stalk_total_quotient”. References: EGA IV (21.6.7), “partial”.

> At every point of a locally Noetherian scheme, the stalk of the presheaf of meromorphic
> functions is the total quotient ring of the local ring.

```lean
lemma stalk_totalQuotientPresheaf_isFractionRing_of_isLocallyNoetherian
    (X : Scheme.{u}) [IsLocallyNoetherian X] (x : X) :
    letI : Algebra (X.presheaf.stalk x) (X.presheaf.totalQuotientPresheaf.stalk x) :=
      ((TopCat.Presheaf.stalkFunctor CommRingCat x).map
        X.presheaf.toTotalQuotientPresheaf).hom.toAlgebra
    IsFractionRing (X.presheaf.stalk x) (X.presheaf.totalQuotientPresheaf.stalk x)
```

## Tag 0EMH, a lemma

[Tag 0EMH](https://stacks.math.columbia.edu/tag/0EMH) in the Stacks Project.

**`Stacks.AlgebraicGeometry.GenericPointCoproduct.meromorphicFunctions_iso_coproduct_of_noEmbeddedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GenericPointCoproduct/Decomposition.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GenericPointCoproduct/Decomposition.lean#L116). The attribute's comment: “meromorphic functions as a direct sum”.

> **Stacks Project, Tag 0EMH.** On a locally Noetherian scheme without embedded points, the
> `𝒪_X`-module of meromorphic functions is the direct sum, over the generic points of the
> irreducible components, of the structure sheaves of the local schemes there, pushed forward to
> `X`.

```lean
theorem meromorphicFunctions_iso_coproduct_of_noEmbeddedPoints (X : Scheme.{u})
    [IsLocallyNoetherian X] (hX : AlgebraicGeometry.HasNoEmbeddedPoints X) :
    Nonempty (meromorphicFunctions X ≅
      ∐ fun η : genericPoints X ↦ genericPointStalkModule X η)
```

**`Stacks.AlgebraicGeometry.GenericPointProduct.meromorphicFunctions_iso_product_of_noEmbeddedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GenericPointProduct/Decomposition.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GenericPointProduct/Decomposition.lean#L108). The attribute's comment: “meromorphic functions as a product”.

> **Stacks Project, Tag 0EMH.** On a locally Noetherian scheme without embedded points, the
> `𝒪_X`-module of meromorphic functions is the product, over the generic points of the irreducible
> components, of the structure sheaves of the local schemes there, pushed forward to `X`.

```lean
theorem meromorphicFunctions_iso_product_of_noEmbeddedPoints (X : Scheme.{u})
    [IsLocallyNoetherian X] (hX : AlgebraicGeometry.HasNoEmbeddedPoints X) :
    Nonempty (meromorphicFunctions X ≅
      ∏ᶜ fun η : genericPoints X ↦ genericPointStalkModule X η)
```

**`AlgebraicGeometry.nonempty_meromorphicSections_iso_product_genericPointStalks_of_hasNoEmbeddedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean, line 696](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean#L696). The attribute's comment: “meromorphic sections as a product”.

> **Stacks 0EMH**, the product decomposition of the sheaf of meromorphic sections.

```lean
theorem nonempty_meromorphicSections_iso_product_genericPointStalks_of_hasNoEmbeddedPoints
    (X : Scheme.{u}) [IsLocallyNoetherian X] (hX : HasNoEmbeddedPoints X)
    (F : X.Modules) [F.IsQuasicoherent] :
    Nonempty (meromorphicSections X F ≅
      ∏ᶜ fun η : genericPoints X ↦ genericPointStalkModuleOf X F η)
```

**`AlgebraicGeometry.nonempty_meromorphicSections_iso_coproduct_genericPointStalks_of_hasNoEmbeddedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean, line 707](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean#L707). The attribute's comment: “meromorphic sections as a direct sum”.

> **Stacks 0EMH**, the direct-sum decomposition of the sheaf of meromorphic sections.

```lean
theorem nonempty_meromorphicSections_iso_coproduct_genericPointStalks_of_hasNoEmbeddedPoints
    (X : Scheme.{u}) [IsLocallyNoetherian X] (hX : HasNoEmbeddedPoints X)
    (F : X.Modules) [F.IsQuasicoherent] :
    Nonempty (meromorphicSections X F ≅
      ∐ fun η : genericPoints X ↦ genericPointStalkModuleOf X F η)
```

**`AlgebraicGeometry.meromorphicSections_isQuasicoherent_of_hasNoEmbeddedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean, line 718](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean#L718). The attribute's comment: “quasi-coherence of meromorphic sections”.

> **Stacks 0EMH**, quasi-coherence of the sheaf of meromorphic sections.

```lean
theorem meromorphicSections_isQuasicoherent_of_hasNoEmbeddedPoints
    (X : Scheme.{u}) [IsLocallyNoetherian X] (hX : HasNoEmbeddedPoints X)
    (F : X.Modules) [F.IsQuasicoherent] :
    (meromorphicSections X F).IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.MeromorphicQuasicoherent.meromorphicFunctions_isQuasicoherent_of_noEmbeddedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicQuasicoherent/Criteria.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MeromorphicQuasicoherent/Criteria.lean#L80). The attribute's comment: “quasi-coherence of meromorphic functions”.

> **Stacks Project, Tag 0EMH.** On a locally Noetherian scheme without embedded points, the
> sheaf of meromorphic functions is quasi-coherent.

```lean
theorem meromorphicFunctions_isQuasicoherent_of_noEmbeddedPoints (X : Scheme.{u})
    [IsLocallyNoetherian X] (hX : AlgebraicGeometry.HasNoEmbeddedPoints X) :
    (meromorphicFunctions X).IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.MeromorphicSectionsTensor.meromorphicSections_isQuasicoherent_of_noEmbeddedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicSectionsTensor/Quasicoherent.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MeromorphicSectionsTensor/Quasicoherent.lean#L89). The attribute's comment: “quasi-coherence of meromorphic sections”.

> **Stacks Project, Tag 0EMH, quasi-coherence of meromorphic sections.** On a locally Noetherian
> scheme without embedded points, the sheaf of meromorphic sections of a quasi-coherent
> `𝒪_X`-module is quasi-coherent.

```lean
theorem meromorphicSections_isQuasicoherent_of_noEmbeddedPoints (X : Scheme.{u})
    [IsLocallyNoetherian X] (hX : AlgebraicGeometry.HasNoEmbeddedPoints X) (F : X.Modules)
    (hF : F.IsQuasicoherent) :
    (meromorphicSections X F).IsQuasicoherent
```

**`AlgebraicGeometry.exists_commRing_rationalFunctions_ringEquiv_totalQuotientSheaf_top_of_hasNoEmbeddedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RationalFunctions/Meromorphic.lean, line 661](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RationalFunctions/Meromorphic.lean#L661). The attribute's comment: “rational functions are meromorphic functions”. References: EGA I (7.1.3), “special case”.

> **[Stacks, Tag 0EMH]**: on a locally Noetherian scheme without embedded points, the ring of
> rational functions is the ring of global meromorphic functions.

```lean
theorem exists_commRing_rationalFunctions_ringEquiv_totalQuotientSheaf_top_of_hasNoEmbeddedPoints
    (X : Scheme.{u}) [IsLocallyNoetherian X] (hX : HasNoEmbeddedPoints X) :
    ∃ _ : CommRing X.rationalFunctions,
      (∀ (U : X.Opens) (hU : Dense (U : Set X)),
          ∃ ψ : Γ(X, U) →+* X.rationalFunctions,
            ∀ s, ψ s = X.rationalFunctionOfSection U hU s) ∧
        Nonempty (X.rationalFunctions ≃+* X.totalQuotientSheaf.presheaf.obj (op ⊤))
```

## Tag 0EMI, a lemma

[Tag 0EMI](https://stacks.math.columbia.edu/tag/0EMI) in the Stacks Project.

**`AlgebraicGeometry.exists_isRegularMeromorphicSection_of_hasNoEmbeddedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/RegularSectionExistence.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Meromorphic/RegularSectionExistence.lean#L450).

> **[Stacks, Tag 0EMI]**, which is case (3) of [Stacks, Tag 02OZ]. An invertible sheaf of
> modules on a locally Noetherian scheme without embedded points has a regular meromorphic
> section.

```lean
theorem exists_isRegularMeromorphicSection_of_hasNoEmbeddedPoints (X : Scheme.{u})
    [IsLocallyNoetherian X] (hX : HasNoEmbeddedPoints X) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L] :
    ∃ s : MeromorphicSection X.sheaf L, IsRegularMeromorphicSection X.sheaf L s
```

## Tag 02P2, a lemma

[Tag 02P2](https://stacks.math.columbia.edu/tag/02P2) in the Stacks Project.

**`AlgebraicGeometry.denominatorIdealSmul`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean#L131). The attribute's comment: “the product of the denominator ideal and the module”.

> The product `I · F` of the ideal of denominators of `s` and the module `F`: the image of the
> action of `I` on `F`.

```lean
def denominatorIdealSmul : X.Modules
```

**`AlgebraicGeometry.denominatorIdealSmulι`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean#L136). The attribute's comment: “the first canonical map”.

> The first canonical map, the inclusion `I · F ⟶ F`.

```lean
def denominatorIdealSmulι : denominatorIdealSmul X L F s ⟶ F
```

**`AlgebraicGeometry.denominatorIdealBadLocus_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean#L161). The attribute's comment: “the exceptional subset is closed”.

> The exceptional subset is closed.
>
> Both cokernels are quotients of modules of finite type — the structure sheaf and the invertible
> sheaf `L`, both coherent on a locally Noetherian scheme — so both supports are closed.
>
> Regularity of `s` is not used: the source assumes it throughout Tag 02P2, but of the
> exceptional subset's two properties only nowhere denseness needs it.

```lean
theorem denominatorIdealBadLocus_isClosed [IsLocallyNoetherian X]
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj
      X.ringCatSheaf.property L) :
    IsClosed (denominatorIdealBadLocus X L s)
```

**`AlgebraicGeometry.denominatorIdealBadLocus_isNowhereDense`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean#L179). The attribute's comment: “the exceptional subset is nowhere dense”.

> The exceptional subset is nowhere dense: each of its two pieces is contained in a closed
> nowhere dense subset by [Stacks, Tag 02P0].

```lean
theorem denominatorIdealBadLocus_isNowhereDense
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj
      X.ringCatSheaf.property L)
    (hs : IsRegularMeromorphicSection X.sheaf L s) :
    IsNowhereDense (denominatorIdealBadLocus X L s)
```

**`AlgebraicGeometry.denominatorIdealSmul_inclusion_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean#L191). The attribute's comment: “injectivity of the first map”.

> The first canonical map is injective: it is the inclusion of the image of the action map,
> hence the kernel of a cokernel projection.

```lean
theorem denominatorIdealSmul_inclusion_mono : Mono (denominatorIdealSmulι X L F s)
```

**`AlgebraicGeometry.denominatorIdealSmul_inclusion_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean#L225). The attribute's comment: “support of the first cokernel”.

> The cokernel of the first canonical map is supported on the exceptional subset.
>
> Off the support of `𝒪_X / I` the stalk map of the ideal inclusion is surjective; tensoring with
> `F` and composing with the left unit constraint keeps it so, and the action map factors through
> `I · F`, so the stalk map of the inclusion `I · F ⟶ F` is surjective there as well.

```lean
theorem denominatorIdealSmul_inclusion_support :
    SheafOfModules.supp (cokernel (denominatorIdealSmulι X L F s)) ⊆
      denominatorIdealBadLocus X L s
```

**`AlgebraicGeometry.denominatorIdealSmulMul`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean#L387). The attribute's comment: “the second canonical map”.

> **The second canonical map `I · F ⟶ F ⊗ L`**, multiplication by the meromorphic section on
> the product `I · F`, together with the identity characterising it: its composite with the
> factorisation of the action map through its image is multiplication by `s` on `I ⊗ F`. Since that
> factorisation is an epimorphism the identity determines the map, so this is the canonical map and
> not an arbitrary one.

```lean
def denominatorIdealSmulMul [IsLocallyNoetherian X]
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj
      X.ringCatSheaf.property L)
    (hs : IsRegularMeromorphicSection X.sheaf L s)
    [F.IsCoherent] (hF : AlgebraicGeometry.HasNoEmbeddedAssociatedPoints F)
    (hSupp : SheafOfModules.supp F = Set.univ) :
    { f : denominatorIdealSmul X L F s ⟶ Scheme.Modules.tensorObj F L //
      Abelian.factorThruImage (denominatorIdealTensorAction X L F s) ≫ f =
        denominatorIdealTensorMul X L F s }
```

**`AlgebraicGeometry.denominatorIdealSmulMul_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean#L403). The attribute's comment: “injectivity of the second map”.

> The second canonical map is injective: the two maps out of `I ⊗ F` have the same kernel, so
> the descents of each along the other's image factorisation are mutually inverse.

```lean
theorem denominatorIdealSmulMul_mono [IsLocallyNoetherian X]
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj
      X.ringCatSheaf.property L)
    (hs : IsRegularMeromorphicSection X.sheaf L s)
    [F.IsCoherent] (hF : AlgebraicGeometry.HasNoEmbeddedAssociatedPoints F)
    (hSupp : SheafOfModules.supp F = Set.univ) :
    Mono (denominatorIdealSmulMul X L F s hL hs hF hSupp).val
```

**`AlgebraicGeometry.denominatorIdealSmulMul_cokernel_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorAction.lean#L421). The attribute's comment: “support of the second cokernel”.

> The cokernel of the second canonical map is supported on the exceptional subset.
>
> Off the support of `L / s(I)` the stalk map of multiplication by `s` on the ideal is surjective;
> tensoring with `F` and composing with the symmetry keeps it so, and multiplication by `s` on
> `I ⊗ F` factors through `I · F`, so the stalk map of the second canonical map is surjective
> there as well.

```lean
theorem denominatorIdealSmulMul_cokernel_support [IsLocallyNoetherian X]
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj
      X.ringCatSheaf.property L)
    (hs : IsRegularMeromorphicSection X.sheaf L s)
    [F.IsCoherent] (hF : AlgebraicGeometry.HasNoEmbeddedAssociatedPoints F)
    (hSupp : SheafOfModules.supp F = Set.univ) :
    SheafOfModules.supp (cokernel (denominatorIdealSmulMul X L F s hL hs hF hSupp).val) ⊆
      denominatorIdealBadLocus X L s
```

**`AlgebraicGeometry.denominatorIdealTimesModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean#L405). The attribute's comment: “the product of the denominator ideal and the module”.

> The product `I F`, as a subobject of `F`.

```lean
noncomputable def denominatorIdealTimesModule
    (L F : SheafOfModules.{u} X.ringCatSheaf)
    (s : MeromorphicSection X.sheaf L) :
    SheafOfModules.{u} X.ringCatSheaf
```

**`AlgebraicGeometry.denominatorIdealTimesModuleι`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean#L413). The attribute's comment: “the first canonical map”.

> The inclusion `I F ⟶ F`.

```lean
noncomputable def denominatorIdealTimesModuleι
    (L F : SheafOfModules.{u} X.ringCatSheaf)
    (s : MeromorphicSection X.sheaf L) :
    denominatorIdealTimesModule X L F s ⟶ F
```

**`AlgebraicGeometry.denominatorBadLocus_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean#L466). The attribute's comment: “the exceptional subset is closed”.

> If `L` is invertible and `s` is a regular meromorphic section of `L` on a locally Noetherian
> scheme, then `denominatorBadLocus X L s` is closed.

```lean
theorem denominatorBadLocus_isClosed
    (L : SheafOfModules.{u} X.ringCatSheaf)
    (s : MeromorphicSection X.sheaf L)
    [IsLocallyNoetherian X]
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L)
    (hs : IsRegularMeromorphicSection X.sheaf L s) :
    IsClosed (denominatorBadLocus X L s)
```

**`AlgebraicGeometry.denominatorBadLocus_isNowhereDense`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean#L499). The attribute's comment: “the exceptional subset is nowhere dense”.

> If `L` is invertible and `s` is a regular meromorphic section of `L` on a locally Noetherian
> scheme, then `denominatorBadLocus X L s` is nowhere dense.

```lean
theorem denominatorBadLocus_isNowhereDense
    (L : SheafOfModules.{u} X.ringCatSheaf)
    (s : MeromorphicSection X.sheaf L)
    [IsLocallyNoetherian X]
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L)
    (hs : IsRegularMeromorphicSection X.sheaf L s) :
    IsNowhereDense (denominatorBadLocus X L s)
```

**`AlgebraicGeometry.denominatorIdealTimesModuleMul`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean, line 871](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean#L871). The attribute's comment: “the second canonical map”.

> The canonical section action, specified by its value on local products.

```lean
noncomputable def denominatorIdealTimesModuleMul
    (L F : SheafOfModules.{u} X.ringCatSheaf)
    (s : MeromorphicSection X.sheaf L)
    [IsLocallyNoetherian X]
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L)
    (hs : IsRegularMeromorphicSection X.sheaf L s)
    [F.IsCoherent]
    (hF : HasNoEmbeddedAssociatedPoints F)
    (hSupp : (AlgebraicGeometry.SheafOfModules.moduleSheafOfModules F).supp = Set.univ) :
      { f : denominatorIdealTimesModule X L F s ⟶
          (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
      ⟨X.toRingedSpace.presheaf, X.toRingedSpace.IsSheaf⟩).obj F).obj L) //
        Abelian.factorThruImage (denominatorIdealAction X L F s) ≫ f =
          denominatorIdealSectionTensor X L F s }
```

**`AlgebraicGeometry.denominatorIdealTimesModuleι_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean, line 894](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean#L894). The attribute's comment: “injectivity of the first map”.

> The inclusion `I F ⟶ F` is a monomorphism, because `I F` is by definition the image of the
> action of `I` on `F`.

```lean
theorem denominatorIdealTimesModuleι_mono
    (L F : SheafOfModules.{u} X.ringCatSheaf)
    (s : MeromorphicSection X.sheaf L) :
    Mono (denominatorIdealTimesModuleι X L F s)
```

**`AlgebraicGeometry.denominatorIdealTimesModuleMul_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean, line 903](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean#L903). The attribute's comment: “injectivity of the second map”.

> Under the hypotheses of `denominatorIdealTimesModuleMul`, the second canonical map
> `I F ⟶ F ⊗ L` is a monomorphism.

```lean
theorem denominatorIdealTimesModuleMul_mono
    (L F : SheafOfModules.{u} X.ringCatSheaf)
    (s : MeromorphicSection X.sheaf L)
    [IsLocallyNoetherian X]
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L)
    (hs : IsRegularMeromorphicSection X.sheaf L s)
    [F.IsCoherent]
    (hF : HasNoEmbeddedAssociatedPoints F)
    (hSupp : (AlgebraicGeometry.SheafOfModules.moduleSheafOfModules F).supp = Set.univ) :
    Mono (denominatorIdealTimesModuleMul X L F s hL hs hF hSupp).val
```

**`AlgebraicGeometry.denominatorIdealTimesModuleι_cokernel_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean, line 919](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean#L919). The attribute's comment: “support of the first cokernel”.

> The cokernel of the inclusion `I F ⟶ F` is supported on `denominatorBadLocus X L s`.

```lean
theorem denominatorIdealTimesModuleι_cokernel_support
    (L F : SheafOfModules.{u} X.ringCatSheaf)
    (s : MeromorphicSection X.sheaf L) :
      (AlgebraicGeometry.SheafOfModules.moduleSheafOfModules
        (cokernel (denominatorIdealTimesModuleι X L F s))).supp ⊆
      denominatorBadLocus X L s
```

**`AlgebraicGeometry.denominatorIdealTimesModuleMul_cokernel_supp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean, line 938](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Meromorphic/IdealTimesModule.lean#L938). The attribute's comment: “support of the second cokernel”.

> Under the hypotheses of `denominatorIdealTimesModuleMul`, the cokernel of the second
> canonical map `I F ⟶ F ⊗ L` is supported on `denominatorBadLocus X L s`.

```lean
theorem denominatorIdealTimesModuleMul_cokernel_supp
    (L F : SheafOfModules.{u} X.ringCatSheaf)
    (s : MeromorphicSection X.sheaf L)
    [IsLocallyNoetherian X]
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L)
    (hs : IsRegularMeromorphicSection X.sheaf L s)
    [F.IsCoherent]
    (hF : HasNoEmbeddedAssociatedPoints F)
    (hSupp : (AlgebraicGeometry.SheafOfModules.moduleSheafOfModules F).supp = Set.univ) :
    (AlgebraicGeometry.SheafOfModules.moduleSheafOfModules
      (cokernel (denominatorIdealTimesModuleMul X L F s hL hs hF hSupp).val)).supp ⊆
      denominatorBadLocus X L s
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.25, Tag 0EMG](https://stacks.math.columbia.edu/tag/0EMG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
