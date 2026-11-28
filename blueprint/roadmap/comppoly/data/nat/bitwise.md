---
catalog: module
lean: ENat.le_floor_NNReal_iff, ENNReal.mul_inv_rev_ENNReal, ENNReal.coe_le_of_NNRat, ENNReal.coe_NNRat_coe_NNReal, ENNReal.coe_div_of_NNRat, ENNReal.coe_Nat_coe_NNRat, ENNReal.coe_NNRat_eq_coe_NNRat, Nat.max_eq_add_sub, Nat.sub_add_eq_sub_sub_rev, Nat.cast_gt_Real_one, Nat.sub_div_two_add_one_le, Nat.lt_add_of_pos_right_of_le, Nat.cast_div_le_div_cast_NNReal, Nat.two_mul_lt_iff_le_half_of_sub_one, Nat.dvd_of_pow_sub_one_dvd_pow_sub_one, Nat.getBit, Nat.testBit_true_eq_getBit_eq_1, Nat.testBit_eq_getBit, Nat.testBit_false_eq_getBit_eq_0, Nat.popCount, Nat.getBit_lt_2, Nat.getBit_eq_testBit, Nat.getBit_zero_eq_zero, Nat.getBit_eq_zero_or_one, Nat.getBit_zero_eq_self, Nat.getBit_zero_of_two_mul, Nat.getLowBits, Nat.getLowBits_zero_eq_zero, Nat.getLowBits_eq_mod_two_pow, Nat.getLowBits_lt_two_pow, Nat.getLowBits_le_self, Nat.and_eq_zero_iff, Nat.eq_iff_eq_all_getBits, Nat.shiftRight_and_one_distrib, Nat.and_eq_zero_iff_and_each_getBit_eq_zero, Nat.ge_two_pow_of_getBit_1, Nat.exists_ge_and_getBit_1_of_ge_two_pow, Nat.getBit_1_of_ge_two_pow_and_lt_two_pow_succ, Nat.getBit_two_pow, Nat.and_two_pow_eq_zero_of_getBit_0, Nat.and_two_pow_eq_two_pow_of_getBit_1, Nat.and_two_pow_eq_two_pow_of_getBit_eq_one, Nat.and_one_eq_of_eq, Nat.eq_zero_or_eq_one_of_lt_two, Nat.div_2_form, Nat.and_by_split_lowBits, Nat.xor_by_split_lowBits, Nat.or_by_split_lowBits, Nat.sum_eq_xor_plus_twice_and, Nat.add_shiftRight_distrib, Nat.sum_of_and_eq_zero_is_xor, Nat.xor_of_and_eq_zero_is_or, Nat.sum_of_and_eq_zero_is_or, Nat.xor_eq_sub_iff_submask, Nat.getBit_of_add_distrib, Nat.add_two_pow_of_getBit_eq_zero_lt_two_pow, Nat.getBit_of_multiple_of_power_of_two, Nat.getBit_of_shiftLeft, Nat.getBit_of_shiftRight, Nat.getBit_of_or, Nat.getBit_of_xor, Nat.getBit_of_and, Nat.getBit_of_two_pow_sub_one, Nat.getBit_of_sub_two_pow_of_bit_1, Nat.getBit_of_lowBits, Nat.getBit_eq_succ_getBit_of_mul_two, Nat.getBit_eq_succ_getBit_of_mul_two_add_one, Nat.getBit_eq_pred_getBit_of_div_two, Nat.getBit_repr, Nat.getBit_repr_univ, Nat.getBit_injective, Nat.getBit_repr_unique, Nat.getLowBits_succ, Nat.getHighBits_no_shl, Nat.getHighBits, Nat.and_highBits_lowBits_eq_zero, Nat.num_eq_highBits_add_lowBits, Nat.num_eq_highBits_xor_lowBits, Nat.getBit_of_highBits, Nat.getBit_of_highBits_no_shl, Nat.getBit_of_lt_two_pow, Nat.exist_bit_diff_if_diff, Nat.binaryFinMapToNat, Nat.getBit_of_binaryFinMapToNat, Nat.getMiddleBits, Nat.getBit_of_middleBits, Nat.getMiddleBits_lt_two_pow, Nat.getMiddleBits_eq_mod, Nat.and_shl_eq_zero_of_lt_two_pow, Nat.joinBits, Nat.getBit_joinBits, Nat.getLowBits_joinBits, Nat.getHighBits_no_shl_joinBits
statement: formalized
proof: formalized
---

# Bit operations on natural numbers

`CompPoly.Data.Nat.Bitwise`, in [CompPoly/Data/Nat/Bitwise.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean), by Chung Thai Nguyen, Quang Dao.

> Naming convention:
> - ..._getBit_1 or _eq_one : the value of getBit is 1 at the specified bit(s)
> - getBit_of_... : the value of getBit is the value of the specified bit(s), under some preconditions

`ENat.le_floor_NNReal_iff` (lemma, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L39))

```lean
lemma ENat.le_floor_NNReal_iff (x : ENat) (y : ℝ≥0) (hx_ne_top : x ≠ ⊤) :
    (x : ENat) ≤ ((Nat.floor y) : ENat) ↔ x.toNat ≤ Nat.floor y
```

`ENNReal.mul_inv_rev_ENNReal` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L57))

```lean
theorem ENNReal.mul_inv_rev_ENNReal {a b : ℕ} (ha : a ≠ 0) :
    ((a : ENNReal)⁻¹ * (b : ENNReal)⁻¹) = ((a : ENNReal) * (b : ENNReal))⁻¹
```

`ENNReal.coe_le_of_NNRat` (lemma, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L63))

```lean
lemma ENNReal.coe_le_of_NNRat {a b : ℚ≥0} : ((a : ENNReal)) ≤ (b) ↔ a ≤ b
```

`ENNReal.coe_NNRat_coe_NNReal` (lemma, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L66))

```lean
lemma ENNReal.coe_NNRat_coe_NNReal (x : ℚ≥0) : (x : ENNReal) = ((x : ℝ≥0) : ENNReal)
```

`ENNReal.coe_div_of_NNRat` (lemma, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L69))

```lean
lemma ENNReal.coe_div_of_NNRat {a b : ℚ≥0} (hb : b ≠ 0) :
    ((a : ENNReal) / (b : ENNReal)) = (((a / b) : ℚ≥0) : ENNReal)
```

`ENNReal.coe_Nat_coe_NNRat` (lemma, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L77))

```lean
lemma ENNReal.coe_Nat_coe_NNRat (x : ℕ) : (x : ENNReal) = ((x : ℚ≥0) : ENNReal)
```

`ENNReal.coe_NNRat_eq_coe_NNRat` (lemma, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L80))

```lean
lemma ENNReal.coe_NNRat_eq_coe_NNRat (x y : ℚ≥0) : (x : ENNReal) = (y : ENNReal) ↔ x = y
```

`Nat.max_eq_add_sub` (theorem, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L95))

```lean
theorem max_eq_add_sub {m n : Nat} : Nat.max m n = m + (n - m)
```

`Nat.sub_add_eq_sub_sub_rev` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L100))

```lean
theorem sub_add_eq_sub_sub_rev (a b c : Nat) (h1 : c ≤ b) (h2 : b ≤ a) :
    a - b + c = a - (b - c)
```

`Nat.cast_gt_Real_one` (lemma, [line 108](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L108))

```lean
lemma cast_gt_Real_one (a : ℕ) (ha : a > 1) : (a : ℝ) > 1
```

`Nat.sub_div_two_add_one_le` (lemma, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L114))

```lean
lemma sub_div_two_add_one_le (n k : ℕ) [NeZero n] [NeZero k] (hkn : k ≤ n) :
    (n - k) / 2 + 1 ≤ n
```

`Nat.lt_add_of_pos_right_of_le` (lemma, [line 127](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L127))

```lean
lemma lt_add_of_pos_right_of_le (a b c : ℕ) [NeZero c] (h : a ≤ b) : a < b + c
```

`Nat.cast_div_le_div_cast_NNReal` (lemma, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L132))

```lean
lemma cast_div_le_div_cast_NNReal (x y : ℕ) :
    ((x / y : ℕ) : ℝ≥0) ≤ (x : ℝ≥0) / (y : ℝ≥0)
```

`Nat.two_mul_lt_iff_le_half_of_sub_one` (theorem, [line 143](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L143))

```lean
theorem two_mul_lt_iff_le_half_of_sub_one (a b : ℕ) (h_b_pos : b > 0) :
    2 * a < b ↔ a ≤ (b - 1) / 2
```

`Nat.dvd_of_pow_sub_one_dvd_pow_sub_one` (lemma, [line 161](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L161))

> **Reverse Divisibility of Powers:**
> If `q > 1` and `q^d - 1` divides `q^n - 1`, then `d` must divide `n`.
> (This corresponds to the fact that cyclic subgroups are unique).

```lean
lemma dvd_of_pow_sub_one_dvd_pow_sub_one {q n d : ℕ} (hq : 1 < q)
    (h_dvd : q ^ d - 1 ∣ q ^ n - 1) : d ∣ n
```

`Nat.getBit` (definition, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L185))

> Returns the `k`-th least significant bit of a natural number `n` as a natural number (in `{0, 1}`).
>
> We decompose each number `j < 2^ℓ` into its binary representation : `j = Σ k ∈ Fin ℓ, jₖ * 2ᵏ`

```lean
def getBit (k n : Nat) : Nat
```

`Nat.testBit_true_eq_getBit_eq_1` (lemma, [line 187](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L187))

```lean
lemma testBit_true_eq_getBit_eq_1 (k n : Nat) : n.testBit k = ((Nat.getBit k n) = 1)
```

`Nat.testBit_eq_getBit` (lemma, [line 192](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L192))

```lean
lemma testBit_eq_getBit (k n : Nat) : (n.testBit k : Bool) = ((Nat.getBit k n) = 1)
```

`Nat.testBit_false_eq_getBit_eq_0` (lemma, [line 195](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L195))

```lean
lemma testBit_false_eq_getBit_eq_0 (k n : Nat) :
    (n.testBit k = false) = ((Nat.getBit k n) = 0)
```

`Nat.popCount` (definition, [line 202](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L202))

```lean
def popCount (n : Nat)
```

`Nat.getBit_lt_2` (lemma, [line 206](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L206))

```lean
lemma getBit_lt_2 {k n : Nat} : getBit k n < 2
```

`Nat.getBit_eq_testBit` (lemma, [line 211](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L211))

```lean
lemma getBit_eq_testBit (k n : Nat) : getBit k n = if n.testBit k then 1 else 0
```

`Nat.getBit_zero_eq_zero` (lemma, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L223))

```lean
lemma getBit_zero_eq_zero {k : Nat} : getBit k 0 = 0
```

`Nat.getBit_eq_zero_or_one` (lemma, [line 228](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L228))

```lean
lemma getBit_eq_zero_or_one {k n : Nat} :
    getBit k n = 0 ∨ getBit k n = 1
```

`Nat.getBit_zero_eq_self` (lemma, [line 234](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L234))

```lean
lemma getBit_zero_eq_self {n : ℕ} (h_n : n < 2) : getBit 0 n = n
```

`Nat.getBit_zero_of_two_mul` (lemma, [line 240](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L240))

```lean
lemma getBit_zero_of_two_mul {n : ℕ} : getBit 0 (2*n) = 0
```

`Nat.getLowBits` (definition, [line 245](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L245))

> Get the `numLowBits` least significant bits of `n`.

```lean
def getLowBits (numLowBits : ℕ) (n : ℕ)
```

`Nat.getLowBits_zero_eq_zero` (lemma, [line 247](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L247))

```lean
lemma getLowBits_zero_eq_zero {n : ℕ} : getLowBits 0 n = 0
```

`Nat.getLowBits_eq_mod_two_pow` (lemma, [line 251](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L251))

```lean
lemma getLowBits_eq_mod_two_pow {numLowBits : ℕ} (n : ℕ) :
    getLowBits numLowBits n = n % (2 ^ numLowBits)
```

`Nat.getLowBits_lt_two_pow` (lemma, [line 257](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L257))

```lean
lemma getLowBits_lt_two_pow {n : ℕ} (numLowBits : ℕ) :
    getLowBits numLowBits n < 2 ^ numLowBits
```

`Nat.getLowBits_le_self` (lemma, [line 262](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L262))

```lean
lemma getLowBits_le_self {n : ℕ} (numLowBits : ℕ) : getLowBits numLowBits n ≤ n
```

`Nat.and_eq_zero_iff` (lemma, [line 266](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L266))

```lean
lemma and_eq_zero_iff {n m : ℕ} : n &&& m = 0 ↔ ∀ k, (n >>> k) &&& (m >>> k) = 0
```

`Nat.eq_iff_eq_all_getBits` (lemma, [line 277](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L277))

```lean
lemma eq_iff_eq_all_getBits {n m : ℕ} : n = m ↔ ∀ k, getBit k n = getBit k m
```

`Nat.shiftRight_and_one_distrib` (lemma, [line 289](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L289))

```lean
lemma shiftRight_and_one_distrib {n m k : ℕ} :
    Nat.getBit k (n &&& m) = Nat.getBit k n &&& Nat.getBit k m
```

`Nat.and_eq_zero_iff_and_each_getBit_eq_zero` (lemma, [line 300](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L300))

```lean
lemma and_eq_zero_iff_and_each_getBit_eq_zero {n m : ℕ} :
    n &&& m = 0 ↔ ∀ k, Nat.getBit k n &&& Nat.getBit k m = 0
```

`Nat.ge_two_pow_of_getBit_1` (lemma, [line 319](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L319))

```lean
lemma ge_two_pow_of_getBit_1 {n i : ℕ} (h_getBit : Nat.getBit i n = 1) : n ≥ 2^i
```

`Nat.exists_ge_and_getBit_1_of_ge_two_pow` (lemma, [line 326](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L326))

```lean
lemma exists_ge_and_getBit_1_of_ge_two_pow {n x : Nat} (p : x ≥ 2 ^ n) :
    ∃ (i : Nat), i ≥ n ∧ Nat.getBit i x = 1
```

`Nat.getBit_1_of_ge_two_pow_and_lt_two_pow_succ` (lemma, [line 332](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L332))

```lean
lemma getBit_1_of_ge_two_pow_and_lt_two_pow_succ {x i : ℕ}
    (h_ge_two_pow : x ≥ 2 ^ i) (h_lt_two_pow_succ : x < 2 ^ (i + 1)) : Nat.getBit i x = 1
```

`Nat.getBit_two_pow` (lemma, [line 348](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L348))

```lean
lemma getBit_two_pow {i k : ℕ} : (getBit k (2^i) = if i == k then 1 else 0)
```

`Nat.and_two_pow_eq_zero_of_getBit_0` (lemma, [line 399](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L399))

```lean
lemma and_two_pow_eq_zero_of_getBit_0 {n i : ℕ} (h_getBit : getBit i n = 0) :
    n &&& (2 ^ i) = 0
```

`Nat.and_two_pow_eq_two_pow_of_getBit_1` (lemma, [line 415](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L415))

```lean
lemma and_two_pow_eq_two_pow_of_getBit_1 {n i : ℕ} (h_getBit: getBit i n = 1) :
    n &&& (2 ^ i) = 2 ^ i
```

`Nat.and_two_pow_eq_two_pow_of_getBit_eq_one` (lemma, [line 424](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L424))

```lean
lemma and_two_pow_eq_two_pow_of_getBit_eq_one {n i : ℕ} (h_getBit: getBit i n = 1) :
    n &&& (2 ^ i) = 2 ^ i
```

`Nat.and_one_eq_of_eq` (lemma, [line 444](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L444))

```lean
lemma and_one_eq_of_eq {a b : ℕ} : a = b → a &&& 1 = b &&& 1
```

`Nat.eq_zero_or_eq_one_of_lt_two` (lemma, [line 448](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L448))

```lean
lemma eq_zero_or_eq_one_of_lt_two {n : ℕ} (h_lt : n < 2) : n = 0 ∨ n = 1
```

`Nat.div_2_form` (lemma, [line 453](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L453))

```lean
lemma div_2_form {nD2 b : ℕ} (h_b : b < 2) :
    (nD2 * 2 + b) / 2 = nD2
```

`Nat.and_by_split_lowBits` (lemma, [line 457](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L457))

```lean
lemma and_by_split_lowBits {n m n1 m1 bn bm : ℕ} (h_bn : bn < 2) (h_bm : bm < 2)
    (h_n : n = n1 * 2 + bn) (h_m : m = m1 * 2 + bm) :
    n &&& m = (n1 &&& m1) * 2 + (bn &&& bm)
```

`Nat.xor_by_split_lowBits` (lemma, [line 486](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L486))

```lean
lemma xor_by_split_lowBits {n m n1 m1 bn bm : ℕ} (h_bn : bn < 2) (h_bm : bm < 2)
    (h_n : n = n1 * 2 + bn) (h_m : m = m1 * 2 + bm) :
    n ^^^ m = (n1 ^^^ m1) * 2 + (bn ^^^ bm)
```

`Nat.or_by_split_lowBits` (lemma, [line 517](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L517))

```lean
lemma or_by_split_lowBits {n m n1 m1 bn bm : ℕ} (h_bn : bn < 2) (h_bm : bm < 2)
    (h_n : n = n1 * 2 + bn) (h_m : m = m1 * 2 + bm) :
    n ||| m = (n1 ||| m1) * 2 + (bn ||| bm)
```

`Nat.sum_eq_xor_plus_twice_and` (lemma, [line 548](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L548))

```lean
lemma sum_eq_xor_plus_twice_and (n : Nat) : ∀ m : ℕ, n + m = (n ^^^ m) + 2 * (n &&& m)
```

`Nat.add_shiftRight_distrib` (lemma, [line 684](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L684))

```lean
lemma add_shiftRight_distrib {n m k : ℕ} (h_and_zero : n &&& m = 0) :
    (n + m) >>> k = (n >>> k) + (m >>> k)
```

`Nat.sum_of_and_eq_zero_is_xor` (lemma, [line 694](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L694))

```lean
lemma sum_of_and_eq_zero_is_xor {n m : ℕ} (h_n_AND_m : n &&& m = 0) : n + m = n ^^^ m
```

`Nat.xor_of_and_eq_zero_is_or` (lemma, [line 698](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L698))

```lean
lemma xor_of_and_eq_zero_is_or {n m : ℕ} (h_n_AND_m : n &&& m = 0) : n ^^^ m = n ||| m
```

`Nat.sum_of_and_eq_zero_is_or` (lemma, [line 724](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L724))

```lean
lemma sum_of_and_eq_zero_is_or {n m : ℕ} (h_n_AND_m : n &&& m = 0) : n + m = n ||| m
```

`Nat.xor_eq_sub_iff_submask` (lemma, [line 728](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L728))

```lean
lemma xor_eq_sub_iff_submask {n m : ℕ} (h: m ≤ n) : n ^^^ m = n - m ↔ n &&& m = m
```

`Nat.getBit_of_add_distrib` (lemma, [line 757](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L757))

```lean
lemma getBit_of_add_distrib {n m k : ℕ}
    (h_n_AND_m : n &&& m = 0) : getBit k (n + m) = getBit k n + getBit k m
```

`Nat.add_two_pow_of_getBit_eq_zero_lt_two_pow` (lemma, [line 774](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L774))

```lean
lemma add_two_pow_of_getBit_eq_zero_lt_two_pow {n m i : ℕ} (h_n: n < 2^m) (h_i: i < m)
    (h_getBit_at_i_eq_zero: getBit i n = 0) :
    n + 2^i < 2^m
```

`Nat.getBit_of_multiple_of_power_of_two` (lemma, [line 786](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L786))

```lean
lemma getBit_of_multiple_of_power_of_two {n p : ℕ} : ∀ k,
    getBit (k) (2^p * n) = if k < p then 0 else getBit (k-p) n
```

`Nat.getBit_of_shiftLeft` (lemma, [line 816](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L816))

```lean
lemma getBit_of_shiftLeft {n p : ℕ} :
    ∀ k, getBit (k) (n <<< p) = if k < p then 0 else getBit (k - p) n
```

`Nat.getBit_of_shiftRight` (lemma, [line 823](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L823))

```lean
lemma getBit_of_shiftRight {n p : ℕ} :
    ∀ k, getBit k (n >>> p) = getBit (k+p) n
```

`Nat.getBit_of_or` (lemma, [line 830](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L830))

```lean
lemma getBit_of_or {n m k: ℕ} : getBit k (n ||| m) = getBit k n ||| getBit k m
```

`Nat.getBit_of_xor` (lemma, [line 836](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L836))

```lean
lemma getBit_of_xor {n m k: ℕ} : getBit k (n ^^^ m) = getBit k n ^^^ getBit k m
```

`Nat.getBit_of_and` (lemma, [line 842](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L842))

```lean
lemma getBit_of_and {n m k: ℕ} : getBit k (n &&& m) = getBit k n &&& getBit k m
```

`Nat.getBit_of_two_pow_sub_one` (lemma, [line 849](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L849))

```lean
lemma getBit_of_two_pow_sub_one {i k: ℕ} :
    getBit k (2^i - 1) = if k < i then 1 else 0
```

`Nat.getBit_of_sub_two_pow_of_bit_1` (lemma, [line 863](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L863))

```lean
lemma getBit_of_sub_two_pow_of_bit_1 {n i j: ℕ} (h_getBit_eq_1: getBit i n = 1) :
    getBit j (n - 2^i) = (if j = i then 0 else getBit j n)
```

`Nat.getBit_of_lowBits` (lemma, [line 885](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L885))

```lean
lemma getBit_of_lowBits {n: ℕ} (numLowBits : ℕ) : ∀ k, getBit k (getLowBits numLowBits n) =
    if k < numLowBits then getBit k n else 0
```

`Nat.getBit_eq_succ_getBit_of_mul_two` (lemma, [line 912](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L912))

```lean
lemma getBit_eq_succ_getBit_of_mul_two {n k : ℕ} : getBit (k+1) (2*n) = getBit k n
```

`Nat.getBit_eq_succ_getBit_of_mul_two_add_one` (lemma, [line 918](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L918))

```lean
lemma getBit_eq_succ_getBit_of_mul_two_add_one {n k : ℕ} : getBit (k+1) (2*n + 1) = getBit k n
```

`Nat.getBit_eq_pred_getBit_of_div_two` (lemma, [line 924](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L924))

```lean
lemma getBit_eq_pred_getBit_of_div_two {n k : ℕ} (h_k: k > 0) :
    getBit k (n) = getBit (k-1) (n/2)
```

`Nat.getBit_repr` (theorem, [line 931](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L931))

```lean
theorem getBit_repr {ℓ : Nat} :
    ∀ j, j < 2^ℓ → j = ∑ k ∈ Finset.Icc 0 (ℓ-1), (getBit k j) * 2^k
```

`Nat.getBit_repr_univ` (theorem, [line 1056](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1056))

```lean
theorem getBit_repr_univ {ℓ : Nat} :
    ∀ j, j < 2^ℓ → j = ∑ k ∈ Finset.univ (α:=Fin ℓ), (getBit k j) * 2^k.val
```

`Nat.getBit_injective` (theorem, [line 1083](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1083))

> Two natural numbers with identical bits at every position are equal.

```lean
theorem getBit_injective (a b : ℕ) (h : ∀ k, getBit k a = getBit k b) : a = b
```

`Nat.getBit_repr_unique` (theorem, [line 1093](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1093))

> The binary representation of a number via `getBit` is unique: any sequence of
> 0/1 coefficients that sums to `j` must agree with `getBit` at each position.

```lean
theorem getBit_repr_unique {ℓ : ℕ} {j : ℕ} (h_j : j < 2 ^ ℓ)
    (c : ℕ → ℕ) (h_bin : ∀ k, k < ℓ → c k = 0 ∨ c k = 1)
    (h_sum : j = ∑ k ∈ Finset.Icc 0 (ℓ - 1), c k * 2 ^ k) :
    ∀ k, k < ℓ → c k = getBit k j
```

`Nat.getLowBits_succ` (lemma, [line 1154](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1154))

```lean
lemma getLowBits_succ {n: ℕ} (numLowBits: ℕ) :
    getLowBits (numLowBits + 1) n = getLowBits numLowBits n
    + (getBit numLowBits n) <<< numLowBits
```

`Nat.getHighBits_no_shl` (definition, [line 1222](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1222))

> This takes a argument for the number of lowBitss to remove from the number

```lean
def getHighBits_no_shl (numLowBits : ℕ) (n : ℕ) : ℕ
```

`Nat.getHighBits` (definition, [line 1224](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1224))

```lean
def getHighBits (numLowBits : ℕ) (n : ℕ) : ℕ
```

`Nat.and_highBits_lowBits_eq_zero` (theorem, [line 1227](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1227))

```lean
theorem and_highBits_lowBits_eq_zero {n : ℕ} (numLowBits : ℕ) :
    getHighBits numLowBits n &&& getLowBits numLowBits n = 0
```

`Nat.num_eq_highBits_add_lowBits` (lemma, [line 1251](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1251))

```lean
lemma num_eq_highBits_add_lowBits {n: ℕ} (numLowBits: ℕ) :
    n = getHighBits numLowBits n + getLowBits numLowBits n
```

`Nat.num_eq_highBits_xor_lowBits` (lemma, [line 1278](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1278))

```lean
lemma num_eq_highBits_xor_lowBits {n: ℕ} (numLowBits: ℕ) :
    n = getHighBits numLowBits n ^^^ getLowBits numLowBits n
```

`Nat.getBit_of_highBits` (lemma, [line 1284](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1284))

```lean
lemma getBit_of_highBits {n: ℕ} (numLowBits : ℕ) :
    ∀ k, getBit k (getHighBits numLowBits n) = if k < numLowBits then 0 else getBit (k) (n)
```

`Nat.getBit_of_highBits_no_shl` (lemma, [line 1296](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1296))

```lean
lemma getBit_of_highBits_no_shl {n: ℕ} (numLowBits : ℕ) :
    ∀ k, getBit k (getHighBits_no_shl numLowBits n) = getBit (k + numLowBits) (n)
```

`Nat.getBit_of_lt_two_pow` (lemma, [line 1302](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1302))

```lean
lemma getBit_of_lt_two_pow {n: ℕ} (a: Fin (2^n)) (k: ℕ) :
    getBit k a = if k < n then getBit k a else 0
```

`Nat.exist_bit_diff_if_diff` (lemma, [line 1316](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1316))

```lean
lemma exist_bit_diff_if_diff {n: ℕ} (a: Fin (2^n)) (b: Fin (2^n)) (h_a_ne_b: a ≠ b) :
    ∃ k: Fin n, getBit k a ≠ getBit k b
```

`Nat.binaryFinMapToNat` (definition, [line 1338](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1338))

```lean
def binaryFinMapToNat {n : ℕ} (m : Fin n → ℕ) (h_binary : ∀ j: Fin n, m j ≤ 1) : Fin (2^n)
```

`Nat.getBit_of_binaryFinMapToNat` (lemma, [line 1365](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1365))

```lean
lemma getBit_of_binaryFinMapToNat {n : ℕ} (m : Fin n → ℕ) (h_binary: ∀ j: Fin n, m j ≤ 1) :
    ∀ k: ℕ, Nat.getBit k (binaryFinMapToNat m h_binary).val
      = if h_k: k < n then m ⟨k, by omega⟩ else 0
```

`Nat.getMiddleBits` (definition, [line 1454](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1454))

> Middle bits: take `len` bits starting at `offset` from `n`.

```lean
def getMiddleBits (offset len n : ℕ) : ℕ
```

`Nat.getBit_of_middleBits` (lemma, [line 1458](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1458))

> Bit-level characterization of middle bits.

```lean
lemma getBit_of_middleBits {n offset len k : ℕ} :
    getBit k (getMiddleBits offset len n) = if k < len then getBit (k + offset) n else 0
```

`Nat.getMiddleBits_lt_two_pow` (lemma, [line 1465](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1465))

> Middle bits are strictly less than `2^len`.

```lean
lemma getMiddleBits_lt_two_pow {n offset len : ℕ} :
    getMiddleBits offset len n < 2 ^ len
```

`Nat.getMiddleBits_eq_mod` (lemma, [line 1471](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1471))

> Middle bits as a modulus form.

```lean
lemma getMiddleBits_eq_mod {n offset len : ℕ} :
    getMiddleBits offset len n = (n >>> offset) % (2 ^ len)
```

`Nat.and_shl_eq_zero_of_lt_two_pow` (lemma, [line 1476](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1476))

```lean
lemma and_shl_eq_zero_of_lt_two_pow {a n b : ℕ} (hb : b < 2 ^ n) : (a <<< n) &&& b = 0
```

`Nat.joinBits` (definition, [line 1486](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1486))

> Concatenate high (length m) and low (length n) using shifts.

```lean
def joinBits {n m : ℕ} (low : Fin (2 ^ n)) (high : Fin (2 ^ m)) : Fin (2 ^ (m+n))
```

`Nat.getBit_joinBits` (lemma, [line 1502](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1502))

> Bit characterization: below cut use low, above cut use high.

```lean
lemma getBit_joinBits {n m k : ℕ} (low : Fin (2 ^ n)) (high : Fin (2 ^ m)) :
    getBit k (joinBits low high).val = if k < n then getBit k low.val
      else getBit (k - n) high.val
```

`Nat.getLowBits_joinBits` (lemma, [line 1515](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1515))

> Low n bits of joinBits are exactly low.

```lean
lemma getLowBits_joinBits {n m : ℕ} (low : Fin (2 ^ n)) (high : Fin (2 ^ m)) :
    getLowBits n (joinBits low high).val = low.val
```

`Nat.getHighBits_no_shl_joinBits` (lemma, [line 1527](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean#L1527))

> Dropping low n bits by shifting right recovers high.

```lean
lemma getHighBits_no_shl_joinBits {n m : ℕ} (low : Fin (2 ^ n)) (high : Fin (2 ^ m)) :
    getHighBits_no_shl n (joinBits low high).val = high.val
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Proof depends on

- [More lemmas about Fin and big operators](../fin/bigoperators.md)

## Sources

- [CompPoly/Data/Nat/Bitwise.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Nat/Bitwise.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Nat.Bitwise.json)
