---
declaration: module
origin: cited
lean: ProbabilisticTheory.NormedJordanAlgebra.jordanSpectrum.compactSpace, ProbabilisticTheory.NormedJordanAlgebra.enorm_aeval_closedGenerator_eq_enorm_toContinuousMapOn, ProbabilisticTheory.NormedJordanAlgebra.jordanSpectrum_polynomialFunctions_dense, ProbabilisticTheory.NormedJordanAlgebra.exists_polynomialRepresentative, ProbabilisticTheory.NormedJordanAlgebra.polynomialRepresentative, ProbabilisticTheory.NormedJordanAlgebra.toContinuousMapOn_polynomialRepresentative, ProbabilisticTheory.NormedJordanAlgebra.aeval_closedGenerator_eq_of_toContinuousMapOn_eq, ProbabilisticTheory.NormedJordanAlgebra.polynomialCfcLinearMap
statement: formalized
proof: formalized
---

# Continuous functional calculus in JB-algebras

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.JB.GeneratedByOne.CFC`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean): 76 declarations, 74 with a docstring.

> The isometric continuous functional calculus of an observable in a JB-algebra.

## i. Overview

> Evaluating polynomials at an observable `a` of a JB-algebra is isometric for the sup norm on its
> spectrum. By Stone–Weierstrass and completeness it extends to an isometric isomorphism from the
> continuous functions on the spectrum onto `C(a)`, the continuous functional calculus. It gives
> square roots, absolute values and positive and negative parts.

## ii. Key results

> - `NormedJordanAlgebra.jordanCfcEquiv` : the functional calculus as an isomorphism onto `C(a)`.
> - `NormedJordanAlgebra.jordanCfc` : the functional calculus.
> - `NormedJordanAlgebra.jordanCfc_nonneg_iff` : `f(a) ≥ 0` iff `f ≥ 0` on the spectrum.
> - `NormedJordanAlgebra.jordanSqrt` : the square root of a nonnegative observable.
> - `NormedJordanAlgebra.jordanAbs`, `NormedJordanAlgebra.jordanPosPart`,
>   `NormedJordanAlgebra.jordanNegPart` : absolute value and positive and negative parts.
> - `NormedJordanAlgebra.jordanCfc_mul` : the functional calculus is multiplicative.
> - `NormedJordanAlgebra.jordanPosPart_sub_jordanNegPart` : `a = a₊ - a₋`.
> - `NormedJordanAlgebra.jordanPosPart_jordanOrthogonal_jordanNegPart` : `a₊ ∘ a₋ = 0`.

## iv. References

> * None.

**`ProbabilisticTheory.NormedJordanAlgebra.jordanSpectrum.compactSpace`**, an instance, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L66).

> The intrinsic spectrum of a complete Jordan observable is a compact type.  Bundling this
> standard consequence of spectral compactness lets the continuous-function algebra carry its
> ordinary sup norm without any auxiliary choice of a compact set.

```lean
noncomputable instance jordanSpectrum.compactSpace (a : E) : CompactSpace (jordanSpectrum a)
```

**`ProbabilisticTheory.NormedJordanAlgebra.enorm_aeval_closedGenerator_eq_enorm_toContinuousMapOn`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L78).

> Polynomial evaluation at the closed generator has exactly the sup norm of the corresponding
> polynomial function on the intrinsic Jordan spectrum.  This is the isometric polynomial core of
> the intrinsic continuous functional calculus.

```lean
lemma enorm_aeval_closedGenerator_eq_enorm_toContinuousMapOn [Nontrivial E]
    (a : E) (p : Polynomial ℝ) :
    ‖Polynomial.aeval (closedGenerator a) p‖ₑ =
      ‖p.toContinuousMapOn (jordanSpectrum a)‖ₑ
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanSpectrum_polynomialFunctions_dense`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L88).

> The polynomial functions on the intrinsic spectrum are dense in its real continuous-function
> algebra.  This is the approximation input for the JB continuous functional calculus.

```lean
lemma jordanSpectrum_polynomialFunctions_dense (a : E) :
    Dense (polynomialFunctions (jordanSpectrum a) : Set C(jordanSpectrum a, ℝ))
```

## A. The descended polynomial map

**`ProbabilisticTheory.NormedJordanAlgebra.exists_polynomialRepresentative`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L101).

> Every polynomial function on the intrinsic spectrum has a polynomial representative.

```lean
lemma exists_polynomialRepresentative (a : E) (f : polynomialFunctions (jordanSpectrum a)) :
    ∃ p : Polynomial ℝ,
      Polynomial.toContinuousMapOnAlgHom (jordanSpectrum a) p = f
```

**`ProbabilisticTheory.NormedJordanAlgebra.polynomialRepresentative`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L111).

> A chosen polynomial representative.  The choice is only an implementation device:
> `aeval_closedGenerator_eq_of_toContinuousMapOn_eq` proves evaluation is independent of it.

```lean
noncomputable def polynomialRepresentative (a : E)
    (f : polynomialFunctions (jordanSpectrum a)) : Polynomial ℝ
```

**`ProbabilisticTheory.NormedJordanAlgebra.toContinuousMapOn_polynomialRepresentative`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L115).

```lean
lemma toContinuousMapOn_polynomialRepresentative (a : E)
    (f : polynomialFunctions (jordanSpectrum a)) :
    Polynomial.toContinuousMapOnAlgHom (jordanSpectrum a) (polynomialRepresentative a f) = f
```

**`ProbabilisticTheory.NormedJordanAlgebra.aeval_closedGenerator_eq_of_toContinuousMapOn_eq`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L123).

> Equality of polynomial functions on the intrinsic spectrum implies equality of their values
> at the closed generator.  This is exactly the quotient step needed to descend polynomial
> evaluation to `polynomialFunctions (jordanSpectrum a)`.

```lean
lemma aeval_closedGenerator_eq_of_toContinuousMapOn_eq [Nontrivial E] (a : E) {p q : Polynomial ℝ}
    (h : Polynomial.toContinuousMapOnAlgHom (jordanSpectrum a) p =
      Polynomial.toContinuousMapOnAlgHom (jordanSpectrum a) q) :
    Polynomial.aeval (closedGenerator a) p = Polynomial.aeval (closedGenerator a) q
```

**`ProbabilisticTheory.NormedJordanAlgebra.polynomialCfcLinearMap`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L139).

> Polynomial evaluation descended to the subspace of polynomial functions on the intrinsic
> spectrum.  The preceding quotient theorem makes this independent of the chosen representative.

```lean
noncomputable def polynomialCfcLinearMap [Nontrivial E] (a : E) :
    polynomialFunctions (jordanSpectrum a) →ₗ[ℝ] ClosedGeneratedByOne a
```

**`ProbabilisticTheory.NormedJordanAlgebra.enorm_polynomialCfcLinearMap`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L157).

> The descended polynomial map preserves the exact sup norm.

```lean
lemma enorm_polynomialCfcLinearMap [Nontrivial E] (a : E)
    (f : polynomialFunctions (jordanSpectrum a)) :
    ‖polynomialCfcLinearMap a f‖ₑ = ‖f‖ₑ
```

**`ProbabilisticTheory.NormedJordanAlgebra.polynomialCfcLinearIsometry`**, a def, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L169).

> The polynomial calculus is a real linear isometry from polynomial functions with their
> sup norm into the closed algebra generated by the observable.

```lean
noncomputable def polynomialCfcLinearIsometry [Nontrivial E]
    (a : E) : polynomialFunctions (jordanSpectrum a) →ₗᵢ[ℝ] ClosedGeneratedByOne a
```

**`ProbabilisticTheory.NormedJordanAlgebra.polynomialCfcLinearMap_mul`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L179).

> The descended polynomial calculus respects multiplication.

```lean
lemma polynomialCfcLinearMap_mul [Nontrivial E] (a : E)
    (f g : polynomialFunctions (jordanSpectrum a)) :
    polynomialCfcLinearMap a (f * g) = polynomialCfcLinearMap a f * polynomialCfcLinearMap a g
```

## B. Completion from polynomial functions

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfcLinear`**, a def, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L196).

> The canonical continuous linear extension of intrinsic polynomial evaluation.  It is defined
> solely by completion along the dense polynomial functions on `jordanSpectrum a`.

```lean
noncomputable def jordanCfcLinear [Nontrivial E] (a : E) :
    C(jordanSpectrum a, ℝ) →L[ℝ] ClosedGeneratedByOne a
```

**`ProbabilisticTheory.NormedJordanAlgebra.denseRange_polynomialFunctions_subtype`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L201).

```lean
lemma denseRange_polynomialFunctions_subtype (a : E) :
    DenseRange ((polynomialFunctions (jordanSpectrum a)).toSubmodule.subtypeL :
      polynomialFunctions (jordanSpectrum a) →L[ℝ] C(jordanSpectrum a, ℝ))
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfcLinear_eq_polynomialCfcLinearMap`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L211).

> The continuous extension agrees with the descended polynomial calculus on every polynomial
> function.

```lean
lemma jordanCfcLinear_eq_polynomialCfcLinearMap [Nontrivial E]
    (a : E) (f : polynomialFunctions (jordanSpectrum a)) :
    jordanCfcLinear a f = polynomialCfcLinearMap a f
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanSpectrumCoordinatePolynomialFunction`**, a def, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L218).

> The coordinate function, regarded as a polynomial function on the intrinsic spectrum.

```lean
noncomputable def jordanSpectrumCoordinatePolynomialFunction (a : E) :
    polynomialFunctions (jordanSpectrum a)
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfcLinear_coordinate`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L227).

> The intrinsic continuous calculus sends the spectrum coordinate to the closed generator.

```lean
lemma jordanCfcLinear_coordinate [Nontrivial E] (a : E) :
    jordanCfcLinear a (jordanSpectrumCoordinatePolynomialFunction a) = closedGenerator a
```

**`ProbabilisticTheory.NormedJordanAlgebra.norm_jordanCfcLinear`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L240).

> The continuous extension remains an isometry on all real continuous functions.

```lean
lemma norm_jordanCfcLinear [Nontrivial E] (a : E)
    (f : C(jordanSpectrum a, ℝ)) : ‖jordanCfcLinear a f‖ = ‖f‖
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfcLinearIsometry`**, a def, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L250).

> The continuous intrinsic JB calculus as a linear isometry.

```lean
noncomputable def jordanCfcLinearIsometry [Nontrivial E]
    (a : E) : C(jordanSpectrum a, ℝ) →ₗᵢ[ℝ] ClosedGeneratedByOne a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfcLinear_mul`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L257).

> The continuous intrinsic calculus is multiplicative.  Both variables are reduced to
> polynomial functions by density; equality is then closed by continuity of multiplication.

```lean
lemma jordanCfcLinear_mul [Nontrivial E] (a : E) (f g : C(jordanSpectrum a, ℝ)) :
    jordanCfcLinear a (f * g) = jordanCfcLinear a f * jordanCfcLinear a g
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfcLinear_one`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L279).

> The continuous intrinsic calculus preserves the constant one function.

```lean
lemma jordanCfcLinear_one [Nontrivial E] (a : E) :
    jordanCfcLinear a (1 : C(jordanSpectrum a, ℝ)) = 1
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfcHom`**, a def, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L295).

> The intrinsic continuous functional calculus as a unital real algebra homomorphism.

```lean
noncomputable def jordanCfcHom [Nontrivial E] (a : E) :
    C(jordanSpectrum a, ℝ) →ₐ[ℝ] ClosedGeneratedByOne a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfcHom_isometry`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L307).

> The intrinsic CFC algebra homomorphism is an isometry.

```lean
lemma jordanCfcHom_isometry [Nontrivial E] (a : E) :
    Isometry (jordanCfcHom a)
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfcHom_id`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L312).

> The intrinsic CFC sends the canonical coordinate on the spectrum to the observable.

```lean
lemma jordanCfcHom_id [Nontrivial E] (a : E) :
    jordanCfcHom a (ContinuousMap.restrict (jordanSpectrum a) (.id ℝ)) = closedGenerator a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfc`**, a def, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L320).

> Apply the intrinsic continuous functional calculus to a real continuous function on the
> canonical Jordan spectrum.

```lean
noncomputable def jordanCfc [Nontrivial E] (a : E)
    (f : C(jordanSpectrum a, ℝ)) : E
```

**`ProbabilisticTheory.NormedJordanAlgebra.norm_jordanCfc`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L324).

> The intrinsic JB functional calculus has exactly the sup norm.

```lean
lemma norm_jordanCfc [Nontrivial E] (a : E)
    (f : C(jordanSpectrum a, ℝ)) : ‖jordanCfc a f‖ = ‖f‖
```

**`ProbabilisticTheory.NormedJordanAlgebra.isClosed_range_jordanCfcHom`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L330).

> The range of the intrinsic CFC is closed, because its source is complete and the calculus is
> an isometry.

```lean
lemma isClosed_range_jordanCfcHom [Nontrivial E] (a : E) :
    IsClosed (Set.range (jordanCfcHom a))
```

**`ProbabilisticTheory.NormedJordanAlgebra.generatedByOneInClosed`**, a def, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L336).

> The algebraic one-generator submodule included into its norm closure.

```lean
noncomputable def generatedByOneInClosed (a : E) :
    JordanAlgebra.generatedByOne a →ₗ[ℝ] ClosedGeneratedByOne a
```

**`ProbabilisticTheory.NormedJordanAlgebra.denseRange_generatedByOneInClosed`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L341).

> The algebraic one-generator submodule is dense in its closed generated algebra.

```lean
lemma denseRange_generatedByOneInClosed (a : E) :
    DenseRange (generatedByOneInClosed a)
```

**`ProbabilisticTheory.NormedJordanAlgebra.generatedByOneInClosed_jpow`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L350).

> The inclusion of an algebraic Jordan power is the corresponding ordinary power in the
> associative closed one-generator algebra.

```lean
lemma generatedByOneInClosed_jpow (a : E) (n : ℕ) :
    generatedByOneInClosed a ⟨a ^[n], JordanAlgebra.jpow_mem_generatedByOne a n⟩ =
      (closedGenerator a) ^ n
```

**`ProbabilisticTheory.NormedJordanAlgebra.generatedByOneInClosed_jpow_mem_range_jordanCfcHom`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L361).

> Every algebraic Jordan power of the observable lies in the range of the intrinsic CFC.

```lean
lemma generatedByOneInClosed_jpow_mem_range_jordanCfcHom [Nontrivial E] (a : E) (n : ℕ) :
    generatedByOneInClosed a ⟨a ^[n], JordanAlgebra.jpow_mem_generatedByOne a n⟩ ∈
      Set.range (jordanCfcHom a)
```

**`ProbabilisticTheory.NormedJordanAlgebra.generatedByOneInClosed_mem_range_jordanCfcHom`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L368).

> The whole algebraic one-generator submodule lies in the CFC range.

```lean
lemma generatedByOneInClosed_mem_range_jordanCfcHom [Nontrivial E]
    (a : E) (x : JordanAlgebra.generatedByOne a) :
    generatedByOneInClosed a x ∈ Set.range (jordanCfcHom a)
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfcLinear_range_eq_top`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L392).

> The intrinsic continuous functional calculus is onto the closed one-generator JB algebra.

```lean
lemma jordanCfcLinear_range_eq_top [Nontrivial E] (a : E) :
    LinearMap.range (jordanCfcHom a).toLinearMap = ⊤
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfcHom_range_eq_top`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L408).

> The range of the intrinsic CFC algebra homomorphism is the entire closed one-generator
> JB algebra.

```lean
lemma jordanCfcHom_range_eq_top [Nontrivial E] (a : E) :
    (jordanCfcHom a).range = ⊤
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfcEquiv`**, a def, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L417).

> The continuous functional calculus as an isomorphism from continuous functions on the spectrum
> onto `C(a)`.

```lean
noncomputable def jordanCfcEquiv [Nontrivial E] (a : E) :
    C(jordanSpectrum a, ℝ) ≃ₐ[ℝ] ClosedGeneratedByOne a
```

**`ProbabilisticTheory.NormedJordanAlgebra.norm_jordanCfcEquiv_apply`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L427).

> The algebra equivalence supplied by the intrinsic CFC preserves the sup norm exactly.

```lean
lemma norm_jordanCfcEquiv_apply [Nontrivial E] (a : E)
    (f : C(jordanSpectrum a, ℝ)) : ‖jordanCfcEquiv a f‖ = ‖f‖
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfc_id`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L432).

> The pointwise CFC coordinate law.

```lean
lemma jordanCfc_id [Nontrivial E] (a : E) :
    jordanCfc a (ContinuousMap.restrict (jordanSpectrum a) (.id ℝ)) = a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfc_add`**, a lemma, [line 437](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L437).

> The pointwise CFC is additive.

```lean
lemma jordanCfc_add [Nontrivial E] (a : E) (f g : C(jordanSpectrum a, ℝ)) :
    jordanCfc a (f + g) = jordanCfc a f + jordanCfc a g
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfc_sub`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L442).

> The pointwise CFC preserves subtraction.

```lean
lemma jordanCfc_sub [Nontrivial E] (a : E) (f g : C(jordanSpectrum a, ℝ)) :
    jordanCfc a (f - g) = jordanCfc a f - jordanCfc a g
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfc_zero`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L447).

> The pointwise CFC preserves zero.

```lean
lemma jordanCfc_zero [Nontrivial E] (a : E) :
    jordanCfc a (0 : C(jordanSpectrum a, ℝ)) = 0
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfc_mul`**, a lemma, [line 452](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L452).

> The pointwise CFC is multiplicative.

```lean
lemma jordanCfc_mul [Nontrivial E] (a : E) (f g : C(jordanSpectrum a, ℝ)) :
    jordanCfc a (f * g) = jordanCfc a f * jordanCfc a g
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfc_const`**, a lemma, [line 457](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L457).

> The pointwise CFC sends constant functions to the corresponding scalar multiples of one.

```lean
lemma jordanCfc_const [Nontrivial E] (a : E) (r : ℝ) :
    jordanCfc a (ContinuousMap.const (jordanSpectrum a) r) = r • (1 : E)
```

## C. Positive square roots

**`ProbabilisticTheory.NormedJordanAlgebra.jordanSpectrumSqrt`**, a def, [line 474](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L474).

> The continuous square-root function on the intrinsic spectrum of a positive observable.

```lean
noncomputable def jordanSpectrumSqrt (a : E) : C(jordanSpectrum a, ℝ)
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanSqrt`**, a def, [line 479](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L479).

> The canonical intrinsic positive square root of a nonnegative JB observable, obtained by
> applying its own continuous functional calculus to the real square-root function.

```lean
noncomputable def jordanSqrt [Nontrivial E] (a : E) (_ha : 0 ≤ a) : E
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanSpectrumSqrt_mul_self_eq_id`**, a lemma, [line 484](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L484).

> The continuous square-root function squares to the spectral coordinate for a positive
> observable.

```lean
lemma jordanSpectrumSqrt_mul_self_eq_id
    {a : E} (ha : 0 ≤ a) : jordanSpectrumSqrt a * jordanSpectrumSqrt a =
      ContinuousMap.restrict (jordanSpectrum a) (.id ℝ)
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanSqrt_mul_self`**, a lemma, [line 492](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L492).

> The canonical positive square root squares to its input.

```lean
lemma jordanSqrt_mul_self [Nontrivial E] (a : E) (ha : 0 ≤ a) :
    jordanSqrt a ha * jordanSqrt a ha = a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanSqrt_nonneg`**, a lemma, [line 499](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L499).

> The canonical square root is nonnegative.  The fourth-root function is a square root of the
> square-root function, so exact cone reconstruction proves positivity without a representation.

```lean
lemma jordanSqrt_nonneg [Nontrivial E] (a : E) (ha : 0 ≤ a) :
    0 ≤ jordanSqrt a ha
```

## D. Absolute value and positive/negative parts

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfc_nonneg_of_eq_mul_self`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L517).

> A CFC value is positive whenever its defining function is a pointwise square.

```lean
lemma jordanCfc_nonneg_of_eq_mul_self [Nontrivial E]
    (a : E) {f g : C(jordanSpectrum a, ℝ)} (hfg : f = g * g) : 0 ≤ jordanCfc a f
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfc_nonneg`**, a lemma, [line 523](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L523).

> The functional calculus is positive: nonnegative functions give nonnegative observables.

```lean
lemma jordanCfc_nonneg [Nontrivial E] (a : E)
    (f : C(jordanSpectrum a, ℝ)) (hf : ∀ x, 0 ≤ f x) : 0 ≤ jordanCfc a f
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfc_monotone`**, a lemma, [line 534](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L534).

> The intrinsic continuous calculus is monotone for the pointwise order on continuous
> functions.

```lean
lemma jordanCfc_monotone [Nontrivial E] (a : E)
    {f g : C(jordanSpectrum a, ℝ)} (hfg : f ≤ g) : jordanCfc a f ≤ jordanCfc a g
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfc_nonneg_iff`**, a lemma, [line 542](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L542).

> The intrinsic CFC reflects positivity as well as preserving it.  A positive CFC value is a
> square already in its closed generated algebra; transporting that local square witness back
> through the CFC equivalence shows that the defining continuous function is pointwise a square.

```lean
lemma jordanCfc_nonneg_iff [Nontrivial E] (a : E)
    (f : C(jordanSpectrum a, ℝ)) : 0 ≤ jordanCfc a f ↔ ∀ x, 0 ≤ f x
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfc_le_iff`**, a lemma, [line 560](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L560).

> The intrinsic CFC is an order embedding from pointwise-ordered continuous functions onto the
> closed generated JB algebra.

```lean
lemma jordanCfc_le_iff [Nontrivial E] (a : E)
    (f g : C(jordanSpectrum a, ℝ)) : jordanCfc a f ≤ jordanCfc a g ↔ f ≤ g
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanSqrt_eq_of_mem_closedGeneratedByOne`**, a lemma, [line 571](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L571).

> The square root is the unique nonnegative square root in `C(a)`.

```lean
lemma jordanSqrt_eq_of_mem_closedGeneratedByOne [Nontrivial E]
    (a : E) (ha : 0 ≤ a) (b : ClosedGeneratedByOne a) (hb0 : 0 ≤ b)
    (hb : b * b = closedGenerator a) : jordanSqrt a ha = (b : E)
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanSpectrumAbs`**, a def, [line 595](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L595).

> The absolute-value function on the intrinsic spectrum.

```lean
noncomputable def jordanSpectrumAbs (a : E) : C(jordanSpectrum a, ℝ)
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanAbs`**, a def, [line 599](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L599).

> The intrinsic absolute value of a JB observable.

```lean
noncomputable def jordanAbs [Nontrivial E] (a : E) : E
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanAbs_mul_self`**, a lemma, [line 603](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L603).

> Absolute value squares to the square of the observable.

```lean
lemma jordanAbs_mul_self [Nontrivial E] (a : E) :
    jordanAbs a * jordanAbs a = a * a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanAbs_nonneg`**, a lemma, [line 617](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L617).

> Absolute value is nonnegative, witnessed by the CFC square-root of the absolute-value
> function.

```lean
lemma jordanAbs_nonneg [Nontrivial E] (a : E) : 0 ≤ jordanAbs a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanAbs_eq_zero_iff`**, a lemma, [line 628](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L628).

> The intrinsic absolute value vanishes exactly at the zero observable.  The nontrivial
> direction uses the JB zero-square criterion through `|a|² = a²`.

```lean
lemma jordanAbs_eq_zero_iff [Nontrivial E] (a : E) :
    jordanAbs a = 0 ↔ a = 0
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanAbs_eq_self_of_nonneg`**, a lemma, [line 640](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L640).

> Absolute value fixes every positive observable.  Positivity first confines the intrinsic
> spectrum to the nonnegative real line, so the pointwise absolute-value function is the identity.

```lean
lemma jordanAbs_eq_self_of_nonneg [Nontrivial E] (a : E) (ha : 0 ≤ a) :
    jordanAbs a = a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanAbs_eq_self_iff_nonneg`**, a lemma, [line 650](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L650).

> Positivity is exactly the fixed-point condition for intrinsic absolute value.

```lean
lemma jordanAbs_eq_self_iff_nonneg [Nontrivial E] (a : E) :
    jordanAbs a = a ↔ 0 ≤ a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanSpectrumPosPart`**, a def, [line 659](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L659).

> The positive-part function on the intrinsic spectrum.

```lean
noncomputable def jordanSpectrumPosPart (a : E) : C(jordanSpectrum a, ℝ)
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanSpectrumNegPart`**, a def, [line 663](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L663).

> The negative-part function on the intrinsic spectrum.

```lean
noncomputable def jordanSpectrumNegPart (a : E) : C(jordanSpectrum a, ℝ)
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanPosPart`**, a def, [line 667](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L667).

> The positive part of an intrinsic JB observable.

```lean
noncomputable def jordanPosPart [Nontrivial E] (a : E) : E
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanNegPart`**, a def, [line 671](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L671).

> The negative part of an intrinsic JB observable.

```lean
noncomputable def jordanNegPart [Nontrivial E] (a : E) : E
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanPosPart_nonneg`**, a lemma, [line 675](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L675).

> Positive parts are nonnegative.

```lean
lemma jordanPosPart_nonneg [Nontrivial E] (a : E) :
    0 ≤ jordanPosPart a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanNegPart_nonneg`**, a lemma, [line 686](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L686).

> Negative parts are nonnegative.

```lean
lemma jordanNegPart_nonneg [Nontrivial E] (a : E) :
    0 ≤ jordanNegPart a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanPosPart_eq_self_of_nonneg`**, a lemma, [line 698](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L698).

> The positive part fixes a positive observable.

```lean
lemma jordanPosPart_eq_self_of_nonneg [Nontrivial E] (a : E) (ha : 0 ≤ a) :
    jordanPosPart a = a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanNegPart_eq_zero_of_nonneg`**, a lemma, [line 707](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L707).

> The negative part of a positive observable vanishes.

```lean
lemma jordanNegPart_eq_zero_of_nonneg [Nontrivial E] (a : E) (ha : 0 ≤ a) :
    jordanNegPart a = 0
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanPosPart_sub_jordanNegPart`**, a lemma, [line 717](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L717).

> The positive and negative parts reconstruct the observable.

```lean
lemma jordanPosPart_sub_jordanNegPart [Nontrivial E]
    (a : E) : jordanPosPart a - jordanNegPart a = a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanNegPart_eq_zero_iff_nonneg`**, a lemma, [line 734](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L734).

> Positivity is exactly the vanishing of the intrinsic negative part.

```lean
lemma jordanNegPart_eq_zero_iff_nonneg [Nontrivial E] (a : E) :
    jordanNegPart a = 0 ↔ 0 ≤ a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanPosPart_eq_zero_iff_nonpos`**, a lemma, [line 747](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L747).

> Nonpositivity is exactly the vanishing of the intrinsic positive part.  The reverse direction
> uses the exact CFC order equivalence to turn `a ≤ 0` into the pointwise spectral inequality
> `x ≤ 0`.

```lean
lemma jordanPosPart_eq_zero_iff_nonpos [Nontrivial E] (a : E) :
    jordanPosPart a = 0 ↔ a ≤ 0
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanAbs_eq_jordanPosPart_add_jordanNegPart`**, a lemma, [line 769](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L769).

> Absolute value is the sum of the positive and negative parts.  Together with
> `jordanPosPart_sub_jordanNegPart`, this is the intrinsic one-observable Jordan decomposition.

```lean
lemma jordanAbs_eq_jordanPosPart_add_jordanNegPart [Nontrivial E]
    (a : E) : jordanAbs a = jordanPosPart a + jordanNegPart a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanPosPart_le_jordanAbs`**, a lemma, [line 784](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L784).

> The positive part is bounded by the intrinsic absolute value.

```lean
lemma jordanPosPart_le_jordanAbs [Nontrivial E] (a : E) : jordanPosPart a ≤ jordanAbs a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanNegPart_le_jordanAbs`**, a lemma, [line 789](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L789).

> The negative part is bounded by the intrinsic absolute value.

```lean
lemma jordanNegPart_le_jordanAbs [Nontrivial E] (a : E) : jordanNegPart a ≤ jordanAbs a
```

**`ProbabilisticTheory.NormedJordanAlgebra.le_jordanAbs`**, a lemma, [line 794](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L794).

> An observable is bounded above by its intrinsic absolute value.

```lean
lemma le_jordanAbs [Nontrivial E] (a : E) :
    a ≤ jordanAbs a
```

**`ProbabilisticTheory.NormedJordanAlgebra.neg_le_jordanAbs`**, a lemma, [line 804](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L804).

> The negative of an observable is bounded above by its intrinsic absolute value.

```lean
lemma neg_le_jordanAbs [Nontrivial E] (a : E) :
    -a ≤ jordanAbs a
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanPosPart_jordanOrthogonal_jordanNegPart`**, a lemma, [line 817](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean#L817).

> Positive and negative parts are Jordan-orthogonal.

```lean
lemma jordanPosPart_jordanOrthogonal_jordanNegPart [Nontrivial E]
    (a : E) : JordanAlgebra.JordanOrthogonal (jordanPosPart a) (jordanNegPart a)
```

## Depends on

- [The spectrum of an observable in a JB-algebra](jb-generatedbyone-spectrum.md)
- [Moments, variance and Jordan projections](../part-01/observable.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/CFC.lean)
