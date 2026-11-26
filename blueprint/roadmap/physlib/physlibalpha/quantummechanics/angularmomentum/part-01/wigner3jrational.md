---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.invFactQ, PhyslibAlpha.Sl2.cast_invFactQ, PhyslibAlpha.Sl2.negOnePowQ, PhyslibAlpha.Sl2.cast_negOnePowQ, PhyslibAlpha.Sl2.sixTermQ, PhyslibAlpha.Sl2.cast_sixTermQ, PhyslibAlpha.Sl2.sixSumQ, PhyslibAlpha.Sl2.cast_sixSumQ
statement: formalized
proof: formalized
---

# Rational values of the Wigner 3j symbols

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.Wigner3jRational`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean): 18 declarations, 11 with a docstring.

> Computable rational functions for the square of the 3j symbol of a Regge square and for that
> symbol times its absolute value, with proofs that they agree with the real definitions of
> `Wigner3j`.

## i. Overview

> The 3j symbol `threeJR R = (-1)^(R₂₀ + R₁₁) √(∏ R_ij! / (J + 1)!) · S` of a Regge square `R`
> contains a square root and a `finsum`, so it cannot be evaluated. Its square and the product
> `threeJR R · |threeJR R|` are rational:
>
> - `threeJR R ^ 2 = ∏ R_ij! / (J + 1)! · S²`,
> - `threeJR R · |threeJR R| = (-1)^(R₂₀ + R₁₁) ∏ R_ij! / (J + 1)! · S |S|`,
>
> where the six-factorial sum `S` is a finite sum of rationals over the range in which all
> factorials have nonnegative arguments (`sixSumQ`). The second form keeps the sign.
>
> The functions below are defined by finite sums and products over `ℚ`, so concrete values can be
> checked in the kernel with `decide +kernel`.

## ii. Key results

> - `sixSumQ`, `cast_sixSumQ`: the six-factorial sum over `ℚ`.
> - `threeJRSqQ`, `cast_threeJRSqQ`: `threeJR R ^ 2` over `ℚ`.
> - `threeJRSgnSqQ`, `cast_threeJRSgnSqQ`: `threeJR R · |threeJR R|` over `ℚ`.

## iv. References

> - D. A. Varshalovich, A. N. Moskalev, V. K. Khersonskii, *Quantum Theory of Angular Momentum*,
>   World Scientific (1988): Sec. 8.1.3, p. 237, Eqs. 8.1(14)–(18) (the Regge symbol); Sec. 8.2,
>   p. 237, Eq. 8.2(1) (the Δ symbol); Sec. 8.2.1, p. 238, Eq. 8.2(3) (Racah's sum for the
>   Clebsch–Gordan coefficients).
> - NIST Digital Library of Mathematical Functions, Sec. 34.2, Eqs. 34.2.4–34.2.5,
>   https://dlmf.nist.gov/34.2.

## A. The six-factorial sum over ℚ

**`PhyslibAlpha.Sl2.invFactQ`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L63).

> `1/u!` in `ℚ` for `u ≥ 0` and `0` for `u < 0`.

```lean
def invFactQ (u : ℤ) : ℚ
```

**`PhyslibAlpha.Sl2.cast_invFactQ`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L65).

```lean
lemma cast_invFactQ (u : ℤ) : (invFactQ u : ℝ) = invFact u
```

**`PhyslibAlpha.Sl2.negOnePowQ`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L70).

> `(-1)^z` in `ℚ`, by the parity of `z`.

```lean
def negOnePowQ (z : ℤ) : ℚ
```

**`PhyslibAlpha.Sl2.cast_negOnePowQ`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L72).

```lean
lemma cast_negOnePowQ (z : ℤ) : (negOnePowQ z : ℝ) = (-1) ^ z
```

**`PhyslibAlpha.Sl2.sixTermQ`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L81).

> The summand of `sixSumQ`.

```lean
def sixTermQ (a₁ a₂ a₃ b₁ b₂ b₃ z : ℤ) : ℚ
```

**`PhyslibAlpha.Sl2.cast_sixTermQ`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L85).

```lean
lemma cast_sixTermQ (a₁ a₂ a₃ b₁ b₂ b₃ z : ℤ) :
    (sixTermQ a₁ a₂ a₃ b₁ b₂ b₃ z : ℝ) = sixTerm a₁ a₂ a₃ b₁ b₂ b₃ z
```

**`PhyslibAlpha.Sl2.sixSumQ`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L91).

> The six-factorial sum over `ℚ`, over the range `max aᵢ ≤ z ≤ min bᵢ` outside of which all
> summands vanish.

```lean
def sixSumQ (a₁ a₂ a₃ b₁ b₂ b₃ : ℤ) : ℚ
```

**`PhyslibAlpha.Sl2.cast_sixSumQ`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L94).

```lean
lemma cast_sixSumQ (a₁ a₂ a₃ b₁ b₂ b₃ : ℤ) :
    (sixSumQ a₁ a₂ a₃ b₁ b₂ b₃ : ℝ) = sixSum a₁ a₂ a₃ b₁ b₂ b₃
```

## B. The 3j symbol of a Regge square

**`PhyslibAlpha.Sl2.threeJRRadQ`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L118).

> The rational number `∏ R_ij! / (J + 1)!` under the square root of `threeJR`.

```lean
def threeJRRadQ (R : Fin 3 → Fin 3 → ℕ) : ℚ
```

**`PhyslibAlpha.Sl2.threeJRSumQ`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L122).

> The six-factorial sum of `threeJR` over `ℚ`.

```lean
def threeJRSumQ (R : Fin 3 → Fin 3 → ℕ) : ℚ
```

**`PhyslibAlpha.Sl2.threeJRSqQ`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L126).

> `threeJR R ^ 2` over `ℚ`.

```lean
def threeJRSqQ (R : Fin 3 → Fin 3 → ℕ) : ℚ
```

**`PhyslibAlpha.Sl2.threeJRSgnSqQ`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L129).

> `threeJR R · |threeJR R|` over `ℚ`.

```lean
def threeJRSgnSqQ (R : Fin 3 → Fin 3 → ℕ) : ℚ
```

**`PhyslibAlpha.Sl2.cast_threeJRRadQ`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L132).

```lean
lemma cast_threeJRRadQ (R : Fin 3 → Fin 3 → ℕ) : (threeJRRadQ R : ℝ) =
    (∏ i, ∏ j, ((R i j).factorial : ℝ)) / ((R 0 0 + R 0 1 + R 0 2 + 1).factorial : ℝ)
```

**`PhyslibAlpha.Sl2.threeJRRadQ_nonneg`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L136).

```lean
lemma threeJRRadQ_nonneg (R : Fin 3 → Fin 3 → ℕ) : 0 ≤ (threeJRRadQ R : ℝ)
```

**`PhyslibAlpha.Sl2.cast_threeJRSumQ`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L140).

```lean
lemma cast_threeJRSumQ (R : Fin 3 → Fin 3 → ℕ) : (threeJRSumQ R : ℝ) =
    sixSum 0 ((R 1 0 : ℤ) - R 0 1) ((R 2 1 : ℤ) - R 0 0) (R 0 2) (R 1 0) (R 2 1)
```

**`PhyslibAlpha.Sl2.threeJR_eq_rat`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L146).

> The 3j symbol of a Regge square in terms of the rational radicand `threeJRRadQ` and the
> rational six-factorial sum `threeJRSumQ`.

```lean
lemma threeJR_eq_rat (R : Fin 3 → Fin 3 → ℕ) :
    threeJR R = (-1) ^ (R 2 0 + R 1 1) * Real.sqrt (threeJRRadQ R : ℝ) * (threeJRSumQ R : ℝ)
```

**`PhyslibAlpha.Sl2.cast_threeJRSqQ`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L151).

> `threeJRSqQ R` is the square of the 3j symbol of the Regge square `R`.

```lean
lemma cast_threeJRSqQ (R : Fin 3 → Fin 3 → ℕ) : (threeJRSqQ R : ℝ) = threeJR R ^ 2
```

**`PhyslibAlpha.Sl2.cast_threeJRSgnSqQ`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean#L158).

> `threeJRSgnSqQ R` is the 3j symbol of the Regge square `R` times its absolute value.

```lean
lemma cast_threeJRSgnSqQ (R : Fin 3 → Fin 3 → ℕ) :
    (threeJRSgnSqQ R : ℝ) = threeJR R * |threeJR R|
```

## C. Examples

> Two values checked in the kernel. The Regge square of `(j₁ j₂ j₃; m₁ m₂ m₃)` has the rows
> `(-j₁ + j₂ + j₃, j₁ - j₂ + j₃, j₁ + j₂ - j₃)`, `(j₁ - m₁, j₂ - m₂, j₃ - m₃)` and
> `(j₁ + m₁, j₂ + m₂, j₃ + m₃)`.

## Depends on

- [Wigner 3j symbols](wigner3j.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/Wigner3jRational.lean)
