---
declaration: module
origin: cited
lean: QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction, QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_eq, QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_zero, QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_eq_mul_eigenfunction_zero, QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_integrable, QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_conj, QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_point_norm, QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_point_norm_sq
statement: formalized
proof: formalized
---

# Eigenfunction of the Harmonic Oscillator

The module `Physlib.QuantumMechanics.HarmonicOscillator.OneDimension.Eigenfunction`, [Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean): 20 declarations, 14 with a docstring.

> Note: These eigenfunctions have been generalized to `d` dimensions in
> `QuantumMechanics/HarmonicOscillator/Eigenstates.lean`.

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction`**, a def, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L38).

> The `n`th eigenfunction of the Harmonic oscillator is defined as the function `ℝ → ℂ`
> taking `x : ℝ` to
>
> `1/√(2^n n!) 1/√(√π ξ) * physHermite n (x / ξ) * e ^ (- x²/ (2 ξ²))`.

```lean
noncomputable def eigenfunction (n : ℕ) : ℝ → ℂ
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_eq`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L42).

```lean
lemma eigenfunction_eq (n : ℕ) :
    Q.eigenfunction n = fun (x : ℝ) => (1/√(2 ^ n * n !) * (1/ √(√Real.pi * Q.ξ))) *
    Complex.ofReal (physHermite n (x / Q.ξ) * Real.exp (- x^2 / (2 * Q.ξ^2)))
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_zero`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L51).

```lean
lemma eigenfunction_zero : Q.eigenfunction 0 = fun (x : ℝ) =>
    (1/ √(√Real.pi * Q.ξ)) * Complex.exp (- x^2 / (2 * Q.ξ^2))
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_eq_mul_eigenfunction_zero`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L56).

```lean
lemma eigenfunction_eq_mul_eigenfunction_zero (n : ℕ) :
    Q.eigenfunction n = fun x => Complex.ofReal (1/√(2 ^ n * n !))
    * Complex.ofReal (physHermite n (x / Q.ξ)) * Q.eigenfunction 0 x
```

## Basic properties of the eigenfunctions

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_integrable`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L77).

> The eigenfunctions are integrable.

```lean
lemma eigenfunction_integrable (n : ℕ) : Integrable (Q.eigenfunction n)
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_conj`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L92).

> The eigenfunctions are real.

```lean
lemma eigenfunction_conj (n : ℕ) (x : ℝ) :
    (starRingEnd ℂ) (Q.eigenfunction n x) = Q.eigenfunction n x
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_point_norm`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L97).

```lean
lemma eigenfunction_point_norm (n : ℕ) (x : ℝ) :
    ‖Q.eigenfunction n x‖ = (1/√(2 ^ n * n !) * (1/ √(√Real.pi * Q.ξ))) *
    (|physHermite n (x / Q.ξ)| * Real.exp (- x ^ 2 / (2 * Q.ξ ^ 2)))
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_point_norm_sq`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L112).

```lean
lemma eigenfunction_point_norm_sq (n : ℕ) (x : ℝ) :
    ‖Q.eigenfunction n x‖ ^ 2 = (1/√(2 ^ n * n !) * (1/ √(√Real.pi * Q.ξ))) ^ 2 *
    ((physHermite n (x / Q.ξ)) ^ 2 * Real.exp (- x^2 / Q.ξ ^ 2))
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_square_integrable`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L128).

> The eigenfunctions are square integrable.

```lean
lemma eigenfunction_square_integrable (n : ℕ) :
    MeasureTheory.Integrable (fun x => ‖Q.eigenfunction n x‖ ^ 2)
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_aeStronglyMeasurable`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L146).

> The eigenfunctions are almost everywhere strongly measurable.

```lean
lemma eigenfunction_aeStronglyMeasurable (n : ℕ) :
    MeasureTheory.AEStronglyMeasurable (Q.eigenfunction n)
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_memHS`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L151).

> The eigenfunctions are members of the Hilbert space.

```lean
lemma eigenfunction_memHS (n : ℕ) : MemHS (Q.eigenfunction n)
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_differentiableAt`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L157).

> The eigenfunctions are differentiable.

```lean
lemma eigenfunction_differentiableAt (x : ℝ) (n : ℕ) :
    DifferentiableAt ℝ (Q.eigenfunction n) x
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_continuous`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L164).

> The eigenfunctions are continuous.

```lean
lemma eigenfunction_continuous (n : ℕ) : Continuous (Q.eigenfunction n)
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_parity`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L170).

> The `n`th eigenfunction is an eigenfunction of the parity operator with
> the eigenvalue `(-1) ^ n`.

```lean
lemma eigenfunction_parity (n : ℕ) :
    parityOperator (Q.eigenfunction n) = (-1) ^ n * Q.eigenfunction n
```

## Orthonormality

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_mul`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L188).

> A simplification of the product of two eigenfunctions.

```lean
lemma eigenfunction_mul (n p : ℕ) :
    (Q.eigenfunction n x) * (Q.eigenfunction p x) =
    1/√(2 ^ n * n !) * 1/√(2 ^ p * p !) * (1/ (√Real.pi * Q.ξ)) * Complex.ofReal
    (physHermite n (x / Q.ξ) * physHermite p (x / Q.ξ) * Real.exp (- x^2 / Q.ξ^2))
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_mul_self`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L220).

```lean
lemma eigenfunction_mul_self (n : ℕ) : (Q.eigenfunction n x) * (Q.eigenfunction n x) =
    (1/ (2 ^ n * n !) * (1/ (√Real.pi * Q.ξ))) *
    Complex.ofReal ((physHermite n (x / Q.ξ))^2 * Real.exp (- x^2 / Q.ξ^2))
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_normalized`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L243).

> The eigenfunction are normalized.

```lean
lemma eigenfunction_normalized (n : ℕ) : ⟪HilbertSpace.mk (Q.eigenfunction_memHS n),
    HilbertSpace.mk (Q.eigenfunction_memHS n)⟫_ℂ = 1
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_orthogonal`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L266).

> The eigenfunctions of the quantum harmonic oscillator are orthogonal.

```lean
lemma eigenfunction_orthogonal {n p : ℕ} (hnp : n ≠ p) :
    ⟪HilbertSpace.mk (Q.eigenfunction_memHS n),
      HilbertSpace.mk (Q.eigenfunction_memHS p)⟫_ℂ = 0
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_orthonormal`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L285).

> The eigenfunctions are orthonormal within the Hilbert space.

```lean
lemma eigenfunction_orthonormal :
    Orthonormal ℂ (fun n => HilbertSpace.mk (Q.eigenfunction_memHS n))
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_linearIndependent`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean#L296).

> The eigenfunctions are linearly independent.

```lean
lemma eigenfunction_linearIndependent :
    LinearIndependent ℂ (fun n => HilbertSpace.mk (Q.eigenfunction_memHS n))
```

## Depends on

- [Physicist's Hermite Polynomials](../../mathematics/specialfunctions/physhermite.md)
- [1d Harmonic Oscillator](onedimension-basic.md)

## Sources

- [Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Eigenfunction.lean)
