---
declaration: section
origin: cited
lean: Stacks.ChaoticSite.isZero_leftDerivedColim_symmetricPowerDiagram_of_lt, Stacks.ChaoticSite.nonempty_linearEquiv_leftDerivedColim_symmetricPowerDiagram, MvPolynomial.tor_map_variableIdeal_pow_succ_eq_zero, CommAlgCat.quillenSpectralSequence_of_surjective, CommAlgCat.isZero_lowerShriekZero_polynomialCotangentSheaf_of_surjective, CommAlgCat.isZero_leftDerivedColim_symmetricPower_polynomialCotangent_of_surjective, CommAlgCat.pageOneDisplay_of_surjective, CommAlgCat.polynomialSiteHomologyOneCotangentNegOneIso
statement: formalized
proof: formalized
---

# 92.12 A spectral sequence of Quillen

Section 92.12 of the Stacks Project, [Tag 08RC](https://stacks.math.columbia.edu/tag/08RC). 6 tags here are carried by 32 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08RD, a lemma

[Tag 08RD](https://stacks.math.columbia.edu/tag/08RD) in the Stacks Project.

**`Stacks.ChaoticSite.isZero_leftDerivedColim_symmetricPowerDiagram_of_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SymmetricPowerVanishing/HomologyVanishing.lean, line 717](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SymmetricPowerVanishing/HomologyVanishing.lean#L717). The attribute's comment: “No hypothesis beyond the source statement: C is any small category, H_l(C, -) is L_l of the colimit over Cᵒᵖ at linear coefficients, which is Tag 08PF's definition of the homology of a category, the B-module F on the chaotic site is the diagram F, flat means that every module of sections is flat, Sym^k is the sectionwise symmetric power, U is a point resolution as in Tag 08Q9, and the induction on k over the Koszul resolution is carried out in full for every k. The Künneth input of the source proof, the Eilenberg-Zilber comparison of Tag 08QD, is replaced by the weaker vanishing statement `StacksDraft.SimplicialTensor.isZero_homology_tensor_of_lt`, which is proved here.”.

> Let `C` be a small category with the chaotic topology, let `B` be a commutative ring and let
> `F` be a `B̲`-module on `C` — that is, a diagram `F : Cᵒᵖ ⥤ ModuleCat B`, every presheaf being
> a sheaf for the chaotic topology — which is flat, meaning that every module of sections is flat.
> Assume `C` carries a cosimplicial object `U_•` which is a point resolution, as in Tag 08Q9, and
> that `H_0(C, F) = 0`. Then `H_l(C, Sym^k_{B̲}(F)) = 0` for every `l < k`.
>
> Here `H_l(C, -) = L_lπ_!` is the `l`th left derived functor of the colimit over `Cᵒᵖ`, as in
> Tag 08PF, read at linear coefficients.

```lean
theorem isZero_leftDerivedColim_symmetricPowerDiagram_of_lt
    (C : Type u) [SmallCategory C] (B : Type u) [CommRing B]
    (U : CosimplicialObject C) (hU : IsPointResolution U)
    (F : Cᵒᵖ ⥤ ModuleCat.{u} B) (hF : ∀ X, Module.Flat B (F.obj X))
    (h₀ : IsZero (((colim : (Cᵒᵖ ⥤ ModuleCat.{u} B) ⥤ ModuleCat.{u} B).leftDerived 0).obj F))
    (k l : ℕ) (hl : l < k) :
    IsZero (((colim : (Cᵒᵖ ⥤ ModuleCat.{u} B) ⥤ ModuleCat.{u} B).leftDerived l).obj
      (symmetricPowerDiagram C B F k))
```

## Tag 08SG, a remark

[Tag 08SG](https://stacks.math.columbia.edu/tag/08SG) in the Stacks Project.

**`Stacks.ChaoticSite.nonempty_linearEquiv_leftDerivedColim_symmetricPowerDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SymmetricPowerDecalage.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SymmetricPowerDecalage.lean#L100). The attribute's comment: “H_k(C, Sym^k_{B̲}(F)) = ∧^k_B(H_1(C, F)) over an arbitrary commutative ring B, with no invertibility hypothesis on 2: C is any small category with the chaotic topology, H_l(C, -) is L_l of the colimit over Cᵒᵖ at linear coefficients, which is Tag 08PF's definition of the homology of a category, the flat B-module F on the chaotic site is the diagram F, flat meaning that every module of sections is flat, Sym^k is the sectionwise symmetric power, and U is a point resolution as in Tag 08Q9. The remark's own route through the sign-twisted S_k-coinvariants of H_1(C, F)^{⊗ k} is a proof erratum: that intermediate step is FALSE for the coefficient ring ℤ, which is the theorem Stacks.ChaoticSite.not_quillenSignedCoinvariants_int, refuted at the polynomial site of the surjection ℤ[x] → ℤ with k = 2. The proof here is Illusie's and Quillen's décalage, run at the Moore complex of F(U_•) over the relative Koszul resolution of Sym^k by the acyclic terms ∧^p W ⊗ Sym^{k-p} D attached to the reduced décalage D and W = ker(D → F(U_•)).”.

> Let `C` be a small category with the chaotic topology, let `B` be a
> commutative ring and let `F` be a flat `B̲`-module on `C` — a diagram `F : Cᵒᵖ ⥤ ModuleCat B`,
> every presheaf being a sheaf for the chaotic topology, flat meaning that every module of
> sections is flat — with `H_0(C, F) = 0`, and let `U_•` be a cosimplicial object of `C` which is a
> point resolution as in Tag 08Q9. Then
>
> `H_k(C, Sym^k_{B̲}(F)) ≅ ∧^k_B(H_1(C, F))`
>
> for every `k`, where `H_l(C, -) = L_lπ_!` is the `l`th left derived functor of the colimit over
> `Cᵒᵖ` read at linear coefficients, which is the definition of the homology of a category in
> Tag 08PF.
>
> No hypothesis is placed on `B`: in particular `2` need not be invertible.

```lean
public theorem nonempty_linearEquiv_leftDerivedColim_symmetricPowerDiagram
    (C : Type u) [SmallCategory C] (B : Type u) [CommRing B]
    (U : CosimplicialObject C) (hU : IsPointResolution U)
    (F : Cᵒᵖ ⥤ ModuleCat.{u} B) (hF : ∀ X, Module.Flat B (F.obj X))
    (h₀ : IsZero (((colim : (Cᵒᵖ ⥤ ModuleCat.{u} B) ⥤ ModuleCat.{u} B).leftDerived 0).obj F))
    (k : ℕ) :
    Nonempty (↥(((colim : (Cᵒᵖ ⥤ ModuleCat.{u} B) ⥤ ModuleCat.{u} B).leftDerived k).obj
        (symmetricPowerDiagram C B F k)) ≃ₗ[B]
      ⋀[B]^k ↥(((colim : (Cᵒᵖ ⥤ ModuleCat.{u} B) ⥤ ModuleCat.{u} B).leftDerived 1).obj F))
```

## Tag 08RE, a lemma

[Tag 08RE](https://stacks.math.columbia.edu/tag/08RE) in the Stacks Project.

**`MvPolynomial.tor_map_variableIdeal_pow_succ_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/QuillenTorVanishing.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/QuillenTorVanishing.lean#L56).

> **Tag 08RE.** Let `P = A[E]` be a polynomial ring and let `I` be the ideal generated by its
> variables.  For any `P`-module on which `I` acts as zero -- equivalently, for any module over
> the coefficient ring, pulled back along the augmentation -- the inclusion `I ^ (n + 1) ⊆ I ^ n`
> induces the zero map on `Tor_i^P` in every degree.

```lean
theorem tor_map_variableIdeal_pow_succ_eq_zero
    (A : Type u) [CommRing A] (E : Type v) (i n : ℕ)
    (M : ModuleCat.{max u v} (MvPolynomial E A))
    (hM : ∀ r ∈ (Ideal.span (Set.range (MvPolynomial.X : E → MvPolynomial E A)) :
        Ideal (MvPolynomial E A)), ∀ m : M, r • m = 0) :
    ((Tor (ModuleCat.{max u v} (MvPolynomial E A)) i).obj M).map
        (ModuleCat.ofHom
          (Submodule.inclusion
            (Ideal.pow_le_pow_right (Nat.le_succ n) :
              (Ideal.span (Set.range (MvPolynomial.X : E → MvPolynomial E A)) ^ (n + 1) :
                  Ideal (MvPolynomial E A)) ≤
                Ideal.span (Set.range (MvPolynomial.X : E → MvPolynomial E A)) ^ n))) = 0
```

## Tag 08RF, a theorem

[Tag 08RF](https://stacks.math.columbia.edu/tag/08RF) in the Stacks Project.

**`CommAlgCat.quillenSpectralSequence_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/QuillenSpectralSequenceSurjective.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/QuillenSpectralSequenceSurjective.lean#L136). The attribute's comment: “whole theorem, for a surjective A → B: the spectral sequence exists as a CohomologicalSpectralSequence of B-modules starting at page 1, so d_r has bidegree (r, -r + 1) by definition of that type; its first page is identified with E₁^{p,q} = H_{-p-q}(C_{B/A}, Sym^p_{B̲}(Ω)) (pageOneIso, zero for p < 0 by pageOne_isZero); it converges to Tor^A_{-p-q}(B, B) in the sense of SpectralSequence.AbutsTo: an infinity page at every bidegree and, on each Tor^A_{-n}(B, B), a finite decreasing filtration whose graded pieces are the infinity-page terms. The second conjunct is the final vanishing H_i(C_{B/A}, Sym^k_{B̲}(Ω)) = 0 for i < k. H_i(C_{B/A}, -) is L_i colim over the opposite of the small model of the polynomial site (Tag 08PF), extended by zero to i < 0; Tor^A_i(B, B) is the i-th left derived functor of B ⊗_A - at B. The sequence is that of the filtered complex C = Ō(U_•) on the standard point resolution, filtered by τ^{≤ -p}(𝒦^p(U_•)), whose cohomology is Lπ_!(Ō) = B ⊗^L_A B; every input (𝒦ⁿ/𝒦ⁿ⁺¹ = Sym^n(Ω), the footnote vanishing H_i(C_{B/A}, 𝒦ⁿ) = 0 for i < n via Tags 08RE, 068F, 08QJ, 08Q2) is proved.”.

> **Stacks 08RF (Quillen spectral sequence).** Let `A → B` be a surjective ring map and
> `Ω = Ω_{𝒪/A} ⊗_𝒪 B̲` on the polynomial site `C_{B/A}`.  Then
>
> * there is a cohomological spectral sequence of `B`-modules `(E_r)_{r ≥ 1}`, with `d_r` of
>   bidegree `(r, -r + 1)`, first page `E₁^{p,q} ≅ H_{-p-q}(C_{B/A}, Sym^p_{B̲}(Ω))` (and `0` for
>   `p < 0`), converging to `Tor^A_{-p-q}(B, B)`: it has an infinity page at every bidegree, and
>   each `Tor^A_{-n}(B, B)` carries a finite decreasing filtration with
>   `E_∞^{p, n - p} ≅ F^p/F^{p+1}`; and
> * `H_i(C_{B/A}, Sym^k_{B̲}(Ω)) = 0` for `i < k`.
>
> The first conjunct is `CommAlgCat.QuillenSpectralSequenceData A B` inhabited, the datum being
> `CommAlgCat.quillenSpectralSequenceDataOfSurjective`; the second is stated on the same entries
> `CommAlgCat.symmetricPowerSiteHomology` the first page is identified with.

```lean
theorem quillenSpectralSequence_of_surjective
    (h : Function.Surjective (algebraMap A (B : Type u))) :
    Nonempty (QuillenSpectralSequenceData A B) ∧
      ∀ (k : ℕ) (i : ℤ), i < k → IsZero (symmetricPowerSiteHomology A B k i)
```

**`CommAlgCat.isZero_lowerShriekZero_polynomialCotangentSheaf_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectionDifferentialsVanishing.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SurjectionDifferentialsVanishing.lean#L71). The attribute's comment: “the final vanishing H_i(C_{B/A}, Symᵏ(Ω)) = 0 for i < k, in the case k = 1, where Sym¹(Ω) = Ω: for a surjective A → B the sections at the point of L₀π_!(Ω_{𝒪/A} ⊗_𝒪 B̲) vanish. As in Tag 08PU, Lπ_! is read degreewise at abelian coefficients on the small model of the footnote-restricted site. The same vanishing for every k, at linear coefficients, is CommAlgCat.isZero_leftDerivedColim_symmetricPower_polynomialCotangent_of_surjective”.

> **Stacks 08RF**, the final vanishing in the case `k = 1`. For a surjective ring map `A → B`
> the zeroth homology of the sheaf of base-changed differentials on the polynomial site vanishes,
> because it is `H⁰(L_{B/A}) = Ω[B⁄A]` and `Ω[B⁄A] = 0` for a surjection.

```lean
theorem isZero_lowerShriekZero_polynomialCotangentSheaf_of_surjective
    (hsurj : Function.Surjective (algebraMap A ↥B)) :
    IsZero ((Stacks.ChaoticSite.pointSections.{u, u + 1, u} AddCommGrpCat.{u}).obj
      (((Stacks.ChaoticSite.abelianPointLowerShriek
            (smallBoundedPolynomialSite A B
              (standardResolutionVarCardinal A B))).leftDerived 0).obj
        (smallPolynomialCotangentSheaf A B (standardResolutionVarCardinal A B))))
```

**`CommAlgCat.isZero_leftDerivedColim_symmetricPower_polynomialCotangent_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectionSymmetricPowerVanishing.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SurjectionSymmetricPowerVanishing.lean#L168). The attribute's comment: “the final vanishing H_i(C_{B/A}, Symᵏ_{B̲}(Ω)) = 0 for i < k, for EVERY k, where Symᵏ is the sectionwise symmetric power, which is the sheaf symmetric power because the topology of C_{B/A} is chaotic. H_i(C_{B/A}, -) is L_i of the colimit over the opposite of the small model of the footnote-restricted site at linear coefficients, which is Tag 08PF's definition of the homology of a category. The proof is the source's: Ω is a flat B̲-module because each Ω[P⁄A] is free over P, π_!(Ω) = Ω_{B/A} = 0 for a surjective A → B, and Tag 08RD turns those into the vanishing. No hypothesis beyond the source's surjectivity of A → B”.

> **Stacks 08RF, the final vanishing, for every `k`.** For a surjective ring map `A → B` and
> the sheaf `Ω = Ω_{𝒪/A} ⊗_𝒪 B̲` on the polynomial site `C_{B/A}`,
>
> `H_i(C_{B/A}, Symᵏ_{B̲}(Ω)) = 0` for `i < k`.
>
> The source's proof: `Ω` is flat and `H₀(C_{B/A}, Ω) = π_!(Ω) = Ω_{B/A} = 0` because `A → B` is
> surjective, and Tag 08RD gives the vanishing from those two facts.

```lean
theorem isZero_leftDerivedColim_symmetricPower_polynomialCotangent_of_surjective
    (hsurj : Function.Surjective (algebraMap A (B : Type u))) (k l : ℕ) (hl : l < k) :
    IsZero (((colim :
          ((smallBoundedPolynomialSite A B (standardResolutionVarCardinal A B))ᵒᵖ ⥤
            ModuleCat.{u} B) ⥤ ModuleCat.{u} B).leftDerived l).obj
      (Stacks.ChaoticSite.symmetricPowerDiagram
        (smallBoundedPolynomialSite A B (standardResolutionVarCardinal A B)) (B : Type u)
        (smallPolynomialCotangentModulePresheaf A B (standardResolutionVarCardinal A B)) k))
```

## Tag 08RG, a remark

[Tag 08RG](https://stacks.math.columbia.edu/tag/08RG) in the Stacks Project.

**`CommAlgCat.pageOneDisplay_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/QuillenSpectralSequence.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/QuillenSpectralSequence.lean#L353). The attribute's comment: “the E₁-page display, for a surjective A → B with I = ker(A → B): every entry of the displayed array is identified. The array is E₁^{p,q} = H_{-p-q}(C_{B/A}, Sym^p_{B̲}(Ω)), which is Theorem 08RF's own identification of the first page, read here as the ℕ × ℤ-indexed family CommAlgCat.pageOneDisplayEntry with p along the columns and q down the rows from q = 0; H_i(C_{B/A}, -) = L_i colim over the opposite of the small model of the footnote-restricted site at linear coefficients is Tag 08PF's definition of the homology of a category, and Sym^p_{B̲} is the sectionwise symmetric power, which is the sheaf symmetric power because the topology of C_{B/A} is chaotic. The six conjuncts are the array's six regions: zero strictly below the antidiagonal p + q = 0 (negative homological degree); zero strictly above the diagonal -p - q = p, by the final clause of Theorem 08RF; B at the top of the column p = 0; zero down the rest of that column, which Theorem 08RF's vanishing does not give since it is vacuous at p = 0; H^{-i}(L_{B/A}) down the column p = 1, by Tag 08PU together with Sym¹(Ω) = Ω, which at the position (1, -2) is the I/I² of the display's third row by the remark's opening clause; and ∧^p_B(I/I²) at the diagonal position (p, -2p), by the remark's second clause. The entries strictly inside the triangle with p ≥ 2, which the display writes as H_3(C_{B/A}, Sym²(Ω)) and H_4(C_{B/A}, Sym²(Ω)), the remark leaves unidentified and so does this statement. The display's parenthetical `with horizontal differential` is Theorem 08RF's clause that d_r has bidegree (r, -r + 1), at r = 1, which holds by definition of the type CohomologicalSpectralSequence _ 1 carried by CommAlgCat.QuillenSpectralSequenceData.sequence. I/I² is (CommAlgCat.surjectionExtension A B h).Cotangent, the conormal module of the presentation of B by A itself, which CommAlgCat.surjectionConormalAddEquiv identifies with Ideal.Cotangent (RingHom.ker (algebraMap A B)). No hypothesis beyond the remark's own surjectivity of A → B”.

> **Stacks 08RG**, the `E₁`-page display, for a surjective ring map `A → B` with kernel `I`:
> every entry of the displayed array
>
> ```
> B
> 0
> 0   I/I²
> 0   H^{-2}(L_{B/A})
> 0   H^{-3}(L_{B/A})   ∧²(I/I²)
> 0   H^{-4}(L_{B/A})   H_3(C_{B/A}, Sym²(Ω))
> 0   H^{-5}(L_{B/A})   H_4(C_{B/A}, Sym²(Ω))   ∧³(I/I²)
> ```
>
> is the module the remark displays there.  The array is `E₁^{p,q} = H_{-p-q}(C_{B/A}, Sym^p(Ω))`
> of Theorem 08RF, `p` along the columns and `q` down the rows from `q = 0`, so the six conjuncts
> below are, in order:
>
> * the entries strictly below the antidiagonal `p + q = 0` vanish — those are the positions the
>   display leaves blank beyond the triangle, where the homological degree `-p - q` is negative;
> * the entries strictly above the diagonal `-p - q = p` vanish — the blanks inside the triangle,
>   by the final clause of Theorem 08RF;
> * the top entry of the column `p = 0` is `B`;
> * the rest of the column `p = 0` vanishes — together with the previous two conjuncts this is the
>   column `B, 0, 0, …` the display opens with;
> * the column `p = 1` is `H^{-i}(L_{B/A})` in homological degree `i`, which at `i = 1`, the
>   position `(1, -2)`, is the `I/I²` of the third row by the remark's opening clause;
> * the diagonal entry at `(p, -2p)` is `∧^p_B(I/I²)`, by the remark's second clause.
>
> The entries strictly inside the triangle with `p ≥ 2` — `H_3(C_{B/A}, Sym²(Ω))` and
> `H_4(C_{B/A}, Sym²(Ω))` in the display — are left as they stand, exactly as the remark leaves
> them.
>
> "With horizontal differential" is Theorem 08RF's own clause that `d_r` has bidegree
> `(r, -r + 1)`, at `r = 1`; it holds by definition of `CohomologicalSpectralSequence _ 1`, which
> is the type of `CommAlgCat.QuillenSpectralSequenceData.sequence`.

```lean
theorem pageOneDisplay_of_surjective (h : Function.Surjective (algebraMap A (B : Type u))) :
    (∀ (p : ℕ) (q : ℤ), 0 < (p : ℤ) + q → IsZero (pageOneDisplayEntry A B p q)) ∧
      (∀ (p : ℕ) (q : ℤ), -(p : ℤ) - q < p → IsZero (pageOneDisplayEntry A B p q)) ∧
      Nonempty (pageOneDisplayEntry A B 0 0 ≅ ModuleCat.of (B : Type u) (B : Type u)) ∧
      (∀ q : ℤ, q < 0 → IsZero (pageOneDisplayEntry A B 0 q)) ∧
      (∀ i : ℕ, Nonempty (pageOneDisplayEntry A B 1 (-1 - (i : ℤ)) ≅
          (cotangentComplex.{u, u} A B).homology (-(i : ℤ)))) ∧
      (∀ p : ℕ, Nonempty (pageOneDisplayEntry A B p (-2 * (p : ℤ)) ≅
          ModuleCat.of (B : Type u)
            (⋀[(B : Type u)]^p (surjectionExtension.{u, u} A B h).Cotangent)))
```

**`CommAlgCat.polynomialSiteHomologyOneCotangentNegOneIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectionSiteConormal.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SurjectionSiteConormal.lean#L174). The attribute's comment: “the first equality of the opening clause, H^{-1}(L_{B/A}) = H_1(C_{B/A}, Ω), as the degree n = 1 case of Tag 08PU: the sections at the point of L₁π_!(Ω_{𝒪/A} ⊗_𝒪 B̲) are the degree -1 cohomology of the cotangent complex of Tag 08PN. As in Tag 08PU, Lπ_! is read degreewise at abelian coefficients, as the left derived functors of the π_! of Tag 08PF, on the small model of the footnote-restricted site, so this is an isomorphism of abelian groups; the B-module statement H^{-1}(L_{B/A}) = I/I² is Tag 08RA, CommAlgCat.cotangentComplex_homologyNegOneIso. Proved for every ring map A → B, hence in particular for the surjective one of the remark”.

> **Stacks 08RG**, the first equality of the remark's opening clause, which is Tag 08PU in
> degree `n = 1`: the sections at the point of `L₁π_!(Ω_{𝒪/A} ⊗_𝒪 B̲)` are the degree `-1`
> cohomology of the cotangent complex `L_{B/A}`. The remark states it for a surjective `A → B`; it
> holds for every ring map.

```lean
def polynomialSiteHomologyOneCotangentNegOneIso :
    (Stacks.ChaoticSite.pointSections.{u, u + 1, u} AddCommGrpCat.{u}).obj
        (((Stacks.ChaoticSite.abelianPointLowerShriek
              (smallBoundedPolynomialSite A B
                (standardResolutionVarCardinal A B))).leftDerived 1).obj
          (smallPolynomialCotangentSheaf A B (standardResolutionVarCardinal A B))) ≅
      (forget₂ (ModuleCat.{u} ↥B) AddCommGrpCat.{u}).obj
        ((cotangentComplex.{u, u} A B).homology (-1))
```

**`CommAlgCat.polynomialSiteHomologyOneConormalIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectionSiteConormal.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SurjectionSiteConormal.lean#L212). The attribute's comment: “the second equality of the opening clause, H_1(C_{B/A}, Ω) = I/I² for I = ker(A → B), as the composite of the first equality with Tag 08RA: for a surjective A → B the sections at the point of L₁π_!(Ω_{𝒪/A} ⊗_𝒪 B̲) are Ideal.Cotangent (RingHom.ker (algebraMap A B)), by way of H^{-1}(L_{B/A}), so the whole opening clause is covered by this declaration together with CommAlgCat.polynomialSiteHomologyOneCotangentNegOneIso. As in Tag 08PU, Lπ_! is read degreewise at abelian coefficients, so this is an isomorphism of abelian groups; the B-module statement H^{-1}(L_{B/A}) = I/I² is Tag 08RA itself. This declaration carries no hypothesis beyond the remark's own surjectivity of A → B. It states the opening clause and that clause alone; the section `Where the rest of 08RG stands` of this module's docstring says where each of the remark's other clauses stands”.

> **Stacks 08RG**, the opening clause `H^{-1}(L_{B/A}) = H_1(C_{B/A}, Ω) = I/I²` for a
> surjective ring map `A → B` with kernel `I`: the sections at the point of
> `L₁π_!(Ω_{𝒪/A} ⊗_𝒪 B̲)` are the conormal module `I/I²`. The isomorphism is the composite of
> `CommAlgCat.polynomialSiteHomologyOneCotangentNegOneIso` with Tag 08RA's
> `CommAlgCat.cotangentComplex_homologyNegOneIso`, so it factors through `H^{-1}(L_{B/A})` exactly
> as the remark says.

```lean
def polynomialSiteHomologyOneConormalIso :
    (Stacks.ChaoticSite.pointSections.{u, u + 1, u} AddCommGrpCat.{u}).obj
        (((Stacks.ChaoticSite.abelianPointLowerShriek
              (smallBoundedPolynomialSite A B
                (standardResolutionVarCardinal A B))).leftDerived 1).obj
          (smallPolynomialCotangentSheaf A B (standardResolutionVarCardinal A B))) ≅
      AddCommGrpCat.of (RingHom.ker (algebraMap A ↥B)).Cotangent
```

**`CommAlgCat.torToCotangentEdge`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectionSiteEdgeMaps.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SurjectionSiteEdgeMaps.lean#L201). The attribute's comment: “the first family of edge maps, Tor_i^A(B, B) → H^{-i}(L_{B/A}) for every i > 0, for a surjective A → B with I = ker(A → B). These are the remark's own edge maps, read -- as the remark reads them -- off the filtration … ⊆ 𝒦² ⊆ 𝒦 ⊆ Ō of the abutment, where Ō = 𝒪 ⊗_A B̲ and 𝒦 = ker(Ō → B̲) are presheaves on C_{B/A}: the composite Tor^A_i(B,B) ≅ H_i(C_{B/A}, Ō) ≅ H_i(C_{B/A}, 𝒦) ⟶ H_i(C_{B/A}, 𝒦/𝒦²) ≅ H^{-i}(L_{B/A}). Tor^A_i(B, B) is RingTheory.TorProducts.torBaseChange, the i-th left derived functor of extension of scalars along A → B, which is the spelling in which this development identifies the abutment H_i(C_{B/A}, Ō) of Theorem 08RF; H^{-i}(L_{B/A}) is the degree -i cohomology of the cotangent complex of Tag 08PN, reached by Tag 08PU at linear coefficients; and H_i(C_{B/A}, -) = L_i colim over the opposite of the small model of the footnote-restricted site is Tag 08PF's definition of the homology of a category. No spectral sequence is involved, and no hypothesis is carried: the construction holds for every ring map A → B, hence in particular for the surjective one of the remark. The remark's SECOND family, ∧^i_B(I/I²) → Tor_i^A(B, B), is not this declaration; it needs the footnote vanishing of Theorem 08RF and is recorded separately”.

> **The first family of edge maps of Stacks Remark 08RG**: for every `i > 0` a map
>
> `Tor_i^A(B, B) ⟶ H^{-i}(L_{B/A})`.
>
> It is the remark's own map, read off the filtration `… ⊆ 𝒦² ⊆ 𝒦 ⊆ Ō` of the abutment: the
> composite
>
> `Tor^A_i(B, B) ≅ H_i(C_{B/A}, Ō) ≅ H_i(C_{B/A}, 𝒦) ⟶ H_i(C_{B/A}, 𝒦/𝒦²) ≅ H^{-i}(L_{B/A})`
>
> of `CommAlgCat.torToCotangentHomologyEdge` with
> `CommAlgCat.siteHomologyGradedOneCotangentIso`.  The first identification is
> `CommAlgCat.leftDerivedColimQuotientTorIso`, the second
> `CommAlgCat.leftDerivedColimAugmentationIdealIsoOfPos` — available because `H_j(C_{B/A}, B̲)`
> vanishes for `j > 0` — the arrow is induced by the projection onto the first graded piece, and
> the last identification is `Ω ≅ 𝒦/𝒦²` followed by Tag 08PU.
>
> The remark states these maps for a surjective `A → B`; they exist for every ring map.

```lean
def torToCotangentEdge (i : ℕ) (hi : 0 < i) :
    (RingTheory.TorProducts.torBaseChange.{u, u, u} A (B : Type u) i).obj
        (ModuleCat.of A (B : Type u)) ⟶
      (cotangentComplex.{u, u} A B).homology (-(i : ℤ))
```

**`CommAlgCat.symmetricPowerToTorEdge_of_surjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectionSiteEdgeMapsUnconditional.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SurjectionSiteEdgeMapsUnconditional.lean#L118). The attribute's comment: “the second family of edge maps, ∧^i_B(I/I²) → Tor_i^A(B, B) for every i > 0, for a surjective A → B with I = ker(A → B). It is the remark's own map, read -- as the remark reads it -- off the filtration … ⊆ 𝒦² ⊆ 𝒦 ⊆ Ō of the abutment, where Ō = 𝒪 ⊗_A B̲ and 𝒦 = ker(Ō → B̲) are presheaves on C_{B/A}: the composite H_i(C_{B/A}, Sym^i(Ω)) ≅ H_i(C_{B/A}, 𝒦ⁱ/𝒦ⁱ⁺¹) ≅ H_i(C_{B/A}, 𝒦ⁱ) ⟶ H_i(C_{B/A}, 𝒦) ≅ H_i(C_{B/A}, Ō) ≅ Tor_i^A(B, B), whose middle isomorphism is the diagonal identification H_i(C_{B/A}, 𝒦ⁱ) ≅ H_i(C_{B/A}, 𝒦ⁱ/𝒦ⁱ⁺¹) and whose arrow is induced by the inclusion 𝒦ⁱ ⊆ 𝒦. Tor_i^A(B, B) is RingTheory.TorProducts.torBaseChange, the i-th left derived functor of extension of scalars along A → B, in which this development identifies the abutment H_i(C_{B/A}, Ō) of Theorem 08RF; and H_i(C_{B/A}, -) = L_i colim over the opposite of the small model of the footnote-restricted site is Tag 08PF's definition of the homology of a category. The source is written ∧^i_B(I/I²) by the remark and H_i(C_{B/A}, Sym^i_{B̲}(Ω)) here; they are the same object by the remark's own second clause, which this library has unconditionally as CommAlgCat.exteriorPower_conormal_leftDerivedColim_symmetricPower_of_surjective, and that clause is the other declaration of this part's covering set. It is stated at the symmetric power because the clause produces its linear equivalence inside a Nonempty -- Remark 08SG is reached by décalage, which chooses an isomorphism rather than constructing a canonical one -- so there is no canonical map out of ∧^i_B(I/I²) to be had. The construction needs the footnote vanishing H_j(C_{B/A}, 𝒦ⁿ) = 0 for j < n of the proof of Theorem 08RF, which is a theorem here for every surjective A → B, so no hypothesis beyond the remark's own surjectivity is carried”.

> **The second family of edge maps of Stacks Remark 08RG**, for a surjective `A → B` and on no
> other hypothesis: for every `i > 0` a map
>
> `∧^i_B(I/I²) = H_i(C_{B/A}, Sym^i_{B̲}(Ω)) ⟶ Tor_i^A(B, B)`.
>
> This is `CommAlgCat.symmetricPowerToTorEdge` with its hypothesis `hvan` discharged by
> `isZero_leftDerivedColim_smallPolynomialAugmentationIdealPow_of_surjective_unconditional`,
> the footnote vanishing of [Stacks, Tag 08RF]. The map itself is the remark's own, read off the
> filtration `… ⊆ 𝒦² ⊆ 𝒦 ⊆ Ō` of the abutment.

```lean
def symmetricPowerToTorEdge_of_surjective
    (hsurj : Function.Surjective (algebraMap A (B : Type u))) (i : ℕ) (hi : 0 < i) :
    (siteHomologyFunctor A B (standardResolutionVarCardinal A B) i).obj
        (Stacks.ChaoticSite.symmetricPowerDiagram
          (smallBoundedPolynomialSite A B (standardResolutionVarCardinal A B)) (B : Type u)
          (smallPolynomialCotangentModulePresheaf A B
            (standardResolutionVarCardinal A B)) i) ⟶
      (RingTheory.TorProducts.torBaseChange.{u, u, u} A (B : Type u) i).obj
        (ModuleCat.of A (B : Type u))
```

**`CommAlgCat.exact_fiveTerm_cotangentNegThree_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectionSiteEdgeMapsUnconditional.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SurjectionSiteEdgeMapsUnconditional.lean#L177). The attribute's comment: “the five term exact sequence of low degree terms, Tor_3^A(B, B) → H^{-3}(L_{B/A}) → ∧²_B(I/I²) → Tor_2^A(B, B) → H^{-2}(L_{B/A}) → 0, for a surjective A → B with I = ker(A → B) -- exactness at H^{-3}(L_{B/A}). The sequence is the five term segment of the long exact sequence of 0 → 𝒦² → 𝒦 → 𝒦/𝒦² → 0 on C_{B/A} read through the remark's identifications H_i(C_{B/A}, 𝒦) = Tor_i^A(B, B) for i ≥ 1, H_i(C_{B/A}, 𝒦/𝒦²) = H^{-i}(L_{B/A}) and H_2(C_{B/A}, 𝒦²) = H_2(C_{B/A}, Sym²(Ω)) = ∧²_B(I/I²), the last of these being the remark's second clause (CommAlgCat.exteriorPower_conormal_leftDerivedColim_symmetricPower_of_surjective); its first and fourth maps are the first family of edge maps, CommAlgCat.torToCotangentEdge, its third is the second family, CommAlgCat.symmetricPowerToTorEdge_of_surjective, and its second is CommAlgCat.fiveTermConnecting_of_surjective. The covering set of this part is this declaration together with CommAlgCat.exact_fiveTerm_exteriorSquare_of_surjective, CommAlgCat.exact_fiveTerm_torTwo_of_surjective and CommAlgCat.epi_fiveTerm_torToCotangentEdge_two_of_surjective, which state exactness at the other two interior terms and the final → 0. No spectral sequence is involved. The footnote vanishing H_j(C_{B/A}, 𝒦ⁿ) = 0 for j < n of the proof of Theorem 08RF, which the sequence needs, is a theorem here for every surjective A → B, so no hypothesis beyond the remark's own surjectivity is carried”.

> **The five term exact sequence of Stacks Remark 08RG, exactness at `H^{-3}(L_{B/A})`**, for
> a surjective `A → B` and on no other hypothesis: the image of the edge map
> `Tor_3^A(B, B) → H^{-3}(L_{B/A})` is the kernel of the middle map `H^{-3}(L_{B/A}) → ∧²_B(I/I²)`.
>
> This is `CommAlgCat.exact_fiveTerm_cotangentNegThree` with its hypothesis `hvan` discharged.

```lean
theorem exact_fiveTerm_cotangentNegThree_of_surjective
    (hsurj : Function.Surjective (algebraMap A (B : Type u))) :
    (ShortComplex.mk (torToCotangentEdge A B 3 (by norm_num))
      (fiveTermConnecting_of_surjective A B hsurj)
      (torToCotangentEdge_comp_fiveTermConnecting A B
        (isZero_leftDerivedColim_smallPolynomialAugmentationIdealPow_of_surjective_unconditional
          A B hsurj))).Exact
```

**`CommAlgCat.exact_fiveTerm_exteriorSquare_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectionSiteEdgeMapsUnconditional.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SurjectionSiteEdgeMapsUnconditional.lean#L206). The attribute's comment: “the five term exact sequence of low degree terms, Tor_3^A(B, B) → H^{-3}(L_{B/A}) → ∧²_B(I/I²) → Tor_2^A(B, B) → H^{-2}(L_{B/A}) → 0, for a surjective A → B with I = ker(A → B) -- exactness at ∧²_B(I/I²), the term the remark writes ∧²_B(I/I²) and this development spells H_2(C_{B/A}, Sym²_{B̲}(Ω)), the two being the same object by the remark's second clause (CommAlgCat.exteriorPower_conormal_leftDerivedColim_symmetricPower_of_surjective). The sequence is the five term segment of the long exact sequence of 0 → 𝒦² → 𝒦 → 𝒦/𝒦² → 0 on C_{B/A} read through the remark's identifications H_i(C_{B/A}, 𝒦) = Tor_i^A(B, B) for i ≥ 1 and H_i(C_{B/A}, 𝒦/𝒦²) = H^{-i}(L_{B/A}). The covering set of this part is this declaration together with CommAlgCat.exact_fiveTerm_cotangentNegThree_of_surjective, CommAlgCat.exact_fiveTerm_torTwo_of_surjective and CommAlgCat.epi_fiveTerm_torToCotangentEdge_two_of_surjective. The footnote vanishing H_j(C_{B/A}, 𝒦ⁿ) = 0 for j < n of the proof of Theorem 08RF, which the sequence needs, is a theorem here for every surjective A → B, so no hypothesis beyond the remark's own surjectivity is carried”.

> **The five term exact sequence of Stacks Remark 08RG, exactness at `∧²_B(I/I²)`**, for a
> surjective `A → B` and on no other hypothesis: the image of the middle map
> `H^{-3}(L_{B/A}) → ∧²_B(I/I²)` is the kernel of the second edge map `∧²_B(I/I²) → Tor_2^A(B, B)`.
>
> This is `CommAlgCat.exact_fiveTerm_exteriorSquare` with its hypothesis `hvan` discharged.

```lean
theorem exact_fiveTerm_exteriorSquare_of_surjective
    (hsurj : Function.Surjective (algebraMap A (B : Type u))) :
    (ShortComplex.mk (fiveTermConnecting_of_surjective A B hsurj)
      (symmetricPowerToTorEdge_of_surjective A B hsurj 2 (by norm_num))
      (fiveTermConnecting_comp_symmetricPowerToTorEdge A B
        (isZero_leftDerivedColim_smallPolynomialAugmentationIdealPow_of_surjective_unconditional
          A B hsurj))).Exact
```

**`CommAlgCat.exact_fiveTerm_torTwo_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectionSiteEdgeMapsUnconditional.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SurjectionSiteEdgeMapsUnconditional.lean#L237). The attribute's comment: “the five term exact sequence of low degree terms, Tor_3^A(B, B) → H^{-3}(L_{B/A}) → ∧²_B(I/I²) → Tor_2^A(B, B) → H^{-2}(L_{B/A}) → 0, for a surjective A → B with I = ker(A → B) -- exactness at Tor_2^A(B, B), which is RingTheory.TorProducts.torBaseChange in degree 2, the second left derived functor of extension of scalars along A → B applied to B, in which this development identifies the abutment H_2(C_{B/A}, Ō) of Theorem 08RF. The sequence is the five term segment of the long exact sequence of 0 → 𝒦² → 𝒦 → 𝒦/𝒦² → 0 on C_{B/A} read through the remark's identifications H_i(C_{B/A}, 𝒦) = Tor_i^A(B, B) for i ≥ 1, H_i(C_{B/A}, 𝒦/𝒦²) = H^{-i}(L_{B/A}) and H_2(C_{B/A}, 𝒦²) = ∧²_B(I/I²). The covering set of this part is this declaration together with CommAlgCat.exact_fiveTerm_cotangentNegThree_of_surjective, CommAlgCat.exact_fiveTerm_exteriorSquare_of_surjective and CommAlgCat.epi_fiveTerm_torToCotangentEdge_two_of_surjective. The footnote vanishing H_j(C_{B/A}, 𝒦ⁿ) = 0 for j < n of the proof of Theorem 08RF, which the sequence needs, is a theorem here for every surjective A → B, so no hypothesis beyond the remark's own surjectivity is carried”.

> **The five term exact sequence of Stacks Remark 08RG, exactness at `Tor_2^A(B, B)`**, for a
> surjective `A → B` and on no other hypothesis: the image of the second edge map
> `∧²_B(I/I²) → Tor_2^A(B, B)` is the kernel of the first edge map
> `Tor_2^A(B, B) → H^{-2}(L_{B/A})`.
>
> This is `CommAlgCat.exact_fiveTerm_torTwo` with its hypothesis `hvan` discharged.

```lean
theorem exact_fiveTerm_torTwo_of_surjective
    (hsurj : Function.Surjective (algebraMap A (B : Type u))) :
    (ShortComplex.mk (symmetricPowerToTorEdge_of_surjective A B hsurj 2 (by norm_num))
      (torToCotangentEdge A B 2 (by norm_num))
      (symmetricPowerToTorEdge_comp_torToCotangentEdge A B
        (isZero_leftDerivedColim_smallPolynomialAugmentationIdealPow_of_surjective_unconditional
          A B hsurj))).Exact
```

**`CommAlgCat.epi_fiveTerm_torToCotangentEdge_two_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectionSiteEdgeMapsUnconditional.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SurjectionSiteEdgeMapsUnconditional.lean#L264). The attribute's comment: “the five term exact sequence of low degree terms, Tor_3^A(B, B) → H^{-3}(L_{B/A}) → ∧²_B(I/I²) → Tor_2^A(B, B) → H^{-2}(L_{B/A}) → 0, for a surjective A → B with I = ker(A → B) -- the final → 0, i.e. surjectivity of the last map Tor_2^A(B, B) → H^{-2}(L_{B/A}), which is the first family of edge maps (CommAlgCat.torToCotangentEdge) in degree 2. It holds because H_1(C_{B/A}, 𝒦²) = 0, the footnote vanishing of the proof of Theorem 08RF at j = 1 < 2 = n, which is a theorem here for every surjective A → B; so no hypothesis beyond the remark's own surjectivity is carried. The covering set of this part is this declaration together with CommAlgCat.exact_fiveTerm_cotangentNegThree_of_surjective, CommAlgCat.exact_fiveTerm_exteriorSquare_of_surjective and CommAlgCat.exact_fiveTerm_torTwo_of_surjective, which state exactness at the sequence's three interior terms”.

> **The five term exact sequence of Stacks Remark 08RG ends in zero**, for a surjective
> `A → B` and on no other hypothesis: the first edge map `Tor_2^A(B, B) → H^{-2}(L_{B/A})` is
> surjective.
>
> This is `CommAlgCat.epi_fiveTerm_torToCotangentEdge_two` with its hypothesis `hvan`
> discharged.

```lean
theorem epi_fiveTerm_torToCotangentEdge_two_of_surjective
    (hsurj : Function.Surjective (algebraMap A (B : Type u))) :
    Epi (torToCotangentEdge A B 2 (by norm_num))
```

**`CommAlgCat.leftDerivedColimOneConormalLinearEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectionSiteExteriorConormal.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SurjectionSiteExteriorConormal.lean#L116). The attribute's comment: “the opening clause H^{-1}(L_{B/A}) = H_1(C_{B/A}, Ω) = I/I² for a surjective A → B with I = ker(A → B), as an isomorphism of B-MODULES: the first left derived functor of the colimit over the opposite of the small model of the footnote-restricted site, applied to Ω = Ω_{𝒪/A} ⊗_𝒪 B̲, is the conormal module I/I² of the presentation of B by A itself. H_1(C_{B/A}, -) = L_1 colim at linear coefficients is Tag 08PF's definition; the first equality is Tag 08PU in degree 1 and the second is Tag 08RA. I/I² is (CommAlgCat.surjectionExtension A B h).Cotangent, which CommAlgCat.surjectionConormalAddEquiv identifies with Ideal.Cotangent (RingHom.ker (algebraMap A B)). No hypothesis beyond the remark's own surjectivity of A → B”.

> **Stacks 08RG**, the opening clause `H^{-1}(L_{B/A}) = H_1(C_{B/A}, Ω) = I/I²` for a
> surjective ring map `A → B` with kernel `I`, as an isomorphism of `B`-modules: the first
> homology of `C_{B/A}` with coefficients in `Ω = Ω_{𝒪/A} ⊗_𝒪 B̲` is the conormal module `I/I²` of
> the presentation of `B` by `A` itself.
>
> The first equality is Tag 08PU in degree `n = 1`, at linear coefficients
> (`CommAlgCat.leftDerivedColimPolynomialCotangentIso`); the second is Tag 08RA
> (`CommAlgCat.cotangentComplex_homologyNegOneIso`). The abelian-group form of the same clause is
> `CommAlgCat.polynomialSiteHomologyOneConormalIso`, which reads `H_1` as the sections at the
> point of `L₁π_!`.

```lean
def leftDerivedColimOneConormalLinearEquiv :
    ↥(((colim :
            ((smallBoundedPolynomialSite A B (standardResolutionVarCardinal A B))ᵒᵖ ⥤
              ModuleCat.{u} B) ⥤ ModuleCat.{u} B).leftDerived 1).obj
        (smallPolynomialCotangentModulePresheaf A B (standardResolutionVarCardinal A B))) ≃ₗ[B]
      (surjectionExtension.{u, u} A B h).Cotangent
```

**`CommAlgCat.exteriorPower_conormal_leftDerivedColim_symmetricPower_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectionSiteExteriorConormal.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SurjectionSiteExteriorConormal.lean#L164). The attribute's comment: “the second clause H_k(C_{B/A}, Sym^k_{B̲}(Ω)) = ∧^k_B(I/I²) for a surjective A → B with I = ker(A → B), as an isomorphism of B-modules, for every k, over an arbitrary commutative ring B and with no hypothesis beyond the remark's own surjectivity of A → B; in particular 2 need not be invertible. H_k(C_{B/A}, -) = L_k colim over the opposite of the small model of the footnote-restricted site at linear coefficients is Tag 08PF's definition of the homology of a category, Sym^k_{B̲} is the sectionwise symmetric power, which is the sheaf symmetric power because the topology of C_{B/A} is chaotic, and I/I² is (CommAlgCat.surjectionExtension A B h).Cotangent, the conormal module of the presentation of B by A itself, which CommAlgCat.surjectionConormalAddEquiv identifies with Ideal.Cotangent (RingHom.ker (algebraMap A B)). The deduction is the remark's own: Remark 08SG applied to ℱ = Ω, which is a flat B̲-module with H_0(C_{B/A}, Ω) = 0 on a site with a point resolution, composed with the remark's opening clause H_1(C_{B/A}, Ω) = I/I². Remark 08SG enters in the form Stacks.ChaoticSite.nonempty_linearEquiv_leftDerivedColim_symmetricPowerDiagram, which holds over every commutative ring by Illusie's and Quillen's décalage; 08SG's own sign-twisted S_k-coinvariants step is a proof erratum, refuted over ℤ by Stacks.ChaoticSite.not_quillenSignedCoinvariants_int, and plays no role here”.

> **Stacks 08RG**, the second clause `H_k(C_{B/A}, Sym^k(Ω)) = ∧^k_B(I/I²)`, which the remark
> gets from Remark 08SG applied to `Ω`.
>
> Let `A → B` be surjective with kernel `I` and let `Ω = Ω_{𝒪/A} ⊗_𝒪 B̲` on `C_{B/A}`. Then the
> `k`-th homology of `C_{B/A}` with coefficients in the `k`-th sectionwise symmetric power of `Ω`
> is the `k`-th exterior power of `I/I²` over `B`, for every `k`.
>
> The deduction is the remark's own: `Ω` is a flat `B̲`-module
> (`CommAlgCat.flat_smallPolynomialCotangentModulePresheaf_obj`) with `H_0(C_{B/A}, Ω) = 0`
> (`CommAlgCat.isZero_leftDerivedColimZero_polynomialCotangentModulePresheaf_of_surjective`) on a
> site with a point resolution
> (`CommAlgCat.isPointResolution_standardResolutionSmallCosimplicialObject`), so Remark 08SG
> applies and gives `H_k(C_{B/A}, Sym^k(Ω)) = ∧^k_B(H_1(C_{B/A}, Ω))`; the remark's opening clause
> `leftDerivedColimOneConormalLinearEquiv` then replaces `H_1(C_{B/A}, Ω)` by `I/I²`.
>
> No hypothesis is placed on `B`; in particular `2` need not be invertible. Remark 08SG is used in
> the form `Stacks.ChaoticSite.nonempty_linearEquiv_leftDerivedColim_symmetricPowerDiagram`, which
> holds over every commutative ring by décalage, and not through 08SG's own sign-twisted
> coinvariants step, which `Stacks.ChaoticSite.not_quillenSignedCoinvariants_int` refutes over
> `ℤ`; see the module docstring.

```lean
theorem exteriorPower_conormal_leftDerivedColim_symmetricPower_of_surjective (k : ℕ) :
    Nonempty (↥(((colim :
              ((smallBoundedPolynomialSite A B (standardResolutionVarCardinal A B))ᵒᵖ ⥤
                ModuleCat.{u} B) ⥤ ModuleCat.{u} B).leftDerived k).obj
            (Stacks.ChaoticSite.symmetricPowerDiagram
              (smallBoundedPolynomialSite A B (standardResolutionVarCardinal A B)) (B : Type u)
              (smallPolynomialCotangentModulePresheaf A B
                (standardResolutionVarCardinal A B)) k)) ≃ₗ[B]
        ⋀[(B : Type u)]^k (surjectionExtension.{u, u} A B h).Cotangent)
```

**`RingHom.torOneSelfIsoCotangent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TorQuotientSelf.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TorQuotientSelf.lean#L112). The attribute's comment: “the clause Tor_1^A(B, B) = I/I² for a surjective ring map f : A → B with I = ker f: the first Tor of B with itself over A is Ideal.Cotangent I, which is Mathlib's I/I². Tor is Mathlib's monoidal Tor on ModuleCat A, the left derived functor of the tensor product, so both sides are read as A-modules; each is annihilated by I and hence a B-module. The route is the vanishing of Tor_1^A(B, A), the long exact sequence of 0 → I → A → B → 0 tensored with B, and B ⊗_A I = I/I². No hypothesis beyond the remark's own surjectivity of A → B”.

> **Stacks 08RG**, the clause `Tor_1^A(B, B) = I/I²`: for a surjective ring map `f : A → B`
> with kernel `I`, the first Tor of `B` with itself over `A` is the conormal module `I/I²`.
>
> The route is the vanishing of `Tor_1^A(B, A)`, the long exact sequence of
> `0 → I → A → B → 0` tensored with `B`, and the identification `B ⊗_A I = I/I²`.

```lean
noncomputable def torOneSelfIsoCotangent
    {A B : Type u} [CommRing A] [CommRing B]
    (f : A →+* B) (hf : Function.Surjective f) :
    letI : Algebra A B := f.toAlgebra
    ((Tor (ModuleCat.{u} A) 1).obj
      (ModuleCat.of A B)).obj (ModuleCat.of A B) ≅
        ModuleCat.of A (RingHom.ker f).Cotangent
```

## Tag 09D6, a remark

[Tag 09D6](https://stacks.math.columbia.edu/tag/09D6) in the Stacks Project.

**`Stacks.Cotangent.TorTwo.cotangentHomologyTwoIsoTorTwoCoker`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/CotangentHomologyTwoTorCoker.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/CotangentHomologyTwoTorCoker.lean#L224). The attribute's comment: “H₂(L_{B/A}) is canonically Coker(Tor₂^{P₁}(B, B) → Tor₂^{P₀}(B, B)), the map being d₀ - d₁, for an arbitrary resolution P_• of B over A (Remark 08QI), as B-modules, with Tor₂^{P_n}(B, B) read as Ker(J_n ⊗_{P_n} J_n → J_n²); obtained from Remark 09D5, Stacks.Cotangent.cotangentComplexHomologyTwoLinearIsoTorOne, as the source obtains it”.

> `H₂(L_{B/A}) = Coker(Tor₂^{P₁}(B, B) → Tor₂^{P₀}(B, B))` for an arbitrary resolution `P_•`
> of `B` over `A`, as `B`-modules, where `Tor₂^{P_n}(B, B) = Ker(J_n ⊗_{P_n} J_n → J_n²)` and the
> map is `d₀ - d₁`. The isomorphism is Remark 09D5's `H₂(L_{B/A}) = H₀(C_{B/A}, Tor₁^𝒪(𝒥, B̲))`,
> followed by `H₀ = Coker(d₀ - d₁)` on the standard resolution and the canonical comparison of the
> cokernels of two resolutions.

```lean
def cotangentHomologyTwoIsoTorTwoCoker (hP : CommAlgCat.IsResolution A B P ε) :
    (cotangentComplex A B).homology (-2) ≅ torTwoCoker hP
```

**`Stacks.Cotangent.TorTwo.toHomologyTwo_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/CotangentHomologyTwoTorCoker.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/CotangentHomologyTwoTorCoker.lean#L264). The attribute's comment: “the exact sequence ∧²_B(J₀/J₀²) → Tor₂^{P₀}(B, B) → H^{-2}(L_{B/A}) → 0 for the resolution of Example 09D4: the last map is surjective”.

> The map `Tor₂^{P₀}(B, B) → H^{-2}(L_{B/A})` is surjective.

```lean
theorem toHomologyTwo_surjective : Function.Surjective (toHomologyTwo p)
```

**`Stacks.Cotangent.TorTwo.exact_wedgeAntisymm_toHomologyTwo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/CotangentHomologyTwoTorCoker.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/CotangentHomologyTwoTorCoker.lean#L274). The attribute's comment: “the exact sequence ∧²_B(J₀/J₀²) → Tor₂^{P₀}(B, B) → H^{-2}(L_{B/A}) → 0 for the resolution of Example 09D4: exactness at Tor₂^{P₀}(B, B), the first map being ā ∧ b̄ ↦ a ⊗ b - b ⊗ a”.

> The exact sequence `∧²_B(J₀/J₀²) → Tor₂^{P₀}(B, B) → H^{-2}(L_{B/A}) → 0` for the resolution
> of Example 09D4: exactness at `Tor₂^{P₀}(B, B)`, the first map being `ā ∧ b̄ ↦ a ⊗ b - b ⊗ a`; the
> second map is surjective by `toHomologyTwo_surjective`. Both maps are `B`-linear.

```lean
theorem exact_wedgeAntisymm_toHomologyTwo :
    Function.Exact (wedgeAntisymm (φ := aug p 0)) (toHomologyTwo p)
```

**`Stacks.Cotangent.TorTwo.Explicit.decomposition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TorTwoExplicitResolution.lean, line 486](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TorTwoExplicitResolution.lean#L486). The attribute's comment: “the decomposition Tor₂^{P₁}(B, B) = ∧²(⨁_{t ∈ T} B) ⊕ ⨁_{t ∈ T} J₀/J₀² ⊕ Tor₂^{P₀}(B, B) for the resolution P_• of Example 09D4, as B-modules, with Tor₂^{P_n}(B, B) read as Ker(J_n ⊗_{P_n} J_n → J_n²) (the remark's own identification, Stacks.Cotangent.torTwoSelfIsoMulKernel); the correspondences are decomposition_wedge, decomposition_mixed and decomposition_degen”.

> **The decomposition of `Tor₂^{P₁}(B, B)` for the explicit resolution**:
>
> `Tor₂^{P₁}(B, B) = ∧²_B(⨁_{t ∈ T} B) ⊕ ⨁_{t ∈ T} J₀/J₀² ⊕ Tor₂^{P₀}(B, B)`
>
> as `B`-modules, `Tor₂` read in the tensor-kernel model. The correspondences are
> `decomposition_wedge`, `decomposition_mixed` and `decomposition_degen`.

```lean
def decomposition :
    (⋀[target p]^2 (p.relationIndex →₀ target p) ×
        (p.relationIndex →₀ (RingHom.ker (aug p 0)).Cotangent) × mulKernel (aug p 0)) ≃ₗ[target p]
      mulKernel (aug p 1)
```

**`Stacks.Cotangent.TorTwo.Explicit.decomposition_wedge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TorTwoExplicitResolution.lean, line 504](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TorTwoExplicitResolution.lean#L504). The attribute's comment: “the basis element x_t ∧ x_{t'} of the first summand corresponds to x_t ⊗ x_{t'} - x_{t'} ⊗ x_t in J₁ ⊗_{P₁} J₁”.

> The basis element `x_t ∧ x_{t'}` of `∧²(⨁_T B)` corresponds to
> `x_t ⊗ x_{t'} - x_{t'} ⊗ x_t`.

```lean
theorem decomposition_wedge (t t' : p.relationIndex) :
    decomposition p (wedgeBilin (Finsupp.single t 1) (Finsupp.single t' 1), 0, 0) =
      antisymm (xJ p t) (xJ p t')
```

**`Stacks.Cotangent.TorTwo.Explicit.decomposition_mixed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TorTwoExplicitResolution.lean, line 514](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TorTwoExplicitResolution.lean#L514). The attribute's comment: “for f ∈ J₀ the element x_t ⊗ f̄ of the second summand corresponds to x_t ⊗ s₀(f) - s₀(f) ⊗ x_t in J₁ ⊗_{P₁} J₁”.

> For `f ∈ J₀`, the element `x_t ⊗ f̄` of `⨁_T J₀/J₀²` corresponds to
> `x_t ⊗ s₀(f) - s₀(f) ⊗ x_t`.

```lean
theorem decomposition_mixed (t : p.relationIndex) (f : RingHom.ker (aug p 0)) :
    decomposition p (0, Finsupp.single t ((RingHom.ker (aug p 0)).toCotangent f), 0) =
      antisymm (xJ p t) (degenJ p f)
```

**`Stacks.Cotangent.TorTwo.Explicit.decomposition_degen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TorTwoExplicitResolution.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TorTwoExplicitResolution.lean#L522). The attribute's comment: “the map Tor₂^{P₀}(B, B) → Tor₂^{P₁}(B, B) onto the last summand is given by s₀”.

> The map `Tor₂^{P₀}(B, B) → Tor₂^{P₁}(B, B)` onto the last summand is given by `s₀`.

```lean
theorem decomposition_degen (k : mulKernel (aug p 0)) :
    decomposition p (0, 0, k) = mulKernelMap (degenMap p) (aug_comp_degenMap p) k
```

**`Stacks.Cotangent.TorTwo.Explicit.face_degen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TorTwoExplicitResolution.lean, line 545](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TorTwoExplicitResolution.lean#L545). The attribute's comment: “d₀ - d₁ : Tor₂^{P₁}(B, B) → Tor₂^{P₀}(B, B) is zero on the last summand”.

> `d₀ - d₁` vanishes on the summand `Tor₂^{P₀}(B, B)`.

```lean
theorem face_degen (k : mulKernel (aug p 0)) :
    face p (mulKernelMap (degenMap p) (aug_comp_degenMap p) k) = 0
```

**`Stacks.Cotangent.TorTwo.Explicit.face_mixed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TorTwoExplicitResolution.lean, line 552](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TorTwoExplicitResolution.lean#L552). The attribute's comment: “d₀ - d₁ maps x_t ⊗ f̄ to f ⊗ f_t - f_t ⊗ f”.

> `d₀ - d₁` sends `x_t ⊗ f̄` to `f ⊗ f_t - f_t ⊗ f`.

```lean
theorem face_mixed (t : p.relationIndex) (f : RingHom.ker (aug p 0)) :
    face p (antisymm (xJ p t) (degenJ p f)) = antisymm f (relJ p t)
```

**`Stacks.Cotangent.TorTwo.Explicit.face_wedge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TorTwoExplicitResolution.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TorTwoExplicitResolution.lean#L560). The attribute's comment: “d₀ - d₁ maps x_t ∧ x_{t'} to f_{t'} ⊗ f_t - f_t ⊗ f_{t'}”.

> `d₀ - d₁` sends `x_t ∧ x_{t'}` to `f_{t'} ⊗ f_t - f_t ⊗ f_{t'}`.

```lean
theorem face_wedge (t t' : p.relationIndex) :
    face p (antisymm (xJ p t) (xJ p t')) = antisymm (relJ p t') (relJ p t)
```

**`Stacks.Cotangent.TorTwo.Explicit.torTwoDecomposition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TorTwoExplicitResolution.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TorTwoExplicitResolution.lean#L592). The attribute's comment: “the decomposition of Tor₂^{P₁}(B, B) read on Mathlib's Tor' itself”.

> **The decomposition of `Tor₂^{P₁}(B, B)`, on Mathlib's `Tor'`**: for the
> `P₁`-algebra `B` (through the augmentation),
>
> `Tor₂^{P₁}(B, B) ≅ ∧²_B(⨁_T B) ⊕ ⨁_T J₀/J₀² ⊕ Tor₂^{P₀}(B, B)`,
>
> an additive isomorphism which is `P₁`-linear for `P₁` acting on the right through `P₁ → B`
> (`torTwoDecomposition_smul`). It is `Stacks.Cotangent.torTwoSelfIsoMulKernel` followed by the
> inverse of `decomposition`.

```lean
def torTwoDecomposition :
    letI : Algebra (term p 1) (target p) := (aug p 1).toAlgebra
    ((CategoryTheory.Tor' (ModuleCat.{max u v w x} (term p 1)) 2).obj
        (ModuleCat.of (term p 1) (target p))).obj (ModuleCat.of (term p 1) (target p)) ≃+
      (⋀[target p]^2 (p.relationIndex →₀ target p) ×
        (p.relationIndex →₀ (RingHom.ker (aug p 0)).Cotangent) × mulKernel (aug p 0))
```

**`Stacks.Cotangent.torTwoSelfIsoTorOneIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TorTwoQuotientSelf.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TorTwoQuotientSelf.lean#L110). The attribute's comment: “Tor₂^P(B, B) = Tor₁^P(J, B)”.

> **Stacks 09D6**, first identification. For a surjection `P → B` with kernel `J`, the
> connecting homomorphism of `0 → J → P → B → 0` for the functor `- ⊗ B` is an isomorphism
> `Tor₂^P(B, B) ≅ Tor₁^P(J, B)`: the two flanking terms are `Tor_i^P(P, B)` for `i = 1, 2`, which
> vanish because `P` is projective over itself.

```lean
noncomputable def torTwoSelfIsoTorOneIdeal (hf : Function.Surjective (algebraMap P B)) :
    ((Tor' (ModuleCat.{u} P) 2).obj (ModuleCat.of P B)).obj (ModuleCat.of P B) ≅
      ((Tor' (ModuleCat.{u} P) 1).obj
          (ModuleCat.of P (RingHom.ker (algebraMap P B)))).obj (ModuleCat.of P B)
```

**`Stacks.Cotangent.torOneIdealIsoMulKernel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TorTwoQuotientSelf.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TorTwoQuotientSelf.lean#L159). The attribute's comment: “Tor₁^P(J, B) = Ker(J ⊗_P J → J²)”.

> **Stacks 09D6**, second identification. For a surjection `P → B` with kernel `J`, the
> connecting homomorphism of `0 → J → P → B → 0` for the functor `J ⊗ -` identifies
> `Tor₁^P(J, B)` with the kernel of the multiplication map `J ⊗_P J → J²`.

```lean
noncomputable def torOneIdealIsoMulKernel (hf : Function.Surjective (algebraMap P B)) :
    ((Tor' (ModuleCat.{u} P) 1).obj
          (ModuleCat.of P (RingHom.ker (algebraMap P B)))).obj (ModuleCat.of P B) ≅
      ModuleCat.of P ↥(LinearMap.ker (Submodule.mulMap' (RingHom.ker (algebraMap P B))
        (RingHom.ker (algebraMap P B))))
```

**`Stacks.Cotangent.torTwoSelfIsoMulKernel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/TorTwoQuotientSelf.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/TorTwoQuotientSelf.lean#L218). The attribute's comment: “Tor₂^P(B, B) = Tor₁^P(J, B) = Ker(J ⊗_P J → J²)”.

> **Stacks 09D6**, the composite identification
> `Tor₂^P(B, B) = Ker(J ⊗_P J → J²)` for a surjection `P → B` with kernel `J`.

```lean
noncomputable def torTwoSelfIsoMulKernel (hf : Function.Surjective (algebraMap P B)) :
    ((Tor' (ModuleCat.{u} P) 2).obj (ModuleCat.of P B)).obj (ModuleCat.of P B) ≅
      ModuleCat.of P ↥(LinearMap.ker (Submodule.mulMap' (RingHom.ker (algebraMap P B))
        (RingHom.ker (algebraMap P B))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.12, Tag 08RC](https://stacks.math.columbia.edu/tag/08RC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
