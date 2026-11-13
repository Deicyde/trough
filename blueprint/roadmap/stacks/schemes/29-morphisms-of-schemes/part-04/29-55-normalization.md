---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.exists_totalQuotientSheaf_iso_pushforward, AlgebraicGeometry.Scheme.quasiCompactFromGenericPointResidueFields, AlgebraicGeometry.Scheme.quasiSeparatedFromGenericPointResidueFields, Stacks.AlgebraicGeometry.GenericPointProduct.finiteComponentsOnCompactOpens_of_isLocallyNoetherian, AlgebraicGeometry.Scheme.existsUnique_iso_normalizationScheme_reduction, AlgebraicGeometry.Scheme.normalizationIsoMeromorphicSpectrum_hom_toBase, AlgebraicGeometry.Scheme.genericPointResidueSpectrum, AlgebraicGeometry.Scheme.fromGenericPointResidueFields
statement: formalized
proof: formalized
---

# 29.55 Normalization

Section 29.55 of the Stacks Project, [Tag 035E](https://stacks.math.columbia.edu/tag/035E). 14 tags here are carried by 28 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 035E, the section

[Tag 035E](https://stacks.math.columbia.edu/tag/035E) in the Stacks Project.

**`AlgebraicGeometry.Scheme.exists_totalQuotientSheaf_iso_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicPushforward.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicPushforward.lean#L178). The attribute's comment: “K\_X = f\_* O\_Y for X reduced”. References: EGA II (6.3.6), “special case”.

> Let `X` be a reduced scheme whose quasi-compact opens have finitely many irreducible
> components, and let `f : Y ⟶ X` be the canonical morphism from the coproduct of the spectra of the
> residue fields at the generic points of `X`. Then the sheaf of meromorphic functions of `X` is
> `f_* 𝒪_Y`, as a sheaf of `𝒪_X`-algebras.

```lean
theorem exists_totalQuotientSheaf_iso_pushforward [IsReduced X]
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    ∃ e : X.totalQuotientSheaf.presheaf ≅
        (fromGenericPointResidueFields X).base _* (genericPointResidueSpectrum X).presheaf,
      X.toTotalQuotientSheaf.hom ≫ e.hom = (fromGenericPointResidueFields X).c
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.quasiCompactFromGenericPointResidueFields`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Scheme.lean#L65), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicPushforward.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicPushforward.lean#L189) (StacksFrontier): “the morphism (035M) is quasi-compact”.
- [`AlgebraicGeometry.Scheme.quasiSeparatedFromGenericPointResidueFields`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Scheme.lean#L86), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicPushforward.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicPushforward.lean#L191) (StacksFrontier): “the morphism (035M) is quasi-separated”.
- [`Stacks.AlgebraicGeometry.GenericPointProduct.finiteComponentsOnCompactOpens_of_isLocallyNoetherian`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GenericPointProduct/Decomposition.lean#L73), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicPushforward.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicPushforward.lean#L193) (StacksFrontier): “a locally Noetherian scheme has locally finitely many irreducible components”.
- [`AlgebraicGeometry.Scheme.existsUnique_iso_normalizationScheme_reduction`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Reduction.lean#L293), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicPushforward.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicPushforward.lean#L195) (StacksFrontier): “the normalization of X is the normalization of X\_red”.
- [`AlgebraicGeometry.Scheme.normalizationIsoMeromorphicSpectrum_hom_toBase`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicRelativeSpec.lean#L417), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicPushforward.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/MeromorphicPushforward.lean#L197) (StacksFrontier): “for X reduced, the normalization is the relative spectrum of the integral closure of O\_X in K\_X”.

## Tag 035M, an equation

[Tag 035M](https://stacks.math.columbia.edu/tag/035M) in the Stacks Project.

**`AlgebraicGeometry.Scheme.genericPointResidueSpectrum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/GenericPoints.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/GenericPoints.lean#L73). The attribute's comment: “the source scheme”.

> **Stacks Project, Tag 035M.** The coproduct of the spectra of the residue fields at the
> generic points of the irreducible components of `X`.

```lean
noncomputable def genericPointResidueSpectrum (X : Scheme.{u}) : Scheme.{u}
```

**`AlgebraicGeometry.Scheme.fromGenericPointResidueFields`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/GenericPoints.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/GenericPoints.lean#L79). The attribute's comment: “the morphism”.

> **Stacks Project, Tag 035M.** The canonical morphism from the spectra of the residue fields
> at the generic points of `X` to `X`.

```lean
noncomputable def fromGenericPointResidueFields (X : Scheme.{u}) :
    genericPointResidueSpectrum X ⟶ X
```

## Tag 035N, a definition

[Tag 035N](https://stacks.math.columbia.edu/tag/035N) in the Stacks Project.

**`AlgebraicGeometry.Scheme.normalization`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Scheme.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Scheme.lean#L118). References: EGA II (7.4.6), “special case”.

> **Stacks Project, Tag 035N.** The normalization morphism of a scheme whose quasi-compact
> opens have finitely many irreducible components.

```lean
noncomputable abbrev normalization (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    normalizationScheme X hX ⟶ X
```

## Tag 035O, a lemma

[Tag 035O](https://stacks.math.columbia.edu/tag/035O) in the Stacks Project.

**`AlgebraicGeometry.Scheme.normalizationToReduction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Reduction.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Reduction.lean#L160). The attribute's comment: “canonical factor”.

> **Stacks Project, Tag 035O.** The canonical factor of the normalization morphism of `X`
> through the reduction of `X`.

```lean
noncomputable def normalizationToReduction (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    X.normalizationScheme hX ⟶ X.nilradical.subscheme
```

**`AlgebraicGeometry.Scheme.normalizationToReduction_subschemeι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Reduction.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Reduction.lean#L169). The attribute's comment: “factorization”.

> **Stacks Project, Tag 035O.** The normalization morphism of `X` is the composite of its
> canonical factor through the reduction with the closed immersion of the reduction.

```lean
theorem normalizationToReduction_subschemeι (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    X.normalizationToReduction hX ≫ X.nilradical.subschemeι = X.normalization hX
```

**`AlgebraicGeometry.Scheme.existsUnique_iso_normalizationScheme_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Reduction.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Reduction.lean#L293). The attribute's comment: “an iso over the reduction with the normalization of the reduction”.

> **Stacks Project, Tag 035O.** The normalization of `X` is the normalization of the reduction
> of `X`: the canonical factor of the normalization morphism of `X` through the reduction is
> uniquely isomorphic, over the reduction, to the normalization morphism of the reduction,
> compatibly with the morphisms from the generic-point residue spectra.

```lean
theorem existsUnique_iso_normalizationScheme_reduction (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    ∃! e : X.normalizationScheme hX ≅
        X.nilradical.subscheme.normalizationScheme
          (X.finite_irreducibleComponents_reduction hX),
      (X.genericPointResidueSpectrumReductionIso.hom ≫ X.toNormalizationScheme hX) ≫ e.hom =
          X.nilradical.subscheme.toNormalizationScheme
            (X.finite_irreducibleComponents_reduction hX) ∧
        e.hom ≫ X.nilradical.subscheme.normalization
            (X.finite_irreducibleComponents_reduction hX) =
          X.normalizationToReduction hX
```

**`AlgebraicGeometry.Scheme.normalizationReductionIso_hom_normalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Reduction.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Reduction.lean#L353). The attribute's comment: “the iso of X^nu with (X\_red)^nu is over X\_red”.

> **Stacks Project, Tag 035O.** The isomorphism of the normalization of `X` with the
> normalization of the reduction of `X` is an isomorphism over the reduction: it carries the
> normalization morphism of the reduction to the canonical factor of the normalization morphism of
> `X` through the reduction.

```lean
theorem normalizationReductionIso_hom_normalization (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    (X.normalizationReductionIso hX).hom ≫
        X.nilradical.subscheme.normalization
          (X.finite_irreducibleComponents_reduction hX) =
      X.normalizationToReduction hX
```

## Tag 035P, a lemma

[Tag 035P](https://stacks.math.columbia.edu/tag/035P) in the Stacks Project.

**`AlgebraicGeometry.preimageNormalizationIsoSpecIntegralClosure_hom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Affine.lean, line 707](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Affine.lean#L707). The attribute's comment: “affine\_normalization”.

> Under `AlgebraicGeometry.preimageNormalizationIsoSpecIntegralClosure`, the restriction of the
> normalization morphism is the spectrum map induced by the inclusion into the integral closure.

```lean
theorem preimageNormalizationIsoSpecIntegralClosure_hom_comp
    {X : Scheme.{u}} [IsReduced X]
    (hX : ∀ V : X.Opens,
      IsCompact (V : Set X) → (irreducibleComponents V).Finite)
    {A : Type u} [CommRing A] (U : X.Opens)
    (e : Spec (.of A) ≅ U.toScheme) :
    (preimageNormalizationIsoSpecIntegralClosure hX U e).hom ≫
        Spec.map (CommRingCat.ofHom
          (algebraMap A (integralClosure A (FractionRing A)))) =
      (Scheme.normalization X hX ∣_ U) ≫ e.inv
```

**`AlgebraicGeometry.finite_minimalPrimes_of_affine_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/TotalFractionRing.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/TotalFractionRing.lean#L64). The attribute's comment: “minimal\_primes”.

> If every quasi-compact open of a scheme has finitely many irreducible components,
> then a ring presenting an affine open of that scheme has finitely many minimal primes.

```lean
theorem finite_minimalPrimes_of_affine_open
    {X : Scheme.{u}}
    {A : Type u} [CommRing A]
    (hX : ∀ (V : X.Opens), IsCompact (V : Set X) → (irreducibleComponents V).Finite)
    (U : X.Opens) (e : Spec (.of A) ≅ (U : Scheme)) :
    (minimalPrimes A).Finite
```

**`minimalPrimes.totalFractionRing_algEquiv_pi_fractionRing_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/TotalFractionRing.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/TotalFractionRing.lean#L136). The attribute's comment: “total\_fraction\_ring”. References: EGA II (6.5.1), “partial”.

> The total ring of fractions of a reduced ring with finitely many minimal primes is the
> product of the fraction fields of its minimal-prime quotients.

```lean
theorem totalFractionRing_algEquiv_pi_fractionRing_quotient
    {A : Type*} [CommRing A] [IsReduced A] (hA : (minimalPrimes A).Finite) :
    letI : (p : minimalPrimes A) → Algebra A (FractionRing (A ⧸ (p : Ideal A))) :=
      fun p => ((algebraMap (A ⧸ (p : Ideal A)) (FractionRing (A ⧸ (p : Ideal A)))).comp
        (Ideal.Quotient.mk (p : Ideal A))).toAlgebra
    Nonempty (FractionRing A ≃ₐ[A]
      (∀ p : minimalPrimes A, FractionRing (A ⧸ (p : Ideal A))))
```

**`minimalPrimes.integralClosure_fractionRing_algEquiv_pi_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/TotalFractionRing.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/TotalFractionRing.lean#L208). The attribute's comment: “integral\_closure\_product”. References: EGA II (6.4.7), “integral closure product”.

> The integral closure of a reduced ring in its total fraction ring is the product of the
> integral closures of its minimal-prime quotients in their fraction fields.

```lean
theorem integralClosure_fractionRing_algEquiv_pi_quotient
    {A : Type*} [CommRing A] [IsReduced A] (hA : (minimalPrimes A).Finite) :
    letI : (p : minimalPrimes A) →
        Algebra A
          (integralClosure (A ⧸ (p : Ideal A)) (FractionRing (A ⧸ (p : Ideal A)))) :=
      fun p =>
        ((algebraMap (A ⧸ (p : Ideal A))
          (integralClosure (A ⧸ (p : Ideal A))
            (FractionRing (A ⧸ (p : Ideal A))))).comp
          (Ideal.Quotient.mk (p : Ideal A))).toAlgebra
    Nonempty
      (integralClosure A (FractionRing A) ≃ₐ[A]
        (∀ p : minimalPrimes A,
          integralClosure (A ⧸ (p : Ideal A)) (FractionRing (A ⧸ (p : Ideal A)))))
```

## Tag 0C3B, a lemma

[Tag 0C3B](https://stacks.math.columbia.edu/tag/0C3B) in the Stacks Project.

**`Stacks.NormalizationStalkAmbient.normalizationStalkAlgEquivIntegralClosureMinimalPrimes`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MinimalPrimeResidueLocalization/Stalk.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MinimalPrimeResidueLocalization/Stalk.lean#L87). The attribute's comment: “the product of the minimal-prime residue fields”.

> The stalk of the pushforward of the structure sheaf of the normalization is canonically
> isomorphic, as an `𝒪_{X,x}`-algebra, to the integral closure of `𝒪_{X,x}` in the product of the
> residue fields of its minimal primes.

```lean
public noncomputable def
    normalizationStalkAlgEquivIntegralClosureMinimalPrimes (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) :
    letI : Algebra (X.presheaf.stalk x) (normalizationPushforwardStalk X hX x) :=
      normalizationPushforwardStalkAlgebra X hX x
    letI : Algebra (X.presheaf.stalk x)
        (minimalPrimeResidueFieldProduct (X.presheaf.stalk x)) :=
      (minimalPrimeResidueFieldProductHom (X.presheaf.stalk x)).toAlgebra
    normalizationPushforwardStalk X hX x ≃ₐ[X.presheaf.stalk x]
      integralClosure (X.presheaf.stalk x)
        (minimalPrimeResidueFieldProduct (X.presheaf.stalk x))
```

**`Stacks.NormalizationStalkAmbient.normalizationStalkAlgEquivIntegralClosureFractionRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MinimalPrimeResidueLocalization/Stalk.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MinimalPrimeResidueLocalization/Stalk.lean#L106). The attribute's comment: “the total ring of fractions of the reduction”.

> The stalk of the pushforward of the structure sheaf of the normalization is canonically
> isomorphic, as an `𝒪_{X,x}`-algebra, to the integral closure of `𝒪_{X,x}` in the total ring of
> fractions of its reduction.

```lean
public noncomputable def
    normalizationStalkAlgEquivIntegralClosureFractionRing (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) :
    letI : Algebra (X.presheaf.stalk x) (normalizationPushforwardStalk X hX x) :=
      normalizationPushforwardStalkAlgebra X hX x
    letI : Algebra (X.presheaf.stalk x)
        (FractionRing (X.presheaf.stalk x ⧸ nilradical (X.presheaf.stalk x))) :=
      (reductionFractionRingHom (X.presheaf.stalk x)).toAlgebra
    normalizationPushforwardStalk X hX x ≃ₐ[X.presheaf.stalk x]
      integralClosure (X.presheaf.stalk x)
        (FractionRing (X.presheaf.stalk x ⧸ nilradical (X.presheaf.stalk x)))
```

**`AlgebraicGeometry.Scheme.normalizationPushforwardStalkEquivIntegralClosureReductionFractionRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Stalk.lean, line 618](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Stalk.lean#L618). The attribute's comment: “the total ring of fractions of the reduction”.

> The stalk of the pushforward of the structure sheaf of the normalization is canonically
> isomorphic, as an `𝒪_{X,x}`-algebra, to the integral closure of `𝒪_{X,x}` in the total ring of
> fractions of its reduction.

```lean
public noncomputable def
    normalizationPushforwardStalkEquivIntegralClosureReductionFractionRing
    (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) :
    let A := X.presheaf.stalk x
    letI : Algebra A (normalizationPushforwardStalk X hX x) :=
      normalizationPushforwardStalkAlgebra X hX x
    letI : Algebra A (FractionRing (A ⧸ _root_.nilradical A)) :=
      (Stacks.NormalizationStalkAmbient.reductionFractionRingHom A).toAlgebra
    normalizationPushforwardStalk X hX x ≃ₐ[A]
      integralClosure A (FractionRing (A ⧸ _root_.nilradical A))
```

**`AlgebraicGeometry.Scheme.normalizationPushforwardStalkEquivIntegralClosureMinimalPrimeResidueFields`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Stalk.lean, line 698](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Stalk.lean#L698). The attribute's comment: “the product of the minimal-prime residue fields”.

> The stalk of the pushforward of the structure sheaf of the normalization is canonically
> isomorphic, as an `𝒪_{X,x}`-algebra, to the integral closure of `𝒪_{X,x}` in the product of the
> residue fields of its minimal primes.

```lean
public noncomputable def
    normalizationPushforwardStalkEquivIntegralClosureMinimalPrimeResidueFields
    (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) :
    let A := X.presheaf.stalk x
    letI (p : minimalPrimes A) : p.1.IsPrime := p.2.1.1
    letI : Algebra A (normalizationPushforwardStalk X hX x) :=
      normalizationPushforwardStalkAlgebra X hX x
    letI : Algebra A (minimalPrimes.residueFieldProduct A) :=
      (minimalPrimes.residueFieldProductHom A).toAlgebra
    normalizationPushforwardStalk X hX x ≃ₐ[A]
      integralClosure A (minimalPrimes.residueFieldProduct A)
```

**`Stacks.StalkMinimalPrimes.Basic.finite_minimalPrimes_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StalkMinimalPrimes/Basic.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/StalkMinimalPrimes/Basic.lean#L60). The attribute's comment: “finiteness of the minimal primes”.

> If every quasi-compact open of `X` has finitely many irreducible components, the local
> ring of `X` at `x` has only finitely many minimal primes.

```lean
public theorem finite_minimalPrimes_stalk (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) : (minimalPrimes (X.presheaf.stalk x)).Finite
```

## Tag 035Q, a lemma

[Tag 035Q](https://stacks.math.columbia.edu/tag/035Q) in the Stacks Project.

**`AlgebraicGeometry.Scheme.exists_iso_sigma_isIntegral_isNormal_normalizationScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Components.lean, line 510](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Components.lean#L510). The attribute's comment: “normalization\_disjoint\_union\_of\_integral\_normal”.

> **Stacks Project, Tag 035Q.** The normalization of a scheme whose quasi-compact opens have
> finitely many irreducible components is a disjoint union of integral normal schemes: it is
> isomorphic to the coproduct of the normalizations of its reduced irreducible components, and
> each of those is integral and normal.

```lean
theorem exists_iso_sigma_isIntegral_isNormal_normalizationScheme
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    ∃ (ι : Type u) (Y : ι → Scheme.{u})
        (_ : ∀ i, IsNormal (Y i)) (_ : ∀ i, IsIntegral (Y i)),
      Nonempty (X.normalizationScheme hX ≅ ∐ Y)
```

**`AlgebraicGeometry.exists_normalizationFactorization_of_integral_of_birational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/IntegralBirational.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/IntegralBirational.lean#L315). The attribute's comment: “normalization\_integral\_birational”.

> **Stacks Project, Tag 035Q.** An integral morphism which is birational over every
> quasi-compact open does not change the normalization.

```lean
theorem exists_normalizationFactorization_of_integral_of_birational
    {X X' : Scheme.{u}} (hX : ∀ U : X.Opens, IsCompact (U : Set X) →
      (irreducibleComponents U).Finite) (α : X' ⟶ X) [IsIntegralHom α]
    (hcomponents : ∀ U : X.Opens, IsCompact (U : Set X) →
      (irreducibleComponents (α ⁻¹ᵁ U)).Finite)
    (hbirational : ∀ U : X.Opens, IsCompact (U : Set X) →
      IsBirational (α ∣_ U)) :
    ∃ (hX' : ∀ V : X'.Opens, IsCompact (V : Set X') →
        (irreducibleComponents V).Finite)
      (g : Scheme.normalizationScheme X hX ⟶ X')
      (e : Scheme.normalizationScheme X hX ≅
        Scheme.normalizationScheme X' hX'),
      g ≫ α = Scheme.normalization X hX ∧
        e.hom ≫ Scheme.normalization X' hX' = g
```

**`AlgebraicGeometry.Scheme.isIntegralHom_surjective_bijOn_irreducibleComponents_normalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/SurjectiveComponents.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/SurjectiveComponents.lean#L143). The attribute's comment: “normalization\_integral\_surjective\_bijection\_on\_components”.

> **Stacks Project, Tag 035Q.** Part (2). Let `X` be a scheme such that every quasi-compact
> open of `X` has finitely many irreducible components. Then the normalization morphism
> `ν : X^ν ⟶ X` is integral, it is surjective, and it induces a bijection on irreducible
> components: sending an irreducible component of `X^ν` to the closure of its image under `ν` is a
> bijection onto the set of irreducible components of `X`.
>
> Integrality is `AlgebraicGeometry.Scheme.isIntegralHom_normalization` (Tag 035I), surjectivity
> is `AlgebraicGeometry.Scheme.surjective_normalization`, and the bijection on components is
> `AlgebraicGeometry.Scheme.bijOn_irreducibleComponents_normalization`, which rests on Tags 035O
> and 0BXC.

```lean
theorem isIntegralHom_surjective_bijOn_irreducibleComponents_normalization
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    IsIntegralHom (X.normalization hX) ∧ Surjective (X.normalization hX) ∧
      Set.BijOn (fun D ↦ closure ((X.normalization hX).base '' D))
        (irreducibleComponents (X.normalizationScheme hX)) (irreducibleComponents X)
```

**`AlgebraicGeometry.Scheme.existsUnique_lift_normalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/UniversalProperty.lean, line 793](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/UniversalProperty.lean#L793). The attribute's comment: “normalization\_universal\_property”. References: EGA II (6.3.9), “special case”; EGA IV (8.12.11), “special case”.

> **Stacks Project, Tag 035Q part (4).** A morphism to `X` from a normal scheme each of whose
> irreducible components dominates an irreducible component of `X` factors uniquely through the
> normalization of `X`.

```lean
theorem existsUnique_lift_normalization {X Z : Scheme.{u}}
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (f : Z ⟶ X) [IsNormal Z]
    (hgeneric : ∀ η : genericPoints Z, f η.1 ∈ genericPoints X) :
    ∃! g : Z ⟶ X.normalizationScheme hX, g ≫ X.normalization hX = f
```

## Tag 0CDV, a lemma

[Tag 0CDV](https://stacks.math.columbia.edu/tag/0CDV) in the Stacks Project.

**`AlgebraicGeometry.Scheme.exists_iso_normalizationScheme_sigma_reducedComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Components.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Components.lean#L476).

> **Stacks Project, Tag 0CDV.** Let `X` be a scheme whose quasi-compact opens have finitely
> many irreducible components, and give each irreducible component of `X` its reduced induced
> closed subscheme structure. Then the coproduct of the normalizations of those components, with
> its canonical morphism to `X`, is the normalization of `X`.

```lean
theorem exists_iso_normalizationScheme_sigma_reducedComponent
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    ∃ e : (∐ fun Z : irreducibleComponents X ↦ (X.reducedComponent Z).normalizationScheme
        (X.finite_irreducibleComponents_reducedComponent Z)) ≅ X.normalizationScheme hX,
      e.hom ≫ X.normalization hX =
        Sigma.desc fun Z : irreducibleComponents X ↦
          (X.reducedComponent Z).normalization
            (X.finite_irreducibleComponents_reducedComponent Z) ≫ X.reducedComponentι Z
```

## Tag 0BXC, a lemma

[Tag 0BXC](https://stacks.math.columbia.edu/tag/0BXC) in the Stacks Project.

**`AlgebraicGeometry.Scheme.isBirational_normalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationBirational/Basic.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NormalizationBirational/Basic.lean#L158).

> **Stacks Project, Tag 0BXC.** The normalization morphism of a reduced scheme whose
> quasi-compact opens have finitely many irreducible components is birational.

```lean
theorem isBirational_normalization
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    IsBirational (X.normalization hX)
```

## Tag 0AB1, a lemma

[Tag 0AB1](https://stacks.math.columbia.edu/tag/0AB1) in the Stacks Project.

**`AlgebraicGeometry.isIso_of_isIntegralHom_of_isBirational_of_isNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/BirationalIsIso.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/BirationalIsIso.lean#L107). References: EGA IV (8.12.10.1), “more general”; EGA II (6.1.15); EGA II (8.11.2), “special case”; EGA IV (17.15.14.1), “(i), special case”; EGA IV (8.12.10), “special case”.

> **Stacks Project, Tag 0AB1.** An integral birational morphism of integral schemes whose
> target is normal is an isomorphism.

```lean
public theorem isIso_of_isIntegralHom_of_isBirational_of_isNormal
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegral X] [IsIntegral Y]
    [IsIntegralHom f] [IsNormal Y] (hf : IsBirational f) :
    IsIso f
```

## Tag 0H7D, a lemma

[Tag 0H7D](https://stacks.math.columbia.edu/tag/0H7D) in the Stacks Project.

**`AlgebraicGeometry.Scheme.isIso_normalization_iff_isNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Normal.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NormalizationBaseChange/Normal.lean#L378).

> **Stacks Project, Tag 0H7D.** The normalization morphism of a scheme whose quasi-compact
> opens have finitely many irreducible components is an isomorphism if and only if the scheme is
> normal.

```lean
theorem isIso_normalization_iff_isNormal (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    IsIso (X.normalization hX) ↔ IsNormal X
```

## Tag 035R, a lemma

[Tag 035R](https://stacks.math.columbia.edu/tag/035R) in the Stacks Project.

**`AlgebraicGeometry.normalization_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Japanese.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Japanese.lean#L95).

> **Stacks Project, Tag 035R.** The normalization morphism of an integral Japanese scheme is
> finite.

```lean
theorem normalization_isFinite (X : Scheme.{u}) [IsIntegral X]
    (hX : IsJapaneseScheme X) :
    let hfinite : ∀ U : X.Opens,
        IsCompact (U : Set X) → (irreducibleComponents U).Finite := by
      intro U _
      cases isEmpty_or_nonempty U with
      | inl hU =>
          rw [Set.finite_def]
          let : IsEmpty U := hU
          exact ⟨⟨∅, fun C ↦ isEmptyElim (C.2.1.nonempty.some)⟩⟩
      | inr hU =>
          let : Nonempty U := hU
          rw [irreducibleComponents_eq_singleton]
          exact Set.finite_singleton _
    IsFinite (Scheme.normalization X hfinite)
```

## Tag 035S, a lemma

[Tag 035S](https://stacks.math.columbia.edu/tag/035S) in the Stacks Project.

**`AlgebraicGeometry.Scheme.isFinite_normalization_of_isNagataScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/Basic.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NagataNormalization/Basic.lean#L252).

> **Stacks Project, Tag 035S.** The normalization morphism `ν : X^ν ⟶ X` of a Nagata scheme
> `X` is finite.
>
> A Nagata scheme is locally Noetherian, so each of its quasi-compact opens is a Noetherian space
> and has finitely many irreducible components; the Nagata hypothesis therefore both forms the
> normalization morphism and makes it finite.

```lean
theorem isFinite_normalization_of_isNagataScheme {X : Scheme.{u}} (hNagata : IsNagataScheme X) :
    IsFinite (X.normalization (finite_irreducibleComponents_of_isNagataScheme X hNagata))
```

## Tag 0GIQ, a lemma

[Tag 0GIQ](https://stacks.math.columbia.edu/tag/0GIQ) in the Stacks Project.

**`AlgebraicGeometry.Scheme.universalHomeomorphism_normalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/UniversalHomeomorphism.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/UniversalHomeomorphism.lean#L94). References: EGA 0 (23.2.2), “sufficiency + homeo”; SGA 3 X (5.14.0), “univ. homeomorphism”; SGA 4 VIII (1.3), “1.3 c), special case”.

> **Stacks Project, Tag 0GIQ.** The normalization morphism of an irreducible, geometrically
> unibranch scheme is a universal homeomorphism.

```lean
public theorem universalHomeomorphism_normalization (X : Scheme.{u}) [IrreducibleSpace X]
    (hX : IsGeometricallyUnibranch X) :
    UniversalHomeomorphism
      (normalization X (finite_irreducibleComponents_of_irreducibleSpace X))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.55, Tag 035E](https://stacks.math.columbia.edu/tag/035E)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
