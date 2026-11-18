---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.Adm3, PhyslibAlpha.Sl2.reggeJ, PhyslibAlpha.Sl2.threeJ, PhyslibAlpha.Sl2.threeJ_of_not, PhyslibAlpha.Sl2.adm3_of_threeJ_ne_zero, PhyslibAlpha.Sl2.isMagic_reggeJ, PhyslibAlpha.Sl2.reggeJ_row_sum, PhyslibAlpha.Sl2.threeJ_swap
statement: formalized
proof: formalized
---

# The tetrahedral symmetry of the 6j symbols

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.SixJSymmetry`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean): 38 declarations, 22 with a docstring.

> The 3j symbols with general arguments, the 6j symbols as sums over four 3j symbols, their
> agreement with the 6j symbols of `SixJ`, and the 24 symmetries of the tetrahedron.

## i. Overview

> `threeJ j₁ j₂ j₃ m₁ m₂ m₃` is the 3j symbol with spins and projections in doubled units, defined
> through the Regge square of `Wigner3j` and set to zero for inadmissible arguments. It changes by
> `(-1)^(j₁ + j₂ + j₃)` under an odd permutation of the columns and under `m ↦ -m`, and is invariant
> under cyclic permutations (`threeJ_swap`, `threeJ_cycle`, `threeJ_neg`).
>
> The 6j symbol
>
> `\{j₁ j₂ j₃; j₄ j₅ j₆} = Σ\_m (-1)^(Σ (jᵢ - mᵢ)) (j₁ j₂ j₃; -m₁ -m₂ -m₃) (j₁ j₅ j₆; m₁ -m₅ m₆)
> (j₄ j₂ j₆; m₄ m₂ -m₆) (j₄ j₅ j₃; -m₄ m₅ m₃)`
>
> (`sixJSym`) is attached to a tetrahedron whose four faces are the four triads. Each generator of
> its symmetry group is a change of summation variables, a permutation and sign change of the six
> projections, under which the four 3j symbols are permuted and transformed by the 3j symmetries;
> the signs cancel on the support. This gives
>
> - `sixJSym_swap₁₂`, `sixJSym_swap₂₃`: invariance under permutations of the columns;
> - `sixJSym_flip₁₂`: invariance under exchange of upper and lower arguments in two columns.
>
> Indexing the six arguments by the edges of the tetrahedron whose vertices `0, 1, 2, 3` are the
> triads `(j₁ j₂ j₃)`, `(j₁ j₅ j₆)`, `(j₄ j₂ j₆)`, `(j₄ j₅ j₃)` (`sixJSymEdge`), the three generators
> become the vertex permutations `(1 2)`, `(2 3)` and `(0 3)(1 2)`. These generate the symmetric
> group on the four vertices, so `sixJSymEdge_comp_map` gives invariance under every permutation of
> the triads. The action on the edges is faithful (`sym2_map_perm_injective`), so these are 24
> distinct symmetries.
>
> The connection to the recoupling coefficients of `SixJ` is `sixJ_eq_sixJSym`. Expanding both
> coupled states in the product basis writes `⟨(j₁ j₂) j₁₂, j₃; J M | j₁, (j₂ j₃) j₂₃; J M⟩` as a sum
> over four Clebsch–Gordan coefficients (`recoupling_eq_sum`). Summing over `M`, which by
> `recoupling_eq_recoupling_zero` multiplies by `2J + 1`, and converting the coefficients into 3j
> symbols turns every summand into a summand of `sixJSym` (`cg_four_eq`, `sum_sixJTerm_eq`).

## ii. Key results

> - `threeJ`, `threeJ_swap`, `threeJ_cycle`, `threeJ_neg`: the 3j symbol and its symmetries.
> - `sixJSym`: the 6j symbol as a sum over four 3j symbols.
> - `sixJSymEdge_comp_map`: invariance under all 24 symmetries of the tetrahedron, with the
>   generators `sixJSym_swap₁₂`, `sixJSym_swap₂₃`, `sixJSym_flip₁₂` as special cases.
> - `recoupling_eq_sum`: the recoupling coefficient through four Clebsch–Gordan coefficients.
> - `sixJ_eq_sixJSym`: the 6j symbols of `SixJ` are the symmetric sums.

## iv. References

> - G. Racah, *Theory of complex spectra. II*, Phys. Rev. 62, 438 (1942).
> - A. R. Edmonds, *Angular Momentum in Quantum Mechanics*, Princeton University Press (1957),
>   chapter 6.

## A. The 3j symbol with general arguments

**`PhyslibAlpha.Sl2.Adm3`**, an abbrev, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L85).

> Admissibility of `(j₁ j₂ j₃; m₁ m₂ m₃)` in doubled units: the projections add up to zero,
> `|mᵢ| ≤ jᵢ`, `jᵢ - mᵢ` is even and the triangle condition holds with even perimeter.

```lean
abbrev Adm3 (j₁ j₂ j₃ : ℕ) (m₁ m₂ m₃ : ℤ) : Prop
```

**`PhyslibAlpha.Sl2.reggeJ`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L92).

> The Regge square of `(j₁ j₂ j₃; m₁ m₂ m₃)` in doubled units.

```lean
def reggeJ (j₁ j₂ j₃ : ℕ) (m₁ m₂ m₃ : ℤ) : Fin 3 → Fin 3 → ℕ
```

**`PhyslibAlpha.Sl2.threeJ`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L99).

> The **3j symbol** `(j₁ j₂ j₃; m₁ m₂ m₃)` with `jᵢ` and `mᵢ` given in doubled units, zero for
> inadmissible arguments.

```lean
def threeJ (j₁ j₂ j₃ : ℕ) (m₁ m₂ m₃ : ℤ) : ℝ
```

**`PhyslibAlpha.Sl2.threeJ_of_not`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L104).

```lean
lemma threeJ_of_not (h : ¬Adm3 j₁ j₂ j₃ m₁ m₂ m₃) : threeJ j₁ j₂ j₃ m₁ m₂ m₃ = 0
```

**`PhyslibAlpha.Sl2.adm3_of_threeJ_ne_zero`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L107).

```lean
lemma adm3_of_threeJ_ne_zero (h : threeJ j₁ j₂ j₃ m₁ m₂ m₃ ≠ 0) : Adm3 j₁ j₂ j₃ m₁ m₂ m₃
```

**`PhyslibAlpha.Sl2.isMagic_reggeJ`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L111).

```lean
lemma isMagic_reggeJ (h : Adm3 j₁ j₂ j₃ m₁ m₂ m₃) : IsMagic (reggeJ j₁ j₂ j₃ m₁ m₂ m₃)
```

**`PhyslibAlpha.Sl2.reggeJ_row_sum`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L129).

```lean
lemma reggeJ_row_sum (h : Adm3 j₁ j₂ j₃ m₁ m₂ m₃) :
    reggeJ j₁ j₂ j₃ m₁ m₂ m₃ 0 0 + reggeJ j₁ j₂ j₃ m₁ m₂ m₃ 0 1 +
      reggeJ j₁ j₂ j₃ m₁ m₂ m₃ 0 2 = (j₁ + j₂ + j₃) / 2
```

**`PhyslibAlpha.Sl2.threeJ_swap`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L138).

> Exchange of the first two columns:
> `(j₂ j₁ j₃; m₂ m₁ m₃) = (-1)^(j₁+j₂+j₃) (j₁ j₂ j₃; m₁ m₂ m₃)`.

```lean
lemma threeJ_swap (j₁ j₂ j₃ : ℕ) (m₁ m₂ m₃ : ℤ) :
    threeJ j₂ j₁ j₃ m₂ m₁ m₃ = (-1) ^ ((j₁ + j₂ + j₃) / 2) * threeJ j₁ j₂ j₃ m₁ m₂ m₃
```

**`PhyslibAlpha.Sl2.threeJ_cycle`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L155).

> Cyclic permutation of the columns: `(j₂ j₃ j₁; m₂ m₃ m₁) = (j₁ j₂ j₃; m₁ m₂ m₃)`.

```lean
lemma threeJ_cycle (j₁ j₂ j₃ : ℕ) (m₁ m₂ m₃ : ℤ) :
    threeJ j₂ j₃ j₁ m₂ m₃ m₁ = threeJ j₁ j₂ j₃ m₁ m₂ m₃
```

**`PhyslibAlpha.Sl2.threeJ_neg`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L172).

> Reversal of the projections:
> `(j₁ j₂ j₃; -m₁ -m₂ -m₃) = (-1)^(j₁+j₂+j₃) (j₁ j₂ j₃; m₁ m₂ m₃)`.

```lean
lemma threeJ_neg (j₁ j₂ j₃ : ℕ) (m₁ m₂ m₃ : ℤ) :
    threeJ j₁ j₂ j₃ (-m₁) (-m₂) (-m₃) = (-1) ^ ((j₁ + j₂ + j₃) / 2) * threeJ j₁ j₂ j₃ m₁ m₂ m₃
```

**`PhyslibAlpha.Sl2.wigner3j_eq_threeJ`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L188).

> The 3j symbols of `Wigner3j` in terms of `threeJ`.

```lean
lemma wigner3j_eq_threeJ {m n k l α β : ℕ} (hkm : k ≤ m) (hkn : k ≤ n)
    (hl : l ≤ m + n - 2 * k) (hα : α ≤ m) (hβ : β ≤ n) :
    wigner3j m n k l α β = threeJ m n (m + n - 2 * k) ((m : ℤ) - 2 * α) ((n : ℤ) - 2 * β)
      (-(((m + n - 2 * k : ℕ) : ℤ) - 2 * l))
```

## B. The 6j symbol as a sum over four 3j symbols

**`PhyslibAlpha.Sl2.sixJTerm`**, a def, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L212).

> The summand of `sixJSym`:
> `(-1)^(Σ (jᵢ - mᵢ)) (j₁ j₂ j₃; -m₁ -m₂ -m₃) (j₁ j₅ j₆; m₁ -m₅ m₆) (j₄ j₂ j₆; m₄ m₂ -m₆)
> (j₄ j₅ j₃; -m₄ m₅ m₃)`.

```lean
def sixJTerm (j₁ j₂ j₃ j₄ j₅ j₆ : ℕ) (m : Fin 6 → ℤ) : ℝ
```

**`PhyslibAlpha.Sl2.sixJBox`**, a def, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L219).

> The projections `|mᵢ| ≤ jᵢ`.

```lean
def sixJBox (j₁ j₂ j₃ j₄ j₅ j₆ : ℕ) : Finset (Fin 6 → ℤ)
```

**`PhyslibAlpha.Sl2.mem_sixJBox`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L224).

```lean
lemma mem_sixJBox {j₁ j₂ j₃ j₄ j₅ j₆ : ℕ} {m : Fin 6 → ℤ} :
    m ∈ sixJBox j₁ j₂ j₃ j₄ j₅ j₆ ↔ (-(j₁ : ℤ) ≤ m 0 ∧ m 0 ≤ j₁) ∧
      (-(j₂ : ℤ) ≤ m 1 ∧ m 1 ≤ j₂) ∧ (-(j₃ : ℤ) ≤ m 2 ∧ m 2 ≤ j₃) ∧
        (-(j₄ : ℤ) ≤ m 3 ∧ m 3 ≤ j₄) ∧ (-(j₅ : ℤ) ≤ m 4 ∧ m 4 ≤ j₅) ∧
          (-(j₆ : ℤ) ≤ m 5 ∧ m 5 ≤ j₆)
```

**`PhyslibAlpha.Sl2.sixJSym`**, a def, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L233).

> The **6j symbol** `{j₁ j₂ j₃; j₄ j₅ j₆}` (doubled units) as a sum over the projections of
> four 3j symbols.

```lean
def sixJSym (j₁ j₂ j₃ j₄ j₅ j₆ : ℕ) : ℝ
```

## C. The tetrahedral symmetry

**`PhyslibAlpha.Sl2.neg_one_zpow_mul_pow_four`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L242).

```lean
lemma neg_one_zpow_mul_pow_four {S S' : ℤ} {p q r s : ℕ}
    (h : (S' + p + q + r + s) % 2 = S % 2) :
    (-1 : ℝ) ^ S' * ((-1) ^ p * (-1) ^ q * (-1) ^ r * (-1) ^ s) = (-1) ^ S
```

**`PhyslibAlpha.Sl2.prod_four_eq_zero_or`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L250).

```lean
lemma prod_four_eq_zero_or {F₁ F₂ F₃ F₄ : ℝ} {P : Prop}
    (h : F₁ ≠ 0 → F₂ ≠ 0 → F₃ ≠ 0 → F₄ ≠ 0 → P) : F₁ * F₂ * F₃ * F₄ = 0 ∨ P
```

**`PhyslibAlpha.Sl2.term_congr_1324`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L262).

```lean
lemma term_congr_1324 {S S' : ℤ} {p q r s : ℕ} {F₁ F₂ F₃ F₄ : ℝ}
    (h : F₁ ≠ 0 → F₂ ≠ 0 → F₃ ≠ 0 → F₄ ≠ 0 → (S' + p + q + r + s) % 2 = S % 2) :
    (-1 : ℝ) ^ S * (F₁ * F₂ * F₃ * F₄) =
      (-1) ^ S' * ((-1) ^ p * F₁ * ((-1) ^ q * F₃) * ((-1) ^ r * F₂) * ((-1) ^ s * F₄))
```

**`PhyslibAlpha.Sl2.term_congr_1243`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L274).

```lean
lemma term_congr_1243 {S S' : ℤ} {p q r s : ℕ} {F₁ F₂ F₃ F₄ : ℝ}
    (h : F₁ ≠ 0 → F₂ ≠ 0 → F₃ ≠ 0 → F₄ ≠ 0 → (S' + p + q + r + s) % 2 = S % 2) :
    (-1 : ℝ) ^ S * (F₁ * F₂ * F₃ * F₄) =
      (-1) ^ S' * ((-1) ^ p * F₁ * ((-1) ^ q * F₂) * ((-1) ^ r * F₄) * ((-1) ^ s * F₃))
```

**`PhyslibAlpha.Sl2.term_congr_4321`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L286).

```lean
lemma term_congr_4321 {S S' : ℤ} {F₁ F₂ F₃ F₄ : ℝ}
    (h : F₁ ≠ 0 → F₂ ≠ 0 → F₃ ≠ 0 → F₄ ≠ 0 → S' % 2 = S % 2) :
    (-1 : ℝ) ^ S * (F₁ * F₂ * F₃ * F₄) = (-1) ^ S' * (F₄ * F₃ * F₂ * F₁)
```

**`PhyslibAlpha.Sl2.threeJ_swap₂₃`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L297).

> Exchange of the last two columns:
> `(j₁ j₃ j₂; m₁ m₃ m₂) = (-1)^(j₁+j₂+j₃) (j₁ j₂ j₃; m₁ m₂ m₃)`.

```lean
lemma threeJ_swap₂₃ (j₁ j₂ j₃ : ℕ) (m₁ m₂ m₃ : ℤ) :
    threeJ j₁ j₃ j₂ m₁ m₃ m₂ = (-1) ^ ((j₁ + j₂ + j₃) / 2) * threeJ j₁ j₂ j₃ m₁ m₂ m₃
```

**`PhyslibAlpha.Sl2.threeJ_negCycle`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L302).

> `(j₂ j₃ j₁; -m₂ m₃ -m₁) = (-1)^(j₁+j₂+j₃) (j₁ j₂ j₃; m₁ m₂ -m₃)`.

```lean
lemma threeJ_negCycle (j₁ j₂ j₃ : ℕ) (x y z : ℤ) :
    threeJ j₂ j₃ j₁ (-y) z (-x) = (-1) ^ ((j₁ + j₂ + j₃) / 2) * threeJ j₁ j₂ j₃ x y (-z)
```

**`PhyslibAlpha.Sl2.sixJSym_swap₁₂`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L311).

> Exchange of the first two columns: `{j₂ j₁ j₃; j₅ j₄ j₆} = {j₁ j₂ j₃; j₄ j₅ j₆}`.

```lean
lemma sixJSym_swap₁₂ : sixJSym j₂ j₁ j₃ j₅ j₄ j₆ = sixJSym j₁ j₂ j₃ j₄ j₅ j₆
```

**`PhyslibAlpha.Sl2.sixJSym_swap₂₃`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L336).

> Exchange of the last two columns: `{j₁ j₃ j₂; j₄ j₆ j₅} = {j₁ j₂ j₃; j₄ j₅ j₆}`.

```lean
lemma sixJSym_swap₂₃ : sixJSym j₁ j₃ j₂ j₄ j₆ j₅ = sixJSym j₁ j₂ j₃ j₄ j₅ j₆
```

**`PhyslibAlpha.Sl2.sixJSym_flip₁₂`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L363).

> Exchange of upper and lower arguments in the first two columns:
> `{j₄ j₅ j₃; j₁ j₂ j₆} = {j₁ j₂ j₃; j₄ j₅ j₆}`.

```lean
lemma sixJSym_flip₁₂ : sixJSym j₄ j₅ j₃ j₁ j₂ j₆ = sixJSym j₁ j₂ j₃ j₄ j₅ j₆
```

**`PhyslibAlpha.Sl2.sixJSymEdge`**, a def, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L388).

> The 6j symbol as a function of the edge labels of the tetrahedron whose vertices are the four
> triads `0 = (j₁ j₂ j₃)`, `1 = (j₁ j₅ j₆)`, `2 = (j₄ j₂ j₆)`, `3 = (j₄ j₅ j₃)`.

```lean
def sixJSymEdge (j : Sym2 (Fin 4) → ℕ) : ℝ
```

**`PhyslibAlpha.Sl2.sixJSymEdge_comp_map_swap₁₂`**, a lemma, [line 391](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L391).

```lean
lemma sixJSymEdge_comp_map_swap₁₂ (j : Sym2 (Fin 4) → ℕ) :
    sixJSymEdge (j ∘ Sym2.map (Equiv.swap 1 2)) = sixJSymEdge j
```

**`PhyslibAlpha.Sl2.sixJSymEdge_comp_map_swap₂₃`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L402).

```lean
lemma sixJSymEdge_comp_map_swap₂₃ (j : Sym2 (Fin 4) → ℕ) :
    sixJSymEdge (j ∘ Sym2.map (Equiv.swap 2 3)) = sixJSymEdge j
```

**`PhyslibAlpha.Sl2.sixJSymEdge_comp_map_flip`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L413).

```lean
lemma sixJSymEdge_comp_map_flip (j : Sym2 (Fin 4) → ℕ) :
    sixJSymEdge (j ∘ Sym2.map (Equiv.swap 0 3 * Equiv.swap 1 2 : Equiv.Perm (Fin 4))) =
      sixJSymEdge j
```

**`PhyslibAlpha.Sl2.sixJSymEdge_comp_map_mul`**, a lemma, [line 431](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L431).

```lean
lemma sixJSymEdge_comp_map_mul {σ τ : Equiv.Perm (Fin 4)}
    (hσ : ∀ j, sixJSymEdge (j ∘ Sym2.map σ) = sixJSymEdge j)
    (hτ : ∀ j, sixJSymEdge (j ∘ Sym2.map τ) = sixJSymEdge j) (j : Sym2 (Fin 4) → ℕ) :
    sixJSymEdge (j ∘ Sym2.map (σ * τ : Equiv.Perm (Fin 4))) = sixJSymEdge j
```

**`PhyslibAlpha.Sl2.sixJSymEdge_comp_map`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L439).

> **Tetrahedral symmetry.** The 6j symbol is invariant under every permutation of the four
> triads.

```lean
lemma sixJSymEdge_comp_map (σ : Equiv.Perm (Fin 4)) (j : Sym2 (Fin 4) → ℕ) :
    sixJSymEdge (j ∘ Sym2.map σ) = sixJSymEdge j
```

**`PhyslibAlpha.Sl2.sym2_map_perm_injective`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L475).

> The permutations of the triads act faithfully on the edges, so the symmetries of
> `sixJSymEdge_comp_map` are 24 distinct permutations of the arguments.

```lean
lemma sym2_map_perm_injective :
    Function.Injective (fun σ : Equiv.Perm (Fin 4) => Sym2.map σ)
```

## D. The 6j symbols of `SixJ` as sums over four 3j symbols

**`PhyslibAlpha.Sl2.link_congr`**, a lemma, [line 493](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L493).

```lean
lemma link_congr {S : ℤ} {p₁ p₂ p₃ p₄ q₁ q₂ q₃ q₄ r : ℕ} {A B C T₁ T₂ T₃ T₄ : ℝ}
    (hA : 0 ≤ A) (hB : 0 ≤ B)
    (h : T₁ ≠ 0 → T₂ ≠ 0 → T₃ ≠ 0 → T₄ ≠ 0 →
      (S + p₁ + p₂ + p₃ + p₄ + q₁ + q₂ + q₃ + q₄ + r) % 2 = 0) :
    (-1) ^ p₂ * Real.sqrt B * T₂ * ((-1) ^ p₁ * Real.sqrt A * T₁ *
        ((-1) ^ p₄ * Real.sqrt B * T₄ * ((-1) ^ p₃ * Real.sqrt C * T₃))) =
      Real.sqrt (A * C) * B * (-1) ^ r * ((-1) ^ S *
        ((-1) ^ q₁ * T₁ * ((-1) ^ q₄ * T₄) * ((-1) ^ q₃ * T₃) * ((-1) ^ q₂ * T₂)))
```

**`PhyslibAlpha.Sl2.tripleForm_normVec_stateB`**, a lemma, [line 521](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L521).

```lean
lemma tripleForm_normVec_stateB (hbc : 0 < b + c) (k₃ : Fin (min b c + 1)) (k₄ l : ℕ)
    {α : ℕ} (hα : α ≤ a) (β γ : ℕ) :
    tripleForm a b c ((normVec a α ⊗ₜ normVec b β) ⊗ₜ normVec c γ) (stateB hbc k₃ k₄ l) =
      ∑ ν ∈ Finset.range (b + c - 2 * (k₃ : ℕ) + 1),
        cgCoefficient a (b + c - 2 * (k₃ : ℕ)) k₄ l α ν * cgCoefficient b c k₃ ν β γ
```

**`PhyslibAlpha.Sl2.recoupling_eq_sum`**, a lemma, [line 547](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L547).

> The recoupling coefficient as a sum over products of four Clebsch–Gordan coefficients.

```lean
lemma recoupling_eq_sum (hab : 0 < a + b) (hbc : 0 < b + c) (K l : ℕ) (k₁ : Fin (min a b + 1))
    (k₃ : Fin (min b c + 1)) :
    recoupling hab hbc K l k₁ k₃ =
      ∑ μ ∈ Finset.range (a + b - 2 * (k₁ : ℕ) + 1), ∑ γ ∈ Finset.range (c + 1),
        cgCoefficient (a + b - 2 * (k₁ : ℕ)) c (K - k₁) l μ γ *
          ∑ α ∈ Finset.range (a + 1), ∑ β ∈ Finset.range (b + 1),
            cgCoefficient a b k₁ μ α β *
              ∑ ν ∈ Finset.range (b + c - 2 * (k₃ : ℕ) + 1),
                cgCoefficient a (b + c - 2 * (k₃ : ℕ)) (K - k₃) l α ν *
                  cgCoefficient b c k₃ ν β γ
```

**`PhyslibAlpha.Sl2.cg_four_eq`**, a lemma, [line 571](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L571).

> One summand of `recoupling_eq_sum` is a summand of `sixJSym`.

```lean
lemma cg_four_eq {a b c e f g k₁ k₂ k₃ k₄ l μ γ α β ν : ℕ}
    (hab : 0 < a + b) (hbc : 0 < b + c) (hec : 0 < e + c) (haf : 0 < a + f)
    (he : e = a + b - 2 * k₁) (hf : f = b + c - 2 * k₃) (hg₂ : g = e + c - 2 * k₂)
    (hg₄ : g = a + f - 2 * k₄) (h₁a : k₁ ≤ a) (h₁b : k₁ ≤ b) (h₂e : k₂ ≤ e) (h₂c : k₂ ≤ c)
    (h₃b : k₃ ≤ b) (h₃c : k₃ ≤ c) (h₄a : k₄ ≤ a) (h₄f : k₄ ≤ f) (hl : l ≤ g) (hμ : μ ≤ e)
    (hγ : γ ≤ c) (hα : α ≤ a) (hβ : β ≤ b) (hν : ν ≤ f) :
    cgCoefficient e c k₂ l μ γ * (cgCoefficient a b k₁ μ α β *
        (cgCoefficient a f k₄ l α ν * cgCoefficient b c k₃ ν β γ)) =
      Real.sqrt (((e + 1 : ℕ) : ℝ) * ((f + 1 : ℕ) : ℝ)) * ((g + 1 : ℕ) : ℝ) *
        (-1) ^ (a + b + c - (k₁ + k₂)) *
          sixJTerm a b e c g f ![(a : ℤ) - 2 * α, (b : ℤ) - 2 * β, -((e : ℤ) - 2 * μ),
            (c : ℤ) - 2 * γ, (g : ℤ) - 2 * l, (f : ℤ) - 2 * ν]
```

**`PhyslibAlpha.Sl2.sum_sixJTerm_eq`**, a lemma, [line 600](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L600).

> The sum of `sixJTerm` over the six projections, written through `jᵢ - 2·index`.

```lean
lemma sum_sixJTerm_eq (a b c e f g : ℕ) :
    ∑ x ∈ Finset.range (g + 1) ×ˢ (Finset.range (e + 1) ×ˢ (Finset.range (c + 1) ×ˢ
        (Finset.range (a + 1) ×ˢ (Finset.range (b + 1) ×ˢ Finset.range (f + 1))))),
      sixJTerm a b e c g f ![(a : ℤ) - 2 * x.2.2.2.1, (b : ℤ) - 2 * x.2.2.2.2.1,
        -((e : ℤ) - 2 * x.2.1), (c : ℤ) - 2 * x.2.2.1, (g : ℤ) - 2 * x.1,
        (f : ℤ) - 2 * x.2.2.2.2.2] = sixJSym a b e c g f
```

**`PhyslibAlpha.Sl2.sixJ_eq_sixJSym`**, a lemma, [line 647](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean#L647).

> **The 6j symbols of `SixJ` are the symmetric sums over four 3j symbols.** With
> `j₁₂ = (a + b)/2 - k₁`, `j₂₃ = (b + c)/2 - k₃` and `J = (a + b + c)/2 - K`,
> `{j₁ j₂ j₁₂; j₃ J j₂₃}` of `sixJ` equals `sixJSym`.

```lean
lemma sixJ_eq_sixJSym (hab : 0 < a + b) (hbc : 0 < b + c) (ha : 0 < a) (hc : 0 < c) {K : ℕ}
    {k₁ : Fin (min a b + 1)} {k₃ : Fin (min b c + 1)} (hA : ValidA a b c K k₁)
    (hB : ValidB a b c K k₃) :
    sixJ hab hbc K k₁ k₃ =
      sixJSym a b (a + b - 2 * (k₁ : ℕ)) c (a + b + c - 2 * K) (b + c - 2 * (k₃ : ℕ))
```

## Depends on

- [Recoupling coefficients and the 6j symbols](sixj.md)
- [Wigner 3j symbols](wigner3j.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SixJSymmetry.lean)
