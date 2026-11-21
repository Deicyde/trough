---
catalog: module
lean: AlgebraTower.natBasis, AlgebraTower.natBasis_repr, AlgebraTower.natBasisVector_eq_natBasis, AlgebraTower.natBasis_succ, AlgebraTower.natBasisVector_succ, AlgebraTower.natBasisOfLE, AlgebraTower.natBasisOfLE_repr, AlgebraTower.natBasisVectorOfLE_eq_natBasisOfLE, AlgebraTower.natBasisOfLE_apply, AlgebraTower.natBasisOfLE_self
statement: formalized
proof: formalized
---

# Bases from adjacent tower coordinates

`CompPoly.Data.RingTheory.AlgebraTower.Basis`, in [CompPoly/Data/RingTheory/AlgebraTower/Basis.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Basis.lean), by CompPoly Contributors.

> `AlgebraTower.natBasis` is the basis determined by the executable equivalence
> `AlgebraTower.natCoordinates`. Its `repr` is the coordinate map, and its vectors equal the
> executable `AlgebraTower.natBasisVector` values.
>
> `AlgebraTower.natBasisOfLE` provides the same basis at arbitrary endpoints `i ≤ j`,
> with vectors in `A j` and coefficients in `A i`. Its representation agrees with
> `AlgebraTower.natCoordinatesOfLE`, and `AlgebraTower.natBasisVectorOfLE` computes its vectors.
>
> The successor basis agrees with `Module.Basis.smulTower'`, reindexed by `finProdFinEquiv`.
> The old coordinate index varies fastest. Each vector is the embedded old basis vector
> multiplied by the corresponding new successor basis vector. No normalization of that
> successor vector is assumed.
>
> The construction uses `Module.Basis.ofEquivFun` and the scalar-tower basis equations from
> Mathlib's `Mathlib.RingTheory.AlgebraTower` module.

`AlgebraTower.natBasis` (definition, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Basis.lean#L42))

> The basis whose coordinates are `natCoordinates`, over the action of the given tower map.

```lean
noncomputable def natBasis (i n : ℕ) :
    letI := t.toAlgebra (Nat.le_add_right i n)
    Module.Basis (Fin (coordinateSize d i n)) (A i) (A (i + n))
```

`AlgebraTower.natBasis_repr` (theorem, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Basis.lean#L50))

> The mathematical basis representation is the executable coordinate map.

```lean
theorem natBasis_repr (i n : ℕ) (x : A (i + n)) (j : Fin (coordinateSize d i n)) :
    letI := t.toAlgebra (Nat.le_add_right i n)
    (natBasis step i n).repr x j = natCoordinates step i n x j
```

`AlgebraTower.natBasisVector_eq_natBasis` (theorem, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Basis.lean#L56))

> Packing a unit coordinate vector gives the corresponding mathematical basis vector.

```lean
theorem natBasisVector_eq_natBasis (i n : ℕ) (j : Fin (coordinateSize d i n)) :
    natBasisVector step i n j = natBasis step i n j
```

`AlgebraTower.natBasis_succ` (theorem, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Basis.lean#L67))

> The next relative basis is the scalar-tower composition of the previous basis and the
> next successor basis, with the old index varying fastest.

```lean
theorem natBasis_succ (i n : ℕ) :
    letI := t.toAlgebra (Nat.le_add_right i n)
    letI := t.toAlgebra (Nat.le_succ (i + n))
    letI := t.toAlgebra (Nat.le_add_right i (n + 1))
    letI := toIsScalarTower t (Nat.le_add_right i n) (Nat.le_succ (i + n))
    natBasis step i (n + 1) =
      ((natBasis step i n).smulTower' (Module.Basis.ofEquivFun (step (i + n)))).reindex
        finProdFinEquiv
```

`AlgebraTower.natBasisVector_succ` (theorem, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Basis.lean#L85))

> At flattened index `oldIndex + oldSize * newIndex`, the vector is the embedded old
> vector multiplied by the new successor vector.

```lean
theorem natBasisVector_succ (i n : ℕ) (b : Fin (d (i + n)))
    (j : Fin (coordinateSize d i n)) :
    natBasisVector step i (n + 1) (finProdFinEquiv (b, j)) =
      t.algebraMap (i + n) (i + n + 1) (Nat.le_succ (i + n)) (natBasisVector step i n j) *
        (step (i + n)).symm (Pi.single b 1)
```

`AlgebraTower.natBasisOfLE` (definition, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Basis.lean#L100))

> The basis at arbitrary comparable endpoints, over the action of the given tower map.

```lean
noncomputable def natBasisOfLE {i j : ℕ} (h : i ≤ j) :
    letI := t.toAlgebra h
    Module.Basis (Fin (coordinateSize d i (j - i))) (A i) (A j)
```

`AlgebraTower.natBasisOfLE_repr` (theorem, [line 108](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Basis.lean#L108))

> The endpoint basis representation is the executable endpoint coordinate map.

```lean
theorem natBasisOfLE_repr {i j : ℕ} (h : i ≤ j) (x : A j)
    (idx : Fin (coordinateSize d i (j - i))) :
    letI := t.toAlgebra h
    (natBasisOfLE step h).repr x idx = natCoordinatesOfLE step h x idx
```

`AlgebraTower.natBasisVectorOfLE_eq_natBasisOfLE` (theorem, [line 115](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Basis.lean#L115))

> Packing a unit coordinate vector computes the corresponding endpoint basis vector.

```lean
theorem natBasisVectorOfLE_eq_natBasisOfLE {i j : ℕ} (h : i ≤ j)
    (idx : Fin (coordinateSize d i (j - i))) :
    natBasisVectorOfLE step h idx = natBasisOfLE step h idx
```

`AlgebraTower.natBasisOfLE_apply` (theorem, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Basis.lean#L126))

> Endpoint basis vectors agree with the height-indexed basis after identifying the endpoints.

```lean
theorem natBasisOfLE_apply {i j : ℕ} (h : i ≤ j)
    (idx : Fin (coordinateSize d i (j - i))) :
    natBasisOfLE step h idx =
      cast (congrArg A (Nat.add_sub_of_le h)) (natBasis step i (j - i) idx)
```

`AlgebraTower.natBasisOfLE_self` (theorem, [line 135](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Basis.lean#L135))

> At equal endpoints the unique basis vector is one.

```lean
theorem natBasisOfLE_self (i : ℕ) (idx : Fin (coordinateSize d i (i - i))) :
    natBasisOfLE step (Nat.le_refl i) idx = 1
```

## Depends on

- [Coordinates along a natural-number-indexed algebra tower](coordinates.md)

## Sources

- [CompPoly/Data/RingTheory/AlgebraTower/Basis.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Basis.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Data.RingTheory.AlgebraTower.Basis.json)
