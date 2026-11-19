---
catalog: module
lean: ConcreteBinaryTower.Coordinates.joinSucc_mul_joinSucc, ConcreteBinaryTower.Coordinates.low_mul, ConcreteBinaryTower.Coordinates.high_mul, ConcreteBinaryTower.Coordinates.conjugate, ConcreteBinaryTower.Coordinates.norm, ConcreteBinaryTower.Coordinates.conjugate_eq_joinSucc, ConcreteBinaryTower.Coordinates.norm_eq, ConcreteBinaryTower.Coordinates.mul_conjugate, ConcreteBinaryTower.Coordinates.conjugate_conjugate, ConcreteBinaryTower.Coordinates.norm_ne_zero, ConcreteBinaryTower.Coordinates.inv_eq_joinSucc
statement: formalized
proof: formalized
---

# Quadratic arithmetic in concrete successor coordinates

`CompPoly.Fields.Binary.Tower.Concrete.CoordinateArithmetic`, in [CompPoly/Fields/Binary/Tower/Concrete/CoordinateArithmetic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/CoordinateArithmetic.lean), by CompPoly Contributors.

> At level `k + 1`, write an element as `lo + hi * Z (k + 1)` using the chosen embedding
> from level `k`. The relation
> `Z (k + 1) ^ 2 = 1 + canonicalAlgMap k (Z k) * Z (k + 1)` gives multiplication,
> conjugation and norm formulas over the predecessor field. The inverse formula is total,
> including zero, and describes the canonical concrete inverse with its existing fast paths.
>
> These are concrete coordinate contracts for the tower described in [DP23], §2.3.
> They use the existing predecessor-field proofs without importing the abstract tower bridge.
>
> ## References
>
> * [Diamond, B. E. and Posen, J., *Succinct arguments over towers of binary fields*][DP23]

`ConcreteBinaryTower.Coordinates.joinSucc_mul_joinSucc` (theorem, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/CoordinateArithmetic.lean#L33))

> Multiplication in constant-first successor coordinates follows the quadratic relation
> with linear coefficient `Z k` and constant coefficient one.

```lean
theorem joinSucc_mul_joinSucc (k : ℕ) (a₀ a₁ b₀ b₁ : ConcreteBTField k) :
    joinSucc k a₀ a₁ * joinSucc k b₀ b₁ =
      joinSucc k (a₀ * b₀ + a₁ * b₁)
        (a₀ * b₁ + b₀ * a₁ + (a₁ * b₁) * Z k)
```

`ConcreteBinaryTower.Coordinates.low_mul` (theorem, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/CoordinateArithmetic.lean#L43))

> The constant coefficient of a product is the sum of the two diagonal products.

```lean
theorem low_mul (k : ℕ) (x y : ConcreteBTField (k + 1)) :
    low k (x * y) = low k x * low k y + high k x * high k y
```

`ConcreteBinaryTower.Coordinates.high_mul` (theorem, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/CoordinateArithmetic.lean#L49))

> The generator coefficient of a product includes the quadratic linear-coefficient term.

```lean
theorem high_mul (k : ℕ) (x y : ConcreteBTField (k + 1)) :
    high k (x * y) = low k x * high k y + low k y * high k x +
      (high k x * high k y) * Z k
```

`ConcreteBinaryTower.Coordinates.conjugate` (definition, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/CoordinateArithmetic.lean#L56))

> Quadratic conjugation replaces the generator by itself plus the embedded `Z k`.

```lean
def conjugate (k : ℕ) (x : ConcreteBTField (k + 1)) : ConcreteBTField (k + 1)
```

`ConcreteBinaryTower.Coordinates.norm` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/CoordinateArithmetic.lean#L60))

> The predecessor-field norm in low/high coordinates.

```lean
def norm (k : ℕ) (x : ConcreteBTField (k + 1)) : ConcreteBTField k
```

`ConcreteBinaryTower.Coordinates.conjugate_eq_joinSucc` (theorem, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/CoordinateArithmetic.lean#L64))

> The conjugate keeps the high coefficient and adds `high * Z k` to the low coefficient.

```lean
theorem conjugate_eq_joinSucc (k : ℕ) (x : ConcreteBTField (k + 1)) :
    conjugate k x = joinSucc k (low k x + high k x * Z k) (high k x)
```

`ConcreteBinaryTower.Coordinates.norm_eq` (theorem, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/CoordinateArithmetic.lean#L68))

> The norm is `lo * (lo + hi * Z k) + hi * hi` in the predecessor field.

```lean
theorem norm_eq (k : ℕ) (x : ConcreteBTField (k + 1)) :
    norm k x = low k x * (low k x + high k x * Z k) + high k x * high k x
```

`ConcreteBinaryTower.Coordinates.mul_conjugate` (theorem, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/CoordinateArithmetic.lean#L72))

> Multiplication by the quadratic conjugate is the embedded predecessor-field norm.

```lean
theorem mul_conjugate (k : ℕ) (x : ConcreteBTField (k + 1)) :
    x * conjugate k x = canonicalAlgMap k (norm k x)
```

`ConcreteBinaryTower.Coordinates.conjugate_conjugate` (theorem, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/CoordinateArithmetic.lean#L86))

> Conjugating twice recovers the original successor-field element.

```lean
theorem conjugate_conjugate (k : ℕ) (x : ConcreteBTField (k + 1)) :
    conjugate k (conjugate k x) = x
```

`ConcreteBinaryTower.Coordinates.norm_ne_zero` (theorem, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/CoordinateArithmetic.lean#L92))

> A nonzero successor-field element has nonzero predecessor-field norm.

```lean
theorem norm_ne_zero (k : ℕ) (x : ConcreteBTField (k + 1)) (hx : x ≠ 0) :
    norm k x ≠ 0
```

`ConcreteBinaryTower.Coordinates.inv_eq_joinSucc` (theorem, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/CoordinateArithmetic.lean#L97))

> The canonical inverse has conjugate coordinates divided by the norm, including at zero.

```lean
theorem inv_eq_joinSucc (k : ℕ) (x : ConcreteBTField (k + 1)) :
    x⁻¹ = joinSucc k ((norm k x)⁻¹ * (low k x + high k x * Z k))
      ((norm k x)⁻¹ * high k x)
```

## Depends on

- [Successor coordinates for concrete binary tower fields](coordinates.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Concrete/CoordinateArithmetic.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/CoordinateArithmetic.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Concrete.CoordinateArithmetic.json)
