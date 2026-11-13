---
declaration: module
origin: cited
lean: CStarMatrix.kron, CStarMatrix.kron_apply, CStarMatrix.kron_add_left, CStarMatrix.kron_add_right, CStarMatrix.kron_smul_left, CStarMatrix.kron_smul_right, CStarMatrix.kron_zero_left, CStarMatrix.kron_zero_right
statement: formalized
proof: formalized
---

# Matrices over a C⋆-algebra as a composite system

The module `PhyslibAlpha.ProbabilisticTheory.CStarAlgebra.MatrixComposite`, [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean): 41 declarations, 19 with a docstring.

> Matrices over a C⋆-algebra as composite observables with an n-level ancilla, and positivity.

## i. Overview

> Coupling a quantum system with observables `A` to an `n`-level ancilla gives the `n × n` matrices
> over `A`. The self-adjoint ones are the composite observables of the self-adjoint part of `A` with
> the `n × n` Hermitian matrices: the product `a ⊗ h` is the matrix `(hᵢⱼ a)`. The positive
> matrices form a cone of composite observables that contains every product of positive observables
> and is Archimedean. When `A` is commutative, every positive matrix is also in the maximal cone:
> applying a character entrywise turns it into a positive scalar matrix.
>
> Applying a map entrywise to matrices is tensoring it with the identity of the ancilla. So complete
> positivity of a map, in the sense of positive matrices, is the complete positivity of composite
> systems, and for maps out of commutative C⋆-algebras it follows from classicality.

## ii. Key results

> - `CStarMatrix.kron` : the matrix `(hᵢⱼ a)`.
> - `CStarMatrix.toMatrix` : the matrix of a composite observable.
> - `CStarMatrix.kron_nonneg` : products of positive observables are positive matrices.
> - `CStarMatrix.matrixCone` : the positive matrices, as a cone of composite observables.
> - `CStarMatrix.isArchimedeanTensorCone_matrixCone` : this cone is Archimedean.
> - `CStarMatrix.exists_toMatrix_eq` : every self-adjoint matrix is a composite observable.
> - `CStarMatrix.mem_maxTensorCone_of_nonneg` : for commutative `A`, positive matrices are in the
>   maximal cone.

## iv. References

> * None.

## A. The matrix of a composite observable

**`CStarMatrix.kron`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L69).

> The matrix `(hᵢⱼ a)`: the observable `a` tensored with the scalar matrix `h`.

```lean
def kron (h : CStarMatrix n n ℂ) (a : A) : CStarMatrix n n A
```

**`CStarMatrix.kron_apply`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L73).

```lean
lemma kron_apply (h : CStarMatrix n n ℂ) (a : A) (i j : n) : kron h a i j = h i j • a
```

**`CStarMatrix.kron_add_left`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L75).

```lean
lemma kron_add_left (h h' : CStarMatrix n n ℂ) (a : A) : kron (h + h') a = kron h a + kron h' a
```

**`CStarMatrix.kron_add_right`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L78).

```lean
lemma kron_add_right (h : CStarMatrix n n ℂ) (a a' : A) : kron h (a + a') = kron h a + kron h a'
```

**`CStarMatrix.kron_smul_left`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L81).

```lean
lemma kron_smul_left (r : ℝ) (h : CStarMatrix n n ℂ) (a : A) : kron (r • h) a = r • kron h a
```

**`CStarMatrix.kron_smul_right`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L84).

```lean
lemma kron_smul_right (r : ℝ) (h : CStarMatrix n n ℂ) (a : A) : kron h (r • a) = r • kron h a
```

**`CStarMatrix.kron_zero_left`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L87).

```lean
lemma kron_zero_left (a : A) : kron (0 : CStarMatrix n n ℂ) a = 0
```

**`CStarMatrix.kron_zero_right`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L90).

```lean
lemma kron_zero_right (h : CStarMatrix n n ℂ) : kron h (0 : A) = 0
```

**`CStarMatrix.map_add'`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L93).

```lean
lemma map_add' {B : Type*} [AddCommMonoid B] (M N : CStarMatrix n n A) (f : A →+ B) :
    (M + N).map f = M.map f + N.map f
```

**`CStarMatrix.star_kron_mul_kron`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L100).

> `kron g b` has adjoint-square `kron (g⋆ g) (b⋆ b)`.

```lean
lemma star_kron_mul_kron (g : CStarMatrix n n ℂ) (b : A) :
    star (kron g b) * kron g b = kron (star g * g) (star b * b)
```

**`CStarMatrix.sum_apply`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L106).

```lean
lemma sum_apply {ι : Type*} (s : Finset ι) (f : ι → CStarMatrix n n A) (i j : n) :
    (∑ k ∈ s, f k) i j = ∑ k ∈ s, f k i j
```

**`CStarMatrix.toMatrix`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L115).

> The matrix of a composite observable of the self-adjoint part of `A` with the `n × n`
> Hermitian matrices.

```lean
noncomputable def toMatrix :
    Composite (selfAdjoint A) (selfAdjoint (CStarMatrix n n ℂ)) →ₗ[ℝ] CStarMatrix n n A
```

**`CStarMatrix.toMatrix_tmul`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L126).

```lean
lemma toMatrix_tmul (a : selfAdjoint A) (h : selfAdjoint (CStarMatrix n n ℂ)) :
    toMatrix n A (Composite.tmul a h) = kron (h : CStarMatrix n n ℂ) (a : A)
```

**`CStarMatrix.toMatrix_one_tmul_one`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L129).

```lean
lemma toMatrix_one_tmul_one :
    toMatrix n A (Composite.tmul (1 : selfAdjoint A) (1 : selfAdjoint (CStarMatrix n n ℂ))) = 1
```

**`CStarMatrix.isSelfAdjoint_kron`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L137).

```lean
lemma isSelfAdjoint_kron {h : CStarMatrix n n ℂ} {a : A} (hh : IsSelfAdjoint h)
    (ha : IsSelfAdjoint a) : IsSelfAdjoint (kron h a)
```

**`CStarMatrix.isSelfAdjoint_toMatrix`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L143).

```lean
lemma isSelfAdjoint_toMatrix (z : Composite (selfAdjoint A) (selfAdjoint (CStarMatrix n n ℂ))) :
    IsSelfAdjoint (toMatrix n A z)
```

## B. Positive matrices

**`CStarMatrix.kron_nonneg`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L154).

> **Products of positive observables are positive matrices.** Both factors are sums of
> adjoint-squares, and `kron` of adjoint-squares is an adjoint-square.

```lean
lemma kron_nonneg {h : CStarMatrix n n ℂ} {a : A} (hh : 0 ≤ h) (ha : 0 ≤ a) : 0 ≤ kron h a
```

**`CStarMatrix.matrixCone`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L170).

> The positive matrices, as a cone of composite observables.

```lean
noncomputable def matrixCone :
    PointedCone ℝ (Composite (selfAdjoint A) (selfAdjoint (CStarMatrix n n ℂ)))
```

**`CStarMatrix.mem_matrixCone`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L181).

```lean
lemma mem_matrixCone {z : Composite (selfAdjoint A) (selfAdjoint (CStarMatrix n n ℂ))} :
    z ∈ matrixCone n A ↔ 0 ≤ toMatrix n A z
```

**`CStarMatrix.minTensorCone_le_matrixCone`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L185).

> The positive matrices contain every product of positive observables.

```lean
lemma minTensorCone_le_matrixCone :
    minTensorCone (selfAdjoint A) (selfAdjoint (CStarMatrix n n ℂ)) ≤ matrixCone n A
```

**`CStarMatrix.isArchimedeanTensorCone_matrixCone`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L193).

> **The positive matrices form an Archimedean cone.**

```lean
lemma isArchimedeanTensorCone_matrixCone :
    IsArchimedeanTensorCone (E := selfAdjoint A) (F := selfAdjoint (CStarMatrix n n ℂ))
      (matrixCone n A)
```

## C. Every self-adjoint matrix is a composite observable

**`CStarMatrix.unit`**, a def, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L208).

> The matrix unit `eᵢⱼ`.

```lean
def unit (i j : n) : CStarMatrix n n ℂ
```

**`CStarMatrix.unit_apply`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L211).

```lean
lemma unit_apply (i j p q : n) : unit i j p q = if i = p ∧ j = q then 1 else 0
```

**`CStarMatrix.star_unit`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L215).

```lean
lemma star_unit (i j : n) : star (unit i j) = unit j i
```

**`CStarMatrix.symUnit`**, a def, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L221).

> The Hermitian matrix `(eᵢⱼ + eⱼᵢ) / 2`.

```lean
noncomputable def symUnit (i j : n) : selfAdjoint (CStarMatrix n n ℂ)
```

**`CStarMatrix.asymUnit`**, a def, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L227).

> The Hermitian matrix `i (eᵢⱼ - eⱼᵢ) / 2`.

```lean
noncomputable def asymUnit (i j : n) : selfAdjoint (CStarMatrix n n ℂ)
```

**`CStarMatrix.entry`**, a def, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L234).

> The entry of a matrix, as a function of the matrix.

```lean
def entry (M : CStarMatrix n n A) (i j : n) : A
```

**`CStarMatrix.ofMatrixSA`**, a def, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L237).

> The composite observable whose matrix is `M`.

```lean
noncomputable def ofMatrixSA (M : CStarMatrix n n A) :
    Composite (selfAdjoint A) (selfAdjoint (CStarMatrix n n ℂ))
```

**`CStarMatrix.kron_symUnit_apply`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L243).

```lean
lemma kron_symUnit_apply (i j p q : n) (a : A) :
    kron (symUnit i j : CStarMatrix n n ℂ) a p q =
      (2 : ℝ)⁻¹ • ((if i = p ∧ j = q then a else 0) + (if j = p ∧ i = q then a else 0))
```

**`CStarMatrix.kron_asymUnit_apply`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L252).

```lean
lemma kron_asymUnit_apply (i j p q : n) (a : A) :
    kron (asymUnit i j : CStarMatrix n n ℂ) a p q =
      (Complex.I / 2) • ((if i = p ∧ j = q then a else 0) - (if j = p ∧ i = q then a else 0))
```

**`CStarMatrix.toMatrix_ofMatrixSA`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L260).

```lean
lemma toMatrix_ofMatrixSA (M : CStarMatrix n n A) :
    toMatrix n A (ofMatrixSA M) = ∑ i, ∑ j,
      (kron (symUnit i j : CStarMatrix n n ℂ) (realPart (entry M i j) : A) +
        kron (asymUnit i j : CStarMatrix n n ℂ) (imaginaryPart (entry M i j) : A))
```

**`CStarMatrix.toMatrix_ofMatrixSA_apply`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L270).

```lean
lemma toMatrix_ofMatrixSA_apply (M : CStarMatrix n n A) (p q : n) :
    toMatrix n A (ofMatrixSA M) p q =
      (2 : ℝ)⁻¹ • ((realPart (entry M p q) : A) + realPart (entry M q p)) +
        (Complex.I / 2) • ((imaginaryPart (entry M p q) : A) - imaginaryPart (entry M q p))
```

**`CStarMatrix.exists_toMatrix_eq`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L280).

> **Every self-adjoint matrix over `A` is a composite observable.**

```lean
lemma exists_toMatrix_eq {M : CStarMatrix n n A} (hM : IsSelfAdjoint M) :
    ∃ z, toMatrix n A z = M
```

## D. Commutative algebras

**`CStarMatrix.characterFunctional`**, a def, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L298).

> A character of `C`, as a positive functional on its observables.

```lean
noncomputable def characterFunctional (χ : WeakDual.characterSpace ℂ C) : selfAdjoint C →ₚ[ℝ] ℝ
```

**`CStarMatrix.coe_characterFunctional`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L301).

```lean
lemma coe_characterFunctional (χ : WeakDual.characterSpace ℂ C) (x : selfAdjoint C) :
    (characterFunctional χ x : ℂ) = χ (x : C)
```

**`CStarMatrix.coe_lslice_characterFunctional`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L306).

> Measuring the first factor with a character is applying the character entrywise.

```lean
lemma coe_lslice_characterFunctional (χ : WeakDual.characterSpace ℂ C)
    (z : Composite (selfAdjoint C) (selfAdjoint (CStarMatrix n n ℂ))) :
    ((PositiveLinearMap.lslice (characterFunctional χ) z : selfAdjoint (CStarMatrix n n ℂ)) :
      CStarMatrix n n ℂ) = (toMatrix n C z).map χ
```

**`CStarMatrix.mem_maxTensorCone_of_nonneg`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L324).

> **For commutative `C`, positive matrices are in the maximal cone.** Measuring the ancilla with a
> positive functional leaves an observable of `C` on which every character is nonnegative, because
> applying a character entrywise keeps a matrix positive.

```lean
lemma mem_maxTensorCone_of_nonneg {z : Composite (selfAdjoint C) (selfAdjoint (CStarMatrix n n ℂ))}
    (hz : 0 ≤ toMatrix n C z) :
    z ∈ maxTensorCone (selfAdjoint C) (selfAdjoint (CStarMatrix n n ℂ))
```

## E. Applying a map entrywise

**`CStarMatrix.toMatrix_map`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L348).

> Applying a positive unital map to the first factor of a composite observable is applying it
> entrywise to its matrix.

```lean
lemma toMatrix_map (f : A →ₚ₁[ℂ] B)
    (z : Composite (selfAdjoint A) (selfAdjoint (CStarMatrix n n ℂ))) :
    toMatrix n B (TensorProduct.map
      (f.restrictSA : Channel (selfAdjoint A) (selfAdjoint B)).toLinearMap LinearMap.id z) =
      (toMatrix n A z).map f
```

## F. Channels out of commutative algebras

**`ProbabilisticTheory.QuantumChannel.map_nonneg_of_commutative`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L383).

> Entrywise, a positive unital map out of a commutative C⋆-algebra keeps positive matrices
> positive: the input is classical, so the map is completely positive.

```lean
lemma map_nonneg_of_commutative (f : C →ₚ₁[ℂ] B) {k : ℕ} {M : CStarMatrix (Fin k) (Fin k) C}
    (hM : 0 ≤ M) : 0 ≤ M.map f
```

**`ProbabilisticTheory.QuantumChannel.ofCommutative`**, a def, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L399).

> **Stinespring's theorem.** A positive unital map out of a commutative C⋆-algebra is a quantum
> channel: it is automatically completely positive.

```lean
noncomputable def ofCommutative (f : C →ₚ₁[ℂ] B) : QuantumChannel C B
```

**`ProbabilisticTheory.QuantumChannel.ofCommutative_apply`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean#L405).

```lean
lemma ofCommutative_apply (f : C →ₚ₁[ℂ] B) (x : C) : ofCommutative f x = f x
```

## Depends on

- [Composite systems](../composite/tensorcone.md)
- [Commutative C⋆-algebras are classical](commutative.md)
- [Quantum channels](quantumchannel.md)

## Proof depends on

- [Complete positivity of classical channels](../composite/completepositivity.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/MatrixComposite.lean)
