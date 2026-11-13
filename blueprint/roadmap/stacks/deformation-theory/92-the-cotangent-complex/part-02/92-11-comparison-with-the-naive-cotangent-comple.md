---
declaration: section
origin: cited
lean: CommAlgCat.polynomialAugmentationModuleHom, CommAlgCat.polynomialAugmentationIdeal, CommAlgCat.isZero_polynomialSiteDerivedLowerShriek_ideal, CommAlgCat.polynomialSiteDerivedLowerShriekCotangentIdealComplexIso, CommAlgCat.polynomialSiteDerivedLowerShriekIdealComplexIso, CommAlgCat.idealComplexToCotangentComplex, CommAlgCat.isZero_polynomialSiteConormalHomology_zero, CommAlgCat.isZero_polynomialSiteConormalHomology_one
statement: formalized
proof: formalized
---

# 92.11 Comparison with the naive cotangent complex

Section 92.11 of the Stacks Project, [Tag 08R6](https://stacks.math.columbia.edu/tag/08R6). 6 tags here are carried by 36 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08R7, a remark

[Tag 08R7](https://stacks.math.columbia.edu/tag/08R7) in the Stacks Project.

**`CommAlgCat.polynomialAugmentationModuleHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteAugmentationIdeal.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteAugmentationIdeal.lean#L66). The attribute's comment: “the augmentation O → B of sheaves of O-modules”.

> The augmentation `𝒪 → B̲`, read as a map of sheaves of `𝒪`-modules: the target is `B̲` with
> its `𝒪`-module structure obtained by restriction of scalars along the augmentation, and the map is
> the one sending the unit section of `𝒪` to the unit section of `B̲`.

```lean
def polynomialAugmentationModuleHom :
    SheafOfModules.unit (polynomialStructureRingSheaf A B) ⟶
      (SheafOfModules.restrictScalars (polynomialAugmentationRingHom A B)).obj
        (SheafOfModules.unit (polynomialConstantRingSheaf A B))
```

**`CommAlgCat.polynomialAugmentationIdeal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteAugmentationIdeal.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteAugmentationIdeal.lean#L80). The attribute's comment: “the defining ideal J = ker(O → B)”.

> The augmentation ideal `𝒥 = ker(𝒪 → B̲)` on the site `C_{B/A}`, a sheaf of `𝒪`-modules. Its
> inclusion `𝒥 ⊂ 𝒪` is `CategoryTheory.Limits.kernel.ι`.

```lean
abbrev polynomialAugmentationIdeal :
    SheafOfModules.{u + 1} (polynomialStructureRingSheaf A B)
```

**`CommAlgCat.isZero_polynomialSiteDerivedLowerShriek_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteNaiveComparison.lean, line 429](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteNaiveComparison.lean#L429). The attribute's comment: “Lπ\_!(𝒥) = 0 for 𝒥 = ker(𝒪 → B̲), in D(A), at the site C\_\{B/A} of Tag 08PR itself, with Lπ\_! the total left derived functor of the colimit over the site (the π\_! of Tag 08PF) and the coefficients at the universe of the site's objects”.

> **`Lπ_!(𝒥) = 0` in `D(A)`**, the first assertion of Remark 08R7, at the site `C_{B/A}`
> itself, for the augmentation ideal `𝒥 = ker(𝒪 → B̲)` read as a sheaf of `A`-modules.

```lean
theorem isZero_polynomialSiteDerivedLowerShriek_ideal :
    IsZero ((polynomialSiteModuleDerivedLowerShriek A B (ULift.{u + 1} A)).obj
      (DerivedCategory.Q.obj ((HomologicalComplex.single _ (ComplexShape.up ℤ) 0).obj
        (polynomialSiteIdealSheaf A B))))
```

**`CommAlgCat.polynomialSiteDerivedLowerShriekCotangentIdealComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteNaiveComparison.lean, line 468](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteNaiveComparison.lean#L468). The attribute's comment: “Lπ\_!(𝒥 → Ω) = Lπ\_!(Ω) in D(A), at the site C\_\{B/A} of Tag 08PR itself, as the isomorphism induced by the inclusion Ω → (𝒥 → Ω) of the degree-zero term”.

> **`Lπ_!(Ω) = Lπ_!(𝒥 → Ω)`** in `D(A)`, induced by the inclusion `Ω → (𝒥 → Ω)`.

```lean
def polynomialSiteDerivedLowerShriekCotangentIdealComplexIso :
    (polynomialSiteModuleDerivedLowerShriek A B (ULift.{u + 1} A)).obj
        (DerivedCategory.Q.obj ((HomologicalComplex.single _ (ComplexShape.up ℤ) 0).obj
          (polynomialSiteCotangentSheafOverBase A B))) ≅
      (polynomialSiteModuleDerivedLowerShriek A B (ULift.{u + 1} A)).obj
        (DerivedCategory.Q.obj (polynomialSiteIdealComplex A B))
```

**`CommAlgCat.polynomialSiteDerivedLowerShriekIdealComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteNaiveComparison.lean, line 487](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteNaiveComparison.lean#L487). The attribute's comment: “Lπ\_!(𝒥 → Ω) = Lπ\_!(Ω) = L\_\{B/A} in D(A), at the site C\_\{B/A} of Tag 08PR itself, for the two-term complex 𝒥 → Ω in degrees -1, 0, Ω = Ω\_\{𝒪/A} ⊗\_𝒪 B̲, the identification being the inverse of the one induced by Ω → (𝒥 → Ω) followed by Tag 08PU”.

> **`Lπ_!(𝒥 → Ω) = L_{B/A}` in `D(A)`**, Remark 08R7, at the site `C_{B/A}` itself: the
> two-term complex `𝒥 → Ω` of sheaves of `A`-modules, in degrees `-1, 0`, has `Lπ_!` the cotangent
> complex of Tag 08PN.

```lean
def polynomialSiteDerivedLowerShriekIdealComplexIso :
    (polynomialSiteModuleDerivedLowerShriek A B (ULift.{u + 1} A)).obj
        (DerivedCategory.Q.obj (polynomialSiteIdealComplex A B)) ≅
      cotangentComplexOverBase A B
```

**`CommAlgCat.idealComplexToCotangentComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteNaiveComparison.lean, line 502](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteNaiveComparison.lean#L502). The attribute's comment: “the map (08R8): (J → Ω\_\{P/A} ⊗\_P B) → L\_\{B/A} in D(A) for every object U = (P → B) of C\_\{B/A}, J = ker(P → B), as the canonical map of Tag 08Q6 followed by Lπ\_!(𝒥 → Ω) = L\_\{B/A}”.

> **The map (08R8) of Remark 08R7**: for an object `U = (P → B)` of `C_{B/A}`, with
> `J = ker(P → B)`, the map `(J → Ω_{P/A} ⊗_P B) ⟶ L_{B/A}` in `D(A)`. It is the canonical map
> `K(U) ⟶ Lπ_!(K)` of Tag 08Q6 for the two-term complex `K = (𝒥 → Ω)`, followed by
> `Lπ_!(𝒥 → Ω) = L_{B/A}`; the two-term complex `J → Ω_{P/A} ⊗_P B` of `A`-modules is the value of
> `𝒥 → Ω` at `U`.

```lean
def idealComplexToCotangentComplex (U : polynomialSite A B) :
    DerivedCategory.Q.obj (CochainComplex.doubleNegOneZero
        ((liftModuleFunctor A).map ((polynomialSiteIdealToCotangent A B).app (op U)))) ⟶
      cotangentComplexOverBase A B
```

**`CommAlgCat.isZero_polynomialSiteConormalHomology_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteNaiveComparisonTruncated.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteNaiveComparisonTruncated.lean#L209). The attribute's comment: “H\_0(C\_\{B/A}, 𝒥/𝒥²) = 0, read as H⁰(Lπ\_!(𝒥/𝒥²)) = 0 in D(B) at the site C\_\{B/A} of Tag 08PR itself, for the B̲-module 𝒥/𝒥² = Tor₀^𝒪(𝒥, B̲) = 𝒥 ⊗\_𝒪 B̲”.

> **`H₀(C_{B/A}, 𝒥/𝒥²) = 0`**, Remark 08R7, at the site `C_{B/A}` itself:
> `H⁰(Lπ_!(𝒥/𝒥²)) = 0` for `𝒥/𝒥² = 𝒥 ⊗_𝒪 B̲ = Tor₀^𝒪(𝒥, B̲)`.

```lean
theorem isZero_polynomialSiteConormalHomology_zero :
    IsZero ((DerivedCategory.homologyFunctor _ 0).obj
      (polynomialSiteDerivedLowerShriekConormal A B))
```

**`CommAlgCat.isZero_polynomialSiteConormalHomology_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteNaiveComparisonTruncated.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteNaiveComparisonTruncated.lean#L219). The attribute's comment: “H\_1(C\_\{B/A}, 𝒥/𝒥²) = 0, read as H⁻¹(Lπ\_!(𝒥/𝒥²)) = 0 in D(B) at the site C\_\{B/A} of Tag 08PR itself, for the B̲-module 𝒥/𝒥² = Tor₀^𝒪(𝒥, B̲) = 𝒥 ⊗\_𝒪 B̲”.

> **`H₁(C_{B/A}, 𝒥/𝒥²) = 0`**, Remark 08R7, at the site `C_{B/A}` itself:
> `H⁻¹(Lπ_!(𝒥/𝒥²)) = 0` for `𝒥/𝒥² = 𝒥 ⊗_𝒪 B̲ = Tor₀^𝒪(𝒥, B̲)`.

```lean
theorem isZero_polynomialSiteConormalHomology_one :
    IsZero ((DerivedCategory.homologyFunctor _ (-1)).obj
      (polynomialSiteDerivedLowerShriekConormal A B))
```

**`CommAlgCat.polynomialSiteTruncGEConormalComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteNaiveComparisonTruncated.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteNaiveComparisonTruncated.lean#L281). The attribute's comment: “τ\_\{≥-1} Lπ\_!(𝒥/𝒥² → Ω) = τ\_\{≥-1} L\_\{B/A} in D(B), at the site C\_\{B/A} of Tag 08PR itself, for the two-term complex 𝒥/𝒥² → Ω of B̲-modules in degrees -1, 0, 𝒥/𝒥² = Tor₀^𝒪(𝒥, B̲) = 𝒥 ⊗\_𝒪 B̲, the identification being induced by Ω → (𝒥/𝒥² → Ω) and Tag 08PU”.

> **`τ_{≥ -1} Lπ_!(𝒥/𝒥² → Ω) = τ_{≥ -1} L_{B/A}` in `D(B)`**, Remark 08R7, at the site
> `C_{B/A}` itself, for the two-term complex `𝒥/𝒥² → Ω` in degrees `-1, 0`.

```lean
def polynomialSiteTruncGEConormalComplexIso :
    (DerivedCategory.TStructure.t.truncGE (-1)).obj
        ((polynomialSiteModuleDerivedLowerShriek A B (ULift.{u + 1} (B : Type u))).obj
          (DerivedCategory.Q.obj (polynomialSiteConormalComplex A B))) ≅
      (DerivedCategory.TStructure.t.truncGE (-1)).obj (cotangentComplexLift A B)
```

**`CommAlgCat.conormalComplexToTruncGECotangentComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteNaiveComparisonTruncated.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteNaiveComparisonTruncated.lean#L307). The attribute's comment: “the map (08R9): (J/J² → Ω\_\{P/A} ⊗\_P B) → τ\_\{≥-1} L\_\{B/A} in D(B) for every object U = (P → B) of C\_\{B/A}, the degree -1 term being the sections B ⊗\_P J of 𝒥/𝒥² = 𝒥 ⊗\_𝒪 B̲, which are J/J² for surjective P → B, as the canonical map of Tag 08Q6 followed by τ\_\{≥-1} Lπ\_!(𝒥/𝒥² → Ω) = τ\_\{≥-1} L\_\{B/A}”.

> **The map (08R9) of Remark 08R7**: for an object `U = (P → B)` of `C_{B/A}`, with
> `J = ker(P → B)`, the map `(J/J² → Ω_{P/A} ⊗_P B) ⟶ τ_{≥ -1} L_{B/A}` in `D(B)`. Its domain is the
> value at `U` of the two-term complex `𝒥/𝒥² → Ω`, whose degree `-1` term is `B ⊗_P J`, which is
> `J/J²` whenever `P → B` is surjective (`Algebra.Extension.tensorKerEquivCotangent`). The map is
> the canonical map `K(U) ⟶ Lπ_!(K)` of Tag 08Q6 for `K = (𝒥/𝒥² → Ω)`, followed by the truncation
> and by `τ_{≥ -1} Lπ_!(𝒥/𝒥² → Ω) = τ_{≥ -1} L_{B/A}`.

```lean
def conormalComplexToTruncGECotangentComplex (U : polynomialSite A B) :
    DerivedCategory.Q.obj (CochainComplex.doubleNegOneZero
        ((liftModuleFunctor (B : Type u)).map
          ((polynomialSiteConormalToCotangent A B).app (op U)))) ⟶
      (DerivedCategory.TStructure.t.truncGE (-1)).obj (cotangentComplexLift A B)
```

## Tag 08R9, an equation

[Tag 08R9](https://stacks.math.columbia.edu/tag/08R9) in the Stacks Project.

**`Algebra.Extension.naiveComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/NaiveComparison.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/NaiveComparison.lean#L142). The attribute's comment: “the source complex (J/J² → Ω\_\{P/A} ⊗\_P B) of the displayed map, for a presentation P → B, in cohomological degrees -1 and 0”.

> **Stacks Project, Tag 08R9 (the source of the displayed map).**
>
> The naive cotangent complex `NL(P → B) : J/J² ⟶ Ω[P⁄A] ⊗[P] B` of a presentation, in
> cohomological degrees `-1` and `0`.

```lean
public noncomputable def naiveComplex : CochainComplex (ModuleCat.{v} S) ℤ
```

**`Stacks.Cotangent.comparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/NaiveComparisonMap.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/NaiveComparisonMap.lean#L301). The attribute's comment: “the displayed map (J/J² → Ω\_\{P/A} ⊗\_P B) → τ\_\{≥ -1} L\_\{B/A} in D(B), at an object (P → B) of C\_\{B/A}, with the source the two-term complex Algebra.Extension.naiveComplex of that object and the target the degree ≥ -1 truncation of the cotangent complex of Tag 08PN”.

> **Stacks Project, Tag 08R9.** The comparison map
>
> `(J/J² → Ω_{P/A} ⊗_P B) ⟶ τ_{≥ -1} L_{B/A}`
>
> in `D(B)`, at an object `U = (P → B)` of `C_{B/A}` with kernel `J`. It is the evaluation at `U`
> of the two-term complex `𝒥/𝒥² → Ω` of Remark 08R7, followed by the identification
> `τ_{≥ -1} Lπ_!(𝒥/𝒥² → Ω) = τ_{≥ -1} L_{B/A}` of that remark, both read on the standard
> resolution.

```lean
def comparison (E : Algebra.Extension.{max u v} A ↥B)
    (hP : Algebra.IsPolynomialAlgebra A E.Ring) :
    DerivedCategory.Q.obj (Algebra.Extension.naiveComplex E) ⟶
      (DerivedCategory.TStructure.t.truncGE (-1)).obj
        (DerivedCategory.Q.obj (cotangentComplex A B))
```

## Tag 08RA, a lemma

[Tag 08RA](https://stacks.math.columbia.edu/tag/08RA) in the Stacks Project.

**`CommAlgCat.cotangentComplex_isZero_homology_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Surjection.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Surjection.lean#L102). The attribute's comment: “the degree-zero conclusion H⁰(L\_\{B/A}) = 0”.

> **Stacks Project, Tag 08RA.** The degree-zero homology of the cotangent complex of a
> surjective ring map vanishes: it is the module of Kähler differentials, which is zero.

```lean
public theorem cotangentComplex_isZero_homology_zero (A : Type u) [CommRing A]
    (B : CommAlgCat.{max u v} A) (h : Function.Surjective (algebraMap A B)) :
    IsZero ((cotangentComplex A B).homology 0)
```

**`CommAlgCat.cotangentComplex_homologyNegOneIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Surjection.lean, line 729](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Surjection.lean#L729). The attribute's comment: “the degree-minus-one conclusion H⁻¹(L\_\{B/A}) = I/I², with I/I² the conormal module of the presentation A → B, the isomorphism being the connecting homomorphism of the short exact sequence 0 → I/I² → J•/J•² → Ω[P•⁄A] ⊗[P•] B → 0 of the Stacks proof”.

> **Stacks Project, Tag 08RA.** For a surjective ring map `A → B` with kernel `I`, the
> degree `-1` homology of the cotangent complex `L_{B/A}` is the conormal module `I/I²`. The
> isomorphism is the connecting homomorphism of the short exact sequence
> `0 → I/I² → J•/J•² → Ω[P•⁄A] ⊗[P•] B → 0` of simplicial modules, which is the sequence used in
> the Stacks proof.

```lean
public noncomputable def cotangentComplex_homologyNegOneIso :
    (cotangentComplex A B).homology (-1) ≅
      ModuleCat.of B (surjectionExtension A B h).Cotangent
```

**`CommAlgCat.cotangentComplexHomologyNegOneIsoComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectionComparisonMap.lean, line 502](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SurjectionComparisonMap.lean#L502). The attribute's comment: “the degree-minus-one conclusion H⁻¹(L\_\{B/A}) = I/I², with the isomorphism the one induced by the comparison map of Tag 08R9 at the object (A → B) of C\_\{B/A}, which is the identification the source's statement names”.

> **Stacks Project, Tag 08RA.** For a surjective ring map `A → B` with kernel `I`, the
> identification `H^{-1}(L_{B/A}) ≅ I/I²` *induced by the comparison map of Tag 08R9 at the object
> `(A → B)` of `C_{B/A}`* — which is the identification the source's statement names.
>
> Read from right to left it is: the conormal module `I/I²` is the degree `-1` cohomology of the
> two-term complex `NL(A → B)`, that cohomology is carried into `H^{-1}(τ_{≥ -1} L_{B/A})` by the
> comparison map, and `τ_{≥ -1}` changes no cohomology in degree `-1`.

```lean
def cotangentComplexHomologyNegOneIsoComparison :
    (cotangentComplex A B).homology (-1) ≅
      ModuleCat.of B (surjectionExtension A B h).Cotangent
```

## Tag 08RB, a lemma

[Tag 08RB](https://stacks.math.columbia.edu/tag/08RB) in the Stacks Project.

**`CommAlgCat.cotangentComplexHomologyZeroIsoNaive`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/NaiveComparison.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/NaiveComparison.lean#L125). The attribute's comment: “degree zero: H⁰(L\_\{B/A}) = H⁰(NL\_\{B/A})”.

> **Stacks 08RB, degree zero.** The degree-zero cohomology of the cotangent complex `L_{B/A}`
> agrees with the degree-zero cohomology of the naive cotangent complex `NL_{B/A}`; both are
> `Ω[B⁄A]`, by the augmentation of the standard resolution on one side and by
> `Algebra.Extension.toKaehler` on the other.

```lean
noncomputable def cotangentComplexHomologyZeroIsoNaive :
    (cotangentComplex A B).homology 0 ≅ ModuleCat.of ↥B (naiveHomologyZero A B)
```

**`Stacks.Cotangent.isIso_comparisonAtNaive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/NaiveComparisonIsIso.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/NaiveComparisonIsIso.lean#L166). The attribute's comment: “the canonical map c : NL\_\{B/A} → τ\_\{≥ -1} L\_\{B/A} of Tag 08R9, at the canonical presentation A[B] → B, is an isomorphism in D(B)”.

> **Stacks 08RB.** For a ring map `A → B`, the canonical map
> `c : NL_{B/A} → τ_{≥ -1} L_{B/A}` of Tag 08R9 at the canonical presentation `A[B] → B` is an
> isomorphism in `D(B)`: the truncation `τ_{≥ -1} L_{B/A}` is canonically quasi-isomorphic to the
> naive cotangent complex.

```lean
theorem isIso_comparisonAtNaive : IsIso (comparisonAtNaive A B)
```

**`Stacks.Cotangent.naiveComparisonIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/NaiveComparisonIsIso.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/NaiveComparisonIsIso.lean#L199). The attribute's comment: “the isomorphism NL\_\{B/A} ≅ τ\_\{≥ -1} L\_\{B/A} in D(B) whose underlying map is the canonical map c of Tag 08R9”.

> **Stacks 08RB.** The isomorphism `NL_{B/A} ≅ τ_{≥ -1} L_{B/A}` in `D(B)`, with the naive
> cotangent complex the two-term complex `I/I² → Ω_{A[B]/A} ⊗_{A[B]} B` of the canonical
> presentation; its underlying map is the canonical map `c` of Tag 08R9.

```lean
def naiveComparisonIso :
    DerivedCategory.Q.obj (Algebra.Extension.naiveComplex (conormalExtension A B (op ⦋0⦌))) ≅
      (DerivedCategory.TStructure.t.truncGE (-1)).obj
        (DerivedCategory.Q.obj (cotangentComplex A B))
```

## Tag 08UP, a remark

[Tag 08UP](https://stacks.math.columbia.edu/tag/08UP) in the Stacks Project.

**`Stacks.Cotangent.explicitNaiveComparison_comp_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/NaiveComparisonAgreement.lean, line 801](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/NaiveComparisonAgreement.lean#L801). The attribute's comment: “the chain map of the remark induces the comparison map of Lemma 08RB: composed with the map of Tag 08R9 at the object A[B] → B it is the truncation map L\_\{B/A} → τ\_\{≥ -1} L\_\{B/A} in D(B)”.

> **Stacks Project, Tag 08UP.** The explicit chain map `L_{B/A} ⟶ NL_{B/A}` of the remark
> induces, in `D(B)`, a map inverse to the comparison map `c` of Lemma 08RB: composed with `c` it is
> the truncation map `L_{B/A} ⟶ τ_{≥ -1} L_{B/A}`.  This is the verification the source omits ("We
> omit the verification that this is the same as the map of Lemma 92.11.3"), with `c` the tagged map
> `Stacks.Cotangent.comparison` of Tag 08R9 at the object `A[B] → B` of `C_{B/A}`.
>
> The proof reduces the equation, by the naturality of `truncGEπ` and the definition of
> `Stacks.Cotangent.truncGEConeIso`, to the vanishing of the difference `f ≫ e - ι` in `D(B)` after
> `τ_{≥ -1}`; see the module docstring for the route.

```lean
theorem explicitNaiveComparison_comp_comparison :
    DerivedCategory.Q.map (explicitNaiveComparison A B) ≫
        comparison A B (standardResolutionExtension A B 0)
          (isPolynomialAlgebra_standardResolutionExtension_ring A B 0) =
      (DerivedCategory.TStructure.t.truncGEπ (-1)).app
        (DerivedCategory.Q.obj (cotangentComplex A B))
```

**`Stacks.Cotangent.explicitNaiveComparison_comp_comparisonAtNaive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/NaiveComparisonAgreement.lean, line 822](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/NaiveComparisonAgreement.lean#L822). The attribute's comment: “the chain map of the remark induces the comparison map of Lemma 08RB: composed with comparisonAtNaive it is the truncation map L\_\{B/A} → τ\_\{≥ -1} L\_\{B/A} in D(B), after the isomorphism naiveSpellingIso identifying the two spellings of NL\_\{B/A}”.

> **Stacks Project, Tag 08UP.** The same equation with `Stacks.Cotangent.comparisonAtNaive`,
> the comparison map of Lemma 08RB at the spelling `Stacks.Cotangent.conormalExtension A B (op ⦋0⦌)`
> of the presentation `A[B] → B`: the two spellings of `NL_{B/A}` differ only by the section of the
> augmentation they carry, and `Stacks.Cotangent.naiveSpellingIso` is the isomorphism between them
> induced by the identity of `A[B]`.

```lean
theorem explicitNaiveComparison_comp_comparisonAtNaive :
    DerivedCategory.Q.map (explicitNaiveComparison A B ≫ (naiveSpellingIso A B 0).hom) ≫
        comparisonAtNaive A B =
      (DerivedCategory.TStructure.t.truncGEπ (-1)).app
        (DerivedCategory.Q.obj (cotangentComplex A B))
```

**`CommAlgCat.comparisonComponent_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/NaiveComparisonChainMap.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/NaiveComparisonChainMap.lean#L315). The attribute's comment: “the comparison vanishes outside degrees 0 and -1, the bottom row being zero there”.

> **Stacks Project, Tag 08UP.** Outside cohomological degrees `0` and `-1` the comparison is
> zero: the bottom row of the diagram vanishes there, so every downward arrow from
> `Ω[Pₙ⁄A] ⊗[Pₙ] B` with `n ≥ 2` is zero.

```lean
theorem comparisonComponent_eq_zero (i : ℤ) (h : i ≠ 0) (h' : i ≠ -1) :
    comparisonComponent A B i = 0
```

**`CommAlgCat.explicitNaiveComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/NaiveComparisonChainMap.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/NaiveComparisonChainMap.lean#L332). The attribute's comment: “the map of complexes L\_\{B/A} → NL\_\{B/A} itself, assembled from the two squares (the source's `Hence a map of complexes`): the identity in degree 0, the explicit arrow d f ⊗ b ↦ (d₀ f - d₁ f) b in degree -1, and zero in every other degree”.

> **Stacks Project, Tag 08UP.** The map of complexes `L_{B/A} ⟶ NL_{B/A}` displayed by the
> remark: the identity in degree zero, the explicit arrow `d f ⊗ b ↦ (d₀ f - d₁ f) b` in degree
> `-1`, and zero above. This is the source's "Hence a map of complexes": the two commuting squares
> are `CommAlgCat.core_lower` and `CommAlgCat.core_upper`, and in every other pair of adjacent
> degrees the bottom row vanishes.
>
> The agreement of this map with the comparison map `c` of Tag 08RB — the verification the source
> omits — is not claimed by this definition; it is
> `Stacks.Cotangent.explicitNaiveComparison_comp_comparison` of
> `StacksFrontier/Cotangent/NaiveComparisonAgreement.lean`.

```lean
noncomputable def explicitNaiveComparison :
    cotangentComplex A B ⟶
      Algebra.Extension.naiveComplex (standardResolutionExtension A B 0)
```

**`CommAlgCat.isIso_comparisonDegreeZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/NaiveComparisonChainMap.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/NaiveComparisonChainMap.lean#L370). The attribute's comment: “degree zero: the downward arrow is the identity, hence an isomorphism, the two rows having the same term there”.

> **Stacks Project, Tag 08UP.** In degree zero the comparison is an isomorphism: the two rows
> of the diagram have the same term `Ω[P₀⁄A] ⊗[P₀] B` there and the downward arrow is the identity
> between the two presentations of it.

```lean
theorem isIso_comparisonDegreeZero : IsIso (comparisonDegreeZero A B)
```

**`CommAlgCat.naiveCotangentComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/NaiveComparisonExplicitArrow.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/NaiveComparisonExplicitArrow.lean#L232). The attribute's comment: “the explicit downward arrow of the diagram, `d f ⊗ b ↦ (d₀ f - d₁ f) b`, with no hypothesis beyond the remark's own standard resolution of B over A; well defined by construction, as the remark's two omitted verifications are discussed in this module's implementation notes”.

> **Stacks Project, Tag 08UP.** The downward arrow of the comparison diagram in degree one:
> the difference of the two faces `P₁ → P₀`, which lands in the kernel `I` of the augmentation,
> read as a map `Ω[P₁⁄A] ⊗[P₁] B → I/I²`.

```lean
noncomputable def naiveCotangentComparison :
    (standardResolutionExtension A B 1).CotangentSpace →ₗ[B]
      (standardResolutionExtension A B 0).Cotangent
```

**`CommAlgCat.naiveCotangentComparison_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/NaiveComparisonExplicitArrow.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/NaiveComparisonExplicitArrow.lean#L239). The attribute's comment: “the value of the arrow on a pure differential”.

> The arrow sends `d f ⊗ b` to `b` times the class of `d₀ f - d₁ f` in `I/I²`.

```lean
theorem naiveCotangentComparison_tmul (b : B)
    (f : (standardResolutionExtension A B 1).Ring) :
    naiveCotangentComparison A B
        (b ⊗ₜ KaehlerDifferential.D A (standardResolutionExtension A B 1).Ring f) =
      b • Algebra.Extension.Cotangent.mk
        ((standardResolutionExtensionFace A B 0 0).subToKer
          (standardResolutionExtensionFace A B 0 1) f)
```

**`CommAlgCat.naiveCotangentComparison_subToKer_coe`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/NaiveComparisonExplicitArrow.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/NaiveComparisonExplicitArrow.lean#L250). The attribute's comment: “the difference of the two faces, which is the element of `I` the arrow uses”.

> The element of `I` whose class the arrow takes: the difference of the two faces.

```lean
theorem naiveCotangentComparison_subToKer_coe
    (f : (standardResolutionExtension A B 1).Ring) :
    ((standardResolutionExtensionFace A B 0 0).subToKer
        (standardResolutionExtensionFace A B 0 1) f).val =
      (standardResolution A B).left.δ (0 : Fin 2) f -
        (standardResolution A B).left.δ (1 : Fin 2) f
```

**`CommAlgCat.naiveCotangentComparison_cotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/NaiveComparisonExplicitArrow.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/NaiveComparisonExplicitArrow.lean#L262). The attribute's comment: “the lower square: compatibility with the differential out of degree one”.

> The lower commuting square of the diagram: following the arrow by the differential
> `I/I² → Ω[P₀⁄A] ⊗[P₀] B` of the naive cotangent complex is the differential
> `Ω[P₁⁄A] ⊗[P₁] B → Ω[P₀⁄A] ⊗[P₀] B`, the difference of the two faces.

```lean
theorem naiveCotangentComparison_cotangentComplex :
    (standardResolutionExtension A B 0).cotangentComplex ∘ₗ naiveCotangentComparison A B =
      Algebra.Extension.CotangentSpace.map (standardResolutionExtensionFace A B 0 0) -
        Algebra.Extension.CotangentSpace.map (standardResolutionExtensionFace A B 0 1)
```

**`CommAlgCat.naiveCotangentComparison_faceSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/NaiveComparisonExplicitArrow.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/NaiveComparisonExplicitArrow.lean#L272). The attribute's comment: “the upper square: the arrow annihilates the differential into degree one”.

> The upper commuting square of the diagram: the arrow annihilates the alternating sum of the
> three faces `P₂ → P₁`, which is the differential of the cotangent complex out of degree two.

```lean
theorem naiveCotangentComparison_faceSum :
    naiveCotangentComparison A B ∘ₗ
        (Algebra.Extension.CotangentSpace.map (standardResolutionExtensionFace A B 1 0) -
          Algebra.Extension.CotangentSpace.map (standardResolutionExtensionFace A B 1 1) +
          Algebra.Extension.CotangentSpace.map (standardResolutionExtensionFace A B 1 2)) = 0
```

## Tag 09D5, a remark

[Tag 09D5](https://stacks.math.columbia.edu/tag/09D5) in the Stacks Project.

**`Stacks.Cotangent.isIso_conormalTorOneDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ConormalTorDifferential.lean, line 746](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/ConormalTorDifferential.lean#L746). The attribute's comment: “the differential H₂(C\_\{B/A}, 𝒥/𝒥²) → H₀(C\_\{B/A}, Tor₁^𝒪(𝒥, B̲)) is an isomorphism, read on the standard resolution; the differential is modelled as the composite of the two connecting maps, which is d₂ of the spectral sequence of Remark 08R7 up to sign (not proved, the spectral sequence is not built)”.

> **Stacks 09D5: the differential `H₂(C_{B/A}, 𝒥/𝒥²) → H₀(C_{B/A}, Tor₁^𝒪(𝒥, B̲))` of the
> spectral sequence of Remark 08R7 is an isomorphism.** The differential is modelled as the
> composite of the two connecting maps, which is `d₂` of that spectral sequence up to sign by the
> informal argument of the module docstring (the spectral sequence is not built in Lean, so this
> identification is not proved); each connecting map is an isomorphism because `H₁` and `H₂` of
> `𝒥`, and `H₀` and `H₁` of `𝒥 ⊗_𝒪 𝒥`, vanish.

```lean
theorem isIso_conormalTorOneDifferential : IsIso (conormalTorOneDifferential.{u, v} A B)
```

**`Stacks.Cotangent.cotangentComplexHomologyTwoLinearIsoTorOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ConormalTorDifferentialLinear.lean, line 456](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/ConormalTorDifferentialLinear.lean#L456). The attribute's comment: “H₂(L\_\{B/A}) = H₀(C\_\{B/A}, Tor₁^𝒪(𝒥, B̲)), an isomorphism of B-modules”.

> **Stacks 09D5: `H₂(L_{B/A}) = H₀(C_{B/A}, Tor₁^𝒪(𝒥, B̲))`, as `B`-modules.** `H₂(L_{B/A})`
> is the homology in cohomological degree `-2` of the cotangent complex of Tag 08PN, and the
> right-hand side is `H₀` of the Moore complex of the simplicial `B`-module
> `n ↦ Tor₁^{Pₙ}(Jₙ, B)` on the standard resolution. The isomorphism is
> `H₂(L_{B/A}) ≅ H₂(C_{B/A}, 𝒥/𝒥²)` followed by the differential, made `B`-linear by
> `Stacks.Cotangent.isoOfRestrictScalarsIso`.

```lean
def cotangentComplexHomologyTwoLinearIsoTorOne :
    (cotangentComplex A B).homology (-2) ≅ (torOneMooreComplexB.{u, v} A B).homology 0
```

**`Stacks.Cotangent.isZero_homology_kernel_conormalToCotangentMoore`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectivePresentationHigherHomology.lean, line 532](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SurjectivePresentationHigherHomology.lean#L532). The attribute's comment: “Ker(d) has vanishing higher homology on C\_\{B/A}”.

> **Stacks 09D5**, the kernel of `d` has no higher homology on `C_{B/A}`. By Tag 08PS the
> homology of a sheaf on `C_{B/A}` is the homology of the simplicial module it gives on the
> standard resolution, and `Ker(d)` is there the *constant* simplicial module on
> `Algebra.H1Cotangent A B` (`Stacks.Cotangent.kernelConormalToCotangentMooreIso`, which is the
> constancy of `Stacks.Cotangent.outerTerms_constant` combined with the exactness of
> `Stacks.Cotangent.surjectivePresentation_exact`); the Moore complex of a constant simplicial
> module has no homology in positive degrees.

```lean
theorem isZero_homology_kernel_conormalToCotangentMoore (n : ℕ) (hn : 0 < n) :
    IsZero ((kernel (conormalToCotangentMoore A B)).homology n)
```

**`Stacks.Cotangent.isZero_homology_cokernel_conormalToCotangentMoore`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectivePresentationHigherHomology.lean, line 542](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SurjectivePresentationHigherHomology.lean#L542). The attribute's comment: “Coker(d) has vanishing higher homology on C\_\{B/A}”.

> **Stacks 09D5**, the cokernel of `d` has no higher homology on `C_{B/A}`: on the standard
> resolution `Coker(d)` is the *constant* simplicial module on `Ω[B⁄A]`
> (`Stacks.Cotangent.cokernelConormalToCotangentMooreIso`), and the Moore complex of a constant
> simplicial module has no homology in positive degrees.

```lean
theorem isZero_homology_cokernel_conormalToCotangentMoore (n : ℕ) (hn : 0 < n) :
    IsZero ((cokernel (conormalToCotangentMoore A B)).homology n)
```

**`Stacks.Cotangent.isIso_homologyMap_conormalToCotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectivePresentationHigherHomology.lean, line 578](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SurjectivePresentationHigherHomology.lean#L578). The attribute's comment: “H\_n(C\_\{B/A}, 𝒥/𝒥²) → H\_n(L\_\{B/A}) is an isomorphism for n ≥ 2, at the cotangent complex of Tag 08PN”.

> **Stacks 09D5**, the map `H_n(C_{B/A}, 𝒥/𝒥²) → H_n(L_{B/A})` is an isomorphism for every
> `n ≥ 2`, stated at the cotangent complex `CommAlgCat.cotangentComplex` of Tag 08PN, whose
> homology in cohomological degree `-n` is `H_n(L_{B/A})`. This is
> `Stacks.Cotangent.isIso_homologyMap_conormalToCotangentMoore` transported along the reindexing,
> which changes no homology.

```lean
theorem isIso_homologyMap_conormalToCotangentComplex (n : ℕ) (hn : 2 ≤ n) :
    IsIso (HomologicalComplex.homologyMap (conormalToCotangentComplex A B) (-(n : ℤ)))
```

**`Stacks.Cotangent.surjectivePresentation_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectivePresentationSequence.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SurjectivePresentationSequence.lean#L148). The attribute's comment: “the exact sequence 0 → H₁(L\_\{B/A}) → J/J² → Ω → Ω\_\{B/A} → 0 at an object of C'\_\{B/A}”.

> **Stacks 09D5**, the exact sequence of sheaves on `C'_{B/A}`, read at an object: for a
> surjection `α : P → B` with `P` a polynomial algebra over `A` and `J = ker α`, the sequence
>
> ```
> 0 ⟶ H₁(L_{B/A}) ⟶ J/J² --d--> Ω_{P/A} ⊗_P B ⟶ Ω[B⁄A] ⟶ 0
> ```
>
> is exact. The source writes the right-hand term as `H₂(L_{B/A})`, which is a slip for
> `H₀(L_{B/A})`; that term is `Ω[B⁄A]`, and
> `Stacks.Cotangent.cokerCotangentComplexIsoHomologyZero` identifies it with the degree-zero
> homology of the cotangent complex of Tag 08PN.

```lean
theorem surjectivePresentation_exact (P : Algebra.Extension.{w} A B)
    (hP : Algebra.IsPolynomialAlgebra A P.Ring) :
    Function.Injective (h1CotangentIncl P) ∧
      Function.Exact (h1CotangentIncl P) P.cotangentComplex ∧
        Function.Exact P.cotangentComplex P.toKaehler ∧
          Function.Surjective P.toKaehler
```

**`Stacks.Cotangent.outerTerms_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectivePresentationSequence.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SurjectivePresentationSequence.lean#L166). The attribute's comment: “Ker(d) and Coker(d) are the constant sheaves on C'\_\{B/A}”.

> **Stacks 09D5**, the outer terms of the sequence are the constant sheaves on `C'_{B/A}`:
> for any morphism `f : P ⟶ P'` of extensions of `B` over `A`, the left-hand map
> `H₁(L_{B/A}) ⟶ J/J²` is carried to the one of `P'` by `f`, and the right-hand map
> `Ω_{P/A} ⊗_P B ⟶ Ω[B⁄A]` is the composite of `f` with the one of `P'`. Hence the identifications
> `Ker(d) = H₁(L_{B/A})` and `Coker(d) = Ω[B⁄A]` of
> `Stacks.Cotangent.surjectivePresentation_exact` do not depend on the object.

```lean
theorem outerTerms_constant {P P' : Algebra.Extension.{w} A B} (f : P.Hom P') :
    Algebra.Extension.Cotangent.map f ∘ₗ h1CotangentIncl P = h1CotangentIncl P' ∧
      P'.toKaehler ∘ₗ Algebra.Extension.CotangentSpace.map f = P.toKaehler
```

**`Stacks.Cotangent.cokerCotangentComplexIsoHomologyZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectivePresentationSequence.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SurjectivePresentationSequence.lean#L202). The attribute's comment: “Coker(d) = H₀(L\_\{B/A})”.

> **Stacks 09D5**, the right-hand term of the sequence is `H₀(L_{B/A})`: at an object
> `α : P → B` of `C'_{B/A}` the cokernel of `d : J/J² → Ω_{P/A} ⊗_P B` is the degree-zero homology
> of the cotangent complex of Tag 08PN, by Tag 08QF.

```lean
def cokerCotangentComplexIsoHomologyZero (P : Algebra.Extension.{max u v} A B) :
    ModuleCat.of (B : Type (max u v))
        (P.CotangentSpace ⧸ LinearMap.range P.cotangentComplex) ≅
      (CommAlgCat.cotangentComplex A B).homology 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.11, Tag 08R6](https://stacks.math.columbia.edu/tag/08R6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
