---
catalog: module
lean: Nat.ofFinDigits, Nat.ofFinDigitsRev, Nat.toFinDigitsFixed, Nat.toFinDigitsFixedRev, Nat.toFinDigits, Nat.toFinDigitsRev, Nat.toFinDigitsRev_eq_reverse_toFinDigits, Nat.toFinDigitsFixedRev_eq_reverse_toFinDigitsFixed, Nat.ofFinDigitsRev_eq_ofFinDigits_reverse, Nat.ofFinDigits_nil, Nat.ofFinDigits_append, Nat.ofFinDigits_cons, Nat.toFinDigitsFixed_zero, Nat.toFinDigitsFixed_succ, Nat.length_toFinDigitsFixed, Nat.ofFinDigits_toFinDigitsFixed, Nat.toFinDigitsFixed_add, Nat.toFinDigits_zero, Nat.toFinDigits_of_ne_zero, Nat.ofFinDigits_toFinDigits, Nat.toFinDigits_eq_append, Nat.ofFinDigits_of_le_one, Nat.toFinDigitsFixed_one, Nat.ofFinDigits_lt_pow, Nat.toFinDigitsFixed_ofFinDigits, Nat.toFinDigits_of_lt_two, Nat.toFinDigits_eq_nil_iff, Nat.toFinDigits_head?_ne_zero, Nat.toFinDigits_ofFinDigits, Nat.Internal.ofFinDigits, Nat.Internal.ofFinDigits_eq, Nat.Internal.toFinDigitsFixed, Nat.Internal.toFinDigitsFixed_eq, Nat.Internal.toFinDigits, Nat.Internal.toFinDigits_eq
statement: formalized
proof: formalized
---

# Digits

`Batteries.Data.Nat.Digits`, in [Batteries/Data/Nat/Digits.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean), by François G. Dorais.

> Conversions between natural numbers and big-endian or little-endian lists of digits in a given
> base. The digits are represented as elements of `Fin base`.
>
> The definitions are simple specifications. They are replaced at runtime, using `csimp`, by
> divide-and-conquer implementations, which are subquadratic when combined with the subquadratic
> multiplication and division of `Nat`.

`Nat.ofFinDigits` (definition, [line 33](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L33))

> Construct a natural number from a big-endian list of digits in the given base:
> ```
> ofFinDigits (base := 10) [2,3,4] = 234 -- 2*10^2 + 3*10^1 + 4*10^0
> ofFinDigits (base := 2) [0,1,0,0] = 4 -- 0*2^3 + 1*2^2 + 0*2^1 + 0*2^0
> ofFinDigits (base := b) [] = 0 -- any base, including "base 0" and "base 1"
> ```
> There are no valid inputs other than `[]` in "base 0". In "base 1", the only valid digit is `0`
> and therefore `ofFinDigits (base := 1) l = 0`.

```lean
public def ofFinDigits (l : List (Fin base)) : Nat
```

`Nat.ofFinDigitsRev` (definition, [line 46](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L46))

> Construct a natural number from a little-endian list of digits in the given base:
> ```
> ofFinDigitsRev (base := 10) [4,3,2] = 234 -- 2*10^2 + 3*10^1 + 4*10^0
> ofFinDigitsRev (base := 2) [0,0,1,0] = 4 -- 0*2^3 + 1*2^2 + 0*2^1 + 0*2^0
> ofFinDigitsRev (base := b) [] = 0 -- any base, including "base 0" and "base 1"
> ```
> There are no valid inputs other than `[]` in "base 0". In "base 1", the only valid digit is `0`
> and therefore `ofFinDigitsRev (base := 1) l = 0`.

```lean
public def ofFinDigitsRev (l : List (Fin base)) : Nat
```

`Nat.toFinDigitsFixed` (definition, [line 61](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L61))

> The `prec` least significant digits of `n` in the given `base`, listed in big-endian order.
>
> Only "base 0" is invalid, this is ensured by a `NeZero base` instance. In "base 1" the result is
> always a list of `0`s with length `prec`.
> ```
> toFinDigitsFixed 123 10 3 = ([1,2,3] : List (Fin 10))
> toFinDigitsFixed 123 10 2 = ([2,3] : List (Fin 10))
> toFinDigitsFixed 4 2 4 = ([0,1,0,0] : List (Fin 2))
> toFinDigitsFixed 12345 1 5 = ([0,0,0,0,0] : List (Fin 1))
> ```

```lean
public def toFinDigitsFixed (n base prec : Nat) [NeZero base] : List (Fin base)
```

`Nat.toFinDigitsFixedRev` (definition, [line 78](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L78))

> The `prec` least significant digits of `n` in the given `base`, listed in little-endian order.
>
> Only "base 0" is invalid, this is ensured by a `NeZero base` instance. In "base 1" the result is
> always a list of `0`s with length `prec`.
> ```
> toFinDigitsFixedRev 123 10 3 = ([3,2,1] : List (Fin 10))
> toFinDigitsFixedRev 123 10 2 = ([3,2] : List (Fin 10))
> toFinDigitsFixedRev 4 2 4 = ([0,0,1,0] : List (Fin 2))
> toFinDigitsFixedRev 12345 1 5 = ([0,0,0,0,0] : List (Fin 1))
> ```

```lean
public def toFinDigitsFixedRev (n base prec : Nat) [NeZero base] : List (Fin base)
```

`Nat.toFinDigits` (definition, [line 94](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L94))

> Big-endian list of digits of a natural number `n` in a given `base`.
>
> When `n` is zero, the result is the empty list. Otherwise, the most significant digit is nonzero.
> The base should be at least 2, the result is always the empty list in "base 0" and "base 1".
> ```
> toFinDigits 123 10 = ([1,2,3] : List (Fin 10))
> toFinDigits 4 2 = ([1,0,0] : List (Fin 2))
> toFinDigits 0 12345 = ([] : List (Fin 12345))
> ```

```lean
public def toFinDigits (n base : Nat) : List (Fin base)
```

`Nat.toFinDigitsRev` (definition, [line 111](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L111))

> Little-endian list of digits of a natural number `n` in a given `base`.
>
> When `n` is zero, the result is the empty list. Otherwise, the most significant digit is nonzero.
> The base should be at least 2, the result is always the empty list in "base 0" and "base 1".
> ```
> toFinDigitsRev 123 10 = ([3,2,1] : List (Fin 10))
> toFinDigitsRev 4 2 = ([0,0,1] : List (Fin 2))
> toFinDigitsRev 0 12345 = ([] : List (Fin 12345))
> ```

```lean
public def toFinDigitsRev (n base : Nat) : List (Fin base)
```

> ### Lemmas

`Nat.toFinDigitsRev_eq_reverse_toFinDigits` (theorem, [line 119](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L119))

```lean
public theorem toFinDigitsRev_eq_reverse_toFinDigits (n : Nat) :
    n.toFinDigitsRev base = (n.toFinDigits base).reverse
```

`Nat.toFinDigitsFixedRev_eq_reverse_toFinDigitsFixed` (theorem, [line 131](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L131))

```lean
public theorem toFinDigitsFixedRev_eq_reverse_toFinDigitsFixed [NeZero base] (n : Nat) :
    n.toFinDigitsFixedRev base prec = (n.toFinDigitsFixed base prec).reverse
```

`Nat.ofFinDigitsRev_eq_ofFinDigits_reverse` (theorem, [line 137](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L137))

```lean
public theorem ofFinDigitsRev_eq_ofFinDigits_reverse (l : List (Fin base)) :
    ofFinDigitsRev l = ofFinDigits l.reverse
```

`Nat.ofFinDigits_nil` (theorem, [line 141](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L141))

```lean
public theorem ofFinDigits_nil : ofFinDigits (base := base) [] = 0
```

`Nat.ofFinDigits_append` (theorem, [line 143](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L143))

```lean
public theorem ofFinDigits_append {l₁ l₂ : List (Fin base)} :
    ofFinDigits (l₁ ++ l₂) = ofFinDigits l₁ * base ^ l₂.length + ofFinDigits l₂
```

`Nat.ofFinDigits_cons` (theorem, [line 155](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L155))

```lean
public theorem ofFinDigits_cons {l : List (Fin base)} :
    ofFinDigits (d :: l) = d * base ^ l.length + ofFinDigits l
```

`Nat.toFinDigitsFixed_zero` (theorem, [line 159](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L159))

```lean
public theorem toFinDigitsFixed_zero [NeZero base] :
    toFinDigitsFixed n base 0 = []
```

`Nat.toFinDigitsFixed_succ` (theorem, [line 162](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L162))

```lean
public theorem toFinDigitsFixed_succ [NeZero base] :
    toFinDigitsFixed n base (prec+1) =
      toFinDigitsFixed (n / base) base prec ++ [Fin.ofNat base n]
```

`Nat.length_toFinDigitsFixed` (theorem, [line 166](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L166))

```lean
public theorem length_toFinDigitsFixed [NeZero base] :
    (toFinDigitsFixed n base prec).length = prec
```

`Nat.ofFinDigits_toFinDigitsFixed` (theorem, [line 170](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L170))

```lean
public theorem ofFinDigits_toFinDigitsFixed [NeZero base] :
    ofFinDigits (toFinDigitsFixed n base prec) = n % base ^ prec
```

`Nat.toFinDigitsFixed_add` (theorem, [line 180](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L180))

```lean
public theorem toFinDigitsFixed_add [NeZero base] : toFinDigitsFixed n base (prec + k) =
    toFinDigitsFixed (n / base ^ k) base prec ++ toFinDigitsFixed (n % base ^ k) base k
```

`Nat.toFinDigits_zero` (theorem, [line 190](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L190))

```lean
public theorem toFinDigits_zero : toFinDigits 0 base = []
```

`Nat.toFinDigits_of_ne_zero` (theorem, [line 193](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L193))

```lean
public theorem toFinDigits_of_ne_zero (h : 2 ≤ base) [NeZero base] (hn : n ≠ 0) :
    toFinDigits n base = toFinDigits (n / base) base ++ [Fin.ofNat base n]
```

`Nat.ofFinDigits_toFinDigits` (theorem, [line 197](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L197))

```lean
public theorem ofFinDigits_toFinDigits (h : 2 ≤ base) :
    ofFinDigits (toFinDigits n base) = n
```

`Nat.toFinDigits_eq_append` (theorem, [line 208](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L208))

```lean
public theorem toFinDigits_eq_append (h : 2 ≤ base) [NeZero base] (hk : base ^ k ≤ n) :
    toFinDigits n base =
      toFinDigits (n / base ^ k) base ++ toFinDigitsFixed (n % base ^ k) base k
```

`Nat.ofFinDigits_of_le_one` (theorem, [line 223](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L223))

> In "base 0" and "base 1", the only valid digits are zeros and `ofFinDigits` is always `0`.

```lean
public theorem ofFinDigits_of_le_one (h : base ≤ 1) {l : List (Fin base)} :
    ofFinDigits l = 0
```

`Nat.toFinDigitsFixed_one` (theorem, [line 232](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L232))

> In "base 1", `toFinDigitsFixed` is a list of zeros.

```lean
public theorem toFinDigitsFixed_one : toFinDigitsFixed n 1 prec = List.replicate prec 0
```

`Nat.ofFinDigits_lt_pow` (theorem, [line 239](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L239))

```lean
public theorem ofFinDigits_lt_pow {l : List (Fin base)} : ofFinDigits l < base ^ l.length
```

`Nat.toFinDigitsFixed_ofFinDigits` (theorem, [line 249](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L249))

```lean
public theorem toFinDigitsFixed_ofFinDigits [NeZero base] {l : List (Fin base)} :
    toFinDigitsFixed (ofFinDigits l) base l.length = l
```

`Nat.toFinDigits_of_lt_two` (theorem, [line 265](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L265))

> In "base 0" and "base 1", `toFinDigits` is always the empty list.

```lean
public theorem toFinDigits_of_lt_two (h : base < 2) : toFinDigits n base = []
```

`Nat.toFinDigits_eq_nil_iff` (theorem, [line 268](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L268))

```lean
public theorem toFinDigits_eq_nil_iff : toFinDigits n base = [] ↔ n = 0 ∨ base < 2
```

`Nat.toFinDigits_head?_ne_zero` (theorem, [line 279](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L279))

> The most significant digit of `toFinDigits n base` is nonzero.

```lean
public theorem toFinDigits_head?_ne_zero : ∀ d ∈ (toFinDigits n base).head?, d.val ≠ 0
```

`Nat.toFinDigits_ofFinDigits` (theorem, [line 303](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L303))

```lean
public theorem toFinDigits_ofFinDigits (h : 2 ≤ base) {l : List (Fin base)}
    (hl : ∀ d ∈ l.head?, d.val ≠ 0) : toFinDigits (ofFinDigits l) base = l
```

> ### Subquadratic implementations
>
> The definitions and theorems in the `Nat.Internal` namespace implement the functions above at
> runtime via `csimp`. They are public only because `csimp` requires it. They are not intended as part
> of the public API and they may change without warning.
>
> Each implementation splits its input roughly in half and falls back to a simple loop on small
> inputs, where computing `base ^ k` and splitting would cost more than it saves. The cutoffs are
> 16 digits for `ofFinDigits` and `toFinDigitsFixed`, and a split size of at least 8 digits for
> `toFinDigits`. They were picked by judgment rather than tuned by benchmarks. Correctness does not
> depend on them.

`Nat.Internal.ofFinDigits` (definition, [line 338](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L338))

> Divide-and-conquer implementation of `Nat.ofFinDigits`.

```lean
public def ofFinDigits (l : List (Fin base)) : Nat
```

`Nat.Internal.ofFinDigits_eq` (theorem, [line 345](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L345))

```lean
public theorem ofFinDigits_eq : @Nat.ofFinDigits = @ofFinDigits
```

`Nat.Internal.toFinDigitsFixed` (definition, [line 353](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L353))

> Divide-and-conquer implementation of `Nat.toFinDigitsFixed`.

```lean
public def toFinDigitsFixed (n base prec : Nat) [NeZero base] : List (Fin base)
```

`Nat.Internal.toFinDigitsFixed_eq` (theorem, [line 382](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L382))

```lean
public theorem toFinDigitsFixed_eq : @Nat.toFinDigitsFixed = @toFinDigitsFixed
```

`Nat.Internal.toFinDigits` (definition, [line 387](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L387))

> Divide-and-conquer implementation of `Nat.toFinDigits`.

```lean
public def toFinDigits (n base : Nat) : List (Fin base)
```

`Nat.Internal.toFinDigits_eq` (theorem, [line 425](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean#L425))

```lean
public theorem toFinDigits_eq : @Nat.toFinDigits = @toFinDigits
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/Nat/Digits.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Digits.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Nat.Digits.json)
