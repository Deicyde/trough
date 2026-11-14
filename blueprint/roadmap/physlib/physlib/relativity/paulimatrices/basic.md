---
declaration: module
origin: cited
lean: PauliMatrix.pauliMatrix, PauliMatrix.pauliMatrix_inl_zero_eq_one, PauliMatrix.pauliMatrix_selfAdjoint, PauliMatrix.pauliMatrix_mul_self, PauliMatrix.pauliMatrixInvertiable, PauliMatrix.pauliMatrix_inv, PauliMatrix.σ2_mul_σ1, PauliMatrix.σ3_mul_σ1
statement: formalized
proof: formalized
---

# Physlib.Relativity.PauliMatrices.Basic

The module `Physlib.Relativity.PauliMatrices.Basic`, [Physlib/Relativity/PauliMatrices/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean): 41 declarations, 24 with a docstring.

## Pauli matrices

> The pauli matrices are defined ultimately through
> - `pauliMatrix` which is a map `Fin 1 ⊕ Fin 3 → Matrix (Fin 2) (Fin 2) ℂ`.
>   The notation `σ` can be used as short hand.
>
> A tensorial structure is put on `Fin 1 ⊕ Fin 3 → Matrix (Fin 2) (Fin 2) ℂ` to allow the
> use of index notation.

**`PauliMatrix.pauliMatrix`**, a def, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L35).

> The Pauli matrices.

```lean
def pauliMatrix : Fin 1 ⊕ Fin 3 → Matrix (Fin 2) (Fin 2) ℂ
```

**`PauliMatrix.pauliMatrix_inl_zero_eq_one`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L56).

```lean
lemma pauliMatrix_inl_zero_eq_one : pauliMatrix (Sum.inl 0) = 1
```

## Matrix relations

**`PauliMatrix.pauliMatrix_selfAdjoint`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L65).

```lean
lemma pauliMatrix_selfAdjoint (μ : Fin 1 ⊕ Fin 3) :
    (σ μ)ᴴ = σ μ
```

### Inversions

> Lemmas related to the inversions of the Pauli matrices.

**`PauliMatrix.pauliMatrix_mul_self`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L84).

```lean
lemma pauliMatrix_mul_self (μ : Fin 1 ⊕ Fin 3) :
    (σ μ) * (σ μ) = 1
```

**`PauliMatrix.pauliMatrixInvertiable`**, an instance, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L91).

```lean
instance pauliMatrixInvertiable (μ : Fin 1 ⊕ Fin 3) : Invertible (σ μ)
```

**`PauliMatrix.pauliMatrix_inv`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L96).

```lean
lemma pauliMatrix_inv (μ : Fin 1 ⊕ Fin 3) :
    ⅟ (σ μ) = σ μ
```

### Products

> These lemmas try to put the terms in numerical order.
> We skip `σ0` since it's just `1` anyway.

**`PauliMatrix.σ2_mul_σ1`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L105).

```lean
lemma σ2_mul_σ1 : σ2 * σ1 = -(σ1 * σ2)
```

**`PauliMatrix.σ3_mul_σ1`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L106).

```lean
lemma σ3_mul_σ1 : σ3 * σ1 = -(σ1 * σ3)
```

**`PauliMatrix.σ3_mul_σ2`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L107).

```lean
lemma σ3_mul_σ2 : σ3 * σ2 = -(σ2 * σ3)
```

### Traces

**`PauliMatrix.trace_σ1`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L115).

```lean
lemma trace_σ1 : Matrix.trace σ1 = 0
```

**`PauliMatrix.trace_σ2`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L116).

```lean
lemma trace_σ2 : Matrix.trace σ2 = 0
```

**`PauliMatrix.trace_σ3`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L117).

```lean
lemma trace_σ3 : Matrix.trace σ3 = 0
```

**`PauliMatrix.σ0_σ0_trace`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L120).

> The trace of `σ0` multiplied by `σ0` is equal to `2`.

```lean
lemma σ0_σ0_trace : Matrix.trace (σ0 * σ0) = 2
```

**`PauliMatrix.σ0_σ1_trace`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L123).

> The trace of `σ0` multiplied by `σ1` is equal to `0`.

```lean
lemma σ0_σ1_trace : Matrix.trace (σ0 * σ1) = 0
```

**`PauliMatrix.σ0_σ2_trace`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L126).

> The trace of `σ0` multiplied by `σ2` is equal to `0`.

```lean
lemma σ0_σ2_trace : Matrix.trace (σ0 * σ2) = 0
```

**`PauliMatrix.σ0_σ3_trace`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L129).

> The trace of `σ0` multiplied by `σ3` is equal to `0`.

```lean
lemma σ0_σ3_trace : Matrix.trace (σ0 * σ3) = 0
```

**`PauliMatrix.σ1_σ0_trace`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L132).

> The trace of `σ1` multiplied by `σ0` is equal to `0`.

```lean
lemma σ1_σ0_trace : Matrix.trace (σ1 * σ0) = 0
```

**`PauliMatrix.σ1_σ1_trace`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L135).

> The trace of `σ1` multiplied by `σ1` is equal to `2`.

```lean
lemma σ1_σ1_trace : Matrix.trace (σ1 * σ1) = 2
```

**`PauliMatrix.σ1_σ2_trace`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L138).

> The trace of `σ1` multiplied by `σ2` is equal to `0`.

```lean
lemma σ1_σ2_trace : Matrix.trace (σ1 * σ2) = 0
```

**`PauliMatrix.σ1_σ3_trace`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L142).

> The trace of `σ1` multiplied by `σ3` is equal to `0`.

```lean
lemma σ1_σ3_trace : Matrix.trace (σ1 * σ3) = 0
```

**`PauliMatrix.σ2_σ0_trace`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L146).

> The trace of `σ2` multiplied by `σ0` is equal to `0`.

```lean
lemma σ2_σ0_trace : Matrix.trace (σ2 * σ0) = 0
```

**`PauliMatrix.σ2_σ1_trace`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L149).

> The trace of `σ2` multiplied by `σ1` is equal to `0`.

```lean
lemma σ2_σ1_trace : Matrix.trace (σ2 * σ1) = 0
```

**`PauliMatrix.σ2_σ2_trace`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L153).

> The trace of `σ2` multiplied by `σ2` is equal to `2`.

```lean
lemma σ2_σ2_trace : Matrix.trace (σ2 * σ2) = 2
```

**`PauliMatrix.σ2_σ3_trace`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L156).

> The trace of `σ2` multiplied by `σ3` is equal to `0`.

```lean
lemma σ2_σ3_trace : Matrix.trace (σ2 * σ3) = 0
```

**`PauliMatrix.σ3_σ0_trace`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L160).

> The trace of `σ3` multiplied by `σ0` is equal to `0`.

```lean
lemma σ3_σ0_trace : Matrix.trace (σ3 * σ0) = 0
```

**`PauliMatrix.σ3_σ1_trace`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L163).

> The trace of `σ3` multiplied by `σ1` is equal to `0`.

```lean
lemma σ3_σ1_trace : Matrix.trace (σ3 * σ1) = 0
```

**`PauliMatrix.σ3_σ2_trace`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L166).

> The trace of `σ3` multiplied by `σ2` is equal to `0`.

```lean
lemma σ3_σ2_trace : Matrix.trace (σ3 * σ2) = 0
```

**`PauliMatrix.σ3_σ3_trace`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L169).

> The trace of `σ3` multiplied by `σ3` is equal to `2`.

```lean
lemma σ3_σ3_trace : Matrix.trace (σ3 * σ3) = 2
```

### Commutation relations

> Lemmas related to the commutation relations of the Pauli matrices.

**`PauliMatrix.σ1_σ2_commutator`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L178).

```lean
lemma σ1_σ2_commutator : σ1 * σ2 - σ2 * σ1 = (2 * I) • σ3
```

**`PauliMatrix.σ1_σ3_commutator`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L184).

```lean
lemma σ1_σ3_commutator : σ1 * σ3 - σ3 * σ1 = - (2 * I) • σ2
```

**`PauliMatrix.σ2_σ1_commutator`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L190).

```lean
lemma σ2_σ1_commutator : σ2 * σ1 - σ1 * σ2 = -(2 * I) • σ3
```

**`PauliMatrix.σ2_σ3_commutator`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L196).

```lean
lemma σ2_σ3_commutator : σ2 * σ3 - σ3 * σ2 = (2 * I) • σ1
```

**`PauliMatrix.σ3_σ1_commutator`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L202).

```lean
lemma σ3_σ1_commutator : σ3 * σ1 - σ1 * σ3 = (2 * I) • σ2
```

**`PauliMatrix.σ3_σ2_commutator`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L208).

```lean
lemma σ3_σ2_commutator : σ3 * σ2 - σ2 * σ3 = -(2 * I) • σ1
```

**`PauliMatrix.pauliMatrix_anticommutator`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L215).

> Pauli matrices satisfy `{σᵢ, σⱼ} = 2 δᵢⱼ I`.

```lean
lemma pauliMatrix_anticommutator (i j : Fin 3) :
    pauliMatrix (Sum.inr i) * pauliMatrix (Sum.inr j) +
      pauliMatrix (Sum.inr j) * pauliMatrix (Sum.inr i) =
        ((2 * kroneckerDelta i j : ℕ) : ℂ) •
          (1 : Matrix (Fin 2) (Fin 2) ℂ)
```

**`PauliMatrix.vectorMatrix`**, a def, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L226).

> The matrix `a · σ` associated to a real three-vector `a`.

```lean
noncomputable def vectorMatrix (a : Fin 3 → ℝ) :
    Matrix (Fin 2) (Fin 2) ℂ
```

**`PauliMatrix.vectorMatrix_anticommutator`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L232).

> The anticommutator of two Pauli vectors is twice their Euclidean dot product
> times the identity.

```lean
lemma vectorMatrix_anticommutator (a b : Fin 3 → ℝ) :
    vectorMatrix a * vectorMatrix b + vectorMatrix b * vectorMatrix a =
      ((2 * (a ⬝ᵥ b) : ℝ) : ℂ) •
        (1 : Matrix (Fin 2) (Fin 2) ℂ)
```

**`PauliMatrix.vectorMatrix_commutator`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L261).

> The commutator of two Pauli vectors is twice `i` times the Pauli vector
> associated to their cross product.

```lean
lemma vectorMatrix_commutator (a b : Fin 3 → ℝ) :
    vectorMatrix a * vectorMatrix b - vectorMatrix b * vectorMatrix a =
      (2 * Complex.I) • vectorMatrix (a ⨯₃ b)
```

**`PauliMatrix.pauliMatrix_commutator`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L283).

> Pauli matrices satisfy `[σᵢ, σⱼ] = 2i ∑ₖ εᵢⱼₖ σₖ`, with the right-handed Levi-Civita symbol
> `ε₀₁₂ = 1` and the indices `0, 1, 2` labelling `x, y, z`. This is the index form of
> `vectorMatrix_commutator`, obtained at the basis vectors `a = eᵢ`, `b = eⱼ`.

```lean
lemma pauliMatrix_commutator (i j : Fin 3) :
    pauliMatrix (Sum.inr i) * pauliMatrix (Sum.inr j) -
      pauliMatrix (Sum.inr j) * pauliMatrix (Sum.inr i) =
        (2 * I) • ∑ k : Fin 3, (leviCivitaSymbol ![i, j, k] : ℂ) • pauliMatrix (Sum.inr k)
```

**`PauliMatrix.vectorMatrix_mul_vectorMatrix`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L298).

> Product formula for Pauli vectors:
> `(a · σ)(b · σ) = (a · b) I + i (a × b) · σ`.

```lean
lemma vectorMatrix_mul_vectorMatrix (a b : Fin 3 → ℝ) :
    vectorMatrix a * vectorMatrix b =
      ((a ⬝ᵥ b : ℝ) : ℂ) •
          (1 : Matrix (Fin 2) (Fin 2) ℂ) +
        Complex.I • vectorMatrix (a ⨯₃ b)
```

**`PauliMatrix.vectorMatrix_sq`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean#L315).

> The square of `a · σ` is `|a|² I`.

```lean
lemma vectorMatrix_sq (a : Fin 3 → ℝ) :
    vectorMatrix a * vectorMatrix a =
      (∑ i : Fin 3, a i ^ 2 : ℝ) • 1
```

## Depends on

- [The Levi-Civita symbol in general dimension](../../mathematics/levicivita/basic.md)

## Sources

- [Physlib/Relativity/PauliMatrices/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/Basic.lean)
