---
declaration: section
origin: cited
lean: OAI.DirectCrouzeix.complete_crouzeix, OAI.DirectCrouzeix.uniform_sharpness, OAI.CompleteCrouzeix.main, OAI.StructuralCrouzeixReference.challenge, OAI.CrouzeixHilbert.hilbert, OAI.HilbertCrouzeix.numericalClosure_geometry, OAI.HilbertCrouzeix.exists_finite_compression, OAI.HilbertCrouzeix.rational_denominator_isUnit
statement: formalized
---

# 325. The complete Crouzeix conjecture

2 manuscripts and 9 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the complete Crouzeix conjecture: for every bounded operator *A* on a complex Hilbert space and every finite matrix-valued polynomial *P*, one has $\lVert P[A]\rVert\le2\sup_{z\in W(A)}\lVert P(z)\rVert$, where $W(A)$ is the numerical range. The constant 2 is sharp, independent of the matrix size, and valid in infinite dimensions.

## A direct proof of the complete Crouzeix inequality

We give a direct proof of the sharp constant-two numerical-range inequality for matrix-valued polynomials in all finite base and coefficient dimensions. This resolves the complete Crouzeix conjecture in its matrix formulation, including matrices whose numerical ranges are points or line segments.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/paper.pdf); the Lean below formalizes results from it.

## The complete Crouzeix theorem: optimal similarity and a common positive boundary representation

We resolve the complete Crouzeix conjecture by proving the sharp constant-two numerical-range inequality for every bounded operator on a complex Hilbert space and every matrix-valued polynomial. No separability assumption is needed. The closure of the numerical range is a complete 2-spectral set, and the bound extends to finite matrix-valued functions holomorphic near that closure. For a finite matrix and a bounded convex domain containing its numerical range with regular real-analytic Jordan boundary, the optimal similarity making its conformal disk image contractive is attained with condition number at most two. For the similar matrix, one continuous positive boundary density of mass the identity represents the evaluation of every matrix-valued function holomorphic near the closed domain.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-complete-Crouzeix-theorem-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The complete Crouzeix inequality bounds a matrix-valued polynomial evaluated at a matrix by its maximum norm on the numerical range. The formalized result proves the bound with constant $2$ for every positive matrix and coefficient size, every polynomial degree, and arbitrary complex coefficients. It also proves that no smaller universal constant works. Normality of the matrix and nonempty interior of its numerical range are not assumed.

The formalization proves the complete Crouzeix inequality with sharp constant two for every bounded operator on an arbitrary complex Hilbert space. For every matrix-valued polynomial, its operator evaluation has norm at most twice its supremum norm on the numerical range. The same bound holds for finite matrix-valued functions holomorphic near the closure of the numerical range and for rational functions with poles outside that closure. No separability assumption is required.

For finite matrices in a bounded convex domain with regular real-analytic Jordan boundary, the structural result gives an attained optimal similarity with condition number at most two and one continuous positive boundary density of mass the identity representing every matrix-valued analytic test. The linked supporting statements include numerical-range geometry and finite-compression identities.

## Lean: Complete Crouzeix inequality and sharpness

```lean
theorem complete_crouzeix : UniversalBound 2
```

Stated in [DirectCrouzeix.lean, line 34](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DirectCrouzeix.lean#L34). Proved in [lean/OAI/Analysis/DirectCrouzeix/CompleteBound.lean, line 65](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/DirectCrouzeix/CompleteBound.lean#L65). formalization.yaml lists it as one of the repository's main results.

```lean
theorem uniform_sharpness (c : ℝ) (hc : UniversalBound c) : 2 ≤ c
```

Stated in [DirectCrouzeix.lean, line 37](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DirectCrouzeix.lean#L37). Proved in [lean/OAI/Analysis/DirectCrouzeix/Sharpness.lean, line 75](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/DirectCrouzeix/Sharpness.lean#L75).

## Lean: Complete polynomial inequality and sharpness

```lean
theorem main : UniversalBound 2 ∧ ∀ C : ℝ, UniversalBound C → 2 ≤ C
```

Stated in [CompleteCrouzeix.lean, line 33](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CompleteCrouzeix.lean#L33). Proved in [lean/OAI/Analysis/NumericalRange/Main.lean, line 61](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/NumericalRange/Main.lean#L61). formalization.yaml lists it as one of the repository's main results.

## Lean: Optimal similarity and boundary representation

```lean
theorem challenge : StructuralCrouzeix.FullEndpoint ∧
    StructuralCrouzeix.IsAdmissible (Metric.ball (0 : ℂ) 1)
```

Stated in [StructuralCrouzeix.lean, line 210](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/StructuralCrouzeix.lean#L210). Proved in [lean/OAI/Analysis/StructuralCrouzeix/Endpoint.lean, line 7](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/StructuralCrouzeix/Endpoint.lean#L7). formalization.yaml lists it as one of the repository's main results.

## Lean: Complete sharp Crouzeix theorem on arbitrary Hilbert spaces

```lean
theorem hilbert (H : Type u) [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    [CompleteSpace H] (A : Operator H) :
    (Nontrivial H → NonzeroConclusion A) ∧
    (Subsingleton H → ZeroConclusion A) ∧ SharpConstant
```

Stated in [CrouzeixHilbert.lean, line 148](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CrouzeixHilbert.lean#L148). Proved in [lean/OAI/Analysis/Crouzeix/HilbertInequality.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Crouzeix/HilbertInequality.lean#L12).

## Lean: Numerical-range geometry and finite-compression support

```lean
theorem numericalClosure_geometry (A : H →L[ℂ] H) :
    IsCompact (numericalClosure A) ∧ Convex ℝ (numericalClosure A) ∧
      spectrum ℂ A ⊆ numericalClosure A
```

Stated in [HilbertCrouzeix.lean, line 115](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HilbertCrouzeix.lean#L115). Its proof is in [lean/OAI/Analysis/HilbertCrouzeix/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/HilbertCrouzeix/Main.lean) or a file it imports further down, which this chapter does not read.

```lean
theorem exists_finite_compression {m d : ℕ} (A : H →L[ℂ] H)
    (B : Fin (d + 1) → Coeff m) (ξ : H ⊗[ℂ] CoeffSpace m) :
    ∃ (E : Submodule ℂ H) (hE : FiniteDimensional ℂ E),
      letI : FiniteDimensional ℂ E := hE
      ∃ η : Amplification E m,
        tensorInclusion E m η = (↑ξ : Amplification H m) ∧
        tensorInclusion E m (polynomialEval (compression A E) B η) =
          polynomialEval A B (↑ξ)
```

Stated in [HilbertCrouzeix.lean, line 121](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HilbertCrouzeix.lean#L121). Its proof is in [lean/OAI/Analysis/HilbertCrouzeix/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/HilbertCrouzeix/Main.lean) or a file it imports further down, which this chapter does not read.

```lean
theorem rational_denominator_isUnit [Nontrivial H] (A : H →L[ℂ] H)
    {m : ℕ} (R : RationalMatrix m) (hR : numericalClosure A ⊆ poleFreeSet R)
    (i j : Fin m) : IsUnit (Polynomial.aeval A (R i j).denom)
```

Stated in [HilbertCrouzeix.lean, line 131](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HilbertCrouzeix.lean#L131). Proved in [lean/OAI/Analysis/HilbertCrouzeix/Calculus.lean, line 51](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/HilbertCrouzeix/Calculus.lean#L51).

```lean
theorem zeroConclusion [Subsingleton H] (A : H →L[ℂ] H) : ZeroConclusion A
```

Stated in [HilbertCrouzeix.lean, line 136](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HilbertCrouzeix.lean#L136). Proved in [lean/OAI/Analysis/HilbertCrouzeix/Calculus.lean, line 84](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/HilbertCrouzeix/Calculus.lean#L84).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/325.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/325.md)
