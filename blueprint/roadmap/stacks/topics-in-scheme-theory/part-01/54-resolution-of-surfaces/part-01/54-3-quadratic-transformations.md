---
declaration: section
origin: cited
lean: Stacks.Blowup.exists_isClosedImmersion_isPullback_projectiveLine_blowUpSpec_maximalIdeal, Stacks.Blowup.exists_isClosedImmersion_blowUpSpec_maximalIdeal, Stacks.Blowup.exists_isClosedImmersion_blowUpSpec_maximalIdeal_exceptional_projectiveLine, AlgebraicGeometry.irreducibleSpace_blowUp_maximalIdeal, AlgebraicGeometry.isRegular_blowUp_maximalIdeal, AlgebraicGeometry.isRegular_and_topologicalKrullDim_blowUp_vanishingIdeal_singleton, AlgebraicGeometry.isRegular_blowUp_vanishingIdeal_of_isRegular, AlgebraicGeometry.subsingleton_picardGroup_compl_exceptionalIdeal
statement: formalized
proof: formalized
---

# 54.3 Quadratic transformations

Section 54.3 of the Stacks Project, [Tag 0AGP](https://stacks.math.columbia.edu/tag/0AGP). 6 tags here are carried by 31 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AGQ, a lemma

[Tag 0AGQ](https://stacks.math.columbia.edu/tag/0AGQ) in the Stacks Project.

**`Stacks.Blowup.exists_isClosedImmersion_isPullback_projectiveLine_blowUpSpec_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ProjectiveLineExceptional.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/ProjectiveLineExceptional.lean#L345). The attribute's comment: “part (1)”.

> Let `(A, 𝔪, κ)` be a regular local ring of dimension two and let `X ⟶ Spec A` be the blowup of
> `Spec A` in `𝔪`. There is a closed immersion `r : X ⟶ 𝐏¹_{Spec A}` over `Spec A` whose restriction
> to the exceptional divisor is an isomorphism `E ≅ 𝐏¹_κ`.
>
> The exceptional divisor is the fibre `E = X ×_{Spec A} Spec κ`, so the last clause is stated as:
> there is a morphism `s : 𝐏¹_κ ⟶ X` over `Spec κ ⟶ Spec A` making `𝐏¹_κ` that fibre — the cartesian
> square — whose composite with `r` is the standard closed immersion `𝐏¹_κ ⟶ 𝐏¹_{Spec A}` given by
> reduction of coefficients. The cartesian square says that `s` induces an isomorphism `𝐏¹_κ ≅ E`,
> and the identity says that this isomorphism is the one induced by `r`, that is `(r|_E)⁻¹`.
>
> Here `𝐏¹_κ` is `Proj κ[T₀,T₁]`, and `r` is the closed immersion of
> `Stacks.Blowup.exists_isClosedImmersion_blowUpSpec_maximalIdeal`.

```lean
theorem exists_isClosedImmersion_isPullback_projectiveLine_blowUpSpec_maximalIdeal
    (A : Type u) [CommRing A] [IsRegularLocalRing A] (hdim : ringKrullDim A = 2) :
    ∃ r : blowUpSpec (IsLocalRing.maximalIdeal A) ⟶
        AlgebraicGeometry.Proj (MvPolynomial.homogeneousSubmodule (Fin 2) A),
      IsClosedImmersion r ∧
        r ≫ projSpaceToSpec A 2 = toSpec (IsLocalRing.maximalIdeal A) ∧
        ∃ s : AlgebraicGeometry.Proj (MvPolynomial.homogeneousSubmodule (Fin 2)
              (IsLocalRing.ResidueField A)) ⟶
            blowUpSpec (IsLocalRing.maximalIdeal A),
          IsPullback s (projSpaceToSpec (IsLocalRing.ResidueField A) 2)
              (toSpec (IsLocalRing.maximalIdeal A))
              (Spec.map (CommRingCat.ofHom (IsLocalRing.residue A))) ∧
            s ≫ r = Proj.map
                (Stacks.ProjectiveCohomology.polyGradedMap (Fin 2) (IsLocalRing.residue A))
                (Stacks.ProjectiveCohomology.irrelevant_le_map_polyGradedMap (Fin 2)
                  (IsLocalRing.residue A))
```

**`Stacks.Blowup.exists_isClosedImmersion_blowUpSpec_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ProjectiveSpaceEmbedding.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/ProjectiveSpaceEmbedding.lean#L324). The attribute's comment: “the closed immersion of the blowup into the projective line over the base”.

> **Stacks Project, Tag 0AGQ.** Let `A` be a regular local ring of dimension two and let
> `X ⟶ Spec A` be the blowup of `Spec A` in its maximal ideal. There is a closed immersion
> `r : X ⟶ 𝐏¹_{Spec A}` over `Spec A`.
>
> The projective line over `Spec A` is `Proj A[T₀, T₁]`, the presentation the source uses.

```lean
theorem exists_isClosedImmersion_blowUpSpec_maximalIdeal (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (hdim : ringKrullDim A = 2) :
    ∃ r : blowUpSpec (IsLocalRing.maximalIdeal A) ⟶
        Proj (MvPolynomial.homogeneousSubmodule (Fin 2) A),
      IsClosedImmersion r ∧
        r ≫ projSpaceToSpec A 2 = toSpec (IsLocalRing.maximalIdeal A)
```

**`Stacks.Blowup.exists_isClosedImmersion_blowUpSpec_maximalIdeal_exceptional_projectiveLine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceProjectiveLine.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceProjectiveLine.lean#L86). The attribute's comment: “for the blowup X of Spec A in the maximal ideal of a regular local ring (A, m, kappa) of dimension 2, with exceptional divisor E: there is a closed immersion r : X -> P^1\_S = Proj A[T\_0, T\_1] over S = Spec A, and an isomorphism rho : E -> P^1\_kappa = Proj kappa[T\_0, T\_1] whose composite with the inclusion of the special fibre P^1\_kappa -> P^1\_S is r restricted to E, such that O\_X(E) = O\_X(-1) = r^* O\_\{P^1\_S}(-1), C\_\{E/X} = rho^* O\_\{P^1\_kappa}(1) and N\_\{E/X} = rho^* O\_\{P^1\_kappa}(-1)”.

> **The blowup of a regular local surface in its closed point embeds in `𝐏¹`.** Let `(A, 𝔪, κ)`
> be a regular local ring of dimension `2`, let `f : X = Proj (⨁ₙ 𝔪ⁿ) ⟶ S = Spec A` be the blowing up
> of `A` in `𝔪` and let `E ⊆ X` be its exceptional divisor. There is a closed immersion
> `r : X ⟶ 𝐏¹_S = Proj A[T₀, T₁]` over `S` such that
>
> 1. `r|_E : E ⟶ 𝐏¹_κ = Proj κ[T₀, T₁]` is an isomorphism: there is an isomorphism `ρ : E ≅ 𝐏¹_κ`
>    whose composite with the inclusion of the special fibre `𝐏¹_κ ⟶ 𝐏¹_S` is the restriction
>    `E ⟶ X ⟶ 𝐏¹_S` of `r`;
> 2. `𝒪_X(E) ≅ 𝒪_X(-1)` and `r^*𝒪_{𝐏¹_S}(-1) ≅ 𝒪_X(-1)`;
> 3. `𝒞_{E/X} ≅ ρ^*𝒪_{𝐏¹_κ}(1)` and `𝒩_{E/X} ≅ ρ^*𝒪_{𝐏¹_κ}(-1)`, with `ρ = r|_E` of (1).

```lean
theorem exists_isClosedImmersion_blowUpSpec_maximalIdeal_exceptional_projectiveLine
    (A : Type u) [CommRing A] [IsRegularLocalRing A] (hdim : ringKrullDim A = 2) :
    ∃ r : blowUpSpec (maximalIdeal A) ⟶ Proj (MvPolynomial.homogeneousSubmodule (Fin 2) A),
      IsClosedImmersion r ∧
      r ≫ projSpaceToSpec A 2 = toSpec (maximalIdeal A) ∧
      ∃ ρ : (exceptionalIdealData (maximalIdeal A)).subscheme ≅
          Proj (MvPolynomial.homogeneousSubmodule (Fin 2) (A ⧸ maximalIdeal A)),
        (exceptionalIdealData (maximalIdeal A)).subschemeι ≫ r =
          ρ.hom ≫ Proj.map
            (Stacks.ProjectiveCohomology.polyGradedMap (Fin 2)
              (Ideal.Quotient.mk (maximalIdeal A)))
            (Stacks.ProjectiveCohomology.irrelevant_le_map_polyGradedMap (Fin 2)
              (Ideal.Quotient.mk (maximalIdeal A))) ∧
        Nonempty (Stacks.Divisors.invertibleSheaf' (exceptionalIdealData (maximalIdeal A)) ≅
          twistingSheaf (reesGrading (maximalIdeal A)) (-1)) ∧
        Nonempty ((Scheme.Modules.pullback r).obj
            (twistingSheaf (MvPolynomial.homogeneousSubmodule (Fin 2) A) (-1)) ≅
          twistingSheaf (reesGrading (maximalIdeal A)) (-1)) ∧
        Nonempty (Stacks.Conormal.conormalSheaf
            (exceptionalIdealData (maximalIdeal A)).subschemeι ≅
          (Scheme.Modules.pullback ρ.hom).obj
            (twistingSheaf
              (MvPolynomial.homogeneousSubmodule (Fin 2) (A ⧸ maximalIdeal A)) 1)) ∧
        Nonempty (Stacks.Divisors.normalSheaf
            (exceptionalIdealData (maximalIdeal A)).subschemeι ≅
          (Scheme.Modules.pullback ρ.hom).obj
            (twistingSheaf
              (MvPolynomial.homogeneousSubmodule (Fin 2) (A ⧸ maximalIdeal A)) (-1)))
```

## Tag 0AGR, a lemma

[Tag 0AGR](https://stacks.math.columbia.edu/tag/0AGR) in the Stacks Project.

**`AlgebraicGeometry.irreducibleSpace_blowUp_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceBlowup.lean, line 499](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceBlowup.lean#L499). The attribute's comment: “irreducibility”.

> **Stacks Project, Tag 0AGR.** The blowup of a two-dimensional regular local ring at its
> closed point is irreducible.

```lean
public theorem irreducibleSpace_blowUp_maximalIdeal (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (hdim : ringKrullDim A = 2) :
    IrreducibleSpace (blowUp (Scheme.IdealSheafData.ofIdealTop
      (Ideal.map (Scheme.ΓSpecIso (CommRingCat.of A)).inv.hom (maximalIdeal A))))
```

**`AlgebraicGeometry.isRegular_blowUp_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceBlowup.lean, line 512](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceBlowup.lean#L512). The attribute's comment: “regularity”.

> **Stacks Project, Tag 0AGR.** The blowup of a two-dimensional regular local ring at its
> closed point is a regular scheme.

```lean
public theorem isRegular_blowUp_maximalIdeal (A : Type u) [CommRing A] [IsRegularLocalRing A]
    (hdim : ringKrullDim A = 2) :
    IsRegular (blowUp (Scheme.IdealSheafData.ofIdealTop
      (Ideal.map (Scheme.ΓSpecIso (CommRingCat.of A)).inv.hom (maximalIdeal A))))
```

**`AlgebraicGeometry.isRegular_and_topologicalKrullDim_blowUp_vanishingIdeal_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceBlowupGlobal.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceBlowupGlobal.lean#L335). The attribute's comment: “the globalization of the source's statement: the blowup of a regular Noetherian scheme of dimension two in a reduced closed point is regular of dimension two. The source's own statement, for the spectrum of a regular local ring of dimension two blown up at its closed point, is `AlgebraicGeometry.isRegular_blowUp_maximalIdeal`. The local ring at a closed point of such a scheme may have dimension `0`, `1` or `2`, and all three cases are treated; see the module docstring”. References: EGA IV (19.4.11), “(iii), special case”.

> **Stacks Project, Tag 0AGR, globally.** The blowup of a regular Noetherian scheme of
> dimension two in a reduced closed point is again regular of dimension two.
>
> The source states this for the spectrum of a regular local ring of dimension two blown up at its
> closed point, which is `AlgebraicGeometry.isRegular_blowUp_maximalIdeal`. Passing to a closed
> point of a scheme needs a case distinction on `ringKrullDim 𝒪_{Y,y}`, which may be `0`, `1` or
> `2`; see the module docstring.

```lean
public theorem isRegular_and_topologicalKrullDim_blowUp_vanishingIdeal_singleton
    (Y : Scheme.{u}) [IsNoetherian Y] (hreg : IsRegular Y)
    (hdim : topologicalKrullDim Y = 2) (y : Y) (hy : IsClosed ({y} : Set Y)) :
    IsRegular (blowUp (Scheme.IdealSheafData.vanishingIdeal (⟨{y}, hy⟩ : Closeds Y))) ∧
      topologicalKrullDim (blowUp (Scheme.IdealSheafData.vanishingIdeal
        (⟨{y}, hy⟩ : Closeds Y))) = 2
```

**`AlgebraicGeometry.isRegular_blowUp_vanishingIdeal_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/RegularPointBlowupRegular.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/RegularPointBlowupRegular.lean#L57). The attribute's comment: “regularity, relative form: the blowup of a regular scheme at a closed point whose local ring is regular of dimension two is regular. The absolute statement, for Spec of a two-dimensional regular local ring, is isRegular\_blowUp\_maximalIdeal”. References: EGA IV (19.4.11), “(iii), special case”.

> The blowup of a regular scheme at a closed point whose local ring is regular of dimension two
> is again a regular scheme. The case `X = Spec A`, for `A` a two-dimensional regular local ring
> and `w` its closed point, is `AlgebraicGeometry.isRegular_blowUp_maximalIdeal`.

```lean
theorem isRegular_blowUp_vanishingIdeal_of_isRegular {X : Scheme.{u}} (hX : IsRegular X) (w : X)
    (hw : IsClosed ({w} : Set X)) (hdim : ringKrullDim (X.presheaf.stalk w) = 2) :
    IsRegular (blowUp (Scheme.IdealSheafData.vanishingIdeal (⟨{w}, hw⟩ : Closeds X)))
```

## Tag 0C5G, a lemma

[Tag 0C5G](https://stacks.math.columbia.edu/tag/0C5G) in the Stacks Project.

**`AlgebraicGeometry.subsingleton_picardGroup_compl_exceptionalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/PicardGroup.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/PicardGroup.lean#L221). The attribute's comment: “the third step of the source's proof: triviality of the Picard group of the complement of the exceptional divisor”.

> **Stacks Project, Tag 0C5G, the third step of the source's proof.** Let `A` be a regular
> local ring and let `X ⟶ Spec A` be the blowup of `Spec A` in its maximal ideal, with exceptional
> divisor `E`. Then `Pic(X ∖ E)` is trivial.
>
> The blowup is an isomorphism over the complement of its centre (Tag 02OS), that complement is
> the punctured spectrum of `A`, and a regular local ring is a unique factorization domain, so the
> Picard group of its punctured spectrum vanishes (Tag 0F2H). No hypothesis on the dimension of
> `A` is used.

```lean
theorem subsingleton_picardGroup_compl_exceptionalIdeal (A : Type u) [CommRing A]
    [IsRegularLocalRing A] :
    Subsingleton (Scheme.Opens.toScheme (exceptionalIdeal (Scheme.IdealSheafData.ofIdealTop
      (Ideal.map (Scheme.ΓSpecIso (.of A)).inv.hom
        (IsLocalRing.maximalIdeal A)))).support.compl).picardGroup
```

**`AlgebraicGeometry.surjective_zsmul_picardClass_exceptionalIdealData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/PicardGroupGeneration.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/PicardGroupGeneration.lean#L151). The attribute's comment: “the generation half, with nothing assumed: every Picard class of the blowup of a regular local ring of dimension two in its maximal ideal is an integral multiple of the class of O\_X(E)”.

> **Stacks Project, Tag 0C5G, the generation half, with nothing assumed.** Let `(A, 𝔪, κ)` be a
> regular local ring of dimension two, let `X ⟶ Spec A` be the blowing up of `Spec A` in `𝔪` and
> let `E` be its exceptional divisor. Then every Picard class of `X` is an integral multiple of the
> class of `𝒪_X(E)`.
>
> `AlgebraicGeometry.surjective_zsmul_picardClass_of_subsingleton_picardGroup_compl` is applied to
> `E`. Its hypotheses are: `X` integral, locally Noetherian and normal, which transport along the
> identification of the affine blowup with the blowup of the ideal sheaf of the closed point, where
> they are [Stacks, Tag 0AGR] and properness over a Noetherian base; the closed subscheme of `E` is
> integral, being the projective line over `κ` by part (1) of [Stacks, Tag 0AGQ]; and `Pic(X ∖ E)`
> is trivial, which is
> `AlgebraicGeometry.subsingleton_picardGroup_compl_exceptionalIdeal` transported along the same
> identification, under which the two exceptional ideal sheaves correspond.

```lean
theorem surjective_zsmul_picardClass_exceptionalIdealData (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (hdim : ringKrullDim A = 2) :
    Function.Surjective fun n : ℤ => n • Stacks.Divisors.picardClass
      (Stacks.Blowup.exceptionalIdealData (maximalIdeal A))
```

**`AlgebraicGeometry.eq_zero_of_zsmul_picardClass_exceptionalIdealData_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/PicardGroupGeneration.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/PicardGroupGeneration.lean#L195). The attribute's comment: “the infinite-order half for the blowup of a regular local ring of dimension two in its maximal ideal, with nothing assumed: no nonzero multiple of the class of O\_X(E) vanishes in Pic(X)”.

> **Stacks Project, Tag 0C5G, the infinite-order half for the blowup itself.** Let `(A, 𝔪, κ)`
> be a regular local ring of dimension two, let `X ⟶ Spec A` be the blowing up of `Spec A` in `𝔪`
> and let `E` be its exceptional divisor. Then no nonzero multiple of the class of `𝒪_X(E)`
> vanishes in `Pic(X)`.
>
> `Scheme.IdealSheafData.IsExceptionalCurveOfFirstKind.eq_zero_of_zsmul_picardClass_eq_zero` proves
> this for an exceptional curve of the first kind, and `E` is one: parts (1) and (3) of
> [Stacks, Tag 0AGQ], read as the predicate by
> `Stacks.Blowup.exists_isExceptionalCurveOfFirstKind_exceptionalIdealData`.

```lean
theorem eq_zero_of_zsmul_picardClass_exceptionalIdealData_eq_zero (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (hdim : ringKrullDim A = 2) (n : ℤ)
    (hn : n • Stacks.Divisors.picardClass
      (Stacks.Blowup.exceptionalIdealData (maximalIdeal A)) = 0) :
    n = 0
```

**`AlgebraicGeometry.picardGroupEquivInt_blowUpSpec_maximalIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/PicardGroupGeneration.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/PicardGroupGeneration.lean#L218). The attribute's comment: “the identification Z ≃+ Pic(X) for the blowup of a regular local ring of dimension two in its maximal ideal, with nothing assumed: both halves, generation and infinite order, are proved for the exceptional divisor of this blowup”.

> **Stacks Project, Tag 0C5G.** Let `(A, 𝔪, κ)` be a regular local ring of dimension two and
> let `X ⟶ Spec A` be the blowing up of `Spec A` in `𝔪`, with exceptional divisor `E`. Then
> `n ↦ n • [𝒪_X(E)]` is an isomorphism `ℤ ≃+ Pic(X)`: so `Pic(X)` is infinite cyclic, generated by
> `𝒪_X(E)`.
>
> The map is injective because `[𝒪_X(E)]` has infinite order, which is
> `Scheme.IdealSheafData.IsExceptionalCurveOfFirstKind.eq_zero_of_zsmul_picardClass_eq_zero` applied
> to `E` through parts (1) and (3) of [Stacks, Tag 0AGQ], and surjective by
> `AlgebraicGeometry.surjective_zsmul_picardClass_exceptionalIdealData`. Nothing is assumed beyond
> regularity and dimension two.

```lean
def picardGroupEquivInt_blowUpSpec_maximalIdeal (A : Type u) [CommRing A] [IsRegularLocalRing A]
    (hdim : ringKrullDim A = 2) :
    ℤ ≃+ Stacks.Picard.ofScheme (Stacks.Blowup.blowUpSpec (maximalIdeal A))
```

**`AlgebraicGeometry.picardGroupEquivInt_blowUpSpec_maximalIdeal_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/PicardGroupGeneration.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/PicardGroupGeneration.lean#L229). The attribute's comment: “the generator clause for the blowup of a regular local ring of dimension two in its maximal ideal, with nothing assumed: the isomorphism carries 1 to the class of O\_X(E)”.

> The isomorphism `ℤ ≃+ Pic(X)` of the blowup carries `1` to the class of `𝒪_X(E)`, so
> `Pic(X)` is infinite cyclic on that class.

```lean
theorem picardGroupEquivInt_blowUpSpec_maximalIdeal_one (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (hdim : ringKrullDim A = 2) :
    picardGroupEquivInt_blowUpSpec_maximalIdeal A hdim 1 =
      Stacks.Divisors.picardClass
        (Stacks.Blowup.exceptionalIdealData (maximalIdeal A))
```

## Tag 0AGS, a lemma

[Tag 0AGS](https://stacks.math.columbia.edu/tag/0AGS) in the Stacks Project.

**`Stacks.Blowup.bijective_negSections_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceNegativeTwistSections.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceNegativeTwistSections.lean#L301). The attribute's comment: “part (4) for n < 0: for the blowup X of Spec A in the maximal ideal m of a regular local ring A of dimension two, the canonical A-linear map from A = m^0 to the global sections of O\_X(n) is bijective for every n < 0, which is Gamma(X, O\_X(n)) = m^(max 0 n) = A in that range”.

> Let `(A, 𝔪, κ)` be a regular local ring of dimension two and let `f : X ⟶ S = Spec A` be the
> blowing up of `A` in `𝔪`. For every `n < 0` the canonical `A`-linear map
>
> `A = 𝔪⁰ ⟶ Γ(X, 𝒪_X(0)) ⟶ Γ(X, 𝒪_X(n))`
>
> is bijective, which is the assertion `Γ(X, 𝒪_X(n)) = 𝔪^{max(0,n)} = 𝔪⁰ = A` in that range. The map
> is `Stacks.Blowup.negSections`: the canonical section map in degree `0` followed by the `(-n)`-fold
> inclusion `𝒪_X(0) ⊆ 𝒪_X(n)`.

```lean
theorem bijective_negSections_maximalIdeal (A : Type u) [CommRing A] [IsRegularLocalRing A]
    (hdim : ringKrullDim A = 2) {n : ℤ} (hn : n < 0) :
    Function.Bijective (negSections (maximalIdeal A) (-n).toNat
      (show n = ((0 : ℕ) : ℤ) - (((-n).toNat : ℕ) : ℤ) by omega))
```

**`Stacks.Blowup.bijective_maxSections_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceNegativeTwistSections.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceNegativeTwistSections.lean#L319). The attribute's comment: “part (4): for the blowup X of Spec A in the maximal ideal m of a regular local ring A of dimension two, the canonical A-linear map from m^(max 0 n) to the global sections of O\_X(n) is bijective for every integer n, i.e. H^0(X, O\_X(n)) = m^(max 0 n)”.

> Let `(A, 𝔪, κ)` be a regular local ring of dimension two and let `f : X ⟶ S = Spec A` be the
> blowing up of `A` in `𝔪`. For every `n : ℤ` the canonical `A`-linear map
>
> `𝔪^{max(0,n)} ⟶ Γ(X, 𝒪_X(max(0,n))) ⟶ Γ(X, 𝒪_X(n))`
>
> is bijective, which is the equality `H⁰(X, 𝒪_X(n)) = 𝔪^{max(0,n)}` read as an isomorphism of
> `A`-modules.

```lean
theorem bijective_maxSections_maximalIdeal (A : Type u) [CommRing A] [IsRegularLocalRing A]
    (hdim : ringKrullDim A = 2) (n : ℤ) :
    Function.Bijective (maxSections (maximalIdeal A) n)
```

**`Stacks.Blowup.bijective_ambientSections_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceTwistSections.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceTwistSections.lean#L383). The attribute's comment: “part (4) for n at least 0: for the blowup X of Spec A in the maximal ideal m of a regular local ring A of dimension two, the canonical map from m^n to the global sections of O\_X(n) is bijective, which is Gamma(X, O\_X(n)) = m^(max 0 n) in that range”.

> **Stacks Project, Tag 0AGS part (4) in nonnegative degrees.** Let `(A, 𝔪)` be a regular
> local ring of dimension two and let `X ⟶ Spec A` be the blowup of `Spec A` in `𝔪`. Then the
> canonical map `𝔪ⁿ ⟶ Γ(X, 𝒪_X(n))` is bijective for every `n : ℕ`, which is the assertion
> `Γ(X, 𝒪_X(n)) = 𝔪^{max(0,n)}` of the source in that range; through
> `Stacks.Blowup.sectionsIsoIdealPow` it is the isomorphism of `A`-modules the equality denotes.
>
> Injectivity is unconditional (`Stacks.Blowup.injective_ambientSections_maximalIdeal`), the Rees
> algebra of a nonzero ideal of a domain having no zero divisors. Surjectivity in degree `n ≥ 0` is
> `Stacks.Blowup.surjective_ambientSections_maximalIdeal`, where it comes from the identification
> of the ideal sheaf of the blowup inside `𝐏¹_A` with `𝒪(-1)` and the vanishing of
> `H¹(𝐏¹_A, 𝒪(n-1))` for `n ≥ 0`.
>
> The range `n < 0` of part (4), where the exponent `max(0,n)` is `0`, is
> `Stacks.Blowup.bijective_negSections_maximalIdeal`.

```lean
theorem bijective_ambientSections_maximalIdeal (A : Type u) [CommRing A] [IsRegularLocalRing A]
    (hdim : ringKrullDim A = 2) (n : ℕ) :
    Function.Bijective (ambientSections (maximalIdeal A) n)
```

**`AlgebraicGeometry.isZero_cohomology_of_two_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowup.lean, line 671](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowup.lean#L671). The attribute's comment: “higher\_cohomology\_vanishes”.

> **Stacks Project, Tag 0AGS.** Quasi-coherent cohomology of the blowup of a two-dimensional
> regular local ring at its closed point vanishes in degrees at least two.

```lean
public theorem isZero_cohomology_of_two_le
    (A : Type u) [CommRing A] [IsRegularLocalRing A]
    (hdim : ringKrullDim A = 2)
    (F : (AlgebraicGeometry.blowUp
      (Scheme.IdealSheafData.ofIdealTop
        (Ideal.map (Scheme.ΓSpecIso (.of A)).inv.hom
          (IsLocalRing.maximalIdeal A)))).Modules)
    [F.IsQuasicoherent] (p : ℕ) (hp : 2 ≤ p) :
    IsZero (((SheafOfModules.toSheaf
      (AlgebraicGeometry.blowUp
        (Scheme.IdealSheafData.ofIdealTop
          (Ideal.map (Scheme.ΓSpecIso (.of A)).inv.hom
            (IsLocalRing.maximalIdeal A)))).ringCatSheaf ⋙
        (sheafSections
          (Opens.grothendieckTopology
            (AlgebraicGeometry.blowUp
              (Scheme.IdealSheafData.ofIdealTop
                (Ideal.map (Scheme.ΓSpecIso (.of A)).inv.hom
                  (IsLocalRing.maximalIdeal A)))))
          AddCommGrpCat).obj (op (⊤ :
          (AlgebraicGeometry.blowUp
              (Scheme.IdealSheafData.ofIdealTop
                (Ideal.map (Scheme.ΓSpecIso (.of A)).inv.hom
                  (IsLocalRing.maximalIdeal A)))).Opens))).rightDerived p).obj F)
```

**`Stacks.ResolutionOfSurfaces.isZero_firstCohomology_of_generatingSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowupFirstCohomology.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowupFirstCohomology.lean#L257). The attribute's comment: “clause (3), for a module generated by global sections”.

> Let `A` be a regular local ring of dimension two and let `X ⟶ Spec(A)` be the blowup of
> `Spec(A)` in the maximal ideal. Then `H¹(X, ℱ) = 0` for every quasi-coherent `𝒪_X`-module `ℱ`
> generated by global sections.
>
> The presentation `⨁_{i ∈ σ.I} 𝒪_X ⟶ ℱ` by the generators has quasi-coherent kernel, `H¹`
> commutes with the direct sum because `X` is quasi-compact and quasi-separated, `H¹(X, 𝒪_X) = 0`,
> and `H²` vanishes on quasi-coherent modules by clause (1) of the same tag.

```lean
theorem isZero_firstCohomology_of_generatingSections
    (A : Type u) [CommRing A] [IsRegularLocalRing A] (hdim : ringKrullDim A = 2)
    (F : (AlgebraicGeometry.blowUp (Scheme.IdealSheafData.ofIdealTop
      (Ideal.map (Scheme.ΓSpecIso (CommRingCat.of A)).inv.hom
        (IsLocalRing.maximalIdeal A)))).Modules) [F.IsQuasicoherent]
    (σ : SheafOfModules.GeneratingSections F) :
    IsZero (((moduleGlobalSections (AlgebraicGeometry.blowUp
      (Scheme.IdealSheafData.ofIdealTop
        (Ideal.map (Scheme.ΓSpecIso (CommRingCat.of A)).inv.hom
          (IsLocalRing.maximalIdeal A))))).rightDerivedPlus 1).obj F)
```

**`Stacks.Blowup.length_firstCohomologySheafAsBaseModule_blowUpTwist_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowupTwistLength.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowupTwistLength.lean#L424). The attribute's comment: “part (5): length\_A H^1(X, O\_X(n)) = (-n)(-n-1)/2 for n < 0”.

> **Stacks Project, Tag 0AGS part (5).** Let `(A, 𝔪, κ)` be a regular local ring of dimension
> two and let `f : X ⟶ S = Spec A` be the blowing up of `A` in `𝔪`. Then for every `n < 0`$$ \text{length}_A H^1(X, \mathcal{O}_X(n)) = \frac{(-n)(-n-1)}{2}. $$
>
> The cohomology is read as an `A`-module through `f`, which is
> `AlgebraicGeometry.firstCohomologySheafAsBaseModule`.
>
> The proof is the source's descending induction. Part (2) of the tag
> (`Stacks.Blowup.isZero_hgroup_one_twistingSheaf_maximalIdeal`) anchors it at `n = -1`, where the
> length is zero. The step is the long exact cohomology sequence of
> `0 → 𝒪_X(n) → 𝒪_X(n-1) → i_*𝒪_E(n-1) → 0`
> (`Stacks.Blowup.shortExact_twist_exceptional`), which in degree one collapses to a short exact
> sequence: the connecting map out of `H⁰(X, i_*𝒪_E(n-1))` vanishes because that module is zero,
> and the one into `H²(X, 𝒪_X(n))` vanishes by part (1) of the tag. The middle term is
> `H¹(𝐏¹_κ, 𝒪(n-1))`, of length `-n` by [Stacks, Tag 01XT]
> (`Stacks.ProjectiveSpace.Cohomology.length_twistCohomology_line_top`) through the identification
> `E ≅ 𝐏¹_κ` of part (1) of [Stacks, Tag 0AGQ]; the lengths therefore satisfy
> `𝓁 H¹(𝒪_X(n-1)) = 𝓁 H¹(𝒪_X(n)) + (-n)`, which is the recursion for `C(-n, 2)`.
>
> Finite length is not assumed: it is a by-product of the induction, since the formula gives a
> natural number at every stage.

```lean
theorem length_firstCohomologySheafAsBaseModule_blowUpTwist_maximalIdeal (A : Type u)
    [CommRing A] [IsRegularLocalRing A] (hdim : ringKrullDim A = 2) {n : ℤ} (hn : n < 0) :
    Module.length A (AlgebraicGeometry.firstCohomologySheafAsBaseModule
        (blowUpSpec (maximalIdeal A)) (toSpec (maximalIdeal A))
        (blowUpTwist (maximalIdeal A) n))
      = ((((-n) * (-n - 1) / 2).toNat : ℕ) : ℕ∞)
```

**`Stacks.Blowup.isZero_hgroup_one_twistingSheaf_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowupTwists.lean, line 418](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowupTwists.lean#L418). The attribute's comment: “part (2): H^1(X, O\_X(n)) = 0 for n at least -1”.

> **Stacks Project, Tag 0AGS part (2).** Let `(A, 𝔪, κ)` be a regular local ring of dimension
> two and let `f : X ⟶ S = Spec A` be the blowing up of `A` in `𝔪`. Then
>
> `H¹(X, 𝒪_X(n)) = 0` for every `n ≥ -1`.
>
> The maximal ideal of a two-dimensional regular local ring is generated by two elements, so
> `Stacks.Blowup.isZero_hgroup_one_twistingSheaf_of_two_generators` applies.

```lean
theorem isZero_hgroup_one_twistingSheaf_maximalIdeal (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (hdim : ringKrullDim A = 2) {n : ℤ} (hn : -1 ≤ n) :
    IsZero (Hgroup (blowUpSpec (IsLocalRing.maximalIdeal A)).ringCatSheaf ⊤ 1
      (twistingSheaf (reesGrading (IsLocalRing.maximalIdeal A)) n))
```

**`Stacks.Blowup.isZero_hgroup_one_of_generatingSections_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowupTwists.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowupTwists.lean#L436). The attribute's comment: “part (3), the case where F itself is globally generated”.

> **Stacks Project, Tag 0AGS part (3), the globally generated case.** Let `(A, 𝔪, κ)` be a
> regular local ring of dimension two and let `f : X ⟶ S = Spec A` be the blowing up of `A` in
> `𝔪`. If a quasi-coherent `𝒪_X`-module `ℱ` is globally generated then `H¹(X, ℱ) = 0`.
>
> Global generation is `SheafOfModules.GeneratingSections`: a family of global sections whose
> associated morphism out of the free module on them is an epimorphism. This is the first of the
> two cases of the source's clause; the second is
> `Stacks.Blowup.isZero_hgroup_one_of_generatingSections_twist_maximalIdeal`, and the clause itself
> is `Stacks.Blowup.isZero_hgroup_one_of_generatingSections_or_twist_maximalIdeal`.

```lean
theorem isZero_hgroup_one_of_generatingSections_maximalIdeal (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (hdim : ringKrullDim A = 2)
    (F : (blowUpSpec (IsLocalRing.maximalIdeal A)).Modules) [F.IsQuasicoherent]
    (σ : _root_.SheafOfModules.GeneratingSections F) :
    IsZero (Hgroup (blowUpSpec (IsLocalRing.maximalIdeal A)).ringCatSheaf ⊤ 1 F)
```

**`Stacks.Blowup.isZero_hgroup_one_of_generatingSections_twist_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowupTwists.lean, line 453](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowupTwists.lean#L453). The attribute's comment: “part (3), the case where F(1) is globally generated”.

> **Stacks Project, Tag 0AGS part (3), the case where `ℱ(1)` is globally generated.** Let
> `(A, 𝔪, κ)` be a regular local ring of dimension two and let `f : X ⟶ S = Spec A` be the blowing
> up of `A` in `𝔪`. If `ℱ` is a quasi-coherent `𝒪_X`-module whose twist `ℱ(1)` is globally
> generated then `H¹(X, ℱ) = 0`.
>
> The maximal ideal of a two-dimensional regular local ring is generated by two elements, so
> `Stacks.Blowup.isZero_hgroup_one_of_generatingSections_twist_of_two_generators` applies.

```lean
theorem isZero_hgroup_one_of_generatingSections_twist_maximalIdeal (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (hdim : ringKrullDim A = 2)
    (F : (blowUpSpec (IsLocalRing.maximalIdeal A)).Modules) [F.IsQuasicoherent]
    (σ : _root_.SheafOfModules.GeneratingSections
      (twistSheafOfModules (reesGrading (IsLocalRing.maximalIdeal A)) F 1)) :
    IsZero (Hgroup (blowUpSpec (IsLocalRing.maximalIdeal A)).ringCatSheaf ⊤ 1 F)
```

**`Stacks.Blowup.isZero_hgroup_one_of_generatingSections_or_twist_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowupTwists.lean, line 477](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowupTwists.lean#L477). The attribute's comment: “part (3): H^1(X,F) = 0 if F or F(1) is globally generated”.

> **Stacks Project, Tag 0AGS part (3).** Let `(A, 𝔪, κ)` be a regular local ring of dimension
> two and let `f : X ⟶ S = Spec A` be the blowing up of `A` in `𝔪`. Then, for a quasi-coherent
> `𝒪_X`-module `ℱ`,
>
> `H¹(X, ℱ) = 0` if `ℱ` or `ℱ(1)` is globally generated.
>
> The two cases are
> `Stacks.Blowup.isZero_hgroup_one_of_generatingSections_maximalIdeal` and
> `Stacks.Blowup.isZero_hgroup_one_of_generatingSections_twist_maximalIdeal`. Global generation of
> a module sheaf is the existence of a `SheafOfModules.GeneratingSections` for it — a family of
> global sections whose associated morphism out of the free module on them is an epimorphism — and
> since that is data rather than a proposition the disjunction is taken between its two
> `Nonempty`s.

```lean
theorem isZero_hgroup_one_of_generatingSections_or_twist_maximalIdeal (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (hdim : ringKrullDim A = 2)
    (F : (blowUpSpec (IsLocalRing.maximalIdeal A)).Modules) [F.IsQuasicoherent]
    (hσ : Nonempty (_root_.SheafOfModules.GeneratingSections F) ∨
      Nonempty (_root_.SheafOfModules.GeneratingSections
        (twistSheafOfModules (reesGrading (IsLocalRing.maximalIdeal A)) F 1))) :
    IsZero (Hgroup (blowUpSpec (IsLocalRing.maximalIdeal A)).ringCatSheaf ⊤ 1 F)
```

**`AlgebraicGeometry.isZero_cohomology_one_twistingSheaf_of_neg_one_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowupTwistVanishing.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowupTwistVanishing.lean#L39). The attribute's comment: “part (2)”.

> For `(A, 𝔪, κ)` a regular local ring of dimension two and
> `X = Stacks.Blowup.blowUpSpec 𝔪 = Proj(⨁ₙ 𝔪ⁿ)` the blowup of `Spec A` in `𝔪`,
> `H¹(X, 𝒪_X(n)) = 0` for every `n ≥ -1`.

```lean
public theorem isZero_cohomology_one_twistingSheaf_of_neg_one_le
    (A : Type u) [CommRing A] [IsRegularLocalRing A] (hdim : ringKrullDim A = 2)
    (n : ℤ) (hn : -1 ≤ n) :
    IsZero (_root_.Hgroup
      (Stacks.Blowup.blowUpSpec (IsLocalRing.maximalIdeal A)).ringCatSheaf ⊤ 1
      (ProjectiveSpectrum.Proj.twistingSheaf
        (Stacks.Blowup.reesGrading (IsLocalRing.maximalIdeal A)) n))
```

**`AlgebraicGeometry.isZero_cohomology_one_of_generatingSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowupTwistVanishing.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Vanishing/RegularLocalBlowupTwistVanishing.lean#L53). The attribute's comment: “part (3), for a globally generated quasi-coherent module”.

> For `(A, 𝔪, κ)` a regular local ring of dimension two, `X = Stacks.Blowup.blowUpSpec 𝔪` the
> blowup of `Spec A` in `𝔪` and `ℱ` a quasi-coherent `𝒪_X`-module generated by global sections
> (`SheafOfModules.GeneratingSections`), `H¹(X, ℱ) = 0`.

```lean
public theorem isZero_cohomology_one_of_generatingSections
    (A : Type u) [CommRing A] [IsRegularLocalRing A] (hdim : ringKrullDim A = 2)
    (F : (Stacks.Blowup.blowUpSpec (IsLocalRing.maximalIdeal A)).Modules)
    (hF : F.IsQuasicoherent) (σ : F.GeneratingSections) :
    IsZero (_root_.Hgroup
      (Stacks.Blowup.blowUpSpec (IsLocalRing.maximalIdeal A)).ringCatSheaf ⊤ 1 F)
```

## Tag 0AGT, a lemma

[Tag 0AGT](https://stacks.math.columbia.edu/tag/0AGT) in the Stacks Project.

**`Stacks.Blowup.Colength.length_globalSections_ge_sum_length_stalkQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Colength/LocalBound.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/Colength/LocalBound.lean#L268). The attribute's comment: “clause (3), the second inequality: the length over the base ring of the global sections of the quotient is at least the sum over the support points of the colengths of the stalks”.

> The length over the base ring of a finite-support quotient is bounded
> below by the sum of the colengths of its stalks.

```lean
public theorem length_globalSections_ge_sum_length_stalkQuotient
    {A : Type*} [CommRing A] {X : Scheme}
    (f : X ⟶ Spec (.of A)) (I : X.IdealSheafData)
    (T : Finset X)
    (hT : (I.support : Set X) = (T : Set X))
    (hclosed : ∀ x ∈ T, IsClosed ({x} : Set X)) :
    letI : Algebra A Γ(I.subscheme, ⊤) :=
      ((Scheme.ΓSpecIso (.of A)).inv ≫ (I.subschemeι ≫ f).appTop).hom.toAlgebra
    (∑ x ∈ T,
      Module.length (X.presheaf.stalk x)
        ((X.presheaf.stalk x) ⧸ IdealSheafData.stalk I x)) ≤
      Module.length A Γ(I.subscheme, ⊤)
```

**`Stacks.Blowup.Colength.pos_order_of_le_center`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Colength/PositiveOrder.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/Colength/PositiveOrder.lean#L39). The attribute's comment: “positive\_order”.

> The maximal order of an ideal sheaf contained in the centre of a blowup is positive
> along the exceptional divisor.

```lean
public theorem pos_order_of_le_center
    {X : Scheme} (M J : X.IdealSheafData) (d : ℕ)
    (hJ : J ≤ M)
    (horder :
      let E := exceptionalIdeal M
      (J.comap (blowUpToBase M) ≤ E ^ d) ∧
        (∀ e : ℕ, J.comap (blowUpToBase M) ≤ E ^ e → e ≤ d)) :
    0 < d
```

**`Stacks.Blowup.Colength.exists_exceptionalIdeal_pow_mul_eq_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Colength/ResidualFactorization.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/Colength/ResidualFactorization.lean#L39). The attribute's comment: “clause (2), the splitting: the pulled-back ideal is the d-th power of the exceptional divisor times a residual ideal sheaf”.

> The pulled-back ideal sheaf is the `d`-th power of the exceptional divisor times a residual
> ideal sheaf on the blowup, whenever it is contained in that power. The residual factor is the
> quotient `(J·𝒪_X) : (dE)`, the source's `I·𝒪_X(dE)`.

```lean
public theorem exists_exceptionalIdeal_pow_mul_eq_comap
    {X : Scheme} (M J : X.IdealSheafData) (d : ℕ)
    (horder : J.comap (blowUpToBase M) ≤ exceptionalIdeal M ^ d) :
    ∃ J' : (blowUp M).IdealSheafData,
      exceptionalIdeal M ^ d * J' = J.comap (blowUpToBase M)
```

**`Stacks.Blowup.Colength.exists_finset_support_residual_and_length_ge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Colength/ResidualFiniteSupport.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/Colength/ResidualFiniteSupport.lean#L51). The attribute's comment: “clause (2), the finite support, together with clause (3)'s second inequality, with the finite support no longer assumed”.

> Let `A` be a two-dimensional regular local ring, `M` the ideal sheaf of its closed point and
> `b : X' ⟶ Spec A` the blowup in `M`. Let `J` be an ideal sheaf with `M ^ n ≤ J`, and suppose the
> inverse image `b⁻¹J·𝒪_{X'}` factors as `E ^ d · Z` with `E` the exceptional ideal and `d` maximal
> among the exponents `e` with `b⁻¹J·𝒪_{X'} ≤ E ^ e`. Then the support of `Z` is a finite set of
> closed points of the blowup, and the length over `A` of the global sections of the subscheme `Z`
> cuts out is at least the sum over that set of the colengths of the stalks of `Z`.

```lean
public theorem exists_finset_support_residual_and_length_ge
    (A : Type u) [CommRing A] [IsRegularLocalRing A] (hdim : ringKrullDim A = 2)
    (M : (Spec (CommRingCat.of A)).IdealSheafData)
    (hM : M = Scheme.IdealSheafData.ofIdealTop
      (Ideal.map (Scheme.ΓSpecIso (CommRingCat.of A)).inv.hom (IsLocalRing.maximalIdeal A)))
    (J : (Spec (CommRingCat.of A)).IdealSheafData) (n : ℕ) (hmn : M ^ n ≤ J)
    (d : ℕ) (Z : (AlgebraicGeometry.blowUp M).IdealSheafData)
    (hfac : J.comap (AlgebraicGeometry.blowUpToBase M) =
      AlgebraicGeometry.exceptionalIdeal M ^ d * Z)
    (hmax : ∀ e : ℕ, J.comap (AlgebraicGeometry.blowUpToBase M) ≤
      AlgebraicGeometry.exceptionalIdeal M ^ e → e ≤ d) :
    letI : Algebra A Γ(Z.subscheme, ⊤) :=
      ((Scheme.ΓSpecIso (CommRingCat.of A)).inv ≫
        (Z.subschemeι ≫ AlgebraicGeometry.blowUpToBase M).appTop).hom.toAlgebra
    ∃ T : Finset (AlgebraicGeometry.blowUp M),
      (Z.support : Set (AlgebraicGeometry.blowUp M)) =
          (T : Set (AlgebraicGeometry.blowUp M)) ∧
      (∀ x ∈ T, IsClosed ({x} : Set (AlgebraicGeometry.blowUp M))) ∧
      ∑ x ∈ T, Module.length ((AlgebraicGeometry.blowUp M).presheaf.stalk x)
          (((AlgebraicGeometry.blowUp M).presheaf.stalk x) ⧸ IdealSheafData.stalk Z x) ≤
        Module.length A Γ(Z.subscheme, ⊤)
```

**`AlgebraicGeometry.exists_residualIdeal_of_maximal_order`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Colength/ResidualIdeal.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/Colength/ResidualIdeal.lean#L228). The attribute's comment: “for the blowup X of a two-dimensional regular local ring (A, m) in m, with exceptional divisor E, and an ideal I with m^n contained in I contained in m: the largest d with I O\_X contained in O\_X(-dE) exists and is positive, the ideal I' with O\_X(-dE) I' = I O\_X exists and is unique, O\_X/I' is supported in a finite set of closed points x\_i, and length\_A(A/I) > length\_A Gamma(X, O\_X/I') >= sum\_i length\_\{O\_\{X,x\_i}}(O\_\{X,x\_i}/I'\_\{x\_i})”.

> Let `(A, 𝔪)` be a regular local ring of dimension two, let `f : X ⟶ Spec A` be the blowing
> up of `A` in `𝔪` (the blowup of the ideal sheaf `ℐ` generated by `𝔪`), with exceptional divisor
> `E` (the ideal sheaf `𝔪𝒪_X = 𝒪_X(-E)`), and let `𝔪ⁿ ⊆ I ⊆ 𝔪` be an ideal. Then there is a
> largest `d ≥ 0` with `I𝒪_X ⊆ 𝒪_X(-dE)`, and for it:
>
> * `d > 0`;
> * the ideal sheaf `ℐ' = I𝒪_X(dE)`, i.e. the unique `ℐ'` with `𝒪_X(-dE) · ℐ' = I𝒪_X`, exists;
> * `𝒪_X/ℐ'` is supported in a finite set `T` of closed points of `X`;
> * `length_A(A/I) > length_A Γ(X, 𝒪_X/ℐ') ≥ ∑_{x ∈ T} length_{𝒪_{X,x}}(𝒪_{X,x}/ℐ'_x)`.
>
> Here `I𝒪_X` is the inverse image of the ideal sheaf generated by `I` on `Spec A`, `Γ(X, 𝒪_X/ℐ')`
> is the ring of global functions of the closed subscheme `V(ℐ')`, with the `A`-module structure
> induced by `f`, and `ℐ'_x` is the stalk of `ℐ'` at `x`.

```lean
public theorem exists_residualIdeal_of_maximal_order
    (hdim : ringKrullDim A = 2) (ℐ : (Spec (CommRingCat.of A)).IdealSheafData)
    (hℐ : ℐ = Scheme.IdealSheafData.ofIdealTop
      (Ideal.map (Scheme.ΓSpecIso (.of A)).inv.hom (IsLocalRing.maximalIdeal A)))
    (I : Ideal A) (n : ℕ)
    (hnI : IsLocalRing.maximalIdeal A ^ n ≤ I) (hIm : I ≤ IsLocalRing.maximalIdeal A) :
    (∃ d : ℕ, (Scheme.IdealSheafData.ofIdealTop
          (I.map (Scheme.ΓSpecIso (.of A)).inv.hom)).comap (blowUpToBase ℐ) ≤
        exceptionalIdeal ℐ ^ d ∧
      ∀ e : ℕ, (Scheme.IdealSheafData.ofIdealTop
          (I.map (Scheme.ΓSpecIso (.of A)).inv.hom)).comap (blowUpToBase ℐ) ≤
        exceptionalIdeal ℐ ^ e → e ≤ d) ∧
    ∀ d : ℕ, (Scheme.IdealSheafData.ofIdealTop
          (I.map (Scheme.ΓSpecIso (.of A)).inv.hom)).comap (blowUpToBase ℐ) ≤
        exceptionalIdeal ℐ ^ d →
      (∀ e : ℕ, (Scheme.IdealSheafData.ofIdealTop
          (I.map (Scheme.ΓSpecIso (.of A)).inv.hom)).comap (blowUpToBase ℐ) ≤
        exceptionalIdeal ℐ ^ e → e ≤ d) →
    0 < d ∧
      ∃ (I' : (blowUp ℐ).IdealSheafData) (T : Finset (blowUp ℐ)),
        exceptionalIdeal ℐ ^ d * I' = (Scheme.IdealSheafData.ofIdealTop
          (I.map (Scheme.ΓSpecIso (.of A)).inv.hom)).comap (blowUpToBase ℐ) ∧
        (∀ K : (blowUp ℐ).IdealSheafData, exceptionalIdeal ℐ ^ d * K =
          (Scheme.IdealSheafData.ofIdealTop
            (I.map (Scheme.ΓSpecIso (.of A)).inv.hom)).comap (blowUpToBase ℐ) → K = I') ∧
        (I'.support : Set (blowUp ℐ)) = (T : Set (blowUp ℐ)) ∧
        (∀ x ∈ T, IsClosed ({x} : Set (blowUp ℐ))) ∧
        letI : Algebra A Γ(I'.subscheme, ⊤) :=
          ((Scheme.ΓSpecIso (.of A)).inv ≫ (I'.subschemeι ≫ blowUpToBase ℐ).appTop).hom.toAlgebra
        Module.length A Γ(I'.subscheme, ⊤) < Module.length A (A ⧸ I) ∧
        (∑ x ∈ T, Module.length ((blowUp ℐ).presheaf.stalk x)
            ((blowUp ℐ).presheaf.stalk x ⧸ IdealSheafData.stalk I' x)) ≤
          Module.length A Γ(I'.subscheme, ⊤)
```

**`AlgebraicGeometry.finite_supportSet_residual_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceResidual.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceResidual.lean#L175). The attribute's comment: “clause (2), the finite support: the residual factor left by dividing out the exceptional divisor is supported at finitely many closed points of the blowup”.

> **Clause (2) of [Stacks, Tag 0AGT].** Let `A` be a two-dimensional regular local ring, `M` the
> ideal sheaf of its closed point, and `b : X' ⟶ Spec A` the blowup in `M`. Let `J` be an ideal
> sheaf with `M ^ n ≤ J`, and suppose the inverse image `b⁻¹J·𝒪_{X'}` factors as `E ^ d · Z` with
> `E` the exceptional ideal and `d` maximal among the exponents `e` with `b⁻¹J·𝒪_{X'} ≤ E ^ e`.
> Then `Z` is supported at finitely many closed points of the blowup.

```lean
public theorem finite_supportSet_residual_maximalIdeal (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (hdim : ringKrullDim A = 2)
    (M : (Spec (CommRingCat.of A)).IdealSheafData)
    (hM : M = Scheme.IdealSheafData.ofIdealTop
      (Ideal.map (Scheme.ΓSpecIso (CommRingCat.of A)).inv.hom (maximalIdeal A)))
    (J : (Spec (CommRingCat.of A)).IdealSheafData) (n : ℕ) (hmn : M ^ n ≤ J)
    (d : ℕ) (Z : (blowUp M).IdealSheafData)
    (hfac : J.comap (blowUpToBase M) = exceptionalIdeal M ^ d * Z)
    (hmax : ∀ e : ℕ, J.comap (blowUpToBase M) ≤ exceptionalIdeal M ^ e → e ≤ d) :
    Z.supportSet.Finite ∧ ∀ z ∈ Z.supportSet, IsClosed ({z} : Set (blowUp M))
```

## Tag 0B4L, a lemma

[Tag 0B4L](https://stacks.math.columbia.edu/tag/0B4L) in the Stacks Project.

**`Stacks.Blowup.isIso_relativeDifferentialsToPushforward_residuePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ExceptionalDifferentials.lean, line 484](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/ExceptionalDifferentials.lean#L484).

> **Stacks Project, Tag 0B4L.** Let `(A, 𝔪, κ)` be a regular local ring of dimension two and
> let `f : X ⟶ S = Spec(A)` be the blowing up of `A` in `𝔪`, with `i : E ⟶ X` the immersion of the
> exceptional divisor. Then `Ω_{X/S} = i_* Ω_{E/κ}`: the canonical map
> `Stacks.Blowup.relativeDifferentialsToPushforward` is an isomorphism.
>
> The centre of the blowup is the closed point `Spec(κ) ⟶ Spec(A)`, whose ideal sheaf is `𝔪` by
> `Stacks.Blowup.ker_residuePoint`. The statement is the case of
> `Stacks.Blowup.isIso_relativeDifferentialsToPushforward` in which the centre is that point; the
> regularity and the dimension are the source's hypotheses and are not used by the proof, which
> runs on the affine charts `A[𝔪/a]` of the blowup directly.

```lean
theorem isIso_relativeDifferentialsToPushforward_residuePoint (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (_hdim : ringKrullDim A = 2) :
    IsIso (relativeDifferentialsToPushforward (residuePoint A))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.3, Tag 0AGP](https://stacks.math.columbia.edu/tag/0AGP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
