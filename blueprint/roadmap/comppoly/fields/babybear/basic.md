---
catalog: module
lean: BabyBear.fieldSize, BabyBear.Field, BabyBear.is_prime, BabyBear.pBits, BabyBear.twoAdicity, BabyBear.inv_eq_pow, BabyBear.fieldSize_sub_one_factorization, BabyBear.twoAdicGenerators, BabyBear.twoAdicGenerators_length, BabyBear.twoAdicGenerators_succ_square_eq', BabyBear.twoAdicGenerators_succ_square_eq, BabyBear.twoAdicity_maximal, BabyBear.twoAdicGenerators_pow_twoPow_eq_one, BabyBear.twoAdicGenerators_pow_twoPow_ne_one_of_lt, BabyBear.isPrimitiveRoot_twoAdicGenerator, BabyBear.twoAdicGenerator_unit_mem_rootsOfUnity, BabyBear.twoAdicGenerators_order
statement: formalized
proof: formalized
---

# BabyBear Field `2^{31} - 2^{27} + 1`

`CompPoly.Fields.BabyBear.Basic`, in [CompPoly/Fields/BabyBear/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean), by Quang Dao, Valerii Huhnin.

> This is the field used by Risc Zero.

`BabyBear.fieldSize` (definition, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L25))

> The BabyBear field modulus, `2^31 - 2^27 + 1`.

```lean
def fieldSize : Nat
```

`BabyBear.Field` (abbreviation, [line 28](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L28))

> The BabyBear prime field as a `ZMod`.

```lean
abbrev Field
```

`BabyBear.is_prime` (theorem, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L31))

> The BabyBear modulus is prime.

```lean
theorem is_prime : Nat.Prime fieldSize
```

> ## Constants
>
> These are convenience constants for the BabyBear field:
> - `pBits = 31`
> - `twoAdicity = 27` with `fieldSize - 1 = 2^27 * 15`

`BabyBear.pBits` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L45))

> Bit width of the BabyBear modulus.

```lean
def pBits : Nat
```

`BabyBear.twoAdicity` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L49))

> The largest supported power-of-two root-of-unity exponent for BabyBear.

```lean
def twoAdicity : Nat
```

`BabyBear.inv_eq_pow` (lemma, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L59))

> Fermat-style inversion in `ZMod fieldSize`.

```lean
lemma inv_eq_pow (a : Field) (ha : a ≠ 0) : a⁻¹ = a ^ (fieldSize - 2)
```

> ## Two-adicity and roots of unity table
>
> We record the factorization of `fieldSize - 1` and provide a precomputed table
> of `2^n`-th roots of unity for `0 ≤ n ≤ twoAdicity`.

`BabyBear.fieldSize_sub_one_factorization` (lemma, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L78))

> The factorization `fieldSize - 1 = 2^twoAdicity * 15`.

```lean
lemma fieldSize_sub_one_factorization : fieldSize - 1 = 2 ^ twoAdicity * 15
```

> A table of `2^n`-th roots of unity. The element at index `n` generates the
> multiplicative subgroup of order `2^n`.
>
> The first entry n = 0 is 1.

`BabyBear.twoAdicGenerators` (definition, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L89))

> Precomputed generators for the BabyBear two-adic subgroups.

```lean
def twoAdicGenerators : List Field
```

`BabyBear.twoAdicGenerators_length` (lemma, [line 122](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L122))

> The BabyBear two-adic generator table has one entry for each supported exponent.

```lean
lemma twoAdicGenerators_length : twoAdicGenerators.length = twoAdicity + 1
```

`BabyBear.twoAdicGenerators_succ_square_eq'` (lemma, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L126))

> Consecutive BabyBear two-adic generators square to the previous generator.

```lean
lemma twoAdicGenerators_succ_square_eq' (idx : Fin twoAdicity) :
    twoAdicGenerators[idx.val + 1] ^ 2 = twoAdicGenerators[idx]
```

`BabyBear.twoAdicGenerators_succ_square_eq` (lemma, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L132))

> Consecutive BabyBear two-adic generators square to the previous generator.

```lean
lemma twoAdicGenerators_succ_square_eq (idx : Nat) (h : idx < twoAdicity) :
    haveI : idx + 1 < twoAdicGenerators.length := by simp [twoAdicGenerators_length, h]
    twoAdicGenerators[idx + 1] ^ 2 = twoAdicGenerators[idx]
```

`BabyBear.twoAdicity_maximal` (lemma, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L138))

> `twoAdicity` is maximal: `2^(twoAdicity+1)` does not divide `fieldSize - 1`.

```lean
lemma twoAdicity_maximal : ¬ (2 ^ (twoAdicity + 1)) ∣ (fieldSize - 1)
```

`BabyBear.twoAdicGenerators_pow_twoPow_eq_one` (lemma, [line 191](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L191))

> The power `(twoAdicGenerators[bits])^(2^bits) = 1`.

```lean
lemma twoAdicGenerators_pow_twoPow_eq_one (bits : Fin (twoAdicity + 1)) :
    twoAdicGenerators[bits] ^ (2 ^ (bits : Nat)) = 1
```

`BabyBear.twoAdicGenerators_pow_twoPow_ne_one_of_lt` (lemma, [line 226](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L226))

> If `m < bits`, then `(twoAdicGenerators[bits])^(2^m) ≠ 1`.

```lean
lemma twoAdicGenerators_pow_twoPow_ne_one_of_lt
    {bits : Fin (twoAdicity + 1)} {m : Nat} (hm : m < bits) :
    (twoAdicGenerators[bits]) ^ (2 ^ m) ≠ (1 : Field)
```

`BabyBear.isPrimitiveRoot_twoAdicGenerator` (lemma, [line 233](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L233))

> The precomputed element at index `bits` is a primitive `2^bits`-th root of unity.

```lean
lemma isPrimitiveRoot_twoAdicGenerator (n : Fin (twoAdicity + 1)) :
    IsPrimitiveRoot (twoAdicGenerators[n]) (2 ^ (n : Nat))
```

`BabyBear.twoAdicGenerator_unit_mem_rootsOfUnity` (lemma, [line 251](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L251))

> As a unit, the precomputed element is a member of `rootsOfUnity (2^bits)`.

```lean
lemma twoAdicGenerator_unit_mem_rootsOfUnity
    (bits : Fin (twoAdicity + 1)) (h : twoAdicGenerators[bits] ≠ 0) :
    Units.mk0 (twoAdicGenerators[bits]) h ∈ rootsOfUnity (2 ^ (bits : Nat)) Field
```

`BabyBear.twoAdicGenerators_order` (lemma, [line 260](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean#L260))

> The order of `twoAdicGenerators[bits]` equals `2^bits`.

```lean
lemma twoAdicGenerators_order (bits : Fin (twoAdicity + 1)) :
    orderOf (twoAdicGenerators[bits]) = 2 ^ (bits : Nat)
```

## Depends on

- [Non-binary fields and polynomial utilities](../basic.md)

## Proof depends on

- [The Lucas test for primes](../prattcertificate.md)

## Sources

- [CompPoly/Fields/BabyBear/Basic.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Basic.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.BabyBear.Basic.json)
