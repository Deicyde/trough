---
declaration: module
origin: cited
lean: ContRepresentation.integratedOperatorL1, ContRepresentation.integratedOperatorL1_apply, ContRepresentation.integratedOperatorL1_toL1, ContRepresentation.norm_integratedOperatorL1_le, ContRepresentation.comp_integratedOperatorL1, ContRepresentation.continuous_comp_integratedOperatorL1, ContRepresentation.commute_integratedOperatorL1, ContRepresentation.integratedOperatorL1_commute
statement: formalized
proof: formalized
---

# The integrated form of a strongly continuous representation

The module `PhyslibAlpha.Mathematics.TauCeti.RepresentationTheory.Continuous.Integrated.Basic`, [PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean): 14 declarations, 14 with a docstring; 2 private, not shown.

> Let `π` be a representation of an additive topological group `G` (written multiplicatively, as a
> `ContRepresentation` of `Multiplicative G`) on a normed space `E`, which is **strongly continuous**
> (every orbit `g ↦ π g v` is continuous) and uniformly bounded, and let `μ` be a measure on `G`.

## i. Overview

> Let `π` be a representation of an additive topological group `G` (written multiplicatively, as a
> `ContRepresentation` of `Multiplicative G`) on a normed space `E`, which is **strongly continuous**
> (every orbit `g ↦ π g v` is continuous) and uniformly bounded, and let `μ` be a measure on `G`. An
> integrable weight `f` then acts on `E` by the **integrated form**
>
> `π(f) v = ∫ g, f g • π g v ∂μ`,
>
> a bounded operator with `‖π(f)‖ ≤ C * ‖f‖₁` when `‖π g‖ ≤ C`. This file builds the map
> `f ↦ π(f)` as a continuous linear map `L¹(G, μ) →L E →L E` and proves the identities that make it a
> representation of the convolution algebra `L¹(G)`: translating the weight composes with `π`,
> convolution of weights becomes composition of operators, and, for a unitary `π` and an
> inversion-invariant `μ`, adjoints correspond to the involution `f^*(g) = conj (f (-g))`.
> For abelian `G`, the integrated operators commute for any measure; they are also normal
> when `π` is unitary and `μ` is inversion-invariant.
>
> The integrated form is how a strongly continuous representation is handled by operator algebra:
> the operators `π g` themselves depend on `g` only strongly continuously, but the left translates
> `π h ∘L π(f)` depend continuously on `h` in the operator norm. Applied to the GNS representation of
> a continuous positive-definite function on a locally compact abelian group, the commutative
> algebra of operators `π(f)` is the standard source of the representing measure in Bochner's
> theorem (Folland, Chapter 4).
>
> **Implementation notes.** The definition integrates the orbits `g ↦ f g • π g v` pointwise in `v`
> and only then bundles the
> result into an operator. The operator-valued map `g ↦ π g` need not be strongly measurable for the
> operator norm: for the regular representation of `ℝ` on `L²(ℝ)`, distinct translations are at
> operator distance `2`, so the map is not almost everywhere separably valued, and `π(f)` cannot be
> written as a Bochner integral in `E →L E`. This is also why
> `TauCeti.ContRepresentation.integratedOperator`, which averages a *norm*-continuous representation
> of a compact group against a continuous weight, does not apply here. The strong continuity and the
> uniform bound are hypotheses of the definition: they are exactly what makes the integrand
> integrable, and they hold for the unitary representations that are the main application.
> Measurability of the integrands `g ↦ f g • π g v` is read off from the continuity of the orbits and
> the inner regularity of `μ` for compact sets
> (`MeasureTheory.AEFinStronglyMeasurable.aestronglyMeasurable_smul`): an integrable weight lives on a
> σ-finite set, which up to a null set is a countable union of compact sets with separable images.
> The Haar measure `MeasureTheory.Measure.addHaar` of a locally compact group is regular, hence has
> this property, so no second countability of `G` or separability of `E` is needed. Only the
> convolution identity, which integrates over `G × G`, still asks for
> `SecondCountableTopologyEither G E`.

## ii. Key results

> * `ContRepresentation.integratedOperatorL1`: the integrated form `f ↦ π(f)`, as a bounded linear
>   map from `L¹(G, μ)` to the bounded operators on `E`.
>
> * `ContRepresentation.integratedOperatorL1_apply`, `ContRepresentation.integratedOperatorL1_toL1`:
>   the pointwise formula `π(f) v = ∫ g, f g • π g v ∂μ`.
> * `ContRepresentation.norm_integratedOperatorL1_le`: `‖π(f)‖ ≤ C * ‖f‖₁` when `‖π g‖ ≤ C`.
> * `ContRepresentation.comp_integratedOperatorL1`: `π h ∘L π(f) = π(f (-h + ·))` for a
>   left-invariant measure.
> * `ContRepresentation.continuous_comp_integratedOperatorL1`: `h ↦ π h ∘L π(f)` is continuous in the
>   operator norm.
> * `ContRepresentation.integratedOperatorL1_convolution`: `π(f₁ ⋆ f₂) = π(f₁) ∘L π(f₂)` on an
>   abelian group with a right-invariant measure.
> * `ContRepresentation.integratedOperatorL1_commute`: integrated operators commute on an abelian
>   group with any measure.
> * `ContRepresentation.inner_integratedOperatorL1_apply`: the matrix coefficients
>   `⟪w, π(f) v⟫ = ∫ g, f g * ⟪w, π g v⟫ ∂μ`.
> * `ContRepresentation.adjoint_integratedOperatorL1`: `π(f)† = π(f^*)` for a unitary `π`.
> * `ContRepresentation.isStarNormal_integratedOperatorL1`: integrated operators of a unitary
>   abelian-group representation are normal for an inversion-invariant measure.
> * `ContRepresentation.tendsto_integratedOperatorL1_apply`: weights of unit integral and bounded
>   `L¹` norm concentrating at `0` form an approximate identity, `π(f i) v → v`.
> * `ContRepresentation.mem_closure_range_integratedOperatorL1_apply`: the integrated form is
>   nondegenerate, every `v` being a limit of vectors `π(f) v`.

## iv. References

> * G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press (2016), §3.2.

## A. Development

**`ContRepresentation.integratedOperatorL1`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean#L150).

> The **integrated form** of a strongly continuous, uniformly bounded representation `π` of an
> additive group `G` (written multiplicatively as `Multiplicative G`): the bounded operator
> `π(f) = ∫ g, f g • π g ∂μ` attached to an integrable weight `f`, defined pointwise by the Bochner
> integral `π(f) v = ∫ g, f g • π g v ∂μ` of the continuous orbit `g ↦ π g v`.

```lean
noncomputable def _root_.ContRepresentation.integratedOperatorL1
    (hcont : ∀ v, Continuous fun g : G ↦ π (.ofAdd g) v)
    (hbdd : ∃ C, ∀ g, ‖π g‖ ≤ C) (μ : Measure G) [μ.InnerRegularCompactLTTop] :
    (G →₁[μ] 𝕜) →L[𝕜] E →L[𝕜] E
```

**`ContRepresentation.integratedOperatorL1_apply`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean#L181).

> The integrated form acts on a vector by integrating its orbit against the weight.

```lean
lemma _root_.ContRepresentation.integratedOperatorL1_apply (f : G →₁[μ] 𝕜) (v : E) :
    π.integratedOperatorL1 hcont hbdd μ f v = ∫ g, f g • π (.ofAdd g) v ∂μ
```

**`ContRepresentation.integratedOperatorL1_toL1`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean#L187).

> The integrated form of the class of an integrable function.

```lean
lemma _root_.ContRepresentation.integratedOperatorL1_toL1 {f : G → 𝕜} (hf : Integrable f μ)
    (v : E) :
    π.integratedOperatorL1 hcont hbdd μ (hf.toL1 f) v = ∫ g, f g • π (.ofAdd g) v ∂μ
```

**`ContRepresentation.norm_integratedOperatorL1_le`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean#L197).

> The integrated form is bounded by the uniform bound of the representation times the `L¹`
> norm of the weight.

```lean
lemma _root_.ContRepresentation.norm_integratedOperatorL1_le {C : ℝ} (hC : ∀ g, ‖π g‖ ≤ C)
    (f : G →₁[μ] 𝕜) :
    ‖π.integratedOperatorL1 hcont hbdd μ f‖ ≤ C * ‖f‖
```

**`ContRepresentation.comp_integratedOperatorL1`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean#L207).

> Translating the weight on the left by `h` amounts to composing the integrated form with
> `π h`.

```lean
lemma _root_.ContRepresentation.comp_integratedOperatorL1 [CompleteSpace E] [MeasurableAdd G]
    [μ.IsAddLeftInvariant] (h : G) (f : G →₁[μ] 𝕜) :
    π (.ofAdd h) ∘L π.integratedOperatorL1 hcont hbdd μ f =
      π.integratedOperatorL1 hcont hbdd μ
        (Lp.compMeasurePreserving (fun g ↦ -h + g) (measurePreserving_add_left μ (-h)) f)
```

**`ContRepresentation.continuous_comp_integratedOperatorL1`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean#L230).

> Although `π` is only strongly continuous, `h ↦ π h ∘L π(f)` is continuous in the operator norm:
> by `comp_integratedOperatorL1` it is the integrated form of the left translates of `f`, which
> depend continuously on `h` in `L¹`.

```lean
lemma _root_.ContRepresentation.continuous_comp_integratedOperatorL1 [CompleteSpace E]
    [IsTopologicalAddGroup G] [MeasurableAdd G] [μ.IsAddLeftInvariant] [IsLocallyFiniteMeasure μ]
    (f : G →₁[μ] 𝕜) :
    Continuous fun h : G ↦ π (.ofAdd h) ∘L π.integratedOperatorL1 hcont hbdd μ f
```

**`ContRepresentation.commute_integratedOperatorL1`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean#L253).

> Every action operator of a representation of an abelian group commutes with its
> integrated operators. No invariance hypothesis on the measure is needed.

```lean
lemma _root_.ContRepresentation.commute_integratedOperatorL1
    (g : Multiplicative G) (f : G →₁[μ] 𝕜) :
    Commute (π g) (π.integratedOperatorL1 hcont hbdd μ f)
```

**`ContRepresentation.integratedOperatorL1_commute`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean#L269).

> Integrated operators of an abelian-group representation commute for any measure.

```lean
lemma _root_.ContRepresentation.integratedOperatorL1_commute (f₁ f₂ : G →₁[μ] 𝕜) :
    Commute (π.integratedOperatorL1 hcont hbdd μ f₁)
      (π.integratedOperatorL1 hcont hbdd μ f₂)
```

**`ContRepresentation.integratedOperatorL1_convolution`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean#L300).

> The integrated form turns convolution of weights into composition of operators:
> `π(f₁ ⋆ f₂) = π(f₁) ∘L π(f₂)`.

```lean
lemma _root_.ContRepresentation.integratedOperatorL1_convolution {f₁ f₂ : G → 𝕜}
    (hf₁ : Integrable f₁ μ) (hf₂ : Integrable f₂ μ) :
    π.integratedOperatorL1 hcont hbdd μ
        ((hf₁.integrable_convolution (ContinuousLinearMap.mul 𝕜 𝕜) hf₂).toL1 _) =
      π.integratedOperatorL1 hcont hbdd μ (hf₁.toL1 f₁) ∘L
        π.integratedOperatorL1 hcont hbdd μ (hf₂.toL1 f₂)
```

**`ContRepresentation.inner_integratedOperatorL1_apply`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean#L350).

> Matrix coefficients of the integrated form are the integrals of the matrix coefficients of the
> representation against the weight.

```lean
lemma _root_.ContRepresentation.inner_integratedOperatorL1_apply (f : G →₁[μ] 𝕜) (w v : E) :
    ⟪w, π.integratedOperatorL1 hcont hbdd μ f v⟫_𝕜 = ∫ g, f g * ⟪w, π (.ofAdd g) v⟫_𝕜 ∂μ
```

**`ContRepresentation.adjoint_integratedOperatorL1`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean#L358).

> The adjoint of the integrated form of a unitary representation is the integrated form of the
> involuted weight `g ↦ conj (f (-g))`.

```lean
lemma _root_.ContRepresentation.adjoint_integratedOperatorL1 [MeasurableNeg G]
    [μ.IsNegInvariant] (hπ : ContRepresentation.IsUnitary π) (f : G →₁[μ] 𝕜) :
    ContinuousLinearMap.adjoint (π.integratedOperatorL1 hcont hbdd μ f) =
      π.integratedOperatorL1 hcont hbdd μ
        (star (Lp.compMeasurePreserving Neg.neg (Measure.measurePreserving_neg μ) f))
```

**`ContRepresentation.isStarNormal_integratedOperatorL1`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean#L388).

> The integrated operators of a unitary abelian-group representation are normal.

```lean
lemma _root_.ContRepresentation.isStarNormal_integratedOperatorL1
    (hπ : ContRepresentation.IsUnitary π) (f : G →₁[μ] 𝕜) :
    IsStarNormal (π.integratedOperatorL1 hcont hbdd μ f)
```

**`ContRepresentation.tendsto_integratedOperatorL1_apply`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean#L412).

> **Approximate identities for the integrated form.** If the weights `f i` eventually have unit
> integral and `L¹` norm at most `C`, and concentrate at `0` (for every neighbourhood `U` of `0`,
> eventually `f i` vanishes almost everywhere outside `U`), then `π(f i)` tends strongly to the
> identity: `π(f i) v → v` for every `v`.

```lean
lemma _root_.ContRepresentation.tendsto_integratedOperatorL1_apply {ι : Type*} {l : Filter ι}
    {f : ι → G →₁[μ] 𝕜} {C : ℝ} (hf : ∀ᶠ i in l, ∫ g, f i g ∂μ = 1)
    (hfC : ∀ᶠ i in l, ‖f i‖ ≤ C)
    (hf₀ : ∀ U ∈ 𝓝 (0 : G), ∀ᶠ i in l, ∀ᵐ g ∂μ, g ∉ U → f i g = 0) (v : E) :
    Tendsto (fun i ↦ π.integratedOperatorL1 hcont hbdd μ (f i) v) l (𝓝 v)
```

**`ContRepresentation.mem_closure_range_integratedOperatorL1_apply`**, a lemma, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean#L425).

> **The integrated form is nondegenerate.** For a measure positive on nonempty open sets and
> finite on some neighbourhood of each point, such as a Haar measure on a locally compact group, every
> vector `v` is a limit of vectors `π(f) v`.

```lean
lemma _root_.ContRepresentation.mem_closure_range_integratedOperatorL1_apply
    [μ.IsOpenPosMeasure] [IsLocallyFiniteMeasure μ] (v : E) :
    v ∈ closure (Set.range fun f : G →₁[μ] 𝕜 ↦ π.integratedOperatorL1 hcont hbdd μ f v)
```

## Depends on

- [Unitary continuous representations](representationtheory-continuous-unitary-basic.md)

## Proof depends on

- [Continuous functions are a.e. strongly measurable for inner regular measures](measuretheory-function-stronglymeasurable-innerr.md)
- [Integrals against `L¹` peak functions concentrating at a point](measuretheory-integral-peakfunction.md)
- [Indexing a net by the members of a filter](order-filter-smallsets.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Integrated/Basic.lean)
