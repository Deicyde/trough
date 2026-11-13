---
declaration: section
origin: cited
lean: Stacks.Chow.rationallyEquivalent_cycles_of_twoPeriodicComplex, Stacks.Chow.chowToWideLayerHom_injective_and_range, Stacks.Chow.layerChowClass_eq_zero_of_layerWideningClass_eq_zero, Stacks.Chow.coherentDimensionLayerImageChowHom, Stacks.Chow.coherentDimensionLayerImageChowHom_coherentDimensionKZeroMk, Stacks.Chow.coherentDimensionLayerImage, Ideal.fraction_smul_denominatorIdeal_le, Ideal.length_fractionalProduct_quotient_sub_length_denominator_quotient
statement: formalized
proof: formalized
---

# 42.69 Appendix B: Alternative approaches

Section 42.69 of the Stacks Project, [Tag 0AYD](https://stacks.math.columbia.edu/tag/0AYD). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02SB, a lemma

[Tag 02SB](https://stacks.math.columbia.edu/tag/02SB) in the Stacks Project.

**`Stacks.Chow.rationallyEquivalent_cycles_of_twoPeriodicComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexHomologyCycles/RationalEquivalence.lean, line 744](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexHomologyCycles/RationalEquivalence.lean#L744).

> **Stacks 02SB.** Let `F` be a coherent sheaf on a scheme `X` locally of finite type over the
> base, carrying a `(2, 1)`-periodic complex whose support has delta-dimension at most `k + 1` and
> whose two cohomology sheaves are supported in delta-dimension at most `k`. Then the two cohomology
> sheaves are coherent, their supports have delta-dimension at most `k`, and the associated
> `k`-cycles `[H⁰]_k` and `[H¹]_k` are rationally equivalent.

```lean
theorem rationallyEquivalent_cycles_of_twoPeriodicComplex
    (C : ChowSituation.{u}) {X : Scheme.{u}}
    (f : X ⟶ C.S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsCoherent]
    (K : CochainComplex X.Modules (ZMod 2))
    (e : ∀ i : ZMod 2, K.X i ≅ F) (k : ℤ)
    (hFk : schemeDeltaDimension C
      ((reducedSupport F).subschemeι ≫ f) ≤ ((k + 1 : ℤ) : EInt))
    (hHk : ∀ (i : ZMod 2) (x : X),
      x ∈ SheafOfModules.supp (K.homology i) →
        relativeDimension C.dimensionFunction f x ≤ k) :
    ∃ (h₀ : (K.homology (0 : ZMod 2)).IsCoherent)
      (h₁ : (K.homology (1 : ZMod 2)).IsCoherent),
      letI := h₀
      letI := h₁
      ∃ (d₀ : schemeDeltaDimension C
          ((reducedSupport (K.homology 0)).subschemeι ≫ f) ≤ (k : EInt))
        (d₁ : schemeDeltaDimension C
          ((reducedSupport (K.homology 1)).subschemeι ≫ f) ≤ (k : EInt)),
        RationallyEquivalent C f k
          (cycleAssociatedToCoherentSheaf C f (K.homology 0) k d₀)
          (cycleAssociatedToCoherentSheaf C f (K.homology 1) k d₁)
```

## Tag 02SC, a lemma

[Tag 02SC](https://stacks.math.columbia.edu/tag/02SC) in the Stacks Project.

**`Stacks.Chow.chowToWideLayerHom_injective_and_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerChowBijection.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerChowBijection.lean#L83).

> **Stacks 02SC.** Let `X` be locally of finite type over `(S, δ)`. The map
> `CH_k(X) ⟶ K₀(Coh_{≤k+1}(X)/Coh_{≤k-1}(X))` of Tag 0FDS is injective, and its image is the image
> `B_k(X)` of `K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X)) ⟶ K₀(Coh_{≤k+1}(X)/Coh_{≤k-1}(X))`; that is, it
> induces a bijection from `CH_k(X)` onto `B_k(X)`.

```lean
theorem chowToWideLayerHom_injective_and_range (C : ChowSituation.{u}) (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (k : ℤ) :
    Function.Injective (chowToWideLayerHom C sX k) ∧
      (chowToWideLayerHom C sX k).range = coherentDimensionLayerImage C sX k
```

**`Stacks.Chow.layerChowClass_eq_zero_of_layerWideningClass_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerChowComparison.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerChowComparison.lean#L233). The attribute's comment: “the comparison: a class killed in `K₀(Coh_{≤k+1}/Coh_{≤k-1})` has trivial cycle”.

> **Stacks 02SC, the comparison.** An element of `K₀(Coh_{≤k}(X))` whose class in
> `K₀(Coh_{≤k+1}(X)/Coh_{≤k-1}(X))` vanishes has rationally trivial `k`-cycle.
>
> This is the content of Stacks 02SC: by Stacks 02MX (1) the vanishing produces an object of
> `Coh_{≤k-1}(X)` correcting the element to one that already dies in `K₀(Coh_{≤k+1}(X))`, by
> Stacks 02MX (2) that corrected element is the difference of the classes of the two homology
> objects of a `(2, 1)`-periodic complex of `Coh_{≤k+1}(X)`, and by Stacks 02SB the `k`-cycles of
> those two homology objects are rationally equivalent.

```lean
theorem layerChowClass_eq_zero_of_layerWideningClass_eq_zero (C : ChowSituation.{u})
    (f : X ⟶ C.S) [LocallyOfFiniteType f] (k : ℤ) (a : KZero (CoherentModulesDimLE C f k))
    (ha : layerWideningClass C f k a = 0) : layerChowClass C f k a = 0
```

**`Stacks.Chow.coherentDimensionLayerImageChowHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerChowComparison.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerChowComparison.lean#L268). The attribute's comment: “the homomorphism `Bₖ(X) → CH_k(X)` the bijection of the tag inverts”.

> **Stacks 02SC.** The homomorphism `Bₖ(X) ⟶ CH_k(X)`. On the class of a coherent
> `𝒪_X`-module `A` with `dim_δ(Supp A) ≤ k` it is the class of the `k`-cycle `[A]_k`; this is
> `Stacks.Chow.coherentDimensionLayerImageChowHom_apply` below. It exists because the `k`-cycle of
> an element of `K₀(Coh_{≤k}(X))` killed by the map to `K₀(Coh_{≤k+1}(X)/Coh_{≤k-1}(X))` is
> rationally trivial, which is
> `Stacks.Chow.layerChowClass_eq_zero_of_layerWideningClass_eq_zero`.

```lean
def coherentDimensionLayerImageChowHom (C : ChowSituation.{u}) (f : X ⟶ C.S)
    [LocallyOfFiniteType f] (k : ℤ) :
    coherentDimensionLayerImage C f k →+ chowGroup C f k
```

**`Stacks.Chow.coherentDimensionLayerImageChowHom_coherentDimensionKZeroMk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerChowComparison.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerChowComparison.lean#L296). The attribute's comment: “the value of `Bₖ(X) → CH_k(X)` on the class of a coherent module”.

> **Stacks 02SC.** The homomorphism `Bₖ(X) ⟶ CH_k(X)` sends the class of a coherent
> `𝒪_X`-module `F` with `dim_δ(Supp F) ≤ k`, read in the layer `(k-1, k+1]`, to the class of the
> `k`-cycle `[F]_k`.

```lean
theorem coherentDimensionLayerImageChowHom_coherentDimensionKZeroMk (C : ChowSituation.{u})
    (f : X ⟶ C.S) [LocallyOfFiniteType f] (k : ℤ) (F : CoherentModulesDimLE C f k)
    (hF : coherentDimensionKZeroMk C f (k - 1) (k + 1) ((dimensionLayerInclusion C f k).obj F) ∈
      coherentDimensionLayerImage C f k) :
    coherentDimensionLayerImageChowHom C f k
        ⟨coherentDimensionKZeroMk C f (k - 1) (k + 1) ((dimensionLayerInclusion C f k).obj F),
          hF⟩ =
      QuotientAddGroup.mk' (rationalEquivalences C f k) (layerCycleOfLE C f k F F.property)
```

**`Stacks.Chow.coherentDimensionLayerImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerKGroup.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerKGroup.lean#L232). The attribute's comment: “b\_k\_x”.

> **Stacks 02SC, `Bₖ(X)`.** The image of the homomorphism of Grothendieck groups induced by the
> inclusion of the dimension layer `(k - 1, k]` into the layer `(k - 1, k + 1]`.

```lean
def coherentDimensionLayerImage (C : ChowSituation.{u}) (f : X ⟶ C.S) [LocallyOfFiniteType f]
    (k : ℤ) : AddSubgroup (coherentDimensionKZero C f (k - 1) (k + 1))
```

## Tag 02QH, a lemma

[Tag 02QH](https://stacks.math.columbia.edu/tag/02QH) in the Stacks Project.

**`Ideal.fraction_smul_denominatorIdeal_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CartierDivisorsK/Basic.lean, line 467](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/CartierDivisorsK/Basic.lean#L467). The attribute's comment: “containment”.

> **Stacks Project, Tag 02QH, containment assertion.** Multiplying `I M` by `a / b` in the
> localization of `M` at the nonzerodivisors lands back in the image of `M`.

```lean
theorem fraction_smul_denominatorIdeal_le
    {R M : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    (a b : R) (hb : b ∈ nonZeroDivisors R) :
    ∀ x ∈ denominatorIdeal a b • (⊤ : Submodule R M),
      IsLocalization.mk' (FractionRing R) a ⟨b, hb⟩ •
          LocalizedModule.mkLinearMap (nonZeroDivisors R) M x ∈
        Set.range (LocalizedModule.mkLinearMap (nonZeroDivisors R) M)
```

**`Ideal.length_fractionalProduct_quotient_sub_length_denominator_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CartierDivisorsK/Basic.lean, line 507](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/CartierDivisorsK/Basic.lean#L507). The attribute's comment: “length formula”.

> **Stacks Project, Tag 02QH, length formula.** The difference between the colength of
> `(a / b) I M` and that of `I M` is the sum of the generic lengths of `M`, weighted by the
> orders of `a / b` on the irreducible components.

```lean
theorem length_fractionalProduct_quotient_sub_length_denominator_quotient
    {R M : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    (a b : R) (ha : a ∈ nonZeroDivisors R) (hb : b ∈ nonZeroDivisors R)
    (hRdim : ringKrullDim R = 1)
    (hMembedded : HasNoEmbeddedAssociatedPrimes R M)
    (hMsupport : Module.support R M = Set.univ) :
    ((Module.length R
        (M ⧸ fractionalProductIdeal a b • (⊤ : Submodule R M))).toNat : ℤ) -
      ((Module.length R
        (M ⧸ denominatorIdeal a b • (⊤ : Submodule R M))).toNat : ℤ) =
      ∑ᶠ q ∈ {q : PrimeSpectrum R | q.asIdeal ∈ minimalPrimes R},
        ((Module.length (Localization.AtPrime q.asIdeal)
          (LocalizedModule q.asIdeal.primeCompl M)).toNat : ℤ) *
          (((Ring.ord (R ⧸ q.asIdeal)
            (Ideal.Quotient.mk q.asIdeal a)).toNat : ℤ) -
            ((Ring.ord (R ⧸ q.asIdeal)
              (Ideal.Quotient.mk q.asIdeal b)).toNat : ℤ))
```

## Tag 02SW, a lemma

[Tag 02SW](https://stacks.math.columbia.edu/tag/02SW) in the Stacks Project.

**`Stacks.Chow.denominatorQuotients_shortExact_isCoherent_and_firstChernClassCap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DenominatorQuotients/CapProductIdentity.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DenominatorQuotients/CapProductIdentity.lean#L226). The attribute's comment: “parts (1), (2), (3) and (4)”.

> **Stacks 02SW.** Let `(S, δ)` be as in Situation 42.7.1, let `X` be locally of finite type
> over `S`, let `ℒ` be an invertible `𝒪_X`-module, let `ℱ` be a coherent `𝒪_X`-module and let
> `s ∈ Γ(X, 𝒦_X(ℒ))` be a meromorphic section of `ℒ`. Assume
>
> 1. `dim_δ(X) ≤ k + 1`,
> 2. `X` has no embedded points,
> 3. `ℱ` has no embedded associated points,
> 4. the support of `ℱ` is `X`, and
> 5. the section `s` is regular meromorphic.
>
> Let `ℐ ⊂ 𝒪_X` be the ideal of denominators of `s`. Then we have the following:
>
> 1. there are short exact sequences
>
>      `0 ⟶ ℐℱ ⟶^1 ℱ ⟶ 𝒬₁ ⟶ 0`,   `0 ⟶ ℐℱ ⟶^s ℱ ⊗_{𝒪_X} ℒ ⟶ 𝒬₂ ⟶ 0`;
>
> 2. the coherent sheaves `𝒬₁`, `𝒬₂` are supported in δ-dimension `≤ k`;
> 3. the section `s` restricts to a regular meromorphic section `sᵢ` on every irreducible
>    component `Xᵢ` of `X` of δ-dimension `k + 1`; and
> 4. writing `[ℱ]_{k+1} = ∑ᵢ mᵢ[Xᵢ]` we have
>
>      `[𝒬₂]_k - [𝒬₁]_k = ∑ᵢ mᵢ (Xᵢ ⟶ X)_* div_{ℒ|_{Xᵢ}}(sᵢ)`   in   `Z_k(X)`,
>
>    in particular
>
>      `[𝒬₂]_k - [𝒬₁]_k = c₁(ℒ) ∩ [ℱ]_{k+1}`   in   `CH_k(X)`.
>
> This is the declaration carrying the tag; the results above and in
> `StacksFrontier.AlgebraicGeometry.Chow.DenominatorQuotients.Basic`,
> `StacksFrontier.AlgebraicGeometry.Chow.DenominatorQuotients.ComponentDivisor` and
> `StacksFrontier.AlgebraicGeometry.Chow.DenominatorQuotients.CycleIdentity` are its components.
>
> An irreducible component of `X` is named by its generic point `η`, carrying the reduced induced
> structure `Stacks.Chow.integralComponentAt η`; `sᵢ` is `Stacks.Chow.componentMeromorphicSection`,
> the pullback of `s` along its closed immersion, and `(Xᵢ ⟶ X)_* div_{ℒ|_{Xᵢ}}(sᵢ)` is
> `Stacks.Chow.componentDivisorCycle`.
>
> The presentation `[ℱ]_{k+1} = ∑ᵢ mᵢ[Xᵢ]` is the first conjunct of part (4): its index is
> `Stacks.Chow.topSupportPoints C f ℱ (k + 1)`, the points of the support of `ℱ` of
> δ-dimension `k + 1`, and its coefficients `mᵢ` are the multiplicities
> `Stacks.Chow.sheafMultiplicity ℱ ηᵢ`. The second conjunct — the equality in `Z_k(X)` — is read
> coefficientwise, at an arbitrary point `x` of `X`, because the family of components of
> δ-dimension `k + 1` is locally finite rather than finite, so both sides exist as locally finite
> sums; a cycle is its coefficient function, so this is the asserted equality of cycles.

```lean
theorem denominatorQuotients_shortExact_isCoherent_and_firstChernClassCap
    (C : ChowSituation.{u}) {X : Scheme.{u}} (f : X ⟶ C.S) [LocallyOfFiniteType f]
    (L F : X.Modules) (s : AlgebraicGeometry.MeromorphicSection X.sheaf L) [F.IsCoherent]
    {k : ℤ}
    (hdim : schemeDeltaDimension C f ≤ ((k + 1 : ℤ) : EInt))
    (hX : HasNoEmbeddedPoints X)
    (hF : HasNoEmbeddedAssociatedPoints F)
    (hSupp : (AlgebraicGeometry.SheafOfModules.moduleSheafOfModules F).supp = Set.univ)
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L)
    (hs : IsRegularMeromorphicSection X.sheaf L s) :
    -- (1) `0 ⟶ ℐℱ ⟶^1 ℱ ⟶ 𝒬₁ ⟶ 0` is short exact
    (denominatorQuotientShortComplex X L F s).ShortExact ∧
    -- (1) `0 ⟶ ℐℱ ⟶^s ℱ ⊗ ℒ ⟶ 𝒬₂ ⟶ 0` is short exact
    (@denominatorSectionQuotientShortComplex X L F s
        (LocallyOfFiniteType.isLocallyNoetherian f) hL hs inferInstance hF hSupp).ShortExact ∧
    -- (2) `𝒬₁` and `𝒬₂` are coherent
    (denominatorQuotient X L F s).IsCoherent ∧
    (@denominatorSectionQuotient X L F s (LocallyOfFiniteType.isLocallyNoetherian f) hL hs
        inferInstance hF hSupp).IsCoherent ∧
    -- (2) and are supported in δ-dimension `≤ k`
    schemeDeltaDimension C ((@reducedSupport X (denominatorQuotient X L F s)
        (isCoherent_denominatorQuotient C f L F s hdim hX hF hSupp hL hs)).subschemeι ≫ f)
      ≤ (k : EInt) ∧
    schemeDeltaDimension C ((@reducedSupport X
        (@denominatorSectionQuotient X L F s (LocallyOfFiniteType.isLocallyNoetherian f) hL hs
          inferInstance hF hSupp)
        (isCoherent_denominatorSectionQuotient C f L F s hdim hX hF hSupp hL hs)).subschemeι ≫ f)
      ≤ (k : EInt) ∧
    -- (3) `s` restricts to a regular meromorphic section on every component of δ-dimension `k+1`
    (∀ (η : X) (hη : η ∈ genericPoints X),
        relativeDimension C.dimensionFunction f η = k + 1 →
        AlgebraicGeometry.IsRegularMeromorphicSection (integralComponentAt η).subscheme.sheaf
          ((Scheme.Modules.pullback (integralComponentAt η).subschemeι).obj L)
          (componentMeromorphicSection L s hη)) ∧
    -- (4) `[ℱ]_{k+1} = ∑ᵢ mᵢ[Xᵢ]`, over the components of δ-dimension `k + 1`
    (∀ x : X, (cycleAssociatedToCoherentSheaf C f F (k + 1)
          (schemeDeltaDimension_reducedSupport_le_of_schemeDeltaDimension_le C f F hdim)).1 x =
        ∑ᶠ j : topSupportPoints C f F (k + 1), sheafMultiplicity F j.1 *
          (cycleAssociatedToClosedSubscheme C f (integralComponentAt j.1).subschemeι (k + 1)).1
            x) ∧
    -- (4) `[𝒬₂]_k - [𝒬₁]_k = ∑ᵢ mᵢ (Xᵢ ⟶ X)_* div_{ℒ|_{Xᵢ}}(sᵢ)` in `Z_k(X)`
    (∀ x : X,
        (denominatorSectionQuotientCycle C f L F s hdim hX hF hSupp hL hs).1 x -
            (denominatorQuotientCycle C f L F s hdim hX hF hSupp hL hs).1 x =
          ∑ᶠ j : topSupportPoints C f F (k + 1), sheafMultiplicity F j.1 *
            (componentDivisorCycle C f L s hL hs
              (mem_genericPoints_of_relativeDimension_eq C f hdim j.2.2) j.2.2).1 x) ∧
    -- (4) in particular `[𝒬₂]_k - [𝒬₁]_k = c₁(ℒ) ∩ [ℱ]_{k+1}` in `CH_k(X)`
    QuotientAddGroup.mk
        (denominatorSectionQuotientCycle C f L F s hdim hX hF hSupp hL hs -
          denominatorQuotientCycle C f L F s hdim hX hF hSupp hL hs) =
      firstChernClassCapOfInvertible C f k L (cycleAssociatedToCoherentSheaf C f F (k + 1)
        (schemeDeltaDimension_reducedSupport_le_of_schemeDeltaDimension_le C f F hdim))
```

## Tag 02SX, a lemma

[Tag 02SX](https://stacks.math.columbia.edu/tag/02SX) in the Stacks Project.

**`Stacks.Chow.exists_mem_coherentDimensionLayerImage_layerMkTensor_sub`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerTwistCap.lean, line 616](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerTwistCap.lean#L616).

> **[Stacks, Tag 02SX].** Let `(S, δ)` be a Chow situation, let `X` be locally of finite type
> over `S`, let `ℒ` be an invertible `𝒪_X`-module and let `ℱ` be a coherent `𝒪_X`-module with
> `dim_δ(Supp ℱ) ≤ k + 1`. Then the element
>
> `[ℱ ⊗ ℒ] - [ℱ] ∈ K₀(Coh_{≤k+1}(X)/Coh_{≤k-1}(X))`
>
> lies in the subgroup `Bₖ(X)` of [Stacks, Tag 02SC] and maps to `c₁(ℒ) ∩ [ℱ]_{k+1}` under the
> homomorphism `Bₖ(X) ⟶ CH_k(X)` of that tag.
>
> Both clauses are asserted: the membership is the existential witness, and the equation is the
> statement about it. The membership is
> `Stacks.Chow.coherentDimensionKZeroMk_layerMkTensor_sub_mem` and the equation is
> `Stacks.Chow.coherentDimensionLayerImageChowHom_eq_firstChernClassCap`.

```lean
theorem exists_mem_coherentDimensionLayerImage_layerMkTensor_sub
    (C : ChowSituation.{u}) {X : Scheme.{u}} (f : X ⟶ C.S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsCoherent] (L : X.Modules)
    [hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    {k : ℤ}
    (hdim : schemeDeltaDimension C ((reducedSupport F).subschemeι ≫ f) ≤ ((k + 1 : ℤ) : EInt)) :
    ∃ hmem : coherentDimensionKZeroMk C f (k - 1) (k + 1)
            (layerMkTensor C f (k + 1) F L hL hdim) -
          coherentDimensionKZeroMk C f (k - 1) (k + 1) (layerMk C f (k + 1) F hdim) ∈
        coherentDimensionLayerImage C f k,
      coherentDimensionLayerImageChowHom C f k ⟨_, hmem⟩ =
        firstChernClassCapOfInvertible C f k L
          (cycleAssociatedToCoherentSheaf C f F (k + 1) hdim)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.69, Tag 0AYD](https://stacks.math.columbia.edu/tag/0AYD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
