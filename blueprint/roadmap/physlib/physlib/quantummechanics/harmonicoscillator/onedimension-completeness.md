---
declaration: module
origin: cited
lean: QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_completeness, QuantumMechanics.OneDimension.HarmonicOscillator.mul_eigenfunction_integrable, QuantumMechanics.OneDimension.HarmonicOscillator.mul_physHermite_integrable, QuantumMechanics.OneDimension.HarmonicOscillator.mul_polynomial_integrable, QuantumMechanics.OneDimension.HarmonicOscillator.mul_power_integrable, QuantumMechanics.OneDimension.HarmonicOscillator.orthogonal_eigenfunction_of_mem_orthogonal, QuantumMechanics.OneDimension.HarmonicOscillator.orthogonal_physHermite_of_mem_orthogonal, QuantumMechanics.OneDimension.HarmonicOscillator.orthogonal_polynomial_of_mem_orthogonal
statement: formalized
proof: formalized
---

# Completeness of the eigenfunctions of the Harmonic Oscillator

The module `Physlib.QuantumMechanics.HarmonicOscillator.OneDimension.Completeness`, [Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean): 13 declarations, 4 with a docstring, 1 listed as significant.

> Completeness of the eigenfunctions follows from Plancherel's theorem.
>
> The steps of this proof are:
>
> 1. Prove that if `f` is orthogonal to all eigenvectors then the Fourier transform of
>   it multiplied by `exp(-c x^2)` for a `0<c` is zero.
>   Part of this is using the concept of `dominated_convergence`.
> 2. Use 'Plancherel's theorem' to show that `f` is zero.

**`QuantumMechanics.OneDimension.HarmonicOscillator.mul_eigenfunction_integrable`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean#L45).

```lean
lemma mul_eigenfunction_integrable (f : ℝ → ℂ) (hf : MemHS f) :
    MeasureTheory.Integrable (fun x => Q.eigenfunction n x * f x)
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.mul_physHermite_integrable`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean#L62).

```lean
lemma mul_physHermite_integrable (f : ℝ → ℂ) (hf : MemHS f) (n : ℕ) :
    MeasureTheory.Integrable (fun x => physHermite n (x/Q.ξ) *
      (f x * ↑(Real.exp (- x ^ 2 / (2 * Q.ξ^2)))))
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.mul_polynomial_integrable`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean#L88).

```lean
lemma mul_polynomial_integrable (f : ℝ → ℂ) (hf : MemHS f) (P : Polynomial ℤ) :
    MeasureTheory.Integrable (fun x => (P (x /Q.ξ)) *
      (f x * Real.exp (- x^2 / (2 * Q.ξ^2)))) volume
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.mul_power_integrable`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean#L117).

```lean
lemma mul_power_integrable (f : ℝ → ℂ) (hf : MemHS f) (r : ℕ) :
    MeasureTheory.Integrable (fun x => x ^ r * (f x * Real.exp (- x^2 / (2 * Q.ξ^2)))) volume
```

## Orthogonality conditions

**`QuantumMechanics.OneDimension.HarmonicOscillator.orthogonal_eigenfunction_of_mem_orthogonal`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean#L145).

```lean
lemma orthogonal_eigenfunction_of_mem_orthogonal (f : ℝ → ℂ) (hf : MemHS f)
    (hOrth : ∀ n : ℕ, ⟪HilbertSpace.mk (Q.eigenfunction_memHS n), HilbertSpace.mk hf⟫_ℂ = 0)
    (n : ℕ) : ∫ (x : ℝ), Q.eigenfunction n x * f x = 0
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.orthogonal_physHermite_of_mem_orthogonal`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean#L159).

```lean
lemma orthogonal_physHermite_of_mem_orthogonal (f : ℝ → ℂ) (hf : MemHS f)
    (hOrth : ∀ n : ℕ, ⟪HilbertSpace.mk (Q.eigenfunction_memHS n), HilbertSpace.mk hf⟫_ℂ = 0)
    (n : ℕ) : ∫ (x : ℝ), (physHermite n (x / Q.ξ)) * (f x * ↑(Real.exp (- x ^ 2 / (2 * Q.ξ ^ 2))))
    = 0
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.orthogonal_polynomial_of_mem_orthogonal`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean#L189).

```lean
lemma orthogonal_polynomial_of_mem_orthogonal (f : ℝ → ℂ) (hf : MemHS f)
    (hOrth : ∀ n : ℕ, ⟪HilbertSpace.mk (Q.eigenfunction_memHS n), HilbertSpace.mk hf⟫_ℂ = 0)
    (P : Polynomial ℤ) :
    ∫ x : ℝ, (P (x /Q.ξ)) * (f x * Real.exp (- x^2 / (2 * Q.ξ^2))) = 0
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.orthogonal_power_of_mem_orthogonal`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean#L230).

> If `f` is a function `ℝ → ℂ` satisfying `MemHS f` such that it is orthogonal
> to all `eigenfunction n` then it is orthogonal to
>
> `x ^ r * e ^ (- x ^ 2 / (2 ξ^2))`
>
> the proof of this result relies on the fact that Hermite polynomials span polynomials.

```lean
lemma orthogonal_power_of_mem_orthogonal (f : ℝ → ℂ) (hf : MemHS f)
    (hOrth : ∀ n : ℕ, ⟪HilbertSpace.mk (Q.eigenfunction_memHS n), HilbertSpace.mk hf⟫_ℂ = 0)
    (r : ℕ) : ∫ x : ℝ, (x ^ r * (f x * Real.exp (- x^2 / (2 * Q.ξ^2)))) = 0
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.orthogonal_exp_of_mem_orthogonal`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean#L270).

> If `f` is a function `ℝ → ℂ` satisfying `MemHS f` such that it is orthogonal
> to all `eigenfunction n` then it is orthogonal to
>
> `e ^ (I c x) * e ^ (- x ^ 2 / (2 ξ^2))`
>
> for any real `c`.
> The proof of this result relies on the expansion of `e ^ (I c x)`
> in terms of `x^r/r!` and using `orthogonal_power_of_mem_orthogonal`
> along with integrability conditions.

```lean
lemma orthogonal_exp_of_mem_orthogonal (f : ℝ → ℂ) (hf : MemHS f)
    (hOrth : ∀ n : ℕ, ⟪HilbertSpace.mk (Q.eigenfunction_memHS n), HilbertSpace.mk hf⟫_ℂ = 0)
    (c : ℝ) : ∫ x : ℝ, Complex.exp (Complex.I * c * x) *
    (f x * Real.exp (- x^2 / (2 * Q.ξ^2))) = 0
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.fourierIntegral_zero_of_mem_orthogonal`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean#L373).

> If `f` is a function `ℝ → ℂ` satisfying `MemHS f` such that it is orthogonal
> to all `eigenfunction n` then the fourier transform of
>
> `f (x) * e ^ (- x ^ 2 / (2 ξ^2))`
>
> is zero.
>
> The proof of this result relies on `orthogonal_exp_of_mem_orthogonal`.

```lean
lemma fourierIntegral_zero_of_mem_orthogonal (f : ℝ → ℂ) (hf : MemHS f)
    (hOrth : ∀ n : ℕ, ⟪HilbertSpace.mk (Q.eigenfunction_memHS n), HilbertSpace.mk hf⟫_ℂ = 0) :
    𝓕 (fun x => f x * Real.exp (- x^2 / (2 * Q.ξ^2))) = 0
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.zero_of_orthogonal_mk`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean#L390).

```lean
lemma zero_of_orthogonal_mk (f : ℝ → ℂ) (hf : MemHS f)
    (hOrth : ∀ n : ℕ, ⟪HilbertSpace.mk (Q.eigenfunction_memHS n), HilbertSpace.mk hf⟫_ℂ = 0)
    (plancherel_theorem: ∀ {f : ℝ → ℂ} (hf : Integrable f volume) (_ : MemLp f 2),
      eLpNorm (𝓕 f) 2 volume = eLpNorm f 2 volume) :
    HilbertSpace.mk hf = 0
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.zero_of_orthogonal_eigenVector`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean#L427).

```lean
lemma zero_of_orthogonal_eigenVector (f : HilbertSpace)
    (hOrth : ∀ n : ℕ, ⟪HilbertSpace.mk (Q.eigenfunction_memHS n), f⟫_ℂ = 0)
    (plancherel_theorem: ∀ {f : ℝ → ℂ} (hf : Integrable f volume) (_ : MemLp f 2),
      eLpNorm (𝓕 f) 2 volume = eLpNorm f 2 volume) : f = 0
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.eigenfunction_completeness`**, a theorem, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean#L446). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Assuming Plancherel's theorem (which is not yet in Mathlib),
> the topological closure of the span of the eigenfunctions of the harmonic oscillator
> is the whole Hilbert space.
>
> The proof of this result relies on `fourierIntegral_zero_of_mem_orthogonal`
> and Plancherel's theorem which together give us that the norm of
>
> `f x * e ^ (- x^2 / (2 * ξ^2))`
>
> is zero for `f` orthogonal to all eigenfunctions, and hence the norm of `f` is zero.

```lean
theorem eigenfunction_completeness
    (plancherel_theorem : ∀ {f : ℝ → ℂ} (hf : Integrable f volume) (_ : MemLp f 2),
      eLpNorm (𝓕 f) 2 volume = eLpNorm f 2 volume) :
    (Submodule.span ℂ
    (Set.range (fun n => HilbertSpace.mk (Q.eigenfunction_memHS n)))).topologicalClosure = ⊤
```

## Depends on

- [Eigenfunction of the Harmonic Oscillator](onedimension-eigenfunction.md)

## Proof depends on

- [Gaussians and the hilbert space](../hilbertspaces/onedimension-gaussians.md)

## Sources

- [Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Completeness.lean)
