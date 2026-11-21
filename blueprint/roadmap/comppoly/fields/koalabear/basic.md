---
catalog: module
lean: KoalaBear.fieldSize, KoalaBear.Field, KoalaBear.is_prime, KoalaBear.pBits, KoalaBear.twoAdicity, KoalaBear.fieldSize_sub_one_factorization, KoalaBear.twoAdicGenerators, KoalaBear.twoAdicGenerators_length, KoalaBear.twoAdicGenerators_succ_square_eq', KoalaBear.twoAdicGenerators_succ_square_eq, KoalaBear.inv_eq_pow, KoalaBear.cube_map_bijective, KoalaBear.coprime_three_fieldSize_sub_one, KoalaBear.twoAdicity_maximal, KoalaBear.twoAdicGenerators_pow_twoPow_eq_one, KoalaBear.twoAdicGenerators_pow_twoPow_ne_one_of_lt, KoalaBear.isPrimitiveRoot_twoAdicGenerator, KoalaBear.twoAdicGenerator_unit_mem_rootsOfUnity, KoalaBear.twoAdicGenerators_order, KoalaBear.primitiveRoot, KoalaBear.primitiveRoot_order, KoalaBear.smoothRootSchedule, KoalaBear.smoothRootSchedule_fold_eq_one
statement: formalized
proof: formalized
---

# KoalaBear Field `2^{31} - 2^{24} + 1`

`CompPoly.Fields.KoalaBear.Basic`, in [CompPoly/Fields/KoalaBear/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean), by Quang Dao, Valerii Huhnin.

> This is the field used for lean Ethereum spec.

`KoalaBear.fieldSize` (definition, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L26))

> The KoalaBear field modulus, `2^31 - 2^24 + 1`.

```lean
def fieldSize : Nat
```

`KoalaBear.Field` (abbreviation, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L32))

> The KoalaBear prime field as a `ZMod`.

```lean
abbrev Field
```

`KoalaBear.is_prime` (theorem, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L35))

> The KoalaBear modulus is prime.

```lean
theorem is_prime : Nat.Prime fieldSize
```

> ## Constants
>
> These are convenience constants to match the Python module:
> - `pBits = 31`
> - `twoAdicity = 24` with `fieldSize - 1 = 2^24 * 127`

`KoalaBear.pBits` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L49))

> Bit width of the KoalaBear modulus.

```lean
def pBits : Nat
```

`KoalaBear.twoAdicity` (definition, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L53))

> The largest supported power-of-two root-of-unity exponent for KoalaBear.

```lean
def twoAdicity : Nat
```

> Provide instances so `KoalaBear.Field = ZMod fieldSize` is available as a `Field`
> and as a `NonBinaryField` (char ≠ 2).

> ## Two-adicity and roots of unity table
>
> We record the factorization of `fieldSize - 1` and provide a precomputed table
> of `2^n`-th roots of unity for `0 ≤ n ≤ twoAdicity`.

`KoalaBear.fieldSize_sub_one_factorization` (lemma, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L78))

> The factorization `fieldSize - 1 = 2^twoAdicity * 127`.

```lean
lemma fieldSize_sub_one_factorization : fieldSize - 1 = 2 ^ twoAdicity * 127
```

> A table of `2^n`-th roots of unity. The element at index `n` generates the
> multiplicative subgroup of order `2^n`.
>
> The first entry n = 0 is 1.

`KoalaBear.twoAdicGenerators` (definition, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L89))

> Precomputed generators for the KoalaBear two-adic subgroups.

```lean
def twoAdicGenerators : List Field
```

`KoalaBear.twoAdicGenerators_length` (lemma, [line 118](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L118))

```lean
lemma twoAdicGenerators_length : twoAdicGenerators.length = twoAdicity + 1
```

`KoalaBear.twoAdicGenerators_succ_square_eq'` (lemma, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L120))

```lean
lemma twoAdicGenerators_succ_square_eq' (idx : Fin twoAdicity) :
    twoAdicGenerators[idx.val + 1] ^ 2 = twoAdicGenerators[idx]
```

`KoalaBear.twoAdicGenerators_succ_square_eq` (lemma, [line 125](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L125))

```lean
lemma twoAdicGenerators_succ_square_eq (idx : Nat) (h : idx < twoAdicity) :
    haveI : idx + 1 < twoAdicGenerators.length := by simp [twoAdicGenerators_length, h]
    twoAdicGenerators[idx + 1] ^ 2 = twoAdicGenerators[idx]
```

> Statements requested by the Python spec translation.

`KoalaBear.inv_eq_pow` (lemma, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L133))

> Fermat-style inversion in `ZMod fieldSize`.

```lean
lemma inv_eq_pow (a : Field) (ha : a ≠ 0) : a⁻¹ = a ^ (fieldSize - 2)
```

`KoalaBear.cube_map_bijective` (lemma, [line 145](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L145))

> Bijectivity of the cube map on the unit group, using `gcd(3, fieldSize-1)=1`.

```lean
lemma cube_map_bijective :
    Function.Bijective (fun x : Fieldˣ ↦ x ^ 3)
```

> The cube map x ↦ x^3 is an automorphism on the multiplicative group because
> `Nat.coprime 3 (fieldSize - 1)` holds. We record the coprimality here.

`KoalaBear.coprime_three_fieldSize_sub_one` (lemma, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L155))

```lean
lemma coprime_three_fieldSize_sub_one : Nat.Coprime 3 (fieldSize - 1)
```

> Additional statements matching the Python spec API.

`KoalaBear.twoAdicity_maximal` (lemma, [line 165](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L165))

> `twoAdicity` is maximal: `2^(twoAdicity+1)` does not divide `fieldSize - 1`.

```lean
lemma twoAdicity_maximal : ¬ (2 ^ (twoAdicity + 1)) ∣ (fieldSize - 1)
```

`KoalaBear.twoAdicGenerators_pow_twoPow_eq_one` (lemma, [line 214](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L214))

> The power `(twoAdicGenerators[bits])^(2^bits) = 1`.

```lean
lemma twoAdicGenerators_pow_twoPow_eq_one (bits : Fin (twoAdicity + 1)) :
    twoAdicGenerators[bits] ^ (2 ^ (bits : Nat)) = 1
```

`KoalaBear.twoAdicGenerators_pow_twoPow_ne_one_of_lt` (lemma, [line 249](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L249))

> If `m < bits`, then `(twoAdicGenerators[bits])^(2^m) ≠ 1`.

```lean
lemma twoAdicGenerators_pow_twoPow_ne_one_of_lt
    {bits : Fin (twoAdicity + 1)} {m : Nat} (hm : m < bits) :
    (twoAdicGenerators[bits]) ^ (2 ^ m) ≠ (1 : Field)
```

`KoalaBear.isPrimitiveRoot_twoAdicGenerator` (lemma, [line 256](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L256))

> The precomputed element at index `bits` is a primitive `2^bits`-th root of unity.

```lean
lemma isPrimitiveRoot_twoAdicGenerator (n : Fin (twoAdicity + 1)) :
    IsPrimitiveRoot (twoAdicGenerators[n]) (2 ^ (n : Nat))
```

`KoalaBear.twoAdicGenerator_unit_mem_rootsOfUnity` (lemma, [line 276](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L276))

> As a unit, the precomputed element is a member of `rootsOfUnity (2^bits)`.

```lean
lemma twoAdicGenerator_unit_mem_rootsOfUnity
    (bits : Fin (twoAdicity + 1)) (h : twoAdicGenerators[bits] ≠ 0) :
    Units.mk0 (twoAdicGenerators[bits]) h ∈ rootsOfUnity (2 ^ (bits : Nat)) Field
```

`KoalaBear.twoAdicGenerators_order` (lemma, [line 285](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L285))

> The order of `twoAdicGenerators[bits]` equals `2^bits`.

```lean
lemma twoAdicGenerators_order (bits : Fin (twoAdicity + 1)) :
    orderOf (twoAdicGenerators[bits]) = 2 ^ (bits : Nat)
```

`KoalaBear.primitiveRoot` (definition, [line 296](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L296))

> Primitive generator used by the smooth field-root splitter.

```lean
def primitiveRoot : Field
```

`KoalaBear.primitiveRoot_order` (lemma, [line 326](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L326))

> The smooth field-root splitter generator has full multiplicative order.

```lean
lemma primitiveRoot_order : orderOf primitiveRoot = fieldSize - 1
```

`KoalaBear.smoothRootSchedule` (definition, [line 346](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L346))

> Smooth subgroup refinement schedule for `fieldSize - 1 = 2^24 * 127`.

```lean
def smoothRootSchedule : Array Nat
```

`KoalaBear.smoothRootSchedule_fold_eq_one` (lemma, [line 350](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean#L350))

> The KoalaBear smooth schedule refines the multiplicative group down to singleton cosets.

```lean
lemma smoothRootSchedule_fold_eq_one :
    smoothRootSchedule.toList.foldl (fun order ell ↦ order / ell) (fieldSize - 1) = 1
```

## Depends on

- [Non-binary fields and polynomial utilities](../basic.md)

## Proof depends on

- [The Lucas test for primes](../prattcertificate.md)

## Sources

- [CompPoly/Fields/KoalaBear/Basic.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Basic.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.KoalaBear.Basic.json)
