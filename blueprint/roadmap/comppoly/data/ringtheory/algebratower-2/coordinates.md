---
catalog: module
lean: AlgebraTower.coordinateSize, AlgebraTower.coordinateSize_zero, AlgebraTower.coordinateSize_succ, AlgebraTower.coordinateSize_const, AlgebraTower.natCoordinates, AlgebraTower.natCoordinates_zero, AlgebraTower.natCoordinates_succ, AlgebraTower.natPack, AlgebraTower.natPack_zero, AlgebraTower.natPack_succ, AlgebraTower.natCoordinates_natPack, AlgebraTower.natPack_natCoordinates, AlgebraTower.natBasisVector, AlgebraTower.natCoordinates_natBasisVector, AlgebraTower.natCoordinatesOfLE, AlgebraTower.natCoordinatesOfLE_apply, AlgebraTower.natCoordinatesOfLE_self, AlgebraTower.natPackOfLE, AlgebraTower.natPackOfLE_eq_natPack, AlgebraTower.natPackOfLE_self, AlgebraTower.natCoordinatesOfLE_natPackOfLE, AlgebraTower.natPackOfLE_natCoordinatesOfLE, AlgebraTower.natBasisVectorOfLE, AlgebraTower.natBasisVectorOfLE_eq_natBasisVector, AlgebraTower.natCoordinatesOfLE_natBasisVectorOfLE, AlgebraTower.natBasisVectorOfLE_self, AlgebraTower.natCoordinatesConstOfLE, AlgebraTower.natCoordinatesConstOfLE_apply, AlgebraTower.natCoordinatesConstOfLE_self
statement: formalized
proof: formalized
---

# Coordinates along a natural-number-indexed algebra tower

`CompPoly.Data.RingTheory.AlgebraTower.Coordinates`, in [CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean), by CompPoly Contributors.

> Given linear coordinate equivalences between adjacent levels of an `AlgebraTower`,
> `AlgebraTower.natCoordinates` gives coordinates at level `i + n` over level `i`. Each scalar
> action is induced by the corresponding map of the given tower. The number of successor
> coordinates may vary with the level, and may be zero when such an equivalence exists.
>
> The old coordinate index varies fastest: a pair `(newIndex, oldIndex)` has flattened index
> `oldIndex + oldSize * newIndex`. Constant successor coordinate count two gives the usual
> least-significant-bit-first order.
>
> `AlgebraTower.natPack` is the inverse coordinate map. `AlgebraTower.natBasisVector` packs
> a unit coordinate vector. Both are executable, with no enumeration of the tower carriers.
> The corresponding mathematical basis is constructed in
> `CompPoly.Data.RingTheory.AlgebraTower.Basis`.
>
> For arbitrary endpoints `h : i ≤ j`, `AlgebraTower.natCoordinatesOfLE` and its packing
> and vector companions accept elements of `A j` directly. `AlgebraTower.natCoordinatesConstOfLE`
> also presents constant successor coordinate count `r` as `Fin (r ^ (j - i))`.
>
> The construction uses `LinearEquiv.restrictScalars`, `LinearEquiv.piCongrRight`,
> `LinearEquiv.curry`, and `finProdFinEquiv`. Endpoint and coordinate-count identifications use
> `LinearEquiv.cast`, `LinearEquiv.funCongrLeft`, and `finCongr`.

`AlgebraTower.coordinateSize` (abbreviation, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L54))

> The number of coordinates from level `i` through `n` steps with chosen coordinate counts `d`.
> The next step contributes a new outer block of coordinates.

```lean
abbrev coordinateSize (d : ℕ → ℕ) (i n : ℕ) : ℕ
```

`AlgebraTower.coordinateSize_zero` (theorem, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L59))

> An interval with no successor steps has one coordinate.

```lean
theorem coordinateSize_zero (d : ℕ → ℕ) (i : ℕ) : coordinateSize d i 0 = 1
```

`AlgebraTower.coordinateSize_succ` (theorem, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L63))

> The number of coordinates is multiplied by the next successor coordinate count.

```lean
theorem coordinateSize_succ (d : ℕ → ℕ) (i n : ℕ) :
    coordinateSize d i (n + 1) = d (i + n) * coordinateSize d i n
```

`AlgebraTower.coordinateSize_const` (theorem, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L67))

> A constant successor coordinate count `r` gives `r ^ n` coordinates over `n` steps.

```lean
theorem coordinateSize_const (r i n : ℕ) :
    coordinateSize (fun _ => r) i n = r ^ n
```

`AlgebraTower.natCoordinates` (definition, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L82))

> Coordinates of `A (i + n)` over `A i`, obtained by composing adjacent equivalences.
>
> The scalar action is induced by the given tower map from `i` to `i + n`. At each step,
> the old index varies fastest, so `(b, j)` is placed at `j + oldSize * b`.

```lean
def natCoordinates (i : ℕ) : (n : ℕ) →
    letI := t.toAlgebra (Nat.le_add_right i n)
    A (i + n) ≃ₗ[A i] (Fin (coordinateSize d i n) → A i)
```

`AlgebraTower.natCoordinates_zero` (theorem, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L116))

> At height zero the single coordinate is the original element.

```lean
theorem natCoordinates_zero (i : ℕ) (x : A i) (j : Fin (coordinateSize d i 0)) :
    natCoordinates step i 0 x j = x
```

`AlgebraTower.natCoordinates_succ` (theorem, [line 122](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L122))

> Read the new outer coordinate, then the old inner coordinate.
> Division selects the outer block and remainder selects the position within that block.

```lean
theorem natCoordinates_succ (i n : ℕ) (x : A (i + (n + 1)))
    (j : Fin (coordinateSize d i (n + 1))) :
    natCoordinates step i (n + 1) x j =
      natCoordinates step i n (step (i + n) x j.divNat) j.modNat
```

`AlgebraTower.natPack` (definition, [line 129](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L129))

> Pack coordinates in the order used by `natCoordinates`, using the inverse successor maps.

```lean
def natPack (i n : ℕ) (c : Fin (coordinateSize d i n) → A i) : A (i + n)
```

`AlgebraTower.natPack_zero` (theorem, [line 134](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L134))

> At height zero packing returns the single input coefficient.

```lean
theorem natPack_zero (i : ℕ) (c : Fin (coordinateSize d i 0) → A i) :
    natPack step i 0 c = c ⟨0, by simp only [coordinateSize_zero]; decide⟩
```

`AlgebraTower.natPack_succ` (theorem, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L139))

> Pack each old coordinate block, then apply the inverse of the next successor map.

```lean
theorem natPack_succ (i n : ℕ) (c : Fin (coordinateSize d i (n + 1)) → A i) :
    natPack step i (n + 1) c =
      (step (i + n)).symm
        (fun b => natPack step i n (fun j => c (finProdFinEquiv (b, j))))
```

`AlgebraTower.natCoordinates_natPack` (theorem, [line 147](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L147))

> Reading back packed coordinates recovers the input coefficients.

```lean
theorem natCoordinates_natPack (i n : ℕ) (c : Fin (coordinateSize d i n) → A i) :
    natCoordinates step i n (natPack step i n c) = c
```

`AlgebraTower.natPack_natCoordinates` (theorem, [line 153](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L153))

> Packing the coordinates of an element recovers that element.

```lean
theorem natPack_natCoordinates (i n : ℕ) (x : A (i + n)) :
    natPack step i n (natCoordinates step i n x) = x
```

`AlgebraTower.natBasisVector` (definition, [line 158](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L158))

> The executable vector whose coordinate at `j` is one and whose other coordinates are zero.

```lean
def natBasisVector (i n : ℕ) (j : Fin (coordinateSize d i n)) : A (i + n)
```

`AlgebraTower.natCoordinates_natBasisVector` (theorem, [line 163](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L163))

> A basis vector reads back as its unit coordinate vector.

```lean
theorem natCoordinates_natBasisVector (i n : ℕ) (j : Fin (coordinateSize d i n)) :
    natCoordinates step i n (natBasisVector step i n j) = Pi.single j 1
```

`AlgebraTower.natCoordinatesOfLE` (definition, [line 176](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L176))

> Coordinates of `A j` over `A i` for comparable endpoints, with the given tower action.
> The coordinate count and order are those of the `j - i` successor steps starting at `i`.

```lean
def natCoordinatesOfLE {i j : ℕ} (h : i ≤ j) :
    letI := t.toAlgebra h
    A j ≃ₗ[A i] (Fin (coordinateSize d i (j - i)) → A i)
```

`AlgebraTower.natCoordinatesOfLE_apply` (theorem, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L190))

> Endpoint coordinates are height coordinates after identifying `j` with `i + (j - i)`.
> The coordinate index is unchanged.

```lean
theorem natCoordinatesOfLE_apply {i j : ℕ} (h : i ≤ j) (x : A j)
    (idx : Fin (coordinateSize d i (j - i))) :
    natCoordinatesOfLE step h x idx =
      natCoordinates step i (j - i) (cast (congrArg A (Nat.add_sub_of_le h).symm) x) idx
```

`AlgebraTower.natCoordinatesOfLE_self` (theorem, [line 198](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L198))

> With equal endpoints the single coordinate is the original element.

```lean
theorem natCoordinatesOfLE_self (i : ℕ) (x : A i)
    (idx : Fin (coordinateSize d i (i - i))) :
    natCoordinatesOfLE step (Nat.le_refl i) x idx = x
```

`AlgebraTower.natPackOfLE` (definition, [line 205](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L205))

> Pack coordinates into `A j`, inverting the coordinate map over the given tower action.

```lean
def natPackOfLE {i j : ℕ} (h : i ≤ j) (c : Fin (coordinateSize d i (j - i)) → A i) : A j
```

`AlgebraTower.natPackOfLE_eq_natPack` (theorem, [line 209](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L209))

> Endpoint packing is height packing followed by the identification `i + (j - i) = j`.

```lean
theorem natPackOfLE_eq_natPack {i j : ℕ} (h : i ≤ j)
    (c : Fin (coordinateSize d i (j - i)) → A i) :
    natPackOfLE step h c = cast (congrArg A (Nat.add_sub_of_le h)) (natPack step i (j - i) c)
```

`AlgebraTower.natPackOfLE_self` (theorem, [line 216](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L216))

> Packing at equal endpoints returns the single coefficient.

```lean
theorem natPackOfLE_self (i : ℕ) (c : Fin (coordinateSize d i (i - i)) → A i) :
    natPackOfLE step (Nat.le_refl i) c =
      c ⟨0, by simp only [Nat.sub_self, coordinateSize_zero]; decide⟩
```

`AlgebraTower.natCoordinatesOfLE_natPackOfLE` (theorem, [line 224](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L224))

> Reading packed endpoint coordinates recovers the input coefficients.

```lean
theorem natCoordinatesOfLE_natPackOfLE {i j : ℕ} (h : i ≤ j)
    (c : Fin (coordinateSize d i (j - i)) → A i) :
    natCoordinatesOfLE step h (natPackOfLE step h c) = c
```

`AlgebraTower.natPackOfLE_natCoordinatesOfLE` (theorem, [line 231](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L231))

> Packing the endpoint coordinates of an element recovers that element.

```lean
theorem natPackOfLE_natCoordinatesOfLE {i j : ℕ} (h : i ≤ j) (x : A j) :
    natPackOfLE step h (natCoordinatesOfLE step h x) = x
```

`AlgebraTower.natBasisVectorOfLE` (definition, [line 236](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L236))

> The executable endpoint vector with coordinate one at `idx` and zero elsewhere.

```lean
def natBasisVectorOfLE {i j : ℕ} (h : i ≤ j) (idx : Fin (coordinateSize d i (j - i))) : A j
```

`AlgebraTower.natBasisVectorOfLE_eq_natBasisVector` (theorem, [line 240](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L240))

> Endpoint vectors agree with height vectors under the canonical endpoint identification.

```lean
theorem natBasisVectorOfLE_eq_natBasisVector {i j : ℕ} (h : i ≤ j)
    (idx : Fin (coordinateSize d i (j - i))) :
    natBasisVectorOfLE step h idx =
      cast (congrArg A (Nat.add_sub_of_le h)) (natBasisVector step i (j - i) idx)
```

`AlgebraTower.natCoordinatesOfLE_natBasisVectorOfLE` (theorem, [line 248](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L248))

> An endpoint vector reads back as its unit coordinate vector.

```lean
theorem natCoordinatesOfLE_natBasisVectorOfLE {i j : ℕ} (h : i ≤ j)
    (idx : Fin (coordinateSize d i (j - i))) :
    natCoordinatesOfLE step h (natBasisVectorOfLE step h idx) = Pi.single idx 1
```

`AlgebraTower.natBasisVectorOfLE_self` (theorem, [line 255](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L255))

> At equal endpoints the unique executable basis vector is one.

```lean
theorem natBasisVectorOfLE_self (i : ℕ) (idx : Fin (coordinateSize d i (i - i))) :
    natBasisVectorOfLE step (Nat.le_refl i) idx = 1
```

`AlgebraTower.natCoordinatesConstOfLE` (definition, [line 271](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L271))

> Endpoint coordinates with constant successor coordinate count `r`, indexed by `Fin (r^(j-i))`.
> Only the coordinate count is identified with a power; each index retains its numeric value.

```lean
def natCoordinatesConstOfLE {i j : ℕ} (h : i ≤ j) :
    letI := t.toAlgebra h
    A j ≃ₗ[A i] (Fin (r ^ (j - i)) → A i)
```

`AlgebraTower.natCoordinatesConstOfLE_apply` (theorem, [line 280](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L280))

> Constant-count coordinates read the same numeric index in the endpoint coordinate map.

```lean
theorem natCoordinatesConstOfLE_apply {i j : ℕ} (h : i ≤ j) (x : A j)
    (idx : Fin (r ^ (j - i))) :
    natCoordinatesConstOfLE constantStep h x idx =
      natCoordinatesOfLE constantStep h x
        (Fin.cast (coordinateSize_const r i (j - i)).symm idx)
```

`AlgebraTower.natCoordinatesConstOfLE_self` (theorem, [line 289](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean#L289))

> Constant-count coordinates at equal endpoints consist of the original element.

```lean
theorem natCoordinatesConstOfLE_self (i : ℕ) (x : A i) (idx : Fin (r ^ (i - i))) :
    natCoordinatesConstOfLE constantStep (Nat.le_refl i) x idx = x
```

## Depends on

- [Towers of algebras and their equivalences](../algebratower.md)

## Sources

- [CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower/Coordinates.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Data.RingTheory.AlgebraTower.Coordinates.json)
