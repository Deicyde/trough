---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.LAdicSheaf.isRational_constantLFunction_of_smoothProjectiveCurve, Stacks.EtaleCohomology.LAdicSheaf.exists_integral_curveNumerator_of_smoothProjectiveCurve, Stacks.EtaleCohomology.LAdicSheaf.isIntegral_curveEigenvalue_of_smoothProjectiveCurve, Stacks.EtaleCohomology.LAdicSheaf.natCard_fieldValuedPoints_eq_one_sub_sum_add_of_smoothProjectiveCurve, Stacks.EtaleCohomology.LAdicSheaf.norm_curveEigenvalue_lt_of_smoothProjectiveCurve, Stacks.TraceFormula.exists_pow_mem_sector
statement: formalized
proof: formalized
---

# 64.23 Constant sheaves

Section 64.23 of the Stacks Project, [Tag 03V7](https://stacks.math.columbia.edu/tag/03V7). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03V8, a lemma

[Tag 03V8](https://stacks.math.columbia.edu/tag/03V8) in the Stacks Project.

**`Stacks.EtaleCohomology.LAdicSheaf.isRational_constantLFunction_of_smoothProjectiveCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ConstantSheafCurveCohomological.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ConstantSheafCurveCohomological.lean#L204). The attribute's comment: “part (1): L(X, Q_ell) is a rational function, for X a smooth projective geometrically irreducible curve over a finite field and ell a prime different from the characteristic; its product with (1 - T)(1 - qT) is det(1 - pi_X^* T | H^1(X_kbar, Q_ell))”.

> **Tag 03V8, part (1).** The L-function `L(X, ℚ_ℓ) = ∏_{x ∈ |X|} (1 - T^{deg x})⁻¹` of a smooth,
> projective, geometrically irreducible curve over a finite field is a rational function: its
> product with a polynomial whose value at `0` is nonzero is a polynomial. (The polynomials are
> `(1 - T)(1 - qT)` and `det(1 - π_X^* T | H¹(X_k̄, ℚ_ℓ))`.)

```lean
theorem LAdicSheaf.isRational_constantLFunction_of_smoothProjectiveCurve (hℓp : ℓ ≠ p) :
    ∃ P Q : Polynomial ℚ_[ℓ], Q.eval 0 ≠ 0 ∧
      constantLFunction f ℚ_[ℓ] * (Q : PowerSeries ℚ_[ℓ]) = (P : PowerSeries ℚ_[ℓ])
```

**`Stacks.EtaleCohomology.LAdicSheaf.exists_integral_curveNumerator_of_smoothProjectiveCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ConstantSheafCurveCohomological.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ConstantSheafCurveCohomological.lean#L223). The attribute's comment: “part (2), independence of ell: dim H^1(X_kbar, Q_ell) = 2g and the characteristic polynomial det(1 - pi_X^* T | H^1) is the image of the integral numerator of the zeta function of X, a polynomial over Z determined by the Euler product of X, in which ell does not occur”.

> **Tag 03V8, part (2), independence of `ℓ`.** `dim H¹(X_k̄, ℚ_ℓ) = 2g`, and for every basis of
> `H¹(X_k̄, ℚ_ℓ)` the polynomial `det(1 - π_X^* T | H¹)` is the image of one integral polynomial of
> degree at most `2g` with constant coefficient `1`: the numerator `L(X, ℤ)·(1 - T)(1 - qT)` of the
> zeta function of `X`, in which `ℓ` does not occur.

```lean
theorem LAdicSheaf.exists_integral_curveNumerator_of_smoothProjectiveCurve (hℓp : ℓ ≠ p) :
    Module.finrank ℚ_[ℓ] (LAdicSheaf.rationalGeometricCompactlySupportedCohomology B X ℓ f
        (CompactificationOf.ofProper f) kbar (LAdicSheaf.constantSystem B X ℓ) ((1 : ℕ) : ℤ)) =
      2 * genus f ∧
    ∀ bV : Module.Basis (Fin (2 * genus f)) ℚ_[ℓ]
        (LAdicSheaf.rationalGeometricCompactlySupportedCohomology B X ℓ f
          (CompactificationOf.ofProper f) kbar (LAdicSheaf.constantSystem B X ℓ) ((1 : ℕ) : ℤ)),
      ∃ P : Polynomial ℤ, P.natDegree ≤ 2 * genus f ∧ P.coeff 0 = 1 ∧
        (P : PowerSeries ℤ) = integralCurveNumerator f (Fintype.card k) ∧
        P.map (Int.castRingHom ℚ_[ℓ]) = localCharPolynomial (LinearMap.toMatrix bV bV
          (LAdicSheaf.rationalGeometricCompactlySupportedFrobenius B X ℓ f
            (CompactificationOf.ofProper f) kbar p r hcard (LAdicSheaf.constantSystem B X ℓ)
              ((1 : ℕ) : ℤ)).hom) 1
```

**`Stacks.EtaleCohomology.LAdicSheaf.isIntegral_curveEigenvalue_of_smoothProjectiveCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ConstantSheafCurveCohomological.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ConstantSheafCurveCohomological.lean#L245). The attribute's comment: “part (2): the eigenvalues alpha_1, ..., alpha_{2g} of pi_X^* on H^1(X_kbar, Q_ell) are algebraic integers, being the reciprocal roots of the integral numerator of the zeta function, of constant coefficient 1”.

> **Tag 03V8, part (2), integrality.** The eigenvalues `α_1, …, α_{2g}` of `π_X^*` on
> `H¹(X_k̄, ℚ_ℓ)` are algebraic integers.

```lean
theorem LAdicSheaf.isIntegral_curveEigenvalue_of_smoothProjectiveCurve (hℓp : ℓ ≠ p)
    (bV : Module.Basis (Fin (2 * genus f)) ℚ_[ℓ]
      (LAdicSheaf.rationalGeometricCompactlySupportedCohomology B X ℓ f
        (CompactificationOf.ofProper f) kbar (LAdicSheaf.constantSystem B X ℓ) ((1 : ℕ) : ℤ)))
    {Ω : Type*} [CommRing Ω] (φ : ℚ_[ℓ] →+* Ω) (α : Fin (2 * genus f) → Ω)
    (hα : (localCharPolynomial (LinearMap.toMatrix bV bV
        (LAdicSheaf.rationalGeometricCompactlySupportedFrobenius B X ℓ f
          (CompactificationOf.ofProper f) kbar p r hcard (LAdicSheaf.constantSystem B X ℓ)
            ((1 : ℕ) : ℤ)).hom) 1).map φ =
      ∏ i, (1 - Polynomial.C (α i) * Polynomial.X))
    (i : Fin (2 * genus f)) : IsIntegral ℤ (α i)
```

**`Stacks.EtaleCohomology.LAdicSheaf.natCard_fieldValuedPoints_eq_one_sub_sum_add_of_smoothProjectiveCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ConstantSheafCurveCohomological.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ConstantSheafCurveCohomological.lean#L264). The attribute's comment: “part (3): #X(k_n) = 1 - sum_{i=1}^{2g} alpha_i^n + q^n for every extension k_n of k of degree n >= 1, alpha_i the eigenvalues of pi_X^* on H^1(X_kbar, Q_ell)”.

> **Tag 03V8, part (3).** The number of points of `X` with values in an extension `k_n` of `k` of
> degree `n ≥ 1` is `#X(k_n) = 1 - ∑_{i=1}^{2g} α_i^n + q^n`, `α_i` the eigenvalues of `π_X^*` on
> `H¹(X_k̄, ℚ_ℓ)`.

```lean
theorem LAdicSheaf.natCard_fieldValuedPoints_eq_one_sub_sum_add_of_smoothProjectiveCurve
    (hℓp : ℓ ≠ p)
    (bV : Module.Basis (Fin (2 * genus f)) ℚ_[ℓ]
      (LAdicSheaf.rationalGeometricCompactlySupportedCohomology B X ℓ f
        (CompactificationOf.ofProper f) kbar (LAdicSheaf.constantSystem B X ℓ) ((1 : ℕ) : ℤ)))
    {Ω : Type*} [CommRing Ω] (φ : ℚ_[ℓ] →+* Ω) (α : Fin (2 * genus f) → Ω)
    (hα : (localCharPolynomial (LinearMap.toMatrix bV bV
        (LAdicSheaf.rationalGeometricCompactlySupportedFrobenius B X ℓ f
          (CompactificationOf.ofProper f) kbar p r hcard (LAdicSheaf.constantSystem B X ℓ)
            ((1 : ℕ) : ℤ)).hom) 1).map φ =
      ∏ i, (1 - Polynomial.C (α i) * Polynomial.X))
    {n : ℕ} (hn : n ≠ 0) (K : Type u) [Field K] [Algebra k K] [Finite K]
    (hK : Module.finrank k K = n) :
    (Nat.card (fieldValuedPoints f K) : Ω) = 1 - ∑ i, α i ^ n + (Fintype.card k : Ω) ^ n
```

**`Stacks.EtaleCohomology.LAdicSheaf.norm_curveEigenvalue_lt_of_smoothProjectiveCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ConstantSheafCurveCohomological.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ConstantSheafCurveCohomological.lean#L319). The attribute's comment: “part (4): |alpha_i| < q for every eigenvalue alpha_i of pi_X^* on H^1(X_kbar, Q_ell) read in C; it follows from the Riemann hypothesis |alpha_i| = sqrt q, which the source states right after the lemma”.

> **Tag 03V8, part (4).** Every eigenvalue `α_i` of `π_X^*` on `H¹(X_k̄, ℚ_ℓ)`, read in `ℂ` along
> a ring map `ℚ_ℓ → ℂ`, has `|α_i| < q`.

```lean
theorem LAdicSheaf.norm_curveEigenvalue_lt_of_smoothProjectiveCurve (hℓp : ℓ ≠ p)
    (bV : Module.Basis (Fin (2 * genus f)) ℚ_[ℓ]
      (LAdicSheaf.rationalGeometricCompactlySupportedCohomology B X ℓ f
        (CompactificationOf.ofProper f) kbar (LAdicSheaf.constantSystem B X ℓ) ((1 : ℕ) : ℤ)))
    (φ : ℚ_[ℓ] →+* ℂ) (α : Fin (2 * genus f) → ℂ)
    (hα : (localCharPolynomial (LinearMap.toMatrix bV bV
        (LAdicSheaf.rationalGeometricCompactlySupportedFrobenius B X ℓ f
          (CompactificationOf.ofProper f) kbar p r hcard (LAdicSheaf.constantSystem B X ℓ)
            ((1 : ℕ) : ℤ)).hom) 1).map φ =
      ∏ i, (1 - Polynomial.C (α i) * Polynomial.X))
    (i : Fin (2 * genus f)) : ‖α i‖ < (Fintype.card k : ℝ)
```

## Tag 03V9, an exercise

[Tag 03V9](https://stacks.math.columbia.edu/tag/03V9) in the Stacks Project.

**`Stacks.TraceFormula.exists_pow_mem_sector`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/TraceFormula/SimultaneousPowersSector.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/NumberTheory/TraceFormula/SimultaneousPowersSector.lean#L110).

> **Exercise 03V9.** For complex numbers `α 1, …, α n` and a conic sector
> `C_ε = {z | |arg z| < ε}` with `ε > 0` about the positive real axis, there is an integer `k ≥ 1`
> with `α 1 ^ k, …, α n ^ k` all in `C_ε`.

```lean
theorem exists_pow_mem_sector (α : ι → ℂ) {ε : ℝ} (hε : 0 < ε) :
    ∃ k : ℕ, 1 ≤ k ∧ ∀ i, α i ^ k ∈ {z : ℂ | |z.arg| < ε}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.23, Tag 03V7](https://stacks.math.columbia.edu/tag/03V7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
