---
declaration: section
origin: cited
lean: Stacks.Chow.zeroDivisor_isEffectiveCartierDivisor, Stacks.Chow.infinityDivisor_isEffectiveCartierDivisor, Stacks.Chow.exists_familyFibreDifferences, Stacks.Chow.fibreCycles_rationallyEquivalent, Stacks.Chow.familyFibreDifferencesRationallyEquivalentToZero, Stacks.Chow.cycleAssociatedToFibres_rationallyEquivalent_of_isEmbeddedPoint, Stacks.Chow.cycleAssociatedToFibres_rationallyEquivalent, Stacks.Chow.cycleAssociatedToCoherentFibres_rationallyEquivalent_of_decompositionRule
statement: formalized
proof: formalized
---

# 42.21 Rational equivalence and the projective line

Section 42.21 of the Stacks Project, [Tag 02S3](https://stacks.math.columbia.edu/tag/02S3). 3 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02S4, a lemma

[Tag 02S4](https://stacks.math.columbia.edu/tag/02S4) in the Stacks Project.

**`Stacks.Chow.zeroDivisor_isEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FamilyFibreDivisors/LocallyPrincipal.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FamilyFibreDivisors/LocallyPrincipal.lean#L120). The attribute's comment: “part (1): zero divisor”.

> **Stacks Project, Tag 02S4, part (1), for the zero divisor.** If `W` is integral and is not
> contained in the image of the zero section, then the zero divisor of `W` is an effective Cartier
> divisor on `W`.

```lean
theorem zeroDivisor_isEffectiveCartierDivisor [IsIntegral W.subscheme]
    (h : ¬ Set.range W.subschemeι ⊆ Set.range (zeroSection f)) :
    Stacks.Divisors.IsEffectiveCartierDivisor (zeroDivisor f W)
```

**`Stacks.Chow.infinityDivisor_isEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FamilyFibreDivisors/LocallyPrincipal.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FamilyFibreDivisors/LocallyPrincipal.lean#L170). The attribute's comment: “part (1): infinity divisor”.

> **Stacks Project, Tag 02S4, part (1), for the infinity divisor.** If `W` is integral and is
> not contained in the image of the infinity section, then the infinity divisor of `W` is an
> effective Cartier divisor on `W`.

```lean
theorem infinityDivisor_isEffectiveCartierDivisor [IsIntegral W.subscheme]
    (h : ¬ Set.range W.subschemeι ⊆ Set.range (infinitySection f)) :
    Stacks.Divisors.IsEffectiveCartierDivisor (infinityDivisor f W)
```

**`Stacks.Chow.exists_familyFibreDifferences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FibreCycles/FamilyFibreDifferenceExistence.lean, line 584](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FibreCycles/FamilyFibreDifferenceExistence.lean#L584). The attribute's comment: “part (4)”.

> **Stacks Project, Tag 02S4, part (4).** A `k`-cycle rationally equivalent to zero is the
> total fibre difference of a locally finite family of integral closed subschemes of
> `X ×_S 𝐏¹_S`, each of relative dimension `k + 1` at its generic points and contained in
> neither distinguished section.
>
> This is the converse of part (3): the family is produced from the family of integral closed
> subschemes and rational functions witnessing rational equivalence, by replacing each member by
> the closure of the graph of its rational function, read inside `X ×_S 𝐏¹_S`. The index type is
> unchanged.

```lean
theorem exists_familyFibreDifferences (k : ℤ) (α : CycleGroup C f k)
    (hα : IsRationallyEquivalentToZero C f k α) :
    ∃ (J : Type u) (W : J → (projectiveLineProduct f).IdealSheafData),
      (∀ j, IsIntegral (W j).subscheme) ∧
      (∀ j, ∀ ξ : genericPoints (W j).subscheme,
        relativeDimension C.dimensionFunction (familyBase f (W j)) ξ.1 = k + 1) ∧
      (∀ j, ¬ Set.range (W j).subschemeι ⊆ Set.range (zeroSection f)) ∧
      (∀ j, ¬ Set.range (W j).subschemeι ⊆ Set.range (infinitySection f)) ∧
      LocallyFinite (fun j ↦ ((W j).support : Set (projectiveLineProduct f))) ∧
      (∀ x : X, α.1 x = familyFibreDifferenceCoefficient C f k W x)
```

**`Stacks.Chow.fibreCycles_rationallyEquivalent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardPrincipal/DimensionDropApplications.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardPrincipal/DimensionDropApplications.lean#L221). The attribute's comment: “part (2)”.

> **Stacks 02S4 part (2), in the two-cycle form the tag states.**

```lean
theorem fibreCycles_rationallyEquivalent
    (W : (projectiveLineProduct f).IdealSheafData) [IsIntegral W.subscheme]
    (hDim : ∀ ξ : genericPoints W.subscheme,
      relativeDimension C.dimensionFunction (familyBase f W) ξ.1 = k + 1)
    (h₀ : ¬ Set.range W.subschemeι ⊆ Set.range (zeroSection f))
    (hInf : ¬ Set.range W.subschemeι ⊆ Set.range (infinitySection f)) :
    RationallyEquivalent C f k
      (cycleAssociatedToClosedSubscheme C f (zeroFiber f W).subschemeι k)
      (cycleAssociatedToClosedSubscheme C f (infinityFiber f W).subschemeι k)
```

**`Stacks.Chow.familyFibreDifferencesRationallyEquivalentToZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardPrincipal/DimensionDropApplications.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardPrincipal/DimensionDropApplications.lean#L236). The attribute's comment: “part (3)”.

> **Stacks 02S4 part (3).** The family form, for a locally finite family of integral closed
> subschemes of `X ×_S ℙ¹_S`.

```lean
theorem familyFibreDifferencesRationallyEquivalentToZero :
    FamilyFibreDifferencesRationallyEquivalentToZero C f k
```

## Tag 02S5, a lemma

[Tag 02S5](https://stacks.math.columbia.edu/tag/02S5) in the Stacks Project.

**`Stacks.Chow.cycleAssociatedToFibres_rationallyEquivalent_of_isEmbeddedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FibreCycles/EmbeddedPointHypothesis.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FibreCycles/EmbeddedPointHypothesis.lean#L206).

> **Stacks 02S5, with hypothesis (3) in the shape the source states it.** For a closed
> subscheme `Z ⊆ X ×_S 𝐏¹_S` with `dim_δ(Z) ≤ k + 1` and `dim_δ(Z₀) ≤ k`, `dim_δ(Z_∞) ≤ k`, the
> cycles of the two fibres are rationally equivalent on `X` as soon as
>
> * `hEmbedded`, the source's hypothesis (3): every embedded point of `Z` either misses both
>   distinguished sections or has relative dimension below `k`; and
> * `hGeneric`, the clause the source omits: no irreducible component of `Z` of relative dimension
>   exactly `k` has its generic point on a distinguished section.
>
> `hGeneric` cannot be dropped — see the module documentation for an integral `Z` with no embedded
> points at all for which the conclusion fails. Together the two clauses give the hypothesis of
> `Stacks.Chow.cycleAssociatedToFibres_rationallyEquivalent`, by
> `Stacks.Chow.sectionAvoidance_of_isEmbeddedPoint_of_genericPoints`, and are given by it, by
> `Stacks.Chow.mem_schemeAssociatedPoints_of_isEmbeddedPoint` and
> `AlgebraicGeometry.mem_schemeAssociatedPoints_of_isGenericPoint_irreducibleComponent`.

```lean
theorem cycleAssociatedToFibres_rationallyEquivalent_of_isEmbeddedPoint
    (hZ : ∀ ζ : Z.subscheme,
      relativeDimension C.dimensionFunction (familyBase f Z) ζ ≤ k + 1)
    (h₀ : schemeDeltaDimension C ((zeroFiber f Z).subschemeι ≫ f) ≤ (k : EInt))
    (hInf : schemeDeltaDimension C ((infinityFiber f Z).subschemeι ≫ f) ≤ (k : EInt))
    (hEmbedded : ∀ ζ : Z.subscheme, AlgebraicGeometry.IsEmbeddedPoint Z.subscheme ζ →
      ((Z.subschemeι ζ ∉ Set.range (zeroSection f) ∧
          Z.subschemeι ζ ∉ Set.range (infinitySection f)) ∨
        relativeDimension C.dimensionFunction (familyBase f Z) ζ < k))
    (hGeneric : ∀ ζ : Z.subscheme, ζ ∈ genericPoints Z.subscheme →
      relativeDimension C.dimensionFunction (familyBase f Z) ζ = k →
      (Z.subschemeι ζ ∉ Set.range (zeroSection f) ∧
        Z.subschemeι ζ ∉ Set.range (infinitySection f))) :
    RationallyEquivalent C f k
      (cycleAssociatedToClosedSubscheme C f (zeroFiber f Z).subschemeι k)
      (cycleAssociatedToClosedSubscheme C f (infinityFiber f Z).subschemeι k)
```

**`Stacks.Chow.cycleAssociatedToFibres_rationallyEquivalent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardPrincipal/DimensionDropApplications.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardPrincipal/DimensionDropApplications.lean#L258).

> **Stacks 02S5.** For a closed subscheme `Z ⊆ X ×_S ℙ¹_S` whose relative dimension is at most
> `k + 1`, whose two fibres have delta-dimension at most `k`, and each of whose associated points
> either misses both distinguished sections or has relative dimension below `k`, the cycles of the
> two fibres are rationally equivalent on `X`.
>
> Both inputs are now theorems: the decomposition rule is
> `Stacks.Chow.fibreCycleComponentDecompositionRule` and part (2) of Stacks 02S4 is
> `Stacks.Chow.fibreCyclesRationallyEquivalentWithin`.
>
> The source states its hypothesis (3) for the *embedded* points of `Z` rather than for all of
> its associated points. That reading is strictly weaker and the lemma is false under it; the two
> differ exactly at the generic points of the irreducible components of `Z` of relative dimension
> `k`, which the source's proof silently assumes away when it reads `dim(A/I) = 1` off
> `δ(ξ) = k`. `Stacks.Chow.cycleAssociatedToFibres_rationallyEquivalent_of_isEmbeddedPoint`
> (`StacksFrontier/AlgebraicGeometry/Chow/FibreCycles/EmbeddedPointHypothesis.lean`) states the
> hypothesis in the source's two-clause shape and documents the counterexample.

```lean
theorem cycleAssociatedToFibres_rationallyEquivalent
    (Z : (projectiveLineProduct f).IdealSheafData)
    (hZ : ∀ ζ : Z.subscheme,
      relativeDimension C.dimensionFunction (familyBase f Z) ζ ≤ k + 1)
    (h₀ : schemeDeltaDimension C ((zeroFiber f Z).subschemeι ≫ f) ≤ (k : EInt))
    (hInf : schemeDeltaDimension C ((infinityFiber f Z).subschemeι ≫ f) ≤ (k : EInt))
    (hAssociated : ∀ ζ : Z.subscheme,
      ζ ∈ Stacks.Divisors.schemeAssociatedPoints Z.subscheme →
      ((Z.subschemeι ζ ∉ Set.range (zeroSection f) ∧
          Z.subschemeι ζ ∉ Set.range (infinitySection f)) ∨
        relativeDimension C.dimensionFunction (familyBase f Z) ζ < k)) :
    RationallyEquivalent C f k
      (cycleAssociatedToClosedSubscheme C f (zeroFiber f Z).subschemeι k)
      (cycleAssociatedToClosedSubscheme C f (infinityFiber f Z).subschemeι k)
```

## Tag 02S6, a lemma

[Tag 02S6](https://stacks.math.columbia.edu/tag/02S6) in the Stacks Project.

**`Stacks.Chow.cycleAssociatedToCoherentFibres_rationallyEquivalent_of_decompositionRule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FibreCycles/CoherentFibreComparison.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FibreCycles/CoherentFibreComparison.lean#L345). The attribute's comment: “all three hypotheses and the conclusion, with hypothesis (3) quantified over every associated point of F, as the source's own proof of this lemma uses it ('since ξ is not an associated point of F by assumption (3)'). The published statement of the tag quantifies (3) over the embedded associated points only; that reading is false, by the counterexample in the module documentation, so it is not what is registered here”.

> **Stacks Tag 02S6.** For a coherent sheaf `F` on `X ×_S 𝐏¹_S` whose support has relative
> dimension at most `k + 1`, whose two fibres have delta-dimension at most `k`, and each of whose
> associated points either misses both distinguished sections or has relative dimension below `k`,
> the cycles `[F₀]_k` and `[F_∞]_k` of the two fibres are rationally equivalent.
>
> The two inputs are `Stacks.Chow.coherentFibreCycleDecompositionRule`, the claim in the source's
> proof, and `Stacks.Chow.familyFibreDifferencesRationallyEquivalentToZero`, Tag 02S4 part (3).

```lean
theorem cycleAssociatedToCoherentFibres_rationallyEquivalent_of_decompositionRule
    [F.IsCoherent]
    (hSupp : ∀ ξ : projectiveLineProduct f, ξ ∈ SheafOfModules.supp F →
      relativeDimension C.dimensionFunction (productBase f) ξ ≤ k + 1)
    (h₀ : schemeDeltaDimension C ((reducedSupport (zeroFibreModule f F)).subschemeι ≫ f)
      ≤ (k : EInt))
    (hInf : schemeDeltaDimension C ((reducedSupport (infinityFibreModule f F)).subschemeι ≫ f)
      ≤ (k : EInt))
    (hAssociated : ∀ ξ : projectiveLineProduct f, ξ ∈ Stacks.Divisors.associatedPoints F →
      ((ξ ∉ Set.range (zeroSection f) ∧ ξ ∉ Set.range (infinitySection f)) ∨
        relativeDimension C.dimensionFunction (productBase f) ξ < k)) :
    RationallyEquivalent C f k
      (cycleAssociatedToCoherentSheaf C f (zeroFibreModule f F) k h₀)
      (cycleAssociatedToCoherentSheaf C f (infinityFibreModule f F) k hInf)
```

**`Stacks.Chow.rationallyEquivalent_cycleAssociatedToCoherentSheaf_fibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FibreCycles/CoherentFibreRationalEquivalence.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FibreCycles/CoherentFibreRationalEquivalence.lean#L59).

> **Stacks 02S6.** Let `F` be a coherent sheaf on `X ×_S 𝐏¹_S` with
> `dim_δ(Supp(F)) ≤ k + 1`, with `dim_δ(Supp(F₀)) ≤ k` and `dim_δ(Supp(F_∞)) ≤ k`, and such that
> every associated point `ξ` of `F` lies outside the union of the two distinguished sections or has
> `δ(ξ) < k`. Then `[F₀]_k` and `[F_∞]_k` are rationally equivalent `k`-cycles on `X`.
>
> The coherence of `F₀` and `F_∞`, needed to form their cycles, is Stacks 0EBF and is supplied in
> the statement rather than assumed.

```lean
theorem rationallyEquivalent_cycleAssociatedToCoherentSheaf_fibres
    (F : (projectiveLineProduct f).Modules) [F.IsCoherent]
    (hSupp : schemeDeltaDimension C ((reducedSupport F).subschemeι ≫ productBase f) ≤
      ((k + 1 : ℤ) : EInt))
    (h₀ : haveI := isCoherent_zeroFibreModule C f F
      schemeDeltaDimension C ((reducedSupport (zeroFibreModule f F)).subschemeι ≫ f) ≤
        (k : EInt))
    (hInf : haveI := isCoherent_infinityFibreModule C f F
      schemeDeltaDimension C ((reducedSupport (infinityFibreModule f F)).subschemeι ≫ f) ≤
        (k : EInt))
    (hAssociated : ∀ ξ ∈ Stacks.Divisors.associatedPoints F,
      ξ ∉ Set.range (zeroSection f) ∪ Set.range (infinitySection f) ∨
        relativeDimension C.dimensionFunction (productBase f) ξ < k) :
    haveI := isCoherent_zeroFibreModule C f F
    haveI := isCoherent_infinityFibreModule C f F
    RationallyEquivalent C f k
      (cycleAssociatedToCoherentSheaf C f (zeroFibreModule f F) k h₀)
      (cycleAssociatedToCoherentSheaf C f (infinityFibreModule f F) k hInf)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.21, Tag 02S3](https://stacks.math.columbia.edu/tag/02S3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
