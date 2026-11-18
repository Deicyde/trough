---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.realToComplex, ProbabilisticTheory.QuantumMechanics.realToComplex_apply, ProbabilisticTheory.QuantumMechanics.realToComplex_add, ProbabilisticTheory.QuantumMechanics.realToComplex_smul, ProbabilisticTheory.QuantumMechanics.starHomRealOperator, ProbabilisticTheory.QuantumMechanics.starHomRealOperator_isSelfAdjoint, ProbabilisticTheory.QuantumMechanics.starHomRealOperator_nonneg, ProbabilisticTheory.QuantumMechanics.starHomScalarFunctional
statement: formalized
proof: formalized
---

# The spectral forms of a representation of continuous functions

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.StarHomSpec.SesquilinearForm`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean): 49 declarations, 23 with a docstring.

> Complex measures `⟪y, E(·) x⟫` of a unital ⋆-homomorphism `C(X, ℂ) → B(H)` and their sesquilinear
> forms.

## i. Overview

> For a unital ⋆-homomorphism `Φ` from the continuous functions on a compact Hausdorff space to the
> bounded operators of a Hilbert space, the functional `f ↦ ⟪x, Φ f y⟫` is given, by the
> Riesz–Markov–Kakutani theorem and polarization, by a complex measure. This is the construction of
> `UnitaryInfra.SesquilinearForm` with the continuous functional calculus of a normal operator
> replaced by an arbitrary ⋆-homomorphism, so that it applies to the joint spectral theory of
> commuting families.

## ii. Key results

> - `starHomScalarMeasure` : the measure representing `f ↦ ⟪x, Φ f x⟫`.
> - `polarizedStarHomScalarMeasure` : the complex measure representing `f ↦ ⟪y, Φ f x⟫`.
> - `starHomSesquilinearForm` : the bounded sesquilinear form of a measurable set.

## iv. References

> * None.

## A. Positive scalar functionals from a ⋆-homomorphism

**`ProbabilisticTheory.QuantumMechanics.realToComplex`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L67).

> Regard a real-valued continuous function on the spectrum of a normal operator as a complex
> valued one.  Keeping this map explicit prevents the real/complex scalar changes in the Riesz
> construction from being hidden in coercions.

```lean
noncomputable def realToComplex
    (f : CompactlySupportedContinuousMap (X) ℝ) :
    C(X, ℂ)
```

**`ProbabilisticTheory.QuantumMechanics.realToComplex_apply`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L76).

```lean
lemma realToComplex_apply
    (f : CompactlySupportedContinuousMap (X) ℝ) (z : X) :
    realToComplex f z = f z
```

**`ProbabilisticTheory.QuantumMechanics.realToComplex_add`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L82).

```lean
lemma realToComplex_add
    (f g : CompactlySupportedContinuousMap (X) ℝ) :
    realToComplex (f + g) =
      realToComplex f + realToComplex g
```

**`ProbabilisticTheory.QuantumMechanics.realToComplex_smul`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L90).

```lean
lemma realToComplex_smul (r : ℝ)
    (f : CompactlySupportedContinuousMap (X) ℝ) :
    realToComplex (r • f) =
      (r : ℂ) • realToComplex f
```

**`ProbabilisticTheory.QuantumMechanics.starHomRealOperator`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L99).

> The operator obtained by applying the complex continuous functional calculus to a real test
> function.

```lean
noncomputable def starHomRealOperator
    (f : CompactlySupportedContinuousMap (X) ℝ) : H →L[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.starHomRealOperator_isSelfAdjoint`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L104).

```lean
lemma starHomRealOperator_isSelfAdjoint
    (f : CompactlySupportedContinuousMap (X) ℝ) :
    IsSelfAdjoint (starHomRealOperator Φ f)
```

**`ProbabilisticTheory.QuantumMechanics.starHomRealOperator_nonneg`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L117).

```lean
lemma starHomRealOperator_nonneg
    (f : CompactlySupportedContinuousMap (X) ℝ)
    (hf : ∀ z, 0 ≤ f z) :
    ContinuousLinearMap.IsPositive (starHomRealOperator Φ f)
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarFunctional`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L138).

> The vector state of the continuous functional calculus, restricted to real test functions.
> The positivity proof is the square-root argument above; this is the exact input required by
> Riesz--Markov.

```lean
noncomputable def starHomScalarFunctional (x : H) :
    CompactPositiveFunctional (X := X)
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarFunctional_apply`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L157).

```lean
lemma starHomScalarFunctional_apply (x : H)
    (f : CompactlySupportedContinuousMap (X) ℝ) :
    (starHomScalarFunctional Φ x).functional f =
      RCLike.re ⟪x, starHomRealOperator Φ f x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L164).

> The scalar spectral measure supplied by Riesz--Markov for the vector state at `x`.

```lean
noncomputable def starHomScalarMeasure (x : H) : Measure (X)
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_regular`**, an instance, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L167).

```lean
instance starHomScalarMeasure_regular (x : H) : (starHomScalarMeasure Φ x).Regular
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_isFinite`**, an instance, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L171).

```lean
instance starHomScalarMeasure_isFinite (x : H) : IsFiniteMeasure (starHomScalarMeasure Φ x)
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_integral`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L175).

```lean
lemma starHomScalarMeasure_integral (x : H)
    (f : CompactlySupportedContinuousMap (X) ℝ) :
    ∫ z, f z ∂starHomScalarMeasure Φ x =
      RCLike.re ⟪x, starHomRealOperator Φ f x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_integral_complex`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L181).

```lean
lemma starHomScalarMeasure_integral_complex (x : H)
    (f : CompactlySupportedContinuousMap (X) ℝ) :
    ((∫ z, f z ∂starHomScalarMeasure Φ x : ℝ) : ℂ) =
      ⟪starHomRealOperator Φ f x, x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomRealIntegral`**, a def, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L199).

> The integral of a real function against the polarized measure.

```lean
noncomputable def polarizedStarHomRealIntegral
    (f : CompactlySupportedContinuousMap (X) ℝ) (x y : H) : ℂ
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomRealIntegral_eq_inner`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L208).

```lean
lemma polarizedStarHomRealIntegral_eq_inner
    (f : CompactlySupportedContinuousMap (X) ℝ) (x y : H) :
    polarizedStarHomRealIntegral Φ f x y =
      ⟪y, starHomRealOperator Φ f x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_parallelogram`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L230).

```lean
lemma starHomScalarMeasure_parallelogram (x y : H) :
    starHomScalarMeasure Φ (x + y) + starHomScalarMeasure Φ (x - y) =
      (starHomScalarMeasure Φ x + starHomScalarMeasure Φ x) +
        (starHomScalarMeasure Φ y + starHomScalarMeasure Φ y)
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_neg`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L260).

```lean
lemma starHomScalarMeasure_neg (x : H) :
    starHomScalarMeasure Φ (-x) = starHomScalarMeasure Φ x
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_I_smul`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L270).

```lean
lemma starHomScalarMeasure_I_smul (x : H) :
    starHomScalarMeasure Φ (Complex.I • x) = starHomScalarMeasure Φ x
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure`**, a def, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L285).

> The complex measure `⟪y, E(·) x⟫`, obtained by polarizing the four measures `⟪v, E(·) v⟫`.

```lean
noncomputable def polarizedStarHomScalarMeasure (x y : H) : ComplexMeasure (X)
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_isFiniteMeasure`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L293).

```lean
lemma polarizedStarHomScalarMeasure_isFiniteMeasure (x y : H) :
    IsFiniteMeasure
      (polarizedStarHomScalarMeasure Φ x y).variation
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_complexIntegral`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L345).

```lean
lemma polarizedStarHomScalarMeasure_complexIntegral
    (f : CompactlySupportedContinuousMap (X) ℝ) (x y : H) :
    ∫ᵛ z, (f z : ℂ) ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ);
      polarizedStarHomScalarMeasure Φ x y] =
      polarizedStarHomRealIntegral Φ f x y
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_complexIntegral_eq_inner`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L394).

```lean
lemma polarizedStarHomScalarMeasure_complexIntegral_eq_inner
    (f : CompactlySupportedContinuousMap (X) ℝ) (x y : H) :
    ∫ᵛ z, (f z : ℂ) ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ);
      polarizedStarHomScalarMeasure Φ x y] =
      ⟪y, starHomRealOperator Φ f x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_apply`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L402).

```lean
lemma polarizedStarHomScalarMeasure_apply {x y : H}
    {S : Set (X)} (hS : MeasurableSet S) :
    polarizedStarHomScalarMeasure Φ x y S =
      ((1 / 4 : ℝ) *
          ((starHomScalarMeasure Φ (x + y)).real S -
            (starHomScalarMeasure Φ (x - y)).real S) : ℂ) +
        Complex.I * ((1 / 4 : ℝ) *
          ((starHomScalarMeasure Φ (x + Complex.I • y)).real S -
            (starHomScalarMeasure Φ (x - Complex.I • y)).real S) : ℂ)
```

## B. Sesquilinearity of the polarized measure

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_real_parallelogram`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L419).

> The real-valued version of the parallelogram law, at a fixed (not necessarily measurable)
> set `S`.  This is the algebraic engine behind the sesquilinearity proofs below.

```lean
lemma starHomScalarMeasure_real_parallelogram (a b : H) (S : Set (X)) :
    (starHomScalarMeasure Φ (a + b)).real S + (starHomScalarMeasure Φ (a - b)).real S =
      2 * (starHomScalarMeasure Φ a).real S + 2 * (starHomScalarMeasure Φ b).real S
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_real_neg`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L434).

```lean
lemma starHomScalarMeasure_real_neg (a : H) (S : Set (X)) :
    (starHomScalarMeasure Φ (-a)).real S = (starHomScalarMeasure Φ a).real S
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_real_I_smul`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L438).

```lean
lemma starHomScalarMeasure_real_I_smul (a : H) (S : Set (X)) :
    (starHomScalarMeasure Φ (Complex.I • a)).real S = (starHomScalarMeasure Φ a).real S
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_real_nonneg`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L442).

```lean
lemma starHomScalarMeasure_real_nonneg (a : H) (S : Set (X)) :
    0 ≤ (starHomScalarMeasure Φ a).real S
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_real_univ`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L447).

> The Riesz measure for the vector state at `x` has total mass `‖x‖ ^ 2`: the vector-state
> counterpart of `Φ 1 = 1`.

```lean
lemma starHomScalarMeasure_real_univ (x : H) :
    (starHomScalarMeasure Φ x).real Set.univ = ‖x‖ ^ 2
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_real_le_univ`**, a lemma, [line 469](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L469).

```lean
lemma starHomScalarMeasure_real_le_univ (a : H) (S : Set (X)) :
    (starHomScalarMeasure Φ a).real S ≤ ‖a‖ ^ 2
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_real_polar_symm`**, a lemma, [line 476](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L476).

> The real polarization `Q(a + b) - Q(a - b)` of the diagonal measures is symmetric in `a` and
> `b`.

```lean
lemma starHomScalarMeasure_real_polar_symm (a b : H) (S : Set (X)) :
    (starHomScalarMeasure Φ (a + b)).real S - (starHomScalarMeasure Φ (a - b)).real S =
      (starHomScalarMeasure Φ (b + a)).real S - (starHomScalarMeasure Φ (b - a)).real S
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_real_polar_add_left`**, a lemma, [line 486](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L486).

> First-argument additivity of the real polarization `Q(a+b) - Q(a-b)`, established by pure
> algebra from the parallelogram law (`starHomScalarMeasure_real_parallelogram`); no continuity is
> needed for this step, matching the classical Jordan--von Neumann polarization argument
> (`Mathlib.Analysis.InnerProductSpace.OfNorm`).

```lean
lemma starHomScalarMeasure_real_polar_add_left (x y z : H) (S : Set (X)) :
    (starHomScalarMeasure Φ (x + y + z)).real S - (starHomScalarMeasure Φ (x + y - z)).real S =
      ((starHomScalarMeasure Φ (x + z)).real S - (starHomScalarMeasure Φ (x - z)).real S) +
        ((starHomScalarMeasure Φ (y + z)).real S - (starHomScalarMeasure Φ (y - z)).real S)
```

**`ProbabilisticTheory.QuantumMechanics.starHomScalarMeasure_real_polar_add_right`**, a lemma, [line 511](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L511).

> Second-argument additivity of the real polarization, obtained from first-argument additivity
> (`starHomScalarMeasure_real_polar_add_left`)
>   via the symmetry `starHomScalarMeasure_real_polar_symm`.

```lean
lemma starHomScalarMeasure_real_polar_add_right (a b c : H) (S : Set (X)) :
    (starHomScalarMeasure Φ (a + (b + c))).real S -
        (starHomScalarMeasure Φ (a - (b + c))).real S =
      ((starHomScalarMeasure Φ (a + b)).real S - (starHomScalarMeasure Φ (a - b)).real S) +
        ((starHomScalarMeasure Φ (a + c)).real S - (starHomScalarMeasure Φ (a - c)).real S)
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_add_right`**, a lemma, [line 531](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L531).

> Additivity of the polarized measure in its second (right) vector argument, for a fixed
> measurable set `S`.  This is the sesquilinearity step promised in the module docstring: it
> follows from the parallelogram law by pure algebra, with no continuity or Riesz-representation
> machinery required.

```lean
lemma polarizedStarHomScalarMeasure_add_right (x y₁ y₂ : H) {S : Set (X)}
    (hS : MeasurableSet S) :
    polarizedStarHomScalarMeasure Φ x (y₁ + y₂) S =
      polarizedStarHomScalarMeasure Φ x y₁ S +
        polarizedStarHomScalarMeasure Φ x y₂ S
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_add_left`**, a lemma, [line 555](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L555).

> Additivity of the polarized measure in its first (left) vector argument, for a fixed
> measurable set `S`.

```lean
lemma polarizedStarHomScalarMeasure_add_left (x₁ x₂ y : H) {S : Set (X)}
    (hS : MeasurableSet S) :
    polarizedStarHomScalarMeasure Φ (x₁ + x₂) y S =
      polarizedStarHomScalarMeasure Φ x₁ y S +
        polarizedStarHomScalarMeasure Φ x₂ y S
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_I_smul_right`**, a lemma, [line 577](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L577).

> Multiplying the second vector by `i` multiplies the polarized measure by `-i`.

```lean
lemma polarizedStarHomScalarMeasure_I_smul_right (x y : H) {S : Set (X)}
    (hS : MeasurableSet S) :
    polarizedStarHomScalarMeasure Φ x (Complex.I • y) S =
      -Complex.I * polarizedStarHomScalarMeasure Φ x y S
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_I_smul_left`**, a lemma, [line 594](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L594).

> Multiplying the first vector by `i` multiplies the polarized measure by `i`.

```lean
lemma polarizedStarHomScalarMeasure_I_smul_left (x y : H) {S : Set (X)}
    (hS : MeasurableSet S) :
    polarizedStarHomScalarMeasure Φ (Complex.I • x) y S =
      Complex.I * polarizedStarHomScalarMeasure Φ x y S
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_norm_le`**, a lemma, [line 616](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L616).

> A crude but sufficient bound on the polarized measure, from the parallelogram law and
> `starHomScalarMeasure_real_le_univ`.
>    This is enough to see `(x, y) ↦ polarizedStarHomScalarMeasure Φ
> x y S` is jointly bounded, the input a Riesz-representation argument needs.

```lean
lemma polarizedStarHomScalarMeasure_norm_le (x y : H) {S : Set (X)}
    (hS : MeasurableSet S) :
    ‖polarizedStarHomScalarMeasure Φ x y S‖ ≤ ‖x‖ ^ 2 + ‖y‖ ^ 2
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_real_smul_right`**, a lemma, [line 652](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L652).

> The polarized measure is real homogeneous in the second vector.

```lean
lemma polarizedStarHomScalarMeasure_real_smul_right (x y : H) (r : ℝ) {S : Set (X)}
    (hS : MeasurableSet S) :
    polarizedStarHomScalarMeasure Φ x (r • y) S =
      (r : ℂ) * polarizedStarHomScalarMeasure Φ x y S
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_real_smul_left`**, a lemma, [line 677](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L677).

> Real-scalar homogeneity in the left (first) argument, the counterpart of
> `polarizedStarHomScalarMeasure_real_smul_right` needed for conjugate-linearity in `x` (real scalars
> are self-conjugate, so the same statement serves both roles).

```lean
lemma polarizedStarHomScalarMeasure_real_smul_left (x y : H) (r : ℝ) {S : Set (X)}
    (hS : MeasurableSet S) :
    polarizedStarHomScalarMeasure Φ (r • x) y S =
      (r : ℂ) * polarizedStarHomScalarMeasure Φ x y S
```

## C. Polarization

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_smul_left`**, a lemma, [line 702](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L702).

> Full `ℂ`-linearity of the polarized measure in its first (left) argument.

```lean
lemma polarizedStarHomScalarMeasure_smul_left (c : ℂ) (x y : H) {S : Set (X)}
    (hS : MeasurableSet S) :
    polarizedStarHomScalarMeasure Φ (c • x) y S =
      c * polarizedStarHomScalarMeasure Φ x y S
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_smul_right`**, a lemma, [line 719](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L719).

> Full conjugate-`ℂ`-linearity of the polarized measure in its second (right) argument.

```lean
lemma polarizedStarHomScalarMeasure_smul_right (c : ℂ) (x y : H) {S : Set (X)}
    (hS : MeasurableSet S) :
    polarizedStarHomScalarMeasure Φ x (c • y) S =
      (starRingEnd ℂ c) * polarizedStarHomScalarMeasure Φ x y S
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_zero_left`**, a lemma, [line 739](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L739).

```lean
lemma polarizedStarHomScalarMeasure_zero_left (y : H) {S : Set (X)}
    (hS : MeasurableSet S) : polarizedStarHomScalarMeasure Φ 0 y S = 0
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_zero_right`**, a lemma, [line 744](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L744).

```lean
lemma polarizedStarHomScalarMeasure_zero_right (x : H) {S : Set (X)}
    (hS : MeasurableSet S) : polarizedStarHomScalarMeasure Φ x 0 S = 0
```

**`ProbabilisticTheory.QuantumMechanics.polarizedStarHomScalarMeasure_norm_le_mul`**, a lemma, [line 750](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L750).

> The polarized measure is bounded by `‖x‖ ‖y‖`.

```lean
lemma polarizedStarHomScalarMeasure_norm_le_mul (x y : H) {S : Set (X)}
    (hS : MeasurableSet S) :
    ‖polarizedStarHomScalarMeasure Φ x y S‖ ≤ 2 * ‖x‖ * ‖y‖
```

## D. Riesz representation of the polarized measure

**`ProbabilisticTheory.QuantumMechanics.starHomSesquilinearFormAux`**, a def, [line 789](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L789).

> The algebraic (not-yet-continuous) sesquilinear form representing `S`, conjugate-linear in the
> first argument and linear in the second — the convention Mathlib's
> `InnerProductSpace.continuousLinearMapOfBilin` expects.

```lean
noncomputable def starHomSesquilinearFormAux (S : Set (X)) (hS : MeasurableSet S) :
    H →ₛₗ[starRingEnd ℂ] H →ₗ[ℂ] ℂ
```

**`ProbabilisticTheory.QuantumMechanics.starHomSesquilinearFormAux_apply`**, a lemma, [line 804](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L804).

```lean
lemma starHomSesquilinearFormAux_apply (S : Set (X)) (hS : MeasurableSet S) (x y : H) :
    starHomSesquilinearFormAux Φ S hS x y =
      starRingEnd ℂ (polarizedStarHomScalarMeasure Φ x y S)
```

**`ProbabilisticTheory.QuantumMechanics.starHomSesquilinearForm`**, a def, [line 810](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L810).

> The continuous sesquilinear form, in the shape `InnerProductSpace.continuousLinearMapOfBilin`
> consumes.

```lean
noncomputable def starHomSesquilinearForm (S : Set (X)) (hS : MeasurableSet S) :
    H →L⋆[ℂ] H →L[ℂ] ℂ
```

**`ProbabilisticTheory.QuantumMechanics.starHomSesquilinearForm_apply`**, a lemma, [line 817](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean#L817).

```lean
lemma starHomSesquilinearForm_apply (S : Set (X)) (hS : MeasurableSet S) (x y : H) :
    starHomSesquilinearForm Φ S hS x y =
      starRingEnd ℂ (polarizedStarHomScalarMeasure Φ x y S)
```

## Depends on

- [The spectral forms of a bounded normal operator](unbounded-unitaryinfra-sesquilinearform.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/SesquilinearForm.lean)
