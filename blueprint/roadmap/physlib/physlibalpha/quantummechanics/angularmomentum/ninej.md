---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.sixJSym_eq_zero_of_lt, PhyslibAlpha.Sl2.nineJSym, PhyslibAlpha.Sl2.nineJSym_eq_sum, PhyslibAlpha.Sl2.nineJSym_transpose
statement: formalized
proof: formalized
---

# The 9j symbols

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.NineJ`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/NineJ.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NineJ.lean): 4 declarations, 4 with a docstring.

> The 9j symbols as sums over products of three 6j symbols, and their invariance under
> transposition.

## i. Overview

> In doubled units, the 9j symbol
> `{j₁₁ j₁₂ j₁₃; j₂₁ j₂₂ j₂₃; j₃₁ j₃₂ j₃₃}` is
> `Σ_J (-1)^J (J + 1) {j₁₁ j₂₁ j₃₁; j₃₂ j₃₃ J} {j₁₂ j₂₂ j₃₂; j₂₁ J j₂₃} {j₁₃ j₂₃ j₃₃; J j₁₁ j₁₂}`
> (`nineJSym`), with the 6j symbols `sixJSym` of `SixJSymmetry`. The first 6j symbol contains the
> triad `(j₁₁ j₃₃ J)`, so it vanishes for `J > j₁₁ + j₃₃` (`sixJSym_eq_zero_of_lt`) and the sum is
> over `J ≤ j₁₁ + j₃₃`. Extending the range does not change it (`nineJSym_eq_sum`).
>
> Transposition of the 3 × 3 array fixes `j₁₁` and `j₃₃`, and hence the range of summation. It
> exchanges the first and third 6j symbols and maps the second to itself, up to the tetrahedral
> symmetries `sixJSym_swap₁₂`, `sixJSym_swap₂₃`, `sixJSym_flip₁₂`. So the 9j symbol is invariant
> under transposition summand by summand (`nineJSym_transpose`).

## ii. Key results

> - `nineJSym`: the 9j symbol as a sum over products of three 6j symbols.
> - `nineJSym_eq_sum`: the sum may be taken over any larger range.
> - `nineJSym_transpose`: invariance under transposition.

## iv. References

> - NIST Digital Library of Mathematical Functions, §34.6, https://dlmf.nist.gov/34.6, equation
>   34.6.2, and §34.7, https://dlmf.nist.gov/34.7.
> - D. A. Varshalovich, A. N. Moskalev, V. K. Khersonskii, *Quantum Theory of Angular Momentum*,
>   World Scientific (1988), chapter 10.

## A. The 9j symbol

**`PhyslibAlpha.Sl2.sixJSym_eq_zero_of_lt`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NineJ.lean#L61).

> A 6j symbol whose triad `(j₁ j₅ j₆)` violates the triangle inequality `j₆ ≤ j₁ + j₅`
> vanishes.

```lean
lemma sixJSym_eq_zero_of_lt {j₁ j₂ j₃ j₄ j₅ j₆ : ℕ} (h : j₁ + j₅ < j₆) :
    sixJSym j₁ j₂ j₃ j₄ j₅ j₆ = 0
```

**`PhyslibAlpha.Sl2.nineJSym`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NineJ.lean#L72).

> The **9j symbol** `{j₁₁ j₁₂ j₁₃; j₂₁ j₂₂ j₂₃; j₃₁ j₃₂ j₃₃}` (doubled units) as a sum over
> products of three 6j symbols.

```lean
def nineJSym (j₁₁ j₁₂ j₁₃ j₂₁ j₂₂ j₂₃ j₃₁ j₃₂ j₃₃ : ℕ) : ℝ
```

**`PhyslibAlpha.Sl2.nineJSym_eq_sum`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NineJ.lean#L78).

> The sum defining `nineJSym` may be taken over any range containing `J ≤ j₁₁ + j₃₃`.

```lean
lemma nineJSym_eq_sum {j₁₁ j₁₂ j₁₃ j₂₁ j₂₂ j₂₃ j₃₁ j₃₂ j₃₃ N : ℕ} (hN : j₁₁ + j₃₃ < N) :
    nineJSym j₁₁ j₁₂ j₁₃ j₂₁ j₂₂ j₂₃ j₃₁ j₃₂ j₃₃ =
      ∑ J ∈ Finset.range N, (-1 : ℝ) ^ J * (J + 1) *
        (sixJSym j₁₁ j₂₁ j₃₁ j₃₂ j₃₃ J * sixJSym j₁₂ j₂₂ j₃₂ j₂₁ J j₂₃ *
          sixJSym j₁₃ j₂₃ j₃₃ J j₁₁ j₁₂)
```

## B. Invariance under transposition

**`PhyslibAlpha.Sl2.nineJSym_transpose`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NineJ.lean#L95).

> **Transposition symmetry.** The 9j symbol is invariant under exchange of rows and columns.

```lean
lemma nineJSym_transpose (j₁₁ j₁₂ j₁₃ j₂₁ j₂₂ j₂₃ j₃₁ j₃₂ j₃₃ : ℕ) :
    nineJSym j₁₁ j₂₁ j₃₁ j₁₂ j₂₂ j₃₂ j₁₃ j₂₃ j₃₃ =
      nineJSym j₁₁ j₁₂ j₁₃ j₂₁ j₂₂ j₂₃ j₃₁ j₃₂ j₃₃
```

## Depends on

- [The tetrahedral symmetry of the 6j symbols](sixjsymmetry.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/NineJ.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/NineJ.lean)
