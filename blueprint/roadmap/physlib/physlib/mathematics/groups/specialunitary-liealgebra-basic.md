---
declaration: module
origin: cited
lean: SULieAlgebra.submodule, SULieAlgebra, SULieAlgebra.ofMatrix, SULieAlgebra.val_ofMatrix, SULieAlgebra.star_val_eq, SULieAlgebra.trace_val_eq_zero, SULieAlgebra.conj, SULieAlgebra.val_conj_apply
statement: formalized
proof: formalized
---

# The Lie algebra `su(n)` in the hermitian presentation

The module `Physlib.Mathematics.Groups.SpecialUnitary.LieAlgebra.Basic`, [Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean): 34 declarations (3 instances with no name), 33 with a docstring.

## i. Overview

> In physics, `su(n)` is described through generators `T^a`, `a = 1, …, n² - 1`, a basis of the
> traceless hermitian `n × n` complex matrices, satisfying `[T^a, T^b] = i f_{abc} T^c` with real
> structure constants `f_{abc}`. Here `i` is the imaginary unit and the repeated index `c` is summed.
> This file makes the traceless hermitian matrices into a real Lie algebra with the bracket
> `⁅x, y⁆ = i (x y - y x)`, on which the unitary group acts by conjugation. The construction allows
> entries in any commutative `*`-ring `R` that is both a real and a complex `*`-algebra, as
> `SULieAlgebra n R`; the Lie algebra `su(n)` itself is `SULieAlgebra n ℂ`.
>
> Sending `z ⊗ x` to the matrix `z x` identifies the complexification `ℂ ⊗[ℝ] su(n)` with the
> traceless complex matrices. The inverse writes a traceless matrix `M` as `ℜ M + i ℑ M`, its real
> and imaginary parts `ℜ M` and `ℑ M` being traceless hermitian.

## ii. Key results

> - `SULieAlgebra n R` : traceless hermitian `n × n` matrices over `R`, as a real Lie algebra.
> - `SULieAlgebra.conj` : the representation `x ↦ U x U†` of the unitary group.
> - `SULieAlgebra.conj_lie` : conjugation by a unitary matrix preserves the bracket.
> - `SULieAlgebra.Complexification n` : the complexification `ℂ ⊗[ℝ] su(n)`.
> - `SULieAlgebra.toMatrixℂ` : the underlying matrix of an element of the complexification.
> - `SULieAlgebra.toMatrixℂ_lie` : the matrix of a bracket is `i` times the commutator.
> - `SULieAlgebra.toMatrixℂ_injective`, `SULieAlgebra.range_toMatrixℂ` : the complexification is
>   the traceless complex matrices.
> - `SULieAlgebra.equivTraceKer` : the linear equivalence between the complexification and the
>   traceless complex matrices.
> - `SULieAlgebra.finrank_eq`, `SULieAlgebra.finrank_complexification` : `su(n)` and its
>   complexification have dimension `n² - 1`.

## iv. References

> * None.

## A. Traceless hermitian matrices

> Since `i A` is skew-hermitian when `A` is hermitian, the traceless hermitian matrices form a real
> vector space.

**`SULieAlgebra.submodule`**, an abbrev, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L82).

> The traceless hermitian `n × n` matrices with entries in `R`, as a real subspace.

```lean
abbrev SULieAlgebra.submodule (n : ℕ) (R : Type*) [CommRing R] [StarRing R] [Algebra ℝ R]
    [StarModule ℝ R] : Submodule ℝ (Matrix (Fin n) (Fin n) R)
```

**`SULieAlgebra`**, an abbrev, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L89).

> Traceless hermitian `n × n` matrices with entries in `R`, as a real Lie algebra;
> `SULieAlgebra n ℂ` is `su(n)`.

```lean
abbrev SULieAlgebra (n : ℕ) (R : Type*) [CommRing R] [StarRing R] [Algebra ℝ R]
    [StarModule ℝ R] : Type _
```

**`SULieAlgebra.ofMatrix`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L98).

> The element given by a traceless hermitian matrix.

```lean
def ofMatrix (A : Matrix (Fin n) (Fin n) R) (hA : star A = A) (hT : A.trace = 0) :
    SULieAlgebra n R
```

**`SULieAlgebra.val_ofMatrix`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L103).

> The underlying matrix of `ofMatrix A hA hT` is `A`.

```lean
lemma val_ofMatrix (A : Matrix (Fin n) (Fin n) R) (hA : star A = A) (hT : A.trace = 0) :
    (ofMatrix A hA hT).1 = A
```

**`SULieAlgebra.star_val_eq`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L107).

> The underlying matrix of an element is hermitian.

```lean
lemma star_val_eq (x : SULieAlgebra n R) : star x.1 = x.1
```

**`SULieAlgebra.trace_val_eq_zero`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L110).

> The underlying matrix of an element is traceless.

```lean
lemma trace_val_eq_zero (x : SULieAlgebra n R) : x.1.trace = 0
```

## B. The conjugation representation

> Conjugation `x ↦ U x U†` by a unitary matrix `U` preserves traceless hermitian matrices, by
> `U† U = 1` and cyclicity of the trace, and defines a representation of the unitary group.

**`SULieAlgebra.conj`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L122).

> The conjugation representation of the unitary group on `SULieAlgebra n R`: `x ↦ U x U†`.

```lean
noncomputable def conj : Representation ℝ (unitaryGroup (Fin n) R) (SULieAlgebra n R)
```

**`SULieAlgebra.val_conj_apply`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L136).

> The underlying matrix of `conj U x` is `U x U†`.

```lean
lemma val_conj_apply (U : unitaryGroup (Fin n) R) (x : SULieAlgebra n R) :
    (conj U x).1 = U.1 * x.1 * star U.1
```

## C. The bracket

> From here on `R` is also a complex `*`-algebra, so that matrices can be multiplied by `i`. The
> commutator of two hermitian matrices is skew-hermitian, and multiplying it by `i` makes it
> hermitian again, giving the bracket `⁅x, y⁆ = i (x y - y x)`. Being `i` times the commutator, it
> is a Lie bracket.
>
> Since `[i x, i y] = i ⁅x, y⁆`, multiplication by `i` turns this bracket into the commutator of
> traceless skew-hermitian matrices, the usual mathematical presentation of `su(n)`.
>
> The factor `i` flips the sign of the structure constants; if `[T^a, T^b] = i f_{abc} T^c`, then
> `⁅T^a, T^b⁆ = -f_{abc} T^c`.

**An instance with no name**, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L159).

> The bracket `⁅x, y⁆ = i (x y - y x)`.

```lean
noncomputable instance : Bracket (SULieAlgebra n R) (SULieAlgebra n R)
```

**`SULieAlgebra.val_bracket`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L168).

> The underlying matrix of `⁅x, y⁆` is `i (x y - y x)`.

```lean
lemma val_bracket (x y : SULieAlgebra n R) :
    ⁅x, y⁆.1 = Complex.I • (x.1 * y.1 - y.1 * x.1)
```

**An instance with no name**, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L172).

> `⁅x, y⁆ = i (x y - y x)` makes `SULieAlgebra n R` a Lie ring.

```lean
noncomputable instance : LieRing (SULieAlgebra n R)
```

**An instance with no name**, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L186).

> The bracket is `ℝ`-bilinear, so `SULieAlgebra n R` is a real Lie algebra.

```lean
noncomputable instance : LieAlgebra ℝ (SULieAlgebra n R)
```

## D. Conjugation preserves the bracket

**`SULieAlgebra.conj_lie`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L202).

> Conjugation by a unitary matrix preserves the bracket, so `conj` acts by Lie algebra
> automorphisms.

```lean
lemma conj_lie (U : unitaryGroup (Fin n) R) (x y : SULieAlgebra n R) :
    conj U ⁅x, y⁆ = ⁅conj U x, conj U y⁆
```

## E. The complexification

**`SULieAlgebra.Complexification`**, an abbrev, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L216).

> The complexification `ℂ ⊗[ℝ] su(n)` of `su(n)`, a complex Lie algebra.

```lean
abbrev Complexification (n : ℕ) : Type
```

### E.1. The underlying matrix of the complexification

**`SULieAlgebra.toMatrixℂ`**, a def, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L225).

> The underlying matrix of an element of the complexification, `z ⊗ x ↦ z x`.

```lean
noncomputable def toMatrixℂ : Complexification n →ₗ[ℂ] Matrix (Fin n) (Fin n) ℂ
```

**`SULieAlgebra.toMatrixℂ_tmul`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L229).

```lean
lemma toMatrixℂ_tmul (z : ℂ) (x : SULieAlgebra n ℂ) : toMatrixℂ (z ⊗ₜ x) = z • x.1
```

**`SULieAlgebra.trace_toMatrixℂ`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L232).

> The underlying matrix of an element of the complexification is traceless.

```lean
lemma trace_toMatrixℂ (A : Complexification n) : (toMatrixℂ A).trace = 0
```

**`SULieAlgebra.toMatrixℂ_lie`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L239).

> The matrix of a bracket is `i` times the commutator of the matrices, `[A, B] ↦ i (A B - B A)`,
> as in `su(n)` itself.

```lean
lemma toMatrixℂ_lie (A B : Complexification n) :
    toMatrixℂ ⁅A, B⁆ = Complex.I • (toMatrixℂ A * toMatrixℂ B - toMatrixℂ B * toMatrixℂ A)
```

### E.2. The element with a given traceless matrix

**`SULieAlgebra.ofTracelessℂ`**, a def, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L265).

> The element `1 ⊗ ℜ M + i ⊗ ℑ M` of the complexification with the traceless matrix `M`.

```lean
noncomputable def ofTracelessℂ (M : Matrix (Fin n) (Fin n) ℂ) (hM : M.trace = 0) :
    Complexification n
```

**`SULieAlgebra.toMatrixℂ_ofTracelessℂ`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L276).

> The matrix of `ofTracelessℂ M` is `M = ℜ M + i ℑ M`.

```lean
lemma toMatrixℂ_ofTracelessℂ (M : Matrix (Fin n) (Fin n) ℂ) (hM : M.trace = 0) :
    toMatrixℂ (ofTracelessℂ M hM) = M
```

**`SULieAlgebra.ofTracelessℂ_add`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L282).

> `ofTracelessℂ` is additive.

```lean
lemma ofTracelessℂ_add (M N : Matrix (Fin n) (Fin n) ℂ) (hM : M.trace = 0) (hN : N.trace = 0)
    (hMN : (M + N).trace = 0) :
    ofTracelessℂ (M + N) hMN = ofTracelessℂ M hM + ofTracelessℂ N hN
```

**`SULieAlgebra.ofTracelessℂ_toMatrixℂ`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L290).

> An element of the complexification is recovered from its matrix.

```lean
lemma ofTracelessℂ_toMatrixℂ (A : Complexification n) :
    ofTracelessℂ (toMatrixℂ A) (trace_toMatrixℂ A) = A
```

### E.3. The injectivity and surjectivity of the matrix map

**`SULieAlgebra.toMatrixℂ_injective`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L318).

> An element of the complexification is determined by its matrix.

```lean
lemma toMatrixℂ_injective : Function.Injective (toMatrixℂ (n := n))
```

**`SULieAlgebra.range_toMatrixℂ`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L323).

> The matrices of elements of the complexification are exactly the traceless matrices.

```lean
lemma range_toMatrixℂ :
    LinearMap.range (toMatrixℂ (n := n)) = LinearMap.ker (Matrix.traceLinearMap (Fin n) ℂ ℂ)
```

### E.4. Commuting with all elements of `su(n)`

**`SULieAlgebra.commute_of_forall_commute_val`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L338).

> A matrix commuting with every element of `su(n)` commutes with every matrix: it commutes with
> the traceless matrices, which `su(n)` spans over `ℂ`, and with the identity.

```lean
lemma commute_of_forall_commute_val {M : Matrix (Fin n) (Fin n) ℂ}
    (h : ∀ x : SULieAlgebra n ℂ, Commute M x.1) (N : Matrix (Fin n) (Fin n) ℂ) : Commute M N
```

### E.5. Linear equivalences

**`SULieAlgebra.equivTraceKer`**, a def, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L360).

> The linear equivalence between the complexification of `su(n)` and the traceless complex
> matrices, sending an element to its matrix.

```lean
noncomputable def equivTraceKer :
    Complexification n ≃ₗ[ℂ] LinearMap.ker (Matrix.traceLinearMap (Fin n) ℂ ℂ)
```

**`SULieAlgebra.val_equivTraceKer`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L371).

> The matrix of `equivTraceKer A` is the matrix of `A`.

```lean
lemma val_equivTraceKer (A : Complexification n) : (equivTraceKer A).1 = toMatrixℂ A
```

**`SULieAlgebra.toMatrixℂ_equivTraceKer_symm`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L375).

> The matrix of `equivTraceKer.symm M` is `M`.

```lean
lemma toMatrixℂ_equivTraceKer_symm (M : LinearMap.ker (traceLinearMap (Fin n) ℂ ℂ)) :
    toMatrixℂ (equivTraceKer.symm M) = M.1
```

### E.6. Specific elements

**`SULieAlgebra.singleℂ`**, a def, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L385).

> The element of the complexification supported at the single off-diagonal entry `(p, q)`.

```lean
noncomputable def singleℂ (p q : Fin n) (h : p ≠ q) : Complexification n
```

**`SULieAlgebra.diagDiffℂ`**, a def, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L390).

> The element of the complexification corresponding to the difference of diagonal
> entries `(p, p) - (q, q)`.

```lean
noncomputable def diagDiffℂ (p q : Fin n) : Complexification n
```

### E.7. Spanning the complexification

> The elements supported at an off-diagonal entry, together with the differences `E_pp - E_qq`,
> span the complexification.

**`SULieAlgebra.submodule_eq_top_of_singleℂ_mem_of_diagDiffℂ_mem`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L404).

> A submodule of the complexification containing every element supported at a single
> off-diagonal entry, and every difference of two diagonal entries, is everything.

```lean
lemma submodule_eq_top_of_singleℂ_mem_of_diagDiffℂ_mem {n : ℕ}
    {W : Submodule ℂ (Complexification n)}
    (hoff : ∀ (p q : Fin n) (h : p ≠ q), singleℂ p q h ∈ W)
    (hdiag : ∀ p q : Fin n, diagDiffℂ p q ∈ W) :
    W = ⊤
```

**`SULieAlgebra.singleℂ_diagDiffℂ_span_eq_top`**, a lemma, [line 431](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L431).

> The elements supported at a single off-diagonal entry, together with the differences of two
> diagonal entries, span the complexification.

```lean
lemma singleℂ_diagDiffℂ_span_eq_top {n : ℕ} :
    Submodule.span ℂ ({A : Complexification n | ∃ (p q : Fin n) (h : p ≠ q), A = singleℂ p q h} ∪
      {A : Complexification n | ∃ p q : Fin n, A = diagDiffℂ p q}) = ⊤
```

## F. The dimension

**`SULieAlgebra.finrank_complexification`**, a lemma, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L446).

> The complexification `ℂ ⊗[ℝ] su(n)` has complex dimension `n² - 1`: it is the traceless
> matrices, and the trace is onto for `0 < n`.

```lean
lemma finrank_complexification : Module.finrank ℂ (Complexification n) = n ^ 2 - 1
```

**`SULieAlgebra.finrank_eq`**, a lemma, [line 458](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean#L458).

> `su(n)` has real dimension `n² - 1`, the dimension of its complexification.

```lean
lemma finrank_eq : Module.finrank ℝ (SULieAlgebra n ℂ) = n ^ 2 - 1
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Basic.lean)
