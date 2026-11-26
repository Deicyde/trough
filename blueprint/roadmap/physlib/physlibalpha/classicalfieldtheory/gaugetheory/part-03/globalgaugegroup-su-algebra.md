---
declaration: module
origin: cited
lean: SUAlgebraOver.submodule, SUAlgebraOver, SUAlgebraOver.mem_iff, SUAlgebraOver.ofMatrix, SUAlgebraOver.ofMatrix_val, SUAlgebraOver.star_val, SUAlgebraOver.trace_val, SUAlgebraOver.ext
statement: formalized
proof: formalized
---

# The Lie algebra `su(n)` over a `*`-algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SU.Algebra`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean): 15 declarations (3 instances with no name), 11 with a docstring.

> The traceless hermitian matrices over a `*`-algebra, with the bracket `i (a b − b a)`.

## i. Overview

> The Lie algebra of `SU(n)` is the real Lie algebra of traceless hermitian `n × n` matrices,
> with bracket `⁅a, b⁆ = i (a b − b a)`. The factor of `i` keeps the bracket of two hermitian
> matrices hermitian. Nothing in this description depends on the entries being complex
> numbers, and it makes sense over any commutative `*`-algebra `R` over `ℂ`, and the two cases the
> theory of jets needs are `R = ℂ` (the Lie algebra itself) and `R` the ring of formal power
> series in the spacetime coordinates (its jets). `SUAlgebraOver R n` is this Lie algebra,
> together with the conjugation action `a ↦ U a U†` of the unitary group of `R`.
>
> Over `R = ℂ` the Lie algebra is real, since `i` times a hermitian matrix is anti-hermitian. Its
> complexification `ℂ ⊗[ℝ] su(n)` is `SUAlgebraComplexified n`, the complex vector space on which
> the adjoint representation of `SU(n)` acts in the complex tensors of `SU(n)`.

## ii. Key results

> - `SUAlgebraOver` : the traceless hermitian matrices as a real Lie algebra.
> - `SUAlgebraOver.conj` : the conjugation representation of the unitary group.
> - `SUAlgebraComplexified` : the complexification of `su(n)`.

## iv. References

> * None.

## A. Traceless hermitian matrices

**`SUAlgebraOver.submodule`**, an abbrev, [line 61](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean#L61).

> The submodule of traceless hermitian matrices.

```lean
abbrev SUAlgebraOver.submodule (R : Type) [CommRing R] [StarRing R] [Algebra ℝ R]
    [StarModule ℝ R] (n : ℕ) : Submodule ℝ (Matrix (Fin n) (Fin n) R)
```

**`SUAlgebraOver`**, an abbrev, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean#L68).

> The Lie algebra `su(n)` over `R`, the traceless hermitian `n × n` matrices with entries in
> `R`, a real Lie algebra with bracket `i (a b − b a)`.

```lean
abbrev SUAlgebraOver (R : Type) [CommRing R] [StarRing R] [Algebra ℝ R] [StarModule ℝ R]
    (n : ℕ) : Type
```

**`SUAlgebraOver.mem_iff`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean#L77).

> A matrix lies in the real Lie algebra `su(n)` exactly when it is hermitian and traceless.

```lean
lemma mem_iff (A : Matrix (Fin n) (Fin n) R) :
    A ∈ submodule R n ↔ star A = A ∧ A.trace = 0
```

**`SUAlgebraOver.ofMatrix`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean#L81).

> An element from a traceless hermitian matrix.

```lean
def ofMatrix (A : Matrix (Fin n) (Fin n) R) (hA : star A = A) (hT : A.trace = 0) :
    SUAlgebraOver R n
```

**`SUAlgebraOver.ofMatrix_val`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean#L86).

```lean
lemma ofMatrix_val (A : Matrix (Fin n) (Fin n) R) (hA : star A = A) (hT : A.trace = 0) :
    (ofMatrix A hA hT).1 = A
```

**`SUAlgebraOver.star_val`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean#L90).

> Every element of `su(n)`, viewed as a matrix, is hermitian.

```lean
lemma star_val (a : SUAlgebraOver R n) : star a.1 = a.1
```

**`SUAlgebraOver.trace_val`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean#L93).

> Every element of `su(n)`, viewed as a matrix, is traceless.

```lean
lemma trace_val (a : SUAlgebraOver R n) : a.1.trace = 0
```

**`SUAlgebraOver.ext`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean#L97).

> Two elements of `su(n)` are equal when their underlying matrices are equal.

```lean
lemma ext {a b : SUAlgebraOver R n} (h : a.1 = b.1) : a = b
```

## B. The conjugation representation

**`SUAlgebraOver.conj`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean#L106).

> The conjugation representation of the unitary group on `su(n)`, `a ↦ U a U†`.

```lean
noncomputable def conj : Representation ℝ (unitaryGroup (Fin n) R) (SUAlgebraOver R n)
```

**`SUAlgebraOver.conj_apply_val`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean#L119).

```lean
lemma conj_apply_val (U : unitaryGroup (Fin n) R) (a : SUAlgebraOver R n) :
    (conj U a).1 = U.1 * a.1 * star U.1
```

## C. The bracket

**An instance with no name**, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean#L131).

> The bracket `i (a b − b a)`.

```lean
noncomputable instance : Bracket (SUAlgebraOver R n) (SUAlgebraOver R n)
```

**`SUAlgebraOver.bracket_val`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean#L140).

> The matrix of the bracket of two elements of `su(n)` is `i` times their commutator.

```lean
lemma bracket_val (a b : SUAlgebraOver R n) :
    ⁅a, b⁆.1 = Complex.I • (a.1 * b.1 - b.1 * a.1)
```

**An instance with no name**, [line 143](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean#L143).

```lean
noncomputable instance : LieRing (SUAlgebraOver R n)
```

**An instance with no name**, [line 158](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean#L158).

```lean
noncomputable instance : LieAlgebra ℝ (SUAlgebraOver R n)
```

## D. The complexification

**`SUAlgebraComplexified`**, an abbrev, [line 176](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean#L176).

> The complexified Lie algebra `su(n)_ℂ = ℂ ⊗[ℝ] su(n)`, a complex vector space.

```lean
abbrev SUAlgebraComplexified (n : ℕ) : Type
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Algebra.lean)
