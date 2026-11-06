# Gelfand–Mazur theorem

Mathlib records this with 3 declarations.

`NormedRing.algEquivComplexOfComplete`: **Gelfand-Mazur theorem**: For a complex Banach division algebra, the natural `algebraMap ℂ A`
is an algebra isomorphism whose inverse is given by selecting the (unique) element of
`spectrum ℂ a`. In addition, `algebraMap_isometry` guarantees this map is an isometry.

Note: because `NormedDivisionRing` requires the field `norm_mul : ∀ a b, ‖a * b‖ = ‖a‖ * ‖b‖`, we
don't use this type class and instead opt for a `NormedRing` in which the nonzero elements are
precisely the units. This allows for the application of this isomorphism in broader contexts, e.g.,
to the quotient of a complex Banach algebra by a maximal ideal. In the case when `A` is actually a
`NormedDivisionRing`, one may fill in the argument `hA` with the lemma `isUnit_iff_ne_zero`.

```lean
NormedRing.algEquivComplexOfComplete.{u_2} {A : Type u_2} [NormedRing A] [NormedAlgebra ℂ A]
  [CompleteSpace A] (hA : ∀ {a : A}, IsUnit a ↔ a ≠ 0) : ℂ ≃ₐ[ℂ] A
```

`NormedAlgebra.Complex.algEquivOfNormMul`: A version of the **Gelfand-Mazur Theorem**.

If `F` is a nontrivial normed `ℂ`-algebra with multiplicative norm, then we obtain a
`ℂ`-algebra equivalence with `ℂ`.

```lean
NormedAlgebra.Complex.algEquivOfNormMul.{u_1} (F : Type u_1) [NormedRing F] [NormOneClass F]
  [NormMulClass F] [NormedAlgebra ℂ F] [Nontrivial F] : ℂ ≃ₐ[ℂ] F
```

`NormedAlgebra.Real.nonempty_algEquiv_or`: A version of the **Gelfand-Mazur Theorem** over `ℝ`.

If a field `F` is a normed `ℝ`-algebra, then `F` is isomorphic as an `ℝ`-algebra
either to `ℝ` or to `ℂ`.

```lean
NormedAlgebra.Real.nonempty_algEquiv_or.{u_2} (F : Type u_2) [NormedField F] [NormedAlgebra ℝ F] :
  Nonempty (F ≃ₐ[ℝ] ℝ) ∨ Nonempty (F ≃ₐ[ℝ] ℂ)
```

The first two are over the complex numbers (with different assumptions), the third is over the real numbers.

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Complex number](../../../overview/general-algebra/numbers/complex-number.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)

## Proof depends on

- [Algebraic extension](../../../overview/general-algebra/field-theory/algebraic-extension.md)
- [Connectedness](../../../overview/topology/general-topology/part-01/connectedness.md)
- [Fundamental theorem of algebra](../../../overview/analysis/complex-analysis/fundamental-theorem-of-algebra.md)
- [The Triangle Inequality](../../../hundred-theorems/part-04/the-triangle-inequality.md)

## Sources

- [Mathlib documentation: `NormedRing.algEquivComplexOfComplete`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Algebra/GelfandFormula.html#NormedRing.algEquivComplexOfComplete)
- [Source of `NormedRing.algEquivComplexOfComplete` in Mathlib/Analysis/Normed/Algebra/GelfandFormula.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Algebra/GelfandFormula.lean#L199)
- [Mathlib documentation: `NormedAlgebra.Complex.algEquivOfNormMul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Algebra/GelfandMazur.html#NormedAlgebra.Complex.algEquivOfNormMul)
- [Source of `NormedAlgebra.Complex.algEquivOfNormMul` in Mathlib/Analysis/Normed/Algebra/GelfandMazur.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Algebra/GelfandMazur.lean#L235)
- [Mathlib documentation: `NormedAlgebra.Real.nonempty_algEquiv_or`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Algebra/GelfandMazur.html#NormedAlgebra.Real.nonempty_algEquiv_or)
- [Source of `NormedAlgebra.Real.nonempty_algEquiv_or` in Mathlib/Analysis/Normed/Algebra/GelfandMazur.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Algebra/GelfandMazur.lean#L402)
- [1000+ theorems list: Q2226677](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2063)
- [1000+ theorems project: Q2226677](https://1000-plus.github.io/all.html?length=-1#Q2226677)
- [Wikipedia: Gelfand–Mazur theorem](https://en.wikipedia.org/wiki/Gelfand%E2%80%93Mazur_theorem)
- [Wikidata: Q2226677](https://www.wikidata.org/wiki/Q2226677)
