---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.ProjAndSpecBlowup.truncationProjIsoBlowUp, Stacks.AlgebraicGeometry.ProjAndSpecBlowup.truncationProjIsoBlowUp_hom_blowUpToBase, Stacks.AlgebraicGeometry.ProjAndSpecBlowup.whereInvertible_one_eq_top, Stacks.AlgebraicGeometry.ProjAndSpecChartIdeals.map_irrelevant_le_ker_chartTau, Stacks.AlgebraicGeometry.ProjAndSpecChartIdeals.chartSigma_self_mem_nonZeroDivisors, Stacks.AlgebraicGeometry.ProjAndSpecChartIdeals.span_chartSigma_self_eq_map_span, Stacks.AlgebraicGeometry.ProjAndSpecChartIdeals.radical_span_chartSigma_self_eq_radical_ker, Stacks.AlgebraicGeometry.ProjAndSpecChartIdeals.span_chartSigma_self_eq_ker_of_mem_one
statement: formalized
proof: formalized
---

# 37.51 Proj and Spec

Section 37.51 of the Stacks Project, [Tag 0EKF](https://stacks.math.columbia.edu/tag/0EKF). 4 tags here are carried by 223 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EKF, the section

[Tag 0EKF](https://stacks.math.columbia.edu/tag/0EKF) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjAndSpecBlowup.truncationProjIsoBlowUp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecBlowup.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecBlowup.lean#L114). The attribute's comment: “L → X is the blowup of X along Z when A is generated over A₀ by f₁, …, f\_r ∈ A₁”.

> **`L → X` is the blowup of `X` along `Z`**: for `A` generated over `A_0` by
> `f_1, …, f_r ∈ A_1`, the cone `L = Proj(⨁_{d ≥ 0} A_{≥ d})` is the blowup of `X = Spec A` in the
> ideal sheaf of the closed subscheme `Z = V(A_+)`. It is an isomorphism over `X` by
> `truncationProjIsoBlowUp_hom_blowUpToBase`.

```lean
def truncationProjIsoBlowUp :
    AlgebraicGeometry.Proj (grading 𝒜) ≅ blowUp (ProjAndSpec.zToX 𝒜).ker
```

**`Stacks.AlgebraicGeometry.ProjAndSpecBlowup.truncationProjIsoBlowUp_hom_blowUpToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecBlowup.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecBlowup.lean#L122). The attribute's comment: “the identification of L with the blowup of X along Z is one over X”.

> **The isomorphism `L ≅ Bl_Z X` is an isomorphism over `X`**: it carries the blowing-up
> morphism to the structure morphism `L → X` of the cone.

```lean
theorem truncationProjIsoBlowUp_hom_blowUpToBase :
    (truncationProjIsoBlowUp hf hgen).hom ≫ blowUpToBase (ProjAndSpec.zToX 𝒜).ker =
      ProjAndSpec.toSpecA (ProjAndSpecTruncation.truncationConeData 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecBlowup.whereInvertible_one_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecBlowup.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecBlowup.lean#L133). The attribute's comment: “W = P when A is generated over A₀ by f₁, …, f\_r ∈ A₁”.

> **`W = P`**: for `A` generated over `A_0` by `f_1, …, f_r ∈ A_1`, the largest open of
> `P = Proj A` on which `𝒪_P(1)` is invertible and the multiplication maps
> `𝒪_P(n) ⊗ 𝒪_P(m) → 𝒪_P(n + m)` are isomorphisms is all of `P`.

```lean
theorem whereInvertible_one_eq_top {r : ℕ} {f : Fin r → A} (hf : ∀ i, f i ∈ 𝒜 1)
    (hgen : Algebra.adjoin (𝒜 0) (Set.range f) = ⊤) :
    ProjInvertibleLocus.whereInvertible 𝒜 1 = ⊤
```

**`Stacks.AlgebraicGeometry.ProjAndSpecChartIdeals.map_irrelevant_le_ker_chartTau`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecChartIdeals.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecChartIdeals.lean#L115). The attribute's comment: “(1): σ(A₊)(B[1/g])₀ ⊆ Ker(τ : (B[1/g])₀ → (A[1/f])₀), g = ψ(f)”.

> **(1) `σ(A₊)(B[1/g])₀ ⊆ Ker(τ : (B[1/g])₀ → (A[1/f])₀)`** for `g = ψ(f)`.

```lean
theorem map_irrelevant_le_ker_chartTau (f : A) :
    Ideal.map (chartSigma 𝒜 f) (HomogeneousIdeal.irrelevant 𝒜).toIdeal ≤
      RingHom.ker (chartTau 𝒜 f)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecChartIdeals.chartSigma_self_mem_nonZeroDivisors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecChartIdeals.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecChartIdeals.lean#L122). The attribute's comment: “(2): σ(f) is a nonzerodivisor of (B[1/g])₀, g = ψ(f)”.

> **(2) `σ(f)` is a nonzerodivisor of `(B[1/g])₀`**, for `f ∈ A_d` and `g = ψ(f)`.

```lean
theorem chartSigma_self_mem_nonZeroDivisors (hf : f ∈ 𝒜 d) :
    chartSigma 𝒜 f f ∈ nonZeroDivisors (Away (grading 𝒜) (psi 𝒜 f))
```

**`Stacks.AlgebraicGeometry.ProjAndSpecChartIdeals.span_chartSigma_self_eq_map_span`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecChartIdeals.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecChartIdeals.lean#L143). The attribute's comment: “(3): σ(f)(B[1/g])₀ = σ(A\_d)(B[1/g])₀ as ideals, g = ψ(f)”.

> **(3) `σ(f)(B[1/g])₀ = σ(A_d)(B[1/g])₀` as ideals**, for `f ∈ A_d` and `g = ψ(f)`.

```lean
theorem span_chartSigma_self_eq_map_span (hf : f ∈ 𝒜 d) :
    Ideal.span {chartSigma 𝒜 f f} =
      Ideal.map (chartSigma 𝒜 f) (Ideal.span (𝒜 d : Set A))
```

**`Stacks.AlgebraicGeometry.ProjAndSpecChartIdeals.radical_span_chartSigma_self_eq_radical_ker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecChartIdeals.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecChartIdeals.lean#L183). The attribute's comment: “(4): σ(f)(B[1/g])₀ and Ker(τ : (B[1/g])₀ → (A[1/f])₀) have the same radical, g = ψ(f), f ∈ A\_d, d > 0”.

> **(4) `σ(f)(B[1/g])₀` and `Ker(τ : (B[1/g])₀ → (A[1/f])₀)` have the same radical**, for
> `f ∈ A_d` with `d > 0` and `g = ψ(f)`.

```lean
theorem radical_span_chartSigma_self_eq_radical_ker (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    (Ideal.span {chartSigma 𝒜 f f}).radical = (RingHom.ker (chartTau 𝒜 f)).radical
```

**`Stacks.AlgebraicGeometry.ProjAndSpecChartIdeals.span_chartSigma_self_eq_ker_of_mem_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecChartIdeals.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecChartIdeals.lean#L207). The attribute's comment: “(5): if d = 1 then σ(f)(B[1/g])₀ = Ker(τ : (B[1/g])₀ → (A[1/f])₀), g = ψ(f)”.

> **(5) If `d = 1` then `σ(f)(B[1/g])₀ = Ker(τ : (B[1/g])₀ → (A[1/f])₀)`**, for `f ∈ A_1` and
> `g = ψ(f)`.

```lean
theorem span_chartSigma_self_eq_ker_of_mem_one (hf : f ∈ 𝒜 1) :
    Ideal.span {chartSigma 𝒜 f f} = RingHom.ker (chartTau 𝒜 f)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecChartIdeals.range_zeroSection_inter_basicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecChartIdeals.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecChartIdeals.lean#L230). The attribute's comment: “0(D₊(f)) = V(σ(f)) ⊆ D₊(g) set theoretically, g = ψ(f)”.

> **Inside `D₊(g)`, `g = ψ(f)`, the image of the zero section is the zero locus of `σ(f)`**:
> `0(D₊(f)) = V(σ(f)) ⊆ D₊(g)` set theoretically, the complement in `D₊(g)` of `D₊(σ(f) g)`.

```lean
theorem range_zeroSection_inter_basicOpen (f : A) (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    Set.range (zeroSection 𝒜) ∩ (Proj.basicOpen (grading 𝒜) (psi 𝒜 f) : Set _) =
      (Proj.basicOpen (grading 𝒜) (psi 𝒜 f) : Set _) \
        (Proj.basicOpen (grading 𝒜) (((sigma 𝒜 f : grading 𝒜 0) : TruncationRing 𝒜) *
          psi 𝒜 f) : Set _)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.projAndSpec_diagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecDiagram.lean, line 497](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecDiagram.lean#L497). The attribute's comment: “the commutative diagram of the section: π : L = Proj(B) → P is a cone, L = Spec\_P(⨁\_\{m ≥ 0} O\_P(m)) with vertex 0 : P → L, π ∘ 0 = id\_P, U = Spec\_P(⨁\_\{m ∈ Z} O\_P(m)) over P is the part of L over U ⊆ X, the squares over U → X → Z commute, and 0 maps set theoretically onto the inverse image of Z in L”. References: EGA II (8.6.3), “special case”.

> **The diagram of [Stacks, Tag 0EKG].** Let `A` be a graded ring, `X = Spec A`,
> `Z = V(A₊) = Spec A₀`, `U = X ∖ Z`, `P = Proj A`, and let `L = Proj B` for
> `B = ⨁_{d ≥ 0} A_{≥ d}`, with cone projection `π : L ⟶ P`, structure morphism `σ : L ⟶ X` and zero
> section `0 : P ⟶ L`. Then, writing `j : Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) ⟶ L` for the top-left arrow and
> `e : Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) ≅ U` for the left identification:
>
> * `π` is a cone over `P` (`truncationCone`, graded by `⨁_{m ≥ 0} 𝒪_P(m)`, whose pieces are the
>   twisting sheaves `𝒪_P(m)`, `m ≥ 0`), and `L = Spec_P(⨁_{m ≥ 0} 𝒪_P(m))` over `P`;
> * `j` lies over `P`, it is an open immersion, and its image is the part of `L` over `U`;
> * `e` is an identification over `P`;
> * the left square `j ≫ σ = e ≫ (U ⟶ X)` and the right square `π ≫ (P ⟶ Z) = σ ≫ (X ⟶ Z)`
>   commute;
> * the zero section is a section of `π`, it is the vertex of the cone (pulling back along it kills
>   the pieces `𝒪_P(m)`, `m > 0`, of `π_* 𝒪_L`), and it maps set theoretically onto the inverse image
>   of `Z` in `L`.

```lean
theorem projAndSpec_diagram :
    -- `π` is a cone over `P`, graded by the nonnegative twists
    (truncationCone 𝒜).π = pi 𝒜 ∧
    (truncationCone 𝒜).grading = nonnegTwistAlgebra 𝒜 ∧
    (truncationCone 𝒜).ι = coneIota 𝒜 ∧
    (∀ m : ℕ, (truncationCone 𝒜).grading.piece m = twistingSheaf 𝒜 m) ∧
    (∀ m : ℤ, (integerTwistAlgebra 𝒜).piece m = twistingSheaf 𝒜 m) ∧
    -- `L = Spec_P(⨁_{m ≥ 0} 𝒪_P(m))` over `P`
    (coneProjIsoRelativeSpecTwistAlgebra 𝒜).hom ≫
        relativeSpecToBase (nonnegTwistAlgebraSheaf 𝒜) = pi 𝒜 ∧
    -- the top-left arrow lies over `P`, is an open immersion, with image the part of `L` over `U`
    puncturedToConeProj 𝒜 ≫ pi 𝒜 = relativeSpecToBase (integerTwistAlgebraSheaf 𝒜) ∧
    IsOpenImmersion (puncturedToConeProj 𝒜) ∧
    (puncturedToConeProj 𝒜).opensRange = openUInL 𝒜 ∧
    -- the left identification `Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) = U` lies over `P`
    (puncturedConeRelativeSpecTwistAlgebraIsoOpenU 𝒜).hom ≫ openUToProj 𝒜 =
      relativeSpecToBase (integerTwistAlgebraSheaf 𝒜) ∧
    -- the left square
    puncturedToConeProj 𝒜 ≫ toSpecA 𝒜 =
      (puncturedConeRelativeSpecTwistAlgebraIsoOpenU 𝒜).hom ≫ (ProjAndSpec.openU 𝒜).ι ∧
    -- the right square
    pi 𝒜 ≫ Proj.toSpecZero 𝒜 = toSpecA 𝒜 ≫ ProjAndSpec.xToZ 𝒜 ∧
    -- the zero section
    zeroSection 𝒜 ≫ pi 𝒜 = 𝟙 (AlgebraicGeometry.Proj 𝒜) ∧
    (∀ (m : ℤ), 0 < m → ∀ (U : Opens (ProjectiveSpectrum.top 𝒜))
        (s : (nonnegTwistingSheaf 𝒜 m).val.obj (op U)),
      (zeroSection 𝒜).appLE (pi 𝒜 ⁻¹ᵁ U) U (le_zeroSection_preimage_pi_preimage 𝒜 U)
        ((coneIota 𝒜 m).val.app (op U) s) = 0) ∧
    Set.range (zeroSection 𝒜) = toSpecA 𝒜 ⁻¹' Set.range (ProjAndSpec.zToX 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecDivisor.exists_isEffectiveCartierDivisor_sigmaIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecDivisor.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecDivisor.lean#L157). The attribute's comment: “if P is quasi-compact, then for d sufficiently divisible the closed subscheme D ⊆ L cut out by σ(A\_d)𝒪\_L is an effective Cartier divisor, 0 : P → L factors through D, and 0(P) = D set theoretically”.

> **Stacks, Section 0EKF: if `P` is quasi-compact, then for `d` sufficiently divisible the
> closed subscheme `D ⊆ L` cut out by `σ(A_d)𝒪_L` is an effective Cartier divisor, `0 : P → L`
> factors through `D`, and `0(P) = D` set theoretically.** "Sufficiently divisible" is divisibility
> by a positive integer `d₀`, the product of the degrees of finitely many homogeneous elements of
> positive degree whose standard opens cover `P`.

```lean
theorem exists_isEffectiveCartierDivisor_sigmaIdealSheaf
    [CompactSpace (AlgebraicGeometry.Proj 𝒜)] :
    ∃ d₀ : ℕ, 0 < d₀ ∧ ∀ d : ℕ, 0 < d → d₀ ∣ d →
      Stacks.Divisors.IsEffectiveCartierDivisor (sigmaIdealSheaf 𝒜 d) ∧
      (∃ g : AlgebraicGeometry.Proj 𝒜 ⟶ (sigmaIdealSheaf 𝒜 d).subscheme,
        g ≫ (sigmaIdealSheaf 𝒜 d).subschemeι = zeroSection 𝒜) ∧
      ((sigmaIdealSheaf 𝒜 d).support : Set (AlgebraicGeometry.Proj (grading 𝒜))) =
        Set.range (zeroSection 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecInvertibleLocus.coneRestrictIsoVectorBundle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecInvertibleLocus.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecInvertibleLocus.lean#L126). The attribute's comment: “over the open W of Tag 01MU for d = 1, L|\_W is the vector bundle V(O\_P(1)|\_W)”.

> **`L|_W = π⁻¹(W) ≅ 𝐕(𝒪_P(1)|_W)`**: over the open `W` of [Stacks, Tag 01MU] for `d = 1` the
> cone is the vector bundle of `𝒪_P(1)|_W`, the relative spectrum of its symmetric algebra.

```lean
def coneRestrictIsoVectorBundle :
    (pi 𝒜 ⁻¹ᵁ locus 𝒜).toScheme ≅ vectorBundle (locus 𝒜).toScheme (twistOneRestrict 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecInvertibleLocus.coneRestrictIsoVectorBundle_hom_comp_vectorBundleToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecInvertibleLocus.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecInvertibleLocus.lean#L145). The attribute's comment: “the identification L|\_W = V(O\_P(1)|\_W) is one over W”.

> **The isomorphism `L|_W ≅ 𝐕(𝒪_P(1)|_W)` lies over `W`**: followed by the projection of the
> vector bundle it is the restriction `π|_W` of the cone projection.

```lean
theorem coneRestrictIsoVectorBundle_hom_comp_vectorBundleToBase :
    (coneRestrictIsoVectorBundle 𝒜).hom ≫ vectorBundleToBase _ (twistOneRestrict 𝒜) =
      pi 𝒜 ∣_ locus 𝒜
```

**`Stacks.AlgebraicGeometry.ProjAndSpecInvertibleLocus.zeroSectionRestrict_comp_coneRestrictIsoVectorBundle_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecInvertibleLocus.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecInvertibleLocus.lean#L181). The attribute's comment: “under L|\_W = V(O\_P(1)|\_W) the zero section 0|\_W is the zero section of the vector bundle”.

> **Under `L|_W ≅ 𝐕(𝒪_P(1)|_W)` the zero section `0|_W` is the zero section of the vector
> bundle**, the point of `𝐕(𝒪_P(1)|_W)` over `W` whose module morphism is zero.

```lean
theorem zeroSectionRestrict_comp_coneRestrictIsoVectorBundle_hom :
    zeroSectionRestrict 𝒜 ≫ (coneRestrictIsoVectorBundle 𝒜).hom =
      (vectorBundleOverZeroSection (twistOneRestrict 𝒜)).left
```

**`Stacks.AlgebraicGeometry.ProjAndSpecInvertibleLocus.isEffectiveCartierDivisor_ker_zeroSectionRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecInvertibleLocus.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecInvertibleLocus.lean#L293). The attribute's comment: “0(W) is an effective Cartier divisor on L|\_W”.

> **`0(W)` is an effective Cartier divisor on `L|_W`**: the ideal sheaf of the closed
> immersion `0|_W : W ⟶ L|_W` is invertible. Over the part of `L|_W` lying above a standard open
> `D₊(cb)` with `deg c = deg b + 1` it is generated by the fibre coordinate.

```lean
theorem isEffectiveCartierDivisor_ker_zeroSectionRestrict :
    Stacks.Divisors.IsEffectiveCartierDivisor (zeroSectionRestrict 𝒜).ker
```

**`Stacks.AlgebraicGeometry.ProjAndSpecInvertibleLocus.coe_preimage_openUInL_eq_compl_range_zeroSectionRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecInvertibleLocus.lean, line 304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecInvertibleLocus.lean#L304). The attribute's comment: “U|\_W is the complement of the zero section of L|\_W”.

> **`U|_W` is the complement of the zero section**: a point of `L|_W` lies in the punctured
> cone `U` exactly when it is not in the image of `0|_W`.

```lean
theorem coe_preimage_openUInL_eq_compl_range_zeroSectionRestrict :
    (((pi 𝒜 ⁻¹ᵁ locus 𝒜).ι ⁻¹ᵁ openUInL 𝒜 : (pi 𝒜 ⁻¹ᵁ locus 𝒜).toScheme.Opens) :
        Set (pi 𝒜 ⁻¹ᵁ locus 𝒜).toScheme) =
      (Set.range (zeroSectionRestrict 𝒜))ᶜ
```

**`Stacks.AlgebraicGeometry.ProjAndSpecInvertibleLocus.zeroSectionRestrict_comp_coneRestrictIsoVectorBundle_hom_eq_vectorBundleZeroSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecInvertibleLocusZeroSection.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecInvertibleLocusZeroSection.lean#L48). The attribute's comment: “under L|\_W = V(O\_P(1)|\_W) the zero section 0|\_W is the zero section of the vector bundle, the section cut out by the augmentation Sym → O\_W”.

> **Under `L|_W ≅ 𝐕(𝒪_P(1)|_W)` the zero section `0|_W` is the zero section of the vector
> bundle**, the section of `𝐕(𝒪_P(1)|_W) ⟶ W` cut out by the augmentation
> `Sym(𝒪_P(1)|_W) ⟶ 𝒪_W`.

```lean
theorem zeroSectionRestrict_comp_coneRestrictIsoVectorBundle_hom_eq_vectorBundleZeroSection :
    zeroSectionRestrict 𝒜 ≫ (coneRestrictIsoVectorBundle 𝒜).hom =
      vectorBundleZeroSection (locus 𝒜).toScheme (twistOneRestrict 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTruncation.isIso_toSpecA_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecIsoOverU.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecIsoOverU.lean#L235). The attribute's comment: “L → X is an isomorphism over U”.

> **The structure morphism `L ⟶ X` is an isomorphism over `U = X ∖ V(A₊)`.** This is the
> equality on the left of the diagram of [Stacks, Tag 0EKG]: being an isomorphism over an open is
> local on that open, and over each standard open of a positive-degree homogeneous element the
> morphism is an isomorphism.

```lean
theorem isIso_toSpecA_restrict : IsIso (toSpecA 𝒜 ∣_ ProjAndSpec.openU 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTruncation.truncationConeData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean#L366). The attribute's comment: “the graded ring B = ⨁\_\{d ≥ 0} A\_\{≥ d} with σ : A → B₀, the graded ring maps ψ : A → B and τ : B → A, and τ ∘ ψ = id\_A”.

> The truncation algebra `B = ⨁_{d ≥ 0} A_{≥ d}` is cone data over `A`: the maps `ψ`,
> `τ` and `σ` satisfy `τ ∘ ψ = id`, the two formulas tying `σ` to `ψ` and `τ`, and the three
> divisibility conditions.

```lean
def truncationConeData : ProjAndSpec.ConeData 𝒜 (grading 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTruncation.pi_preimage_basicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean, line 407](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean#L407). The attribute's comment: “ψ defines π : L → P, and π⁻¹(D₊(f)) = D₊(ψ(f)) for f ∈ A\_d, d > 0”.

> The inverse image under `π` of a standard open of `P` is the standard open of the image
> element: `π⁻¹(D₊(f)) = D₊(ψ f)`.

```lean
theorem pi_preimage_basicOpen (f : A) (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    pi 𝒜 ⁻¹ᵁ Proj.basicOpen 𝒜 f = Proj.basicOpen (grading 𝒜) (psi 𝒜 f)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTruncation.isAffineHom_pi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean, line 413](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean#L413). The attribute's comment: “π : L → P is an affine morphism”.

> The cone projection of the truncation algebra is affine.

```lean
theorem isAffineHom_pi : IsAffineHom (pi 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTruncation.isClosedImmersion_zeroSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean#L423). The attribute's comment: “the surjection τ defines a closed immersion 0 : P → L”.

> The zero section of the truncation algebra is a closed immersion.

```lean
theorem isClosedImmersion_zeroSection : IsClosedImmersion (zeroSection 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTwistPushforward.twistPushforwardHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforward.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforward.lean#L84). The attribute's comment: “the inclusion O\_P(m) to pi\_* O\_L(i), for m ≥ i, as a morphism of sheaves of O\_P-modules, for the truncation cone”.

> **The inclusion `𝒪_P(m) ⟶ π_* 𝒪_L(i)`, for `m ≥ i`**: the morphism of sheaves of
> `𝒪_P`-modules glued from the local inclusions `(A[1/f])_m ⊆ (B[1/ψ f])_i`.

```lean
def twistPushforwardHom (i m : ℤ) (him : i ≤ m) :
    twistingSheaf 𝒜 m ⟶ twistPushforward 𝒜 i
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTwistPushforward.twistPushforwardDirectSumHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforward.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforward.lean#L103). The attribute's comment: “the inclusions O\_P(m) to pi\_* O\_L(i), m ≥ i, as one morphism out of the objectwise direct sum, for the truncation cone”.

> **The inclusions `𝒪_P(m) ⟶ π_* 𝒪_L(i)`, `m ≥ i`, as one morphism out of the objectwise
> direct sum.**

```lean
def twistPushforwardDirectSumHom (i : ℤ) :
    Stacks.directSum (fun m : {m : ℤ // i ≤ m} => (twistingSheaf 𝒜 m.1).val) ⟶
      (twistPushforward 𝒜 i).val
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTwistPushforward.twistSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforward.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforward.lean#L129). The attribute's comment: “the identification of the sections of O\_L(i) over D+(psi f) = pi^\{-1}(D+(f)) with ⨁\_\{m ≥ i} of the sections of O\_P(m) over D+(f)”.

> The standard-open description of the sections of `𝒪_L(i)` over `D₊(ψ f)`:
> `⨁_{m ≥ i} Γ(D₊(f), 𝒪_P(m)) ≃+ Γ(D₊(ψ f), 𝒪_L(i))`, the composite of the descriptions of the
> summands, the equality of homogeneous parts `⨁_{m ≥ i} (A[1/f])_m = (B[1/ψ f])_i`, and the
> description of the sections of `𝒪_L(i)` over `D₊(ψ f)`.

```lean
def twistSectionsEquiv (i : ℤ) {d : ℕ} {f : A} (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    (DirectSum {m : ℤ // i ≤ m} fun m =>
        ↥((twistingSheaf 𝒜 m.1).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f)))) ≃+
      ↥((twistingSheaf (grading 𝒜) i).val.obj
        (op (ProjectiveSpectrum.basicOpen (grading 𝒜) (psi 𝒜 f))))
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTwistPushforward.bijective_twistPushforwardSectionsHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforward.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforward.lean#L179). The attribute's comment: “the identification pi\_* O\_L(i) = ⨁\_\{m ≥ i} O\_P(m) over one standard open D+(f) of P is bijective, with the summands written as the sections of the twisting sheaves”.

> **The standard-open description of the sections of `π_* 𝒪_L(i)` is bijective.**

```lean
theorem bijective_twistPushforwardSectionsHom (i : ℤ) {d : ℕ} {f : A} (hf : f ∈ 𝒜 d)
    (hd : 0 < d) : Function.Bijective (twistPushforwardSectionsHom 𝒜 i hf hd)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTwistPushforward.bijective_twistPushforwardDirectSumHom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforward.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforward.lean#L201). The attribute's comment: “the morphism out of the objectwise direct sum over m ≥ i of the twisting sheaves O\_P(m) into pi\_* O\_L(i) is bijective on the sections over a standard open of a positive-degree homogeneous element, for the truncation cone”.

> **Over a standard open of a positive-degree homogeneous element the comparison out of the
> direct sum is bijective.**

```lean
theorem bijective_twistPushforwardDirectSumHom_app (i : ℤ) (p : PositiveElem 𝒜) :
    Function.Bijective
      ((twistPushforwardDirectSumHom 𝒜 i).app (op (positiveBasicOpen 𝒜 p))).hom
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTwistPushforward.twistPushforwardCoproductIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforward.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforward.lean#L237). The attribute's comment: “the footnote pi\_* O\_L(i) = ⨁ O\_P(m), as an isomorphism of sheaves of O\_P-modules for every integer i, the direct sum being the coproduct. The footnote of the source reads m ≥ -i; the correct range, given by the section's own formula (B[1/g])\_\{m'} = ⨁\_\{m ≥ m'} (A[1/f])\_m at m' = i, is m ≥ i, and that is the range stated here”.

> **`π_* 𝒪_L(i) ≅ ∐_{m ≥ i} 𝒪_P(m)`**, for every integer `i`, as sheaves of `𝒪_P`-modules, for
> the cone `π : L = Proj B ⟶ P = Proj A` of the truncation algebra `B = ⨁_{d ≥ 0} A_{≥ d}`.

```lean
def twistPushforwardCoproductIso (i : ℤ) :
    (Scheme.Modules.pushforward (pi 𝒜)).obj (twistingSheaf (grading 𝒜) i) ≅
      ∐ fun m : {m : ℤ // i ≤ m} => twistingSheaf 𝒜 m.1
```

**`Stacks.Truncation.twistPieceSumEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforwardAlgebra.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforwardAlgebra.lean#L221). The attribute's comment: “the equality of homogeneous parts (B[1/g])\_\{i} = ⨁\_\{m ≥ i} (A[1/f])\_m, g = ψ(f), as an additive equivalence onto the degree-i part”.

> **`⨁_{m ≥ i} (A[1/f])_m ≃+ (B[1/ψ f])_i`** (Stacks, Section 0EKF), with the homogeneous parts
> written as `Stacks.ProjectiveCohomology.awayGrading`.

```lean
def twistPieceSumEquiv (hf : f ∈ 𝒜 d) (hd : 0 < d) (i : ℤ) :
    (DirectSum {m : ℤ // i ≤ m} fun m => Stacks.ProjectiveCohomology.awayGrading 𝒜 hf m.1) ≃+
      Stacks.ProjectiveCohomology.awayGrading (grading 𝒜) ((psi 𝒜).map_mem hf) i
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTwistPushforward.twistPushforwardApp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforwardLocal.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforwardLocal.lean#L163). The attribute's comment: “the inclusion O\_P(m) to pi\_* O\_L(i), m ≥ i, over one standard open D+(f), as a map of modules over the sections of O\_P there”.

> The local inclusion `Γ(D₊(f), 𝒪_P(m)) ⟶ Γ(D₊(f), π_* 𝒪_L(i))`, for `m ≥ i`, as a morphism of
> modules over the sections of `𝒪_P` on `D₊(f)`: `twistLift` followed by the transport along
> `π⁻¹(D₊(f)) = D₊(ψ f)`.

```lean
def twistPushforwardApp (i m : ℤ) (him : i ≤ m) (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    (twistingSheaf 𝒜 m).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f)) ⟶
      (twistPushforward 𝒜 i).val.obj (op (AlgebraicGeometry.Proj.basicOpen 𝒜 f))
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTwistPushforward.twistPushforwardApp_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforwardLocal.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTwistPushforwardLocal.lean#L266). The attribute's comment: “the inclusion O\_P(m) to pi\_* O\_L(i) over standard opens is compatible with restriction between two standard opens”.

> **The local inclusion commutes with restriction to a smaller standard open.**

```lean
theorem twistPushforwardApp_restrict (i m : ℤ) (him : i ≤ m) {d e : ℕ} (hf : f ∈ 𝒜 d)
    (hd : 0 < d) (hg : g ∈ 𝒜 e) (he : 0 < e)
    (hfg : ProjectiveSpectrum.basicOpen 𝒜 g ≤ ProjectiveSpectrum.basicOpen 𝒜 f)
    (s : (twistingSheaf 𝒜 m).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    (twistPushforwardApp 𝒜 i m him e hg he).hom
        ((twistingSheaf 𝒜 m).val.map (homOfLE hfg).op s) =
      (twistPushforward 𝒜 i).val.map (homOfLE hfg).op
        ((twistPushforwardApp 𝒜 i m him d hf hd).hom s)
```

**`Stacks.Truncation.span_range_eq_irrelevant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/TruncationDegreeOne.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/TruncationDegreeOne.lean#L63). The attribute's comment: “A₊ = (f₁, …, f\_r) when A is generated over A₀ by f₁, …, f\_r ∈ A₁”.

> **`A_+ = (f_1, …, f_r)`** when `A` is generated over `A_0` by `f_1, …, f_r ∈ A_1`.

```lean
theorem span_range_eq_irrelevant (hf : ∀ i, f i ∈ 𝒜 1)
    (hgen : Algebra.adjoin (𝒜 0) (Set.range f) = ⊤) :
    Ideal.span (Set.range f) = (HomogeneousIdeal.irrelevant 𝒜).toIdeal
```

**`Stacks.Truncation.span_range_pow_eq_truncationIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/TruncationDegreeOne.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/TruncationDegreeOne.lean#L99). The attribute's comment: “(f₁, …, f\_r)^m = A\_\{≥ m} for all m ≥ 0 when A is generated over A₀ by f₁, …, f\_r ∈ A₁”.

> **`(f_1, …, f_r)^m = A_{≥ m}` for all `m ≥ 0`**, when `A` is generated over `A_0` by
> `f_1, …, f_r ∈ A_1`.

```lean
theorem span_range_pow_eq_truncationIdeal (hf : ∀ i, f i ∈ 𝒜 1)
    (hgen : Algebra.adjoin (𝒜 0) (Set.range f) = ⊤) (m : ℕ) :
    Ideal.span (Set.range f) ^ m = truncationIdeal 𝒜 m
```

**`Stacks.Truncation.truncationRingEquivReesAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/TruncationDegreeOne.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/TruncationDegreeOne.lean#L264). The attribute's comment: “B = ⨁\_\{d ≥ 0} A\_\{≥ d} is the Rees algebra of A₊ = (f₁, …, f\_r) when A is generated over A₀ by f₁, …, f\_r ∈ A₁”.

> **`B` is the Rees algebra of `A_+`**: when `A` is generated over `A_0` by
> `f_1, …, f_r ∈ A_1`, the map `a⁽ᵈ⁾ ↦ a tᵈ` is a ring isomorphism
> `B = ⨁_{d ≥ 0} A_{≥ d} ≃ A[A_+ t]`. It preserves degrees by
> `Stacks.Truncation.truncationRingEquivReesAlgebra_mem_iff`.

```lean
def truncationRingEquivReesAlgebra :
    TruncationRing 𝒜 ≃+* reesAlgebra (HomogeneousIdeal.irrelevant 𝒜).toIdeal
```

**`Stacks.Truncation.truncationRingEquivReesAlgebra_mem_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/TruncationDegreeOne.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/TruncationDegreeOne.lean#L276). The attribute's comment: “the isomorphism of B with the Rees algebra of A₊ respects the gradings”.

> **The isomorphism `B ≃ A[A_+ t]` is graded**: it carries `B_d` onto the degree-`d` part of
> the Rees algebra.

```lean
theorem truncationRingEquivReesAlgebra_mem_iff {d : ℕ} {x : TruncationRing 𝒜} :
    truncationRingEquivReesAlgebra hf hgen x ∈
        Stacks.Blowup.reesGrading (HomogeneousIdeal.irrelevant 𝒜).toIdeal d ↔
      x ∈ grading 𝒜 d
```

**`Stacks.Truncation.map_locPiece_eq_iSup_awayPieceInt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationShift.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationShift.lean#L145). The attribute's comment: “the equality of homogeneous parts (B[1/g])\_\{m'} = ⨁\_\{m ≥ m'} (A[1/f])\_m, g = ψ(f), for every m'”.

> **`(B[1/g])_{m'} = ⨁_{m ≥ m'} (A[1/f])_m`** (Stacks, Section 0EKF), for `f ∈ A_d`, `d > 0`,
> `g = ψ(f)` and any integer `m'`: the map `B[1/g] → A[1/f]`, injective on `(B[1/g])_{m'}` by
> `locToLocalization_injOn_locPiece`, carries `(B[1/g])_{m'}` onto the sum of the homogeneous parts
> `(A[1/f])_m` with `m ≥ m'`.

```lean
theorem map_locPiece_eq_iSup_awayPieceInt (hf : f ∈ 𝒜 d) (hd : 0 < d) (m' : ℤ) :
    (locPiece 𝒜 d hf hd m').map (locToLocalization 𝒜).toAddMonoidHom =
      ⨆ (m : ℤ) (_ : m' ≤ m), awayPieceInt 𝒜 d hf hd m
```

**`Stacks.Truncation.locToLocalization_comp_locRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationShift.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationShift.lean#L244). The attribute's comment: “the identification (B[1/g])\_\{m'} = ⨁\_\{m ≥ m'} (A[1/f])\_m is compatible with further localization: the comparison maps commute with D₊(f f') ⊆ D₊(f)”.

> **The maps `B[1/ψ f] → A[1/f]` commute with further localization.**

```lean
theorem locToLocalization_comp_locRestrict :
    (locToLocalization 𝒜 (f := f * f')).comp (locRestrict 𝒜 f f') =
      (awayRestrict f f').comp (locToLocalization 𝒜 (f := f))
```

**`Stacks.Truncation.map_locPiece_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationShift.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationShift.lean#L292). The attribute's comment: “the localization B[1/ψ f] → B[1/ψ(f f')] preserves the homogeneous parts (B[1/g])\_\{m'}”.

> **`B[1/ψ f] → B[1/ψ(f f')]` carries `(B[1/ψ f])_{m'}` into `(B[1/ψ(f f')])_{m'}`.**

```lean
theorem map_locPiece_le (hf : f ∈ 𝒜 d) (hf' : f' ∈ 𝒜 d') (hd : 0 < d) (m : ℤ) :
    (locPiece 𝒜 d hf hd m).map (locRestrict 𝒜 f f').toAddMonoidHom ≤
      locPiece 𝒜 (d + d') (SetLike.mul_mem_graded hf hf') (by omega) m
```

**`Stacks.Truncation.map_awayPieceInt_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationShift.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationShift.lean#L303). The attribute's comment: “the localization A[1/f] → A[1/(f f')] preserves the homogeneous parts (A[1/f])\_m”.

> **`A[1/f] → A[1/(f f')]` carries `(A[1/f])_m` into `(A[1/(f f')])_m`.**

```lean
theorem map_awayPieceInt_le (hf : f ∈ 𝒜 d) (hf' : f' ∈ 𝒜 d') (hd : 0 < d) (m : ℤ) :
    (awayPieceInt 𝒜 d hf hd m).map (awayRestrict f f').toAddMonoidHom ≤
      awayPieceInt 𝒜 (d + d') (SetLike.mul_mem_graded hf hf') (by omega) m
```

## Tag 0EKG, an equation

[Tag 0EKG](https://stacks.math.columbia.edu/tag/0EKG) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjAndSpec.zToX`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L137). The attribute's comment: “the morphism Z → X”.

> The closed immersion `Z = Spec A₀ ⟶ X = Spec A` induced by the projection `A → A₀`.

```lean
def zToX : Spec (CommRingCat.of (𝒜 0)) ⟶ Spec (CommRingCat.of A)
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.xToZ`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L142). The attribute's comment: “the morphism X → Z”.

> The morphism `X = Spec A ⟶ Z = Spec A₀` induced by the inclusion `A₀ → A`.

```lean
def xToZ : Spec (CommRingCat.of A) ⟶ Spec (CommRingCat.of (𝒜 0))
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.openU`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L154). The attribute's comment: “the open U ⊆ X”.

> The open `U = X ∖ V(A₊)` of `X = Spec A`: the union of the standard opens `D(f)` of the
> homogeneous elements `f` of positive degree.

```lean
def openU : (Spec (CommRingCat.of A)).Opens
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.projMapDomain_tau_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L288). The attribute's comment: “τ defines a morphism on all of Proj(A)”.

> `τ` induces a morphism on all of `P = Proj 𝒜`.

```lean
theorem projMapDomain_tau_eq_top : mapDomain ℬ 𝒜 c.tau = ⊤
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.projMapDomain_psi_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L294). The attribute's comment: “ψ defines a morphism on all of Proj(B)”.

> `ψ` induces a morphism on all of `L = Proj ℬ`: the power condition is exactly the radical
> inclusion of irrelevant ideals that makes the standard opens `D₊(ψ f)` cover `Proj ℬ`.

```lean
theorem projMapDomain_psi_eq_top : mapDomain 𝒜 ℬ c.psi = ⊤
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.pi`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L311). The attribute's comment: “the cone projection π : L → P”.

> The cone projection `π : L = Proj ℬ ⟶ P = Proj 𝒜`, induced by `ψ`.

```lean
def pi : AlgebraicGeometry.Proj ℬ ⟶ AlgebraicGeometry.Proj 𝒜
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.zeroSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L316). The attribute's comment: “the zero section 0 : P → L”.

> The zero section `0 : P = Proj 𝒜 ⟶ L = Proj ℬ`, induced by `τ`.

```lean
def zeroSection : AlgebraicGeometry.Proj 𝒜 ⟶ AlgebraicGeometry.Proj ℬ
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.toSpecA`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L327). The attribute's comment: “the structure morphism L → X”.

> The structure morphism `L = Proj ℬ ⟶ X = Spec A`, using the identification `σ` of `A` with
> the degree-zero part of `B`.

```lean
def toSpecA : AlgebraicGeometry.Proj ℬ ⟶ Spec (CommRingCat.of A)
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.openUInL`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L332). The attribute's comment: “the open U ⊆ L”.

> The inverse image in `L` of the open `U = X ∖ V(A₊)`.

```lean
def openUInL : (AlgebraicGeometry.Proj ℬ).Opens
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.pi_preimage_basicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L362). The attribute's comment: “π⁻¹ of a standard open”.

> **The inverse image under `π` of a standard open** of `P` is the standard open of the image
> element: `π⁻¹(D₊(f)) = D₊(ψ f)`.

```lean
theorem pi_preimage_basicOpen (f : A) (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    pi c ⁻¹ᵁ Proj.basicOpen 𝒜 f = Proj.basicOpen ℬ (c.psi f)
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.isAffineHom_pi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 384](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L384). The attribute's comment: “π is affine”.

> **The cone projection is affine.** The standard opens of positive-degree homogeneous elements
> cover `P` and are affine, and their inverse images are again standard opens of positive-degree
> homogeneous elements.

```lean
theorem isAffineHom_pi : IsAffineHom (pi c)
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.zeroSection_comp_pi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 393](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L393). The attribute's comment: “π ∘ 0 = id\_P”.

> **`π ∘ 0 = id_P`**: the zero section is a section of the cone projection.

```lean
theorem zeroSection_comp_pi : zeroSection c ≫ pi c = 𝟙 (AlgebraicGeometry.Proj 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.isClosedImmersion_zeroSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L403). The attribute's comment: “0 : P → L is a closed immersion”.

> **The zero section is a closed immersion**, `τ` being surjective in every degree.

```lean
theorem isClosedImmersion_zeroSection : IsClosedImmersion (zeroSection c)
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.range_zeroSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 470](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L470). The attribute's comment: “the image of the zero section is the inverse image of Z”.

> **The zero section maps onto the inverse image of `Z`.** Set theoretically the image of
> `0 : P → L` is the complement of the part of `L` lying over `U = X ∖ V(A₊)`. A point of the image
> contains `σ (A₊)` because `τ ∘ σ` kills the positive degrees; conversely a homogeneous prime of
> `B` containing `σ (A₊)` is the image of its own contraction along `ψ`, which is relevant because
> `ψ` is everywhere defined.

```lean
theorem range_zeroSection :
    Set.range (zeroSection c) = ((openUInL c : Set (AlgebraicGeometry.Proj ℬ)))ᶜ
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.isAffineHom_pi_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 519](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L519). The attribute's comment: “U → P is affine”.

> **The punctured cone is affine over `P`.** Over the standard open `D₊(f)` the part of `L`
> lying over `U` is the standard open `D₊(σ f · ψ f)` of a positive-degree homogeneous element,
> hence affine.

```lean
theorem isAffineHom_pi_restrict : IsAffineHom ((openUInL c).ι ≫ pi c)
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.pi_comp_toSpecZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 546](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L546). The attribute's comment: “the square L → P, X → Z commutes”.

> **The right square commutes**: `L → P → Z` equals `L → X → Z`.

```lean
theorem pi_comp_toSpecZero :
    pi c ≫ Proj.toSpecZero 𝒜 = toSpecA c ≫ xToZ 𝒜
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.zeroSection_comp_toSpecA`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean, line 553](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpec.lean#L553). The attribute's comment: “the square P → L, Z → X commutes”.

> **The left square commutes**: `P → L → X` equals `P → Z → X`.

```lean
theorem zeroSection_comp_toSpecA :
    zeroSection c ≫ toSpecA c = Proj.toSpecZero 𝒜 ≫ zToX 𝒜
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.truncationCone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecDiagram.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecDiagram.lean#L320). The attribute's comment: “π : L → P is a cone over P, whose direct-image algebra is graded by the twists O\_P(m), m ≥ 0”.

> **`π : L ⟶ P` is a cone over `P`** in the sense of [Stacks, Tag 062R], graded by the algebra
> `⨁_{m ≥ 0} 𝒪_P(m)` of nonnegative twists: `π` is affine, the homogeneous pieces include in
> `π_* 𝒪_L` by the degreewise inclusions `𝒪_P(m) ⟶ π_* 𝒪_L`, every function on the cone is locally
> a unique finite sum of homogeneous ones, the inclusions are multiplicative, the negative pieces
> vanish and the degree-zero piece is `𝒪_P`, included by the structure map.

```lean
def truncationCone : AbstractCone (AlgebraicGeometry.Proj 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.range_zeroSection_eq_preimage_range_zToX`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecDiagram.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecDiagram.lean#L343). The attribute's comment: “the zero section maps set theoretically onto the inverse image of Z in L”.

> **The zero section `0 : P ⟶ L` maps set theoretically onto the inverse image of `Z` in `L`**:
> its image is the inverse image under `σ : L ⟶ X` of the image of `Z = Spec A₀ ⟶ X`.

```lean
theorem range_zeroSection_eq_preimage_range_zToX :
    Set.range (zeroSection 𝒜) = toSpecA 𝒜 ⁻¹' Set.range (ProjAndSpec.zToX 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.zeroSection_appLE_coneIota_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecDiagram.lean, line 442](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecDiagram.lean#L442). The attribute's comment: “the zero section 0 : P → L is the vertex of the cone π”.

> **The zero section `0 : P ⟶ L` is the vertex of the cone `π : L ⟶ P`**: it is a section of
> `π`, and pulling functions back along it kills every homogeneous piece `𝒪_P(m)`, `m > 0`, of
> `π_* 𝒪_L = ⨁_{m ≥ 0} 𝒪_P(m)`, over every open of `P`. So `0` is the closed immersion cut out by the
> positive part of the grading, `Spec_P(𝒪_P) ⟶ Spec_P(⨁_{m ≥ 0} 𝒪_P(m))`.

```lean
theorem zeroSection_appLE_coneIota_eq_zero (m : ℤ) (hm : 0 < m)
    (U : Opens (ProjectiveSpectrum.top 𝒜)) (s : (nonnegTwistingSheaf 𝒜 m).val.obj (op U)) :
    (zeroSection 𝒜).appLE (pi 𝒜 ⁻¹ᵁ U) U (le_zeroSection_preimage_pi_preimage 𝒜 U)
      ((coneIota 𝒜 m).val.app (op U) s) = 0
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.projAndSpec_diagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecDiagram.lean, line 497](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecDiagram.lean#L497). The attribute's comment: “the commutative diagram Spec\_P(⨁\_\{m ∈ ℤ} O\_P(m)) → L = Spec\_P(⨁\_\{m ≥ 0} O\_P(m)) → P over U → X → Z, with π a cone whose zero section maps set theoretically onto the inverse image of Z in L”. References: EGA II (8.6.3), “special case”.

> **The diagram of [Stacks, Tag 0EKG].** Let `A` be a graded ring, `X = Spec A`,
> `Z = V(A₊) = Spec A₀`, `U = X ∖ Z`, `P = Proj A`, and let `L = Proj B` for
> `B = ⨁_{d ≥ 0} A_{≥ d}`, with cone projection `π : L ⟶ P`, structure morphism `σ : L ⟶ X` and zero
> section `0 : P ⟶ L`. Then, writing `j : Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) ⟶ L` for the top-left arrow and
> `e : Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) ≅ U` for the left identification:
>
> * `π` is a cone over `P` (`truncationCone`, graded by `⨁_{m ≥ 0} 𝒪_P(m)`, whose pieces are the
>   twisting sheaves `𝒪_P(m)`, `m ≥ 0`), and `L = Spec_P(⨁_{m ≥ 0} 𝒪_P(m))` over `P`;
> * `j` lies over `P`, it is an open immersion, and its image is the part of `L` over `U`;
> * `e` is an identification over `P`;
> * the left square `j ≫ σ = e ≫ (U ⟶ X)` and the right square `π ≫ (P ⟶ Z) = σ ≫ (X ⟶ Z)`
>   commute;
> * the zero section is a section of `π`, it is the vertex of the cone (pulling back along it kills
>   the pieces `𝒪_P(m)`, `m > 0`, of `π_* 𝒪_L`), and it maps set theoretically onto the inverse image
>   of `Z` in `L`.

```lean
theorem projAndSpec_diagram :
    -- `π` is a cone over `P`, graded by the nonnegative twists
    (truncationCone 𝒜).π = pi 𝒜 ∧
    (truncationCone 𝒜).grading = nonnegTwistAlgebra 𝒜 ∧
    (truncationCone 𝒜).ι = coneIota 𝒜 ∧
    (∀ m : ℕ, (truncationCone 𝒜).grading.piece m = twistingSheaf 𝒜 m) ∧
    (∀ m : ℤ, (integerTwistAlgebra 𝒜).piece m = twistingSheaf 𝒜 m) ∧
    -- `L = Spec_P(⨁_{m ≥ 0} 𝒪_P(m))` over `P`
    (coneProjIsoRelativeSpecTwistAlgebra 𝒜).hom ≫
        relativeSpecToBase (nonnegTwistAlgebraSheaf 𝒜) = pi 𝒜 ∧
    -- the top-left arrow lies over `P`, is an open immersion, with image the part of `L` over `U`
    puncturedToConeProj 𝒜 ≫ pi 𝒜 = relativeSpecToBase (integerTwistAlgebraSheaf 𝒜) ∧
    IsOpenImmersion (puncturedToConeProj 𝒜) ∧
    (puncturedToConeProj 𝒜).opensRange = openUInL 𝒜 ∧
    -- the left identification `Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) = U` lies over `P`
    (puncturedConeRelativeSpecTwistAlgebraIsoOpenU 𝒜).hom ≫ openUToProj 𝒜 =
      relativeSpecToBase (integerTwistAlgebraSheaf 𝒜) ∧
    -- the left square
    puncturedToConeProj 𝒜 ≫ toSpecA 𝒜 =
      (puncturedConeRelativeSpecTwistAlgebraIsoOpenU 𝒜).hom ≫ (ProjAndSpec.openU 𝒜).ι ∧
    -- the right square
    pi 𝒜 ≫ Proj.toSpecZero 𝒜 = toSpecA 𝒜 ≫ ProjAndSpec.xToZ 𝒜 ∧
    -- the zero section
    zeroSection 𝒜 ≫ pi 𝒜 = 𝟙 (AlgebraicGeometry.Proj 𝒜) ∧
    (∀ (m : ℤ), 0 < m → ∀ (U : Opens (ProjectiveSpectrum.top 𝒜))
        (s : (nonnegTwistingSheaf 𝒜 m).val.obj (op U)),
      (zeroSection 𝒜).appLE (pi 𝒜 ⁻¹ᵁ U) U (le_zeroSection_preimage_pi_preimage 𝒜 U)
        ((coneIota 𝒜 m).val.app (op U) s) = 0) ∧
    Set.range (zeroSection 𝒜) = toSpecA 𝒜 ⁻¹' Set.range (ProjAndSpec.zToX 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTruncation.isIso_toSpecA_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecIsoOverU.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecIsoOverU.lean#L235). The attribute's comment: “L → X is an isomorphism over U”.

> **The structure morphism `L ⟶ X` is an isomorphism over `U = X ∖ V(A₊)`.** This is the
> equality on the left of the diagram of [Stacks, Tag 0EKG]: being an isomorphism over an open is
> local on that open, and over each standard open of a positive-degree homogeneous element the
> morphism is an isomorphism.

```lean
theorem isIso_toSpecA_restrict : IsIso (toSpecA 𝒜 ∣_ ProjAndSpec.openU 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTruncation.openUInL_ι_comp_toSpecA`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecIsoOverU.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecIsoOverU.lean#L264). The attribute's comment: “the part of L over U is U, over X”.

> **The punctured cone is the open `U`, over `X`**: the part of `L` lying over `U` maps to `X`
> through the isomorphism of `Stacks.AlgebraicGeometry.ProjAndSpecTruncation.isIso_toSpecA_restrict`
> followed by the inclusion of `U`.

```lean
theorem openUInL_ι_comp_toSpecA :
    (openUInL 𝒜).ι ≫ toSpecA 𝒜 =
      (toSpecA 𝒜 ∣_ ProjAndSpec.openU 𝒜) ≫ (ProjAndSpec.openU 𝒜).ι
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTruncation.truncationConeData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean#L366). The attribute's comment: “the truncation algebra B = ⨁\_\{d ≥ 0} A\_\{≥ d} is cone data over A”.

> The truncation algebra `B = ⨁_{d ≥ 0} A_{≥ d}` is cone data over `A`: the maps `ψ`,
> `τ` and `σ` satisfy `τ ∘ ψ = id`, the two formulas tying `σ` to `ψ` and `τ`, and the three
> divisibility conditions.

```lean
def truncationConeData : ProjAndSpec.ConeData 𝒜 (grading 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTruncation.openUInL_eq_iSup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean, line 429](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean#L429). The attribute's comment: “U ⊆ L is a union of standard opens, for the truncation algebra”.

> The part of `L` lying over `U` is the union of the standard opens of the
> `σ`-images of the positive-degree homogeneous elements of `A`.

```lean
theorem openUInL_eq_iSup :
    openUInL 𝒜 = ⨆ (d : ℕ) (_ : 0 < d) (f : 𝒜 d),
      Proj.basicOpen (grading 𝒜) ((sigma 𝒜 (f : A) : grading 𝒜 0) : TruncationRing 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTruncation.openUInL_inf_basicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean, line 444](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean#L444). The attribute's comment: “U ⊆ L over a standard open, for the truncation algebra”.

> Over a standard open `D₊(f)` of `P` the part of `L` lying over `U` is the standard open
> of `σ f · ψ f`.

```lean
theorem openUInL_inf_basicOpen (f : A) (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    openUInL 𝒜 ⊓ Proj.basicOpen (grading 𝒜) (psi 𝒜 f) =
      Proj.basicOpen (grading 𝒜)
        (((sigma 𝒜 f : grading 𝒜 0) : TruncationRing 𝒜) * psi 𝒜 f)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTruncation.toSpecA_preimage_specBasicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean, line 506](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean#L506). The attribute's comment: “the inverse image in L of a standard open of X”.

> The inverse image in `L` of a standard open of `X` is the standard open of
> `σ f · ψ f`, a homogeneous element of positive degree, for `f` homogeneous of positive
> degree.

```lean
theorem toSpecA_preimage_specBasicOpen (f : A) (d : ℕ) (hf : f ∈ 𝒜 d) :
    toSpecA 𝒜 ⁻¹ᵁ ProjAndSpec.specBasicOpen f =
      Proj.basicOpen (grading 𝒜)
        (((sigma 𝒜 f : grading 𝒜 0) : TruncationRing 𝒜) * psi 𝒜 f)
```

**`Stacks.AlgebraicGeometry.ProjAndSpecTruncation.isAffineOpen_toSpecA_preimage_specBasicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean, line 517](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecTruncation.lean#L517). The attribute's comment: “the part of L over a standard open of X is affine”.

> The part of `L` lying over a standard open of `X` is affine, for `f` homogeneous of
> positive degree.

```lean
theorem isAffineOpen_toSpecA_preimage_specBasicOpen (f : A) (d : ℕ) (hf : f ∈ 𝒜 d)
    (hd : 0 < d) : IsAffineOpen (toSpecA 𝒜 ⁻¹ᵁ ProjAndSpec.specBasicOpen f)
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.awayι_comp_pi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeChart.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeChart.lean#L68). The attribute's comment: “the cone projection on an affine chart is Spec of the map of degree-zero localizations”.

> **On the affine chart `Spec B_{(ψ f)}` of `L` the cone projection is `Spec` of the map
> `A_{(f)} ⟶ B_{(ψ f)}` of degree-zero localizations.** The chart of `L` is carried by the
> inclusion of `D₊(ψ f)`, on which the cone projection is the local morphism attached to `f`, and
> that local morphism is by construction the one of the degree-zero localizations.

```lean
theorem awayι_comp_pi :
    Proj.awayι ℬ (c.psi f) (c.psi.map_mem hf) hd ≫ pi c =
      Spec.map (CommRingCat.ofHom (Away.map c.psi f)) ≫ Proj.awayι 𝒜 f hf hd
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.awayToSection_comp_pi_appLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeChart.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeChart.lean#L159). The attribute's comment: “the cone projection on functions over a standard open is the map of degree-zero localizations”.

> **The cone projection acts on functions over a standard open by the map of degree-zero
> localizations.** Through the identifications `A_{(f)} = Γ(P, D₊(f))` and
> `B_{(ψ f)} = Γ(L, D₊(ψ f))` of [Stacks, Tag 01M6], the pullback of functions along `π` is
> `HomogeneousLocalization.Away.map ψ f`. This is the module-theoretic content of the chart
> description `Stacks.AlgebraicGeometry.ProjAndSpec.awayι_comp_pi`: it says which
> `A_{(f)}`-algebra the functions on the part of `L` over `D₊(f)` form.

```lean
theorem awayToSection_comp_pi_appLE :
    Proj.awayToSection 𝒜 f ≫ (pi c).appLE (Proj.basicOpen 𝒜 f)
        (Proj.basicOpen ℬ (c.psi f)) (pi_preimage_basicOpen c f d hf hd).ge =
      CommRingCat.ofHom (Away.map c.psi f) ≫ Proj.awayToSection ℬ (c.psi f)
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.awayToSection_comp_pi_appLE_sigmaMulPsi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeChartPunctured.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeChartPunctured.lean#L105). The attribute's comment: “the punctured cone projection on functions over a standard open is the map of degree-zero localizations A\_(f) to B\_(sigma f * psi f)”.

> **On the chart `D₊(σ f · ψ f)` of the punctured cone the projection acts on functions by the
> map `A_{(f)} ⟶ B_{(σ f · ψ f)}` of degree-zero localizations.** Through the identifications
> `A_{(f)} = Γ(P, D₊(f))` and `B_{(σ f · ψ f)} = Γ(L, D₊(σ f · ψ f))` of [Stacks, Tag 01M6], the
> pullback of functions along `π` to the part of `U` over `D₊(f)` is `puncturedAwayMap`.

```lean
theorem awayToSection_comp_pi_appLE_sigmaMulPsi (hd : 0 < d) (hf : f ∈ 𝒜 d) :
    Proj.awayToSection 𝒜 f ≫ (pi c).appLE (Proj.basicOpen 𝒜 f)
        (Proj.basicOpen ℬ ((c.sigma f : B) * c.psi f))
        (basicOpen_sigmaMulPsi_le_pi_preimage c hd hf) =
      CommRingCat.ofHom (puncturedAwayMap c hd hf) ≫
        Proj.awayToSection ℬ ((c.sigma f : B) * c.psi f)
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.awayToSection_comp_puncturedPi_appLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeChartPunctured.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeChartPunctured.lean#L137). The attribute's comment: “the restricted projection pi|\_U on functions over a standard open, on the chart given by the inverse image of D+(sigma f * psi f)”.

> **The same statement for the restricted projection `π|_U : U ⟶ P`**, whose chart over
> `D₊(f)` is the inverse image of `D₊(σ f · ψ f)` under the open immersion of `U`: there too the
> pullback of functions is `puncturedAwayMap`, followed by restriction along that open
> immersion.

```lean
theorem awayToSection_comp_puncturedPi_appLE (hd : 0 < d) (hf : f ∈ 𝒜 d) :
    Proj.awayToSection 𝒜 f ≫ ((openUInL c).ι ≫ pi c).appLE (Proj.basicOpen 𝒜 f)
        ((openUInL c).ι ⁻¹ᵁ Proj.basicOpen ℬ ((c.sigma f : B) * c.psi f))
        (((TopologicalSpace.Opens.map (openUInL c).ι.base).map
          (homOfLE (basicOpen_sigmaMulPsi_le_pi_preimage c hd hf))).le) =
      CommRingCat.ofHom (puncturedAwayMap c hd hf) ≫
        Proj.awayToSection ℬ ((c.sigma f : B) * c.psi f) ≫
          (openUInL c).ι.appLE (Proj.basicOpen ℬ ((c.sigma f : B) * c.psi f))
            ((openUInL c).ι ⁻¹ᵁ Proj.basicOpen ℬ ((c.sigma f : B) * c.psi f)) le_rfl
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneRelativeSpecIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeRelativeSpec.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeRelativeSpec.lean#L115). The attribute's comment: “L is, over P, the relative spectrum of the direct-image algebra of the cone”.

> **`L = Spec_P(π_* 𝒪_L)`**: the cone is, over `P = Proj A`, the relative spectrum of its
> direct-image algebra, the cone projection being affine.

```lean
def coneRelativeSpecIso :
    Over.mk (ProjAndSpec.pi c) ≅
      Over.mk (relativeSpecToBase (pushforwardAlgebra (ProjAndSpec.pi c)))
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeRelativeSpecIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeRelativeSpec.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeRelativeSpec.lean#L123). The attribute's comment: “the punctured cone is, over P, the relative spectrum of its direct-image algebra”.

> **`U = Spec_P((π|_U)_* 𝒪_U)`**: the punctured cone is, over `P = Proj A`, the relative
> spectrum of its direct-image algebra, the restricted cone projection being affine.

```lean
def puncturedConeRelativeSpecIso :
    Over.mk ((ProjAndSpec.openUInL c).ι ≫ ProjAndSpec.pi c) ≅
      Over.mk (relativeSpecToBase
        (pushforwardAlgebra ((ProjAndSpec.openUInL c).ι ≫ ProjAndSpec.pi c)))
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeRelativeSpecIsoOpenU`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeRelativeSpec.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeRelativeSpec.lean#L201). The attribute's comment: “the relative spectrum of the punctured cone's direct-image algebra is U”. References: EGA II (8.12.5), “special case”; EGA II (8.6.2), “special case”.

> **The relative spectrum over `P` of the direct-image algebra of the punctured cone is the
> open `U = X ∖ V(A₊)` of `X`**, for the truncation algebra. This is the equality on the left of the
> diagram of [Stacks, Tag 0EKG]: the punctured cone is that relative spectrum, and `L ⟶ X` carries
> it isomorphically onto `U`.

```lean
def puncturedConeRelativeSpecIsoOpenU :
    Stacks.AffineAlgebraEquivalence.relativeSpec
        (pushforwardAlgebra ((openUInL 𝒜).ι ≫ pi 𝒜)) ≅
      (ProjAndSpec.openU 𝒜).toScheme
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeRelativeSpecTwistAlgebraIsoOpenU`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeRelativeSpec.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeRelativeSpec.lean#L248). The attribute's comment: “the left equality: U is Spec\_P of the integer twist algebra”. References: EGA II (8.12.5), “special case”; EGA II (8.6.2), “special case”.

> **`Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) = U`**: the relative spectrum over `P = Proj A` of the algebra of
> all integral twists is the open `U = X ∖ V(A₊)` of `X = Spec A`. This is the equality on the left
> of the diagram of [Stacks, Tag 0EKG], with the algebra named as the twist algebra
> `⨁_{m ∈ ℤ} 𝒪_P(m)` itself rather than as the direct image `(π|_U)_* 𝒪_U` it was computed from: the
> punctured cone is that relative spectrum by
> `Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeRelativeSpecTwistAlgebraIso`, and `L ⟶ X`
> carries the punctured cone isomorphically onto `U` by
> `Stacks.AlgebraicGeometry.ProjAndSpecTruncation.isIso_toSpecA_restrict`.

```lean
def puncturedConeRelativeSpecTwistAlgebraIsoOpenU :
    Stacks.AffineAlgebraEquivalence.relativeSpec (integerTwistAlgebraSheaf 𝒜) ≅
      (ProjAndSpec.openU 𝒜).toScheme
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.degreeZeroRingMap_coneTwistAwayHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraInclusion.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraInclusion.lean#L97). The attribute's comment: “the degreewise inclusion of the sections of O\_P(m) into the degree-zero localization of the truncation algebra at psi f, followed by restriction to the chart of the punctured cone, is the punctured degreewise inclusion, for a nonnegative degree m”.

> **The degreewise inclusion of `Γ(D₊(f), 𝒪_P(m))` into the functions on the cone chart,
> followed by restriction to the chart of the punctured cone, is the degreewise inclusion into the
> functions on that chart**, for `m ≥ 0`. Both sides are elements of `(B[1/σ f · ψ f])₀`, and the
> comparison map to `A[1/f]` is injective and sends both to the standard-open description of the
> section one starts from.

```lean
theorem degreeZeroRingMap_coneTwistAwayHom (m : ℕ) {d : ℕ} (hf : f ∈ 𝒜 d) (hd : 0 < d)
    (s : (twistingSheaf 𝒜 (m : ℤ)).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    ProjectiveSpectrum.degreeZeroRingMap (grading 𝒜) (psi 𝒜 f) (sigmaMulPsi 𝒜 f)
        ⟨d, hd, GradedRingHom.map_mem (psi 𝒜) hf⟩ ⟨d, hd, sigmaMulPsi_mem_grading 𝒜 d hf⟩
        (basicOpen_sigmaMulPsi_le_psi 𝒜) (coneTwistAwayHom 𝒜 m d hf hd s) =
      puncturedConeTwistAwayHom 𝒜 (m : ℤ) d hf hd s
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.appLE_coneTwistApp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraInclusion.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraInclusion.lean#L117). The attribute's comment: “the local degreewise inclusion O\_P(m) to pi\_* O\_L over a standard open, followed by restriction to the punctured cone, is the punctured local degreewise inclusion, for a nonnegative degree m”.

> **The local degreewise inclusion into `π_* 𝒪_L` over a standard open, followed by restriction
> along the open immersion of the punctured cone, is the punctured local degreewise inclusion**, for
> `m ≥ 0`. Both are read on the chart `D₊(σ f · ψ f)` of the punctured cone inside the chart
> `D₊(ψ f)` of the cone, where restriction of functions is the degree-zero restriction map of `B`
> and `Stacks.AlgebraicGeometry.ProjConeTwist.degreeZeroRingMap_coneTwistAwayHom` applies.

```lean
theorem appLE_coneTwistApp (m : ℕ) {d : ℕ} (hf : f ∈ 𝒜 d) (hd : 0 < d)
    (hle : ((openUInL 𝒜).ι ≫ pi 𝒜) ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen 𝒜 f ≤
      (openUInL 𝒜).ι ⁻¹ᵁ (pi 𝒜 ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen 𝒜 f))
    (s : (twistingSheaf 𝒜 (m : ℤ)).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    ((openUInL 𝒜).ι.appLE (pi 𝒜 ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen 𝒜 f)
          (((openUInL 𝒜).ι ≫ pi 𝒜) ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen 𝒜 f) hle).hom
        ((coneTwistApp 𝒜 m d hf hd).hom s) =
      (puncturedConeTwistApp 𝒜 (m : ℤ) d hf hd).hom s
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.appLE_coneTwistHom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraInclusion.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraInclusion.lean#L161). The attribute's comment: “the degreewise inclusion O\_P(m) to pi\_* O\_L followed by restriction to the punctured cone is the degreewise inclusion O\_P(m) to (pi|\_U)\_* O\_U, for a nonnegative degree m”.

> **The degreewise inclusion `𝒪_P(m) ⟶ π_* 𝒪_L` followed by restriction of functions from the
> cone to the punctured cone is the degreewise inclusion `𝒪_P(m) ⟶ (π|_U)_* 𝒪_U`**, for `m ≥ 0`,
> read on the sections over an arbitrary open of `P`. Both sides are morphisms out of the sheaf
> the punctured inclusion is glued from, so it is enough to compare them over the positive-degree
> standard opens, where the comparison is
> `Stacks.AlgebraicGeometry.ProjConeTwist.appLE_coneTwistApp`.

```lean
theorem appLE_coneTwistHom_app (m : ℕ) (V : Opens (ProjectiveSpectrum.top 𝒜))
    (hleV : ((openUInL 𝒜).ι ≫ pi 𝒜) ⁻¹ᵁ V ≤ (openUInL 𝒜).ι ⁻¹ᵁ (pi 𝒜 ⁻¹ᵁ V))
    (x : (twistingSheaf 𝒜 (m : ℤ)).val.obj (op V)) :
    ((openUInL 𝒜).ι.appLE (pi 𝒜 ⁻¹ᵁ V) (((openUInL 𝒜).ι ≫ pi 𝒜) ⁻¹ᵁ V) hleV).hom
        ((coneTwistHom 𝒜 m).val.app (op V) x) =
      (puncturedTwistHom 𝒜 (m : ℤ)).val.app (op V) x
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.nonnegToIntegerTwistUnitalHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraInclusion.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraInclusion.lean#L207). The attribute's comment: “the inclusion of the nonnegative twist algebra in the integral one, as a unital homomorphism of sheaves of graded algebras”.

> **The inclusion `⨁_{m ≥ 0} 𝒪_P(m) ⟶ ⨁_{m ∈ ℤ} 𝒪_P(m)` as a unital homomorphism of sheaves
> of graded algebras.** It is `Stacks.AlgebraicGeometry.ProjConeTwist.nonnegToIntegerTwistAlgebra`
> with the preservation of the degree-zero unit recorded: both unit sections are the unit section
> `Stacks.AlgebraicGeometry.ProjConeTwist.twistOne` of the untwisted sheaf, and in degree zero the
> inclusion is the identity.

```lean
def nonnegToIntegerTwistUnitalHom :
    SheafOfModules.GradedAlgebra.UnitalHom (nonnegTwistAlgebra 𝒜) (integerTwistAlgebra 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.nonnegToIntegerTwistAlgebraSheafHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraInclusion.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraInclusion.lean#L219). The attribute's comment: “the inclusion of the nonnegative twist algebra in the integral one, as a morphism of sheaves of commutative algebras over the structure sheaf of P”.

> **The inclusion of the two twist algebras as a morphism of sheaves of commutative
> `𝒪_P`-algebras**, which is the shape the relative spectrum of [Stacks, Tag 01LM] consumes. Its
> underlying morphism of sheaves of rings is the one the degreewise inclusions induce on the
> ungraded realizations.

```lean
def nonnegToIntegerTwistAlgebraSheafHom :
    nonnegTwistAlgebraSheaf 𝒜 ⟶ integerTwistAlgebraSheaf 𝒜
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.appLE_coneIota_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraInclusion.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraInclusion.lean#L235). The attribute's comment: “the inclusion of each homogeneous piece of the nonnegative twist algebra in pi\_* O\_L, followed by restriction to the punctured cone, is the degreewise inclusion in (pi|\_U)\_* O\_U after the inclusion of the two twist algebras”.

> **The degreewise inclusion of each homogeneous piece of `⨁_{m ≥ 0} 𝒪_P(m)` into `π_* 𝒪_L`,
> followed by restriction to the punctured cone, is the degreewise inclusion into
> `(π|_U)_* 𝒪_U` composed with the degreewise inclusion of the two twist algebras**: the
> nonnegative-degree case is
> `Stacks.AlgebraicGeometry.ProjConeTwist.appLE_coneTwistHom_app`, and in a negative degree the
> source sheaf is zero, so both sides vanish.

```lean
theorem appLE_coneIota_app (i : ℤ) (W : Opens (ProjectiveSpectrum.top 𝒜))
    (hleW : ((openUInL 𝒜).ι ≫ pi 𝒜) ⁻¹ᵁ W ≤ (openUInL 𝒜).ι ⁻¹ᵁ (pi 𝒜 ⁻¹ᵁ W))
    (y : (nonnegTwistingSheaf 𝒜 i).val.obj (op W)) :
    ((openUInL 𝒜).ι.appLE (pi 𝒜 ⁻¹ᵁ W) (((openUInL 𝒜).ι ≫ pi 𝒜) ⁻¹ᵁ W) hleW).hom
        ((coneIota 𝒜 i).val.app (op W) y) =
      (puncturedTwistHom 𝒜 i).val.app (op W) ((nonnegToIntegerApp 𝒜 i).val.app (op W) y)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.ungradedSheafMap_comp_puncturedConeUngradedSheafIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraInclusion.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraInclusion.lean#L292). The attribute's comment: “the inclusion of the two twist algebras is restriction of functions from the cone to the punctured cone, as morphisms of sheaves of rings”.

> **The inclusion of the two twist algebras is restriction of functions from the cone to the
> punctured cone**, as morphisms of sheaves of rings: the morphism the degreewise inclusions induce
> on the ungraded realizations, followed by the identification of `⨁_{m ∈ ℤ} 𝒪_P(m)` with
> `(π|_U)_* 𝒪_U`, is the identification of `⨁_{m ≥ 0} 𝒪_P(m)` with `π_* 𝒪_L` followed by the
> restriction map of the two direct images.

```lean
theorem ungradedSheafMap_comp_puncturedConeUngradedSheafIso :
    SheafOfModules.GradedAlgebra.ungradedSheafMap (nonnegToIntegerTwistUnitalHom 𝒜) ≫
        (puncturedConeUngradedSheafIso 𝒜).hom =
      (coneUngradedSheafIso 𝒜).hom ≫
        Stacks.RelativeSpec.AlgebraSheaf.ringSheafMap
          (coneToPuncturedConeAlgebra (truncationConeData 𝒜))
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.nonnegToIntegerTwistAlgebraSheafHom_comp_puncturedConeAlgebraSheafIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraInclusion.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraInclusion.lean#L345). The attribute's comment: “the inclusion of the two twist algebras is restriction of functions from the cone to the punctured cone, as morphisms of sheaves of commutative algebras over the structure sheaf of P”.

> **The inclusion of the two twist algebras is restriction of functions from the cone to the
> punctured cone**, as morphisms of sheaves of commutative `𝒪_P`-algebras. This is the square
> that makes the morphism of relative spectra induced by the inclusion the open immersion of the
> punctured cone, and hence the left square of the diagram of [Stacks, Tag 0EKG] commute.

```lean
theorem nonnegToIntegerTwistAlgebraSheafHom_comp_puncturedConeAlgebraSheafIso :
    nonnegToIntegerTwistAlgebraSheafHom 𝒜 ≫ (puncturedConeAlgebraSheafIso 𝒜).hom =
      (coneAlgebraSheafIso 𝒜).hom ≫ coneToPuncturedConeAlgebra (truncationConeData 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.heq_nonnegTwistMul_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraSheaf.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraSheaf.lean#L107). The attribute's comment: “the multiplication of the nonnegative twist algebra is commutative on homogeneous local sections”.

> **The multiplication of the algebra of nonnegative twists is commutative** on homogeneous
> local sections. In a negative degree both products vanish; in nonnegative degrees both are the
> pointwise product of the values in the module fibres.

```lean
theorem heq_nonnegTwistMul_comm (i j : ℤ) (U : (Opens (ProjectiveSpectrum.top 𝒜))ᵒᵖ)
    (a : (nonnegTwistingSheaf 𝒜 i).val.obj U) (b : (nonnegTwistingSheaf 𝒜 j).val.obj U) :
    HEq ((nonnegTwistMul 𝒜 i j).app U a b) ((nonnegTwistMul 𝒜 j i).app U b a)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.nonnegTwistAlgebraSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraSheaf.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraSheaf.lean#L132). The attribute's comment: “the nonnegative twist algebra as a sheaf of commutative algebras over the structure sheaf of P”.

> **The algebra of nonnegative twists `⨁_{m ≥ 0} 𝒪_P(m)` as a sheaf of commutative
> `𝒪_P`-algebras**, which is the shape the relative spectrum of [Stacks, Tag 01LM] takes as
> input. Its sheaf of rings is the ungraded realization of [Stacks, Tag 01CF] and its structure
> morphism is `r ↦ r · 1`.

```lean
def nonnegTwistAlgebraSheaf : Stacks.RelativeSpec.AlgebraSheaf (AlgebraicGeometry.Proj 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTotalMap_structureMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraSheaf.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraSheaf.lean#L145). The attribute's comment: “the degreewise inclusions carry the structure map of the ungraded realization of the nonnegative twist algebra to the pullback of functions along the cone projection”.

> **The degreewise inclusions carry the structure map `r ↦ r · 1` of the ungraded realization
> to the pullback of functions along `π`.** This is what makes the identification of `π_* 𝒪_L` with
> the twist algebra one of algebras over `𝒪_P`, and not merely of sheaves of rings: the inclusions
> are `𝒪_P`-linear and unital, and the action of a section of `𝒪_P` on a function on the cone is
> multiplication by its pullback.

```lean
theorem coneTotalMap_structureMap (U : Opens (ProjectiveSpectrum.top 𝒜))
    (r : (AlgebraicGeometry.Proj 𝒜).ringCatSheaf.obj.obj (op U)) :
    coneTotalMap 𝒜 U ((nonnegTwistPresheafAlgebra 𝒜).structureMap (op U) r) =
      ((pi 𝒜).c.app (op U)).hom r
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneAlgebraSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraSheaf.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraSheaf.lean#L174). The attribute's comment: “the identification pi\_* O\_L = the nonnegative twist algebra, as sheaves of commutative algebras over the structure sheaf of P, for the cone of the truncation algebra”.

> **`π_* 𝒪_L` is the algebra of nonnegative twists**, as sheaves of commutative
> `𝒪_P`-algebras.

```lean
def coneAlgebraSheafIso :
    nonnegTwistAlgebraSheaf 𝒜 ≅ pushforwardAlgebra (pi 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.isQuasicoherent_nonnegTwistAlgebraSheaf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraSheaf.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraSheaf.lean#L191). The attribute's comment: “the nonnegative twist algebra is a quasi-coherent sheaf of algebras over the structure sheaf of P”.

> The algebra of nonnegative twists is a quasi-coherent sheaf of `𝒪_P`-algebras: it is the
> direct image of the structure sheaf of the cone along the affine morphism `π`.

```lean
instance isQuasicoherent_nonnegTwistAlgebraSheaf :
    Stacks.RelativeSpec.AlgebraSheaf.IsQuasicoherent (nonnegTwistAlgebraSheaf 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneRelativeSpecTwistAlgebraIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraSheaf.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistAlgebraSheaf.lean#L202). The attribute's comment: “L is, over P, the relative spectrum of the nonnegative twist algebra, for the cone of the truncation algebra”. References: EGA II (8.7.3), “partial”.

> **`L = Spec_P(⨁_{m ≥ 0} 𝒪_P(m))`**: the cone is, over `P = Proj A`, the relative spectrum of
> the algebra of nonnegative twists. This is the presentation on the right of the diagram of
> [Stacks, Tag 0EKG], with the algebra named as the twist algebra rather than as the direct image
> `π_* 𝒪_L` it was computed from.

```lean
def coneRelativeSpecTwistAlgebraIso :
    Over.mk (pi 𝒜) ≅ Over.mk (relativeSpecToBase (nonnegTwistAlgebraSheaf 𝒜))
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistNatDirectSumHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistConeCoproduct.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistConeCoproduct.lean#L82). The attribute's comment: “the family of degreewise inclusions O\_P(m) -> pi\_* O\_L as one morphism out of the objectwise direct sum over the natural numbers, for the truncation cone”.

> **The degreewise inclusions `𝒪_P(m) ⟶ π_* 𝒪_L` as a single morphism out of the objectwise
> direct sum over the natural numbers.**

```lean
def coneTwistNatDirectSumHom :
    Stacks.directSum (fun n : ℕ => (twistingSheaf 𝒜 (n : ℤ)).val) ⟶
      (Stacks.Morphisms.pushforwardStructureSheaf (pi 𝒜)).val
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.bijective_coneTwistNatDirectSumHom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistConeCoproduct.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistConeCoproduct.lean#L117). The attribute's comment: “the morphism out of the objectwise direct sum over the natural numbers of the twisting sheaves is bijective on the sections over a standard open of a positive-degree homogeneous element, for the cone of the truncation algebra”.

> **Over a standard open of a positive-degree homogeneous element the comparison out of the
> direct sum over the natural numbers is bijective.**

```lean
theorem bijective_coneTwistNatDirectSumHom_app (p : PositiveElem 𝒜) :
    Function.Bijective
      ((coneTwistNatDirectSumHom 𝒜).app (op (positiveBasicOpen 𝒜 p))).hom
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistDirectSumHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistConeCoproduct.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistConeCoproduct.lean#L141). The attribute's comment: “the inclusions of the homogeneous pieces of the nonnegative twist algebra as one morphism out of the objectwise direct sum over all integers, for the truncation cone”.

> **The homogeneous pieces of the algebra of nonnegative twists, included in `π_* 𝒪_L` out of
> the objectwise direct sum over all integers.**

```lean
def coneTwistDirectSumHom :
    Stacks.directSum (fun m : ℤ => (nonnegTwistingSheaf 𝒜 m).val) ⟶
      (Stacks.Morphisms.pushforwardStructureSheaf (pi 𝒜)).val
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistDirectSumHom_app_directSumNatToIntApp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistConeCoproduct.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistConeCoproduct.lean#L163). The attribute's comment: “the inclusion of the nonnegative part of the objectwise direct sum carries the integer-indexed comparison to the one indexed by the natural numbers, on the sections over a standard open of a positive-degree homogeneous element”.

> **The reindexing `ℕ → ℤ` identifies the two comparisons** on the sections over a standard
> open of the basis.

```lean
theorem coneTwistDirectSumHom_app_directSumNatToIntApp (p : PositiveElem 𝒜)
    (z : Stacks.DirectSumType (fun k : ℕ => (nonnegTwistingSheaf 𝒜 (k : ℤ)).val)
      (op (positiveBasicOpen 𝒜 p))) :
    (coneTwistDirectSumHom 𝒜).app (op (positiveBasicOpen 𝒜 p))
        (Stacks.directSumNatToIntApp (fun m : ℤ => (nonnegTwistingSheaf 𝒜 m).val)
          (op (positiveBasicOpen 𝒜 p)) z) =
      (coneTwistNatDirectSumHom 𝒜).app (op (positiveBasicOpen 𝒜 p)) z
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.bijective_coneTwistDirectSumHom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistConeCoproduct.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistConeCoproduct.lean#L190). The attribute's comment: “the morphism out of the objectwise direct sum over all integers of the homogeneous pieces of the nonnegative twist algebra is bijective on the sections over a standard open of a positive-degree homogeneous element, for the cone of the truncation algebra”.

> **Over a standard open of a positive-degree homogeneous element the comparison out of the
> direct sum over all integers is bijective.**

```lean
theorem bijective_coneTwistDirectSumHom_app (p : PositiveElem 𝒜) :
    Function.Bijective
      ((coneTwistDirectSumHom 𝒜).app (op (positiveBasicOpen 𝒜 p))).hom
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneStructureSheafifyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistConeCoproduct.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistConeCoproduct.lean#L207). The attribute's comment: “the direct image of the structure sheaf of the cone is the sheafification of the objectwise direct sum of the homogeneous pieces of the nonnegative twist algebra, for the truncation cone”.

> **`π_* 𝒪_L` is the sheafification of the objectwise direct sum of the homogeneous pieces of
> the algebra of nonnegative twists.**

```lean
def coneStructureSheafifyIso :
    (PresheafOfModules.sheafification (𝟙 _)).obj
        (Stacks.directSum fun m : ℤ => (nonnegTwistingSheaf 𝒜 m).val) ≅
      Stacks.Morphisms.pushforwardStructureSheaf (pi 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneStructureCoproductIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistConeCoproduct.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistConeCoproduct.lean#L224). The attribute's comment: “the identification pi\_* O\_L = the coproduct of the homogeneous pieces of the nonnegative twist algebra, as sheaves of O\_P-modules, for the cone of the truncation algebra”.

> **`π_* 𝒪_L ≅ ∐_{m ∈ ℤ} (nonnegTwistAlgebra 𝒜).piece m`**: the identification of the direct
> image of the structure sheaf of the cone with the coproduct of the homogeneous pieces of the
> algebra of nonnegative twists.

```lean
def coneStructureCoproductIso :
    Stacks.Morphisms.pushforwardStructureSheaf (pi 𝒜) ≅
      ∐ fun m : ℤ => nonnegTwistingSheaf 𝒜 m
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistAwayHom_degreeZeroRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMap.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMap.lean#L140). The attribute's comment: “the degreewise inclusion of the sections of O\_P(m) into the degree-zero localization of the truncation algebra commutes with restriction between two standard opens”.

> The degreewise inclusion commutes with restriction between two standard opens, read in the
> degree-zero localizations of the truncation algebra.

```lean
theorem coneTwistAwayHom_degreeZeroRingMap (m : ℕ) {d e : ℕ} (hf : f ∈ 𝒜 d) (hd : 0 < d)
    (hg : g ∈ 𝒜 e) (he : 0 < e)
    (hfg : ProjectiveSpectrum.basicOpen 𝒜 g ≤ ProjectiveSpectrum.basicOpen 𝒜 f)
    (s : (ProjectiveSpectrum.Proj.twistingSheaf 𝒜 (m : ℤ)).val.obj
      (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    coneTwistAwayHom 𝒜 m e hg he
        (((ProjectiveSpectrum.Proj.twistingSheaf 𝒜 (m : ℤ)).val.map (homOfLE hfg).op).hom s) =
      ProjectiveSpectrum.degreeZeroRingMap (grading 𝒜) (psi 𝒜 f) (psi 𝒜 g)
        (exists_psi_mem 𝒜 hf hd) (exists_psi_mem 𝒜 hg he)
        (basicOpen_psi_le 𝒜 hf hd hg he hfg) (coneTwistAwayHom 𝒜 m d hf hd s)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistApp_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMap.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMap.lean#L194). The attribute's comment: “the degreewise inclusion O\_P(m) to pi\_* O\_L over standard opens is compatible with restriction between two standard opens”.

> The local degreewise inclusion commutes with restriction to a smaller standard open.

```lean
theorem coneTwistApp_restrict (m : ℕ) {d e : ℕ} (hf : f ∈ 𝒜 d) (hd : 0 < d) (hg : g ∈ 𝒜 e)
    (he : 0 < e)
    (hfg : ProjectiveSpectrum.basicOpen 𝒜 g ≤ ProjectiveSpectrum.basicOpen 𝒜 f)
    (s : (ProjectiveSpectrum.Proj.twistingSheaf 𝒜 (m : ℤ)).val.obj
      (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    (coneTwistApp 𝒜 m e hg he).hom
        (((ProjectiveSpectrum.Proj.twistingSheaf 𝒜 (m : ℤ)).val.map (homOfLE hfg).op).hom s) =
      ((Stacks.Morphisms.pushforwardStructureSheaf (pi 𝒜)).val.map (homOfLE hfg).op).hom
        ((coneTwistApp 𝒜 m d hf hd).hom s)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistApp_degree_indep`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMap.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMap.lean#L244). The attribute's comment: “the degreewise inclusion O\_P(m) to pi\_* O\_L over one standard open depends only on that open, not on the degree of the element cutting it out”.

> The local degreewise inclusion depends only on the standard open, not on the degree in
> which the element cutting it out is homogeneous.

```lean
theorem coneTwistApp_degree_indep (m : ℕ) {d d' : ℕ} (hf : f ∈ 𝒜 d) (hd : 0 < d)
    (hf' : f ∈ 𝒜 d') (hd' : 0 < d') :
    coneTwistApp 𝒜 m d hf hd = coneTwistApp 𝒜 m d' hf' hd'
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMap.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMap.lean#L286). The attribute's comment: “the degreewise inclusion O\_P(m) to pi\_* O\_L as a morphism of sheaves of O\_P-modules, for the truncation cone and a nonnegative degree m”.

> The degreewise inclusion `𝒪_P(m) ⟶ π_* 𝒪_L`, for `m ≥ 0`: the morphism of sheaves of
> `𝒪_P`-modules glued from the local maps over the standard opens of positive-degree homogeneous
> elements.

```lean
def coneTwistHom (m : ℕ) :
    ProjectiveSpectrum.Proj.twistingSheaf 𝒜 (m : ℤ) ⟶
      Stacks.Morphisms.pushforwardStructureSheaf (pi 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistHom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMap.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMap.lean#L294). The attribute's comment: “the global degreewise inclusion restricts on each standard open to the local one”.

> The glued morphism restricts on a standard open to the local degreewise inclusion.

```lean
theorem coneTwistHom_app (m : ℕ) {d : ℕ} (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    (coneTwistHom 𝒜 m).val.app (op (ProjectiveSpectrum.basicOpen 𝒜 f)) =
      coneTwistApp 𝒜 m d hf hd
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneIota`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMap.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMap.lean#L307). The attribute's comment: “the inclusion of each homogeneous piece of the nonnegative twist algebra in pi\_* O\_L, for the truncation cone”.

> The inclusion of each homogeneous piece of `⨁_{m ≥ 0} 𝒪_P(m)` in `π_* 𝒪_L`: the glued
> degreewise inclusion in a nonnegative degree, and the morphism out of the zero sheaf in a
> negative one.

```lean
def coneIota : ∀ n : ℤ, nonnegTwistingSheaf 𝒜 n ⟶
    Stacks.Morphisms.pushforwardStructureSheaf (pi 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistHom_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMul.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMul.lean#L97). The attribute's comment: “the glued degreewise inclusion O\_P(m) to pi\_* O\_L is multiplicative over a standard open of a positive-degree homogeneous element”.

> **The glued degreewise inclusion is multiplicative over a standard open** of a
> positive-degree homogeneous element.

```lean
theorem coneTwistHom_mul {f : A} {d : ℕ} (hf : f ∈ 𝒜 d) (hd : 0 < d) (i j : ℕ)
    (x : (twistingSheaf 𝒜 (i : ℤ)).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f)))
    (y : (twistingSheaf 𝒜 (j : ℤ)).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    (show coneSections 𝒜 (ProjectiveSpectrum.basicOpen 𝒜 f) from
        (coneTwistHom 𝒜 (i + j)).val.app (op (ProjectiveSpectrum.basicOpen 𝒜 f))
          (natTwistMulSection 𝒜 i j (op (ProjectiveSpectrum.basicOpen 𝒜 f)) x y)) =
      (show coneSections 𝒜 (ProjectiveSpectrum.basicOpen 𝒜 f) from
          (coneTwistHom 𝒜 i).val.app (op (ProjectiveSpectrum.basicOpen 𝒜 f)) x) *
        (show coneSections 𝒜 (ProjectiveSpectrum.basicOpen 𝒜 f) from
          (coneTwistHom 𝒜 j).val.app (op (ProjectiveSpectrum.basicOpen 𝒜 f)) y)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistHom_mul_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMul.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMul.lean#L119). The attribute's comment: “the glued degreewise inclusion O\_P(m) to pi\_* O\_L is multiplicative over every open of P, in nonnegative degrees”.

> **The glued degreewise inclusion `𝒪_P(i) ⟶ π_* 𝒪_L` is multiplicative over every open of
> `P`.** The standard opens of positive-degree homogeneous elements are a basis, and both sides
> restrict to them as the standard-open statement says.

```lean
theorem coneTwistHom_mul_app (i j : ℕ) (U : Opens (ProjectiveSpectrum.top 𝒜))
    (a : (twistingSheaf 𝒜 (i : ℤ)).val.obj (op U))
    (b : (twistingSheaf 𝒜 (j : ℤ)).val.obj (op U)) :
    (show coneSections 𝒜 U from
        (coneTwistHom 𝒜 (i + j)).val.app (op U) (natTwistMulSection 𝒜 i j (op U) a b)) =
      (show coneSections 𝒜 U from (coneTwistHom 𝒜 i).val.app (op U) a) *
        (show coneSections 𝒜 U from (coneTwistHom 𝒜 j).val.app (op U) b)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneIota_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMul.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistGlobalMul.lean#L160). The attribute's comment: “the inclusions of the homogeneous pieces of the nonnegative twist algebra in pi\_* O\_L are multiplicative, over every open of P and in every integer degree, for the truncation cone”.

> **The inclusions of the homogeneous pieces of the algebra of nonnegative twists in `π_* 𝒪_L`
> multiply as the grading prescribes**, over every open of `P` and in all integer degrees. This is
> the `ι_mul` condition of `AlgebraicGeometry.AbstractCone` for the cone of the truncation algebra,
> graded by `Stacks.AlgebraicGeometry.ProjConeTwist.nonnegTwistAlgebra`. In a negative degree the
> piece is the zero sheaf, so both sides vanish.

```lean
theorem coneIota_mul (i j : ℤ) (U : Opens (ProjectiveSpectrum.top 𝒜))
    (a : (nonnegTwistingSheaf 𝒜 i).val.obj (op U))
    (b : (nonnegTwistingSheaf 𝒜 j).val.obj (op U)) :
    (show coneSections 𝒜 U from
        (coneIota 𝒜 (i + j)).val.app (op U) ((nonnegTwistMul 𝒜 i j).app (op U) a b)) =
      (show coneSections 𝒜 U from (coneIota 𝒜 i).val.app (op U) a) *
        (show coneSections 𝒜 U from (coneIota 𝒜 j).val.app (op U) b)
```

**`Stacks.Truncation.awayToLocalization_map_psi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistLocalMap.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistLocalMap.lean#L67). The attribute's comment: “the comparison map (B[1/psi f])\_0 to A[1/f] undoes the map of degree-zero localizations attached to psi”.

> The comparison map `(B[1/ψ f])₀ → A[1/f]` undoes `HomogeneousLocalization.Away.map ψ f`:
> the fraction `ψ a / (ψ f)ᵏ` of the truncation algebra is sent to the fraction `a / fᵏ`.

```lean
theorem awayToLocalization_map_psi (d : ℕ) (hf : f ∈ 𝒜 d)
    (r : HomogeneousLocalization.Away 𝒜 f) :
    awayToLocalization 𝒜 (HomogeneousLocalization.Away.map (psi 𝒜) f r) = r.val
```

**`Stacks.Truncation.awayGradingEquivSectionsTwist_symm_degree_indep`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistLocalMap.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistLocalMap.lean#L106). The attribute's comment: “the degreewise inclusion of the sections of O\_P(m) over D+(f) into the functions on the cone depends only on the standard open, not on the degree of f”.

> The degreewise inclusion depends only on the standard open, not on the degree in which `f`
> is homogeneous.

```lean
theorem awayGradingEquivSectionsTwist_symm_degree_indep {d d' : ℕ} (hf : f ∈ 𝒜 d) (hd : 0 < d)
    (hf' : f ∈ 𝒜 d') (hd' : 0 < d') (m : ℕ)
    (s : (twistingSheaf 𝒜 (m : ℤ)).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    (((awayGradingEquivSectionsTwist 𝒜 d hf hd m).symm s :
        HomogeneousLocalization.Away (grading 𝒜) (psi 𝒜 f))) =
      (((awayGradingEquivSectionsTwist 𝒜 d' hf' hd' m).symm s :
        HomogeneousLocalization.Away (grading 𝒜) (psi 𝒜 f)))
```

**`Stacks.Truncation.awayGradingEquivSectionsTwist_symm_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistLocalMap.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistLocalMap.lean#L126). The attribute's comment: “the degreewise inclusion is semilinear for the map of degree-zero localizations attached to psi, over one standard open D+(f)”.

> The degreewise inclusion `Γ(D₊(f), 𝒪_P(m)) → (B[1/ψ f])₀` is semilinear for the map
> `HomogeneousLocalization.Away.map ψ f` of degree-zero localizations: scaling a section of
> `𝒪_P(m)` by the degree-zero fraction `r` multiplies its image by the image of `r`.

```lean
theorem awayGradingEquivSectionsTwist_symm_smul (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) (m : ℕ)
    (r : HomogeneousLocalization.Away 𝒜 f)
    (s : (twistingSheaf 𝒜 (m : ℤ)).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    (((awayGradingEquivSectionsTwist 𝒜 d hf hd m).symm
          ((ProjectiveSpectrum.Proj.awayToSection 𝒜 f).hom r • s) :
        HomogeneousLocalization.Away (grading 𝒜) (psi 𝒜 f))) =
      HomogeneousLocalization.Away.map (psi 𝒜) f r *
        (((awayGradingEquivSectionsTwist 𝒜 d hf hd m).symm s :
          HomogeneousLocalization.Away (grading 𝒜) (psi 𝒜 f)))
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.awayToSection_pi_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistLocalMap.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistLocalMap.lean#L205). The attribute's comment: “the cone projection on functions over a standard open, with the sections over D+(psi f) transported along the identity of opens pi^\{-1}(D+(f)) = D+(psi f)”.

> The cone projection on functions over a standard open: the image of a degree-zero fraction of
> `A` under `ψ`, read as a function on `D₊(ψ f)` and transported along `π⁻¹(D₊(f)) = D₊(ψ f)`, is
> the pullback of that fraction along `π`.

```lean
theorem awayToSection_pi_app (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d)
    (r : HomogeneousLocalization.Away 𝒜 f) :
    (AlgebraicGeometry.Proj (grading 𝒜)).presheaf.map
        (eqToHom (pi_preimage_basicOpen 𝒜 f d hf hd)).op
        ((AlgebraicGeometry.Proj.awayToSection (grading 𝒜) (psi 𝒜 f)).hom
          (HomogeneousLocalization.Away.map (psi 𝒜) f r)) =
      ((pi 𝒜).app (AlgebraicGeometry.Proj.basicOpen 𝒜 f)).hom
        ((AlgebraicGeometry.Proj.awayToSection 𝒜 f).hom r)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistAwayHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistLocalMap.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistLocalMap.lean#L231). The attribute's comment: “the degreewise inclusion of the sections of O\_P(m) over D+(f) into the degree-zero localization of the truncation algebra, as an additive map”.

> The degreewise inclusion `Γ(D₊(f), 𝒪_P(m)) → (B[1/ψ f])₀`, as an additive map: the
> inverse of `Stacks.Truncation.awayGradingEquivSectionsTwist` followed by the inclusion of the
> degree-`m` summand.

```lean
def coneTwistAwayHom (m d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    ((twistingSheaf 𝒜 (m : ℤ)).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) →+
      HomogeneousLocalization.Away (grading 𝒜) (psi 𝒜 f)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistApp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistLocalMap.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistLocalMap.lean#L250). The attribute's comment: “the degreewise inclusion O\_P(m) to pi\_* O\_L over one standard open D+(f), as a map of modules over the sections of O\_P there”.

> The local degreewise inclusion `Γ(D₊(f), 𝒪_P(m)) ⟶ Γ(D₊(f), π_* 𝒪_L)`, as a morphism of
> modules over the sections of `𝒪_P` on `D₊(f)`.

```lean
def coneTwistApp (m d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    (twistingSheaf 𝒜 (m : ℤ)).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f)) ⟶
      (Stacks.Morphisms.pushforwardStructureSheaf (pi 𝒜)).val.obj
        (op (AlgebraicGeometry.Proj.basicOpen 𝒜 f))
```

**`Stacks.Truncation.awayToLocalization_degreeZeroRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistLocalRestriction.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistLocalRestriction.lean#L99). The attribute's comment: “the comparison maps (B[1/psi f])\_0 to A[1/f] commute with the restriction maps of degree-zero localizations, for a general inclusion D+(g) <= D+(f) of standard opens”.

> The comparison maps `(B[1/ψ f])₀ → A[1/f]` commute with the restriction maps of
> degree-zero localizations: the one of `B` attached to `D₊(ψ g) ⊆ D₊(ψ f)` on the source, the
> one of `A` attached to `D₊(g) ⊆ D₊(f)` on the target.

```lean
theorem awayToLocalization_degreeZeroRingMap
    (hf : ∃ d : ℕ, 0 < d ∧ f ∈ 𝒜 d) (hg : ∃ e : ℕ, 0 < e ∧ g ∈ 𝒜 e)
    (hψf : ∃ d : ℕ, 0 < d ∧ psi 𝒜 f ∈ grading 𝒜 d)
    (hψg : ∃ e : ℕ, 0 < e ∧ psi 𝒜 g ∈ grading 𝒜 e)
    (hfg : ProjectiveSpectrum.basicOpen 𝒜 g ≤ ProjectiveSpectrum.basicOpen 𝒜 f)
    (hψfg : ProjectiveSpectrum.basicOpen (grading 𝒜) (psi 𝒜 g) ≤
      ProjectiveSpectrum.basicOpen (grading 𝒜) (psi 𝒜 f))
    (z : HomogeneousLocalization.Away (grading 𝒜) (psi 𝒜 f)) :
    awayToLocalization 𝒜
        (ProjectiveSpectrum.degreeZeroRingMap (grading 𝒜) (psi 𝒜 f) (psi 𝒜 g)
          hψf hψg hψfg z) =
      ProjectiveSpectrum.localizedRingMap 𝒜 f g hf hg hfg (awayToLocalization 𝒜 z)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.integerTwistAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean#L248). The attribute's comment: “the graded algebra of all integral twists”.

> The graded algebra `⨁_{m ∈ ℤ} 𝒪_P(m)` of all integral twists on `P = Proj A`.

```lean
def integerTwistAlgebra :
    SheafOfModules.GradedAlgebra (AlgebraicGeometry.Proj 𝒜).ringCatSheaf
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.isZero_nonnegTwistingSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean#L286). The attribute's comment: “the homogeneous pieces in negative degrees”.

> In negative degrees the pieces of the algebra of nonnegative twists vanish.

```lean
theorem isZero_nonnegTwistingSheaf {n : ℤ} (hn : n < 0) :
    IsZero (nonnegTwistingSheaf 𝒜 n)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.nonnegTwistAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean#L337). The attribute's comment: “the graded algebra of nonnegative twists”.

> The graded algebra `⨁_{m ≥ 0} 𝒪_P(m)` of nonnegative twists on `P = Proj A`.

```lean
def nonnegTwistAlgebra :
    SheafOfModules.GradedAlgebra (AlgebraicGeometry.Proj 𝒜).ringCatSheaf
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.nonnegPieceIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean#L409). The attribute's comment: “the homogeneous pieces in nonnegative degrees”.

> In nonnegative degrees the piece of the algebra of nonnegative twists is the twisting sheaf.

```lean
def nonnegPieceIso {n : ℤ} (hn : 0 ≤ n) :
    (nonnegTwistAlgebra 𝒜).piece n ≅ twistingSheaf 𝒜 n
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.nonnegToIntegerTwistAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean, line 474](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean#L474). The attribute's comment: “the inclusion of the nonnegative twist algebra in the integral one”.

> The inclusion `⨁_{m ≥ 0} 𝒪_P(m) ⟶ ⨁_{m ∈ ℤ} 𝒪_P(m)` of graded algebras.

```lean
def nonnegToIntegerTwistAlgebra :
    SheafOfModules.GradedAlgebra.Hom (nonnegTwistAlgebra 𝒜) (integerTwistAlgebra 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.nonnegToIntegerTwistAlgebra_app_natCast`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean, line 481](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean#L481). The attribute's comment: “the inclusion is the identity on each nonnegative twist”.

> In nonnegative degrees the inclusion of the two twist algebras is the identity.

```lean
theorem nonnegToIntegerTwistAlgebra_app_natCast (m : ℕ) :
    (nonnegToIntegerTwistAlgebra 𝒜).app (m : ℤ) = CategoryStruct.id _
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean, line 509](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean#L509). The attribute's comment: “the direct-image algebra of the cone”.

> The direct-image algebra `π_* 𝒪_L` of the cone.

```lean
def coneAlgebra : Stacks.RelativeSpec.AlgebraSheaf (AlgebraicGeometry.Proj 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean, line 515](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean#L515). The attribute's comment: “the direct-image algebra of the punctured cone”.

> The direct-image algebra `(π|_U)_* 𝒪_U` of the punctured cone, the part of `L` lying over
> `U = X ∖ V(A₊)`.

```lean
def puncturedConeAlgebra : Stacks.RelativeSpec.AlgebraSheaf (AlgebraicGeometry.Proj 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneToPuncturedConeAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean, line 522](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean#L522). The attribute's comment: “the inclusion of the two direct-image algebras”.

> Restriction of functions from the cone to the punctured cone, as a morphism of
> `𝒪_P`-algebras.

```lean
def coneToPuncturedConeAlgebra : coneAlgebra c ⟶ puncturedConeAlgebra c
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneToPuncturedConeAlgebra_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean, line 529](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean#L529). The attribute's comment: “the restriction formula for the inclusion of the two algebras”.

> Over an open of `P` the restriction map of the two direct-image algebras is the canonical map
> on functions induced by the open immersion of the punctured cone.

```lean
theorem coneToPuncturedConeAlgebra_app (U : (AlgebraicGeometry.Proj 𝒜).Opens)
    (hle : ((ProjAndSpec.openUInL c).ι ≫ ProjAndSpec.pi c) ⁻¹ᵁ U ≤
      (ProjAndSpec.openUInL c).ι ⁻¹ᵁ (ProjAndSpec.pi c ⁻¹ᵁ U)) :
    (coneToPuncturedConeAlgebra c).right.hom.app (op U) =
      (ProjAndSpec.openUInL c).ι.appLE (ProjAndSpec.pi c ⁻¹ᵁ U)
        (((ProjAndSpec.openUInL c).ι ≫ ProjAndSpec.pi c) ⁻¹ᵁ U) hle
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.structureSheafToTwistZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean, line 572](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean#L572). The attribute's comment: “the comparison of the degree-zero piece with the structure sheaf”.

> A section of the structure sheaf, read in the localizations of `A`, as a section of the
> untwisted sheaf.

```lean
def structureSheafToTwistZero (U : Opens (ProjectiveSpectrum.top 𝒜))
    (r : (ProjectiveSpectrum.Proj.structureSheaf 𝒜).obj.obj (op U)) :
    (twistingSheaf 𝒜 0).val.obj (op U)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.structureSheafToTwistZero_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean, line 586](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean#L586). The attribute's comment: “the degree-zero comparison preserves the unit”.

> The comparison carries the unit section of the structure sheaf to the unit section of the
> untwisted sheaf.

```lean
theorem structureSheafToTwistZero_one (U : Opens (ProjectiveSpectrum.top 𝒜)) :
    structureSheafToTwistZero 𝒜 U 1 = (twistOne 𝒜).eval (op U)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.structureSheafToTwistZero_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean, line 593](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean#L593). The attribute's comment: “the degree-zero comparison is multiplicative”.

> The comparison is multiplicative, the product on the right being the degree-zero part of the
> multiplication of twists.

```lean
theorem structureSheafToTwistZero_mul (U : Opens (ProjectiveSpectrum.top 𝒜))
    (r r' : (ProjectiveSpectrum.Proj.structureSheaf 𝒜).obj.obj (op U)) :
    structureSheafToTwistZero 𝒜 U (r * r') =
      twistMulSection 𝒜 0 0 (op U) (structureSheafToTwistZero 𝒜 U r)
        (structureSheafToTwistZero 𝒜 U r')
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.structureSheafToTwistZero_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean, line 609](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean#L609). The attribute's comment: “injectivity of the degree-zero comparison”.

> The comparison of the structure sheaf with `𝒪_P(0)` is injective over every open.

```lean
theorem structureSheafToTwistZero_injective (U : Opens (ProjectiveSpectrum.top 𝒜)) :
    Function.Injective (structureSheafToTwistZero 𝒜 U)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.structureSheafToTwistZero_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean, line 617](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean#L617). The attribute's comment: “surjectivity of the degree-zero comparison”.

> The comparison of the structure sheaf with `𝒪_P(0)` is surjective over every open.

```lean
theorem structureSheafToTwistZero_surjective (U : Opens (ProjectiveSpectrum.top 𝒜)) :
    Function.Surjective (structureSheafToTwistZero 𝒜 U)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.structureSheafToTwistZero_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean, line 642](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPresentation.lean#L642). The attribute's comment: “the degree-zero piece is the structure sheaf”.

> The degree-zero piece of the twist algebra is the structure sheaf: over every open the
> comparison is a bijection.

```lean
theorem structureSheafToTwistZero_bijective (U : Opens (ProjectiveSpectrum.top 𝒜)) :
    Function.Bijective (structureSheafToTwistZero 𝒜 U)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedTotalPresheafHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedAlgebraSheaf.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedAlgebraSheaf.lean#L97). The attribute's comment: “the degreewise inclusions as a morphism of presheaves of rings from the ungraded realization of the integral twist algebra to (pi|\_U)\_* O\_U, for the truncation cone”.

> **The degreewise inclusions as a morphism of presheaves of rings** from the ungraded
> realization of the algebra of all integral twists into `(π|_U)_* 𝒪_U`.

```lean
def puncturedTotalPresheafHom :
    (integerTwistPresheafAlgebra 𝒜).totalPresheaf ⟶ (puncturedConePushforwardRingSheaf 𝒜).obj
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeUngradedSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedAlgebraSheaf.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedAlgebraSheaf.lean#L131). The attribute's comment: “the identification (pi|\_U)\_* O\_U = the ungraded realization of the integral twist algebra, as sheaves of rings, for the punctured cone of the truncation algebra”.

> **`(π|_U)_* 𝒪_U` is the ungraded realization of the algebra of all integral twists**, as
> sheaves of rings.

```lean
def puncturedConeUngradedSheafIso :
    (integerTwistAlgebra 𝒜).ungradedSheaf ≅ puncturedConePushforwardRingSheaf 𝒜
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.heq_twistMul_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedAlgebraSheaf.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedAlgebraSheaf.lean#L151). The attribute's comment: “the multiplication of the integral twist algebra is commutative on homogeneous local sections”.

> **The multiplication of the algebra of all integral twists is commutative** on homogeneous
> local sections: it is the pointwise product of the values in the module fibres.

```lean
theorem heq_twistMul_comm (i j : ℤ) (V : (Opens (ProjectiveSpectrum.top 𝒜))ᵒᵖ)
    (a : (twistingSheaf 𝒜 i).val.obj V) (b : (twistingSheaf 𝒜 j).val.obj V) :
    HEq ((twistMul 𝒜 i j).app V a b) ((twistMul 𝒜 j i).app V b a)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.integerTwistAlgebraSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedAlgebraSheaf.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedAlgebraSheaf.lean#L164). The attribute's comment: “the integral twist algebra as a sheaf of commutative algebras over the structure sheaf of P”.

> **The algebra of all integral twists `⨁_{m ∈ ℤ} 𝒪_P(m)` as a sheaf of commutative
> `𝒪_P`-algebras.**

```lean
def integerTwistAlgebraSheaf : Stacks.RelativeSpec.AlgebraSheaf (AlgebraicGeometry.Proj 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedTotalMap_structureMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedAlgebraSheaf.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedAlgebraSheaf.lean#L174). The attribute's comment: “the degreewise inclusions carry the structure map of the ungraded realization of the integral twist algebra to the pullback of functions along the punctured cone projection”.

> **The degreewise inclusions carry the structure map `r ↦ r · 1` of the ungraded realization to
> the pullback of functions along `π|_U`.**

```lean
theorem puncturedTotalMap_structureMap (V : Opens (ProjectiveSpectrum.top 𝒜))
    (r : ((ProjectiveSpectrum.Proj.structureSheaf 𝒜).obj ⋙
      forget₂ CommRingCat.{u} RingCat.{u}).obj (op V)) :
    puncturedTotalMap 𝒜 V ((integerTwistPresheafAlgebra 𝒜).structureMap (op V) r) =
      (((openUInL 𝒜).ι ≫ pi 𝒜).c.app (op V)).hom r
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeAlgebraSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedAlgebraSheaf.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedAlgebraSheaf.lean#L205). The attribute's comment: “the identification (pi|\_U)\_* O\_U = the integral twist algebra, as sheaves of commutative algebras over the structure sheaf of P, for the punctured cone of the truncation algebra”.

> **`(π|_U)_* 𝒪_U` is the algebra of all integral twists**, as sheaves of commutative
> `𝒪_P`-algebras.

```lean
def puncturedConeAlgebraSheafIso :
    integerTwistAlgebraSheaf 𝒜 ≅ pushforwardAlgebra ((openUInL 𝒜).ι ≫ pi 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.isQuasicoherent_integerTwistAlgebraSheaf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedAlgebraSheaf.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedAlgebraSheaf.lean#L222). The attribute's comment: “the integral twist algebra is a quasi-coherent sheaf of algebras over the structure sheaf of P”.

> The algebra of all integral twists is a quasi-coherent sheaf of `𝒪_P`-algebras: it is the
> direct image of the structure sheaf of the punctured cone along the affine morphism `π|_U`.

```lean
instance isQuasicoherent_integerTwistAlgebraSheaf :
    Stacks.RelativeSpec.AlgebraSheaf.IsQuasicoherent (integerTwistAlgebraSheaf 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeRelativeSpecTwistAlgebraIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedAlgebraSheaf.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedAlgebraSheaf.lean#L231). The attribute's comment: “U is, over P, the relative spectrum of the integral twist algebra, for the punctured cone of the truncation algebra”.

> **`U = Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m))`**: the punctured cone is, over `P = Proj A`, the relative
> spectrum of the algebra of all integral twists.

```lean
def puncturedConeRelativeSpecTwistAlgebraIso :
    Over.mk ((openUInL 𝒜).ι ≫ pi 𝒜) ≅
      Over.mk (relativeSpecToBase (integerTwistAlgebraSheaf 𝒜))
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedTwistDirectSumHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedCoproduct.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedCoproduct.lean#L95). The attribute's comment: “the family of degreewise inclusions O\_P(m) -> (pi|\_U)\_* O\_U as one morphism out of the objectwise direct sum over all integers m, for the truncation cone”.

> **The family of punctured degreewise inclusions as a single morphism out of the objectwise
> direct sum** `⨁_{m ∈ ℤ} 𝒪_P(m) ⟶ (π|_U)_* 𝒪_U`.

```lean
def puncturedTwistDirectSumHom :
    Stacks.directSum (fun m : ℤ => (twistingSheaf 𝒜 m).val) ⟶
      (Stacks.Morphisms.pushforwardStructureSheaf ((openUInL 𝒜).ι ≫ pi 𝒜)).val
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.bijective_puncturedTwistDirectSumHom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedCoproduct.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedCoproduct.lean#L123). The attribute's comment: “the morphism out of the objectwise direct sum of the twisting sheaves is bijective on the sections over a standard open of a positive-degree homogeneous element, for the punctured cone of the truncation algebra”.

> **Over a standard open of a positive-degree homogeneous element the morphism out of the
> objectwise direct sum is bijective.** It agrees there with the additive equivalence
> `Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeAlgebraSectionsEquivTwistSections`, read
> backwards.

```lean
theorem bijective_puncturedTwistDirectSumHom_app (p : PositiveElem 𝒜) :
    Function.Bijective
      ((puncturedTwistDirectSumHom 𝒜).app (op (positiveBasicOpen 𝒜 p))).hom
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeStructureSheafifyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedCoproduct.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedCoproduct.lean#L151). The attribute's comment: “the direct image of the structure sheaf of the punctured cone is the sheafification of the objectwise direct sum of all the twisting sheaves, for the truncation cone”.

> **`(π|_U)_* 𝒪_U` is the sheafification of the objectwise direct sum `⨁_{m ∈ ℤ} 𝒪_P(m)`.**
> The comparison morphism is bijective on the sections over every standard open of a
> positive-degree homogeneous element, and those form a basis of `P`.

```lean
def puncturedConeStructureSheafifyIso :
    (PresheafOfModules.sheafification (𝟙 _)).obj
        (Stacks.directSum fun m : ℤ => (twistingSheaf 𝒜 m).val) ≅
      Stacks.Morphisms.pushforwardStructureSheaf ((openUInL 𝒜).ι ≫ pi 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeStructureCoproductIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedCoproduct.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedCoproduct.lean#L169). The attribute's comment: “the identification (pi|\_U)\_* O\_U = the coproduct over all integers m of the twisting sheaves O\_P(m), as sheaves of O\_P-modules, for the punctured cone of the truncation algebra”.

> **`(π|_U)_* 𝒪_U ≅ ∐_{m ∈ ℤ} 𝒪_P(m)`**: the identification of [Stacks, Tag 0EKG] of the direct
> image of the structure sheaf of the punctured cone with the coproduct, over all integers, of the
> twisting sheaves of `P = Proj A`.

```lean
def puncturedConeStructureCoproductIso :
    Stacks.Morphisms.pushforwardStructureSheaf ((openUInL 𝒜).ι ≫ pi 𝒜) ≅
      ∐ fun m : ℤ => twistingSheaf 𝒜 m
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeStructurePushforwardCoproductIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedCoproduct.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedCoproduct.lean#L182). The attribute's comment: “the identification (pi|\_U)\_* O\_U = the coproduct over all integers m of the twisting sheaves O\_P(m), with the source written as the direct image along the punctured cone projection of the truncation cone data”.

> **`(π|_U)_* 𝒪_U ≅ ∐_{m ∈ ℤ} 𝒪_P(m)`**, with the source written as the direct image along
> `Stacks.AlgebraicGeometry.ProjAndSpec.puncturedConeProj` of the structure sheaf of the punctured
> cone. This is the form in which the identification is consumed by the projection formula along
> `π|_U`.

```lean
def puncturedConeStructurePushforwardCoproductIso :
    (Scheme.Modules.pushforward
          (Stacks.AlgebraicGeometry.ProjAndSpec.puncturedConeProj (truncationConeData 𝒜))).obj
        (SheafOfModules.unit
          (Stacks.AlgebraicGeometry.ProjAndSpec.openUInL
            (truncationConeData 𝒜)).toScheme.ringCatSheaf) ≅
      ∐ fun m : ℤ => twistingSheaf 𝒜 m
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeTwistApp_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedGlobalMap.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedGlobalMap.lean#L143). The attribute's comment: “the degreewise inclusion O\_P(m) to (pi|\_U)\_* O\_U over standard opens is compatible with restriction between two standard opens, for every integer m”.

> **The local punctured degreewise inclusion commutes with restriction to a smaller standard
> open.** This is the compatibility the gluing principle of [Stacks, Tag 009U] asks for.

```lean
theorem puncturedConeTwistApp_restrict (m : ℤ) {d e : ℕ} (hf : f ∈ 𝒜 d) (hd : 0 < d)
    (hg : g ∈ 𝒜 e) (he : 0 < e)
    (hfg : ProjectiveSpectrum.basicOpen 𝒜 g ≤ ProjectiveSpectrum.basicOpen 𝒜 f)
    (s : (twistingSheaf 𝒜 m).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    (puncturedConeTwistApp 𝒜 m e hg he).hom
        (((twistingSheaf 𝒜 m).val.map (homOfLE hfg).op).hom s) =
      ((Stacks.Morphisms.pushforwardStructureSheaf ((openUInL 𝒜).ι ≫ pi 𝒜)).val.map
          (homOfLE hfg).op).hom ((puncturedConeTwistApp 𝒜 m d hf hd).hom s)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeTwistApp_degree_indep`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedGlobalMap.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedGlobalMap.lean#L184). The attribute's comment: “the degreewise inclusion O\_P(m) to (pi|\_U)\_* O\_U over one standard open depends only on that open, not on the degree of the element cutting it out, for every integer m”.

> **The local punctured degreewise inclusion depends only on the standard open**, not on the
> degree in which the element cutting it out is homogeneous.

```lean
theorem puncturedConeTwistApp_degree_indep (m : ℤ) {d d' : ℕ} (hf : f ∈ 𝒜 d) (hd : 0 < d)
    (hf' : f ∈ 𝒜 d') (hd' : 0 < d') :
    puncturedConeTwistApp 𝒜 m d hf hd = puncturedConeTwistApp 𝒜 m d' hf' hd'
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedTwistHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedGlobalMap.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedGlobalMap.lean#L227). The attribute's comment: “the degreewise inclusion O\_P(m) to (pi|\_U)\_* O\_U as a morphism of sheaves of O\_P-modules, for the punctured cone of the truncation algebra and every integer m”.

> **The degreewise inclusion `𝒪_P(m) ⟶ (π|_U)_* 𝒪_U`**, for every integer `m`: the morphism of
> sheaves of `𝒪_P`-modules glued from the local maps over the standard opens of positive-degree
> homogeneous elements. This is the degreewise half of the presentation
> `(π|_U)_* 𝒪_U = ⨁_{m ∈ ℤ} 𝒪_P(m)` of [Stacks, Tag 0EKG].

```lean
def puncturedTwistHom (m : ℤ) :
    ProjectiveSpectrum.Proj.twistingSheaf 𝒜 m ⟶
      Stacks.Morphisms.pushforwardStructureSheaf ((openUInL 𝒜).ι ≫ pi 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedTwistHom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedGlobalMap.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedGlobalMap.lean#L238). The attribute's comment: “the global punctured degreewise inclusion restricts on each standard open to the local one, for every integer m”.

> **The glued punctured morphism restricts on a standard open to the local degreewise
> inclusion.**

```lean
theorem puncturedTwistHom_app (m : ℤ) (p : PositiveElem 𝒜) :
    (puncturedTwistHom 𝒜 m).val.app (op (positiveBasicOpen 𝒜 p)) =
      puncturedConeTwistStandardOpenApp 𝒜 m p
```

**`Stacks.Truncation.puncturedToLocalization_degreeZeroRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean#L119). The attribute's comment: “the comparison maps (B[1/sigma f * psi f])\_0 to A[1/f] and (B[1/psi f])\_0 to A[1/f] agree across the degree-zero restriction map of B attached to D+(sigma f * psi f) <= D+(psi f)”.

> The comparison maps `(B[1/σ f · ψ f])₀ → A[1/f]` and `(B[1/ψ f])₀ → A[1/f]` agree across the
> restriction map of `B` attached to `D₊(σ f · ψ f) ⊆ D₊(ψ f)`.

```lean
theorem puncturedToLocalization_degreeZeroRingMap
    (hψf : ∃ e : ℕ, 0 < e ∧ psi 𝒜 f ∈ grading 𝒜 e)
    (hσψf : ∃ e : ℕ, 0 < e ∧ sigmaMulPsi 𝒜 f ∈ grading 𝒜 e)
    (hle : ProjectiveSpectrum.basicOpen (grading 𝒜) (sigmaMulPsi 𝒜 f) ≤
      ProjectiveSpectrum.basicOpen (grading 𝒜) (psi 𝒜 f))
    (z : HomogeneousLocalization.Away (grading 𝒜) (psi 𝒜 f)) :
    puncturedToLocalization 𝒜
        (ProjectiveSpectrum.degreeZeroRingMap (grading 𝒜) (psi 𝒜 f) (sigmaMulPsi 𝒜 f)
          hψf hσψf hle z) =
      awayToLocalization 𝒜 z
```

**`Stacks.Truncation.puncturedToLocalization_degreeZeroRingMap_map_psi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean#L153). The attribute's comment: “the comparison map (B[1/sigma f * psi f])\_0 to A[1/f] undoes the chart description of the punctured cone projection on a standard open”.

> The comparison map `(B[1/σ f · ψ f])₀ → A[1/f]` undoes the chart description of the punctured
> cone projection, the map `A₍f₎ → B₍σ f · ψ f₎` of degree-zero localizations attached to `ψ`
> followed by restriction.

```lean
theorem puncturedToLocalization_degreeZeroRingMap_map_psi (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d)
    (r : HomogeneousLocalization.Away 𝒜 f) :
    puncturedToLocalization 𝒜
        (ProjectiveSpectrum.degreeZeroRingMap (grading 𝒜) (psi 𝒜 f) (sigmaMulPsi 𝒜 f)
          ⟨d, hd, GradedRingHom.map_mem (psi 𝒜) hf⟩ ⟨d, hd, sigmaMulPsi_mem_grading 𝒜 d hf⟩
          (basicOpen_sigmaMulPsi_le_psi 𝒜)
          (HomogeneousLocalization.Away.map (psi 𝒜) f r)) =
      r.val
```

**`Stacks.Truncation.puncturedGradingEquivSectionsTwist_symm_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean#L185). The attribute's comment: “the degreewise inclusion of the sections of O\_P(m) over D+(f) into the degree-zero localization of the truncation algebra at sigma f * psi f is semilinear for the chart description of the punctured cone projection, for every integer m”.

> **The degreewise inclusion `Γ(D₊(f), 𝒪_P(m)) → (B[1/σ f · ψ f])₀` is semilinear for the chart
> description of the punctured cone projection**, the map `A₍f₎ → B₍σ f · ψ f₎` of degree-zero
> localizations attached to `ψ` followed by restriction. Scaling a section of `𝒪_P(m)` by a
> degree-zero fraction `r` multiplies its image by the image of `r`.

```lean
theorem puncturedGradingEquivSectionsTwist_symm_smul (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) (m : ℤ)
    (r : HomogeneousLocalization.Away 𝒜 f)
    (s : (twistingSheaf 𝒜 m).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    (((puncturedGradingEquivSectionsTwist 𝒜 d hf hd m).symm
          ((ProjectiveSpectrum.Proj.awayToSection 𝒜 f).hom r • s) :
        HomogeneousLocalization.Away (grading 𝒜) (sigmaMulPsi 𝒜 f))) =
      ProjectiveSpectrum.degreeZeroRingMap (grading 𝒜) (psi 𝒜 f) (sigmaMulPsi 𝒜 f)
          ⟨d, hd, GradedRingHom.map_mem (psi 𝒜) hf⟩ ⟨d, hd, sigmaMulPsi_mem_grading 𝒜 d hf⟩
          (basicOpen_sigmaMulPsi_le_psi 𝒜) (HomogeneousLocalization.Away.map (psi 𝒜) f r) *
        (((puncturedGradingEquivSectionsTwist 𝒜 d hf hd m).symm s :
          HomogeneousLocalization.Away (grading 𝒜) (sigmaMulPsi 𝒜 f)))
```

**`Stacks.Truncation.puncturedGradingEquivSectionsTwist_symm_degree_indep`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean#L207). The attribute's comment: “the punctured degreewise inclusion over one standard open depends only on that open, not on the degree of the element cutting it out”.

> **The punctured degreewise inclusion depends only on the standard open**, not on the degree
> in which `f` is homogeneous.

```lean
theorem puncturedGradingEquivSectionsTwist_symm_degree_indep {d d' : ℕ} (hf : f ∈ 𝒜 d)
    (hd : 0 < d) (hf' : f ∈ 𝒜 d') (hd' : 0 < d') (m : ℤ)
    (s : (twistingSheaf 𝒜 m).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    (((puncturedGradingEquivSectionsTwist 𝒜 d hf hd m).symm s :
        HomogeneousLocalization.Away (grading 𝒜) (sigmaMulPsi 𝒜 f))) =
      (((puncturedGradingEquivSectionsTwist 𝒜 d' hf' hd' m).symm s :
        HomogeneousLocalization.Away (grading 𝒜) (sigmaMulPsi 𝒜 f)))
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.openUInL_image_puncturedPi_preimage_basicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean#L262). The attribute's comment: “the image in L of the chart of U over a standard open D+(f) is the standard open D+(sigma f * psi f), for the truncation cone”.

> **The image in `L` of the chart of `U` over `D₊(f)` is the standard open `D₊(σ f · ψ f)`.**

```lean
theorem openUInL_image_puncturedPi_preimage_basicOpen (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    (openUInL 𝒜).ι ''ᵁ (((openUInL 𝒜).ι ≫ pi 𝒜) ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen 𝒜 f) =
      AlgebraicGeometry.Proj.basicOpen (grading 𝒜) (sigmaMulPsi 𝒜 f)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedPi_preimage_basicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean#L272). The attribute's comment: “the chart of U over a standard open D+(f) is the inverse image of D+(sigma f * psi f) under the open immersion of U, for the truncation cone”.

> **The chart of `U` over `D₊(f)` is the inverse image of `D₊(σ f · ψ f)`.**

```lean
theorem puncturedPi_preimage_basicOpen (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    ((openUInL 𝒜).ι ≫ pi 𝒜) ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen 𝒜 f =
      (openUInL 𝒜).ι ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen (grading 𝒜) (sigmaMulPsi 𝒜 f)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.awayToSection_puncturedPi_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean#L330). The attribute's comment: “the punctured cone projection on functions over a standard open, with the sections over D+(sigma f * psi f) restricted to the chart of U over D+(f)”.

> **The punctured cone projection on functions over a standard open, in the form the direct
> image needs:** the image of a degree-zero fraction of `A` under the chart description
> `puncturedAwayMap`, read as a function on `D₊(σ f · ψ f)` and restricted to the chart of `U` over
> `D₊(f)`, is the pullback of that fraction along `π|_U`.

```lean
theorem awayToSection_puncturedPi_app (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d)
    (r : HomogeneousLocalization.Away 𝒜 f) :
    (puncturedChartRestrict 𝒜 d hf hd).hom
        ((AlgebraicGeometry.Proj.awayToSection (grading 𝒜) (sigmaMulPsi 𝒜 f)).hom
          (ProjectiveSpectrum.degreeZeroRingMap (grading 𝒜) (psi 𝒜 f) (sigmaMulPsi 𝒜 f)
            ⟨d, hd, GradedRingHom.map_mem (psi 𝒜) hf⟩
            ⟨d, hd, sigmaMulPsi_mem_grading 𝒜 d hf⟩ (basicOpen_sigmaMulPsi_le_psi 𝒜)
            (HomogeneousLocalization.Away.map (psi 𝒜) f r))) =
      (((openUInL 𝒜).ι ≫ pi 𝒜).app (AlgebraicGeometry.Proj.basicOpen 𝒜 f)).hom
        ((AlgebraicGeometry.Proj.awayToSection 𝒜 f).hom r)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeTwistAwayHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean#L365). The attribute's comment: “the degreewise inclusion of the sections of O\_P(m) over D+(f) into the degree-zero localization of the truncation algebra at sigma f * psi f, as an additive map, for every integer m”.

> **The degreewise inclusion `Γ(D₊(f), 𝒪_P(m)) → (B[1/σ f · ψ f])₀`, as an additive map**, for
> every integer `m`. It is the inverse of
> `Stacks.Truncation.puncturedGradingEquivSectionsTwist` followed by the inclusion of the
> degree-`m` summand.

```lean
def puncturedConeTwistAwayHom (m : ℤ) (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    ((twistingSheaf 𝒜 m).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) →+
      HomogeneousLocalization.Away (grading 𝒜) (sigmaMulPsi 𝒜 f)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeTwistApp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean, line 384](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalMap.lean#L384). The attribute's comment: “the degreewise inclusion O\_P(m) to (pi|\_U)\_* O\_U over one standard open D+(f), as a map of modules over the sections of O\_P there, for every integer m”.

> **The local degreewise inclusion `Γ(D₊(f), 𝒪_P(m)) ⟶ Γ(D₊(f), (π|_U)_* 𝒪_U)`, as a morphism
> of modules over the sections of `𝒪_P` on `D₊(f)`**, for every integer `m`. This is the local
> datum from which the global morphism `𝒪_P(m) ⟶ (π|_U)_* 𝒪_U` is glued.

```lean
def puncturedConeTwistApp (m : ℤ) (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    (twistingSheaf 𝒜 m).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f)) ⟶
      (Stacks.Morphisms.pushforwardStructureSheaf ((openUInL 𝒜).ι ≫ pi 𝒜)).val.obj
        (op (AlgebraicGeometry.Proj.basicOpen 𝒜 f))
```

**`Stacks.Truncation.puncturedToLocalization_degreeZeroRingMap_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalRestriction.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalRestriction.lean#L82). The attribute's comment: “the comparison maps (B[1/sigma f * psi f])\_0 to A[1/f] commute with the restriction maps of degree-zero localizations, for a general inclusion D+(g) <= D+(f) of standard opens”.

> **The comparison maps `(B[1/σ f · ψ f])₀ → A[1/f]` commute with the restriction maps of
> degree-zero localizations:** the one of `B` attached to `D₊(σ g · ψ g) ⊆ D₊(σ f · ψ f)` on the
> source, the one of `A` attached to `D₊(g) ⊆ D₊(f)` on the target. This is the restriction
> compatibility of the degreewise description of the functions on the punctured cone.

```lean
theorem puncturedToLocalization_degreeZeroRingMap_le
    (hf : ∃ d : ℕ, 0 < d ∧ f ∈ 𝒜 d) (hg : ∃ e : ℕ, 0 < e ∧ g ∈ 𝒜 e)
    (hσψf : ∃ d : ℕ, 0 < d ∧ sigmaMulPsi 𝒜 f ∈ grading 𝒜 d)
    (hσψg : ∃ e : ℕ, 0 < e ∧ sigmaMulPsi 𝒜 g ∈ grading 𝒜 e)
    (hfg : ProjectiveSpectrum.basicOpen 𝒜 g ≤ ProjectiveSpectrum.basicOpen 𝒜 f)
    (hσψfg : ProjectiveSpectrum.basicOpen (grading 𝒜) (sigmaMulPsi 𝒜 g) ≤
      ProjectiveSpectrum.basicOpen (grading 𝒜) (sigmaMulPsi 𝒜 f))
    (z : HomogeneousLocalization.Away (grading 𝒜) (sigmaMulPsi 𝒜 f)) :
    puncturedToLocalization 𝒜
        (ProjectiveSpectrum.degreeZeroRingMap (grading 𝒜) (sigmaMulPsi 𝒜 f) (sigmaMulPsi 𝒜 g)
          hσψf hσψg hσψfg z) =
      ProjectiveSpectrum.localizedRingMap 𝒜 f g hf hg hfg (puncturedToLocalization 𝒜 z)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.basicOpen_sigmaMulPsi_le_of_basicOpen_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalRestriction.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalRestriction.lean#L126). The attribute's comment: “the chart of U over D+(g) is contained in the chart over D+(f), for the truncation cone and an inclusion D+(g) <= D+(f) of standard opens of P”.

> **The chart of `U` over `D₊(g)` is contained in the chart over `D₊(f)`** as soon as
> `D₊(g) ⊆ D₊(f)`: each chart is the part `U ⊓ D₊(ψ ·)` of the punctured cone lying over the
> standard open, and `ψ` carries the inclusion to one of standard opens of `L`.

```lean
theorem basicOpen_sigmaMulPsi_le_of_basicOpen_le {d e : ℕ} (hf : f ∈ 𝒜 d) (hd : 0 < d)
    (hg : g ∈ 𝒜 e) (he : 0 < e)
    (hfg : ProjectiveSpectrum.basicOpen 𝒜 g ≤ ProjectiveSpectrum.basicOpen 𝒜 f) :
    ProjectiveSpectrum.basicOpen (grading 𝒜) (sigmaMulPsi 𝒜 g) ≤
      ProjectiveSpectrum.basicOpen (grading 𝒜) (sigmaMulPsi 𝒜 f)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeTwistAwayHom_degreeZeroRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalRestriction.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedLocalRestriction.lean#L146). The attribute's comment: “the punctured degreewise inclusion of the sections of O\_P(m) into the degree-zero localization of the truncation algebra at sigma f * psi f commutes with restriction between two standard opens, for every integer m”.

> **The punctured degreewise inclusion commutes with restriction between two standard opens,
> read in the degree-zero localizations of the truncation algebra.** On the source the restriction
> of a section of `𝒪_P(m)` is the map of localizations of the shifted regular module, on the target
> it is the degree-zero restriction map of `B`, and the comparison maps to `A[1/g]` identify the
> two.

```lean
theorem puncturedConeTwistAwayHom_degreeZeroRingMap (m : ℤ) {d e : ℕ} (hf : f ∈ 𝒜 d) (hd : 0 < d)
    (hg : g ∈ 𝒜 e) (he : 0 < e)
    (hfg : ProjectiveSpectrum.basicOpen 𝒜 g ≤ ProjectiveSpectrum.basicOpen 𝒜 f)
    (s : (ProjectiveSpectrum.Proj.twistingSheaf 𝒜 m).val.obj
      (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    puncturedConeTwistAwayHom 𝒜 m e hg he
        (((ProjectiveSpectrum.Proj.twistingSheaf 𝒜 m).val.map (homOfLE hfg).op).hom s) =
      ProjectiveSpectrum.degreeZeroRingMap (grading 𝒜) (sigmaMulPsi 𝒜 f) (sigmaMulPsi 𝒜 g)
        ⟨d, hd, sigmaMulPsi_mem_grading 𝒜 d hf⟩ ⟨e, he, sigmaMulPsi_mem_grading 𝒜 e hg⟩
        (basicOpen_sigmaMulPsi_le_of_basicOpen_le 𝒜 hf hd hg he hfg)
        (puncturedConeTwistAwayHom 𝒜 m d hf hd s)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeTwistAwayHom_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedMul.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedMul.lean#L88). The attribute's comment: “the punctured degreewise inclusion of the sections of the twisting sheaves over D+(f) into the degree-zero localization of the truncation algebra at sigma f * psi f is multiplicative, in every pair of integer degrees”.

> **The punctured degreewise inclusion `Γ(D₊(f), 𝒪_P(m)) → (B[1/σ f · ψ f])₀` is
> multiplicative**, in every pair of integer degrees.

```lean
theorem puncturedConeTwistAwayHom_mul (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) (i j : ℤ)
    (x : (twistingSheaf 𝒜 i).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f)))
    (y : (twistingSheaf 𝒜 j).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    puncturedConeTwistAwayHom 𝒜 (i + j) d hf hd
        (twistMulSection 𝒜 i j (op (ProjectiveSpectrum.basicOpen 𝒜 f)) x y) =
      puncturedConeTwistAwayHom 𝒜 i d hf hd x * puncturedConeTwistAwayHom 𝒜 j d hf hd y
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeTwistAwayHom_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedMul.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedMul.lean#L111). The attribute's comment: “the punctured degreewise inclusion of the sections of the untwisted sheaf over D+(f) into the degree-zero localization of the truncation algebra at sigma f * psi f carries the unit section to 1”.

> **The punctured degreewise inclusion `Γ(D₊(f), 𝒪_P(0)) → (B[1/σ f · ψ f])₀` is unital.**

```lean
theorem puncturedConeTwistAwayHom_one (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    puncturedConeTwistAwayHom 𝒜 0 d hf hd
        ((twistOne 𝒜).eval (op (ProjectiveSpectrum.basicOpen 𝒜 f))) = 1
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeTwistApp_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedMul.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedMul.lean#L126). The attribute's comment: “the local punctured degreewise inclusion of the sections of O\_P(m) into the functions on the punctured cone over D+(f) is multiplicative, in every pair of integer degrees”.

> **The local punctured degreewise inclusion on sections is multiplicative**, in every pair of
> integer degrees.

```lean
theorem puncturedConeTwistApp_mul (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) (i j : ℤ)
    (x : (twistingSheaf 𝒜 i).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f)))
    (y : (twistingSheaf 𝒜 j).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    (show puncturedConeSections 𝒜 (ProjectiveSpectrum.basicOpen 𝒜 f) from
        (puncturedConeTwistApp 𝒜 (i + j) d hf hd).hom
          (twistMulSection 𝒜 i j (op (ProjectiveSpectrum.basicOpen 𝒜 f)) x y)) =
      (show puncturedConeSections 𝒜 (ProjectiveSpectrum.basicOpen 𝒜 f) from
          (puncturedConeTwistApp 𝒜 i d hf hd).hom x) *
        (show puncturedConeSections 𝒜 (ProjectiveSpectrum.basicOpen 𝒜 f) from
          (puncturedConeTwistApp 𝒜 j d hf hd).hom y)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeTwistApp_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedMul.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedMul.lean#L148). The attribute's comment: “the local punctured degreewise inclusion in degree zero carries the unit section of the untwisted sheaf to the function 1 on the punctured cone, over a standard open”.

> **The local punctured degreewise inclusion in degree zero carries the unit section to the
> function `1`** on the part of the punctured cone over the standard open.

```lean
theorem puncturedConeTwistApp_one (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    (show puncturedConeSections 𝒜 (ProjectiveSpectrum.basicOpen 𝒜 f) from
        (puncturedConeTwistApp 𝒜 0 d hf hd).hom
          ((twistOne 𝒜).eval (op (ProjectiveSpectrum.basicOpen 𝒜 f)))) = 1
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedTwistHom_mul_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedMul.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedMul.lean#L243). The attribute's comment: “the inclusions of the homogeneous pieces of the integral twist algebra in (pi|\_U)\_* O\_U are multiplicative, over every open of P and in every pair of integer degrees, for the punctured cone of the truncation algebra”.

> **The inclusions of the homogeneous pieces of the algebra of all integral twists in
> `(π|_U)_* 𝒪_U` multiply as the grading prescribes**, over every open of `P` and in every pair of
> integer degrees. This is the `ι_mul` condition of `AlgebraicGeometry.AbstractCone` for the
> punctured cone of the truncation algebra, graded by
> `Stacks.AlgebraicGeometry.ProjConeTwist.integerTwistAlgebra`.

```lean
theorem puncturedTwistHom_mul_app (i j : ℤ) (U : Opens (ProjectiveSpectrum.top 𝒜))
    (a : (twistingSheaf 𝒜 i).val.obj (op U)) (b : (twistingSheaf 𝒜 j).val.obj (op U)) :
    (show puncturedConeSections 𝒜 U from
        (puncturedTwistHom 𝒜 (i + j)).val.app (op U)
          ((twistMul 𝒜 i j).app (op U) a b)) =
      (show puncturedConeSections 𝒜 U from (puncturedTwistHom 𝒜 i).val.app (op U) a) *
        (show puncturedConeSections 𝒜 U from (puncturedTwistHom 𝒜 j).val.app (op U) b)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedTwistHom_one_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedMul.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedMul.lean#L267). The attribute's comment: “the inclusion of the degree-zero piece of the integral twist algebra carries the unit of the algebra to the function 1 on the punctured cone, over every open of P”.

> **The inclusion of the degree-zero piece of the algebra of all integral twists carries the
> unit of that algebra to the function `1`** on the punctured cone, over every open of `P`.

```lean
theorem puncturedTwistHom_one_app (U : Opens (ProjectiveSpectrum.top 𝒜)) :
    (show puncturedConeSections 𝒜 U from
        (puncturedTwistHom 𝒜 0).val.app (op U) ((twistOne 𝒜).eval (op U))) = 1
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeAlgebraSectionsEquivAway`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedPushforward.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedPushforward.lean#L67). The attribute's comment: “the sections of the direct image of the structure sheaf of the punctured cone over a standard open D₊(f) of P are the localization A[1/f]”.

> The sections of the direct image of the structure sheaf of the punctured cone over a standard
> open `D₊(f)` of `P = Proj A` are the localization of `A` at `f`:
> `((π|_U)_* 𝒪_U)(D₊(f)) ≃+* A[1/f]`.

```lean
def puncturedConeAlgebraSectionsEquivAway (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    (puncturedConeAlgebra (truncationConeData 𝒜)).right.obj.obj
        (op (Proj.basicOpen 𝒜 f)) ≃+*
      Localization.Away f
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeAlgebraSectionsRingEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedPushforward.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedPushforward.lean#L82). The attribute's comment: “the footnote computation (π|\_U)\_* O\_U = ⨁\_\{m ∈ ℤ} O\_P(m), over one standard open D₊(f) of P and for the truncation algebra, with the summands written as the homogeneous parts of A[1/f]”.

> The sections of the direct image of the structure sheaf of the punctured cone over a standard
> open `D₊(f)` of `P = Proj A` are the direct sum, over *all* integer degrees, of the homogeneous
> parts of the localization `A[1/f]`: `((π|_U)_* 𝒪_U)(D₊(f)) ≃+* ⨁_{m ∈ ℤ} (A[1/f])_m`.

```lean
def puncturedConeAlgebraSectionsRingEquiv (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    (puncturedConeAlgebra (truncationConeData 𝒜)).right.obj.obj
        (op (Proj.basicOpen 𝒜 f)) ≃+*
      (⨁ m : ℤ, ↥(puncturedGrading 𝒜 d hf m))
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeAlgebraSectionsEquivTwistSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedPushforward.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedPushforward.lean#L98). The attribute's comment: “the footnote computation (π|\_U)\_* O\_U = ⨁\_\{m ∈ ℤ} O\_P(m), over one standard open D₊(f) of P and for the truncation algebra, with the summands written as the sections of the twisting sheaves”.

> The sections of the direct image of the structure sheaf of the punctured cone over a standard
> open `D₊(f)` of `P = Proj A` are the direct sum of the sections of the twisting sheaves over
> `D₊(f)`: `((π|_U)_* 𝒪_U)(D₊(f)) ≃+ ⨁_{m ∈ ℤ} Γ(D₊(f), 𝒪_P(m))`.

```lean
def puncturedConeAlgebraSectionsEquivTwistSections (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    (puncturedConeAlgebra (truncationConeData 𝒜)).right.obj.obj
        (op (Proj.basicOpen 𝒜 f)) ≃+
      (⨁ m : ℤ, ↥((ProjectiveSpectrum.Proj.twistingSheaf 𝒜 m).val.obj
        (op (ProjectiveSpectrum.basicOpen 𝒜 f))))
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneAlgebraSectionsEquivTwistSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedPushforward.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedPushforward.lean#L112). The attribute's comment: “the footnote computation π\_* O\_L = ⨁\_\{m ≥ 0} O\_P(m), over one standard open D₊(f) of P and for the truncation algebra, with the summands written as the sections of the twisting sheaves”.

> The sections of the direct image of the structure sheaf of the cone over a standard open
> `D₊(f)` of `P = Proj A` are the direct sum of the sections of the nonnegative twisting sheaves
> over `D₊(f)`: `(π_* 𝒪_L)(D₊(f)) ≃+ ⨁_{m ≥ 0} Γ(D₊(f), 𝒪_P(m))`.

```lean
def coneAlgebraSectionsEquivTwistSections (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    (coneAlgebra (truncationConeData 𝒜)).right.obj.obj
        (op (Proj.basicOpen 𝒜 f)) ≃+
      (⨁ m : ℕ, ↥((ProjectiveSpectrum.Proj.twistingSheaf 𝒜 (m : ℤ)).val.obj
        (op (ProjectiveSpectrum.basicOpen 𝒜 f))))
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeAlgebraSectionsRingEquiv_symm_of`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedStandardOpenSum.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedStandardOpenSum.lean#L75). The attribute's comment: “the inverse of the standard-open direct-sum decomposition of the functions on the punctured cone carries the m-th summand to the inclusion of a degree-m fraction, for every integer m”.

> **The `m`-th summand of the ring isomorphism
> `Γ(D₊(f), (π|_U)_* 𝒪_U) ≃+* ⨁_{m ∈ ℤ} (A[1/f])_m`.** Read backwards, a degree-`m` element `y` of
> `(B[1/σ f · ψ f])₀` placed in the `m`-th summand is `y` itself, read as a function on
> `D₊(σ f · ψ f)` through the identification of [Stacks, Tag 01M6] and restricted to the chart of
> `U` over `D₊(f)`.

```lean
theorem puncturedConeAlgebraSectionsRingEquiv_symm_of (m : ℤ) (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d)
    (y : puncturedGrading 𝒜 d hf m) :
    (puncturedConeAlgebraSectionsRingEquiv 𝒜 d hf hd).symm
        (DirectSum.of (fun k : ℤ => ↥(puncturedGrading 𝒜 d hf k)) m y) =
      (eqToHom (puncturedConeAlgebra_sections_basicOpen 𝒜 d hf hd).symm).hom
        ((AlgebraicGeometry.Proj.awayToSection (grading 𝒜) (sigmaMulPsi 𝒜 f)).hom
          (y : HomogeneousLocalization.Away (grading 𝒜) (sigmaMulPsi 𝒜 f)))
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeAlgebraSectionsEquivTwistSections_symm_of`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedStandardOpenSum.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedStandardOpenSum.lean#L104). The attribute's comment: “the m-th summand of the standard-open direct-sum decomposition of the functions on the punctured cone is the local degreewise inclusion of the sections of O\_P(m), for the truncation cone and every integer m”.

> **The `m`-th summand of the standard-open decomposition
> `Γ(D₊(f), (π|_U)_* 𝒪_U) = ⨁_{m ∈ ℤ} Γ(D₊(f), 𝒪_P(m))` is the local degreewise inclusion
> `Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeTwistApp`.** This identifies the footnote
> computation of [Stacks, Tag 0EKG] over one standard open with the local datum the morphism
> `𝒪_P(m) ⟶ (π|_U)_* 𝒪_U` of sheaves of `𝒪_P`-modules is glued from.

```lean
theorem puncturedConeAlgebraSectionsEquivTwistSections_symm_of (m : ℤ) (d : ℕ) (hf : f ∈ 𝒜 d)
    (hd : 0 < d)
    (s : (ProjectiveSpectrum.Proj.twistingSheaf 𝒜 m).val.obj
      (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    (puncturedConeAlgebraSectionsEquivTwistSections 𝒜 d hf hd).symm (DirectSum.of _ m s) =
      (puncturedConeTwistApp 𝒜 m d hf hd).hom s
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedTotalMap_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedTotalRing.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedTotalRing.lean#L158). The attribute's comment: “the comparison from the objectwise direct sum of the twisting sheaves to the functions on the punctured cone is multiplicative, over every open of P”.

> **The map is multiplicative.**

```lean
theorem puncturedTotalMap_mul (V : Opens (ProjectiveSpectrum.top 𝒜))
    (z w : (integerTwistPresheafAlgebra 𝒜).Total (op V)) :
    puncturedTotalMap 𝒜 V (z * w) = puncturedTotalMap 𝒜 V z * puncturedTotalMap 𝒜 V w
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedTotalRingHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedTotalRing.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPuncturedTotalRing.lean#L174). The attribute's comment: “the degreewise inclusions as a ring homomorphism from the sections of the ungraded realization of the integral twist algebra to the functions on the punctured cone, over every open of P, for the truncation cone”.

> **The degreewise inclusions as a ring homomorphism
> `Γ(V, ⨁_{m ∈ ℤ} 𝒪_P(m)) →+* Γ(U, (π|_U)⁻¹V)`.** The sections of the ungraded realization of the
> algebra of all integral twists over `V` map to the functions on the part of the punctured cone
> lying over `V`, degreewise by the inclusion of the twisting sheaf.

```lean
def puncturedTotalRingHom (V : Opens (ProjectiveSpectrum.top 𝒜)) :
    (integerTwistPresheafAlgebra 𝒜).Total (op V) →+* puncturedConeSections 𝒜 V
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneAlgebraSectionsRingEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPushforward.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistPushforward.lean#L55). The attribute's comment: “the footnote computation π\_* O\_L = ⨁\_\{m ≥ 0} O\_P(m), over one standard open D₊(f) of P and for the truncation algebra, with the summands written as the homogeneous parts of A[1/f]”.

> The sections of the direct image of the structure sheaf of the cone over a standard open
> `D₊(f)` of `P = Proj A` are the direct sum, over the nonnegative degrees, of the homogeneous parts
> of the localization `A[1/f]`: `(π_* 𝒪_L)(D₊(f)) ≃+* ⨁_{m ≥ 0} (A[1/f])_m`.

```lean
def coneAlgebraSectionsRingEquiv (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    (coneAlgebra (truncationConeData 𝒜)).right.obj.obj (op (Proj.basicOpen 𝒜 f)) ≃+*
      (⨁ m : ℕ, ↥(awayGrading 𝒜 d hf m))
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedToConeRelativeSpecTwistAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean#L94). The attribute's comment: “the top-left arrow of the diagram, the morphism of relative spectra over P induced by the inclusion of the nonnegative twist algebra in the integral one”.

> The morphism `Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) ⟶ Spec_P(⨁_{m ≥ 0} 𝒪_P(m))` over `P = Proj A`
> induced by the inclusion `⨁_{m ≥ 0} 𝒪_P(m) ↪ ⨁_{m ∈ ℤ} 𝒪_P(m)` of
> `Stacks.AlgebraicGeometry.ProjConeTwist.nonnegToIntegerTwistAlgebraSheafHom`.

```lean
def puncturedToConeRelativeSpecTwistAlgebra :
    Over.mk (relativeSpecToBase (integerTwistAlgebraSheaf 𝒜)) ⟶
      Over.mk (relativeSpecToBase (nonnegTwistAlgebraSheaf 𝒜))
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedToConeRelativeSpecTwistAlgebra_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean#L105). The attribute's comment: “the top-left arrow of the diagram is the open immersion of the punctured cone in the cone, under the two presentations as relative spectra, as morphisms over P”.

> The morphism `Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) ⟶ Spec_P(⨁_{m ≥ 0} 𝒪_P(m))` is the open immersion
> of the punctured cone in the cone, under the two presentations `L = Spec_P(⨁_{m ≥ 0} 𝒪_P(m))`
> and `U = Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m))`, as morphisms over `P = Proj A`.

```lean
theorem puncturedToConeRelativeSpecTwistAlgebra_comp :
    puncturedToConeRelativeSpecTwistAlgebra 𝒜 ≫ (coneRelativeSpecTwistAlgebraIso 𝒜).inv =
      (puncturedConeRelativeSpecTwistAlgebraIso 𝒜).inv ≫ openUInLOver 𝒜
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedToConeRelativeSpecTwistAlgebra_left_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean#L146). The attribute's comment: “the left square of the diagram commutes: the top-left arrow followed by L → X is the left identification with U followed by the inclusion of U in X”. References: EGA II (8.6.2), “special case”.

> The morphism `Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) ⟶ Spec_P(⨁_{m ≥ 0} 𝒪_P(m)) = L` followed by the
> structure morphism `σ : L ⟶ X` is the identification `Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) ≅ U` of
> `Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeRelativeSpecTwistAlgebraIsoOpenU` followed
> by the inclusion `U ⟶ X`.

```lean
theorem puncturedToConeRelativeSpecTwistAlgebra_left_comp :
    (puncturedToConeRelativeSpecTwistAlgebra 𝒜).left ≫
        (coneRelativeSpecTwistAlgebraIso 𝒜).inv.left ≫ toSpecA 𝒜 =
      (puncturedConeRelativeSpecTwistAlgebraIsoOpenU 𝒜).hom ≫ (ProjAndSpec.openU 𝒜).ι
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneProjIsoRelativeSpecTwistAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean#L160). The attribute's comment: “L = Proj B is, as a scheme, the relative spectrum over P of the nonnegative twist algebra”.

> The cone `L = Proj B` of the truncation algebra `B = ⨁_{d ≥ 0} A_{≥ d}` is, as a scheme, the
> relative spectrum over `P = Proj A` of the algebra of nonnegative twists.

```lean
def coneProjIsoRelativeSpecTwistAlgebra :
    AlgebraicGeometry.Proj (grading 𝒜) ≅
      Stacks.AffineAlgebraEquivalence.relativeSpec (nonnegTwistAlgebraSheaf 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneProjIsoRelativeSpecTwistAlgebra_hom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean#L169). The attribute's comment: “the identification of L = Proj B with the relative spectrum of the nonnegative twist algebra is one over P, as morphisms of schemes”.

> The identification `L = Proj B ≅ Spec_P(⨁_{m ≥ 0} 𝒪_P(m))` is one over `P`: followed by the
> structure morphism of the relative spectrum it is the cone projection `π : L ⟶ P`.

```lean
theorem coneProjIsoRelativeSpecTwistAlgebra_hom_comp :
    (coneProjIsoRelativeSpecTwistAlgebra 𝒜).hom ≫
        relativeSpecToBase (nonnegTwistAlgebraSheaf 𝒜) =
      pi 𝒜
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneRelativeSpecIsoTwistAlgebraViaDirectImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean#L190). The attribute's comment: “L is, over P, the relative spectrum of the nonnegative twist algebra by the route of the diagram: the presentation of L as the relative spectrum of pi\_* O\_L composed with the comparison of pi\_* O\_L with the direct sum of the twists O\_P(m) over m at least 0”. References: EGA II (8.7.3), “partial”.

> `L ≅ Spec_P(⨁_{m ≥ 0} 𝒪_P(m))` over `P`, as the presentation of the cone as the relative
> spectrum of its direct-image algebra `π_* 𝒪_L`
> (`Stacks.AlgebraicGeometry.ProjConeTwist.coneRelativeSpecIso`) followed by the comparison
> `Stacks.AlgebraicGeometry.ProjConeTwist.coneAlgebraSheafIso` of `π_* 𝒪_L` with the algebra of
> nonnegative twists.

```lean
def coneRelativeSpecIsoTwistAlgebraViaDirectImage :
    Over.mk (pi 𝒜) ≅ Over.mk (relativeSpecToBase (nonnegTwistAlgebraSheaf 𝒜))
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneRelativeSpecIsoTwistAlgebraViaDirectImage_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean#L201). The attribute's comment: “the route through pi\_* O\_L is the one-step identification of L with the relative spectrum of the nonnegative twist algebra”.

> The identification of `L` with `Spec_P(⨁_{m ≥ 0} 𝒪_P(m))` through `π_* 𝒪_L` is
> `Stacks.AlgebraicGeometry.ProjConeTwist.coneRelativeSpecTwistAlgebraIso`.

```lean
theorem coneRelativeSpecIsoTwistAlgebraViaDirectImage_eq :
    coneRelativeSpecIsoTwistAlgebraViaDirectImage 𝒜 = coneRelativeSpecTwistAlgebraIso 𝒜
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedToConeRelativeSpecTwistAlgebra_left_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean#L234). The attribute's comment: “the top-left arrow of the diagram, as a morphism of schemes, is the open immersion of the punctured cone in L conjugated by the two relative-spectrum identifications”.

> As a morphism of schemes, `Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) ⟶ Spec_P(⨁_{m ≥ 0} 𝒪_P(m))` is the
> identification `Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) ≅ U`, then the open immersion `U ⟶ L`, then the
> identification `L ≅ Spec_P(⨁_{m ≥ 0} 𝒪_P(m))`.

```lean
theorem puncturedToConeRelativeSpecTwistAlgebra_left_eq :
    (puncturedToConeRelativeSpecTwistAlgebra 𝒜).left =
      ((Over.forget (AlgebraicGeometry.Proj 𝒜)).mapIso
            (puncturedConeRelativeSpecTwistAlgebraIso 𝒜)).inv ≫
        (openUInL 𝒜).ι ≫ (coneProjIsoRelativeSpecTwistAlgebra 𝒜).hom
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.isOpenImmersion_puncturedToConeRelativeSpecTwistAlgebra_left`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean#L245). The attribute's comment: “the top-left arrow of the diagram is an open immersion of schemes”.

> The morphism `Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) ⟶ Spec_P(⨁_{m ≥ 0} 𝒪_P(m))` is an open immersion of
> schemes.

```lean
instance isOpenImmersion_puncturedToConeRelativeSpecTwistAlgebra_left :
    IsOpenImmersion (puncturedToConeRelativeSpecTwistAlgebra 𝒜).left
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.opensRange_puncturedToConeRelativeSpecTwistAlgebra_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean#L259). The attribute's comment: “the image in L = Proj B of the top-left arrow of the diagram, read through the identification of L with the relative spectrum, is the open punctured cone”.

> Read through the identification of `L = Proj B` with `Spec_P(⨁_{m ≥ 0} 𝒪_P(m))`, the
> morphism `Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) ⟶ L` has image the punctured cone
> `Stacks.AlgebraicGeometry.ProjAndSpecTruncation.openUInL`.

```lean
theorem opensRange_puncturedToConeRelativeSpecTwistAlgebra_left :
    ((puncturedToConeRelativeSpecTwistAlgebra 𝒜).left ≫
        (coneProjIsoRelativeSpecTwistAlgebra 𝒜).inv).opensRange = openUInL 𝒜
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedToConeProj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean#L278). The attribute's comment: “the top-left arrow of the diagram as a morphism of schemes whose target is the cone L = Proj B”.

> The morphism `Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) ⟶ L = Proj B` of schemes: the morphism of relative
> spectra over `P` read on underlying schemes, followed by the identification
> `Spec_P(⨁_{m ≥ 0} 𝒪_P(m)) ≅ Proj B` of
> `Stacks.AlgebraicGeometry.ProjConeTwist.coneProjIsoRelativeSpecTwistAlgebra`.

```lean
def puncturedToConeProj :
    Stacks.AffineAlgebraEquivalence.relativeSpec (integerTwistAlgebraSheaf 𝒜) ⟶
      AlgebraicGeometry.Proj (grading 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedConeRelativeSpecTwistAlgebraIsoOpenUOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean#L308). The attribute's comment: “the left square as an isomorphism over X: the left identification of Spec\_P of the integer twist algebra with U is an isomorphism of schemes over X, its source lying over X by the top-left arrow followed by L → X”. References: EGA II (8.12.5), “special case”; EGA II (8.6.2), “special case”.

> The identification `Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) ≅ U` as an isomorphism of schemes over
> `X = Spec A`, the source lying over `X` by the morphism to `L` followed by `σ : L ⟶ X` and the
> target by the inclusion `U ⟶ X`.

```lean
def puncturedConeRelativeSpecTwistAlgebraIsoOpenUOver :
    Over.mk (puncturedToConeProj 𝒜 ≫ toSpecA 𝒜) ≅ Over.mk (ProjAndSpec.openU 𝒜).ι
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.puncturedToConeProjOverSpecA`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistRelativeSpecInclusion.lean#L319). The attribute's comment: “the left square as a morphism over X: the top-left arrow of the diagram is a morphism of schemes over X, its source lying over X by the left identification with U followed by the inclusion of U in X”.

> The morphism `Spec_P(⨁_{m ∈ ℤ} 𝒪_P(m)) ⟶ L = Proj B` as a morphism of schemes over
> `X = Spec A`, the source lying over `X` by the identification with `U` followed by the inclusion
> `U ⟶ X` and the cone by `σ : L ⟶ X`.

```lean
def puncturedToConeProjOverSpecA :
    Over.mk ((puncturedConeRelativeSpecTwistAlgebraIsoOpenU 𝒜).hom ≫
        (ProjAndSpec.openU 𝒜).ι) ⟶
      Over.mk (toSpecA 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coe_associatedModuleSheafStandardOpenEquiv_twistMul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistStandardOpenMul.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistStandardOpenMul.lean#L152). The attribute's comment: “the standard-open identification of the sections of a twisting sheaf with the degree-zero fractions carries the product of two twists to the product of the fractions”.

> The standard-open identification `Γ(D₊(f), 𝒪_P(i)) = (A[1/f])_i` carries the product of two
> twists to the product of their fractions.

```lean
theorem coe_associatedModuleSheafStandardOpenEquiv_twistMul {d : ℕ} (hf : f ∈ 𝒜 d) (hd : 0 < d)
    (i j : ℤ)
    (x : (twistingSheaf 𝒜 i).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f)))
    (y : (twistingSheaf 𝒜 j).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    ((associatedModuleSheafStandardOpenEquiv 𝒜 (twistGrading (S := A) 𝒜 (i + j)) hf hd
          (twistMulSection 𝒜 i j (op (ProjectiveSpectrum.basicOpen 𝒜 f)) x y) :
        LocalizedModule.Away f A)) =
      (associatedModuleSheafStandardOpenEquiv 𝒜 (twistGrading (S := A) 𝒜 i) hf hd x :
          LocalizedModule.Away f A) *
        (associatedModuleSheafStandardOpenEquiv 𝒜 (twistGrading (S := A) 𝒜 j) hf hd y :
          LocalizedModule.Away f A)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coe_sectionsTwistEquivAwayGrading_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistStandardOpenMul.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistStandardOpenMul.lean#L195). The attribute's comment: “the identification of the sections of a twisting sheaf over a standard open with a homogeneous part of the localization is multiplicative”.

> The identification of the sections of `𝒪_P(i)` over `D₊(f)` with the degree-`i` part of
> `A[1/f]` is multiplicative.

```lean
theorem coe_sectionsTwistEquivAwayGrading_mul {d : ℕ} (hf : f ∈ 𝒜 d) (hd : 0 < d) (i j : ℤ)
    (x : (twistingSheaf 𝒜 i).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f)))
    (y : (twistingSheaf 𝒜 j).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    ((Stacks.ProjectiveCohomology.sectionsTwistEquivAwayGrading 𝒜 hf hd (i + j)
          (twistMulSection 𝒜 i j (op (ProjectiveSpectrum.basicOpen 𝒜 f)) x y) :
        LocalizedModule.Away f A)) =
      (Stacks.ProjectiveCohomology.sectionsTwistEquivAwayGrading 𝒜 hf hd i x :
          LocalizedModule.Away f A) *
        (Stacks.ProjectiveCohomology.sectionsTwistEquivAwayGrading 𝒜 hf hd j y :
          LocalizedModule.Away f A)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistAwayHom_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistStandardOpenMul.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistStandardOpenMul.lean#L252). The attribute's comment: “the degreewise inclusion of the sections of the twisting sheaves over D+(f) into the degree-zero localization of the truncation algebra is multiplicative”.

> The degreewise inclusion `Γ(D₊(f), 𝒪_P(m)) → (B[1/ψ f])₀` is multiplicative: the product
> of a section of `𝒪_P(i)` and one of `𝒪_P(j)` goes to the product of their images.

```lean
theorem coneTwistAwayHom_mul (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) (i j : ℕ)
    (x : (twistingSheaf 𝒜 (i : ℤ)).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f)))
    (y : (twistingSheaf 𝒜 (j : ℤ)).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    coneTwistAwayHom 𝒜 (i + j) d hf hd
        (natTwistMulSection 𝒜 i j (op (ProjectiveSpectrum.basicOpen 𝒜 f)) x y) =
      coneTwistAwayHom 𝒜 i d hf hd x * coneTwistAwayHom 𝒜 j d hf hd y
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistApp_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistStandardOpenMul.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistStandardOpenMul.lean#L270). The attribute's comment: “the local degreewise inclusion of the sections of O\_P(m) into the functions on the cone over D+(f) is multiplicative, for the truncation cone”.

> The local degreewise inclusion `Γ(D₊(f), 𝒪_P(m)) ⟶ Γ(D₊(f), π_* 𝒪_L)` is
> multiplicative.

```lean
theorem coneTwistApp_mul (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) (i j : ℕ)
    (x : (twistingSheaf 𝒜 (i : ℤ)).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f)))
    (y : (twistingSheaf 𝒜 (j : ℤ)).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    (show (AlgebraicGeometry.Proj (grading 𝒜)).presheaf.obj
          (op (pi 𝒜 ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen 𝒜 f)) from
        (coneTwistApp 𝒜 (i + j) d hf hd).hom
          (natTwistMulSection 𝒜 i j (op (ProjectiveSpectrum.basicOpen 𝒜 f)) x y)) =
      (show (AlgebraicGeometry.Proj (grading 𝒜)).presheaf.obj
            (op (pi 𝒜 ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen 𝒜 f)) from
          (coneTwistApp 𝒜 i d hf hd).hom x) *
        (show (AlgebraicGeometry.Proj (grading 𝒜)).presheaf.obj
            (op (pi 𝒜 ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen 𝒜 f)) from
          (coneTwistApp 𝒜 j d hf hd).hom y)
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneAlgebraSectionsRingEquiv_symm_of`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistStandardOpenSum.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistStandardOpenSum.lean#L53). The attribute's comment: “the inverse of the standard-open direct-sum decomposition of the functions on the cone carries the m-th summand to the inclusion of a degree-m fraction”.

> The inverse of the ring isomorphism `(π_* 𝒪_L)(D₊(f)) ≃+* ⨁_{m ≥ 0} (A[1/f])_m` sends a
> degree-`m` element `y` of `(B[1/ψ f])₀`, placed in the `m`-th summand, to `y` read as a function
> on `D₊(ψ f)` by `AlgebraicGeometry.Proj.awayToSection` and transported along
> `π⁻¹(D₊(f)) = D₊(ψ f)`.

```lean
theorem coneAlgebraSectionsRingEquiv_symm_of (m d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d)
    (y : awayGrading 𝒜 d hf m) :
    (coneAlgebraSectionsRingEquiv 𝒜 d hf hd).symm
        (DirectSum.of (fun k : ℕ => ↥(awayGrading 𝒜 d hf k)) m y) =
      (eqToHom (coneAlgebra_sections_basicOpen 𝒜 d hf hd).symm).hom
        ((AlgebraicGeometry.Proj.awayToSection (grading 𝒜) (psi 𝒜 f)).hom
          (y : HomogeneousLocalization.Away (grading 𝒜) (psi 𝒜 f)))
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneAlgebraSectionsEquivTwistSections_symm_of`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistStandardOpenSum.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistStandardOpenSum.lean#L78). The attribute's comment: “the m-th summand of the standard-open direct-sum decomposition of the functions on the cone is the local degreewise inclusion of the sections of O\_P(m), for the truncation cone”.

> The inclusion of the `m`-th summand of the standard-open decomposition
> `Γ(D₊(f), π_* 𝒪_L) = ⨁_{m ≥ 0} Γ(D₊(f), 𝒪_P(m))` is the degreewise inclusion
> `Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistApp`.

```lean
theorem coneAlgebraSectionsEquivTwistSections_symm_of (m d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d)
    (s : (ProjectiveSpectrum.Proj.twistingSheaf 𝒜 (m : ℤ)).val.obj
      (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    (coneAlgebraSectionsEquivTwistSections 𝒜 d hf hd).symm (DirectSum.of _ m s) =
      (coneTwistApp 𝒜 m d hf hd).hom s
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTotalMap_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistTotalRing.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistTotalRing.lean#L134). The attribute's comment: “the comparison from the objectwise direct sum of the homogeneous pieces of the nonnegative twist algebra to the functions on the cone is multiplicative, over every open of P”.

> **The map is multiplicative.**

```lean
theorem coneTotalMap_mul (U : Opens (ProjectiveSpectrum.top 𝒜))
    (z w : (nonnegTwistPresheafAlgebra 𝒜).Total (op U)) :
    coneTotalMap 𝒜 U (z * w) = coneTotalMap 𝒜 U z * coneTotalMap 𝒜 U w
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTotalRingHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistTotalRing.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistTotalRing.lean#L156). The attribute's comment: “the degreewise inclusions as a ring homomorphism from the sections of the ungraded realization of the nonnegative twist algebra to the functions on the cone, over every open of P, for the truncation cone”.

> **The degreewise inclusions as a ring homomorphism `Γ(U, ⨁_{m ≥ 0} 𝒪_P(m)) →+* Γ(L, π⁻¹U)`.**
> The sections of the ungraded realization of the algebra of nonnegative twists over `U` map to the
> functions on the part of the cone lying over `U`, degreewise by the inclusion of the homogeneous
> piece.

```lean
def coneTotalRingHom (U : Opens (ProjectiveSpectrum.top 𝒜)) :
    (nonnegTwistPresheafAlgebra 𝒜).Total (op U) →+* coneSections 𝒜 U
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTotalPresheafHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistUngradedSheaf.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistUngradedSheaf.lean#L97). The attribute's comment: “the degreewise inclusions as a morphism of presheaves of rings from the ungraded realization of the nonnegative twist algebra to pi\_* O\_L, for the truncation cone”.

> **The degreewise inclusions as a morphism of presheaves of rings** from the ungraded
> realization of the algebra of nonnegative twists into `π_* 𝒪_L`. Over an open of `P` it is the
> ring homomorphism `Stacks.AlgebraicGeometry.ProjConeTwist.coneTotalRingHom`; naturality is the
> naturality of `Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistDirectSumHom`.

```lean
def coneTotalPresheafHom :
    (nonnegTwistPresheafAlgebra 𝒜).totalPresheaf ⟶ (conePushforwardRingSheaf 𝒜).obj
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneUngradedSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistUngradedSheaf.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistUngradedSheaf.lean#L133). The attribute's comment: “the identification pi\_* O\_L = the ungraded realization of the nonnegative twist algebra, as sheaves of rings, for the cone of the truncation algebra”.

> **`π_* 𝒪_L` is the ungraded realization of the algebra of nonnegative twists**, as sheaves of
> rings. This is the identification of [Stacks, Tag 0EKG] at the level of sheaves of rings, as
> opposed to the identification `coneStructureCoproductIso` of the underlying sheaves of
> `𝒪_P`-modules.

```lean
def coneUngradedSheafIso :
    (nonnegTwistAlgebra 𝒜).ungradedSheaf ≅ conePushforwardRingSheaf 𝒜
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coe_sectionsTwistEquivAwayGrading_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistUnit.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistUnit.lean#L107). The attribute's comment: “the standard-open identification of the sections of the untwisted sheaf with the degree-zero fractions carries the unit section to 1”.

> **The standard-open identification carries the unit section of `𝒪_P(0)` to `1`.**

```lean
theorem coe_sectionsTwistEquivAwayGrading_one {d : ℕ} (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    ((Stacks.ProjectiveCohomology.sectionsTwistEquivAwayGrading 𝒜 hf hd 0
          ((twistOne 𝒜).eval (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
        LocalizedModule.Away f A)) = 1
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistAwayHom_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistUnit.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistUnit.lean#L129). The attribute's comment: “the degreewise inclusion of the sections of the untwisted sheaf over D+(f) into the degree-zero localization of the truncation algebra carries the unit section to 1”.

> **The degreewise inclusion `Γ(D₊(f), 𝒪_P(0)) → (B[1/ψ f])₀` is unital.**

```lean
theorem coneTwistAwayHom_one (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    coneTwistAwayHom 𝒜 0 d hf hd ((twistOne 𝒜).eval
        (op (ProjectiveSpectrum.basicOpen 𝒜 f))) = 1
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneTwistApp_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistUnit.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistUnit.lean#L144). The attribute's comment: “the local degreewise inclusion in degree zero carries the unit section of the untwisted sheaf to the function 1 on the cone, over a standard open”.

> **The local degreewise inclusion in degree zero carries the unit section to the function
> `1`** on the part of the cone over the standard open.

```lean
theorem coneTwistApp_one (d : ℕ) (hf : f ∈ 𝒜 d) (hd : 0 < d) :
    (show coneSections 𝒜 (ProjectiveSpectrum.basicOpen 𝒜 f) from
        (coneTwistApp 𝒜 0 d hf hd).hom
          ((twistOne 𝒜).eval (op (ProjectiveSpectrum.basicOpen 𝒜 f)))) = 1
```

**`Stacks.AlgebraicGeometry.ProjConeTwist.coneIota_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistUnit.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjConeTwistUnit.lean#L178). The attribute's comment: “the inclusion of the degree-zero piece of the nonnegative twist algebra carries the unit of the algebra to the function 1, over every open of P, for the truncation cone”.

> **The inclusion of the degree-zero piece of the algebra of nonnegative twists carries the
> unit of that algebra to the function `1`**, over every open of `P`. With
> `Stacks.AlgebraicGeometry.ProjConeTwist.coneIota_mul` this exhibits the inclusions as a unital
> ring homomorphism out of the ungraded realization of the twist algebra.

```lean
theorem coneIota_one (U : Opens (ProjectiveSpectrum.top 𝒜)) :
    (show coneSections 𝒜 U from
        (coneIota 𝒜 0).val.app (op U) ((twistOne 𝒜).eval (op U))) = 1
```

**`Stacks.AlgebraicGeometry.ProjTwistAwayPiece.coe_sectionsTwistEquivGradedPiece_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistAwayPieceScalars.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjTwistAwayPieceScalars.lean#L78). The attribute's comment: “the description of the sections of a twisting sheaf over a standard open as a homogeneous piece of the graded localization is multiplicative”.

> The identification `Γ(D₊(f), 𝒪_X(n)) ≅ (A_f)_n` is multiplicative: the product of a section
> of `𝒪_X(i)` and a section of `𝒪_X(j)` over `D₊(f)`, read in `(A_f)_{i + j}`, is the product in
> `A_f` of the two underlying elements.

```lean
theorem coe_sectionsTwistEquivGradedPiece_mul (hf : f ∈ 𝒜 k) (hk : 0 < k) (i j : ℤ)
    (x : (twistingSheaf 𝒜 i).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f)))
    (y : (twistingSheaf 𝒜 j).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))) :
    ((sectionsTwistEquivGradedPiece 𝒜 hf hk (i + j)
          (Stacks.AlgebraicGeometry.ProjConeTwist.twistMulSection 𝒜 i j
            (op (ProjectiveSpectrum.basicOpen 𝒜 f)) x y) :
        LocalizedModule.Away f A))
      = (sectionsTwistEquivGradedPiece 𝒜 hf hk i x : LocalizedModule.Away f A) *
        (sectionsTwistEquivGradedPiece 𝒜 hf hk j y : LocalizedModule.Away f A)
```

**`Stacks.Truncation.instGradedRingGrading`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Truncation.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Truncation.lean#L320). The attribute's comment: “the graded ring B = ⨁\_\{d ≥ 0} A\_\{≥ d}”.

> `B = ⨁_{d ≥ 0} A_{≥ d}` is a graded ring with degree-`d` part `B_d ≃ A_{≥ d}`.

```lean
instance instGradedRingGrading : GradedRing (grading 𝒜)
```

**`Stacks.Truncation.sigma`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Truncation.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Truncation.lean#L348). The attribute's comment: “the isomorphism σ : A ≃ B₀”.

> The ring isomorphism `σ : A ≃+* B_0`, `a ↦ a⁽⁰⁾`.

```lean
def sigma : A ≃+* grading 𝒜 0
```

**`Stacks.Truncation.psi`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Truncation.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Truncation.lean#L401). The attribute's comment: “the graded ring map ψ : A → B”.

> The graded ring map `ψ : A → B` with `ψ(a) = a⁽ᵈ⁾` for `a ∈ A_d`.

```lean
def psi : 𝒜 →+*ᵍ grading 𝒜
```

**`Stacks.Truncation.tau`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Truncation.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Truncation.lean#L436). The attribute's comment: “the graded ring map τ : B → A”.

> The surjective graded ring map `τ : B → A` with `τ(a⁽ᵈ⁾) = a_d`.

```lean
def tau : grading 𝒜 →+*ᵍ 𝒜
```

**`Stacks.Truncation.truncationAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Truncation.lean, line 494](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Truncation.lean#L494). The attribute's comment: “the graded ring B and the maps σ, ψ, τ”.

> The graded ring `B = ⨁_{d ≥ 0} A_{≥ d}` with its canonical maps `σ`, `ψ` and `τ`.

```lean
def truncationAlgebra : TruncationAlgebra 𝒜
```

**`Stacks.Truncation.tau_comp_psi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Truncation.lean, line 510](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Truncation.lean#L510). The attribute's comment: “τ ∘ ψ = id”.

> `τ ∘ ψ = id_A`.

```lean
theorem tau_comp_psi : s.tau.comp s.psi = GradedRingHom.id 𝒜
```

**`Stacks.Truncation.tau_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Truncation.lean, line 524](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Truncation.lean#L524). The attribute's comment: “τ is surjective”.

> `τ` is surjective.

```lean
theorem tau_surjective : Function.Surjective s.tau
```

**`Stacks.Truncation.truncationAlgebra_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Truncation.lean, line 632](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Truncation.lean#L632). The attribute's comment: “uniqueness of the graded ring B”.

> Two truncation algebras are isomorphic by a unique ring isomorphism compatible with the
> identifications `A_{≥ d} ≃+ B_d`.

```lean
theorem truncationAlgebra_unique :
    ∃! e : s.B ≃+* t.B, ∀ (d : ℕ) (a : truncation 𝒜 d),
      e ((s.degreeEquiv d a : s.B)) = ((t.degreeEquiv d a : t.B))
```

**`Stacks.Truncation.isInternal_awayGrading`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationGraded.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationGraded.lean#L149). The attribute's comment: “the equality of homogeneous parts (B[1/ψ f])\_0 = ⨁\_\{m ≥ 0} (A[1/f])\_m, the ring-theoretic form of the identification of π\_* O\_L with the sum of the nonnegative twists”.

> `(B_{ψ f})₀ = ⨁_{m ≥ 0} (A_f)_m`: the degree-zero part of the localization of the
> truncation algebra at `ψ f` is the internal direct sum of its homogeneous pieces, which the
> comparison map identifies with the homogeneous parts of `A_f` in nonnegative degrees.

```lean
theorem isInternal_awayGrading (hf : f ∈ 𝒜 d) :
    DirectSum.IsInternal (awayGrading 𝒜 d hf)
```

**`Stacks.Truncation.awayGradingEquivAwayPiece`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationGraded.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationGraded.lean#L183). The attribute's comment: “the degree-m piece of (B[1/ψ f])\_0 is (A[1/f])\_m”.

> The degree-`m` piece of `(B_{ψ f})₀` is the degree-`m` part `(A_f)_m` of `A_f`.

```lean
def awayGradingEquivAwayPiece (hf : f ∈ 𝒜 d) (m : ℕ) :
    awayGrading 𝒜 d hf m ≃+ awayPiece 𝒜 d hf m
```

**`Stacks.Truncation.puncturedRingEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationPunctured.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationPunctured.lean#L211). The attribute's comment: “the equality of rings (B[1/σ f · ψ f])\_0 = A[1/f], the functions on the punctured cone over a standard open D₊(f) of P”.

> `(B[1/σ f · ψ f])₀ = A[1/f]`: the degree-zero part of the localization of the truncation
> algebra at `σ f · ψ f` is the whole localization of `A` at `f`, the comparison map
> `a⁽ᵏᵈ⁾ / (σ f · ψ f)ᵏ ↦ a / f ²ᵏ` being a ring isomorphism.

```lean
def puncturedRingEquiv (hf : f ∈ 𝒜 d) :
    HomogeneousLocalization.Away (grading 𝒜) (sigmaMulPsi 𝒜 f) ≃+* Localization.Away f
```

**`Stacks.Truncation.isInternal_puncturedGrading`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationPunctured.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationPunctured.lean#L298). The attribute's comment: “the equality of homogeneous parts (B[1/σ f · ψ f])\_0 = ⨁\_\{m ∈ ℤ} (A[1/f])\_m, the ring-theoretic form of the identification of the direct image of the structure sheaf of the punctured cone with the sum of all the integral twists”.

> `(B[1/σ f · ψ f])₀ = ⨁_{m ∈ ℤ} (A[1/f])_m`: the degree-zero part of the localization of the
> truncation algebra at `σ f · ψ f` is the internal direct sum of its homogeneous pieces, which the
> comparison map identifies with the homogeneous parts of `A[1/f]` in all integer degrees.

```lean
theorem isInternal_puncturedGrading (hf : f ∈ 𝒜 d) :
    DirectSum.IsInternal (puncturedGrading 𝒜 d hf)
```

**`Stacks.Truncation.puncturedGradingEquivAwayGrading`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationPunctured.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationPunctured.lean#L342). The attribute's comment: “the degree-m piece of (B[1/σ f · ψ f])\_0 is (A[1/f])\_m, for every integer m”.

> The degree-`m` piece of `(B[1/σ f · ψ f])₀` is the degree-`m` part of `A[1/f]`, for every
> integer `m`.

```lean
def puncturedGradingEquivAwayGrading (hf : f ∈ 𝒜 d) (m : ℤ) :
    puncturedGrading 𝒜 d hf m ≃+ Stacks.ProjectiveCohomology.awayGrading 𝒜 hf m
```

**`Stacks.Truncation.awayGradingEquivSectionsTwist`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationPunctured.lean, line 387](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationPunctured.lean#L387). The attribute's comment: “the degree-m summand of the functions on the cone over D₊(f) is the module of sections of O\_P(m) over D₊(f), for m ≥ 0”.

> The degree-`m` summand of `(B[1/ψ f])₀` is the module of sections of the twisting sheaf
> `𝒪_P(m)` over `D₊(f)`, for `m ≥ 0`.

```lean
def awayGradingEquivSectionsTwist (hf : f ∈ 𝒜 d) (hd : 0 < d) (m : ℕ) :
    awayGrading 𝒜 d hf m ≃+
      (twistingSheaf 𝒜 (m : ℤ)).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))
```

**`Stacks.Truncation.puncturedGradingEquivSectionsTwist`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationPunctured.lean, line 397](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/TruncationLocalizationPunctured.lean#L397). The attribute's comment: “the degree-m summand of the functions on the punctured cone over D₊(f) is the module of sections of O\_P(m) over D₊(f), for every integer m”.

> The degree-`m` summand of `(B[1/σ f · ψ f])₀` is the module of sections of the twisting
> sheaf `𝒪_P(m)` over `D₊(f)`, for every integer `m`.

```lean
def puncturedGradingEquivSectionsTwist (hf : f ∈ 𝒜 d) (hd : 0 < d) (m : ℤ) :
    puncturedGrading 𝒜 d hf m ≃+
      (twistingSheaf 𝒜 m).val.obj (op (ProjectiveSpectrum.basicOpen 𝒜 f))
```

## Tag 0EKH, an equation

[Tag 0EKH](https://stacks.math.columbia.edu/tag/0EKH) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjAndSpec.derivedPushforwardPuncturedConeIsoTruncation_hom_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecPuncturedConeFunctorial.lean, line 692](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecPuncturedConeFunctorial.lean#L692). The attribute's comment: “the decomposition RΓ(U, F\_U) = ⊕\_m RΓ(P, F ⊗ O\_P(m)) is functorial in F; RΓ is read as derived direct image to Spec A₀”.

> **The decomposition `RΓ(U, 𝓕_U) = ⨁_m RΓ(P, 𝓕(m))` is functorial in `𝓕`.** For a morphism
> `φ : 𝓕 ⟶ 𝓖` of quasi-coherent `𝒪_P`-modules, the morphism `RΓ(U, φ_U)` induced on derived
> global sections of the pullbacks to the punctured cone is carried by
> `derivedPushforwardPuncturedConeIsoTruncation` to the direct sum, over all integers `m`, of the
> morphisms `RΓ(P, φ ⊗ 1) : RΓ(P, 𝓕(m)) ⟶ RΓ(P, 𝓖(m))`.

```lean
theorem derivedPushforwardPuncturedConeIsoTruncation_hom_naturality
    [CompactSpace (AlgebraicGeometry.Proj 𝒜)] {F G : (AlgebraicGeometry.Proj 𝒜).Modules}
    [F.IsQuasicoherent] [G.IsQuasicoherent] (φ : F ⟶ G) :
    (Stacks.Duality.derivedPushforward
          (puncturedConeProj (truncationConeData 𝒜) ≫
            AlgebraicGeometry.Proj.toSpecZero 𝒜)).map
        ((DerivedCategory.singleFunctor (openUInL (truncationConeData 𝒜)).toScheme.Modules 0).map
          ((Scheme.Modules.pullback (puncturedConeProj (truncationConeData 𝒜))).map φ)) ≫
        (derivedPushforwardPuncturedConeIsoTruncation 𝒜 G).hom =
      (derivedPushforwardPuncturedConeIsoTruncation 𝒜 F).hom ≫
        Limits.Sigma.map (fun m : ℤ => (Stacks.Duality.derivedPushforward
          (AlgebraicGeometry.Proj.toSpecZero 𝒜)).map
          ((DerivedCategory.singleFunctor (AlgebraicGeometry.Proj 𝒜).Modules 0).map
            (((Stacks.SheafOfModules.Tensor.sheafTensor
              (J := (Opens.grothendieckTopology (ProjectiveSpectrum.top 𝒜)))
              (ProjectiveSpectrum.Proj.structureSheaf 𝒜)).map φ).app (twistingSheaf 𝒜 m))))
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.derivedPushforwardPuncturedConeIsoTruncation_hom_smul_all`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecPuncturedConeModuleStructure.lean, line 642](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecPuncturedConeModuleStructure.lean#L642). The attribute's comment: “the A-module structure on the right of RΓ(U, F\_U) = ⊕\_m RΓ(P, F ⊗ O\_P(m)), where a ∈ A acts through its homogeneous components a\_k : F(m) → F(k + m), agrees with the one on the left coming from U ⊆ X; RΓ is read as derived direct image to Spec A₀”.

> **The `A`-module structures on the two sides of `RΓ(U, 𝓕_U) = ⨁_m RΓ(P, 𝓕(m))` agree.** For
> every `a ∈ A`, the decomposition `derivedPushforwardPuncturedConeIsoTruncation` carries
> multiplication by `a` on `RΓ(U, 𝓕_U)`, through `U ⊆ X = Spec A` (`puncturedConeSmul`), to the
> graded action `twistSumSmul` of `a` on `⨁_m RΓ(P, 𝓕(m))`, in which each homogeneous component
> `a_k` sends `RΓ(P, 𝓕(m))` to `RΓ(P, 𝓕(k + m))`.

```lean
theorem derivedPushforwardPuncturedConeIsoTruncation_hom_smul_all
    [CompactSpace (AlgebraicGeometry.Proj 𝒜)] (F : (AlgebraicGeometry.Proj 𝒜).Modules)
    [F.IsQuasicoherent] (a : A) :
    (derivedPushforward (puncturedConeProj (truncationConeData 𝒜) ≫
          AlgebraicGeometry.Proj.toSpecZero 𝒜)).map
        ((DerivedCategory.singleFunctor (openUInL (truncationConeData 𝒜)).toScheme.Modules 0).map
          ((puncturedConeSmul (truncationConeData 𝒜) a).asHom.app
            (puncturedConePullback (truncationConeData 𝒜) F) :
            puncturedConePullback (truncationConeData 𝒜) F ⟶
              puncturedConePullback (truncationConeData 𝒜) F)) ≫
        (derivedPushforwardPuncturedConeIsoTruncation 𝒜 F).hom =
      (derivedPushforwardPuncturedConeIsoTruncation 𝒜 F).hom ≫ twistSumSmul 𝒜 F a
```

**`Stacks.AlgebraicGeometry.ProjAndSpec.derivedPushforwardPuncturedConeIsoTruncation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecPuncturedConeProjectionFormula.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjAndSpecPuncturedConeProjectionFormula.lean#L280). The attribute's comment: “the direct-sum decomposition, with RΓ read as derived direct image to Spec A₀; its functoriality and its A-linearity are the \_hom\_naturality and \_hom\_smul theorems”.

> **`RΓ(U, 𝓕_U) = ⨁_{m ∈ Z} RΓ(P, 𝓕 ⊗_{𝒪_P} 𝒪_P(m))`.** Let `A` be a nonnegatively graded
> ring, `P = Proj A` quasi-compact, `π : L ⟶ P` the cone of the truncation algebra
> `B = ⨁_{d ≥ 0} A_{≥ d}` and `U ⊆ L` the punctured cone. For a quasi-coherent `𝒪_P`-module `𝓕`
> with pullback `𝓕_U = (π|_U)^*𝓕`, the derived global sections of `𝓕_U` decompose as the direct
> sum, over all integers `m`, of the derived global sections of the `m`-th twist of `𝓕`; both sides
> are read as derived direct images to `Z = Spec A₀`.
>
> Its functoriality in `𝓕` is
> `Stacks.AlgebraicGeometry.ProjAndSpec.derivedPushforwardPuncturedConeIsoTruncation_hom_naturality`
> and its compatibility with the `A`-module structures is
> `Stacks.AlgebraicGeometry.ProjAndSpec.derivedPushforwardPuncturedConeIsoTruncation_hom_smul`.

```lean
def derivedPushforwardPuncturedConeIsoTruncation
    [CompactSpace (AlgebraicGeometry.Proj 𝒜)] (F : (AlgebraicGeometry.Proj 𝒜).Modules)
    [F.IsQuasicoherent] :
    (Stacks.Duality.derivedPushforward
          (puncturedConeProj (truncationConeData 𝒜) ≫
            AlgebraicGeometry.Proj.toSpecZero 𝒜)).obj
        ((DerivedCategory.singleFunctor _ 0).obj
          (puncturedConePullback (truncationConeData 𝒜) F)) ≅
      ∐ fun m : ℤ => (Stacks.Duality.derivedPushforward
        (AlgebraicGeometry.Proj.toSpecZero 𝒜)).obj
        ((DerivedCategory.singleFunctor _ 0).obj (twistSheafOfModules 𝒜 F m))
```

## Tag 0EKI, a lemma

[Tag 0EKI](https://stacks.math.columbia.edu/tag/0EKI) in the Stacks Project.

**`Stacks.SectionRingProjIso.projAndSpecDiagram_eq_laurentDiagram_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjIso/DiagramArrows.lean, line 364](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SectionRingProjIso/DiagramArrows.lean#L364). The attribute's comment: “the whole statement: P = Proj A and diagram 0EKG becomes, arrow by arrow, the diagram of the relative spectra over P of the Laurent algebras of the ample module: the open immersion U → L is the morphism induced by the inclusion of algebras, the projections to P are the structure morphisms, and the left and right squares commute”. References: EGA II (8.7.4), “(ii), special case”; EGA II (8.8.3), “special case”.

> **Stacks Project, Tag 0EKI: for `P` proper over `R` and `𝓛` ample, diagram 0EKG is the
> diagram of `Spec_P(⨁_{m ∈ ℤ} 𝓛^{⊗ m}) ⟶ Spec_P(⨁_{m ≥ 0} 𝓛^{⊗ m}) ⟶ P`, arrow by arrow.**
>
> Let `A = Γ_*(P, 𝓛)`, `r : P ⟶ Proj A` the canonical morphism, `π : L ⟶ Proj A` the cone of
> [Stacks, Tag 0EKG] with its punctured cone `U ⊆ L`, `σ : L ⟶ X = Spec A`, and `ρ`, `Φ_L`, `Φ_U`
> the identifications `P ≅ Proj A`, `L ≅ Spec_P(⨁_{m ≥ 0} 𝓛^{⊗ m})`, `U ≅ Spec_P(⨁_{m ∈ ℤ} 𝓛^{⊗ m})`
> (the last two over `P`). Then:
>
> 1. `r` is an isomorphism (`P = Proj A`);
> 2. **the top arrow**: under `Φ_U` and `Φ_L` the open immersion `U ⟶ L` is the morphism
>    `Spec_P(⨁_{m ∈ ℤ} 𝓛^{⊗ m}) ⟶ Spec_P(⨁_{m ≥ 0} 𝓛^{⊗ m})` induced by the inclusion of algebras
>    `⨁_{m ≥ 0} 𝓛^{⊗ m} ⊆ ⨁_{m ∈ ℤ} 𝓛^{⊗ m}`, as morphisms over `P`;
> 3. **the projections**: under `Φ_L` and `ρ` the cone projection `π` is the structure morphism of
>    `Spec_P(⨁_{m ≥ 0} 𝓛^{⊗ m})`, and under `Φ_U` and `ρ` its restriction `π|_U` is that of
>    `Spec_P(⨁_{m ∈ ℤ} 𝓛^{⊗ m})`;
> 4. the top arrow is a morphism over `P` and an open immersion;
> 5. **the left vertical identification** `Spec_P(⨁_{m ∈ ℤ} 𝓛^{⊗ m}) ≅ U ⊆ X` (the `=` of the
>    diagram) is `Φ_U⁻¹` followed by `σ|_U`, an isomorphism;
> 6. **the left square** of the new diagram commutes: the top arrow followed by `σ` (read through
>    `Φ_L`) is the identification with `U` followed by `U ⊆ X`;
> 7. **the right square** of the new diagram commutes: the projection to `P` followed by
>    `P = Proj A ⟶ Z = Spec A₀` is `σ` (read through `Φ_L`) followed by `X ⟶ Z`.

```lean
theorem projAndSpecDiagram_eq_laurentDiagram_of_isProper :
    IsIso (projHomOfIsAmple L hL) ∧
    (puncturedConeIsoLaurentOfIsProper L hL f).inv ≫ openUInLOverOfIsProper L hL f =
      laurentToNonnegLaurentRelativeSpec L hL ≫ (coneIsoNonnegLaurentOfIsProper L hL f).inv ∧
    (coneIsoNonnegLaurentOfIsProper L hL f).hom.left ≫ (nonnegLaurentRelativeSpecOver L hL).hom =
      pi (grading L) ≫ (projIsoOfIsProper L hL f).inv ∧
    (puncturedConeIsoLaurentOfIsProper L hL f).hom.left ≫ (laurentRelativeSpecOver L hL).hom =
      (openUInL (grading L)).ι ≫ pi (grading L) ≫ (projIsoOfIsProper L hL f).inv ∧
    (laurentToNonnegLaurentRelativeSpec L hL).left ≫ (nonnegLaurentRelativeSpecOver L hL).hom =
      (laurentRelativeSpecOver L hL).hom ∧
    IsOpenImmersion (laurentToNonnegLaurentRelativeSpec L hL).left ∧
    IsIso ((puncturedConeIsoLaurentOfIsProper L hL f).inv.left ≫
      (toSpecA (grading L) ∣_ Stacks.AlgebraicGeometry.ProjAndSpec.openU (grading L))) ∧
    (laurentToNonnegLaurentRelativeSpec L hL).left ≫
        (coneIsoNonnegLaurentOfIsProper L hL f).inv.left ≫ toSpecA (grading L) =
      ((puncturedConeIsoLaurentOfIsProper L hL f).inv.left ≫
        (toSpecA (grading L) ∣_ Stacks.AlgebraicGeometry.ProjAndSpec.openU (grading L))) ≫
        (Stacks.AlgebraicGeometry.ProjAndSpec.openU (grading L)).ι ∧
    (nonnegLaurentRelativeSpecOver L hL).hom ≫ (projIsoOfIsProper L hL f).hom ≫
        Proj.toSpecZero (grading L) =
      (coneIsoNonnegLaurentOfIsProper L hL f).inv.left ≫ toSpecA (grading L) ≫
        Stacks.AlgebraicGeometry.ProjAndSpec.xToZ (grading L)
```

**`Stacks.SectionRingProjIso.coneIsoNonnegLaurentOfIsProper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjIso/DiagramClause.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SectionRingProjIso/DiagramClause.lean#L241). The attribute's comment: “the diagram clause: the nonnegatively graded left-hand entry L of diagram 0EKG becomes Spec\_P of the direct sum of the nonnegative tensor powers of the ample module”.

> **The diagram clause of [Stacks, Tag 0EKI], nonnegatively graded entry.** For `P` proper over
> a ring `R` and `𝓛` an ample invertible `𝒪_P`-module with section ring `A = Γ_*(P, 𝓛)`, the
> nonnegatively graded left-hand entry `L` of [Stacks, Tag 0EKG]'s diagram, read over `P` through
> the identification `P = Proj A`, is `Spec_P(⨁_{m ≥ 0} 𝓛^{⊗ m})`.
>
> The structure morphism on the left is the cone projection `π` followed by the inverse of the
> canonical morphism `r : P ⟶ Proj A` of [Stacks, Tag 01PZ], which is an isomorphism by
> `Stacks.SectionRingProjIso.isIso_projHomOfIsAmple_of_isProper`; that is what makes the base
> change in `coneBaseChangeIsoNonnegLaurent` the identity, by
> `Stacks.AlgebraicGeometry.OverBaseChange.overPullbackIsoOfIsIso`.

```lean
def coneIsoNonnegLaurentOfIsProper :
    Over.mk (pi (grading L) ≫ (projIsoOfIsProper L hL f).inv) ≅
      nonnegLaurentRelativeSpecOver L hL
```

**`Stacks.SectionRingProjIso.puncturedConeIsoLaurentOfIsProper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjIso/DiagramClause.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SectionRingProjIso/DiagramClause.lean#L255). The attribute's comment: “the diagram clause: the integer-graded left-hand entry U of diagram 0EKG becomes Spec\_P of the direct sum of all integral tensor powers of the ample module”.

> **The diagram clause of [Stacks, Tag 0EKI], integer-graded entry.** For `P` proper over a ring
> `R` and `𝓛` an ample invertible `𝒪_P`-module with section ring `A = Γ_*(P, 𝓛)`, the
> integer-graded left-hand entry `U` of [Stacks, Tag 0EKG]'s diagram, read over `P` through the
> identification `P = Proj A`, is `Spec_P(⨁_{m ∈ ℤ} 𝓛^{⊗ m})`.

```lean
def puncturedConeIsoLaurentOfIsProper :
    Over.mk ((openUInL (grading L)).ι ≫ pi (grading L) ≫ (projIsoOfIsProper L hL f).inv) ≅
      laurentRelativeSpecOver L hL
```

**`Stacks.SectionRingProjIso.isIso_projHomOfIsAmple_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjIso/Proper.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SectionRingProjIso/Proper.lean#L112). The attribute's comment: “the identification P = Proj(A), for P proper over R”.

> Let `P` be a proper scheme over a ring `R` and `𝓛` an ample invertible `𝒪_P`-module with
> graded section ring `A = Γ_*(P, 𝓛)`. Then the canonical morphism `r : P ⟶ Proj A` of
> [Stacks, Tag 01PZ] is an isomorphism.

```lean
theorem isIso_projHomOfIsAmple_of_isProper (hL : IsAmple X L) {R : CommRingCat.{u}}
    (f : X ⟶ Spec R) [IsProper f] :
    IsIso (projHomOfIsAmple L hL)
```

**`Stacks.SectionRingProjIso.projIsoOfIsProper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjIso/Proper.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SectionRingProjIso/Proper.lean#L125). The attribute's comment: “the identification P = Proj(A) as an isomorphism P ≅ Proj Γ\_*(P, 𝓛), for P proper over R”.

> The isomorphism `P ≅ Proj Γ_*(P, 𝓛)` whose underlying morphism is the canonical one of
> [Stacks, Tag 01PZ], for `P` proper over `R` and `𝓛` ample.

```lean
noncomputable def projIsoOfIsProper (hL : IsAmple X L) {R : CommRingCat.{u}}
    (f : X ⟶ Spec R) [IsProper f] :
    X ≅ AlgebraicGeometry.Proj (grading L)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.51, Tag 0EKF](https://stacks.math.columbia.edu/tag/0EKF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
