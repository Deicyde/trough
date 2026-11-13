---
declaration: module
origin: cited
lean: TwoHiggsDoublet.PotentialParameters, TwoHiggsDoublet.PotentialParameters.zero_m₁₁2, TwoHiggsDoublet.PotentialParameters.zero_m₂₂2, TwoHiggsDoublet.PotentialParameters.zero_m₁₂2, TwoHiggsDoublet.PotentialParameters.zero_𝓵₁, TwoHiggsDoublet.PotentialParameters.zero_𝓵₂, TwoHiggsDoublet.PotentialParameters.zero_𝓵₃, TwoHiggsDoublet.PotentialParameters.zero_𝓵₄
statement: formalized
proof: formalized
---

# The potential of the Two Higgs doublet model

The module `Physlib.Particles.BeyondTheStandardModel.TwoHDM.Potential`, [Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean): 58 declarations (1 instance with no name), 13 with a docstring.

## i. Overview

> In this module we give the define the parameters of the 2HDM potential, and
> give stability properties of the potential.

## ii. Key results

> - `PotentialParameters` : The parameters of the 2HDM potential.
> - `massTerm` : The mass term of the 2HDM potential.
> - `quarticTerm` : The quartic term of the 2HDM potential.
> - `potential` : The full potential of the 2HDM.
> - `PotentialIsStable` : The condition that the potential is stable.

## iv. References

> * For the parameterization of the potential we follow the convention of
>   https://arxiv.org/pdf/1605.03237. [ref: arxiv\_1605\_03237]
> * Stability arguments of the potential follow, in part, those from
>   https://arxiv.org/abs/hep-ph/0605184, although we note that we explicitly prove that one of
>   the steps in this paper is not valid. [ref: arxiv\_hep\_ph\_0605184]

## A. The parameters of the potential

> We define a type for the parameters of the Higgs potential in the 2HDM.
>
> We follow the convention of `1605.03237` [ref: arxiv\_1605\_03237], which is highlighted in the
> explicit construction of the potential itself.
>
> We relate these parameters to the `ξ` and `η` parameters used in the gram vector formalism
> given in arXiv:hep-ph/0605184 [ref: arxiv\_hep\_ph\_0605184].

**`TwoHiggsDoublet.PotentialParameters`**, a structure, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L74).

> The parameters of the Two Higgs doublet model potential.
> Following the convention of https://arxiv.org/pdf/1605.03237 [ref: arxiv\_1605\_03237].

```lean
structure PotentialParameters where
  /-- The parameter corresponding to `m₁₁²` in the 2HDM potential. -/
  m₁₁2 : ℝ
  /-- The parameter corresponding to `m₂₂²` in the 2HDM potential. -/
  m₂₂2 : ℝ
  /-- The parameter corresponding to `m₁₂²` in the 2HDM potential. -/
  m₁₂2 : ℂ
  /-- The parameter corresponding to `λ₁` in the 2HDM potential. -/
  𝓵₁ : ℝ
  /-- The parameter corresponding to `λ₂` in the 2HDM potential. -/
  𝓵₂ : ℝ
  /-- The parameter corresponding to `λ₃` in the 2HDM potential. -/
  𝓵₃ : ℝ
  /-- The parameter corresponding to `λ₄` in the 2HDM potential. -/
  𝓵₄ : ℝ
  /-- The parameter corresponding to `λ₅` in the 2HDM potential. -/
  𝓵₅ : ℂ
  /-- The parameter corresponding to `λ₆` in the 2HDM potential. -/
  𝓵₆ : ℂ
  /-- The parameter corresponding to `λ₇` in the 2HDM potential. -/
  𝓵₇ : ℂ
```

### A.1. The potential parameters corresponding to zero

> We define an instance of `Zero` for the potential parameters, corresponding to all
> parameters being zero, and therefore the potential itself being zero.

**An instance with no name**, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L107).

```lean
instance : Zero PotentialParameters
```

**`TwoHiggsDoublet.PotentialParameters.zero_m₁₁2`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L120).

```lean
lemma zero_m₁₁2 : (0 : PotentialParameters).m₁₁2 = 0
```

**`TwoHiggsDoublet.PotentialParameters.zero_m₂₂2`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L122).

```lean
lemma zero_m₂₂2 : (0 : PotentialParameters).m₂₂2 = 0
```

**`TwoHiggsDoublet.PotentialParameters.zero_m₁₂2`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L124).

```lean
lemma zero_m₁₂2 : (0 : PotentialParameters).m₁₂2 = 0
```

**`TwoHiggsDoublet.PotentialParameters.zero_𝓵₁`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L126).

```lean
lemma zero_𝓵₁ : (0 : PotentialParameters).𝓵₁ = 0
```

**`TwoHiggsDoublet.PotentialParameters.zero_𝓵₂`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L128).

```lean
lemma zero_𝓵₂ : (0 : PotentialParameters).𝓵₂ = 0
```

**`TwoHiggsDoublet.PotentialParameters.zero_𝓵₃`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L130).

```lean
lemma zero_𝓵₃ : (0 : PotentialParameters).𝓵₃ = 0
```

**`TwoHiggsDoublet.PotentialParameters.zero_𝓵₄`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L132).

```lean
lemma zero_𝓵₄ : (0 : PotentialParameters).𝓵₄ = 0
```

**`TwoHiggsDoublet.PotentialParameters.zero_𝓵₅`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L134).

```lean
lemma zero_𝓵₅ : (0 : PotentialParameters).𝓵₅ = 0
```

**`TwoHiggsDoublet.PotentialParameters.zero_𝓵₆`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L136).

```lean
lemma zero_𝓵₆ : (0 : PotentialParameters).𝓵₆ = 0
```

**`TwoHiggsDoublet.PotentialParameters.zero_𝓵₇`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L138).

```lean
lemma zero_𝓵₇ : (0 : PotentialParameters).𝓵₇ = 0
```

### A.2. Gram parameters

> A reparameterization of the potential parameters corresponding to `ξ` and `η` in
> arXiv:hep-ph/0605184 [ref: arxiv\_hep\_ph\_0605184].

**`TwoHiggsDoublet.PotentialParameters.ξ`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L151).

> A reparameterization of the parameters of the quadratic terms of the
> potential for use with the gramVector.

```lean
noncomputable def ξ (P : PotentialParameters) (μ : Fin 1 ⊕ Fin 3) : ℝ
```

**`TwoHiggsDoublet.PotentialParameters.ξ_zero`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L159).

```lean
lemma ξ_zero : (0 : PotentialParameters).ξ = 0
```

**`TwoHiggsDoublet.PotentialParameters.η`**, a def, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L165).

> A reparameterization of the parameters of the quartic terms of the
> potential for use with the gramVector.

```lean
noncomputable def η (P : PotentialParameters) : Fin 1 ⊕ Fin 3 → Fin 1 ⊕ Fin 3 → ℝ
```

**`TwoHiggsDoublet.PotentialParameters.η_symm`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L183).

```lean
lemma η_symm (P : PotentialParameters) (μ ν : Fin 1 ⊕ Fin 3) :
    P.η μ ν = P.η ν μ
```

**`TwoHiggsDoublet.PotentialParameters.η_zero`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L188).

```lean
lemma η_zero : (0 : PotentialParameters).η = 0
```

### A.3. Specific cases

**`TwoHiggsDoublet.PotentialParameters.stabilityCounterExample`**, a def, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L210).

> An example of potential parameters that serve as a counterexample to the stability
> condition given in arXiv:hep-ph/0605184 [ref: arxiv\_hep\_ph\_0605184].
> This corresponds to the potential:
> `2 * (⟪H.Φ1, H.Φ2⟫_ℂ).im + ‖H.Φ1 - H.Φ2‖ ^ 4`
> which has the property that the quartic term is non-negative and only zero if
> the mass term is also zero, but the potential is not stable.
> In the proof that `stabilityCounterExample_not_potentialIsStable`, we give
> explicit vectors `H.Φ1` and `H.Φ2` that show this potential is not stable.
>
> This is the first occurrence of such a counterexample in the literature to the best of
> the author's knowledge.

```lean
def stabilityCounterExample : PotentialParameters
```

**`TwoHiggsDoublet.PotentialParameters.stabilityCounterExample_ξ`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L220).

```lean
lemma stabilityCounterExample_ξ :
    stabilityCounterExample.ξ = fun
      | .inl 0 => 0
      | .inr 0 => 0
      | .inr 1 => 1
      | .inr 2 => 0
```

**`TwoHiggsDoublet.PotentialParameters.stabilityCounterExample_η`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L229).

```lean
lemma stabilityCounterExample_η :
    stabilityCounterExample.η = fun μ => fun ν =>
    match μ, ν with
    | .inl 0, .inl 0 => 1
    | .inl 0, .inr 0 => -1
    | .inl 0, .inr 1 => 0
    | .inl 0, .inr 2 => 0
    | .inr 0, .inl 0 => -1
    | .inr 1, .inl 0 => 0
    | .inr 2, .inl 0 => 0
    | .inr 0, .inr 0 => 1
    | .inr 1, .inr 1 => 0
    | .inr 2, .inr 2 => 0
    | .inr 0, .inr 1 => 0
    | .inr 2, .inr 0 => 0
    | .inr 2, .inr 1 => 0
    | .inr 1, .inr 0 => 0
    | .inr 0, .inr 2 => 0
    | .inr 1, .inr 2 => 0
```

## B. The mass term

> We define the mass term of the potential, write it in terms of the gram vector,
> and prove that it is gauge invariant.

**`TwoHiggsDoublet.massTerm`**, a def, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L266).

> The mass term of the two Higgs doublet model potential.

```lean
noncomputable def massTerm (P : PotentialParameters) (H : TwoHiggsDoublet) : ℝ
```

**`TwoHiggsDoublet.massTerm_eq_gramVector`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L270).

```lean
lemma massTerm_eq_gramVector (P : PotentialParameters) (H : TwoHiggsDoublet) :
    massTerm P H = ∑ μ, P.ξ μ * H.gramVector μ
```

**`TwoHiggsDoublet.gaugeGroupI_smul_massTerm`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L277).

```lean
lemma gaugeGroupI_smul_massTerm (g : StandardModel.GaugeGroupI) (P : PotentialParameters)
    (H : TwoHiggsDoublet) :
    massTerm P (g • H) = massTerm P H
```

**`TwoHiggsDoublet.massTerm_zero`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L283).

```lean
lemma massTerm_zero : massTerm 0 = 0
```

**`TwoHiggsDoublet.massTerm_stabilityCounterExample`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L287).

```lean
lemma massTerm_stabilityCounterExample (H : TwoHiggsDoublet) :
    massTerm PotentialParameters.stabilityCounterExample H =
    2 * (⟪H.Φ1, H.Φ2⟫_ℂ).im
```

## C. The quartic term

> We define the quartic term of the potential, write it in terms of the gram vector,
> and prove that it is gauge invariant.

**`TwoHiggsDoublet.quarticTerm`**, a def, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L304).

> The quartic term of the two Higgs doublet model potential.

```lean
noncomputable def quarticTerm (P : PotentialParameters) (H : TwoHiggsDoublet) : ℝ
```

**`TwoHiggsDoublet.quarticTerm_𝓵₄_expand`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L312).

```lean
lemma quarticTerm_𝓵₄_expand (P : PotentialParameters) (H : TwoHiggsDoublet) :
    H.quarticTerm P =
    1/2 * P.𝓵₁ * ‖H.Φ1‖ ^ 2 * ‖H.Φ1‖ ^ 2 + 1/2 * P.𝓵₂ * ‖H.Φ2‖ ^ 2 * ‖H.Φ2‖ ^ 2
    + P.𝓵₃ * ‖H.Φ1‖ ^ 2 * ‖H.Φ2‖ ^ 2
    + P.𝓵₄ * (⟪H.Φ1, H.Φ2⟫_ℂ * ⟪H.Φ2, H.Φ1⟫_ℂ).re
    + (1/2 * P.𝓵₅ * ⟪H.Φ1, H.Φ2⟫_ℂ ^ 2 + 1/2 * conj P.𝓵₅ * ⟪H.Φ2, H.Φ1⟫_ℂ ^ 2).re
    + (P.𝓵₆ * ‖H.Φ1‖ ^ 2 * ⟪H.Φ1, H.Φ2⟫_ℂ + conj P.𝓵₆ * ‖H.Φ1‖ ^ 2 * ⟪H.Φ2, H.Φ1⟫_ℂ).re
    + (P.𝓵₇ * ‖H.Φ2‖ ^ 2 * ⟪H.Φ1, H.Φ2⟫_ℂ + conj P.𝓵₇ * ‖H.Φ2‖ ^ 2 * ⟪H.Φ2, H.Φ1⟫_ℂ).re
```

**`TwoHiggsDoublet.quarticTerm_eq_gramVector`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L325).

```lean
lemma quarticTerm_eq_gramVector (P : PotentialParameters) (H : TwoHiggsDoublet) :
    quarticTerm P H = ∑ a, ∑ b, H.gramVector a * H.gramVector b * P.η a b
```

**`TwoHiggsDoublet.gaugeGroupI_smul_quarticTerm`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L335).

```lean
lemma gaugeGroupI_smul_quarticTerm (g : StandardModel.GaugeGroupI) (P : PotentialParameters)
    (H : TwoHiggsDoublet) :
    quarticTerm P (g • H) = quarticTerm P H
```

**`TwoHiggsDoublet.quarticTerm_zero`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L341).

```lean
lemma quarticTerm_zero : quarticTerm 0 = 0
```

**`TwoHiggsDoublet.quarticTerm_stabilityCounterExample`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L345).

```lean
lemma quarticTerm_stabilityCounterExample (H : TwoHiggsDoublet) :
    quarticTerm .stabilityCounterExample H =
    (‖H.Φ1‖ ^ 2 + ‖H.Φ2‖ ^ 2 - 2 * (⟪H.Φ1, H.Φ2⟫_ℂ).re) ^ 2
```

**`TwoHiggsDoublet.quarticTerm_stabilityCounterExample_eq_norm_pow_four`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L360).

```lean
lemma quarticTerm_stabilityCounterExample_eq_norm_pow_four (H : TwoHiggsDoublet) :
    quarticTerm .stabilityCounterExample H = ‖H.Φ1 - H.Φ2‖ ^ 4
```

**`TwoHiggsDoublet.quarticTerm_stabilityCounterExample_nonneg`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L367).

```lean
lemma quarticTerm_stabilityCounterExample_nonneg (H : TwoHiggsDoublet) :
    0 ≤ quarticTerm .stabilityCounterExample H
```

**`TwoHiggsDoublet.massTerm_zero_of_quarticTerm_zero_stabilityCounterExample`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L372).

```lean
lemma massTerm_zero_of_quarticTerm_zero_stabilityCounterExample (H : TwoHiggsDoublet)
    (h : quarticTerm .stabilityCounterExample H = 0) :
    massTerm .stabilityCounterExample H = 0
```

## D. The full potential

> We define the full potential as the sum of the mass and quartic terms,
> and prove that it is gauge invariant.

**`TwoHiggsDoublet.potential`**, a def, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L390).

> The potential of the two Higgs doublet model.

```lean
noncomputable def potential (P : PotentialParameters) (H : TwoHiggsDoublet) : ℝ
```

**`TwoHiggsDoublet.gaugeGroupI_smul_potential`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L394).

```lean
lemma gaugeGroupI_smul_potential (g : StandardModel.GaugeGroupI)
    (P : PotentialParameters) (H : TwoHiggsDoublet) :
    potential P (g • H) = potential P H
```

**`TwoHiggsDoublet.potential_zero`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L400).

```lean
lemma potential_zero : potential 0 = 0
```

**`TwoHiggsDoublet.potential_stabilityCounterExample`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L404).

```lean
lemma potential_stabilityCounterExample (H : TwoHiggsDoublet) :
    potential .stabilityCounterExample H = 2 * (⟪H.Φ1, H.Φ2⟫_ℂ).im + ‖H.Φ1 - H.Φ2‖ ^ 4
```

**`TwoHiggsDoublet.potential_eq_gramVector`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L409).

```lean
lemma potential_eq_gramVector (P : PotentialParameters) (H : TwoHiggsDoublet) :
    potential P H = ∑ μ, P.ξ μ * H.gramVector μ +
    ∑ a, ∑ b, H.gramVector a * H.gramVector b * P.η a b
```

## E. Stability of the potential

### E.1. The stability condition

> We define the condition that the potential is stable, that is, bounded from below.

**`TwoHiggsDoublet.PotentialIsStable`**, a def, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L432).

> The condition that the potential is stable.

```lean
def PotentialIsStable (P : PotentialParameters) : Prop
```

### E.2. Instability of the stabilityCounterExample potential

**`TwoHiggsDoublet.stabilityCounterExample_not_potentialIsStable`**, a lemma, [line 444](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L444).

> The potential `stabilityCounterExample` is not stable.

```lean
lemma stabilityCounterExample_not_potentialIsStable :
    ¬ PotentialIsStable .stabilityCounterExample
```

### E.3. The reduced mass term

> The reduced mass term is a function that helps express the stability condition.
> It is the function `J2` in https://arxiv.org/abs/hep-ph/0605184 [ref: arxiv\_hep\_ph\_0605184].

**`TwoHiggsDoublet.massTermReduced`**, a def, [line 539](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L539).

> A function related to the mass term of the potential, used in the stableness
> condition and equivalent to the term `J2` in
> https://arxiv.org/abs/hep-ph/0605184 [ref: arxiv\_hep\_ph\_0605184].

```lean
noncomputable def massTermReduced (P : PotentialParameters) (k : EuclideanSpace ℝ (Fin 3)) : ℝ
```

**`TwoHiggsDoublet.massTermReduced_lower_bound`**, a lemma, [line 542](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L542).

```lean
lemma massTermReduced_lower_bound (P : PotentialParameters) (k : EuclideanSpace ℝ (Fin 3))
    (hk : ‖k‖ ^ 2 ≤ 1) : P.ξ (Sum.inl 0) - √(∑ a, |P.ξ (Sum.inr a)| ^ 2) ≤ massTermReduced P k
```

**`TwoHiggsDoublet.massTermReduced_zero`**, a lemma, [line 564](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L564).

```lean
lemma massTermReduced_zero : massTermReduced 0 = 0
```

**`TwoHiggsDoublet.massTermReduced_stabilityCounterExample`**, a lemma, [line 568](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L568).

```lean
lemma massTermReduced_stabilityCounterExample (k : EuclideanSpace ℝ (Fin 3)) :
    massTermReduced .stabilityCounterExample k = k 1
```

### E.4. The reduced quartic term

> The reduced quartic term is a function that helps express the stability condition.
> It is the function `J4` in https://arxiv.org/abs/hep-ph/0605184 [ref: arxiv\_hep\_ph\_0605184].

**`TwoHiggsDoublet.quarticTermReduced`**, a def, [line 585](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L585).

> A function related to the quartic term of the potential, used in the stableness
> condition and equivalent to the term `J4` in
> https://arxiv.org/abs/hep-ph/0605184 [ref: arxiv\_hep\_ph\_0605184].

```lean
noncomputable def quarticTermReduced (P : PotentialParameters) (k : EuclideanSpace ℝ (Fin 3)) : ℝ
```

**`TwoHiggsDoublet.quarticTermReduced_zero`**, a lemma, [line 590](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L590).

```lean
lemma quarticTermReduced_zero : quarticTermReduced 0 = 0
```

**`TwoHiggsDoublet.quarticTermReduced_stabilityCounterExample`**, a lemma, [line 594](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L594).

```lean
lemma quarticTermReduced_stabilityCounterExample (k : EuclideanSpace ℝ (Fin 3)) :
    quarticTermReduced .stabilityCounterExample k = (1 - k 0) ^ 2
```

**`TwoHiggsDoublet.quarticTermReduced_stabilityCounterExample_nonneg`**, a lemma, [line 600](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L600).

```lean
lemma quarticTermReduced_stabilityCounterExample_nonneg (k : EuclideanSpace ℝ (Fin 3)) :
    0 ≤ quarticTermReduced .stabilityCounterExample k
```

### E.5. Stability in terms of the gram vectors

> We give some necessary and sufficient conditions for the potential to be stable
> in terms of the gram vectors.
>
> This follows the analysis in https://arxiv.org/abs/hep-ph/0605184 [ref: arxiv\_hep\_ph\_0605184].
>
> We also give some necessary conditions.

**`TwoHiggsDoublet.potentialIsStable_iff_forall_gramVector`**, a lemma, [line 618](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L618).

```lean
lemma potentialIsStable_iff_forall_gramVector (P : PotentialParameters) :
    PotentialIsStable P ↔ ∃ c : ℝ, ∀ K : Fin 1 ⊕ Fin 3 → ℝ, 0 ≤ K (Sum.inl 0) →
      ∑ μ : Fin 3, K (Sum.inr μ) ^ 2 ≤ K (Sum.inl 0) ^ 2 →
      c ≤ ∑ μ, P.ξ μ * K μ + ∑ a, ∑ b, K a * K b * P.η a b
```

**`TwoHiggsDoublet.potentialIsStable_iff_forall_euclid`**, a lemma, [line 634](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L634).

```lean
lemma potentialIsStable_iff_forall_euclid (P : PotentialParameters) :
    PotentialIsStable P ↔ ∃ c, ∀ K0 : ℝ, ∀ K : EuclideanSpace ℝ (Fin 3), 0 ≤ K0 →
      ‖K‖ ^ 2 ≤ K0 ^ 2 → c ≤ P.ξ (Sum.inl 0) * K0 + ∑ μ, P.ξ (Sum.inr μ) * K μ
      + K0 ^ 2 * P.η (Sum.inl 0) (Sum.inl 0)
      + 2 * K0 * ∑ b, K b * P.η (Sum.inl 0) (Sum.inr b) +
      ∑ a, ∑ b, K a * K b * P.η (Sum.inr a) (Sum.inr b)
```

**`TwoHiggsDoublet.potentialIsStable_iff_forall_euclid_lt`**, a lemma, [line 665](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L665).

```lean
lemma potentialIsStable_iff_forall_euclid_lt (P : PotentialParameters) :
    PotentialIsStable P ↔ ∃ c ≤ 0, ∀ K0 : ℝ, ∀ K : EuclideanSpace ℝ (Fin 3), 0 < K0 →
      ‖K‖ ^ 2 ≤ K0 ^ 2 → c ≤ P.ξ (Sum.inl 0) * K0 + ∑ μ, P.ξ (Sum.inr μ) * K μ
      + K0 ^ 2 * P.η (Sum.inl 0) (Sum.inl 0)
      + 2 * K0 * ∑ b, K b * P.η (Sum.inl 0) (Sum.inr b) +
      ∑ a, ∑ b, K a * K b * P.η (Sum.inr a) (Sum.inr b)
```

**`TwoHiggsDoublet.potentialIsStable_iff_exists_forall_forall_reduced`**, a lemma, [line 684](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L684).

```lean
lemma potentialIsStable_iff_exists_forall_forall_reduced (P : PotentialParameters) :
    PotentialIsStable P ↔ ∃ c ≤ 0, ∀ K0 : ℝ, ∀ k : EuclideanSpace ℝ (Fin 3), 0 < K0 →
      ‖k‖ ^ 2 ≤ 1 → c ≤ K0 * massTermReduced P k + K0 ^ 2 * quarticTermReduced P k
```

**`TwoHiggsDoublet.quarticTermReduced_nonneg_of_potentialIsStable`**, a lemma, [line 713](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L713).

```lean
lemma quarticTermReduced_nonneg_of_potentialIsStable (P : PotentialParameters)
    (hP : PotentialIsStable P) (k : EuclideanSpace ℝ (Fin 3))
    (hk : ‖k‖ ^ 2 ≤ 1) : 0 ≤ quarticTermReduced P k
```

**`TwoHiggsDoublet.potentialIsStable_iff_massTermReduced_sq_le_quarticTermReduced`**, a lemma, [line 758](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L758).

```lean
lemma potentialIsStable_iff_massTermReduced_sq_le_quarticTermReduced (P : PotentialParameters) :
    PotentialIsStable P ↔ ∃ c, 0 ≤ c ∧ ∀ k : EuclideanSpace ℝ (Fin 3), ‖k‖ ^ 2 ≤ 1 →
      0 ≤ quarticTermReduced P k ∧
      (massTermReduced P k < 0 →
      massTermReduced P k ^ 2 ≤ 4 * quarticTermReduced P k * c)
```

**`TwoHiggsDoublet.massTermReduced_pos_of_quarticTermReduced_zero_potentialIsStable`**, a lemma, [line 824](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L824).

```lean
lemma massTermReduced_pos_of_quarticTermReduced_zero_potentialIsStable (P : PotentialParameters)
    (hP : PotentialIsStable P) (k : EuclideanSpace ℝ (Fin 3))
    (hk : ‖k‖ ^ 2 ≤ 1) (hq : quarticTermReduced P k = 0) : 0 ≤ massTermReduced P k
```

### E.6. Strong stability implies stability

> Stability in terms of the positivity of the quartic term, implies that the whole
> potential is stable.

**`TwoHiggsDoublet.potentialIsStable_of_strong`**, a lemma, [line 846](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L846).

> The potential is stable if it is strongly stable, i.e. its quartic term is always positive.
> The proof of this result relies on the compactness of the closed unit ball in
> `EuclideanSpace ℝ (Fin 3)`, and the `extreme value theorem`.

```lean
lemma potentialIsStable_of_strong (P : PotentialParameters)
    (h : ∀ k, ‖k‖ ^ 2 ≤ 1 → 0 < quarticTermReduced P k) :
    PotentialIsStable P
```

### E.7. Showing step in hep-ph/0605184 is invalid

**`TwoHiggsDoublet.forall_reduced_exists_not_potentialIsStable`**, a lemma, [line 887](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean#L887).

> A lemma invalidating the step in https://arxiv.org/pdf/hep-ph/0605184
> [ref: arxiv\_hep\_ph\_0605184] leading to equation (4.4).

```lean
lemma forall_reduced_exists_not_potentialIsStable :
    ∃ P, ¬ PotentialIsStable P ∧ (∀ k : EuclideanSpace ℝ (Fin 3), ‖k‖ ^ 2 ≤ 1 →
    0 ≤ quarticTermReduced P k ∧ (quarticTermReduced P k = 0 → 0 ≤ massTermReduced P k))
```

## Depends on

- [The gram matrix for the two Higgs doublet model](grammatrix.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/Potential.lean)
