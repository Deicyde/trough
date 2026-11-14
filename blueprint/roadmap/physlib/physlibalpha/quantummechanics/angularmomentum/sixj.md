---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.tripleH_stateA, PhyslibAlpha.Sl2.tripleCas_stateA, PhyslibAlpha.Sl2.tripleF_stateA, PhyslibAlpha.Sl2.tripleH_stateB, PhyslibAlpha.Sl2.tripleCas_stateB, PhyslibAlpha.Sl2.tripleE_stateB_succ, PhyslibAlpha.Sl2.tripleForm_stateB_self, PhyslibAlpha.Sl2.tripleForm_stateB_of_ne
statement: formalized
proof: formalized
---

# Recoupling coefficients and the 6j symbols

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.SixJ`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean): 27 declarations (1 instance with no name), 13 with a docstring.

> The recoupling coefficients between the two coupling schemes of `j₁ ⊗ j₂ ⊗ j₃` and the
> 6j symbols, with their independence of `M` and their orthogonality.

## i. Overview

> The two coupling schemes `stateA` and `stateB` of `CouplingSchemes` consist of eigenvectors of
> the total `J²` and `J_z`. The recoupling coefficient
> `⟨(j₁ j₂) j₁₂, j₃; J M | j₁, (j₂ j₃) j₂₃; J M⟩` is the contravariant form between the two
> (`recoupling`). The main results are:
>
> - both schemes consist of eigenvectors of the total `J²` and `J_z`, so states of different `J` or
>   `M` are orthogonal (`tripleForm_stateA_stateB_eq_zero`);
> - the first scheme is an orthonormal basis (`eq_sum_vecA`), so the recoupling coefficients form
>   an orthogonal matrix (`sum_recoupling_mul_recoupling`);
> - the recoupling coefficients do not depend on `M` (`recoupling_eq_recoupling_zero`): the total
>   lowering operator moves `M` in both schemes by the same factor `√((J + M)(J - M + 1))`, and it
>   is adjoint to the raising operator.
>
> The 6j symbol is defined by
> `⟨(j₁ j₂) j₁₂, j₃; J | j₁, (j₂ j₃) j₂₃; J⟩ = (-1)^(j₁ + j₂ + j₃ + J) √((2j₁₂ + 1)(2j₂₃ + 1))
> \{j₁ j₂ j₁₂; j₃ J j₂₃}` (`sixJ`), and satisfies
> `Σ_{j₁₂} (2j₁₂ + 1)(2j₂₃ + 1) {j₁ j₂ j₁₂; j₃ J j₂₃} {j₁ j₂ j₁₂; j₃ J j₂₃'} = δ_{j₂₃ j₂₃'}`
> (`sum_sixJ_mul_sixJ`).
>
> Racah's closed formula for the 6j symbols is not proved here.

## ii. Key results

> - `eq_sum_vecA`: completeness of the first scheme.
> - `tripleForm_stateA_stateB_eq_zero`: separation by `J` and `M`.
> - `recoupling`, `recoupling_eq_recoupling_zero`, `sum_recoupling_mul_recoupling`.
> - `sixJ`, `recoupling_eq_sixJ`, `sum_sixJ_mul_sixJ`.

## iv. References

> - G. Racah, *Theory of complex spectra. II*, Phys. Rev. 62, 438 (1942).
> - A. R. Edmonds, *Angular Momentum in Quantum Mechanics*, Princeton University Press (1957),
>   chapter 6.

## A. Eigenvalues, ladders and orthonormality of the coupled states

**`PhyslibAlpha.Sl2.tripleH_stateA`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L90).

```lean
lemma tripleH_stateA (l : ℕ) :
    tripleH a b c (stateA hab k₁ k₂ l) =
      (((a + b - 2 * (k₁ : ℕ) + c - 2 * k₂ : ℕ) : ℝ) - 2 * l) • stateA hab k₁ k₂ l
```

**`PhyslibAlpha.Sl2.tripleCas_stateA`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L96).

```lean
lemma tripleCas_stateA (l : ℕ) :
    tripleCas a b c (stateA hab k₁ k₂ l) =
      (((a + b - 2 * (k₁ : ℕ) + c - 2 * k₂ : ℕ) : ℝ) *
        (((a + b - 2 * (k₁ : ℕ) + c - 2 * k₂ : ℕ) : ℝ) + 2) / 2) • stateA hab k₁ k₂ l
```

**`PhyslibAlpha.Sl2.tripleF_stateA`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L103).

```lean
lemma tripleF_stateA {l : ℕ} (hl : l < a + b - 2 * (k₁ : ℕ) + c - 2 * k₂) :
    tripleF a b c (stateA hab k₁ k₂ l) =
      Real.sqrt (((l : ℝ) + 1) * (((a + b - 2 * (k₁ : ℕ) + c - 2 * k₂ : ℕ) : ℝ) - l)) •
        stateA hab k₁ k₂ (l + 1)
```

**`PhyslibAlpha.Sl2.tripleH_stateB`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L117).

```lean
lemma tripleH_stateB (l : ℕ) :
    tripleH a b c (stateB hbc k₃ k₄ l) =
      (((a + (b + c - 2 * (k₃ : ℕ)) - 2 * k₄ : ℕ) : ℝ) - 2 * l) • stateB hbc k₃ k₄ l
```

**`PhyslibAlpha.Sl2.tripleCas_stateB`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L123).

```lean
lemma tripleCas_stateB (l : ℕ) :
    tripleCas a b c (stateB hbc k₃ k₄ l) =
      (((a + (b + c - 2 * (k₃ : ℕ)) - 2 * k₄ : ℕ) : ℝ) *
        (((a + (b + c - 2 * (k₃ : ℕ)) - 2 * k₄ : ℕ) : ℝ) + 2) / 2) • stateB hbc k₃ k₄ l
```

**`PhyslibAlpha.Sl2.tripleE_stateB_succ`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L130).

```lean
lemma tripleE_stateB_succ {l : ℕ} (hl : l < a + (b + c - 2 * (k₃ : ℕ)) - 2 * k₄) :
    tripleE a b c (stateB hbc k₃ k₄ (l + 1)) =
      Real.sqrt (((l : ℝ) + 1) * (((a + (b + c - 2 * (k₃ : ℕ)) - 2 * k₄ : ℕ) : ℝ) - l)) •
        stateB hbc k₃ k₄ l
```

**`PhyslibAlpha.Sl2.tripleForm_stateB_self`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L137).

```lean
lemma tripleForm_stateB_self {l : ℕ} (hl : l ≤ a + (b + c - 2 * (k₃ : ℕ)) - 2 * k₄) :
    tripleForm a b c (stateB hbc k₃ k₄ l) (stateB hbc k₃ k₄ l) = 1
```

**`PhyslibAlpha.Sl2.tripleForm_stateB_of_ne`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L142).

```lean
lemma tripleForm_stateB_of_ne {k₃' : Fin (min b c + 1)} (hk : k₃ ≠ k₃') (k₄' l l' : ℕ) :
    tripleForm a b c (stateB hbc k₃ k₄ l) (stateB hbc k₃' k₄' l') = 0
```

### A.1. Completeness of the first coupling scheme

**`PhyslibAlpha.Sl2.eq_sum_of_orthonormal`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L155).

> An orthonormal family of `finrank` many vectors expands every vector.

```lean
lemma eq_sum_of_orthonormal {ι M : Type*} [Fintype ι] [DecidableEq ι] [Nonempty ι] [AddCommGroup M]
    [Module ℝ M] (B : LinearMap.BilinForm ℝ M) (v : ι → M)
    (hv : ∀ i j, B (v i) (v j) = if i = j then 1 else 0)
    (hcard : Fintype.card ι = Module.finrank ℝ M) (x : M) :
    x = ∑ i, B (v i) x • v i
```

**`PhyslibAlpha.Sl2.IndexA`**, an abbrev, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L179).

> The index set `(k₁, k₂, l)` of the first coupling scheme.

```lean
abbrev IndexA : Type
```

**An instance with no name**, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L181).

```lean
instance : Nonempty (IndexA a b c)
```

**`PhyslibAlpha.Sl2.vecA`**, a def, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L184).

> The states of the first coupling scheme, as a family indexed by `IndexA`.

```lean
def vecA (hab : 0 < a + b) (i : IndexA a b c) : Triple a b c
```

**`PhyslibAlpha.Sl2.card_indexA`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L186).

```lean
lemma card_indexA : Fintype.card (IndexA a b c) = Module.finrank ℝ (Triple a b c)
```

**`PhyslibAlpha.Sl2.tripleForm_vecA`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L195).

```lean
lemma tripleForm_vecA (hab : 0 < a + b) (hc : 0 < c) (i j : IndexA a b c) :
    tripleForm a b c (vecA hab i) (vecA hab j) = if i = j then 1 else 0
```

**`PhyslibAlpha.Sl2.eq_sum_vecA`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L219).

> **Completeness.** The states `|(j₁ j₂) j₁₂, j₃; J, M⟩` form an orthonormal basis.

```lean
lemma eq_sum_vecA (hab : 0 < a + b) (hc : 0 < c) (x : Triple a b c) :
    x = ∑ i, tripleForm a b c (vecA hab i) x • vecA hab i
```

### A.2. Separation by `J` and `M`

**`PhyslibAlpha.Sl2.nat_eq_of_mul_add_two_eq`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L229).

```lean
lemma nat_eq_of_mul_add_two_eq {p q : ℕ} (h : p * (p + 2) = q * (q + 2)) : p = q
```

**`PhyslibAlpha.Sl2.tripleForm_stateA_stateB_eq_zero`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L238).

> States of different total `J` or different `M` are orthogonal.

```lean
lemma tripleForm_stateA_stateB_eq_zero (hab : 0 < a + b) (hbc : 0 < b + c) (ha : 0 < a)
    (hc : 0 < c) {k₁ : Fin (min a b + 1)} {k₃ : Fin (min b c + 1)} {k₂ k₄ l' l : ℕ}
    (h₁ : k₂ ≤ a + b - 2 * (k₁ : ℕ)) (h₂ : k₂ ≤ c) (h₃ : k₄ ≤ a)
    (h₄ : k₄ ≤ b + c - 2 * (k₃ : ℕ)) (h : ¬((k₁ : ℕ) + k₂ = k₃ + k₄ ∧ l' = l)) :
    tripleForm a b c (stateA hab k₁ k₂ l') (stateB hbc k₃ k₄ l) = 0
```

### A.3. The recoupling coefficients

**`PhyslibAlpha.Sl2.ValidA`**, an abbrev, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L272).

> `k₁` gives an admissible intermediate `j₁₂` for the total `J = (a + b + c)/2 - K`.

```lean
abbrev ValidA (K k₁ : ℕ) : Prop
```

**`PhyslibAlpha.Sl2.ValidB`**, an abbrev, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L276).

> `k₃` gives an admissible intermediate `j₂₃` for the total `J = (a + b + c)/2 - K`.

```lean
abbrev ValidB (K k₃ : ℕ) : Prop
```

**`PhyslibAlpha.Sl2.recoupling`**, a def, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L280).

> The recoupling coefficient `⟨(j₁ j₂) j₁₂, j₃; J M | j₁, (j₂ j₃) j₂₃; J M⟩` with
> `J = (a + b + c)/2 - K`, `M = J - l`, `j₁₂ = (a + b)/2 - k₁` and `j₂₃ = (b + c)/2 - k₃`.

```lean
def recoupling (hab : 0 < a + b) (hbc : 0 < b + c) (K l : ℕ) (k₁ : Fin (min a b + 1))
    (k₃ : Fin (min b c + 1)) : ℝ
```

**`PhyslibAlpha.Sl2.recoupling_succ`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L284).

```lean
lemma recoupling_succ (hab : 0 < a + b) (hbc : 0 < b + c) (ha : 0 < a) {K l : ℕ}
    {k₁ : Fin (min a b + 1)} {k₃ : Fin (min b c + 1)} (hA : ValidA a b c K k₁)
    (hB : ValidB a b c K k₃) (hl : l < a + b + c - 2 * K) :
    recoupling hab hbc K (l + 1) k₁ k₃ = recoupling hab hbc K l k₁ k₃
```

**`PhyslibAlpha.Sl2.recoupling_eq_recoupling_zero`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L306).

> The recoupling coefficients do not depend on `M`.

```lean
lemma recoupling_eq_recoupling_zero (hab : 0 < a + b) (hbc : 0 < b + c) (ha : 0 < a)
    {K l : ℕ} {k₁ : Fin (min a b + 1)} {k₃ : Fin (min b c + 1)} (hA : ValidA a b c K k₁)
    (hB : ValidB a b c K k₃) (hl : l ≤ a + b + c - 2 * K) :
    recoupling hab hbc K l k₁ k₃ = recoupling hab hbc K 0 k₁ k₃
```

### A.4. Orthogonality

**`PhyslibAlpha.Sl2.sum_recoupling_mul_recoupling`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L323).

> **Orthogonality of the recoupling coefficients.** For fixed `J` and `M`,
> `Σ\_\{j₁₂} ⟨(j₁ j₂) j₁₂, j₃; J M | j₁, (j₂ j₃) j₂₃; J M⟩ ⟨(j₁ j₂) j₁₂, j₃; J M |
> j₁, (j₂ j₃) j₂₃'; J M⟩ = δ\_\{j₂₃ j₂₃'}`.

```lean
lemma sum_recoupling_mul_recoupling (hab : 0 < a + b) (hbc : 0 < b + c) (ha : 0 < a)
    (hc : 0 < c) {K l : ℕ} (hl : l ≤ a + b + c - 2 * K) {k₃ k₃' : Fin (min b c + 1)}
    (hB : ValidB a b c K k₃) (hB' : ValidB a b c K k₃') :
    ∑ k₁ : Fin (min a b + 1), (if ValidA a b c K k₁ then
      recoupling hab hbc K l k₁ k₃ * recoupling hab hbc K l k₁ k₃' else 0) =
        if k₃ = k₃' then 1 else 0
```

## B. The 6j symbols

**`PhyslibAlpha.Sl2.sixJ`**, a def, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L384).

> The **6j symbol** `{j₁ j₂ j₁₂; j₃ J j₂₃}`, with `j₁ = a/2`, `j₂ = b/2`, `j₃ = c/2`,
> `j₁₂ = (a + b)/2 - k₁`, `j₂₃ = (b + c)/2 - k₃` and `J = (a + b + c)/2 - K`, defined through
> `⟨(j₁ j₂) j₁₂, j₃; J | j₁, (j₂ j₃) j₂₃; J⟩ = (-1)^(j₁ + j₂ + j₃ + J) √((2j₁₂ + 1)(2j₂₃ + 1)) {6j}`
> (`j₁ + j₂ + j₃ + J = a + b + c - K`), and zero for inadmissible arguments.

```lean
def sixJ (hab : 0 < a + b) (hbc : 0 < b + c) (K : ℕ) (k₁ : Fin (min a b + 1))
    (k₃ : Fin (min b c + 1)) : ℝ
```

**`PhyslibAlpha.Sl2.recoupling_eq_sixJ`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L392).

> The recoupling coefficients in terms of the 6j symbols, for every `M`.

```lean
lemma recoupling_eq_sixJ (hab : 0 < a + b) (hbc : 0 < b + c) (ha : 0 < a) {K l : ℕ}
    {k₁ : Fin (min a b + 1)} {k₃ : Fin (min b c + 1)} (hA : ValidA a b c K k₁)
    (hB : ValidB a b c K k₃) (hl : l ≤ a + b + c - 2 * K) :
    recoupling hab hbc K l k₁ k₃ = (-1) ^ (a + b + c - K) *
      Real.sqrt (((a + b - 2 * (k₁ : ℕ) + 1 : ℕ) : ℝ) * ((b + c - 2 * (k₃ : ℕ) + 1 : ℕ) : ℝ)) *
        sixJ hab hbc K k₁ k₃
```

**`PhyslibAlpha.Sl2.mul_mul_div_mul_div_sqrt`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L406).

```lean
lemma mul_mul_div_mul_div_sqrt {s U U' p₁ p₃ p₃' : ℝ} (hs : s * s = 1) (h₁ : 0 < p₁) :
    p₁ * p₃ * (s * U / Real.sqrt (p₁ * p₃)) * (s * U' / Real.sqrt (p₁ * p₃')) =
      Real.sqrt p₃ / Real.sqrt p₃' * (U * U')
```

**`PhyslibAlpha.Sl2.sum_sixJ_mul_sixJ`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean#L417).

> **Orthogonality of the 6j symbols.**
> `Σ_{j₁₂} (2j₁₂ + 1)(2j₂₃ + 1) {j₁ j₂ j₁₂; j₃ J j₂₃} {j₁ j₂ j₁₂; j₃ J j₂₃'} = δ_{j₂₃ j₂₃'}`.

```lean
lemma sum_sixJ_mul_sixJ (hab : 0 < a + b) (hbc : 0 < b + c) (ha : 0 < a) (hc : 0 < c)
    {K : ℕ} {k₃ k₃' : Fin (min b c + 1)} (hB : ValidB a b c K k₃)
    (hB' : ValidB a b c K k₃') :
    ∑ k₁ : Fin (min a b + 1), ((a + b - 2 * (k₁ : ℕ) + 1 : ℕ) : ℝ) *
      ((b + c - 2 * (k₃ : ℕ) + 1 : ℕ) : ℝ) * sixJ hab hbc K k₁ k₃ * sixJ hab hbc K k₁ k₃' =
        if k₃ = k₃' then 1 else 0
```

## Depends on

- [The two coupling schemes of three angular momenta](couplingschemes.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJ.lean)
