---
catalog: module
lean: CompPoly.Bytes.toListLE, CompPoly.Bytes.ofListLE, CompPoly.Bytes.toListLE_zero, CompPoly.Bytes.toListLE_succ, CompPoly.Bytes.ofListLE_nil, CompPoly.Bytes.ofListLE_cons, CompPoly.Bytes.length_toListLE, CompPoly.Bytes.ofListLE_toListLE, CompPoly.Bytes.ofListLE_toListLE_of_lt, CompPoly.Bytes.ofListLE_lt, CompPoly.Bytes.toListLE_ofListLE, CompPoly.Bytes.toListLE_inj_of_lt, CompPoly.Bytes.ofListLE_append, CompPoly.Bytes.bytesFor, CompPoly.Bytes.bytesFor_pos, CompPoly.Bytes.le_pow_bytesFor, CompPoly.Bytes.bytesFor_two_pow, CompPoly.Bytes.toVecLE, CompPoly.Bytes.ofVecLE, CompPoly.Bytes.toList_toVecLE, CompPoly.Bytes.ofVecLE_toVecLE, CompPoly.Bytes.ofVecLE_toVecLE_of_lt, CompPoly.Bytes.ofVecLE_lt, CompPoly.Bytes.toVecLE_ofVecLE, CompPoly.Bytes.toVecLE_inj_of_lt, CompPoly.Bytes.toByteArrayLE, CompPoly.Bytes.ofByteArrayLE, CompPoly.Bytes.size_toByteArrayLE, CompPoly.Bytes.data_toByteArrayLE, CompPoly.Bytes.ofByteArrayLE_toByteArrayLE, CompPoly.Bytes.ofByteArrayLE_toByteArrayLE_of_lt, CompPoly.Bytes.toByteArrayLE_inj_of_lt
statement: formalized
proof: formalized
---

# Little-endian byte encodings of naturals

`CompPoly.Data.Bytes.LittleEndian`, in [CompPoly/Data/Bytes/LittleEndian.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean), by Derek Sorensen.

> The one encoder every fixed-width serialization in CompPoly is built from: a natural number
> becomes exactly `w` bytes, least significant first, and `w` bytes become a natural.
>
> * `toListLE w n` / `ofListLE` on `List UInt8`, with the round-trip laws
>   `ofListLE_toListLE` (as `n % 256 ^ w`, hence exact below `256 ^ w`) and
>   `toListLE_ofListLE`, and the concatenation law `ofListLE_append`.
> * `toVecLE` / `ofVecLE` and `toByteArrayLE` / `ofByteArrayLE`, the same maps on `Vector UInt8 w`
>   and `ByteArray`.
> * `bytesFor bound`, the number of bytes needed to hold every natural below `bound`, with
>   `le_pow_bytesFor : bound ≤ 256 ^ bytesFor bound`. It is `Nat.log2`-based so that the kernel
>   evaluates it on numerals by `decide`.
>
> The layout is the one arkworks and plonky3 use for field elements: the canonical integer,
> little-endian, padded to a fixed width.

> ## Lists

`CompPoly.Bytes.toListLE` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L38))

> The `w` little-endian bytes of `n`; bits above `8 * w` are dropped.

```lean
def toListLE : ℕ → ℕ → List UInt8
```

`CompPoly.Bytes.ofListLE` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L43))

> The natural with the given little-endian bytes.

```lean
def ofListLE : List UInt8 → ℕ
```

`CompPoly.Bytes.toListLE_zero` (theorem, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L47))

```lean
theorem toListLE_zero (n : ℕ) : toListLE 0 n = []
```

`CompPoly.Bytes.toListLE_succ` (theorem, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L49))

```lean
theorem toListLE_succ (w n : ℕ) :
    toListLE (w + 1) n = UInt8.ofNat (n % 256) :: toListLE w (n / 256)
```

`CompPoly.Bytes.ofListLE_nil` (theorem, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L52))

```lean
theorem ofListLE_nil : ofListLE [] = 0
```

`CompPoly.Bytes.ofListLE_cons` (theorem, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L54))

```lean
theorem ofListLE_cons (b : UInt8) (bs : List UInt8) :
    ofListLE (b :: bs) = b.toNat + 256 * ofListLE bs
```

`CompPoly.Bytes.length_toListLE` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L57))

```lean
theorem length_toListLE (w n : ℕ) : (toListLE w n).length = w
```

`CompPoly.Bytes.ofListLE_toListLE` (theorem, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L62))

```lean
theorem ofListLE_toListLE (w n : ℕ) : ofListLE (toListLE w n) = n % 256 ^ w
```

`CompPoly.Bytes.ofListLE_toListLE_of_lt` (theorem, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L70))

```lean
theorem ofListLE_toListLE_of_lt {w n : ℕ} (h : n < 256 ^ w) : ofListLE (toListLE w n) = n
```

`CompPoly.Bytes.ofListLE_lt` (theorem, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L73))

```lean
theorem ofListLE_lt (l : List UInt8) : ofListLE l < 256 ^ l.length
```

`CompPoly.Bytes.toListLE_ofListLE` (theorem, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L81))

```lean
theorem toListLE_ofListLE (l : List UInt8) : toListLE l.length (ofListLE l) = l
```

`CompPoly.Bytes.toListLE_inj_of_lt` (theorem, [line 91](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L91))

```lean
theorem toListLE_inj_of_lt {w n m : ℕ} (hn : n < 256 ^ w) (hm : m < 256 ^ w)
    (h : toListLE w n = toListLE w m) : n = m
```

`CompPoly.Bytes.ofListLE_append` (theorem, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L96))

```lean
theorem ofListLE_append (l₁ l₂ : List UInt8) :
    ofListLE (l₁ ++ l₂) = ofListLE l₁ + 256 ^ l₁.length * ofListLE l₂
```

> ## Widths

`CompPoly.Bytes.bytesFor` (definition, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L109))

> The number of bytes needed to hold every natural below `bound`: one byte for `bound ≤ 256`,
> and in general the least `w` with `bound ≤ 256 ^ w`, except that `bound ≤ 1` still takes one
> byte. Defined through `Nat.log2` so that the kernel evaluates it on numerals.

```lean
def bytesFor (bound : ℕ) : ℕ
```

`CompPoly.Bytes.bytesFor_pos` (theorem, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L111))

```lean
theorem bytesFor_pos (bound : ℕ) : 0 < bytesFor bound
```

`CompPoly.Bytes.le_pow_bytesFor` (theorem, [line 115](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L115))

```lean
theorem le_pow_bytesFor (bound : ℕ) : bound ≤ 256 ^ bytesFor bound
```

`CompPoly.Bytes.bytesFor_two_pow` (theorem, [line 134](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L134))

> The width of a power of two: `k` bits need `⌈k / 8⌉` bytes. Stated so that a bit-pattern
> type's width is a small numeral computation rather than a kernel evaluation of `2 ^ k`.

```lean
theorem bytesFor_two_pow {k : ℕ} (hk : 0 < k) : bytesFor (2 ^ k) = (k + 7) / 8
```

> ## Vectors

`CompPoly.Bytes.toVecLE` (definition, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L155))

> The `w` little-endian bytes of `n` as a vector.

```lean
def toVecLE (w n : ℕ) : Vector UInt8 w
```

`CompPoly.Bytes.ofVecLE` (definition, [line 159](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L159))

> The natural with the given little-endian bytes.

```lean
def ofVecLE {w : ℕ} (v : Vector UInt8 w) : ℕ
```

`CompPoly.Bytes.toList_toVecLE` (theorem, [line 161](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L161))

```lean
theorem toList_toVecLE (w n : ℕ) : (toVecLE w n).toList = toListLE w n
```

`CompPoly.Bytes.ofVecLE_toVecLE` (theorem, [line 163](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L163))

```lean
theorem ofVecLE_toVecLE (w n : ℕ) : ofVecLE (toVecLE w n) = n % 256 ^ w
```

`CompPoly.Bytes.ofVecLE_toVecLE_of_lt` (theorem, [line 166](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L166))

```lean
theorem ofVecLE_toVecLE_of_lt {w n : ℕ} (h : n < 256 ^ w) : ofVecLE (toVecLE w n) = n
```

`CompPoly.Bytes.ofVecLE_lt` (theorem, [line 169](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L169))

```lean
theorem ofVecLE_lt {w : ℕ} (v : Vector UInt8 w) : ofVecLE v < 256 ^ w
```

`CompPoly.Bytes.toVecLE_ofVecLE` (theorem, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L173))

```lean
theorem toVecLE_ofVecLE {w : ℕ} (v : Vector UInt8 w) : toVecLE w (ofVecLE v) = v
```

`CompPoly.Bytes.toVecLE_inj_of_lt` (theorem, [line 178](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L178))

```lean
theorem toVecLE_inj_of_lt {w n m : ℕ} (hn : n < 256 ^ w) (hm : m < 256 ^ w)
    (h : toVecLE w n = toVecLE w m) : n = m
```

> ## Byte arrays

`CompPoly.Bytes.toByteArrayLE` (definition, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L185))

> The `w` little-endian bytes of `n` as a `ByteArray`.

```lean
def toByteArrayLE (w n : ℕ) : ByteArray
```

`CompPoly.Bytes.ofByteArrayLE` (definition, [line 188](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L188))

> The natural with the given little-endian bytes.

```lean
def ofByteArrayLE (b : ByteArray) : ℕ
```

`CompPoly.Bytes.size_toByteArrayLE` (theorem, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L190))

```lean
theorem size_toByteArrayLE (w n : ℕ) : (toByteArrayLE w n).size = w
```

`CompPoly.Bytes.data_toByteArrayLE` (theorem, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L193))

```lean
theorem data_toByteArrayLE (w n : ℕ) :
    (toByteArrayLE w n).data = (toListLE w n).toArray
```

`CompPoly.Bytes.ofByteArrayLE_toByteArrayLE` (theorem, [line 196](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L196))

```lean
theorem ofByteArrayLE_toByteArrayLE (w n : ℕ) : ofByteArrayLE (toByteArrayLE w n) = n % 256 ^ w
```

`CompPoly.Bytes.ofByteArrayLE_toByteArrayLE_of_lt` (theorem, [line 199](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L199))

```lean
theorem ofByteArrayLE_toByteArrayLE_of_lt {w n : ℕ} (h : n < 256 ^ w) :
    ofByteArrayLE (toByteArrayLE w n) = n
```

`CompPoly.Bytes.toByteArrayLE_inj_of_lt` (theorem, [line 203](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean#L203))

```lean
theorem toByteArrayLE_inj_of_lt {w n m : ℕ} (hn : n < 256 ^ w) (hm : m < 256 ^ w)
    (h : toByteArrayLE w n = toByteArrayLE w m) : n = m
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Data/Bytes/LittleEndian.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/LittleEndian.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Bytes.LittleEndian.json)
