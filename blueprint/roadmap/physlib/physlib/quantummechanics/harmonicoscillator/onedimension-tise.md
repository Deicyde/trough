---
declaration: module
origin: cited
lean: QuantumMechanics.OneDimension.HarmonicOscillator.eigenValue, QuantumMechanics.OneDimension.HarmonicOscillator.deriv_eigenfunction_zero, QuantumMechanics.OneDimension.HarmonicOscillator.deriv_eigenfunction_zero', QuantumMechanics.OneDimension.HarmonicOscillator.deriv_physHermite_characteristic_length, QuantumMechanics.OneDimension.HarmonicOscillator.deriv_eigenfunction_succ, QuantumMechanics.OneDimension.HarmonicOscillator.deriv_deriv_eigenfunction_zero, QuantumMechanics.OneDimension.HarmonicOscillator.deriv_deriv_eigenfunction_succ, QuantumMechanics.OneDimension.HarmonicOscillator.deriv_deriv_eigenfunction
statement: formalized
proof: formalized
---

# The time-independent Schrodinger equation

The module `Physlib.QuantumMechanics.HarmonicOscillator.OneDimension.TISE`, [Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/TISE.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/TISE.lean): 9 declarations, 2 with a docstring.

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenValue`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/TISE.lean#L29).

> The `n`th eigenvalues for a Harmonic oscillator is defined as `(n + 1/2) * ℏ * ω`.

```lean
noncomputable def eigenValue (n : ℕ) : ℝ
```

## Derivatives of the eigenfunctions

**`QuantumMechanics.OneDimension.HarmonicOscillator.deriv_eigenfunction_zero`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/TISE.lean#L37).

```lean
lemma deriv_eigenfunction_zero : deriv (Q.eigenfunction 0) =
    Complex.ofReal (- 1 / Q.ξ ^2) • Complex.ofReal * Q.eigenfunction 0
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.deriv_eigenfunction_zero'`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/TISE.lean#L61).

```lean
lemma deriv_eigenfunction_zero' : deriv (Q.eigenfunction 0) =
    (- √2 / (2 * Q.ξ) : ℂ) • Q.eigenfunction 1
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.deriv_physHermite_characteristic_length`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/TISE.lean#L69).

```lean
lemma deriv_physHermite_characteristic_length (n : ℕ) :
    deriv (fun x => Complex.ofReal (physHermite n (x/Q.ξ))) = fun x =>
    Complex.ofReal (1/Q.ξ) * 2 * n * physHermite (n-1) (x/Q.ξ)
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.deriv_eigenfunction_succ`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/TISE.lean#L80).

```lean
lemma deriv_eigenfunction_succ (n : ℕ) :
    deriv (Q.eigenfunction (n + 1)) = fun x =>
    Complex.ofReal (1/√(2 ^ (n + 1) * (n + 1)!) * (1/Q.ξ)) •
    ((2 * (n + 1) * physHermite n (x/Q.ξ)
      - (x/Q.ξ) * physHermite (n + 1) (x/Q.ξ)) * Q.eigenfunction 0 x)
```

## Second derivatives of the eigenfunctions.

**`QuantumMechanics.OneDimension.HarmonicOscillator.deriv_deriv_eigenfunction_zero`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/TISE.lean#L103).

```lean
lemma deriv_deriv_eigenfunction_zero (x : ℝ) : deriv (deriv (Q.eigenfunction 0)) x =
    (- 1 / Q.ξ^2) * (1 + ((- 1/ Q.ξ^2) * x ^ 2)) * Q.eigenfunction 0 x
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.deriv_deriv_eigenfunction_succ`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/TISE.lean#L122).

```lean
lemma deriv_deriv_eigenfunction_succ (n : ℕ) (x : ℝ) :
    deriv (fun x => deriv (Q.eigenfunction (n + 1)) x) x =
    Complex.ofReal (1/√(2 ^ (n + 1) * (n + 1) !) * (1/Q.ξ)) *
      ((2 * (↑n + 1) * deriv (fun x => ↑(physHermite n (x/Q.ξ))) x +
      (-(1/Q.ξ^2)) * (4 * (↑n + 1) * x) *
      (physHermite n (x/Q.ξ)) + (- (1/Q.ξ)) * (1 + (- (1/Q.ξ^2)) * x ^ 2) *
      (physHermite (n + 1) (x/Q.ξ))) * Q.eigenfunction 0 x)
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.deriv_deriv_eigenfunction`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/TISE.lean#L150).

```lean
lemma deriv_deriv_eigenfunction (n : ℕ) (x : ℝ) :
    deriv (fun x => deriv (Q.eigenfunction n) x) x = (- 1 / Q.ξ^2) * ((2 * n + 1)
    + ((- 1/ Q.ξ^2) * x ^ 2)) * Q.eigenfunction n x
```

## Application of the schrodingerOperator

**`QuantumMechanics.OneDimension.HarmonicOscillator.schrodingerOperator_eigenfunction`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/TISE.lean#L189).

> The `n`th eigenfunction satisfies the time-independent Schrodinger equation with
> respect to the `n`th eigenvalue. That is to say for `Q` a harmonic oscillator,
>
> `Q.schrodingerOperator (Q.eigenfunction n) x = Q.eigenValue n * Q.eigenfunction n x`.
>
> The proof of this result is done by explicit calculation of derivatives.

```lean
lemma schrodingerOperator_eigenfunction (n : ℕ) (x : ℝ) :
    Q.schrodingerOperator (Q.eigenfunction n) x = Q.eigenValue n * Q.eigenfunction n x
```

## Depends on

- [Eigenfunction of the Harmonic Oscillator](onedimension-eigenfunction.md)

## Sources

- [Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/TISE.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/TISE.lean)
