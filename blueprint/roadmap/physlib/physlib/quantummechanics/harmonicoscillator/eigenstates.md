---
declaration: module
origin: cited
lean: QuantumMechanics.HarmonicOscillator.eigenEnergy, QuantumMechanics.HarmonicOscillator.eigenEnergy_eq, QuantumMechanics.HarmonicOscillator.eigenEnergy_strictMono, QuantumMechanics.HarmonicOscillator.eigenCoeff, QuantumMechanics.HarmonicOscillator.eigenCoeff_eq, QuantumMechanics.HarmonicOscillator.eigenCoeff_update_succ, QuantumMechanics.HarmonicOscillator.eigenCoeff_update_pred, QuantumMechanics.HarmonicOscillator.eigenfunction
statement: formalized
proof: formalized
---

# Energy eigenstates of the quantum harmonic oscillator

The module `Physlib.QuantumMechanics.HarmonicOscillator.Eigenstates`, [Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean): 27 declarations, 21 with a docstring.

## i. Overview

> The quantum harmonic oscillator in `d` dimensions is exactly solvable - the energy eigenvalues
> and eigenfunction can be computed analytically.
>
> The ground-state wavefunction is a normalized Gaussian with covariance controlled
> by the harmonic oscillator's characteristic lengths. A general state is then obtained by acting
> on the ground state with the raising operators and is labelled by `d` integer quantum numbers.
> Their wavefunctions are given by products of (physicist's) Hermite polynomials multiplying
> the ground-state Gaussian. The ladder operators of `LadderOperators.lean` act on them by shifting
> one quantum number, `aᵢ† ψₙ = √(nᵢ + 1) ψₙ₊ₑᵢ` and `aᵢ ψₙ = √nᵢ ψₙ₋ₑᵢ`, so that `Nᵢ ψₙ = nᵢ ψₙ` and
> `H ψₙ = Eₙ ψₙ` with `Eₙ = ∑ᵢ ℏ ωᵢ (nᵢ + ½)` for the Hamiltonian of `Basic.lean`, which acts on
> Schwartz maps as `∑ᵢ ℏ ωᵢ (Nᵢ + ½)` (`hamiltonian_apply_schwartz`).
>
> When the potential is isotropic another description of the energy eigenstates is possible;
> energy eigenspaces carry SO(d) representations and eigenfunctions can be written in terms of
> hyperspherical harmonics. In such cases the energies only depend on the radial quantum number.

## ii. Key results

> - `raising_eigenfunction`, `lowering_eigenfunction`: `aᵢ† ψₙ = √(nᵢ + 1) ψₙ₊ₑᵢ`,
>   `aᵢ ψₙ = √nᵢ ψₙ₋ₑᵢ`; `lowering_eigenfunction_zero`: `aᵢ ψ₀ = 0`.
> - `number_eigenfunction`: `Nᵢ ψₙ = nᵢ ψₙ`.
> - `sum_number_eigenfunction`, `hamiltonian_eigenstate`: `H ψₙ = Eₙ ψₙ`.

## iv. References

> * None.

## A. Cartesian basis

## A.1. Energy eigenvalues

**`QuantumMechanics.HarmonicOscillator.eigenEnergy`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L82).

> The energy eigenvalues, `∑ i, ℏ ωᵢ (nᵢ + ½)`.

```lean
def eigenEnergy : ℝ
```

**`QuantumMechanics.HarmonicOscillator.eigenEnergy_eq`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L84).

```lean
lemma eigenEnergy_eq : Q.eigenEnergy n = ∑ i, ℏ * Q.ω i * (n i + 1 / 2)
```

**`QuantumMechanics.HarmonicOscillator.eigenEnergy_strictMono`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L86).

```lean
lemma eigenEnergy_strictMono : StrictMono Q.eigenEnergy
```

### A.2. Eigenfunctions

**`QuantumMechanics.HarmonicOscillator.eigenCoeff`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L96).

> The `i`th normalization constant for `Q.eigenfunction n`, `1 / √(2 ^ nᵢ * nᵢ! * √π * ξᵢ)`.

```lean
def eigenCoeff (i : Fin d) : ℝ
```

**`QuantumMechanics.HarmonicOscillator.eigenCoeff_eq`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L98).

```lean
lemma eigenCoeff_eq (i : Fin d) : Q.eigenCoeff n i = 1 / √(2 ^ n i * (n i)! * √π * Q.ξ i)
```

**`QuantumMechanics.HarmonicOscillator.eigenCoeff_update_succ`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L101).

> `√(nᵢ + 1) c(n + eᵢ)ᵢ = c(n)ᵢ / √2`.

```lean
lemma eigenCoeff_update_succ (i : Fin d) (n : Fin d → ℕ) :
    √((n i : ℝ) + 1) * Q.eigenCoeff (Function.update n i (n i + 1)) i
      = (√2)⁻¹ * Q.eigenCoeff n i
```

**`QuantumMechanics.HarmonicOscillator.eigenCoeff_update_pred`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L119).

> `√nᵢ c(n - eᵢ)ᵢ = 2 nᵢ c(n)ᵢ / √2` (both sides vanish when `nᵢ = 0`).

```lean
lemma eigenCoeff_update_pred (i : Fin d) (n : Fin d → ℕ) :
    √(n i : ℝ) * Q.eigenCoeff (Function.update n i (n i - 1)) i
      = (√2)⁻¹ * (2 * n i) * Q.eigenCoeff n i
```

**`QuantumMechanics.HarmonicOscillator.eigenfunction`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L144).

> The eigenfunction labelled by the integer quantum numbers `n : Fin d → ℕ`, defined as a product
> of (physicist's) Hermite polynomials multiplying a Gaussian with covariance controlled
> by the characteristic lengths, `Q.ξ`.

```lean
def eigenfunction : 𝓢(Space d, ℂ)
```

**`QuantumMechanics.HarmonicOscillator.eigenfunction_eq`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L148).

```lean
lemma eigenfunction_eq :
    Q.eigenfunction n = compCLMOfContinuousLinearEquiv ℂ Q.ξEquiv.symm (smulLeftCLM ℂ
      (fun x ↦ ∏ i, Q.eigenCoeff n i * physHermite (n i) (x i)) (stdGaussian (Space d) ℂ))
```

**`QuantumMechanics.HarmonicOscillator.eigenfunction_apply`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L152).

```lean
lemma eigenfunction_apply :
    Q.eigenfunction n x =
      ∏ i, Q.eigenCoeff n i *
        physHermite (n i) (x i / Q.ξ i) * cexp (-2⁻¹ * (x i / Q.ξ i) ^ 2)
```

**`QuantumMechanics.HarmonicOscillator.oneDim`**, a def, [line 163](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L163).

> The one-dimensional harmonic oscillator of mass `m` and angular frequency `ωⱼ`, along the
> `j`th axis. `Q.eigenfunction n` is the product over `j` of the `nⱼ`th eigenfunctions of these
> oscillators (`eigenfunction_eq_prod_oneDim`).

```lean
def oneDim (j : Fin d) : OneDimension.HarmonicOscillator
```

**`QuantumMechanics.HarmonicOscillator.oneDim_ξ`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L170).

> The length scale of `Q.oneDim j` is `ξⱼ`.

```lean
lemma oneDim_ξ (j : Fin d) : (Q.oneDim j).ξ = Q.ξ j
```

**`QuantumMechanics.HarmonicOscillator.oneDim_eigenfunction_apply`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L176).

> The `nⱼ`th eigenfunction of `Q.oneDim j` is `y ↦ c(n)ⱼ Hₙⱼ(y / ξⱼ) exp(-½ (y / ξⱼ)²)`.

```lean
lemma oneDim_eigenfunction_apply (j : Fin d) (y : ℝ) :
    (Q.oneDim j).eigenfunction (n j) y =
      (Q.eigenCoeff n j : ℂ) * (physHermite (n j) (y / Q.ξ j) : ℂ) *
        cexp (-2⁻¹ * ((y : ℂ) / (Q.ξ j : ℂ)) ^ 2)
```

**`QuantumMechanics.HarmonicOscillator.eigenfunction_eq_prod_oneDim`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L187).

> The eigenfunction is the product of the eigenfunctions of the one-dimensional oscillators.

```lean
lemma eigenfunction_eq_prod_oneDim :
    Q.eigenfunction n x = ∏ j, (Q.oneDim j).eigenfunction (n j) (x j)
```

**`QuantumMechanics.HarmonicOscillator.deriv_oneDim_eigenfunction`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L194).

> The derivative of the `nⱼ`th eigenfunction of `Q.oneDim j`,
> `c(n)ⱼ ((2 nⱼ/ξⱼ) Hₙⱼ₋₁(y/ξⱼ) - (y/ξⱼ²) Hₙⱼ(y/ξⱼ)) exp(-½ (y/ξⱼ)²)`.

```lean
lemma deriv_oneDim_eigenfunction (j : Fin d) (y : ℝ) :
    _root_.deriv ((Q.oneDim j).eigenfunction (n j)) y
      = (Q.eigenCoeff n j : ℂ) *
        (((2 * n j / Q.ξ j : ℝ) : ℂ) * (physHermite (n j - 1) (y / Q.ξ j) : ℂ)
          - ((y / Q.ξ j ^ 2 : ℝ) : ℂ) * (physHermite (n j) (y / Q.ξ j) : ℂ)) *
        cexp (-2⁻¹ * ((y : ℂ) / (Q.ξ j : ℂ)) ^ 2)
```

**`QuantumMechanics.HarmonicOscillator.eigenfunction_update_apply`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L231).

> The eigenfunction with the `i`th quantum number changed to `k`, factor `i` set apart.

```lean
lemma eigenfunction_update_apply (i : Fin d) (k : ℕ) :
    Q.eigenfunction (Function.update n i k) x =
      (Q.oneDim i).eigenfunction (Function.update n i k i) (x i) *
        ∏ j ∈ univ.erase i, (Q.oneDim j).eigenfunction (n j) (x j)
```

**`QuantumMechanics.HarmonicOscillator.deriv_eigenfunction_apply`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L241).

> The `i`th spatial derivative of the eigenfunction, factor `i` differentiated.

```lean
lemma deriv_eigenfunction_apply (i : Fin d) :
    ∂[i] (Q.eigenfunction n) x =
      _root_.deriv ((Q.oneDim i).eigenfunction (n i)) (x i) *
        ∏ j ∈ univ.erase i, (Q.oneDim j).eigenfunction (n j) (x j)
```

### A.3. Eigenstates

**`QuantumMechanics.HarmonicOscillator.eigenstate`**, a def, [line 256](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L256).

> `Q.eigenfunction n` as an element of the Schwartz submodule of the Hilbert space.

```lean
def eigenstate : SchwartzSubmodule d
```

**`QuantumMechanics.HarmonicOscillator.eigenstate_eq`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L258).

```lean
lemma eigenstate_eq : Q.eigenstate n = schwartzEquiv _ (Q.eigenfunction n)
```

**`QuantumMechanics.HarmonicOscillator.eigenstates_orthonormal`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L262).

> The energy eigenstates are orthonormal.

```lean
lemma eigenstates_orthonormal : ⟪(Q.eigenstate n : Q.HS), Q.eigenstate n'⟫_ℂ = δ[n,n']
```

## B. The ladder operators on the eigenfunctions

**`QuantumMechanics.HarmonicOscillator.raising_eigenfunction`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L285).

> `aᵢ† ψₙ = √(nᵢ + 1) ψₙ₊ₑᵢ`: the raising operator raises the `i`th quantum number by one.

```lean
lemma raising_eigenfunction (i : Fin d) (n : Fin d → ℕ) :
    Q.raisingCLM i (Q.eigenfunction n) =
      ((Real.sqrt (n i + 1) : ℝ) : ℂ) • Q.eigenfunction (Function.update n i (n i + 1))
```

**`QuantumMechanics.HarmonicOscillator.lowering_eigenfunction`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L319).

> `aᵢ ψₙ = √nᵢ ψₙ₋ₑᵢ`: the lowering operator lowers the `i`th quantum number by one (and
> annihilates the eigenfunction when `nᵢ = 0`, since `√0 = 0`).

```lean
lemma lowering_eigenfunction (i : Fin d) (n : Fin d → ℕ) :
    Q.loweringCLM i (Q.eigenfunction n) =
      ((Real.sqrt (n i) : ℝ) : ℂ) • Q.eigenfunction (Function.update n i (n i - 1))
```

**`QuantumMechanics.HarmonicOscillator.lowering_eigenfunction_zero`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L350).

> The ground state is annihilated by every lowering operator.

```lean
lemma lowering_eigenfunction_zero (i : Fin d) : Q.loweringCLM i (Q.eigenfunction 0) = 0
```

**`QuantumMechanics.HarmonicOscillator.number_eigenfunction`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L355).

> `Nᵢ ψₙ = nᵢ ψₙ`: the eigenfunctions are eigenfunctions of the number operators.

```lean
lemma number_eigenfunction (i : Fin d) (n : Fin d → ℕ) :
    Q.numberCLM i (Q.eigenfunction n) = ((n i : ℕ) : ℂ) • Q.eigenfunction n
```

## C. The eigenvalue equation

**`QuantumMechanics.HarmonicOscillator.sum_number_eigenfunction`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L375).

> `∑ᵢ ℏ ωᵢ (Nᵢ + ½) ψₙ = Eₙ ψₙ`: the eigenvalue equation for the Hamiltonian written with the
> number operators.

```lean
lemma sum_number_eigenfunction :
    (∑ j, ((ℏ * Q.ω j : ℝ) : ℂ) •
      (Q.numberCLM j + (2⁻¹ : ℂ) • ContinuousLinearMap.id ℂ 𝓢(Space d, ℂ))) (Q.eigenfunction n) =
      (Q.eigenEnergy n : ℂ) • Q.eigenfunction n
```

**`QuantumMechanics.HarmonicOscillator.eigenstate_mem_hamiltonian_domain`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L388).

> The eigenstates lie in the domain of the Hamiltonian.

```lean
lemma eigenstate_mem_hamiltonian_domain : (Q.eigenstate n : Q.HS) ∈ Q.hamiltonian.domain
```

**`QuantumMechanics.HarmonicOscillator.hamiltonian_eigenstate`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean#L393).

> `H ψₙ = Eₙ ψₙ`: the time-independent Schrodinger equation for the eigenstates, with the
> Hamiltonian `kineticOperator + potentialOperator` of `Basic.lean`.

```lean
lemma hamiltonian_eigenstate (h : (Q.eigenstate n : Q.HS) ∈ Q.hamiltonian.domain) :
    Q.hamiltonian ⟨Q.eigenstate n, h⟩ = (Q.eigenEnergy n : ℂ) • (Q.eigenstate n : Q.HS)
```

## Depends on

- [Gaussians in inner product spaces](../../mathematics/innerproductspace/gaussian.md)
- [Number operators](numberoperator.md)
- [Eigenfunction of the Harmonic Oscillator](onedimension-eigenfunction.md)

## Sources

- [Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HarmonicOscillator/Eigenstates.lean)
