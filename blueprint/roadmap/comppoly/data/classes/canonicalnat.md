---
catalog: module
lean: CompPoly.CanonicalNat, CompPoly.CanonicalNat.bound_pos, CompPoly.CanonicalNat.toNat_injective, CompPoly.CanonicalNat.toNat_inj, CompPoly.CanonicalNat.toNat_ofNat, CompPoly.CanonicalNat.ofNat?, CompPoly.CanonicalNat.ofNat?_toNat, CompPoly.CanonicalNat.ofNat?_eq_some_iff, CompPoly.CanonicalNat.ofNat?_eq_none_iff, CompPoly.CanonicalNat.equivFin, CompPoly.CanonicalNat.card_eq, CompPoly.CanonicalNat.ofToField, CompPoly.CanonicalNat.ofBitVec, CompPoly.instCanonicalNatZMod, CompPoly.CanonicalNat.bound_zmod, CompPoly.CanonicalNat.toNat_zmod, CompPoly.CanonicalNat.ofNat_zmod
statement: formalized
proof: formalized
---

# Canonical naturals

`CompPoly.Data.Classes.CanonicalNat`, in [CompPoly/Data/Classes/CanonicalNat.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean), by Derek Sorensen.

> `CanonicalNat F` says that every element of `F` has a canonical natural number below a fixed
> `bound`, and that every natural reduces to an element by `ofNat`, with `ofNat` acting as
> reduction modulo `bound`. The laws make `toNat` a bijection onto `Fin bound`, so `bound` is the
> cardinality of `F` and `ofNat` is exactly "the element whose canonical natural is `n % bound`".
>
> For a prime field the canonical natural is the residue in `[0, p)`; for a binary field it is
> the bit pattern of the declared basis; for an extension of degree `d` over a base of size `q`
> it is the base-`q` expansion of the coefficients.
>
> Serialization is *derived* from this class rather than stated with it. The fixed-width byte
> codec of a scalar field is the little-endian bytes of `toNat` (`ByteCodec.ofCanonicalNat` in
> `CompPoly.Data.Bytes.CanonicalNat`), and sampling a field element from a longer byte string
> is `ofNat` of the string's integer, which is uniform up to a bound proved in `Nat` terms.
> Two carriers of the same field agree on `toNat`, so they agree on every derived encoding.

`CompPoly.CanonicalNat` (class, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L38))

> `F` has a canonical natural below `bound` for every element, and every natural reduces to
> an element of `F` modulo `bound`. The laws make `toNat` a bijection `F ≃ Fin bound`.

```lean
class CanonicalNat (F : Type u) where
  /-- The exclusive upper bound on canonical naturals; equal to the cardinality of `F`. -/
  bound : ℕ
  /-- The canonical natural of an element. -/
  toNat : F → ℕ
  /-- The element with canonical natural `n % bound`. -/
  ofNat : ℕ → F
  toNat_lt (x : F) : toNat x < bound
  ofNat_toNat (x : F) : ofNat (toNat x) = x
  toNat_ofNat_of_lt {n : ℕ} (h : n < bound) : toNat (ofNat n) = n
  ofNat_mod (n : ℕ) : ofNat (n % bound) = ofNat n
```

`CompPoly.CanonicalNat.bound_pos` (theorem, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L56))

```lean
theorem bound_pos : 0 < bound F
```

`CompPoly.CanonicalNat.toNat_injective` (theorem, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L59))

```lean
theorem toNat_injective : Function.Injective (toNat : F → ℕ)
```

`CompPoly.CanonicalNat.toNat_inj` (theorem, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L63))

```lean
theorem toNat_inj {x y : F} : toNat x = toNat y ↔ x = y
```

`CompPoly.CanonicalNat.toNat_ofNat` (theorem, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L67))

```lean
theorem toNat_ofNat (n : ℕ) : toNat (ofNat (F := F) n) = n % bound F
```

`CompPoly.CanonicalNat.ofNat?` (definition, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L71))

> Decode a natural as an element, failing when it is not a canonical natural.

```lean
def ofNat? (n : ℕ) : Option F
```

`CompPoly.CanonicalNat.ofNat?_toNat` (theorem, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L75))

```lean
theorem ofNat?_toNat (x : F) : ofNat? (toNat x) = some x
```

`CompPoly.CanonicalNat.ofNat?_eq_some_iff` (theorem, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L78))

```lean
theorem ofNat?_eq_some_iff {n : ℕ} {x : F} : ofNat? n = some x ↔ n < bound F ∧ toNat x = n
```

`CompPoly.CanonicalNat.ofNat?_eq_none_iff` (theorem, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L92))

```lean
theorem ofNat?_eq_none_iff {n : ℕ} : ofNat? (F := F) n = none ↔ bound F ≤ n
```

`CompPoly.CanonicalNat.equivFin` (definition, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L98))

> The canonical natural as an equivalence with `Fin (bound F)`.

```lean
def equivFin : F ≃ Fin (bound F)
```

`CompPoly.CanonicalNat.card_eq` (theorem, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L105))

> The bound is the cardinality of `F`.

```lean
theorem card_eq [Fintype F] : Fintype.card F = bound F
```

> ## Constructors
>
> Two ways a concrete type acquires the structure. A fast carrier of a prime field supplies its
> own `toNat` together with the conversion from `ZMod p`; a binary field supplies its bit
> pattern. Both are `@[instance_reducible]` definitions so an instance can be
> `CanonicalNat.ofToField …` or `CanonicalNat.ofBitVec …` directly.

`CompPoly.CanonicalNat.ofToField` (definition, [line 119](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L119))

> The canonical-natural structure of a carrier of `ZMod p`: the carrier's own `toNat`, with
> `ofField` as the way back. The hypothesis `toNat_ofField` is the carrier-agreement law, so
> every encoding derived from this structure agrees with the one on `ZMod p`.

```lean
def ofToField {p : ℕ} [NeZero p] (toNat : F → ℕ) (ofField : ZMod p → F)
    (toNat_lt : ∀ x, toNat x < p) (ofField_cast_toNat : ∀ x, ofField (toNat x : ZMod p) = x)
    (toNat_ofField : ∀ n : ZMod p, toNat (ofField n) = n.val) : CanonicalNat F
```

`CompPoly.CanonicalNat.ofBitVec` (definition, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L133))

> The canonical-natural structure of a type presented as `k`-bit patterns: the bit pattern
> read as an integer, with `bound = 2 ^ k`.

```lean
def ofBitVec {k : ℕ} (toBitVec : F → BitVec k) (ofBitVec : BitVec k → F)
    (ofBitVec_toBitVec : ∀ x, ofBitVec (toBitVec x) = x)
    (toBitVec_ofBitVec : ∀ b, toBitVec (ofBitVec b) = b) : CanonicalNat F
```

`CompPoly.instCanonicalNatZMod` (instance, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L149))

> `ZMod p` with the residue in `[0, p)` as canonical natural.

```lean
instance instCanonicalNatZMod (p : ℕ) [NeZero p] : CanonicalNat (ZMod p)
```

`CompPoly.CanonicalNat.bound_zmod` (theorem, [line 158](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L158))

```lean
theorem CanonicalNat.bound_zmod (p : ℕ) [NeZero p] : CanonicalNat.bound (ZMod p) = p
```

`CompPoly.CanonicalNat.toNat_zmod` (theorem, [line 160](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L160))

```lean
theorem CanonicalNat.toNat_zmod {p : ℕ} [NeZero p] (x : ZMod p) :
    CanonicalNat.toNat x = x.val
```

`CompPoly.CanonicalNat.ofNat_zmod` (theorem, [line 163](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean#L163))

```lean
theorem CanonicalNat.ofNat_zmod {p : ℕ} [NeZero p] (n : ℕ) :
    CanonicalNat.ofNat (F := ZMod p) n = (n : ZMod p)
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Data/Classes/CanonicalNat.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/CanonicalNat.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Classes.CanonicalNat.json)
