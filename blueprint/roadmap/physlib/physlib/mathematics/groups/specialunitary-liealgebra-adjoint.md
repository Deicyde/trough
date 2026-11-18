---
declaration: module
origin: cited
lean: SULieAlgebra.adjoint, SULieAlgebra.adjoint_val, SULieAlgebra.adjoint_lie, SULieAlgebra.adjoint_eq_one_iff, SULieAlgebra.adjoint_eq_iff, SULieAlgebra.adjointℂ, SULieAlgebra.adjointℂ_tmul, SULieAlgebra.adjointℂ_lie
statement: formalized
proof: formalized
---

# The adjoint representation of `SU(n)`

The module `Physlib.Mathematics.Groups.SpecialUnitary.LieAlgebra.Adjoint`, [Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean): 22 declarations, 20 with a docstring.

> The adjoint representation of `SU(n)` and its complexification, defined as `x ↦ g x g†`, and
> the irreducibility of the latter.

## i. Overview

> We define the adjont representation of `SU(n)` on its Lie algebra `su(n)` and its complexification.
> The adjoint is defined by conjugation, `x ↦ g x g†`. It preserves the bracket, and its kernel is
> the centre of `SU(n)`, the scalar matrices (A.1, A.2). On the underlying matrices of the
> complexification the adjoint action of any unitary matrix, and in particular of any permutation of
> the coordinates, is realised by an element of `SU(n)`; diagonal elements of `SU(n)` act on the
> entries by phases (A.3). The complex adjoint representation is irreducible for `2 ≤ n` (C.1),
> and hence, by Schur's lemma over an algebraically closed field, that every endomorphism of the
> complexification commuting with the adjoint action is a multiple of the identity (C.2).

## ii. Key results

> - `SULieAlgebra.adjoint` : the adjoint representation on `su(n)`.
> - `SULieAlgebra.adjointℂ` : the adjoint representation on the complexification.
> - `SULieAlgebra.adjoint_eq_iff` : the adjoint representation is faithful modulo the centre.
> - `SULieAlgebra.isIrreducible_adjointℂ` : the complex adjoint representation is irreducible.
> - `SULieAlgebra.end_eq_smul_id_of_commute_adjointℂ` : Schur's lemma for the complex adjoint
>   representation.

## iv. References

> * None.

## A. The adjoint representation

### A.1. The real adjoint representation

**`SULieAlgebra.adjoint`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L76).

> The adjoint representation `x ↦ g x g†` of `SU(n)` on its real Lie algebra `su(n)`.

```lean
noncomputable def adjoint {n : ℕ} :
    Representation ℝ (specialUnitaryGroup (Fin n) ℂ) (SULieAlgebra n ℂ)
```

**`SULieAlgebra.adjoint_val`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L82).

> The underlying matrix of `adjoint g x` is `g x g†`.

```lean
lemma adjoint_val {n : ℕ} (g : specialUnitaryGroup (Fin n) ℂ) (x : SULieAlgebra n ℂ) :
    (adjoint g x).1 = g.1 * x.1 * star g.1
```

**`SULieAlgebra.adjoint_lie`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L87).

> The adjoint representation preserves the bracket, so `SU(n)` acts on `su(n)` by Lie algebra
> automorphisms.

```lean
lemma adjoint_lie {n : ℕ} (g : specialUnitaryGroup (Fin n) ℂ) (x y : SULieAlgebra n ℂ) :
    adjoint g ⁅x, y⁆ = ⁅adjoint g x, adjoint g y⁆
```

**`SULieAlgebra.adjoint_eq_one_iff`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L93).

> The kernel of the adjoint representation is the centre of `SU(n)`: `g` acts trivially exactly
> when it is a scalar matrix `c 1`.

```lean
lemma adjoint_eq_one_iff {n : ℕ} (g : specialUnitaryGroup (Fin n) ℂ) :
    adjoint g = 1 ↔ ∃ c : ℂ, g.1 = c • 1
```

**`SULieAlgebra.adjoint_eq_iff`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L118).

> Two elements of `SU(n)` have the same adjoint action exactly when they differ by a scalar:
> the adjoint representation is faithful on `SU(n)` modulo its centre.

```lean
lemma adjoint_eq_iff {n : ℕ} (g h : specialUnitaryGroup (Fin n) ℂ) :
    adjoint g = adjoint h ↔ ∃ c : ℂ, g.1 = c • h.1
```

### A.2. The complex adjoint representation

**`SULieAlgebra.adjointℂ`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L141).

> The adjoint representation of `SU(n)` on the complexification `ℂ ⊗[ℝ] su(n)`: the
> complexification of the adjoint representation `adjoint` on `su(n)`.

```lean
noncomputable def adjointℂ {n : ℕ} :
    Representation ℂ (specialUnitaryGroup (Fin n) ℂ) (Complexification n)
```

**`SULieAlgebra.adjointℂ_tmul`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L147).

```lean
lemma adjointℂ_tmul {n : ℕ} (g : specialUnitaryGroup (Fin n) ℂ) (z : ℂ) (x : SULieAlgebra n ℂ) :
    adjointℂ g (z ⊗ₜ x) = z ⊗ₜ adjoint g x
```

**`SULieAlgebra.adjointℂ_lie`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L152).

> The complex adjoint representation preserves the bracket of the complexification, so `SU(n)`
> acts on `ℂ ⊗[ℝ] su(n)` by Lie algebra automorphisms.

```lean
lemma adjointℂ_lie {n : ℕ} (g : specialUnitaryGroup (Fin n) ℂ) (A B : Complexification n) :
    adjointℂ g ⁅A, B⁆ = ⁅adjointℂ g A, adjointℂ g B⁆
```

**`SULieAlgebra.adjointℂ_eq_one_iff`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L169).

> The kernel of the complex adjoint representation is the centre of `SU(n)`, as for the real
> adjoint representation.

```lean
lemma adjointℂ_eq_one_iff {n : ℕ} (g : specialUnitaryGroup (Fin n) ℂ) :
    adjointℂ g = 1 ↔ ∃ c : ℂ, g.1 = c • 1
```

**`SULieAlgebra.adjointℂ_eq_iff`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L181).

> Two elements of `SU(n)` have the same complex adjoint action exactly when they differ by a
> scalar, as for the real adjoint representation.

```lean
lemma adjointℂ_eq_iff {n : ℕ} (g h : specialUnitaryGroup (Fin n) ℂ) :
    adjointℂ g = adjointℂ h ↔ ∃ c : ℂ, g.1 = c • h.1
```

### A.3. The action on the underlying matrices

**`SULieAlgebra.toMatrixℂ_adjointℂ`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L198).

> The adjoint representation conjugates the matrix, `M ↦ g M g†`.

```lean
lemma toMatrixℂ_adjointℂ {n} (g : specialUnitaryGroup (Fin n) ℂ) (A : Complexification n) :
    toMatrixℂ (adjointℂ g A) = g.1 * toMatrixℂ A * star g.1
```

**`SULieAlgebra.exists_toMatrixℂ_adjointℂ_eq_unitary`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L209).

> Conjugation by any unitary matrix is the adjoint action of an element of `SU(n)`: a
> unitary matrix agrees with an element of `SU(n)` up to a phase, which conjugation does not
> see.

```lean
lemma exists_toMatrixℂ_adjointℂ_eq_unitary {n : ℕ} (U : unitaryGroup (Fin n) ℂ) :
    ∃ g : specialUnitaryGroup (Fin n) ℂ, ∀ A : Complexification n,
      toMatrixℂ (adjointℂ g A) = U.1 * toMatrixℂ A * star U.1
```

**`SULieAlgebra.exists_toMatrixℂ_adjointℂ_apply_perm`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L231).

> The adjoint action realises any permutation `σ` of the coordinates: some element of `SU(n)`
> moves the entry `(x, y)` of every matrix to `(σ x, σ y)`.

```lean
lemma exists_toMatrixℂ_adjointℂ_apply_perm {n : ℕ} (σ : Equiv.Perm (Fin n)) :
    ∃ g : specialUnitaryGroup (Fin n) ℂ, ∀ A x y,
      toMatrixℂ (adjointℂ g A) (σ x) (σ y) = toMatrixℂ A x y
```

**`SULieAlgebra.toMatrixℂ_adjointℂ_apply_of_diagonal`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L248).

> The adjoint action of a diagonal element of `SU(n)` scales the entry at `(x, y)` of the
> matrix by `d x * star (d y)`.

```lean
lemma toMatrixℂ_adjointℂ_apply_of_diagonal {n} {g : specialUnitaryGroup (Fin n) ℂ}
    {d : Fin n → ℂ} (hg : g.1 = diagonal d) (A : Complexification n) (x y : Fin n) :
    toMatrixℂ (adjointℂ g A) x y = d x * star (d y) * toMatrixℂ A x y
```

**`SULieAlgebra.toMatrixℂ_adjointℂ_trace`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L255).

```lean
lemma toMatrixℂ_adjointℂ_trace {n} (g : specialUnitaryGroup (Fin n) ℂ) (A : Complexification n) :
    (toMatrixℂ (adjointℂ g A)).trace = (toMatrixℂ A).trace
```

## B. The relation to single-entry elements

**`SULieAlgebra.exists_adjointℂ_singleℂ_eq_singleℂ`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L267).

> All the off-diagonal matrix units `singleℂ` lie in one adjoint orbit

```lean
lemma exists_adjointℂ_singleℂ_eq_singleℂ {n : ℕ} {i j p q : Fin n} (hij : i ≠ j) (hpq : p ≠ q) :
    ∃ g : specialUnitaryGroup (Fin n) ℂ, adjointℂ g (singleℂ i j hij) = singleℂ p q hpq
```

**`SULieAlgebra.singleℂ_mem_span_range_adjointℂ`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L281).

> If the matrix of `A` has a non-zero entry at the off-diagonal position `(p, q)`, then
> `singleℂ p q h` lies in the span of the adjoint orbit of `A`.

```lean
lemma singleℂ_mem_span_range_adjointℂ {n : ℕ} {p q : Fin n} (h : p ≠ q)
    {A : Complexification n} (hA : toMatrixℂ A p q ≠ 0) :
    singleℂ p q h ∈ Submodule.span ℂ (Set.range fun g => adjointℂ g A)
```

**`SULieAlgebra.exists_adjointℂ_eq_of_toMatrixℂ_eq_diagonal`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L327).

> The adjoint action of some element of `SU(n)` — the rotation by `π / 4` in the `(p, q)`-plane —
> changes an element whose matrix is the diagonal matrix `d` only in the `(p, q)`-block, by
> `(d p - d q) / 2` times `singleℂ p q h + singleℂ q p h.symm - diagDiffℂ p q`.

```lean
lemma exists_adjointℂ_eq_of_toMatrixℂ_eq_diagonal {n : ℕ} {p q : Fin n} (h : p ≠ q)
    {A : Complexification n} {d : Fin n → ℂ} (hA : toMatrixℂ A = diagonal d) :
    ∃ g : specialUnitaryGroup (Fin n) ℂ, adjointℂ g A =
      A + ((d p - d q) / 2) • (singleℂ p q h + singleℂ q p h.symm - diagDiffℂ p q)
```

**`SULieAlgebra.exists_diagDiffℂ_eq_adjointℂ_singleℂ_add_singleℂ`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L358).

> The difference of two diagonal entries lies in the adjoint orbit of the sum of the two
> elements supported at the corresponding off-diagonal entries.

```lean
lemma exists_diagDiffℂ_eq_adjointℂ_singleℂ_add_singleℂ {n : ℕ} {p q : Fin n} (h : p ≠ q) :
    ∃ g : specialUnitaryGroup (Fin n) ℂ,
      diagDiffℂ p q = adjointℂ g (singleℂ p q h + singleℂ q p h.symm)
```

**`SULieAlgebra.exists_singleℂ_mem_span_range_adjointℂ`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L377).

> The span of the adjoint orbit of a non-zero element contains an element supported at a single
> off-diagonal entry.

```lean
lemma exists_singleℂ_mem_span_range_adjointℂ {n : ℕ} {A : Complexification n} (hA : A ≠ 0) :
    ∃ (p q : Fin n) (h : p ≠ q),
      singleℂ p q h ∈ Submodule.span ℂ (Set.range fun g => adjointℂ g A)
```

## C. Irreducibility and Schur's lemma

### C.1. Irreducibility

> The complex adjoint representation has no proper non-zero subrepresentations.

**`SULieAlgebra.isIrreducible_adjointℂ`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L417).

> The complex adjoint representation of `SU(n)` is irreducible for `2 ≤ n`.

```lean
lemma isIrreducible_adjointℂ {n : ℕ} (hn : 2 ≤ n) : (adjointℂ (n := n)).IsIrreducible
```

### C.2. Schur's lemma

**`SULieAlgebra.end_eq_smul_id_of_commute_adjointℂ`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean#L449).

> An endomorphism of the complexification commuting with the adjoint action is a scalar.

```lean
lemma end_eq_smul_id_of_commute_adjointℂ {n : ℕ} {T : Module.End ℂ (Complexification n)}
    (hT : ∀ g, T ∘ₗ adjointℂ g = adjointℂ g ∘ₗ T) : ∃ μ : ℂ, T = μ • LinearMap.id
```

## Depends on

- [The Lie algebra `su(n)` in the hermitian presentation](specialunitary-liealgebra-basic.md)

## Sources

- [Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Adjoint.lean)
