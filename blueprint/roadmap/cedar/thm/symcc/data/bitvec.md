---
catalog: module
lean: BitVec.toInt_ofInt64_toBitVec, BitVec.Int64_toBitVec_toInt_eq_toInt, BitVec.eq_iff_UInt64_toInt64_eq_64, BitVec.toInt_min_64, BitVec.toInt_max_64, BitVec.toInt_ge_INT64_MIN, BitVec.toInt_le_INT64_MAX, BitVec.signedMin_eq_INT64_MIN, BitVec.signedMax_eq_INT64_MAX, BitVec.toInt_ofInt_64, BitVec.overflows_false_64, BitVec.overflows_true_64, BitVec.Int64_ofInt?_eq_none_iff_overflows, BitVec.neg_toInt_eq_neg_64, BitVec.add_toInt_eq_add_64, BitVec.sub_toInt_eq_sub_64, BitVec.mul_eq_toInt_mul_ofInt_64, BitVec.mul_toInt_eq_mul_64, BitVec.mul_toInt_eq_toInt_mul, BitVec.sdiv_pos_lt_INT64_MAX, BitVec.sdiv_pos_gt_INT64_MIN, BitVec.toInt_sdiv_eq_tdiv_toInt, BitVec.sdiv_pos_bounded, BitVec.mul_toInt_sdiv_eq_toInt_mul_sdiv, BitVec.smtSDiv_eq_sdiv, BitVec.bvule_iff_le, Int.bmod_bounded_eq_self
statement: formalized
proof: formalized
---

# Bitvector utilities

`Cedar.Thm.SymCC.Data.BitVec`, in [Cedar/Thm/SymCC/Data/BitVec.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean).

> This file contains definitions and lemmas for working with bitvectors. These
> lemmas are true in general, but the general proofs are much harder. So, we prove
> them only for the specific bitwidths we need.

`BitVec.toInt_ofInt64_toBitVec` (theorem, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L39))

```lean
public theorem toInt_ofInt64_toBitVec {bv : BitVec 64} :
  (Int64.ofInt bv.toInt).toBitVec = bv
```

`BitVec.Int64_toBitVec_toInt_eq_toInt` (theorem, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L45))

```lean
public theorem Int64_toBitVec_toInt_eq_toInt (x : Int64) : x.toBitVec.toInt = x.toInt
```

`BitVec.eq_iff_UInt64_toInt64_eq_64` (theorem, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L47))

```lean
public theorem eq_iff_UInt64_toInt64_eq_64 {bv₁ bv₂ : BitVec 64} :
  bv₁ = bv₂ ↔ (UInt64.toInt64 {toBitVec := bv₁}) = (UInt64.toInt64 {toBitVec := bv₂})
```

`BitVec.toInt_min_64` (theorem, [line 55](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L55))

```lean
public theorem toInt_min_64 {bv : BitVec 64} :
  BitVec.signedMin 64 ≤ bv.toInt
```

`BitVec.toInt_max_64` (theorem, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L62))

```lean
public theorem toInt_max_64 {bv : BitVec 64} :
  bv.toInt ≤ BitVec.signedMax 64
```

`BitVec.toInt_ge_INT64_MIN` (theorem, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L69))

```lean
public theorem toInt_ge_INT64_MIN (bv : BitVec 64) :
  Int64.MIN ≤ bv.toInt
```

`BitVec.toInt_le_INT64_MAX` (theorem, [line 73](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L73))

```lean
public theorem toInt_le_INT64_MAX (bv : BitVec 64) :
  bv.toInt ≤ Int64.MAX
```

`BitVec.signedMin_eq_INT64_MIN` (theorem, [line 77](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L77))

```lean
public theorem signedMin_eq_INT64_MIN :
  BitVec.signedMin 64 = Int64.MIN
```

`BitVec.signedMax_eq_INT64_MAX` (theorem, [line 83](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L83))

```lean
public theorem signedMax_eq_INT64_MAX :
  BitVec.signedMax 64 = Int64.MAX
```

`BitVec.toInt_ofInt_64` (theorem, [line 90](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L90))

```lean
public theorem toInt_ofInt_64 {bv : BitVec 64} :
  BitVec.ofInt 64 (BitVec.toInt bv) = bv
```

`BitVec.overflows_false_64` (theorem, [line 100](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L100))

```lean
public theorem overflows_false_64 {i : Int} :
  Int64.MIN ≤ i ∧ i ≤ Int64.MAX ↔ BitVec.overflows 64 i = false
```

`BitVec.overflows_true_64` (theorem, [line 105](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L105))

```lean
public theorem overflows_true_64 {i : Int} :
  ¬ (Int64.MIN ≤ i ∧ i ≤ Int64.MAX) ↔ BitVec.overflows 64 i = true
```

`BitVec.Int64_ofInt?_eq_none_iff_overflows` (theorem, [line 111](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L111))

```lean
public theorem Int64_ofInt?_eq_none_iff_overflows {i : Int} :
  Int64.ofInt? i = none ↔ BitVec.overflows 64 i
```

`BitVec.neg_toInt_eq_neg_64` (theorem, [line 121](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L121))

```lean
public theorem neg_toInt_eq_neg_64 {bv : BitVec 64} {i : Int64}
  (h₁ : Int64.MIN ≤ -i.toInt ∧ -i.toInt ≤ Int64.MAX)
  (h₂ : BitVec.toInt bv = i.toInt) :
  BitVec.toInt (-bv) = -i.toInt
```

`BitVec.add_toInt_eq_add_64` (theorem, [line 131](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L131))

```lean
public theorem add_toInt_eq_add_64 {bv₁ bv₂ : BitVec 64} {i₁ i₂ : Int64}
  (h₀ : Int64.MIN ≤ i₁.toInt + i₂.toInt ∧ i₁.toInt + i₂.toInt ≤ Int64.MAX)
  (h₁ : BitVec.toInt bv₁ = i₁.toInt)
  (h₂ : BitVec.toInt bv₂ = i₂.toInt) :
  BitVec.toInt (bv₁ + bv₂) = i₁.toInt + i₂.toInt
```

`BitVec.sub_toInt_eq_sub_64` (theorem, [line 143](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L143))

```lean
public theorem sub_toInt_eq_sub_64 {bv₁ bv₂ : BitVec 64} {i₁ i₂ : Int64}
  (h₀ : Int64.MIN ≤ i₁.toInt - i₂.toInt ∧ i₁.toInt - i₂.toInt ≤ Int64.MAX)
  (h₁ : BitVec.toInt bv₁ = i₁.toInt)
  (h₂ : BitVec.toInt bv₂ = i₂.toInt) :
  BitVec.toInt (bv₁ - bv₂) = i₁.toInt - i₂.toInt
```

`BitVec.mul_eq_toInt_mul_ofInt_64` (theorem, [line 155](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L155))

```lean
public theorem mul_eq_toInt_mul_ofInt_64 {bv₁ bv₂ : BitVec 64} :
  bv₁ * bv₂ = BitVec.ofInt 64 (BitVec.toInt bv₁ * BitVec.toInt bv₂)
```

`BitVec.mul_toInt_eq_mul_64` (theorem, [line 173](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L173))

```lean
public theorem mul_toInt_eq_mul_64 {bv₁ bv₂ : BitVec 64} {i₁ i₂ : Int64}
  (h₀ : Int64.MIN ≤ i₁.toInt * i₂.toInt ∧ i₁.toInt * i₂.toInt ≤ Int64.MAX)
  (h₁ : BitVec.toInt bv₁ = i₁.toInt)
  (h₂ : BitVec.toInt bv₂ = i₂.toInt) :
  BitVec.toInt (bv₁ * bv₂) = i₁.toInt * i₂.toInt
```

`BitVec.mul_toInt_eq_toInt_mul` (theorem, [line 188](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L188))

```lean
public theorem mul_toInt_eq_toInt_mul {bv₁ bv₂ : BitVec 64}
  (h : Int64.MIN ≤ bv₁.toInt * bv₂.toInt ∧ bv₁.toInt * bv₂.toInt ≤ Int64.MAX) :
  BitVec.toInt (bv₁ * bv₂) = bv₁.toInt * bv₂.toInt
```

`BitVec.sdiv_pos_lt_INT64_MAX` (theorem, [line 276](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L276))

```lean
public theorem sdiv_pos_lt_INT64_MAX {bv₁ bv₂ : BitVec 64}
  (h : 1 < bv₂.toInt) :
  (bv₁.sdiv bv₂).toInt < Int64.MAX
```

`BitVec.sdiv_pos_gt_INT64_MIN` (theorem, [line 367](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L367))

```lean
public theorem sdiv_pos_gt_INT64_MIN {bv₁ bv₂ : BitVec 64}
  (h : 1 < bv₂.toInt) :
  Int64.MIN < (bv₁.sdiv bv₂).toInt
```

`BitVec.toInt_sdiv_eq_tdiv_toInt` (theorem, [line 425](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L425))

```lean
public theorem toInt_sdiv_eq_tdiv_toInt {bv₁ bv₂ : BitVec 64}
  (h₀ : 0 < bv₂.toInt) :
  BitVec.toInt (bv₁.sdiv bv₂) = bv₁.toInt.tdiv bv₂.toInt
```

`BitVec.sdiv_pos_bounded` (theorem, [line 514](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L514))

```lean
public theorem sdiv_pos_bounded {bv₁ bv₂ : BitVec 64}
  (h₀ : 0 < bv₂.toInt) :
  Int64.MIN.tdiv bv₂.toInt ≤ (bv₁.sdiv bv₂).toInt ∧ (bv₁.sdiv bv₂).toInt ≤ Int64.MAX.tdiv bv₂.toInt
```

`BitVec.mul_toInt_sdiv_eq_toInt_mul_sdiv` (theorem, [line 559](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L559))

```lean
public theorem mul_toInt_sdiv_eq_toInt_mul_sdiv {bv₁ bv₂ : BitVec 64}
  (h : 0 < bv₂.toInt) :
  bv₂.toInt * (bv₁.sdiv bv₂).toInt = (bv₂ * (bv₁.sdiv bv₂)).toInt
```

`BitVec.smtSDiv_eq_sdiv` (theorem, [line 570](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L570))

```lean
public theorem smtSDiv_eq_sdiv {n : Nat} {bv₁ bv₂ : BitVec n}
  (h : bv₂ ≠ 0) :
  bv₁.smtSDiv bv₂ = bv₁.sdiv bv₂
```

`BitVec.bvule_iff_le` (theorem, [line 578](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L578))

```lean
public theorem bvule_iff_le {n : Nat} {bv₁ bv₂ : BitVec n} :
  bv₁.ule bv₂ = decide (bv₁ ≤ bv₂)
```

`Int.bmod_bounded_eq_self` (theorem, [line 586](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean#L586))

```lean
public theorem Int.bmod_bounded_eq_self {n : Nat} {i : Int}
  (hlow : -2^n ≤ i)
  (hhigh : i ≤ 2^n - 1) :
  i.bmod (2^(n + 1)) = i
```

## Depends on

- [Int64](../../../data/int64.md)
- [Data](../../../symcc/part-01/data.md)

## Sources

- [Cedar/Thm/SymCC/Data/BitVec.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/BitVec.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Data.BitVec.json)
