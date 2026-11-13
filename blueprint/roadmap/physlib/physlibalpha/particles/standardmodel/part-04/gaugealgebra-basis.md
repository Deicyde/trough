---
declaration: module
origin: cited
lean: StandardModel.planeEmbed, StandardModel.gellMannMatrix, StandardModel.gellMannMatrix_zero, StandardModel.gellMannMatrix_one, StandardModel.gellMannMatrix_two, StandardModel.gellMannMatrix_three, StandardModel.gellMannMatrix_four, StandardModel.gellMannMatrix_five
statement: formalized
proof: formalized
---

# The standard basis of the gauge algebra

The module `PhyslibAlpha.Particles.StandardModel.GaugeAlgebra.Basis`, [PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean): 76 declarations, 43 with a docstring.

## i. Overview

> The standard basis of the gauge algebra of the Standard Model, indexed by
> `Fin 8 ⊕ Fin 3 ⊕ Fin 1`: the eight Gell-Mann matrices on the `su(3)` factor, the three
> Pauli matrices on the `su(2)` factor, and `1` on the `u(1)` factor.
>
> In this basis the adjoint action of the gauge group is the block-diagonal matrix
> `adjointMatrix`, whose blocks are the trace pairings of the basis elements with their
> conjugates; `adjoint_stdBasis` and `toMatrix_adjoint` identify its action with the
> adjoint action.

## ii. Key results

> - `adjointMatrix`
> - `adjoint_stdBasis` : the adjoint action of the gauge group acts on the standard basis through
>   `adjointMatrix`
> - `toMatrix_adjoint` : the matrix of the adjoint action in the standard basis is `adjointMatrix`

## iv. References

> * None.

## A. The Gell-Mann matrices

> The Pauli matrices `σ1`, `σ2`, `σ3` embedded along the three coordinate planes of
> `Fin 3`, together with the normalised traceless diagonal matrix.

**`StandardModel.planeEmbed`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L66).

> The embedding of `2 × 2` matrices into the `3 × 3` matrices supported on the plane
> of two coordinate directions: the entries of `A` land at the row and column indices
> `p 0` and `p 1`, every other entry vanishing.

```lean
def planeEmbed (p : Fin 2 → Fin 3) (A : Matrix (Fin 2) (Fin 2) ℂ) :
    Matrix (Fin 3) (Fin 3) ℂ
```

**`StandardModel.gellMannMatrix`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L73).

> The Gell-Mann matrices: the standard basis of the traceless hermitian `3 × 3`
> matrices. The first seven are the Pauli matrices `σ1`, `σ2`, `σ3` embedded along the
> three coordinate planes; the eighth is the normalised traceless diagonal matrix.

```lean
def gellMannMatrix : Fin 8 → Matrix (Fin 3) (Fin 3) ℂ
```

**`StandardModel.gellMannMatrix_zero`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L83).

```lean
lemma gellMannMatrix_zero : gellMannMatrix 0 = !![0, 1, 0; 1, 0, 0; 0, 0, 0]
```

**`StandardModel.gellMannMatrix_one`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L88).

```lean
lemma gellMannMatrix_one :
    gellMannMatrix 1 = !![0, -Complex.I, 0; Complex.I, 0, 0; 0, 0, 0]
```

**`StandardModel.gellMannMatrix_two`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L94).

```lean
lemma gellMannMatrix_two : gellMannMatrix 2 = !![1, 0, 0; 0, -1, 0; 0, 0, 0]
```

**`StandardModel.gellMannMatrix_three`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L99).

```lean
lemma gellMannMatrix_three : gellMannMatrix 3 = !![0, 0, 1; 0, 0, 0; 1, 0, 0]
```

**`StandardModel.gellMannMatrix_four`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L104).

```lean
lemma gellMannMatrix_four :
    gellMannMatrix 4 = !![0, 0, -Complex.I; 0, 0, 0; Complex.I, 0, 0]
```

**`StandardModel.gellMannMatrix_five`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L110).

```lean
lemma gellMannMatrix_five : gellMannMatrix 5 = !![0, 0, 0; 0, 0, 1; 0, 1, 0]
```

**`StandardModel.gellMannMatrix_six`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L115).

```lean
lemma gellMannMatrix_six :
    gellMannMatrix 6 = !![0, 0, 0; 0, 0, -Complex.I; 0, Complex.I, 0]
```

**`StandardModel.gellMannMatrix_seven`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L121).

```lean
lemma gellMannMatrix_seven :
    gellMannMatrix 7 = (((Real.sqrt 3 : ℝ) : ℂ))⁻¹ • !![1, 0, 0; 0, 1, 0; 0, 0, -2]
```

**`StandardModel.gellMannMatrix_selfAdjoint`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L125).

> The Gell-Mann matrices are hermitian.

```lean
lemma gellMannMatrix_selfAdjoint (k : Fin 8) :
    star (gellMannMatrix k) = gellMannMatrix k
```

**`StandardModel.gellMannMatrix_trace`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L136).

> The Gell-Mann matrices are traceless.

```lean
lemma gellMannMatrix_trace (k : Fin 8) : (gellMannMatrix k).trace = 0
```

**`StandardModel.sum_smul_gellMannMatrix`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L145).

> A combination of the Gell-Mann matrices, entry by entry.

```lean
lemma sum_smul_gellMannMatrix (g : Fin 8 → ℝ) :
    ∑ k, g k • gellMannMatrix k =
      !![((g 2 + (Real.sqrt 3)⁻¹ * g 7 : ℝ) : ℂ),
          ((g 0 : ℝ) : ℂ) - ((g 1 : ℝ) : ℂ) * Complex.I,
          ((g 3 : ℝ) : ℂ) - ((g 4 : ℝ) : ℂ) * Complex.I;
        ((g 0 : ℝ) : ℂ) + ((g 1 : ℝ) : ℂ) * Complex.I,
          ((-g 2 + (Real.sqrt 3)⁻¹ * g 7 : ℝ) : ℂ),
          ((g 5 : ℝ) : ℂ) - ((g 6 : ℝ) : ℂ) * Complex.I;
        ((g 3 : ℝ) : ℂ) + ((g 4 : ℝ) : ℂ) * Complex.I,
          ((g 5 : ℝ) : ℂ) + ((g 6 : ℝ) : ℂ) * Complex.I,
          ((-2 * (Real.sqrt 3)⁻¹ * g 7 : ℝ) : ℂ)]
```

**`StandardModel.sum_smul_pauliMatrix_inr`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L165).

> A combination of the three Pauli matrices `σ1`, `σ2`, `σ3`, entry by entry.

```lean
lemma sum_smul_pauliMatrix_inr (g : Fin 3 → ℝ) :
    ∑ i, g i • pauliMatrix (Sum.inr i) =
      !![((g 2 : ℝ) : ℂ), ((g 0 : ℝ) : ℂ) - ((g 1 : ℝ) : ℂ) * Complex.I;
        ((g 0 : ℝ) : ℂ) + ((g 1 : ℝ) : ℂ) * Complex.I, ((-g 2 : ℝ) : ℂ)]
```

**`StandardModel.pauliMatrix_inr_star`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L176).

> The Pauli matrices `σ1`, `σ2`, `σ3` are hermitian, phrased through `star`.

```lean
lemma pauliMatrix_inr_star (i : Fin 3) :
    star (pauliMatrix (Sum.inr i)) = pauliMatrix (Sum.inr i)
```

**`StandardModel.pauliMatrix_inr_trace`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L182).

> The Pauli matrices `σ1`, `σ2`, `σ3` are traceless.

```lean
lemma pauliMatrix_inr_trace (i : Fin 3) : (pauliMatrix (Sum.inr i)).trace = 0
```

## B. Coordinates in the Gell-Mann and Pauli bases

> The coordinates of a traceless hermitian matrix in the Gell-Mann and Pauli bases, read
> off from its entries; they coincide with the trace pairings
> `2⁻¹ * (trace (T k * M)).re` with the basis matrices.

**`StandardModel.entry_symm_of_star_eq`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L196).

> The entries of a hermitian matrix are conjugate-symmetric.

```lean
lemma entry_symm_of_star_eq {n : ℕ} {M : Matrix (Fin n) (Fin n) ℂ} (hself : star M = M)
    (i j : Fin n) : M j i = (starRingEnd ℂ) (M i j)
```

**`StandardModel.diag_re_of_star_eq`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L203).

> The diagonal entries of a hermitian matrix are real.

```lean
lemma diag_re_of_star_eq {n : ℕ} {M : Matrix (Fin n) (Fin n) ℂ} (hself : star M = M)
    (i : Fin n) : M i i = ((M i i).re : ℂ)
```

**`StandardModel.gellMannCoeff`**, a def, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L208).

> The coordinates of a matrix in the Gell-Mann basis, read off from its entries.

```lean
def gellMannCoeff (M : Matrix (Fin 3) (Fin 3) ℂ) : Fin 8 → ℝ
```

**`StandardModel.pauliCoeff`**, a def, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L220).

> The coordinates of a matrix in the Pauli basis `σ1`, `σ2`, `σ3`, read off from its
> entries.

```lean
def pauliCoeff (M : Matrix (Fin 2) (Fin 2) ℂ) : Fin 3 → ℝ
```

**`StandardModel.eq_sum_gellMannCoeff_smul`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L227).

> A traceless hermitian `3 × 3` matrix is the combination of the Gell-Mann matrices
> with its `gellMannCoeff` coordinates.

```lean
lemma eq_sum_gellMannCoeff_smul {M : Matrix (Fin 3) (Fin 3) ℂ}
    (hself : star M = M) (htr : M.trace = 0) :
    M = ∑ k, gellMannCoeff M k • gellMannMatrix k
```

**`StandardModel.eq_sum_pauliCoeff_smul`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L294).

> A traceless hermitian `2 × 2` matrix is the combination of the Pauli matrices
> `σ1`, `σ2`, `σ3` with its `pauliCoeff` coordinates.

```lean
lemma eq_sum_pauliCoeff_smul {M : Matrix (Fin 2) (Fin 2) ℂ}
    (hself : star M = M) (htr : M.trace = 0) :
    M = ∑ i, pauliCoeff M i • pauliMatrix (Sum.inr i)
```

**`StandardModel.gellMannCoeff_eq_trace`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L322).

> The Gell-Mann coordinates of a traceless hermitian matrix are its trace pairings
> with the Gell-Mann matrices.

```lean
lemma gellMannCoeff_eq_trace {M : Matrix (Fin 3) (Fin 3) ℂ}
    (hself : star M = M) (htr : M.trace = 0) (k : Fin 8) :
    gellMannCoeff M k = 2⁻¹ * (Matrix.trace (gellMannMatrix k * M)).re
```

**`StandardModel.pauliCoeff_eq_trace`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L395).

> The Pauli coordinates of a traceless hermitian matrix are its trace pairings with
> the Pauli matrices `σ1`, `σ2`, `σ3`.

```lean
lemma pauliCoeff_eq_trace {M : Matrix (Fin 2) (Fin 2) ℂ}
    (hself : star M = M) (htr : M.trace = 0) (i : Fin 3) :
    pauliCoeff M i = 2⁻¹ * (Matrix.trace (pauliMatrix (Sum.inr i) * M)).re
```

## C. The Gell-Mann basis of the su(3) factor

**`StandardModel.GaugeAlgebra.gellMannSU3`**, a def, [line 428](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L428).

> The Gell-Mann matrices as elements of the `su(3)` factor of the gauge algebra.

```lean
def gellMannSU3 (k : Fin 8) :
    ↥(selfAdjoint.submodule ℝ (Matrix (Fin 3) (Fin 3) ℂ) ⊓
      LinearMap.ker (Matrix.traceLinearMap (Fin 3) ℝ ℂ))
```

**`StandardModel.GaugeAlgebra.coe_gellMannSU3`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L434).

```lean
lemma coe_gellMannSU3 (k : Fin 8) :
    (gellMannSU3 k : Matrix (Fin 3) (Fin 3) ℂ) = gellMannMatrix k
```

**`StandardModel.GaugeAlgebra.gellMannSU3_linearIndependent`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L438).

> The Gell-Mann matrices are linearly independent.

```lean
lemma gellMannSU3_linearIndependent : LinearIndependent ℝ gellMannSU3
```

**`StandardModel.GaugeAlgebra.gellMannSU3_span`**, a lemma, [line 461](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L461).

> The Gell-Mann matrices span the `su(3)` factor.

```lean
lemma gellMannSU3_span : ⊤ ≤ Submodule.span ℝ (Set.range gellMannSU3)
```

**`StandardModel.GaugeAlgebra.su3Basis`**, a def, [line 469](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L469).

> The Gell-Mann basis of the `su(3)` factor of the gauge algebra.

```lean
def su3Basis : Basis (Fin 8) ℝ
    ↥(selfAdjoint.submodule ℝ (Matrix (Fin 3) (Fin 3) ℂ) ⊓
      LinearMap.ker (Matrix.traceLinearMap (Fin 3) ℝ ℂ))
```

**`StandardModel.GaugeAlgebra.su3Basis_apply`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L475).

```lean
lemma su3Basis_apply (k : Fin 8) : su3Basis k = gellMannSU3 k
```

## D. The Pauli basis of the su(2) factor

**`StandardModel.GaugeAlgebra.pauliSU2`**, a def, [line 486](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L486).

> The Pauli matrices `σ1`, `σ2`, `σ3` as elements of the `su(2)` factor of the gauge
> algebra.

```lean
def pauliSU2 (i : Fin 3) :
    ↥(selfAdjoint.submodule ℝ (Matrix (Fin 2) (Fin 2) ℂ) ⊓
      LinearMap.ker (Matrix.traceLinearMap (Fin 2) ℝ ℂ))
```

**`StandardModel.GaugeAlgebra.coe_pauliSU2`**, a lemma, [line 492](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L492).

```lean
lemma coe_pauliSU2 (i : Fin 3) :
    (pauliSU2 i : Matrix (Fin 2) (Fin 2) ℂ) = pauliMatrix (Sum.inr i)
```

**`StandardModel.GaugeAlgebra.pauliSU2_linearIndependent`**, a lemma, [line 496](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L496).

> The Pauli matrices `σ1`, `σ2`, `σ3` are linearly independent.

```lean
lemma pauliSU2_linearIndependent : LinearIndependent ℝ pauliSU2
```

**`StandardModel.GaugeAlgebra.pauliSU2_span`**, a lemma, [line 510](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L510).

> The Pauli matrices `σ1`, `σ2`, `σ3` span the `su(2)` factor.

```lean
lemma pauliSU2_span : ⊤ ≤ Submodule.span ℝ (Set.range pauliSU2)
```

**`StandardModel.GaugeAlgebra.su2Basis`**, a def, [line 518](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L518).

> The Pauli basis of the `su(2)` factor of the gauge algebra.

```lean
def su2Basis : Basis (Fin 3) ℝ
    ↥(selfAdjoint.submodule ℝ (Matrix (Fin 2) (Fin 2) ℂ) ⊓
      LinearMap.ker (Matrix.traceLinearMap (Fin 2) ℝ ℂ))
```

**`StandardModel.GaugeAlgebra.su2Basis_apply`**, a lemma, [line 524](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L524).

```lean
lemma su2Basis_apply (i : Fin 3) : su2Basis i = pauliSU2 i
```

## E. The basis of the u(1) factor

**`StandardModel.GaugeAlgebra.u1One`**, a def, [line 535](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L535).

> The unit `1` as the single basis element of the `u(1)` factor of the gauge
> algebra.

```lean
def u1One (_ : Fin 1) : selfAdjoint ℂ
```

**`StandardModel.GaugeAlgebra.coe_u1One`**, a lemma, [line 538](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L538).

```lean
lemma coe_u1One (i : Fin 1) : (u1One i : ℂ) = 1
```

**`StandardModel.GaugeAlgebra.u1One_linearIndependent`**, a lemma, [line 541](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L541).

> The unit is linearly independent.

```lean
lemma u1One_linearIndependent : LinearIndependent ℝ u1One
```

**`StandardModel.GaugeAlgebra.u1One_span`**, a lemma, [line 551](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L551).

> The unit spans the `u(1)` factor.

```lean
lemma u1One_span : ⊤ ≤ Submodule.span ℝ (Set.range u1One)
```

**`StandardModel.GaugeAlgebra.u1Basis`**, a def, [line 558](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L558).

> The basis of the `u(1)` factor of the gauge algebra.

```lean
def u1Basis : Basis (Fin 1) ℝ (selfAdjoint ℂ)
```

**`StandardModel.GaugeAlgebra.u1Basis_apply`**, a lemma, [line 562](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L562).

```lean
lemma u1Basis_apply (i : Fin 1) : u1Basis i = 1
```

## F. The standard basis of the gauge algebra

**`StandardModel.GaugeAlgebra.stdBasis`**, a def, [line 574](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L574).

> The standard basis of the gauge algebra, indexed by `Fin 8 ⊕ Fin 3 ⊕ Fin 1`: the
> eight Gell-Mann matrices on the `su(3)` factor, the three Pauli matrices `σ1`, `σ2`,
> `σ3` on the `su(2)` factor, and `1` on the `u(1)` factor.

```lean
def stdBasis : Basis (Fin 8 ⊕ Fin 3 ⊕ Fin 1) ℝ GaugeAlgebra
```

**`StandardModel.GaugeAlgebra.stdBasis_inl_toSU3Matrix`**, a lemma, [line 578](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L578).

```lean
lemma stdBasis_inl_toSU3Matrix (k : Fin 8) :
    (stdBasis (Sum.inl k)).toSU3Matrix = gellMannMatrix k
```

**`StandardModel.GaugeAlgebra.stdBasis_inl_toSU2Matrix`**, a lemma, [line 583](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L583).

```lean
lemma stdBasis_inl_toSU2Matrix (k : Fin 8) :
    (stdBasis (Sum.inl k)).toSU2Matrix = 0
```

**`StandardModel.GaugeAlgebra.stdBasis_inl_toU1Value`**, a lemma, [line 589](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L589).

```lean
lemma stdBasis_inl_toU1Value (k : Fin 8) :
    (stdBasis (Sum.inl k)).toU1Value = 0
```

**`StandardModel.GaugeAlgebra.stdBasis_inr_inl_toSU3Matrix`**, a lemma, [line 595](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L595).

```lean
lemma stdBasis_inr_inl_toSU3Matrix (i : Fin 3) :
    (stdBasis (Sum.inr (Sum.inl i))).toSU3Matrix = 0
```

**`StandardModel.GaugeAlgebra.stdBasis_inr_inl_toSU2Matrix`**, a lemma, [line 600](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L600).

```lean
lemma stdBasis_inr_inl_toSU2Matrix (i : Fin 3) :
    (stdBasis (Sum.inr (Sum.inl i))).toSU2Matrix = pauliMatrix (Sum.inr i)
```

**`StandardModel.GaugeAlgebra.stdBasis_inr_inl_toU1Value`**, a lemma, [line 606](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L606).

```lean
lemma stdBasis_inr_inl_toU1Value (i : Fin 3) :
    (stdBasis (Sum.inr (Sum.inl i))).toU1Value = 0
```

**`StandardModel.GaugeAlgebra.stdBasis_inr_inr_toSU3Matrix`**, a lemma, [line 612](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L612).

```lean
lemma stdBasis_inr_inr_toSU3Matrix (i : Fin 1) :
    (stdBasis (Sum.inr (Sum.inr i))).toSU3Matrix = 0
```

**`StandardModel.GaugeAlgebra.stdBasis_inr_inr_toSU2Matrix`**, a lemma, [line 617](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L617).

```lean
lemma stdBasis_inr_inr_toSU2Matrix (i : Fin 1) :
    (stdBasis (Sum.inr (Sum.inr i))).toSU2Matrix = 0
```

**`StandardModel.GaugeAlgebra.stdBasis_inr_inr_toU1Value`**, a lemma, [line 623](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L623).

```lean
lemma stdBasis_inr_inr_toU1Value (i : Fin 1) :
    (stdBasis (Sum.inr (Sum.inr i))).toU1Value = 1
```

**`StandardModel.GaugeAlgebra.stdBasis_coord_inr_inr_lie`**, a lemma, [line 630](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L630).

> The hypercharge coordinate vanishes on every bracket: the `u(1)` factor is abelian, so a
> bracket has no `u(1)` component.

```lean
lemma stdBasis_coord_inr_inr_lie (i : Fin 1) (x y : GaugeAlgebra) :
    stdBasis.coord (Sum.inr (Sum.inr i)) ⁅x, y⁆ = 0
```

## G. The adjoint action in the standard basis

> In the standard basis the adjoint action of a gauge group element is the block-diagonal
> matrix `adjointMatrix`: the `su(3)` and `su(2)` blocks pair the basis elements with
> their conjugates through the trace, and the `u(1)` entry is `1`.

**`StandardModel.GaugeAlgebra.toSU3Matrix_sum`**, a lemma, [line 646](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L646).

```lean
lemma toSU3Matrix_sum {ι : Type*} (s : Finset ι) (f : ι → GaugeAlgebra) :
    (∑ x ∈ s, f x).toSU3Matrix = ∑ x ∈ s, (f x).toSU3Matrix
```

**`StandardModel.GaugeAlgebra.toSU2Matrix_sum`**, a lemma, [line 653](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L653).

```lean
lemma toSU2Matrix_sum {ι : Type*} (s : Finset ι) (f : ι → GaugeAlgebra) :
    (∑ x ∈ s, f x).toSU2Matrix = ∑ x ∈ s, (f x).toSU2Matrix
```

**`StandardModel.GaugeAlgebra.toU1Value_sum`**, a lemma, [line 660](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L660).

```lean
lemma toU1Value_sum {ι : Type*} (s : Finset ι) (f : ι → GaugeAlgebra) :
    (∑ x ∈ s, f x).toU1Value = ∑ x ∈ s, (f x).toU1Value
```

**`StandardModel.GaugeAlgebra.adjointMatrix`**, a def, [line 671](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L671).

> The matrix of the adjoint action of a gauge group element in the standard basis:
> block diagonal, with the `su(3)` and `su(2)` blocks the trace pairings
> `2⁻¹ * (trace (T a * g T b g⁻¹)).re` of the basis elements with the conjugated basis
> elements, `1` on the `u(1)` entry, and `0` between different factors.

```lean
noncomputable def adjointMatrix (g : GaugeGroupI) :
    Matrix (Fin 8 ⊕ Fin 3 ⊕ Fin 1) (Fin 8 ⊕ Fin 3 ⊕ Fin 1) ℝ
```

**`StandardModel.GaugeAlgebra.adjointMatrix_inl_inl`**, a lemma, [line 685](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L685).

```lean
lemma adjointMatrix_inl_inl (g : GaugeGroupI) (a b : Fin 8) :
    adjointMatrix g (Sum.inl a) (Sum.inl b)
      = 2⁻¹ * (Matrix.trace (gellMannMatrix a *
          (g.toSU3.1 * gellMannMatrix b * star g.toSU3.1))).re
```

**`StandardModel.GaugeAlgebra.adjointMatrix_inl_inr`**, a lemma, [line 691](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L691).

```lean
lemma adjointMatrix_inl_inr (g : GaugeGroupI) (a : Fin 8) (x : Fin 3 ⊕ Fin 1) :
    adjointMatrix g (Sum.inl a) (Sum.inr x) = 0
```

**`StandardModel.GaugeAlgebra.adjointMatrix_inr_inl`**, a lemma, [line 696](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L696).

```lean
lemma adjointMatrix_inr_inl (g : GaugeGroupI) (x : Fin 3 ⊕ Fin 1) (b : Fin 8) :
    adjointMatrix g (Sum.inr x) (Sum.inl b) = 0
```

**`StandardModel.GaugeAlgebra.adjointMatrix_inr_inl_inr_inl`**, a lemma, [line 701](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L701).

```lean
lemma adjointMatrix_inr_inl_inr_inl (g : GaugeGroupI) (i j : Fin 3) :
    adjointMatrix g (Sum.inr (Sum.inl i)) (Sum.inr (Sum.inl j))
      = 2⁻¹ * (Matrix.trace (pauliMatrix (Sum.inr i) *
          (g.toSU2.1 * pauliMatrix (Sum.inr j) * star g.toSU2.1))).re
```

**`StandardModel.GaugeAlgebra.adjointMatrix_inr_inl_inr_inr`**, a lemma, [line 707](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L707).

```lean
lemma adjointMatrix_inr_inl_inr_inr (g : GaugeGroupI) (i : Fin 3) (u : Fin 1) :
    adjointMatrix g (Sum.inr (Sum.inl i)) (Sum.inr (Sum.inr u)) = 0
```

**`StandardModel.GaugeAlgebra.adjointMatrix_inr_inr_inr_inl`**, a lemma, [line 711](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L711).

```lean
lemma adjointMatrix_inr_inr_inr_inl (g : GaugeGroupI) (u : Fin 1) (j : Fin 3) :
    adjointMatrix g (Sum.inr (Sum.inr u)) (Sum.inr (Sum.inl j)) = 0
```

**`StandardModel.GaugeAlgebra.adjointMatrix_inr_inr_inr_inr`**, a lemma, [line 715](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L715).

```lean
lemma adjointMatrix_inr_inr_inr_inr (g : GaugeGroupI) (u v : Fin 1) :
    adjointMatrix g (Sum.inr (Sum.inr u)) (Sum.inr (Sum.inr v)) = 1
```

**`StandardModel.GaugeAlgebra.adjoint_stdBasis`**, a lemma, [line 720](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L720).

> The adjoint action of the gauge group acts on the standard basis through
> `adjointMatrix`.

```lean
lemma adjoint_stdBasis (g : GaugeGroupI) (b : Fin 8 ⊕ Fin 3 ⊕ Fin 1) :
    adjoint g (stdBasis b) = ∑ a, adjointMatrix g a b • stdBasis a
```

**`StandardModel.GaugeAlgebra.toMatrix_adjoint`**, a lemma, [line 761](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L761).

> The matrix of the adjoint action in the standard basis is `adjointMatrix`.

```lean
lemma toMatrix_adjoint (g : GaugeGroupI) :
    LinearMap.toMatrix stdBasis stdBasis (adjoint g) = adjointMatrix g
```

**`StandardModel.GaugeAlgebra.adjointMatrix_mulVec_repr`**, a lemma, [line 769](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L769).

> The action of `adjointMatrix` on coordinates in the standard basis corresponds to
> the adjoint action of the gauge group on the gauge algebra.

```lean
lemma adjointMatrix_mulVec_repr (g : GaugeGroupI) (a : GaugeAlgebra) :
    (adjointMatrix g).mulVec (stdBasis.repr a) = ⇑(stdBasis.repr (adjoint g a))
```

**`StandardModel.GaugeAlgebra.adjoint_dualMap_coord`**, a lemma, [line 776](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L776).

> The dual adjoint action on the dual standard basis: the coordinate functions
> transform through the rows of `adjointMatrix`.

```lean
lemma adjoint_dualMap_coord (g : GaugeGroupI) (a : Fin 8 ⊕ Fin 3 ⊕ Fin 1) :
    (adjoint g).dualMap (stdBasis.coord a)
      = ∑ b, adjointMatrix g a b • stdBasis.coord b
```

## H. Orthogonality of the adjoint matrix

> The adjoint action preserves the trace pairing of the standard basis, so `adjointMatrix`
> is an orthogonal matrix. Multiplicativity turns the star of a group element into the
> transpose of its matrix, and the two combine to the orthogonality relation.

**`StandardModel.GaugeAlgebra.adjointMatrix_mul`**, a lemma, [line 798](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L798).

> The matrix of the adjoint action turns a product in the gauge group into the
> product of the corresponding matrices.

```lean
lemma adjointMatrix_mul (g h : GaugeGroupI) :
    GaugeAlgebra.adjointMatrix (g * h)
      = GaugeAlgebra.adjointMatrix g * GaugeAlgebra.adjointMatrix h
```

**`StandardModel.GaugeAlgebra.adjointMatrix_one`**, a lemma, [line 805](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L805).

> The matrix of the adjoint action of the identity is the identity matrix.

```lean
lemma adjointMatrix_one : GaugeAlgebra.adjointMatrix (1 : GaugeGroupI) = 1
```

**`StandardModel.GaugeAlgebra.gaugeGroup_mul_star_self`**, a lemma, [line 809](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L809).

> The star of a gauge group element is its inverse.

```lean
lemma gaugeGroup_mul_star_self (g : GaugeGroupI) : g * star g = 1
```

**`StandardModel.GaugeAlgebra.adjointMatrix_star`**, a lemma, [line 818](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L818).

> The matrix of the adjoint action of the star of a gauge group element is the
> transpose of the matrix of the adjoint action, since the trace pairing is symmetric
> under moving the conjugation from one argument to the other.

```lean
lemma adjointMatrix_star (g : GaugeGroupI) :
    GaugeAlgebra.adjointMatrix (star g) = (GaugeAlgebra.adjointMatrix g)ᵀ
```

**`StandardModel.GaugeAlgebra.adjointMatrix_mul_transpose`**, a lemma, [line 845](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L845).

> The matrix of the adjoint action is orthogonal.

```lean
lemma adjointMatrix_mul_transpose (g : GaugeGroupI) :
    GaugeAlgebra.adjointMatrix g * (GaugeAlgebra.adjointMatrix g)ᵀ = 1
```

**`StandardModel.GaugeAlgebra.sum_adjointMatrix_inl_row_mul`**, a lemma, [line 852](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L852).

> The rows of the `su(3)` block of the adjoint matrix are orthonormal. The matrix is
> block diagonal, so orthogonality of the whole matrix restricts to each block.

```lean
lemma sum_adjointMatrix_inl_row_mul (g : GaugeGroupI) (c d : Fin 8) :
    ∑ a : Fin 8, adjointMatrix g (Sum.inl c) (Sum.inl a) *
      adjointMatrix g (Sum.inl d) (Sum.inl a) = if c = d then 1 else 0
```

**`StandardModel.GaugeAlgebra.sum_adjointMatrix_inr_inl_row_mul`**, a lemma, [line 863](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L863).

> The rows of the `su(2)` block of the adjoint matrix are orthonormal.

```lean
lemma sum_adjointMatrix_inr_inl_row_mul (g : GaugeGroupI) (c d : Fin 3) :
    ∑ a : Fin 3, adjointMatrix g (Sum.inr (Sum.inl c)) (Sum.inr (Sum.inl a)) *
      adjointMatrix g (Sum.inr (Sum.inl d)) (Sum.inr (Sum.inl a))
      = if c = d then 1 else 0
```

**`StandardModel.GaugeAlgebra.adjointMatrix_inv_apply`**, a lemma, [line 877](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean#L877).

> The matrix of the adjoint action of the inverse of a gauge group element is the
> transpose of the matrix of the adjoint action.

```lean
lemma adjointMatrix_inv_apply (g : GaugeGroupI) (a b : Fin 8 ⊕ Fin 3 ⊕ Fin 1) :
    adjointMatrix g⁻¹ a b = adjointMatrix g b a
```

## Depends on

- [Physlib.Relativity.PauliMatrices.Basic](../../../../physlib/relativity/paulimatrices/basic.md)
- [The gauge algebra of the Standard Model](../part-03/gaugealgebra-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/Basis.lean)
