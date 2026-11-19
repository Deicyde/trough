---
catalog: module
lean: ConcreteBinaryTower.Coordinates.multilinearBasis_repr, ConcreteBinaryTower.Coordinates.coordinates_multilinearBasis, ConcreteBinaryTower.Coordinates.pack_single_eq_multilinearBasis, ConcreteBinaryTower.Coordinates.pack_eq_sum_multilinearBasis
statement: formalized
proof: formalized
---

# Existing multilinear basis and concrete coordinates

`CompPoly.Fields.Binary.Tower.Concrete.BasisCoordinates`, in [CompPoly/Fields/Binary/Tower/Concrete/BasisCoordinates.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/BasisCoordinates.lean), by Chung Thai Nguyen, Quang Dao.

> The representation of `ConcreteBinaryTower.multilinearBasis` agrees at each numeric index
> with `ConcreteBinaryTower.Coordinates.coordinates`. Consequently, packing a unit coefficient
> vector computes the existing basis vector, and packing arbitrary coefficients is their linear
> combination under the concrete tower embedding.
>
> The proof compares the existing basis's generator-product formula with the successor-vector
> law in `AlgebraTower.natBasisVector_succ`. Both use low-first coordinate order: earlier tower
> generators correspond to lower index bits. An auxiliary basis constructed with
> `Module.Basis.ofEquivFun` is private to the identification proof.
>
> The generator-product basis and its ordering are those of [DP23], §2.3, with the
> paper's generator `X_k` represented by `Z (k + 1)`.
>
> ## References
>
> * [Diamond, B. E. and Posen, J., *Succinct arguments over towers of binary fields*][DP23]

`ConcreteBinaryTower.Coordinates.multilinearBasis_repr` (theorem, [line 162](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/BasisCoordinates.lean#L162))

> The coefficient at numeric index `q` in the multilinear basis is the executable coordinate
> at the same index, for the scalar action induced by the concrete tower embedding.

```lean
theorem multilinearBasis_repr {i j : ℕ} (h : i ≤ j) (x : ConcreteBTField j)
    (q : Fin (2 ^ (j - i))) :
    let := ConcreteBTFieldAlgebra h
    (multilinearBasis i j h).repr x q = coordinates h x q
```

`ConcreteBinaryTower.Coordinates.coordinates_multilinearBasis` (theorem, [line 171](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/BasisCoordinates.lean#L171))

> The multilinear basis vector at numeric index `q` has coordinate one at `q`
> and coordinate zero at every other index.

```lean
theorem coordinates_multilinearBasis {i j : ℕ} (h : i ≤ j)
    (q : Fin (2 ^ (j - i))) :
    coordinates h (multilinearBasis i j h q) = Pi.single q 1
```

`ConcreteBinaryTower.Coordinates.pack_single_eq_multilinearBasis` (theorem, [line 181](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/BasisCoordinates.lean#L181))

> Packing a unit coefficient vector computes the multilinear basis vector at the same
> numeric index.

```lean
theorem pack_single_eq_multilinearBasis {i j : ℕ} (h : i ≤ j)
    (q : Fin (2 ^ (j - i))) :
    pack h (Pi.single q 1) = multilinearBasis i j h q
```

`ConcreteBinaryTower.Coordinates.pack_eq_sum_multilinearBasis` (theorem, [line 188](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/BasisCoordinates.lean#L188))

> Packing is the sum of the multilinear basis vectors multiplied by their
> coefficients embedded from level `i` into level `j` through the concrete tower map.

```lean
theorem pack_eq_sum_multilinearBasis {i j : ℕ} (h : i ≤ j)
    (c : Fin (2 ^ (j - i)) → ConcreteBTField i) :
    pack h c = ∑ q, concreteTowerAlgebraMap i j h (c q) * multilinearBasis i j h q
```

## Depends on

- [Concrete Binary Tower Basis](basis.md)
- [Relative coordinates for concrete binary tower fields](relativecoordinates.md)

## Proof depends on

- [Bases from adjacent tower coordinates](../../../../data/ringtheory/algebratower-2/basis.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Concrete/BasisCoordinates.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/BasisCoordinates.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Concrete.BasisCoordinates.json)
