---
catalog: module
lean: Fin.encodeEmpty, Fin.decodeEmpty, Fin.encodeEmpty_decodeEmpty, Fin.decodeEmpty_encodeEmpty, Fin.encodePUnit, Fin.decodePUnit, Fin.encodeUnit, Fin.decodeUnit, Fin.encodePUnit_decodePUnit, Fin.decodePUnit_encodePUnit, Fin.encodeBool, Fin.decodeBool, Fin.encodeBool_decodeBool, Fin.decodeBool_encodeBool, Fin.encodeOrdering, Fin.decodeOrdering, Fin.encodeOrdering_decodeOrdering, Fin.decodeOrdering_encodeOrdering, Fin.encodeChar, Fin.decodeChar, Fin.encodeChar_decodeChar, Fin.decodeChar_encodeChar, Fin.encodeOption, Fin.decodeOption, Fin.encodeOption_decodeOption, Fin.decodeOption_encodeOption, Fin.encodeSum, Fin.decodeSum, Fin.encodeSum_decodeSum, Fin.decodeSum_encodeSum, Fin.encodeProd, Fin.decodeProd, Fin.encodeProd_decodeProd, Fin.decodeProd_encodeProd, Fin.encodeSigma, Fin.decodeSigma, Fin.encodeSigma_decodeSigma, Fin.decodeSigma_encodeSigma, Fin.encodeFun, Fin.decodeFun, Fin.encodeFun_decodeFun, Fin.decodeFun_encodeFun, Fin.encodePi, Fin.decodePi, Fin.encodePi_decodePi, Fin.decodePi_encodePi, Fin.encodeSubtype, Fin.decodeSubtype, Fin.encodeSubtype_zero_pos, Fin.encodeSubtype_succ_pos, Fin.encodeSubtype_succ_neg, Fin.encodeSubtype_decodeSubtype, Fin.decodeSubtype_encodeSubtype, Fin.getRepr, Fin.equiv_getRepr, Fin.getRepr_equiv, Fin.getRepr_eq_getRepr_of_equiv, Fin.getRepr_getRepr, Fin.encodeQuotient, Fin.decodeQuotient, Fin.encodeQuotient_decodeQuotient, Fin.decodeQuotient_encodeQuotient
statement: formalized
proof: formalized
---

# Low-level coding recipes for `Fin` types

`Batteries.Data.Fin.Coding`, in [Batteries/Data/Fin/Coding.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean), by François G. Dorais.

> This module collects encoding/decoding bijections to represent basic type constructors of `Fin`
> types as `Fin` types. These functions implement the isomorphism `Option (Fin n) ≃ Fin (n+1)`,
> `Fin m ⊕ Fin n ≃ Fin (m + n)`, `Fin m × Fin n ≃ Fin (m * n)`, ..., including, dependent sums,
> dependent products, decidable subtypes and decidable quotients.
>
> Only a minimal API is provided. These utility functions are intended for use in other constructions.
> Such constructions should avoid exposing these functions as they are not meant for public use.

`Fin.encodeEmpty` (definition, [line 29](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L29))

> Encode `Empty` into `Fin 0`.

```lean
def encodeEmpty : Empty → Fin 0
```

`Fin.decodeEmpty` (definition, [line 32](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L32))

> Decode `Empty` from `Fin 0`.

```lean
def decodeEmpty : Fin 0 → Empty
```

`Fin.encodeEmpty_decodeEmpty` (theorem, [line 34](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L34))

```lean
theorem encodeEmpty_decodeEmpty (x : Fin 0) : encodeEmpty (decodeEmpty x) = x
```

`Fin.decodeEmpty_encodeEmpty` (theorem, [line 36](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L36))

```lean
theorem decodeEmpty_encodeEmpty (x : Empty) : decodeEmpty (encodeEmpty x) = x
```

`Fin.encodePUnit` (definition, [line 40](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L40))

> Encode `PUnit` into `Fin 1`.

```lean
def encodePUnit : PUnit → Fin 1
```

`Fin.decodePUnit` (definition, [line 44](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L44))

> Decode `PUnit` from `Fin 1`.

```lean
def decodePUnit : Fin 1 → PUnit
```

`Fin.encodeUnit` (abbreviation, [line 48](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L48))

> Encode `Unit` into `Fin 1`.

```lean
abbrev encodeUnit : Unit → Fin 1
```

`Fin.decodeUnit` (abbreviation, [line 51](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L51))

> Decode `Unit` from `Fin 1`.

```lean
abbrev decodeUnit : Fin 1 → Unit
```

`Fin.encodePUnit_decodePUnit` (theorem, [line 53](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L53))

```lean
theorem encodePUnit_decodePUnit : (x : Fin 1) → encodePUnit (decodePUnit x) = x
```

`Fin.decodePUnit_encodePUnit` (theorem, [line 56](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L56))

```lean
theorem decodePUnit_encodePUnit : (x : PUnit) → decodePUnit (encodePUnit x) = x
```

`Fin.encodeBool` (definition, [line 60](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L60))

> Encode `Bool` into `Fin 2`.

```lean
def encodeBool : Bool → Fin 2
```

`Fin.decodeBool` (definition, [line 65](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L65))

> Decode `Bool` from `Fin 2`.

```lean
def decodeBool : Fin 2 → Bool
```

`Fin.encodeBool_decodeBool` (theorem, [line 69](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L69))

```lean
theorem encodeBool_decodeBool : (x : Fin 2) → encodeBool (decodeBool x) = x
```

`Fin.decodeBool_encodeBool` (theorem, [line 72](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L72))

```lean
theorem decodeBool_encodeBool : (x : Bool) → decodeBool (encodeBool x) = x
```

`Fin.encodeOrdering` (definition, [line 76](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L76))

> Encode `Ordering` into `Fin 3`.

```lean
def encodeOrdering : Ordering → Fin 3
```

`Fin.decodeOrdering` (definition, [line 82](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L82))

> Decode `Ordering` from `Fin 3`.

```lean
def decodeOrdering : Fin 3 → Ordering
```

`Fin.encodeOrdering_decodeOrdering` (theorem, [line 87](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L87))

```lean
theorem encodeOrdering_decodeOrdering : (x : Fin 3) → encodeOrdering (decodeOrdering x) = x
```

`Fin.decodeOrdering_encodeOrdering` (theorem, [line 90](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L90))

```lean
theorem decodeOrdering_encodeOrdering :
    (x : Ordering) → decodeOrdering (encodeOrdering x) = x
```

`Fin.encodeChar` (definition, [line 95](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L95))

> Encode `Char` into `Fin Char.count`.

```lean
def encodeChar (c : Char) : Fin Char.count
```

`Fin.decodeChar` (definition, [line 102](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L102))

> Decode `Char` from `Fin Char.count`.

```lean
def decodeChar (i : Fin Char.count) : Char
```

`Fin.encodeChar_decodeChar` (theorem, [line 108](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L108))

```lean
theorem encodeChar_decodeChar (x) : encodeChar (decodeChar x) = x
```

`Fin.decodeChar_encodeChar` (theorem, [line 115](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L115))

```lean
theorem decodeChar_encodeChar (x) : decodeChar (encodeChar x) = x
```

`Fin.encodeOption` (definition, [line 125](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L125))

> Encode `Option (Fin n)` into `Fin (n+1)`.

```lean
def encodeOption : Option (Fin n) → Fin (n+1)
```

`Fin.decodeOption` (definition, [line 130](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L130))

> Decode `Option (Fin n)` from `Fin (n+1)`.

```lean
def decodeOption : Fin (n+1) → Option (Fin n)
```

`Fin.encodeOption_decodeOption` (theorem, [line 134](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L134))

```lean
theorem encodeOption_decodeOption (x : Fin (n+1)) : encodeOption (decodeOption x) = x
```

`Fin.decodeOption_encodeOption` (theorem, [line 146](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L146))

```lean
theorem decodeOption_encodeOption (x : Option (Fin n)) :
    decodeOption (encodeOption x) = x
```

`Fin.encodeSum` (definition, [line 160](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L160))

> Encode `Fin n ⊕ Fin m` into `Fin (n + m)`.

```lean
def encodeSum : Sum (Fin n) (Fin m) → Fin (n + m)
```

`Fin.decodeSum` (definition, [line 165](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L165))

> Decode `Fin n ⊕ Fin m` from `Fin (n + m)`.

```lean
def decodeSum (x : Fin (n + m)) : Sum (Fin n) (Fin m)
```

`Fin.encodeSum_decodeSum` (theorem, [line 168](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L168))

```lean
theorem encodeSum_decodeSum (x : Fin (n + m)) :
    encodeSum (decodeSum x) = x
```

`Fin.decodeSum_encodeSum` (theorem, [line 173](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L173))

```lean
theorem decodeSum_encodeSum (x : Sum (Fin n) (Fin m)) :
    decodeSum (encodeSum x) = x
```

`Fin.encodeProd` (definition, [line 179](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L179))

> Encode `Fin m × Fin n` into `Fin (m * n)`.

```lean
def encodeProd : Fin m × Fin n → Fin (m * n)
```

`Fin.decodeProd` (definition, [line 183](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L183))

> Decode `Fin m × Fin n` from `Fin (m * n)`.

```lean
def decodeProd (z : Fin (m * n)) : Fin m × Fin n
```

`Fin.encodeProd_decodeProd` (theorem, [line 186](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L186))

```lean
theorem encodeProd_decodeProd (x : Fin (m * n)) : encodeProd (decodeProd x) = x
```

`Fin.decodeProd_encodeProd` (theorem, [line 189](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L189))

```lean
theorem decodeProd_encodeProd (x : Fin m × Fin n) : decodeProd (encodeProd x) = x
```

`Fin.encodeSigma` (definition, [line 193](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L193))

> Encode `(i : Fin n) × Fin (f i)` into `Fin (Fin.sum f)`.

```lean
def encodeSigma (f : Fin n → Nat) (x : (i : Fin n) × Fin (f i)) : Fin (Fin.sum f)
```

`Fin.decodeSigma` (definition, [line 202](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L202))

> Decode `(i : Fin n) × Fin (f i)` from `Fin (Fin.sum f)`.

```lean
def decodeSigma (f : Fin n → Nat) (x : Fin (Fin.sum f)) : (i : Fin n) × Fin (f i)
```

`Fin.encodeSigma_decodeSigma` (theorem, [line 213](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L213))

```lean
theorem encodeSigma_decodeSigma (f : Fin n → Nat) (x : Fin (Fin.sum f)) :
    encodeSigma f (decodeSigma f x) = x
```

`Fin.decodeSigma_encodeSigma` (theorem, [line 229](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L229))

```lean
theorem decodeSigma_encodeSigma (f : Fin n → Nat) (x : (i : Fin n) × Fin (f i)) :
    decodeSigma f (encodeSigma f x) = x
```

`Fin.encodeFun` (definition, [line 256](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L256))

> Encode `Fin m → Fin n` into `Fin (n ^ m)`.

```lean
def encodeFun : {m : Nat} → (Fin m → Fin n) → Fin (n ^ m)
  | 0, _ => ⟨0, by simp⟩
  | m+1, f => Fin.mk (n * (encodeFun fun k => f k.succ).val + (f 0).val) <| calc
    _ < n * (encodeFun fun k => f k.succ).val + n
```

`Fin.decodeFun` (definition, [line 266](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L266))

> Decode `Fin m → Fin n` from `Fin (n ^ m)`.

```lean
def decodeFun : {m : Nat} → Fin (n ^ m) → Fin m → Fin n
```

`Fin.encodeFun_decodeFun` (theorem, [line 276](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L276))

```lean
theorem encodeFun_decodeFun (x : Fin (n ^ m)) : encodeFun (decodeFun x) = x
```

`Fin.decodeFun_encodeFun` (theorem, [line 281](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L281))

```lean
theorem decodeFun_encodeFun (x : Fin m → Fin n) : decodeFun (encodeFun x) = x
```

`Fin.encodePi` (definition, [line 294](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L294))

> Encode `(i : Fin n) → Fin (f i)` into `Fin (Fin.prod f)`.

```lean
def encodePi (f : Fin n → Nat) (x : (i : Fin n) → Fin (f i)) : Fin (Fin.prod f)
```

`Fin.decodePi` (definition, [line 306](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L306))

> Decode `(i : Fin n) → Fin (f i)` from `Fin (Fin.prod f)`.

```lean
def decodePi (f : Fin n → Nat) (x : Fin (Fin.prod f)) : (i : Fin n) → Fin (f i)
```

`Fin.encodePi_decodePi` (theorem, [line 319](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L319))

```lean
theorem encodePi_decodePi (f : Fin n → Nat) (x : Fin (Fin.prod f)) :
    encodePi f (decodePi f x) = x
```

`Fin.decodePi_encodePi` (theorem, [line 332](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L332))

```lean
theorem decodePi_encodePi (f : Fin n → Nat) (x : (i : Fin n) → Fin (f i)) :
    decodePi f (encodePi f x) = x
```

`Fin.encodeSubtype` (definition, [line 349](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L349))

> Encode `{ i : Fin n // P i }` into `Fin (Fin.countP P)` where `P` is a decidable predicate.

```lean
def encodeSubtype (P : Fin n → Prop) [inst : DecidablePred P] (i : { i // P i }) :
    Fin (Fin.countP (P ·))
```

`Fin.decodeSubtype` (definition, [line 368](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L368))

> Decode `{ i : Fin n // P i }` from `Fin (Fin.countP P)` where `P` is a decidable predicate.

```lean
def decodeSubtype (P : Fin n → Prop) [inst : DecidablePred P] (k : Fin (Fin.countP (P ·))) :
    { i // P i }
```

`Fin.encodeSubtype_zero_pos` (theorem, [line 386](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L386))

```lean
theorem encodeSubtype_zero_pos {P : Fin (n+1) → Prop} [DecidablePred P] (h₀ : P 0) :
    encodeSubtype P ⟨0, h₀⟩ = ⟨0, by grind [countP_succ]⟩
```

`Fin.encodeSubtype_succ_pos` (theorem, [line 390](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L390))

```lean
theorem encodeSubtype_succ_pos {P : Fin (n+1) → Prop} [DecidablePred P] (h₀ : P 0) {i : Fin n}
    (h : P i.succ) : encodeSubtype P ⟨i.succ, h⟩ =
      (encodeSubtype (fun i => P i.succ) ⟨i, h⟩).succ.cast (by grind [countP_succ])
```

`Fin.encodeSubtype_succ_neg` (theorem, [line 395](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L395))

```lean
theorem encodeSubtype_succ_neg {P : Fin (n+1) → Prop} [DecidablePred P] (h₀ : ¬ P 0) {i : Fin n}
    (h : P i.succ) : encodeSubtype P ⟨i.succ, h⟩ =
      (encodeSubtype (fun i => P i.succ) ⟨i, h⟩).cast
        (by simp [-countP_eq_countP_map_finRange, countP_succ, *])
```

`Fin.encodeSubtype_decodeSubtype` (theorem, [line 401](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L401))

```lean
theorem encodeSubtype_decodeSubtype (P : Fin n → Prop) [DecidablePred P]
    (x : Fin (Fin.countP (P ·))) : encodeSubtype P (decodeSubtype P x) = x
```

`Fin.decodeSubtype_encodeSubtype` (theorem, [line 411](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L411))

```lean
theorem decodeSubtype_encodeSubtype (P : Fin n → Prop) [DecidablePred P] (x : { x // P x}) :
    decodeSubtype P (encodeSubtype P x) = x
```

`Fin.getRepr` (abbreviation, [line 438](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L438))

> Get representative for the equivalence class of `x`.

```lean
abbrev getRepr (s : Setoid (Fin n)) [DecidableRel s.r] (x : Fin n) : Fin n
```

`Fin.equiv_getRepr` (theorem, [line 449](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L449))

```lean
theorem equiv_getRepr (s : Setoid (Fin n)) [DecidableRel s.r] (x : Fin n) :
    s.r x (getRepr s x)
```

`Fin.getRepr_equiv` (theorem, [line 461](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L461))

```lean
theorem getRepr_equiv (s : Setoid (Fin n)) [DecidableRel s.r] (x : Fin n) :
    s.r (getRepr s x) x
```

`Fin.getRepr_eq_getRepr_of_equiv` (theorem, [line 464](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L464))

```lean
theorem getRepr_eq_getRepr_of_equiv (s : Setoid (Fin n)) [DecidableRel s.r] (h : s.r x y) :
    getRepr s x = getRepr s y
```

`Fin.getRepr_getRepr` (theorem, [line 491](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L491))

```lean
theorem getRepr_getRepr (s : Setoid (Fin n)) [DecidableRel s.r] (x : Fin n) :
    getRepr s (getRepr s x) = getRepr s x
```

`Fin.encodeQuotient` (definition, [line 497](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L497))

> Encode `Quotient s` into `Fin m` where `s` is a decidable setoid on `Fin n`.

```lean
def encodeQuotient (s : Setoid (Fin n)) [DecidableRel s.r] (x : Quotient s) :
    Fin (Fin.countP fun i => getRepr s i = i)
```

`Fin.decodeQuotient` (definition, [line 505](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L505))

> Decode `Quotient s` from `Fin m` where `s` is a decidable setoid on `Fin n`.

```lean
def decodeQuotient (s : Setoid (Fin n)) [DecidableRel s.r]
    (i : Fin (Fin.countP fun i => getRepr s i = i)) : Quotient s
```

`Fin.encodeQuotient_decodeQuotient` (theorem, [line 509](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L509))

```lean
theorem encodeQuotient_decodeQuotient (s : Setoid (Fin n)) [DecidableRel s.r] (x) :
    encodeQuotient s (decodeQuotient s x) = x
```

`Fin.decodeQuotient_encodeQuotient` (theorem, [line 516](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean#L516))

```lean
theorem decodeQuotient_encodeQuotient (s : Setoid (Fin n)) [DecidableRel s.r] (x) :
    decodeQuotient s (encodeQuotient s x) = x
```

## Depends on

- [Char/Basic](../char/basic.md)
- [Fin/Basic](basic.md)

## Proof depends on

- [Fin/Lemmas](lemmas.md)

## Sources

- [Batteries/Data/Fin/Coding.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Coding.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Fin.Coding.json)
