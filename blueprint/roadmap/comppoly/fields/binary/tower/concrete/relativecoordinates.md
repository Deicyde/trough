---
catalog: module
lean: ConcreteBinaryTower.Coordinates.coordinates, ConcreteBinaryTower.Coordinates.coordinates_eq_natCoordinatesConstOfLE, ConcreteBinaryTower.Coordinates.pack, ConcreteBinaryTower.Coordinates.coordinates_pack, ConcreteBinaryTower.Coordinates.pack_coordinates, ConcreteBinaryTower.Coordinates.coordinates_self, ConcreteBinaryTower.Coordinates.pack_self, ConcreteBinaryTower.Coordinates.coordinates_add, ConcreteBinaryTower.Coordinates.pack_add, ConcreteBinaryTower.Coordinates.coordinates_smul, ConcreteBinaryTower.Coordinates.pack_smul, ConcreteBinaryTower.Coordinates.coordinates_eq_setWidth_ushiftRight, ConcreteBinaryTower.Coordinates.toBitVec_coordinates, ConcreteBinaryTower.Coordinates.getLsbD_coordinates, ConcreteBinaryTower.Coordinates.toNat_coordinates
statement: formalized
proof: formalized
---

# Relative coordinates for concrete binary tower fields

`CompPoly.Fields.Binary.Tower.Concrete.RelativeCoordinates`, in [CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean), by Chung Thai Nguyen, Quang Dao.

> `ConcreteBinaryTower.Coordinates.coordinates h` identifies level `j` with
> `2 ^ (j - i)` coefficients in level `i`, for `h : i ≤ j`. The scalar action is induced by
> the existing concrete tower embedding. Coordinate `q` is the block of `2 ^ i` bits starting
> at bit `2 ^ i * q`; blocks and bits within each block retain their numeric order.
>
> The equivalence composes `succCoordinates` through `AlgebraTower.natCoordinatesConstOfLE`.
> Its inverse `pack` reconstructs the original word. The readback theorems relate the algebraic
> coordinates to bitvector slicing and natural-number bit blocks. They refer to raw stored words,
> which differ from field numerals in characteristic two.
>
> The coefficient ordering follows the relative multilinear basis of [DP23], §2.3:
> earlier tower generators correspond to lower index bits.
>
> ## References
>
> * [Diamond, B. E. and Posen, J., *Succinct arguments over towers of binary fields*][DP23]

`ConcreteBinaryTower.Coordinates.coordinates` (definition, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean#L40))

> Coordinates of level `j` over level `i`, ordered by increasing bit-block offset, for the
> scalar action induced by the concrete tower embedding associated with `h`.

```lean
def coordinates {i j : ℕ} (h : i ≤ j) :
    letI := ConcreteBTFieldAlgebra h
    ConcreteBTField j ≃ₗ[ConcreteBTField i] (Fin (2 ^ (j - i)) → ConcreteBTField i)
```

`ConcreteBinaryTower.Coordinates.coordinates_eq_natCoordinatesConstOfLE` (theorem, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean#L47))

> The relative equivalence is the constant-two composition of the low-first successor
> coordinate equivalences, with the scalar action induced by the concrete tower embedding.

```lean
theorem coordinates_eq_natCoordinatesConstOfLE {i j : ℕ} (h : i ≤ j) :
    coordinates h = natCoordinatesConstOfLE succCoordinates h
```

`ConcreteBinaryTower.Coordinates.pack` (definition, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean#L53))

> Construct a level-`j` word from level-`i` coefficients, with coefficient `q` occupying
> the block of `2 ^ i` bits starting at bit `2 ^ i * q`.

```lean
def pack {i j : ℕ} (h : i ≤ j) (c : Fin (2 ^ (j - i)) → ConcreteBTField i) :
    ConcreteBTField j
```

`ConcreteBinaryTower.Coordinates.coordinates_pack` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean#L57))

> Reading the coordinates of a packed word recovers every input coefficient.

```lean
theorem coordinates_pack {i j : ℕ} (h : i ≤ j)
    (c : Fin (2 ^ (j - i)) → ConcreteBTField i) : coordinates h (pack h c) = c
```

`ConcreteBinaryTower.Coordinates.pack_coordinates` (theorem, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean#L62))

> Packing all coordinates recovers the original word.

```lean
theorem pack_coordinates {i j : ℕ} (h : i ≤ j) (x : ConcreteBTField j) :
    pack h (coordinates h x) = x
```

`ConcreteBinaryTower.Coordinates.coordinates_self` (theorem, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean#L66))

> At equal endpoints the single coordinate is the original word.

```lean
theorem coordinates_self (i : ℕ) (h : i ≤ i) (x : ConcreteBTField i)
    (q : Fin (2 ^ (i - i))) : coordinates h x q = x
```

`ConcreteBinaryTower.Coordinates.pack_self` (theorem, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean#L71))

> Packing at equal endpoints returns the single coefficient.

```lean
theorem pack_self (i : ℕ) (h : i ≤ i) (c : Fin (2 ^ (i - i)) → ConcreteBTField i) :
    pack h c = c 0
```

`ConcreteBinaryTower.Coordinates.coordinates_add` (theorem, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean#L76))

> Coordinates preserve the canonical field addition, coefficient by coefficient.

```lean
theorem coordinates_add {i j : ℕ} (h : i ≤ j) (x y : ConcreteBTField j) :
    coordinates h (x + y) = coordinates h x + coordinates h y
```

`ConcreteBinaryTower.Coordinates.pack_add` (theorem, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean#L81))

> Packing preserves coefficientwise canonical field addition.

```lean
theorem pack_add {i j : ℕ} (h : i ≤ j)
    (c d : Fin (2 ^ (j - i)) → ConcreteBTField i) :
    pack h (c + d) = pack h c + pack h d
```

`ConcreteBinaryTower.Coordinates.coordinates_smul` (theorem, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean#L86))

> The tower embedding's scalar action multiplies each coordinate by the lower-level scalar.

```lean
theorem coordinates_smul {i j : ℕ} (h : i ≤ j) (a : ConcreteBTField i)
    (x : ConcreteBTField j) (q : Fin (2 ^ (j - i))) :
    letI := ConcreteBTFieldAlgebra h
    coordinates h (a • x) q = a * coordinates h x q
```

`ConcreteBinaryTower.Coordinates.pack_smul` (theorem, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean#L93))

> Scaling all coefficients commutes with packing under the tower embedding's scalar action.

```lean
theorem pack_smul {i j : ℕ} (h : i ≤ j) (a : ConcreteBTField i)
    (c : Fin (2 ^ (j - i)) → ConcreteBTField i) :
    letI := ConcreteBTFieldAlgebra h
    pack h (fun q => a * c q) = a • pack h c
```

`ConcreteBinaryTower.Coordinates.coordinates_eq_setWidth_ushiftRight` (theorem, [line 211](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean#L211))

> Coordinate `q` is the raw bit block of width `2 ^ i` starting at bit `2 ^ i * q`.

```lean
theorem coordinates_eq_setWidth_ushiftRight {i j : ℕ} (h : i ≤ j) (x : ConcreteBTField j)
    (q : Fin (2 ^ (j - i))) :
    coordinates h x q =
      ConcreteBTField.ofBitVec
        ((BitVec.ushiftRight x.toBitVec (2 ^ i * q.val)).setWidth (2 ^ i))
```

`ConcreteBinaryTower.Coordinates.toBitVec_coordinates` (theorem, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean#L227))

> Encoding coordinate `q` returns the corresponding low-first bit block of the input word.

```lean
theorem toBitVec_coordinates {i j : ℕ} (h : i ≤ j) (x : ConcreteBTField j)
    (q : Fin (2 ^ (j - i))) :
    (coordinates h x q).toBitVec =
      (BitVec.ushiftRight x.toBitVec (2 ^ i * q.val)).setWidth (2 ^ i)
```

`ConcreteBinaryTower.Coordinates.getLsbD_coordinates` (theorem, [line 235](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean#L235))

> Reading bit `b` within coordinate `q` reads the bit at offset `2 ^ i * q + b`
> in the original word. The bound keeps `b` inside the coefficient's bit width.

```lean
theorem getLsbD_coordinates {i j : ℕ} (h : i ≤ j) (x : ConcreteBTField j)
    (q : Fin (2 ^ (j - i))) (b : ℕ) (hb : b < 2 ^ i) :
    (coordinates h x q).toBitVec.getLsbD b = x.toBitVec.getLsbD (2 ^ i * q.val + b)
```

`ConcreteBinaryTower.Coordinates.toNat_coordinates` (theorem, [line 244](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean#L244))

> The stored natural word of coordinate `q` is the block of `2 ^ i` bits starting at
> bit `2 ^ i * q` in the original word.

```lean
theorem toNat_coordinates {i j : ℕ} (h : i ≤ j) (x : ConcreteBTField j)
    (q : Fin (2 ^ (j - i))) :
    (coordinates h x q).toNat =
      Nat.getMiddleBits (2 ^ i * q.val) (2 ^ i) x.toNat
```

## Depends on

- [Bit operations on natural numbers](../../../../data/nat/bitwise.md)
- [Coordinates along a natural-number-indexed algebra tower](../../../../data/ringtheory/algebratower-2/coordinates.md)
- [Successor coordinates for concrete binary tower fields](coordinates.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/RelativeCoordinates.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Concrete.RelativeCoordinates.json)
