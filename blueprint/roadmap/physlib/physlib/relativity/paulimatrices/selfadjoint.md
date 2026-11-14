---
declaration: module
origin: cited
lean: PauliMatrix.trace_pauliMatrix_mul_selfAdjoint_re, PauliMatrix.selfAdjoint_ext_complex, PauliMatrix.selfAdjoint_ext, PauliMatrix.pauliSelfAdjoint, PauliMatrix.pauliSelfAdjoint_linearly_independent, PauliMatrix.trace_pauliMatrix_mul_pauliMatrix, PauliMatrix.pauliCoeff, PauliMatrix.sum_pauliCoeff
statement: formalized
proof: formalized
---

# Physlib.Relativity.PauliMatrices.SelfAdjoint

The module `Physlib.Relativity.PauliMatrices.SelfAdjoint`, [Physlib/Relativity/PauliMatrices/SelfAdjoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean): 33 declarations, 32 with a docstring.

## Interaction of Pauli matrices with self-adjoint matrices

**`PauliMatrix.trace_pauliMatrix_mul_selfAdjoint_re`**, a lemma, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L25).

> The trace of a pauli-matrix multiplied by a self-adjoint `2×2` matrix is real.

```lean
lemma trace_pauliMatrix_mul_selfAdjoint_re (μ : Fin 1 ⊕ Fin 3)
    (A : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    (Matrix.trace (pauliMatrix μ * A.1)).re = Matrix.trace (pauliMatrix μ * A.1)
```

**`PauliMatrix.selfAdjoint_ext_complex`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L35).

> Two `2×2` self-adjoint matrices are equal if the (complex) traces of each matrix multiplied by
> each of the Pauli-matrices are equal.

```lean
lemma selfAdjoint_ext_complex {A B : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)}
    (h0 : Matrix.trace (σ0 * A.1) = Matrix.trace (σ0 * B.1))
    (h1 : Matrix.trace (σ1 * A.1) = Matrix.trace (σ1 * B.1))
    (h2 : Matrix.trace (σ2 * A.1) = Matrix.trace (σ2 * B.1))
    (h3 : Matrix.trace (σ3 * A.1) = Matrix.trace (σ3 * B.1)) : A = B
```

**`PauliMatrix.selfAdjoint_ext`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L67).

> Two `2×2` self-adjoint matrices are equal if the real traces of each matrix multiplied by
> each of the Pauli-matrices are equal.

```lean
lemma selfAdjoint_ext {A B : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)}
    (h0 : ((Matrix.trace (σ0 * A.1))).re = ((Matrix.trace (σ0 * B.1))).re)
    (h1 : ((Matrix.trace (σ1 * A.1))).re = ((Matrix.trace (σ1 * B.1))).re)
    (h2 : ((Matrix.trace (σ2 * A.1))).re = ((Matrix.trace (σ2 * B.1))).re)
    (h3 : ((Matrix.trace (σ3 * A.1))).re = ((Matrix.trace (σ3 * B.1))).re) :
    A = B
```

**`PauliMatrix.pauliSelfAdjoint`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L84).

> An auxiliary function which on `i : Fin 1 ⊕ Fin 3` returns the corresponding
> Pauli matrix as a self-adjoint matrix.

```lean
def pauliSelfAdjoint (i : Fin 1 ⊕ Fin 3) :
    selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)
```

**`PauliMatrix.pauliSelfAdjoint_linearly_independent`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L89).

> The Pauli matrices are linearly independent.

```lean
lemma pauliSelfAdjoint_linearly_independent : LinearIndependent ℝ pauliSelfAdjoint
```

**`PauliMatrix.trace_pauliMatrix_mul_pauliMatrix`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L105).

> Pauli matrices are orthogonal with respect to the trace pairing: `tr(σ_μ σ_ν) = 2 δ_μν`.

```lean
lemma trace_pauliMatrix_mul_pauliMatrix (μ ν : Fin 1 ⊕ Fin 3) :
    Matrix.trace (pauliMatrix μ * pauliMatrix ν) = ((2 * kroneckerDelta μ ν : ℕ) : ℂ)
```

**`PauliMatrix.pauliCoeff`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L110).

> The four real Pauli coefficients of a self-adjoint `2 × 2` matrix.

```lean
noncomputable def pauliCoeff
    (A : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    Fin 1 ⊕ Fin 3 → ℝ
```

**`PauliMatrix.sum_pauliCoeff`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L119).

> Every self-adjoint `2 × 2` matrix is its Pauli decomposition.

```lean
lemma sum_pauliCoeff
    (A : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    ∑ i, pauliCoeff A i • pauliSelfAdjoint i = A
```

**`PauliMatrix.eq_sum_pauli`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L155).

> Every self-adjoint `2 × 2` matrix is a real linear combination of the Pauli matrices.

```lean
lemma eq_sum_pauli
    (A : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    A = ∑ i, pauliCoeff A i • pauliSelfAdjoint i
```

**`PauliMatrix.pauliSelfAdjoint_span`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L161).

> The Pauli matrices span all self-adjoint matrices.

```lean
lemma pauliSelfAdjoint_span :
    ⊤ ≤ Submodule.span ℝ (Set.range pauliSelfAdjoint)
```

**`PauliMatrix.pauliBasis`**, a def, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L168).

> The basis of `selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)` formed by Pauli matrices.

```lean
def pauliBasis :
    Basis (Fin 1 ⊕ Fin 3) ℝ (selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ))
```

### Pauli coordinates of self-adjoint `2 × 2` matrices

**`PauliMatrix.scalarCoeff`**, a def, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L175).

> The coefficient of the identity in the Pauli decomposition.

```lean
noncomputable def scalarCoeff
    (A : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) : ℝ
```

**`PauliMatrix.vectorCoeff`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L180).

> The three spatial Pauli coefficients.

```lean
noncomputable def vectorCoeff
    (A : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) : Fin 3 → ℝ
```

**`PauliMatrix.vectorPart`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L185).

> The traceless Pauli-vector part `a · σ`.

```lean
noncomputable def vectorPart
    (A : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    Matrix (Fin 2) (Fin 2) ℂ
```

**`PauliMatrix.pauliRadius`**, a def, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L191).

> The Euclidean length of the spatial Pauli coefficients.

```lean
noncomputable def pauliRadius
    (A : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) : ℝ
```

**`PauliMatrix.pauliRadius_sq`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L197).

> The Pauli radius is the square root of the squared Euclidean length of the
> spatial Pauli coefficients.

```lean
lemma pauliRadius_sq
    (A : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    pauliRadius A ^ 2 =
      ∑ i : Fin 3, vectorCoeff A i ^ 2
```

**`PauliMatrix.pauliRadius_nonneg`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L205).

```lean
lemma pauliRadius_nonneg
    (A : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    0 ≤ pauliRadius A
```

### Explicit coefficients

**`PauliMatrix.matrix_eq_scalar_add_vector`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L213).

> A self-adjoint matrix is its scalar part plus its Pauli-vector part.

```lean
lemma matrix_eq_scalar_add_vector
    (A : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    A.val = (scalarCoeff A : ℂ) • 1 + vectorPart A
```

**`PauliMatrix.trace_eq_two_mul_scalarCoeff`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L227).

> The trace of a self-adjoint matrix is twice its scalar Pauli coefficient.

```lean
lemma trace_eq_two_mul_scalarCoeff
    (A : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    Matrix.trace A.1 = 2 * scalarCoeff A
```

**`PauliMatrix.trace_vectorPart`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L244).

> The Pauli-vector part has zero trace.

```lean
lemma trace_vectorPart
    (A : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    Matrix.trace (vectorPart A) = 0
```

**`PauliMatrix.vectorPart_sq`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L254).

> The square of the vector part of a self-adjoint matrix is its squared
> Pauli radius times the identity.

```lean
lemma vectorPart_sq
    (A : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    vectorPart A * vectorPart A =
      (pauliRadius A ^ 2 : ℝ) • 1
```

**`PauliMatrix.pauliSelfAdjoint'`**, a def, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L262).

> An auxiliary function which on `i : Fin 1 ⊕ Fin 3` returns the corresponding
> Pauli-matrix as a self-adjoint matrix with a minus sign for `Sum.inr _`.

```lean
def pauliSelfAdjoint' (i : Fin 1 ⊕ Fin 3) : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)
```

**`PauliMatrix.trace_pauliSelfAdjoint'_mul`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L271).

> Trace orthogonality of the covariant Pauli basis:
> `tr (σ'_a σ'_b) = 2 δ_{a b}`.

```lean
lemma trace_pauliSelfAdjoint'_mul (a b : Fin 1 ⊕ Fin 3) :
    Matrix.trace ((pauliSelfAdjoint' a).1 * (pauliSelfAdjoint' b).1) =
      if a = b then 2 else 0
```

**`PauliMatrix.trace_pauliSelfAdjoint'_mul_apply`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L283).

> The trace pairing of a covariant Pauli matrix with an arbitrary matrix, expressed through the
> matrix entries.

```lean
lemma trace_pauliSelfAdjoint'_mul_apply (l : Fin 1 ⊕ Fin 3)
    (N : Matrix (Fin 2) (Fin 2) ℂ) :
    Matrix.trace ((pauliSelfAdjoint' l).1 * N) =
      match l with
      | Sum.inl 0 => N 0 0 + N 1 1
      | Sum.inr 0 => -(N 0 1 + N 1 0)
      | Sum.inr 1 => -(Complex.I * (N 0 1 - N 1 0))
      | Sum.inr 2 => -(N 0 0 - N 1 1)
```

**`PauliMatrix.pauliSelfAdjoint'_linearly_independent`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L297).

> The Pauli matrices where `σi` are negated are linearly independent.

```lean
lemma pauliSelfAdjoint'_linearly_independent : LinearIndependent ℝ pauliSelfAdjoint'
```

**`PauliMatrix.pauliSelfAdjoint'_span`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L310).

> The Pauli matrices where `σi` are negated span all Self-adjoint matrices.

```lean
lemma pauliSelfAdjoint'_span : ⊤ ≤ Submodule.span ℝ (Set.range pauliSelfAdjoint')
```

**`PauliMatrix.pauliBasis'`**, a def, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L354).

> The basis of `selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)` formed by Pauli matrices
> where the `1, 2, 3` pauli matrices are negated. These can be thought of as the
> covariant Pauli-matrices.

```lean
def pauliBasis' : Basis (Fin 1 ⊕ Fin 3) ℝ (selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ))
```

**`PauliMatrix.pauliBasis'_decomp`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L358).

> The decomposition of a self-adjoint matrix into the Pauli matrices (where `σi` are negated).

```lean
lemma pauliBasis'_decomp (M : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    M = (1/2 * (Matrix.trace (σ0 * M.1)).re) • pauliBasis' (Sum.inl 0)
    + (-1/2 * (Matrix.trace (σ1 * M.1)).re) • pauliBasis' (Sum.inr 0)
    + (-1/2 * (Matrix.trace (σ2 * M.1)).re) • pauliBasis' (Sum.inr 1)
    + (-1/2 * (Matrix.trace (σ3 * M.1)).re) • pauliBasis' (Sum.inr 2)
```

**`PauliMatrix.pauliBasis'_repr_inl_0`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L396).

> The component of a self-adjoint matrix in the direction `σ0` under
> the basis formed by the covariant Pauli matrices.

```lean
lemma pauliBasis'_repr_inl_0 (M : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    pauliBasis'.repr M (Sum.inl 0) = 1 / 2 * Matrix.trace (σ0 * M.1)
```

**`PauliMatrix.pauliBasis'_repr_inr_0`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L414).

> The component of a self-adjoint matrix in the direction `-σ1` under
> the basis formed by the covariant Pauli matrices.

```lean
lemma pauliBasis'_repr_inr_0 (M : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    pauliBasis'.repr M (Sum.inr 0) = - 1 / 2 * Matrix.trace (σ1 * M.1)
```

**`PauliMatrix.pauliBasis'_repr_inr_1`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L432).

> The component of a self-adjoint matrix in the direction `-σ2` under
> the basis formed by the covariant Pauli matrices.

```lean
lemma pauliBasis'_repr_inr_1 (M : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    pauliBasis'.repr M (Sum.inr 1) = - 1 / 2 * Matrix.trace (σ2 * M.1)
```

**`PauliMatrix.pauliBasis'_repr_inr_2`**, a lemma, [line 450](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L450).

> The component of a self-adjoint matrix in the direction `-σ3` under
> the basis formed by the covariant Pauli matrices.

```lean
lemma pauliBasis'_repr_inr_2 (M : selfAdjoint (Matrix (Fin 2) (Fin 2) ℂ)) :
    pauliBasis'.repr M (Sum.inr 2) = - 1 / 2 * Matrix.trace (σ3 * M.1)
```

**`PauliMatrix.pauliBasis_minkowskiMetric_pauliBasis'`**, a lemma, [line 467](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean#L467).

> The relationship between the basis `pauliBasis` of contravariant Pauli-matrices and the basis
> `pauliBasis'` of covariant Pauli matrices is by multiplication by the Minkowski matrix.

```lean
lemma pauliBasis_minkowskiMetric_pauliBasis' (i : Fin 1 ⊕ Fin 3) :
    pauliBasis i = minkowskiMatrix i i • pauliBasis' i
```

## Depends on

- [The Minkowski matrix](../minkowskimatrix.md)
- [Physlib.Relativity.PauliMatrices.Basic](basic.md)

## Sources

- [Physlib/Relativity/PauliMatrices/SelfAdjoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/PauliMatrices/SelfAdjoint.lean)
