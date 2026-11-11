---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsAffineOpen.isLocalization_totalQuotientPresheaf_obj, AlgebraicGeometry.regularSectionGerms_eq_nonZeroDivisors_of_isReduced, AlgebraicGeometry.stalk_totalQuotientPresheaf_isFractionRing_of_isReduced, Stacks.AlgebraicGeometry.GenericPointCoproduct.meromorphicFunctions_iso_coproduct_genericPointStalks, Stacks.AlgebraicGeometry.GenericPointProduct.meromorphicFunctions_iso_product_genericPointStalks, AlgebraicGeometry.meromorphicFunctions_iso_coproduct_genericPointStalks_of_isReduced, AlgebraicGeometry.nonempty_meromorphicSections_iso_product_genericPointStalks_of_isReduced, AlgebraicGeometry.nonempty_meromorphicSections_iso_coproduct_genericPointStalks_of_isReduced
statement: formalized
proof: formalized
---

# 31.26 Meromorphic functions and sections; reduced case

Section 31.26 of the Stacks Project, [Tag 0EMJ](https://stacks.math.columbia.edu/tag/0EMJ). 4 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02OW, a lemma

[Tag 02OW](https://stacks.math.columbia.edu/tag/02OW) in the Stacks Project.

**`AlgebraicGeometry.IsAffineOpen.isLocalization_totalQuotientPresheaf_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/StalksReduced.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/StalksReduced.lean#L56). The attribute's comment: “part (5)”.

> On an affine open of any scheme, the meromorphic functions form the total quotient ring of
> the ring of regular functions: the localization at all nonzerodivisors.

```lean
theorem IsAffineOpen.isLocalization_totalQuotientPresheaf_obj
    {X : Scheme.{u}} {U : X.Opens} (hU : IsAffineOpen U) :
    letI : Algebra Γ(X, U)
        ((X.presheaf.totalQuotientPresheaf).obj (Opposite.op U)) :=
      (X.presheaf.toTotalQuotientPresheaf.app (Opposite.op U)).hom.toAlgebra
    IsLocalization (nonZeroDivisors Γ(X, U))
      ((X.presheaf.totalQuotientPresheaf).obj (Opposite.op U))
```

**`AlgebraicGeometry.regularSectionGerms_eq_nonZeroDivisors_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/StalksReduced.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/StalksReduced.lean#L76). The attribute's comment: “part (3)”.

> On a reduced scheme whose quasi-compact opens have finitely many irreducible components,
> the germs of regular sections at every point are exactly the nonzerodivisors in its local
> ring.

```lean
theorem regularSectionGerms_eq_nonZeroDivisors_of_isReduced (X : Scheme.{u}) [IsReduced X]
    (hfinite : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) :
    (⨆ (U : Opens X) (hx : x ∈ U),
      ((X.presheaf.submonoidPresheafOfStalk
        (fun y ↦ nonZeroDivisors (X.presheaf.stalk y))).obj (Opposite.op U)).map
          (X.presheaf.germ U x hx).hom) =
      nonZeroDivisors (X.presheaf.stalk x)
```

**`AlgebraicGeometry.stalk_totalQuotientPresheaf_isFractionRing_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/StalksReduced.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/StalksReduced.lean#L91). The attribute's comment: “part (4)”.

> On a reduced scheme whose quasi-compact opens have finitely many irreducible components,
> the stalk of the presheaf of meromorphic functions at any point is the total quotient ring of
> the local ring there.

```lean
theorem stalk_totalQuotientPresheaf_isFractionRing_of_isReduced (X : Scheme.{u}) [IsReduced X]
    (hfinite : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) :
    letI : Algebra (X.presheaf.stalk x) (X.presheaf.totalQuotientPresheaf.stalk x) :=
      ((TopCat.Presheaf.stalkFunctor CommRingCat x).map
        X.presheaf.toTotalQuotientPresheaf).hom.toAlgebra
    IsFractionRing (X.presheaf.stalk x) (X.presheaf.totalQuotientPresheaf.stalk x)
```

**`Stacks.AlgebraicGeometry.GenericPointCoproduct.meromorphicFunctions_iso_coproduct_genericPointStalks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GenericPointCoproduct/Decomposition.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GenericPointCoproduct/Decomposition.lean#L104). The attribute's comment: “generic-point direct sum”.

> **Stacks Project, Tag 02OW.** On a reduced scheme whose quasi-compact opens have finitely
> many irreducible components, the `𝒪_X`-module of meromorphic functions is the direct sum, over
> the generic points of the irreducible components, of the structure sheaves of the local schemes
> there, pushed forward to `X`.

```lean
theorem meromorphicFunctions_iso_coproduct_genericPointStalks (X : Scheme.{u}) [IsReduced X]
    (hfinite : GenericPointProduct.FiniteComponentsOnCompactOpens X) :
    Nonempty (meromorphicFunctions X ≅
      ∐ fun η : genericPoints X ↦ genericPointStalkModule X η)
```

**`Stacks.AlgebraicGeometry.GenericPointProduct.meromorphicFunctions_iso_product_genericPointStalks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GenericPointProduct/Decomposition.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GenericPointProduct/Decomposition.lean#L63). The attribute's comment: “generic-point product”.

> **Stacks Project, Tag 02OW.** On a reduced scheme whose quasi-compact opens have finitely many
> irreducible components, the `𝒪_X`-module of meromorphic functions is the product, over the generic
> points of the irreducible components, of the structure sheaves of the local schemes there, pushed
> forward to `X`.

```lean
theorem meromorphicFunctions_iso_product_genericPointStalks (X : Scheme.{u}) [IsReduced X]
    (hfinite : FiniteComponentsOnCompactOpens X) :
    Nonempty (meromorphicFunctions X ≅
      ∏ᶜ fun η : genericPoints X ↦ genericPointStalkModule X η)
```

**`AlgebraicGeometry.meromorphicFunctions_iso_coproduct_genericPointStalks_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Coproduct.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Coproduct.lean#L259). The attribute's comment: “generic-point direct sum”.

> **Stacks 02OW, displayed direct-sum decomposition.** On a reduced scheme whose quasi-compact
> opens have finitely many irreducible components, the `𝒪_X`-module of meromorphic functions is the
> direct sum of the generic-point contributions.

```lean
theorem meromorphicFunctions_iso_coproduct_genericPointStalks_of_isReduced (X : Scheme.{u})
    [IsReduced X]
    (hfinite : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    Nonempty (meromorphicFunctions X ≅
      ∐ fun η : genericPoints X ↦ genericPointStalkModule X η)
```

**`AlgebraicGeometry.nonempty_meromorphicSections_iso_product_genericPointStalks_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean, line 664](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean#L664). The attribute's comment: “part (2), product”.

> **Stacks 02OW, part (2), product decomposition.** On a reduced scheme whose quasi-compact
> opens have finitely many irreducible components, the sheaf of meromorphic sections of a
> quasi-coherent module is the product over the generic points of the irreducible components of
> the generic-point contributions.

```lean
theorem nonempty_meromorphicSections_iso_product_genericPointStalks_of_isReduced
    (X : Scheme.{u}) [IsReduced X]
    (hfinite : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (F : X.Modules) [F.IsQuasicoherent] :
    Nonempty (meromorphicSections X F ≅
      ∏ᶜ fun η : genericPoints X ↦ genericPointStalkModuleOf X F η)
```

**`AlgebraicGeometry.nonempty_meromorphicSections_iso_coproduct_genericPointStalks_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean, line 675](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean#L675). The attribute's comment: “part (2), direct sum”.

> **Stacks 02OW, part (2), direct-sum decomposition.**

```lean
theorem nonempty_meromorphicSections_iso_coproduct_genericPointStalks_of_isReduced
    (X : Scheme.{u}) [IsReduced X]
    (hfinite : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (F : X.Modules) [F.IsQuasicoherent] :
    Nonempty (meromorphicSections X F ≅
      ∐ fun η : genericPoints X ↦ genericPointStalkModuleOf X F η)
```

**`AlgebraicGeometry.meromorphicSections_isQuasicoherent_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean, line 686](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean#L686). The attribute's comment: “part (2), quasi-coherence”.

> **Stacks 02OW, part (2), quasi-coherence.**

```lean
theorem meromorphicSections_isQuasicoherent_of_isReduced
    (X : Scheme.{u}) [IsReduced X]
    (hfinite : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (F : X.Modules) [F.IsQuasicoherent] :
    (meromorphicSections X F).IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.MeromorphicQuasicoherent.meromorphicFunctions_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicQuasicoherent/Criteria.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MeromorphicQuasicoherent/Criteria.lean#L71). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 02OW, part (1).** On a reduced scheme whose quasi-compact opens have
> finitely many irreducible components, the sheaf of meromorphic functions is quasi-coherent.

```lean
theorem meromorphicFunctions_isQuasicoherent (X : Scheme.{u}) [IsReduced X]
    (hfinite : FiniteComponentsOnCompactOpens X) :
    (meromorphicFunctions X).IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.MeromorphicSectionsTensor.meromorphicSections_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicSectionsTensor/Quasicoherent.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MeromorphicSectionsTensor/Quasicoherent.lean#L78). The attribute's comment: “part (2), quasi-coherence”.

> **Stacks Project, Tag 02OW, part (2), quasi-coherence.** On a reduced scheme whose
> quasi-compact opens have finitely many irreducible components, the sheaf of meromorphic sections
> of a quasi-coherent `𝒪_X`-module is quasi-coherent.

```lean
theorem meromorphicSections_isQuasicoherent (X : Scheme.{u}) [IsReduced X]
    (hfinite : GenericPointProduct.FiniteComponentsOnCompactOpens X)
    (F : X.Modules) [F.IsQuasicoherent] :
    (meromorphicSections X F).IsQuasicoherent
```

**`AlgebraicGeometry.exists_commRing_rationalFunctions_ringEquiv_totalQuotientSheaf_top_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RationalFunctions/Meromorphic.lean, line 647](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RationalFunctions/Meromorphic.lean#L647). The attribute's comment: “part (6)”. References: EGA IV (20.2.13), “(ii) global sections”; EGA I (7.1.3), “special case”.

> **Part (6) of [Stacks, Tag 02OW].** On a reduced scheme whose quasi-compact opens have
> finitely many irreducible components, the ring of rational functions is the ring of global
> meromorphic functions.

```lean
theorem exists_commRing_rationalFunctions_ringEquiv_totalQuotientSheaf_top_of_isReduced
    (X : Scheme.{u}) [IsReduced X]
    (hfinite : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    ∃ _ : CommRing X.rationalFunctions,
      (∀ (U : X.Opens) (hU : Dense (U : Set X)),
          ∃ ψ : Γ(X, U) →+* X.rationalFunctions,
            ∀ s, ψ s = X.rationalFunctionOfSection U hU s) ∧
        Nonempty (X.rationalFunctions ≃+* X.totalQuotientSheaf.presheaf.obj (op ⊤))
```

**`Stacks.AlgebraicGeometry.ReducedTotalQuotient.regularSectionGerms_eq_nonZeroDivisors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ReducedTotalQuotient/Basic.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ReducedTotalQuotient/Basic.lean#L74). The attribute's comment: “part (3)”.

> Germs of regular sections are precisely the nonzerodivisors.

```lean
theorem regularSectionGerms_eq_nonZeroDivisors
    (X : Scheme.{u}) [IsReduced X]
    (hfinite : FiniteComponentsOnCompactOpens X) (x : X) :
    (⨆ (U : Opens X) (hx : x ∈ U),
      ((X.presheaf.submonoidPresheafOfStalk
        (fun y ↦ nonZeroDivisors (X.presheaf.stalk y))).obj (Opposite.op U)).map
          (X.presheaf.germ U x hx).hom) =
      nonZeroDivisors (X.presheaf.stalk x)
```

**`Stacks.AlgebraicGeometry.ReducedTotalQuotient.stalk_totalQuotientPresheaf_isFractionRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ReducedTotalQuotient/Basic.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ReducedTotalQuotient/Basic.lean#L87). The attribute's comment: “part (4)”.

> A stalk of the meromorphic-function sheaf is the total quotient ring of the local ring.

```lean
theorem stalk_totalQuotientPresheaf_isFractionRing
    (X : Scheme.{u}) [IsReduced X]
    (hfinite : FiniteComponentsOnCompactOpens X) (x : X) :
    letI : Algebra (X.presheaf.stalk x) (X.presheaf.totalQuotientPresheaf.stalk x) :=
      ((TopCat.Presheaf.stalkFunctor CommRingCat x).map
        X.presheaf.toTotalQuotientPresheaf).hom.toAlgebra
    IsFractionRing (X.presheaf.stalk x)
      (X.presheaf.totalQuotientPresheaf.stalk x)
```

**`Stacks.AlgebraicGeometry.ReducedTotalQuotient.isLocalization_totalQuotientPresheaf_obj_of_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ReducedTotalQuotient/Basic.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ReducedTotalQuotient/Basic.lean#L100). The attribute's comment: “part (5)”.

> Meromorphic functions on an affine open form the total quotient ring of its functions.

```lean
theorem isLocalization_totalQuotientPresheaf_obj_of_isAffineOpen
    (X : Scheme.{u}) [IsReduced X]
    (_hfinite : FiniteComponentsOnCompactOpens X)
    (U : X.Opens) (hU : IsAffineOpen U) :
    letI : Algebra Γ(X, U)
        ((X.presheaf.totalQuotientPresheaf).obj (Opposite.op U)) :=
      (X.presheaf.toTotalQuotientPresheaf.app (Opposite.op U)).hom.toAlgebra
    IsLocalization (nonZeroDivisors Γ(X, U))
      ((X.presheaf.totalQuotientPresheaf).obj (Opposite.op U))
```

## Tag 035T, a lemma

[Tag 035T](https://stacks.math.columbia.edu/tag/035T) in the Stacks Project.

**`AlgebraicGeometry.Scheme.normalizationGluedSpectrum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicRelativeSpec.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicRelativeSpec.lean#L393). The attribute's comment: “the normalization carries the charts of the relative spectrum”. References: EGA II (7.4.6), “special case”.

> **Stacks Project, Tag 035T.** The normalization of a reduced scheme whose quasi-compact
> opens have finitely many irreducible components, carrying the charts that present it as a
> relative spectrum of the integral closure of `𝒪_X` in the sheaf of meromorphic functions.

```lean
def normalizationGluedSpectrum (X : Scheme.{u}) [IsReduced X]
    (hfinite : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    GluedSpectrum (X.meromorphicIntegralClosureSituation hfinite)
```

**`AlgebraicGeometry.Scheme.normalizationIsoMeromorphicSpectrum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicRelativeSpec.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicRelativeSpec.lean#L407). The attribute's comment: “the comparison isomorphism”. References: EGA II (7.4.6), “special case”.

> **Stacks Project, Tag 035T.** For a reduced scheme whose quasi-compact opens have finitely
> many irreducible components, the normalization is the relative spectrum of the integral closure
> `𝒪'` of `𝒪_X` in the sheaf of meromorphic functions.

```lean
def normalizationIsoMeromorphicSpectrum (X : Scheme.{u}) [IsReduced X]
    (hfinite : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    X.normalizationScheme hfinite ≅
      (gluedSpectrum (X.meromorphicIntegralClosureSituation hfinite)).scheme
```

**`AlgebraicGeometry.Scheme.normalizationIsoMeromorphicSpectrum_hom_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicRelativeSpec.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicRelativeSpec.lean#L417). The attribute's comment: “the normalization is the structure morphism of the relative spectrum”.

> **Stacks Project, Tag 035T.** The comparison isomorphism lies over `X`: the normalization
> morphism `ν : X^ν ⟶ X` is the structure morphism of the relative spectrum of `𝒪'`.

```lean
theorem normalizationIsoMeromorphicSpectrum_hom_toBase (X : Scheme.{u}) [IsReduced X]
    (hfinite : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    (normalizationIsoMeromorphicSpectrum X hfinite).hom ≫
        (gluedSpectrum (X.meromorphicIntegralClosureSituation hfinite)).toBase =
      X.normalization hfinite
```

## Tag 01X5, a lemma

[Tag 01X5](https://stacks.math.columbia.edu/tag/01X5) in the Stacks Project.

**`AlgebraicGeometry.totalQuotientSheafIsoConstant`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/ConstantOnIntegral.lean, line 628](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/ConstantOnIntegral.lean#L628). The attribute's comment: “part (1)”. References: EGA I (7.3.6), “F = O\_X, integral”.

> An isomorphism between the sheaf of meromorphic functions on an integral scheme and the
> constant sheaf on its function field, carrying a regular section to the constant section
> determined by its germ at the generic point.

```lean
noncomputable def totalQuotientSheafIsoConstant (X : Scheme.{u}) [IsIntegral X] :
    { e : totalQuotientSheaf X.sheaf ≅
        constantSheafOnSpace X CommRingCat.{u} X.functionField //
      ∀ (U : X.Opens) (s : X.presheaf.obj (Opposite.op U))
        (h : genericPoint X ∈ U),
        (e.hom.hom.app (Opposite.op U)).hom
          ((toTotalQuotientSheaf X.sheaf).hom.app (Opposite.op U) s) =
        (toSheafify (Opens.grothendieckTopology X)
          ((Functor.const (Opens X)ᵒᵖ).obj X.functionField)).app (Opposite.op U)
            (X.presheaf.germ U (genericPoint X) h s) }
```

**`AlgebraicGeometry.nonempty_meromorphicSectionSheafIsoConstant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MeromorphicSectionsConstant.lean, line 985](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/MeromorphicSectionsConstant.lean#L985). The attribute's comment: “part (2)”. References: EGA I (7.3.6), “integral case”.

> On an integral scheme the sheaf of meromorphic sections of a quasi-coherent module `F` is the
> constant sheaf on the stalk of `F` at the generic point, read as a sheaf of modules over the sheaf
> of meromorphic functions through `AlgebraicGeometry.totalQuotientSheafIsoConstant`. For every
> adjunction `adj` between extension and restriction of scalars, the isomorphism may be chosen to
> carry the image of a section under the unit of `adj` to the constant section determined by its
> germ at the generic point.

```lean
theorem nonempty_meromorphicSectionSheafIsoConstant [F.IsQuasicoherent] :
    Nonempty { e : meromorphicSectionSheaf X.sheaf F ≅
      (SheafOfModules.restrictScalars
        ((sheafCompose (Opens.grothendieckTopology X)
          (forget₂ CommRingCat RingCat.{u})).map
            (totalQuotientSheafIsoConstant X).val.hom)).obj
        (constantGenericStalkModuleSheaf X F) //
      ∀ (U : X.Opens) (m : F.val.obj (Opposite.op U))
        (h : genericPoint X ∈ U),
        (e.hom.val.app (Opposite.op U))
          ((adj.unit.app F).val.app (Opposite.op U) m) =
          constantGenericStalkModuleSection X F U
            (F.presheaf.germ U (genericPoint X) h m) }
```

**`Stacks.AlgebraicGeometry.MeromorphicConstant.totalQuotientSheafIsoConstant`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicConstant/Basic.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MeromorphicConstant/Basic.lean#L417). The attribute's comment: “part (1)”. References: EGA I (7.3.6), “F = O\_X, integral”.

> On an integral scheme the sheaf of meromorphic functions is the constant sheaf with value the
> function field, by an isomorphism carrying the image of a regular function to the constant
> section given by its germ at the generic point.

```lean
noncomputable def totalQuotientSheafIsoConstant :
    { e : totalQuotientSheaf X.sheaf ≅ constantSheafOnSpace X CommRingCat.{u} X.functionField //
      ∀ (U : X.Opens) (s : X.presheaf.obj (op U)) (h : genericPoint X ∈ U),
        (e.hom.hom.app (op U)).hom
          ((toTotalQuotientSheaf X.sheaf).hom.app (op U) s) =
        (toSheafify (Opens.grothendieckTopology X)
          ((Functor.const (Opens X)ᵒᵖ).obj X.functionField)).app (op U)
            (X.presheaf.germ U (genericPoint X) h s) }
```

**`Stacks.AlgebraicGeometry.MeromorphicConstantModule.meromorphicSectionSheafIsoConstant`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicConstantModule/Basic.lean, line 572](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MeromorphicConstantModule/Basic.lean#L572). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 01X5, part (2).** On an integral scheme the sheaf of meromorphic
> sections of a quasi-coherent module `F` is the constant sheaf of modules with value the stalk of
> `F` at the generic point, over the sheaf of meromorphic functions, compatibly with the germ at
> the generic point.

```lean
noncomputable def meromorphicSectionSheafIsoConstant :
    { e : meromorphicSectionSheaf.{u, u} X.sheaf F ≅ constGenericStalkSheaf F //
      ∀ (U : X.Opens) (m : (pmod F).obj (op U)) (h : genericPoint X ∈ U),
        (e.hom.val.app (op U)).hom (toMeromorphicSection F U m) =
          constGenericStalkSection F U (F.presheaf.germ U (genericPoint X) h m) }
```

## Tag 02OZ, a lemma

[Tag 02OZ](https://stacks.math.columbia.edu/tag/02OZ) in the Stacks Project.

**`AlgebraicGeometry.exists_isRegularMeromorphicSection_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularSectionExistence.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularSectionExistence.lean#L160). The attribute's comment: “part (1)”.

> An invertible sheaf of modules on an integral scheme has a regular meromorphic section.

```lean
theorem exists_isRegularMeromorphicSection_of_isIntegral
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property F] :
    ∃ s : MeromorphicSection X.sheaf F, IsRegularMeromorphicSection X.sheaf F s
```

**`AlgebraicGeometry.exists_isRegularMeromorphicSection_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularSectionExistenceReduced.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularSectionExistenceReduced.lean#L138). The attribute's comment: “part (2)”.

> **Stacks 02OZ, part (2).** An invertible sheaf of modules on a reduced scheme every
> quasi-compact open of which has finitely many irreducible components has a regular meromorphic
> section.

```lean
theorem exists_isRegularMeromorphicSection_of_isReduced (X : Scheme.{u}) [IsReduced X]
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (L : X.Modules) [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L] :
    ∃ s : MeromorphicSection X.sheaf L, IsRegularMeromorphicSection X.sheaf L s
```

**`AlgebraicGeometry.exists_isRegularMeromorphicSection_of_noEmbeddedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularSectionExistenceReduced.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularSectionExistenceReduced.lean#L148). The attribute's comment: “part (3)”.

> **Stacks 02OZ, part (3).** An invertible sheaf of modules on a locally Noetherian scheme
> without embedded points has a regular meromorphic section.

```lean
theorem exists_isRegularMeromorphicSection_of_noEmbeddedPoints (X : Scheme.{u})
    [IsLocallyNoetherian X] (hX : HasNoEmbeddedPoints X) (L : X.Modules)
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L] :
    ∃ s : MeromorphicSection X.sheaf L, IsRegularMeromorphicSection X.sheaf L s
```

**`AlgebraicGeometry.exists_isRegularMeromorphicSection_of_hasNoEmbeddedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/RegularSectionExistence.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Meromorphic/RegularSectionExistence.lean#L450). The attribute's comment: “case (3), X locally Noetherian without embedded points”.

> **[Stacks, Tag 0EMI]**, which is case (3) of [Stacks, Tag 02OZ]. An invertible sheaf of
> modules on a locally Noetherian scheme without embedded points has a regular meromorphic
> section.

```lean
theorem exists_isRegularMeromorphicSection_of_hasNoEmbeddedPoints (X : Scheme.{u})
    [IsLocallyNoetherian X] (hX : HasNoEmbeddedPoints X) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L] :
    ∃ s : MeromorphicSection X.sheaf L, IsRegularMeromorphicSection X.sheaf L s
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.26, Tag 0EMJ](https://stacks.math.columbia.edu/tag/0EMJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
