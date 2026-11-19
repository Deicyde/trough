---
catalog: module
lean: ConcreteBinaryTower.Coordinates.low, ConcreteBinaryTower.Coordinates.high, ConcreteBinaryTower.Coordinates.joinSucc, ConcreteBinaryTower.Coordinates.low_joinSucc, ConcreteBinaryTower.Coordinates.high_joinSucc, ConcreteBinaryTower.Coordinates.joinSucc_low_high, ConcreteBinaryTower.Coordinates.low_add, ConcreteBinaryTower.Coordinates.high_add, ConcreteBinaryTower.Coordinates.joinSucc_eq_map_mul_add, ConcreteBinaryTower.Coordinates.smul_joinSucc, ConcreteBinaryTower.Coordinates.low_smul, ConcreteBinaryTower.Coordinates.high_smul, ConcreteBinaryTower.Coordinates.succCoordinates, ConcreteBinaryTower.Coordinates.succCoordinates_apply, ConcreteBinaryTower.Coordinates.succCoordinates_symm_apply
statement: formalized
proof: formalized
---

# Successor coordinates for concrete binary tower fields

`CompPoly.Fields.Binary.Tower.Concrete.Coordinates`, in [CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean), by Chung Thai Nguyen, Quang Dao.

> `ConcreteBinaryTower.Coordinates.succCoordinates k` identifies level `k + 1` with two
> coefficients in level `k`, ordered as the constant coefficient followed by the coefficient
> of the new generator `Z (k + 1)`. Its scalar action is induced by the existing tower map
> from level `k` to level `k + 1`.
>
> The underlying `split` and `join` functions use high/low order. The executable `low`, `high`,
> and `joinSucc` adapters expose low/high order and their bodies for direct word reduction.
> The linear equivalence is characterized by its application and inverse-application lemmas.
> The decomposition and linearity proofs use the existing algebraic expansion lemmas in
> `CompPoly.Fields.Binary.Tower.Concrete.Algebra`.
>
> These successor equivalences can be passed to `AlgebraTower.natCoordinatesOfLE` from
> `CompPoly.Data.RingTheory.AlgebraTower.Coordinates` to obtain coordinates between any ordered
> pair of levels.
>
> The tower and constant-first successor expansion are described in [DP23], §2.3.
> The paper's generator `X_k` corresponds to `Z (k + 1)` here.
>
> ## References
>
> * [Diamond, B. E. and Posen, J., *Succinct arguments over towers of binary fields*][DP23]

`ConcreteBinaryTower.Coordinates.low` (definition, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean#L41))

> The constant coefficient of a level-`k + 1` word, stored in its low `2 ^ k` bits.

```lean
def low (k : ℕ) (x : ConcreteBTField (k + 1)) : ConcreteBTField k
```

`ConcreteBinaryTower.Coordinates.high` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean#L45))

> The coefficient of `Z (k + 1)`, stored in the high `2 ^ k` bits of the word.

```lean
def high (k : ℕ) (x : ConcreteBTField (k + 1)) : ConcreteBTField k
```

`ConcreteBinaryTower.Coordinates.joinSucc` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean#L49))

> Construct a level-`k + 1` word with constant coefficient `lo` and generator coefficient `hi`.

```lean
def joinSucc (k : ℕ) (lo hi : ConcreteBTField k) : ConcreteBTField (k + 1)
```

`ConcreteBinaryTower.Coordinates.low_joinSucc` (theorem, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean#L53))

> Reading the low coefficient after joining recovers it.

```lean
theorem low_joinSucc (k : ℕ) (lo hi : ConcreteBTField k) :
    low k (joinSucc k lo hi) = lo
```

`ConcreteBinaryTower.Coordinates.high_joinSucc` (theorem, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean#L58))

> Reading the high coefficient after joining recovers it.

```lean
theorem high_joinSucc (k : ℕ) (lo hi : ConcreteBTField k) :
    high k (joinSucc k lo hi) = hi
```

`ConcreteBinaryTower.Coordinates.joinSucc_low_high` (theorem, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean#L63))

> Joining the two coefficients recovers the original word.

```lean
theorem joinSucc_low_high (k : ℕ) (x : ConcreteBTField (k + 1)) :
    joinSucc k (low k x) (high k x) = x
```

`ConcreteBinaryTower.Coordinates.low_add` (theorem, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean#L68))

> The low coefficient preserves the canonical field addition.

```lean
theorem low_add (k : ℕ) (x y : ConcreteBTField (k + 1)) :
    low k (x + y) = low k x + low k y
```

`ConcreteBinaryTower.Coordinates.high_add` (theorem, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean#L74))

> The high coefficient preserves the canonical field addition.

```lean
theorem high_add (k : ℕ) (x y : ConcreteBTField (k + 1)) :
    high k (x + y) = high k x + high k y
```

`ConcreteBinaryTower.Coordinates.joinSucc_eq_map_mul_add` (theorem, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean#L80))

> A joined word is the sum of its embedded constant and generator terms.

```lean
theorem joinSucc_eq_map_mul_add (k : ℕ) (lo hi : ConcreteBTField k) :
    joinSucc k lo hi =
      concreteTowerAlgebraMap k (k + 1) (Nat.le_succ k) hi * Z (k + 1) +
        concreteTowerAlgebraMap k (k + 1) (Nat.le_succ k) lo
```

`ConcreteBinaryTower.Coordinates.smul_joinSucc` (theorem, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean#L88))

> The action induced by the tower embedding multiplies both coefficients by the scalar.

```lean
theorem smul_joinSucc (k : ℕ) (a lo hi : ConcreteBTField k) :
    letI := ConcreteBTFieldAlgebra (Nat.le_succ k)
    a • joinSucc k lo hi = joinSucc k (a * lo) (a * hi)
```

`ConcreteBinaryTower.Coordinates.low_smul` (theorem, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean#L96))

> The constant coefficient commutes with the scalar action induced by the tower embedding.

```lean
theorem low_smul (k : ℕ) (a : ConcreteBTField k) (x : ConcreteBTField (k + 1)) :
    letI := ConcreteBTFieldAlgebra (Nat.le_succ k)
    low k (a • x) = a * low k x
```

`ConcreteBinaryTower.Coordinates.high_smul` (theorem, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean#L103))

> The generator coefficient commutes with the scalar action induced by the tower embedding.

```lean
theorem high_smul (k : ℕ) (a : ConcreteBTField k) (x : ConcreteBTField (k + 1)) :
    letI := ConcreteBTFieldAlgebra (Nat.le_succ k)
    high k (a • x) = a * high k x
```

`ConcreteBinaryTower.Coordinates.succCoordinates` (definition, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean#L111))

> Coordinates `(constant coefficient, generator coefficient)` for the scalar action
> induced by the tower embedding from level `k` to level `k + 1`.

```lean
def succCoordinates (k : ℕ) :
    letI := ConcreteBTFieldAlgebra (Nat.le_succ k)
    ConcreteBTField (k + 1) ≃ₗ[ConcreteBTField k] (Fin 2 → ConcreteBTField k)
```

`ConcreteBinaryTower.Coordinates.succCoordinates_apply` (theorem, [line 136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean#L136))

> The forward function is exactly low/high readback, in that order.

```lean
theorem succCoordinates_apply (k : ℕ) (x : ConcreteBTField (k + 1)) :
    succCoordinates k x = ![low k x, high k x]
```

`ConcreteBinaryTower.Coordinates.succCoordinates_symm_apply` (theorem, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean#L142))

> The inverse constructs a word with constant coefficient `c 0` and generator coefficient
> `c 1`.

```lean
theorem succCoordinates_symm_apply (k : ℕ) (c : Fin 2 → ConcreteBTField k) :
    (succCoordinates k).symm c = joinSucc k (c 0) (c 1)
```

## Depends on

- [Concrete Binary Tower Algebra](algebra.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Coordinates.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Concrete.Coordinates.json)
