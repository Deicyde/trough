---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.threeJSqQ, PhyslibAlpha.Sl2.threeJSgnSqQ, PhyslibAlpha.Sl2.cast_threeJSqQ, PhyslibAlpha.Sl2.cast_threeJSgnSqQ, PhyslibAlpha.Sl2.threeJ_eq_sign_mul_sqrt, PhyslibAlpha.Sl2.sq_cgCoefficient, PhyslibAlpha.Sl2.triangleSqQ, PhyslibAlpha.Sl2.facPairQ
statement: formalized
proof: formalized
---

# Rational values of the Wigner 3j symbols with general arguments

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.ThreeJRational`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean): 14 declarations, 11 with a docstring.

> The 3j symbols `threeJ` squared, and times their absolute value, as rational numbers, through the
> rational values of the 3j symbols of a Regge square in `Wigner3jRational`.

## i. Overview

> `threeJ j₁ j₂ j₃ m₁ m₂ m₃` is the 3j symbol `threeJR` of the Regge square
> `reggeJ j₁ j₂ j₃ m₁ m₂ m₃` for admissible arguments and `0` otherwise. The rational functions of
> `Wigner3jRational` therefore give its square and its product with its absolute value as rational
> numbers (`threeJSqQ`, `threeJSgnSqQ`), and the 3j symbol is `sign(q) √|q|` with
> `q = threeJSgnSqQ` (`threeJ_eq_sign_mul_sqrt`). The same gives the squares of the Clebsch–Gordan
> coefficients (`sq_cgCoefficient`). Section C checks proven identities in the kernel with
> `decide +kernel`: the diagonal orthogonality relations and the symmetries of `SixJSymmetry` on a
> grid of small spins.
>
> For an admissible symbol the radicand `∏ R_ij! / (J + 1)!` splits into the triangle coefficient
> `Δ(j₁j₂j₃)²` and the factorials `(jᵢ - mᵢ)! (jᵢ + mᵢ)!` of the projections (`threeJRRadQ_reggeJ`),
> so `threeJ = √(Δ² ∏ᵢ (jᵢ - mᵢ)! (jᵢ + mᵢ)!) · threeJNumQ` (`threeJ_eq_sqrt_mul`). This is the form
> in which the four 3j symbols of a 6j symbol combine in `SixJRational`.

## ii. Key results

> - `threeJSqQ`, `cast_threeJSqQ`, `threeJSgnSqQ`, `cast_threeJSgnSqQ`: `threeJ ^ 2` and
>   `threeJ · |threeJ|` over `ℚ`.
> - `threeJ_eq_sign_mul_sqrt`: `threeJ = sign(q) √|q|` with `q = threeJSgnSqQ`.
> - `sq_cgCoefficient`: the square of a Clebsch–Gordan coefficient as a rational number.
> - `triangleSqQ`, `facPairQ`, `threeJNumQ`: the triangle coefficient, the factorials of the
>   projections and the 3j symbol without its square root, over `ℚ`.
> - `threeJ_eq_sqrt_mul`: `threeJ = √(Δ² ∏ᵢ (jᵢ - mᵢ)! (jᵢ + mᵢ)!) · threeJNumQ`.

## iv. References

> - D. A. Varshalovich, A. N. Moskalev, V. K. Khersonskii, *Quantum Theory of Angular Momentum*,
>   World Scientific (1988): Sec. 8.1.3, p. 237, Eqs. 8.1(14)–(18) (the Regge symbol); Sec. 8.2,
>   p. 237, Eq. 8.2(1) (the Δ symbol); Sec. 8.2.1, p. 238, Eq. 8.2(3) (Racah's sum for the
>   Clebsch–Gordan coefficients).
> - NIST Digital Library of Mathematical Functions, Sec. 34.2, Eqs. 34.2.4–34.2.5,
>   https://dlmf.nist.gov/34.2.

## A. The 3j symbol with general arguments

**`PhyslibAlpha.Sl2.threeJSqQ`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean#L73).

> `threeJ j₁ j₂ j₃ m₁ m₂ m₃ ^ 2` over `ℚ` (doubled units).

```lean
def threeJSqQ (j₁ j₂ j₃ : ℕ) (m₁ m₂ m₃ : ℤ) : ℚ
```

**`PhyslibAlpha.Sl2.threeJSgnSqQ`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean#L77).

> `threeJ j₁ j₂ j₃ m₁ m₂ m₃ · |threeJ j₁ j₂ j₃ m₁ m₂ m₃|` over `ℚ` (doubled units).

```lean
def threeJSgnSqQ (j₁ j₂ j₃ : ℕ) (m₁ m₂ m₃ : ℤ) : ℚ
```

**`PhyslibAlpha.Sl2.cast_threeJSqQ`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean#L83).

> `threeJSqQ` is the square of the 3j symbol `threeJ`.

```lean
lemma cast_threeJSqQ : (threeJSqQ j₁ j₂ j₃ m₁ m₂ m₃ : ℝ) = threeJ j₁ j₂ j₃ m₁ m₂ m₃ ^ 2
```

**`PhyslibAlpha.Sl2.cast_threeJSgnSqQ`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean#L90).

> `threeJSgnSqQ` is the 3j symbol `threeJ` times its absolute value.

```lean
lemma cast_threeJSgnSqQ :
    (threeJSgnSqQ j₁ j₂ j₃ m₁ m₂ m₃ : ℝ) =
      threeJ j₁ j₂ j₃ m₁ m₂ m₃ * |threeJ j₁ j₂ j₃ m₁ m₂ m₃|
```

**`PhyslibAlpha.Sl2.threeJ_eq_sign_mul_sqrt`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean#L100).

> **The 3j symbol from a rational number.** `threeJ = sign(q) √|q|` with
> `q = threeJSgnSqQ`.

```lean
lemma threeJ_eq_sign_mul_sqrt :
    threeJ j₁ j₂ j₃ m₁ m₂ m₃ =
      Real.sign (threeJSgnSqQ j₁ j₂ j₃ m₁ m₂ m₃ : ℝ) *
        Real.sqrt |(threeJSgnSqQ j₁ j₂ j₃ m₁ m₂ m₃ : ℝ)|
```

## B. The Clebsch–Gordan coefficients

**`PhyslibAlpha.Sl2.sq_cgCoefficient`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean#L122).

> **Clebsch–Gordan coefficients squared are rational.**
> `⟨j₁ m₁ j₂ m₂ | J M⟩² = (2J + 1) (j₁ j₂ J; m₁ m₂ -M)²`, in the parameters of
> `ClebschGordanCoefficients`.

```lean
lemma sq_cgCoefficient {m n : ℕ} (hmn : 0 < m + n) {k l α β : ℕ} (hkm : k ≤ m) (hkn : k ≤ n)
    (hl : l ≤ m + n - 2 * k) (hα : α ≤ m) (hβ : β ≤ n) :
    cgCoefficient m n k l α β ^ 2 = ((m + n - 2 * k + 1 : ℕ) : ℝ) *
      (threeJSqQ m n (m + n - 2 * k) ((m : ℤ) - 2 * α) ((n : ℤ) - 2 * β)
        (-(((m + n - 2 * k : ℕ) : ℤ) - 2 * l)) : ℝ)
```

## C. Checks in the kernel

> Proven identities, evaluated with `decide +kernel` on small spins (doubled units). The
> orthogonality relations involving two different 3j symbols are not rational term by term, so only
> the diagonal relations are checked.

## D. Triangle coefficients and the 3j symbols

**`PhyslibAlpha.Sl2.triangleSqQ`**, a def, [line 193](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean#L193).

> `Δ(j₁ j₂ j₃)² = (j₁+j₂-j₃)! (j₁-j₂+j₃)! (-j₁+j₂+j₃)! / (j₁+j₂+j₃+1)!` in doubled units.

```lean
def triangleSqQ (j₁ j₂ j₃ : ℕ) : ℚ
```

**`PhyslibAlpha.Sl2.facPairQ`**, a def, [line 198](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean#L198).

> `(j - m)! (j + m)!` in doubled units.

```lean
def facPairQ (j : ℕ) (m : ℤ) : ℚ
```

**`PhyslibAlpha.Sl2.facPairQ_neg`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean#L201).

```lean
lemma facPairQ_neg (j : ℕ) (m : ℤ) : facPairQ j (-m) = facPairQ j m
```

**`PhyslibAlpha.Sl2.facPairQ_nonneg`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean#L204).

```lean
lemma facPairQ_nonneg (j : ℕ) (m : ℤ) : 0 ≤ facPairQ j m
```

**`PhyslibAlpha.Sl2.triangleSqQ_nonneg`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean#L208).

```lean
lemma triangleSqQ_nonneg (j₁ j₂ j₃ : ℕ) : 0 ≤ triangleSqQ j₁ j₂ j₃
```

**`PhyslibAlpha.Sl2.threeJNumQ`**, a def, [line 213](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean#L213).

> The 3j symbol without its square root: `(-1)^(R₂₀ + R₁₁)` times the six-factorial sum.

```lean
def threeJNumQ (j₁ j₂ j₃ : ℕ) (m₁ m₂ m₃ : ℤ) : ℚ
```

**`PhyslibAlpha.Sl2.threeJRRadQ_reggeJ`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean#L219).

> The radicand of the 3j symbol splits into the triangle coefficient and the factorials of the
> projections.

```lean
lemma threeJRRadQ_reggeJ {j₁ j₂ j₃ : ℕ} {m₁ m₂ m₃ : ℤ} (h : Adm3 j₁ j₂ j₃ m₁ m₂ m₃) :
    threeJRRadQ (reggeJ j₁ j₂ j₃ m₁ m₂ m₃) =
      triangleSqQ j₁ j₂ j₃ * facPairQ j₁ m₁ * facPairQ j₂ m₂ * facPairQ j₃ m₃
```

**`PhyslibAlpha.Sl2.threeJ_eq_sqrt_mul`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean#L228).

> `threeJ = √(Δ² (j₁-m₁)!(j₁+m₁)! (j₂-m₂)!(j₂+m₂)! (j₃-m₃)!(j₃+m₃)!) · threeJNumQ`.

```lean
lemma threeJ_eq_sqrt_mul {j₁ j₂ j₃ : ℕ} {m₁ m₂ m₃ : ℤ} (h : Adm3 j₁ j₂ j₃ m₁ m₂ m₃) :
    threeJ j₁ j₂ j₃ m₁ m₂ m₃ =
      Real.sqrt ((triangleSqQ j₁ j₂ j₃ * facPairQ j₁ m₁ * facPairQ j₂ m₂ * facPairQ j₃ m₃ : ℚ) :
        ℝ) * (threeJNumQ j₁ j₂ j₃ m₁ m₂ m₃ : ℝ)
```

## Depends on

- [The tetrahedral symmetry of the 6j symbols](sixjsymmetry.md)
- [Rational values of the Wigner 3j symbols](wigner3jrational.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/AngularMomentum/ThreeJRational.lean)
