---
declaration: section
origin: cited
lean: AlgebraicGeometry.normalization_of_isLocallyNoetherian_dimension_one, AlgebraicGeometry.Scheme.isBirational_normalization_morphismRestrict, Stacks.AlgebraicGeometry.NormalizationQuotient.existsUnique_linearEquiv_quotient_adicCompletion_normalizationPushforwardStalk, Stacks.AlgebraicGeometry.NormalizationQuotient.normalizationQuotient_iso_coproduct_skyscraperModule, Stacks.AlgebraicGeometry.NormalizationQuotient.normalizationQuotientStalk_linearEquiv_quotient_range, Stacks.AlgebraicGeometry.NormalizationQuotient.length_normalizationQuotientStalk, Stacks.AlgebraicGeometry.NormalizationQuotient.isFiniteLength_normalizationQuotientStalk, Stacks.AlgebraicGeometry.NormalizationQuotientDirectSum.normalizationQuotientIsoCoproductSkyscraper
statement: formalized
proof: formalized
---

# 33.41 Normalization of one dimensional schemes

Section 33.41 of the Stacks Project, [Tag 0C44](https://stacks.math.columbia.edu/tag/0C44). 2 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 9 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C45, a lemma

[Tag 0C45](https://stacks.math.columbia.edu/tag/0C45) in the Stacks Project.

**`AlgebraicGeometry.normalization_of_isLocallyNoetherian_dimension_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationNoetherianDimensionOne.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationNoetherianDimensionOne.lean#L140). References: EGA IV (18.9.7.8), “more general”.

> **Stacks Project, Tag 0C45.** Let `X` be a locally Noetherian scheme of dimension `1` and
> let `ν : X^ν → X` be its normalization. Then
>
> 1. `ν` is integral, surjective, and induces a bijection on irreducible components,
> 2. there is a factorization `X^ν → X_red → X` and the morphism `X^ν → X_red` is the
>    normalization of `X_red`,
> 3. `X^ν → X_red` is birational,
> 4. for every closed point `x ∈ X` the stalk `(ν_* 𝒪_{X^ν})_x` is the integral closure of
>    `𝒪_{X,x}` in the total ring of fractions of `(𝒪_{X,x})_red = 𝒪_{X_red,x}`,
> 5. the fibres of `ν` are finite and the residue field extensions are finite,
> 6. `X^ν` is a disjoint union of integral normal locally Noetherian schemes and each affine open
>    is the spectrum of a finite product of Dedekind domains.

```lean
theorem normalization_of_isLocallyNoetherian_dimension_one (X : Scheme.{u})
    [IsLocallyNoetherian X] (hdim : topologicalKrullDim X = 1) :
    -- (1)
    (IsIntegralHom X.normalizationOfIsLocallyNoetherian ∧
        Surjective X.normalizationOfIsLocallyNoetherian ∧
        Set.BijOn (fun C ↦ closure (X.normalizationOfIsLocallyNoetherian.base '' C))
          (irreducibleComponents X.normalizationSchemeOfIsLocallyNoetherian)
          (irreducibleComponents X)) ∧
      -- (2) and (3)
      (∃ g : X.normalizationSchemeOfIsLocallyNoetherian ⟶ X.nilradical.subscheme,
        g ≫ X.nilradical.subschemeι = X.normalizationOfIsLocallyNoetherian ∧
          IsBirational g ∧
          ∃ e : X.normalizationSchemeOfIsLocallyNoetherian ≅
            X.nilradical.subscheme.normalizationScheme
              (X.finite_irreducibleComponents_reduction
                (finite_irreducibleComponents_of_isCompact X)),
            e.hom ≫ X.nilradical.subscheme.normalization
              (X.finite_irreducibleComponents_reduction
                (finite_irreducibleComponents_of_isCompact X)) = g) ∧
      -- (4)
      (∀ x : X, IsClosed ({x} : Set X) →
        letI := normalizationPushforwardStalkAlgebra X
          (finite_irreducibleComponents_of_isCompact X) x
        letI : Algebra (X.presheaf.stalk x)
            (FractionRing (X.presheaf.stalk x ⧸ nilradical (X.presheaf.stalk x))) :=
          (reductionFractionRingHom (X.presheaf.stalk x)).toAlgebra
        Nonempty (normalizationPushforwardStalk X
              (finite_irreducibleComponents_of_isCompact X) x ≃ₐ[X.presheaf.stalk x]
            integralClosure (X.presheaf.stalk x)
              (FractionRing (X.presheaf.stalk x ⧸ nilradical (X.presheaf.stalk x)))) ∧
          ∀ z : X.nilradical.subscheme, X.nilradical.subschemeι z = x →
            Nonempty ((X.presheaf.stalk x ⧸ nilradical (X.presheaf.stalk x)) ≃+*
              X.nilradical.subscheme.presheaf.stalk z)) ∧
      -- (5)
      ((∀ x : X, (X.normalizationOfIsLocallyNoetherian.base ⁻¹' {x}).Finite) ∧
        ∀ y : X.normalizationSchemeOfIsLocallyNoetherian,
          (X.normalizationOfIsLocallyNoetherian.residueFieldMap y).hom.Finite) ∧
      -- (6)
      ((∃ (ι : Type u) (Y : ι → Scheme.{u}) (_ : ∀ i, IsIntegral (Y i))
          (_ : ∀ i, IsNormal (Y i)) (_ : ∀ i, IsLocallyNoetherian (Y i)),
          Nonempty (X.normalizationSchemeOfIsLocallyNoetherian ≅ ∐ Y)) ∧
        ∀ W : X.normalizationSchemeOfIsLocallyNoetherian.Opens, IsAffineOpen W →
          Stacks.IsFiniteProductOfDedekindDomains
            Γ(X.normalizationSchemeOfIsLocallyNoetherian, W))
```

## Tag 0C1R, a lemma

[Tag 0C1R](https://stacks.math.columbia.edu/tag/0C1R) in the Stacks Project.

**`AlgebraicGeometry.Scheme.isBirational_normalization_morphismRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/RestrictOpen.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/RestrictOpen.lean#L104). The attribute's comment: “finite_normalization”.

> **Stacks Project, Tag 0C1R.** Over every open of a reduced scheme, the normalization
> morphism is birational.

```lean
public theorem isBirational_normalization_morphismRestrict (X : Scheme.{u}) [IsReduced X]
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (V : X.Opens) : IsBirational (X.normalization hX ∣_ V)
```

**`Stacks.AlgebraicGeometry.NormalizationQuotient.existsUnique_linearEquiv_quotient_adicCompletion_normalizationPushforwardStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationQuotient/Completion.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationQuotient/Completion.lean#L138). The attribute's comment: “quotient_completion”.

> **Stacks Project, Tag 0C1R.** Let `X` be a reduced scheme of dimension one with
> normalization `ν`, let `x ∈ X`, write `A = 𝒪_{X,x}` and `A' = (ν_* 𝒪_{X^ν})_x`, and complete at
> the maximal ideal of `A`.  There is exactly one `A`-linear isomorphism `A'/A ≅ A'^∧/A^∧`
> compatible with the canonical maps to the completions.
>
> The closedness of the point assumed in the source is not used; the dimension hypothesis is.

```lean
public theorem existsUnique_linearEquiv_quotient_adicCompletion_normalizationPushforwardStalk
    (X : Scheme.{u}) [IsReduced X] (hNagata : IsNagataScheme X)
    (hdim : topologicalKrullDim X = 1)
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) (x : X) :
    letI : Algebra (X.presheaf.stalk x) (normalizationPushforwardStalk X hX x) :=
      normalizationPushforwardStalkAlgebra X hX x
    ∃! e :
        (normalizationPushforwardStalk X hX x ⧸
            LinearMap.range (Algebra.linearMap (X.presheaf.stalk x)
              (normalizationPushforwardStalk X hX x))) ≃ₗ[X.presheaf.stalk x]
          (AdicCompletion (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
              (normalizationPushforwardStalk X hX x) ⧸
            LinearMap.range (AdicCompletion.map
              (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
              (Algebra.linearMap (X.presheaf.stalk x)
                (normalizationPushforwardStalk X hX x)))),
      ∀ a : normalizationPushforwardStalk X hX x,
        e (Submodule.mkQ _ a) = Submodule.mkQ _
          (AdicCompletion.of (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
            (normalizationPushforwardStalk X hX x) a)
```

**`Stacks.AlgebraicGeometry.NormalizationQuotient.normalizationQuotient_iso_coproduct_skyscraperModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationQuotient/DirectSum.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationQuotient/DirectSum.lean#L60). The attribute's comment: “quotient_sheaf”.

> **Stacks Project, Tag 0C1R(2).** For a reduced Nagata scheme of dimension one the quotient
> `ν_* 𝒪_{X^ν} / 𝒪_X` is the direct sum of the skyscraper sheaves of its stalks at the singular
> points: the quotient's stalk vanishes at every regular point, and the singular locus is closed
> and discrete.

```lean
public theorem normalizationQuotient_iso_coproduct_skyscraperModule (X : Scheme.{u})
    [IsReduced X] (hX : IsNagataScheme X) (hdim : topologicalKrullDim X = 1) :
    Nonempty
      (normalizationQuotient X (finite_irreducibleComponents_of_isNagataScheme X hX) ≅
        ∐ fun z : singularLocus X =>
          skyscraperModule X z.1
            (normalizationQuotientStalk X
              (finite_irreducibleComponents_of_isNagataScheme X hX) z.1))
```

**`Stacks.AlgebraicGeometry.NormalizationQuotient.normalizationQuotientStalk_linearEquiv_quotient_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationQuotient/StalkLength.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationQuotient/StalkLength.lean#L441). The attribute's comment: “delta_length”.

> **Stacks Project, Tag 0C1R.** The stalk of the normalization quotient `ν_* 𝒪_{X^ν} / 𝒪_X`
> at a point of a reduced scheme is the normalization stalk modulo the image of the local ring.
>
> Neither the Nagata hypothesis, nor the dimension of `X`, nor closedness of the point is
> needed.

```lean
public theorem normalizationQuotientStalk_linearEquiv_quotient_range
    (X : Scheme.{u}) [IsReduced X]
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) (x : X) :
    letI : Algebra (X.presheaf.stalk x) (normalizationPushforwardStalk X hX x) :=
      normalizationPushforwardStalkAlgebra X hX x
    Nonempty (normalizationQuotientStalk X hX x ≃ₗ[X.presheaf.stalk x]
      (normalizationPushforwardStalk X hX x ⧸
        LinearMap.range (Algebra.linearMap (X.presheaf.stalk x)
          (normalizationPushforwardStalk X hX x))))
```

**`Stacks.AlgebraicGeometry.NormalizationQuotient.length_normalizationQuotientStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationQuotient/StalkLength.lean, line 582](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationQuotient/StalkLength.lean#L582). The attribute's comment: “delta_length”.

> **Stacks Project, Tag 0C1R.** The length of the stalk of the normalization quotient is the
> delta invariant of the local ring.
>
> Neither the Nagata hypothesis, nor the dimension of `X`, nor closedness of the point is needed;
> without them both sides may be infinite.

```lean
public theorem length_normalizationQuotientStalk (X : Scheme.{u}) [IsReduced X]
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) (x : X) :
    Module.length (X.presheaf.stalk x) (normalizationQuotientStalk X hX x) =
      Ring.deltaInvariant (X.presheaf.stalk x)
```

**`Stacks.AlgebraicGeometry.NormalizationQuotient.isFiniteLength_normalizationQuotientStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationQuotient/StalkLength.lean, line 625](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationQuotient/StalkLength.lean#L625). The attribute's comment: “delta_length”.

> **Stacks Project, Tag 0C1R.** On a reduced Nagata scheme of dimension one the stalk of the
> normalization quotient has finite length.
>
> Closedness of the point is not needed, and the dimension hypothesis is used only through the
> dimension of the local ring at `x`.

```lean
public theorem isFiniteLength_normalizationQuotientStalk (X : Scheme.{u}) [IsReduced X]
    (hNagata : IsNagataScheme X) (hdim : topologicalKrullDim X = 1)
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) (x : X) :
    IsFiniteLength (X.presheaf.stalk x) (normalizationQuotientStalk X hX x)
```

**`Stacks.AlgebraicGeometry.NormalizationQuotientDirectSum.normalizationQuotientIsoCoproductSkyscraper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationQuotientDirectSum/Basic.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationQuotientDirectSum/Basic.lean#L41). The attribute's comment: “quotient_sheaf”.

> For a reduced Nagata scheme `X` of dimension one, the normalization quotient of `X` is
> isomorphic to the direct sum, over the singular points `x` of `X`, of the skyscraper modules at
> `x` of its stalks.

```lean
public theorem normalizationQuotientIsoCoproductSkyscraper (X : Scheme.{u}) [IsReduced X]
    (hX : IsNagataScheme X) (hdim : topologicalKrullDim X = 1) :
    Nonempty
      (normalizationQuotient X
          (Stacks.AlgebraicGeometry.Normalization.finite_irreducibleComponents_of_isNagataScheme
            X hX) ≅
        ∐ fun x : singularLocus X =>
          skyscraperModule X x.1
            (normalizationQuotientStalk X
              (Stacks.AlgebraicGeometry.Normalization.finite_irreducibleComponents_of_isNagataScheme
                X hX) x.1))
```

**`AlgebraicGeometry.existsUnique_algHom_normalizationPushforwardStalk_fractionRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationStalkAmbient/UniqueEmbedding.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationStalkAmbient/UniqueEmbedding.lean#L108). The attribute's comment: “normalization_stalk”.

> **Stacks Project, Tag 0C1R.** At a point of a reduced scheme the stalk of the pushforward of
> the structure sheaf of the normalization carries exactly one injective algebra map into the total
> ring of fractions of the local ring whose image is the integral closure: the canonical embedding
> of the normalization stalk.
>
> Neither the dimension-one hypothesis nor the closedness of the point is used, and the Nagata
> hypothesis of the source enters only through the finiteness of irreducible components needed to
> form the normalization.

```lean
public theorem existsUnique_algHom_normalizationPushforwardStalk_fractionRing
    (X : Scheme.{u}) [IsReduced X]
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) (x : X) :
    letI : Algebra (X.presheaf.stalk x) (normalizationPushforwardStalk X hX x) :=
      normalizationPushforwardStalkAlgebra X hX x
    ∃! f : normalizationPushforwardStalk X hX x →ₐ[X.presheaf.stalk x]
        FractionRing (X.presheaf.stalk x),
      Function.Injective f ∧
        f.range = integralClosure (X.presheaf.stalk x) (FractionRing (X.presheaf.stalk x))
```

**`AlgebraicGeometry.exists_pi_isDiscreteValuationRing_adicCompletion_normalizationStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationStalkCompletion.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationStalkCompletion.lean#L417). The attribute's comment: “complete_dvr_product”.

> **Stacks Project, Tag 0C1R.** At a point of a reduced Nagata scheme whose local ring has
> dimension one, the completion of the stalk of the pushforward of the structure sheaf of the
> normalization, along the ideal generated by the maximal ideal of the local ring, is a nonempty
> finite product of complete discrete valuation rings.
>
> Neither the dimension of `X` nor the closedness of the point is needed: the dimension
> hypothesis of the source enters only through the dimension of the local ring at `x`.

```lean
public theorem exists_pi_isDiscreteValuationRing_adicCompletion_normalizationStalk
    (X : Scheme.{u}) [IsReduced X] (hNagata : IsNagataScheme X)
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) (x : X)
    (hxdim : ringKrullDim (X.presheaf.stalk x) = 1) :
    letI : Algebra (X.presheaf.stalk x) (normalizationPushforwardStalk X hX x) :=
      normalizationPushforwardStalkAlgebra X hX x
    ∃ (n : ℕ) (D : Fin n → Type u) (_ : ∀ i, CommRing (D i)) (_ : ∀ i, IsDomain (D i))
        (_ : ∀ i, IsDiscreteValuationRing (D i)),
      0 < n ∧ (∀ i, IsAdicComplete (maximalIdeal (D i)) (D i)) ∧
        Nonempty (AdicCompletion
          ((maximalIdeal (X.presheaf.stalk x)).map
            (algebraMap (X.presheaf.stalk x) (normalizationPushforwardStalk X hX x)))
          (normalizationPushforwardStalk X hX x) ≃+* ∀ i, D i)
```

**`AlgebraicGeometry.exists_injective_range_eq_integralClosure_adicCompletion_normalizationStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationStalkCompletion.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationStalkCompletion.lean#L471). The attribute's comment: “normalization_after_completion”. References: EGA IV (7.6.1), “special case”.

> **Stacks Project, Tag 0C1R.** Completing the stalk of the pushforward of the structure sheaf
> of the normalization of a reduced one-dimensional Nagata scheme, along the ideal generated by
> the maximal ideal of the local ring at the point, gives the integral closure of the completed
> local ring in its own total ring of fractions.
>
> The two compatibility equations say that the resulting embedding extends the structure map of
> the completed local ring and the given embedding `f₀` of the normalization stalk; the embedding
> `f₀` exists and is unique by
> `existsUnique_algHom_normalizationPushforwardStalk_fractionRing`.
>
> Closedness of the point is not needed.  The points whose local ring is zero-dimensional are
> covered: there the local ring is a field and both completions are trivial.

```lean
public theorem exists_injective_range_eq_integralClosure_adicCompletion_normalizationStalk
    (X : Scheme.{u}) [IsReduced X] (hNagata : IsNagataScheme X)
    (hdim : topologicalKrullDim X = 1)
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) (x : X) :
    letI : Algebra (X.presheaf.stalk x) (normalizationPushforwardStalk X hX x) :=
      normalizationPushforwardStalkAlgebra X hX x
    let A := X.presheaf.stalk x
    let A' := normalizationPushforwardStalk X hX x
    let Ac := AdicCompletion (maximalIdeal A) A
    let J := (maximalIdeal A).map (algebraMap A A')
    let C := AdicCompletion J A'
    let k : Ac →+* C := adicCompletionMap (algebraMap A A') (maximalIdeal A) J le_rfl
    ∀ f₀ : A' →ₐ[A] FractionRing A, Function.Injective f₀ →
      f₀.range = integralClosure A (FractionRing A) →
      ∃ q : FractionRing A →+* FractionRing Ac,
        (∀ a : A, q (algebraMap A (FractionRing A) a) =
          algebraMap Ac (FractionRing Ac) (algebraMap A Ac a)) ∧
        ∃ g : C →+* FractionRing Ac,
          Function.Injective g ∧
          g.range = (integralClosure Ac (FractionRing Ac)).toSubring ∧
          (∀ y : Ac, g (k y) = algebraMap Ac (FractionRing Ac) y) ∧
          (∀ a' : A', g (algebraMap A' C a') = q (f₀ a'))
```

**`AlgebraicGeometry.Scheme.isFinite_surjective_isBirational_normalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/PrepareDeltaInvariant.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/PrepareDeltaInvariant.lean#L85). The attribute's comment: “part (1): ν is finite, surjective and birational”. References: EGA II (6.3.8), “special case”.

> **Stacks Project, Tag 0C1R, part (1).** The normalization `ν : X^ν ⟶ X` of a reduced Nagata
> scheme is finite, surjective and birational.
>
> The dimension of `X` is not used.

```lean
public theorem isFinite_surjective_isBirational_normalization (X : Scheme.{u}) [IsReduced X]
    (hX : IsNagataScheme X) :
    IsFinite (X.normalization (finite_irreducibleComponents_of_isNagataScheme X hX)) ∧
      Surjective (X.normalization (finite_irreducibleComponents_of_isNagataScheme X hX)) ∧
      IsBirational (X.normalization (finite_irreducibleComponents_of_isNagataScheme X hX))
```

**`AlgebraicGeometry.normalizationQuotient_mono_iso_coproduct_skyscraperModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/PrepareDeltaInvariant.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/PrepareDeltaInvariant.lean#L120). The attribute's comment: “part (2): O_X ⊂ ν_*O, the quotient a sum of skyscrapers Q_x at singular points”.

> **Stacks Project, Tag 0C1R, part (2).** For a reduced Nagata scheme `X` of dimension one,
> `𝒪_X ⊂ ν_* 𝒪_{X^ν}` — the map is a monomorphism both of sheaves of rings and of `𝒪_X`-modules —
> and the quotient `ν_* 𝒪_{X^ν} / 𝒪_X` is the direct sum, over the singular points `x` of `X`, of
> the skyscraper sheaves at `x` with value `𝒬_x`, the stalk of the quotient at `x`; that stalk is
> nonzero exactly at the singular points.

```lean
public theorem normalizationQuotient_mono_iso_coproduct_skyscraperModule (X : Scheme.{u})
    [IsReduced X] (hX : IsNagataScheme X) (hdim : topologicalKrullDim X = 1) :
    Mono (Scheme.Hom.toRingCatSheafHom
        (X.normalization (finite_irreducibleComponents_of_isNagataScheme X hX))) ∧
      Mono (normalizationModuleMap X (finite_irreducibleComponents_of_isNagataScheme X hX)) ∧
      Nonempty
        (normalizationQuotient X (finite_irreducibleComponents_of_isNagataScheme X hX) ≅
          ∐ fun z : singularLocus X =>
            skyscraperModule X z.1
              (normalizationQuotientStalk X
                (finite_irreducibleComponents_of_isNagataScheme X hX) z.1)) ∧
      ∀ x : X, ¬ IsZero (normalizationQuotientStalk X
          (finite_irreducibleComponents_of_isNagataScheme X hX) x) ↔ x ∈ singularLocus X
```

**`AlgebraicGeometry.normalizationQuotientStalk_finiteLength_eq_deltaInvariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/PrepareDeltaInvariant.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/PrepareDeltaInvariant.lean#L144). The attribute's comment: “part (4): Q_x = A'/A has finite length equal to the δ-invariant”.

> **Stacks Project, Tag 0C1R, part (4).** On a reduced Nagata scheme of dimension one, the
> stalk `𝒬_x` of `ν_* 𝒪_{X^ν} / 𝒪_X` at `x` is `A' / A`, where `A = 𝒪_{X,x}` and
> `A' = (ν_* 𝒪_{X^ν})_x`; it has finite length over `A`, and that length is the `δ`-invariant of
> `X` at `x`.

```lean
public theorem normalizationQuotientStalk_finiteLength_eq_deltaInvariant (X : Scheme.{u})
    [IsReduced X] (hX : IsNagataScheme X) (hdim : topologicalKrullDim X = 1) (x : X) :
    letI : Algebra (X.presheaf.stalk x)
        (normalizationPushforwardStalk X (finite_irreducibleComponents_of_isNagataScheme X hX) x) :=
      normalizationPushforwardStalkAlgebra X _ x
    Nonempty (normalizationQuotientStalk X (finite_irreducibleComponents_of_isNagataScheme X hX) x
        ≃ₗ[X.presheaf.stalk x]
        (normalizationPushforwardStalk X (finite_irreducibleComponents_of_isNagataScheme X hX) x ⧸
          LinearMap.range (Algebra.linearMap (X.presheaf.stalk x)
            (normalizationPushforwardStalk X
              (finite_irreducibleComponents_of_isNagataScheme X hX) x)))) ∧
      IsFiniteLength (X.presheaf.stalk x)
        (normalizationQuotientStalk X (finite_irreducibleComponents_of_isNagataScheme X hX) x) ∧
      Module.length (X.presheaf.stalk x)
          (normalizationQuotientStalk X (finite_irreducibleComponents_of_isNagataScheme X hX) x) =
        Ring.deltaInvariant (X.presheaf.stalk x)
```

**`AlgebraicGeometry.normalizationPushforwardStalk_semilocal_finiteProductOfDedekindDomains`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/PrepareDeltaInvariant.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/PrepareDeltaInvariant.lean#L170). The attribute's comment: “part (5): A' is semi-local and a finite product of Dedekind domains”.

> **Stacks Project, Tag 0C1R, part (5).** On a Nagata scheme of dimension one, the stalk
> `A' = (ν_* 𝒪_{X^ν})_x` is a semi-local ring — it has finitely many maximal ideals — which is a
> finite product of Dedekind domains.
>
> Reducedness of `X` is not used.

```lean
public theorem normalizationPushforwardStalk_semilocal_finiteProductOfDedekindDomains
    (X : Scheme.{u}) (hX : IsNagataScheme X) (hdim : topologicalKrullDim X = 1) (x : X) :
    Finite (MaximalSpectrum
        (normalizationPushforwardStalk X (finite_irreducibleComponents_of_isNagataScheme X hX) x)) ∧
      IsDiscreteValuationRing.IsFiniteProductOfDedekindDomains
        (normalizationPushforwardStalk X (finite_irreducibleComponents_of_isNagataScheme X hX) x)
```

**`AlgebraicGeometry.adicCompletion_stalk_reduced_noetherian_complete_local_dim_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/PrepareDeltaInvariant.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/PrepareDeltaInvariant.lean#L188). The attribute's comment: “part (6): A^ is reduced Noetherian complete local of dimension 1 (dim A = 1)”. References: EGA IV (7.3.19), “dim(Â)=1”.

> **Stacks Project, Tag 0C1R, part (6)**, at a point whose local ring has dimension one. For a
> reduced Nagata scheme `X` and a point `x` with `dim 𝒪_{X,x} = 1`, the completion `A^∧` of
> `A = 𝒪_{X,x}` at its maximal ideal is a reduced Noetherian complete local ring of dimension one.
>
> The hypothesis on `dim 𝒪_{X,x}` corrects the source: at a closed point of a one-dimensional scheme
> whose local ring is a field (an isolated point), `A^∧ = A` has dimension zero.  Everything except
> the dimension holds without it.

```lean
public theorem adicCompletion_stalk_reduced_noetherian_complete_local_dim_one (X : Scheme.{u})
    [IsReduced X] (hX : IsNagataScheme X) (x : X)
    (hxdim : ringKrullDim (X.presheaf.stalk x) = 1) :
    _root_.IsReduced (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) ∧
      IsNoetherianRing (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) ∧
      ∃ _ : IsLocalRing
          (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)),
        IsAdicComplete
            (maximalIdeal
              (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)))
            (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) ∧
          ringKrullDim
              (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) = 1
```

**`AlgebraicGeometry.adicCompletion_stalk_reduced_noetherian_complete_local_ringKrullDim_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/PrepareDeltaInvariant.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/PrepareDeltaInvariant.lean#L218). The attribute's comment: “part (6) at every point: A^ reduced Noetherian complete local, dim A^ = dim A ≤ 1”. References: EGA IV (7.3.19), “dim(Â)=1”.

> **Stacks Project, Tag 0C1R, part (6)**, at every point. Let `X` be a reduced Nagata scheme of
> dimension one, `x ∈ X` and `A = 𝒪_{X,x}`.  The completion `A^∧` of `A` at its maximal ideal is a
> reduced Noetherian complete local ring with `dim A^∧ = dim A`; moreover `dim A ≤ 1`, with
> `dim A = 1` exactly when `A` is not a field.  So the source's "of dimension 1" is precisely the
> case `dim A = 1`, the one `adicCompletion_stalk_reduced_noetherian_complete_local_dim_one` states.
>
> Part (6) as printed fails when `A` is a field, which happens at an isolated point: the scheme
> `X = Spec (k × k[t])` is reduced, Nagata and of dimension one, its point `Spec k` is closed, and
> there `A = A^∧ = k` has dimension zero.  Neither closedness of `x` nor any hypothesis on `dim A` is
> used.

```lean
public theorem adicCompletion_stalk_reduced_noetherian_complete_local_ringKrullDim_eq
    (X : Scheme.{u}) [IsReduced X] (hX : IsNagataScheme X) (hdim : topologicalKrullDim X = 1)
    (x : X) :
    _root_.IsReduced (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) ∧
      IsNoetherianRing (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) ∧
      (∃ _ : IsLocalRing
          (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)),
        IsAdicComplete
            (maximalIdeal
              (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)))
            (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) ∧
          ringKrullDim
              (AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)) =
            ringKrullDim (X.presheaf.stalk x)) ∧
      ringKrullDim (X.presheaf.stalk x) ≤ 1 ∧
      (ringKrullDim (X.presheaf.stalk x) = 1 ↔ ¬ IsField (X.presheaf.stalk x))
```

**`AlgebraicGeometry.exists_injective_range_eq_integralClosure_adicCompletion_normalizationStalk_of_isNagataScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/PrepareDeltaInvariant.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/PrepareDeltaInvariant.lean#L266). The attribute's comment: “part (7): (A')^ is the integral closure of A^ in its total ring of fractions”.

> **Stacks Project, Tag 0C1R, part (7).** Let `X` be a reduced Nagata scheme of dimension one,
> `A = 𝒪_{X,x}` and `A' = (ν_* 𝒪_{X^ν})_x`.  The completion `(A')^∧` of `A'` along `𝔪_A A'` is the
> integral closure of `A^∧` in its total ring of fractions: there is an injective ring map
> `(A')^∧ → Frac(A^∧)` extending the structure map of `A^∧`, whose image is the integral closure of
> `A^∧` in `Frac(A^∧)`.
>
> Closedness of the point is not needed.

```lean
public theorem
    exists_injective_range_eq_integralClosure_adicCompletion_normalizationStalk_of_isNagataScheme
    (X : Scheme.{u}) [IsReduced X] (hX : IsNagataScheme X) (hdim : topologicalKrullDim X = 1)
    (x : X) :
    letI : Algebra (X.presheaf.stalk x)
        (normalizationPushforwardStalk X (finite_irreducibleComponents_of_isNagataScheme X hX) x) :=
      normalizationPushforwardStalkAlgebra X _ x
    let A := X.presheaf.stalk x
    let A' :=
      normalizationPushforwardStalk X (finite_irreducibleComponents_of_isNagataScheme X hX) x
    let Ac := AdicCompletion (maximalIdeal A) A
    let J := (maximalIdeal A).map (algebraMap A A')
    let C := AdicCompletion J A'
    let k : Ac →+* C := adicCompletionMap (algebraMap A A') (maximalIdeal A) J le_rfl
    ∃ g : C →+* FractionRing Ac,
      Function.Injective g ∧
        g.range = (integralClosure Ac (FractionRing Ac)).toSubring ∧
        ∀ y : Ac, g (k y) = algebraMap Ac (FractionRing Ac) y
```

**`AlgebraicGeometry.finite_maximalSpectrum_normalizationPushforwardStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/SemilocalDedekind.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/SemilocalDedekind.lean#L151). The attribute's comment: “semilocal_dedekind”.

> **Stacks Project, Tag 0C1R.** The stalk of the pushforward of the structure sheaf of the
> normalization of a Nagata scheme is semilocal: it has finitely many maximal ideals.
>
> The point is not assumed closed, and the dimension hypothesis of the source is not used.

```lean
public theorem finite_maximalSpectrum_normalizationPushforwardStalk
    (X : Scheme.{u}) (hNagata : IsNagataScheme X)
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) (x : X) :
    letI : Algebra (X.presheaf.stalk x) (normalizationPushforwardStalk X hX x) :=
      normalizationPushforwardStalkAlgebra X hX x
    Finite (MaximalSpectrum (normalizationPushforwardStalk X hX x))
```

**`AlgebraicGeometry.isFiniteProductOfDedekindDomains_normalizationPushforwardStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/SemilocalDedekind.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/SemilocalDedekind.lean#L174). The attribute's comment: “semilocal_dedekind”.

> **Stacks Project, Tag 0C1R.** On a Nagata scheme of dimension one, the stalk of the
> pushforward of the structure sheaf of the normalization is a finite product of Dedekind
> domains.
>
> The point is not assumed closed.

```lean
public theorem isFiniteProductOfDedekindDomains_normalizationPushforwardStalk
    (X : Scheme.{u}) (hNagata : IsNagataScheme X) (hdim : topologicalKrullDim X = 1)
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) (x : X) :
    IsDiscreteValuationRing.IsFiniteProductOfDedekindDomains
      (normalizationPushforwardStalk X hX x)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.isFinite_normalization`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataNormalization/Basic.lean#L233), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/RestrictOpen.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/RestrictOpen.lean#L113) (StacksFrontier): “finite_normalization”.
- [`AlgebraicGeometry.Scheme.surjective_normalization`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/UniversalHomeomorphism.lean#L75), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/RestrictOpen.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/RestrictOpen.lean#L114) (StacksFrontier): “finite_normalization”.
- [`Stacks.AlgebraicGeometry.Normalization.mono_toRingCatSheafHom_normalization`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationMono/Basic.lean#L127), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/NormalizationQuotient/DirectSum.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationQuotient/DirectSum.lean#L77) (StacksFrontier): “quotient_sheaf”.
- [`normalizationQuotientStalk_nonzero_iff_mem_singularLocus`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=normalizationQuotientStalk_nonzero_iff_mem_singularLocus#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/NormalizationQuotient/DirectSum.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormalizationQuotient/DirectSum.lean#L80) (StacksFrontier): “quotient_sheaf”.
- [`AdicCompletion.isNoetherianRing`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AdicCompletion/NoetherianRing/PowerSeriesSurjection.lean#L236), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean#L44) (StacksFrontier): “completed_local_ring”.
- [`AdicCompletion.isLocalRing_of_fg`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AdicCompletion.isLocalRing_of_fg#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean#L45) (StacksFrontier): “completed_local_ring”. References: EGA IV (8.11.4), “Â is a local ring”; SGA 3 VIIB (0.1.1), “special case”; SGA 3 X (4.0), “partial”.
- [`AdicCompletion.isAdicComplete_of_fg`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AdicCompletion.isAdicComplete_of_fg#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean#L46) (StacksFrontier): “completed_local_ring”. References: EGA 0 (7.2.12), “special case”.
- [`IsLocalRing.isReduced_adicCompletion_maximalIdeal_of_isNagataRing`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean#L55), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean#L77) (StacksFrontier): “completed_local_ring”.
- [`IsLocalRing.ringKrullDim_adicCompletion_maximalIdeal`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean#L70), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean#L79) (StacksFrontier): “completed_local_ring”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.41, Tag 0C44](https://stacks.math.columbia.edu/tag/0C44)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
