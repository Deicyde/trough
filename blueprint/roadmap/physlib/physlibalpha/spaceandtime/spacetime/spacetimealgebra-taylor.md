---
declaration: module
origin: cited
lean: SpaceTimeAlgebra.taylorMatrix, SpaceTimeAlgebra.taylorMatrix_apply, SpaceTimeAlgebra.map_constantCoeff_iteratedPDeriv_taylorMatrix, SpaceTimeAlgebra.derivValueMatrix, SpaceTimeAlgebra.derivValueMatrix_cons, SpaceTimeAlgebra.derivValueMatrix_add, SpaceTimeAlgebra.derivValueMatrix_real_smul, SpaceTimeAlgebra.derivValueMatrix_zero_right
statement: formalized
proof: formalized
---

# Taylor data of matrices of jets

The module `PhyslibAlpha.SpaceAndTime.SpaceTime.SpaceTimeAlgebra.Taylor`, [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean): 11 declarations, 9 with a docstring.

> Matrices of jets are determined by, and can be built from, their base-point Taylor data.

## i. Overview

> A jet is determined by the base-point values of its iterated derivatives, and every family of
> such values is realized by a jet, `SpaceTimeAlgebra.ofDerivValues` (both in Physlib). This file
> carries these two facts, Taylor determinacy and Taylor completeness, over to matrices of jets
> entrywise. `taylorMatrix` builds the matrix of jets with prescribed base-point Taylor data, and
> `derivValueMatrix` reads the base-point Taylor data off a matrix of jets. They are what make a
> Lie algebra jet of a matrix gauge group determined by, and freely prescribed through, its
> base-point Taylor data.

## ii. Key results

> - `SpaceTimeAlgebra.taylorMatrix` : the matrix of jets with prescribed base-point Taylor data.
> - `SpaceTimeAlgebra.map_constantCoeff_iteratedPDeriv_taylorMatrix` : Taylor completeness for
>   matrices of jets.
> - `SpaceTimeAlgebra.derivValueMatrix` : the base-point Taylor data of a matrix of jets.
> - `SpaceTimeAlgebra.derivValueMatrix_eq_smul_map_coeff` : the base-point derivative along
>   `s` is `s!` times the matrix of Taylor coefficients of `x^s`.
> - `SpaceTimeAlgebra.matrix_ext_of_derivValueMatrix` : Taylor determinacy for matrices of jets.

## iv. References

> * None.

## A. Taylor completeness

**`SpaceTimeAlgebra.taylorMatrix`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L59).

> The matrix of jets with prescribed base-point Taylor data `M`, entrywise.

```lean
noncomputable def taylorMatrix {κ : Type} (M : Multiset (Fin 1 ⊕ Fin 3) → Matrix κ κ ℂ) :
    Matrix κ κ SpaceTimeAlgebra
```

**`SpaceTimeAlgebra.taylorMatrix_apply`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L64).

> An entry of `taylorMatrix M` is the jet with the Taylor data of that entry.

```lean
lemma taylorMatrix_apply {κ : Type} (M : Multiset (Fin 1 ⊕ Fin 3) → Matrix κ κ ℂ) (i j : κ) :
    taylorMatrix M i j = ofDerivValues fun s => M s i j
```

**`SpaceTimeAlgebra.map_constantCoeff_iteratedPDeriv_taylorMatrix`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L69).

> The base-point Taylor data of `taylorMatrix M` are `M`, entrywise.

```lean
lemma map_constantCoeff_iteratedPDeriv_taylorMatrix {κ : Type}
    (M : Multiset (Fin 1 ⊕ Fin 3) → Matrix κ κ ℂ) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    (taylorMatrix M).map (fun f => constantCoeff (iteratedPDeriv s f)) = M s
```

## B. Base-point derivatives of matrices of jets

**`SpaceTimeAlgebra.derivValueMatrix`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L88).

> The base-point values of the iterated derivatives of a matrix of jets along a multiset
> of directions, taken entrywise. These are the Taylor coefficients up to the factorial
> factor, matching `SpaceTimeAlgebra.ofDerivValues`.

```lean
noncomputable def derivValueMatrix (s : Multiset (Fin 1 ⊕ Fin 3))
    (A : Matrix κ κ SpaceTimeAlgebra) : Matrix κ κ ℂ
```

**`SpaceTimeAlgebra.derivValueMatrix_cons`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L93).

> One more direction in `s` differentiates the matrix entrywise first.

```lean
lemma derivValueMatrix_cons (μ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (A : Matrix κ κ SpaceTimeAlgebra) :
    derivValueMatrix (μ ::ₘ s) A = derivValueMatrix s (A.map (pderiv μ))
```

**`SpaceTimeAlgebra.derivValueMatrix_add`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L100).

> The base-point Taylor data of a matrix of jets are additive.

```lean
lemma derivValueMatrix_add (s : Multiset (Fin 1 ⊕ Fin 3)) (A B : Matrix κ κ SpaceTimeAlgebra) :
    derivValueMatrix s (A + B) = derivValueMatrix s A + derivValueMatrix s B
```

**`SpaceTimeAlgebra.derivValueMatrix_real_smul`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L106).

> The base-point Taylor data of a matrix of jets commute with real scaling.

```lean
lemma derivValueMatrix_real_smul (s : Multiset (Fin 1 ⊕ Fin 3)) (r : ℝ)
    (A : Matrix κ κ SpaceTimeAlgebra) :
    derivValueMatrix s (r • A) = r • derivValueMatrix s A
```

**`SpaceTimeAlgebra.derivValueMatrix_zero_right`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L115).

```lean
lemma derivValueMatrix_zero_right (s : Multiset (Fin 1 ⊕ Fin 3)) :
    derivValueMatrix s (0 : Matrix κ κ SpaceTimeAlgebra) = 0
```

**`SpaceTimeAlgebra.derivValueMatrix_zero`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L123).

```lean
lemma derivValueMatrix_zero (A : Matrix κ κ SpaceTimeAlgebra) :
    derivValueMatrix 0 A = (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix A
```

**`SpaceTimeAlgebra.derivValueMatrix_eq_smul_map_coeff`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L130).

> The base-point derivative of a matrix of jets along `s` is `s!` times its matrix of
> Taylor coefficients of `x^s`, with `s!` the product of the factorials of the
> multiplicities in `s`.

```lean
lemma derivValueMatrix_eq_smul_map_coeff (s : Multiset (Fin 1 ⊕ Fin 3))
    (A : Matrix κ κ SpaceTimeAlgebra) :
    derivValueMatrix s A = ((∏ ν, (s.count ν).factorial : ℕ) : ℝ) •
      A.map (coeff (Multiset.toFinsupp s))
```

**`SpaceTimeAlgebra.matrix_ext_of_derivValueMatrix`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L140).

> A matrix of jets is determined by its base-point derivatives.

```lean
lemma matrix_ext_of_derivValueMatrix {A B : Matrix κ κ SpaceTimeAlgebra}
    (h : ∀ s, derivValueMatrix s A = derivValueMatrix s B) : A = B
```

## Depends on

- [The spacetime algebra](../../../physlib/spaceandtime/spacetime/spacetimealgebra-basic.md)

## Proof depends on

- [Star, derivatives, truncation and the Euler operator on the jet ring](spacetimealgebra-basic.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean)
