---
declaration: module
origin: cited
lean: SULieAlgebra.GellMannIndex.equivTwo, SULieAlgebra.gellMannMatrices_two, SULieAlgebra.GellMannIndex.equivThree, SULieAlgebra.gellMannMatrices_three
statement: formalized
proof: formalized
---

# The Pauli and Gell-Mann matrices

The module `Physlib.Mathematics.Groups.SpecialUnitary.LieAlgebra.GellMann.SpecialCases`, [Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/SpecialCases.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/SpecialCases.lean): 4 declarations, 4 with a docstring.

> The generalized Gell-Mann matrices in the special cases `n = 2` and `n = 3`.

## i. Overview

> For `n = 2` the generalized Gell-Mann matrices are the Pauli matrices `σ₁, σ₂, σ₃` (A), and for
> `n = 3` they are the Gell-Mann matrices `λ₁, …, λ₈` (B). In each case an equivalence of
> `GellMannIndex n` with `Fin (n² - 1)` puts the labels in the standard order.

## ii. Key results

> - `SULieAlgebra.gellMannMatrices_two` : for `n = 2`, the Pauli matrices `σ₁, σ₂, σ₃`.
> - `SULieAlgebra.gellMannMatrices_three` : for `n = 3`, the Gell-Mann matrices `λ₁, …, λ₈`.

## iv. References

> * https://mathworld.wolfram.com/GeneralizedGell-MannMatrix.html

## A. The case `n = 2`

**`SULieAlgebra.GellMannIndex.equivTwo`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/SpecialCases.lean#L52).

> For `n = 2`, the labelling of the generalized Gell-Mann matrices as the Pauli matrices
> `σ₁, σ₂, σ₃` (as `0, 1, 2`): the symmetric, antisymmetric and diagonal matrices.

```lean
def GellMannIndex.equivTwo : GellMannIndex 2 ≃ Fin 3
```

**`SULieAlgebra.gellMannMatrices_two`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/SpecialCases.lean#L68).

> For `n = 2` the generalized Gell-Mann matrices are the Pauli matrices `σ₁, σ₂, σ₃`, labelled
> by `GellMannIndex.equivTwo`.

```lean
lemma gellMannMatrices_two (i : Fin 3) :
    (gellMannMatrices (GellMannIndex.equivTwo.symm i)).1 = PauliMatrix.pauliMatrix (Sum.inr i)
```

## B. The case `n = 3`

**`SULieAlgebra.GellMannIndex.equivThree`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/SpecialCases.lean#L83).

> For `n = 3`, the labelling of the Gell-Mann matrices in the standard order `λ₁, …, λ₈`
> (as `0, …, 7`): `λ₁, λ₂, λ₃` are the symmetric, antisymmetric and diagonal matrices of the first
> two coordinates, `λ₄, λ₅` the symmetric and antisymmetric ones of the coordinates `0, 2`,
> `λ₆, λ₇` those of the coordinates `1, 2`, and `λ₈` the second diagonal matrix.

```lean
def GellMannIndex.equivThree : GellMannIndex 3 ≃ Fin 8
```

**`SULieAlgebra.gellMannMatrices_three`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/SpecialCases.lean#L99).

> For `n = 3` the generalized Gell-Mann matrices are the Gell-Mann matrices `λ₁, …, λ₈`, labelled
> in the standard order by `GellMannIndex.equivThree`.

```lean
lemma gellMannMatrices_three :
    (fun i => (gellMannMatrices (GellMannIndex.equivThree.symm i)).1) =
    ![!![0, 1, 0; 1, 0, 0; 0, 0, 0],
      !![0, -Complex.I, 0; Complex.I, 0, 0; 0, 0, 0],
      !![1, 0, 0; 0, -1, 0; 0, 0, 0],
      !![0, 0, 1; 0, 0, 0; 1, 0, 0],
      !![0, 0, -Complex.I; 0, 0, 0; Complex.I, 0, 0],
      !![0, 0, 0; 0, 0, 1; 0, 1, 0],
      !![0, 0, 0; 0, 0, -Complex.I; 0, Complex.I, 0],
      (1 / Real.sqrt 3 : ℂ) • !![1, 0, 0; 0, 1, 0; 0, 0, -2]]
```

## Depends on

- [The generalized Gell-Mann matrices (Physlib)](specialunitary-liealgebra-gellmann-basic.md)
- [Physlib.Relativity.PauliMatrices.Basic](../../relativity/paulimatrices/basic.md)

## Sources

- [Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/SpecialCases.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/SpecialCases.lean)
