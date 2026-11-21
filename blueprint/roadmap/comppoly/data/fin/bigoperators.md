---
catalog: module
lean: mul_two_add_bit_lt_two_pow, div_two_pow_lt_two_pow, lt_two_pow_of_lt_two_pow_exp_le, Fin.val_add_one', Fin.cast_val_eq_val, Fin.val_sub_one, Fin.lt_iff_le_pred, Fin.le_iff_lt_succ, Fin.lt_succ', Fin.le_succ, Fin.succRecOnSameFinType, Fin.predRecOnSameFinType, Fin.sum_univ_split_even_add_odd, Fin.sum_univ_pow_two_even_add_odd, sum_Icc_split, equivFinFunSplitLast
statement: formalized
proof: formalized
---

# More lemmas about Fin and big operators

`CompPoly.Data.Fin.BigOperators`, in [CompPoly/Data/Fin/BigOperators.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean), by Chung Thai Nguyen, Quang Dao.

`mul_two_add_bit_lt_two_pow` (theorem, [line 21](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean#L21))

```lean
theorem mul_two_add_bit_lt_two_pow (a b c : ℕ) (i : Fin 2)
    (h_a : a < 2 ^ b) (h_b : b < c) :
    a * 2 + i.val < 2^c
```

`div_two_pow_lt_two_pow` (theorem, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean#L44))

```lean
theorem div_two_pow_lt_two_pow (x i j : ℕ) (h_x_lt_2_pow_i : x < 2 ^ (i + j)): x / 2^j < 2^(i)
```

`lt_two_pow_of_lt_two_pow_exp_le` (lemma, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean#L57))

```lean
lemma lt_two_pow_of_lt_two_pow_exp_le (x i j: ℕ)
    (h_x_lt_2_pow_i: x < 2^i) (h_i_le_j: i ≤ j): x < 2^j
```

`Fin.val_add_one'` (lemma, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean#L65))

```lean
lemma Fin.val_add_one' (a : Fin r) (h_a_add_1 : a + 1 < r) : (a + 1).val = a.val + 1
```

`Fin.cast_val_eq_val` (theorem, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean#L72))

```lean
theorem Fin.cast_val_eq_val {n m : ℕ} [NeZero n] (a : Fin n) (h_eq : n = m):
    (Fin.cast (h_eq) a).val = a.val
```

`Fin.val_sub_one` (lemma, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean#L77))

```lean
lemma Fin.val_sub_one (a : Fin r) (h_a_sub_1 : a > 0) : (a - 1).val = a.val - 1
```

`Fin.lt_iff_le_pred` (lemma, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean#L80))

```lean
lemma Fin.lt_iff_le_pred (a b : Fin r) (h_b : b > 0) : a < b ↔ a ≤ b - 1
```

`Fin.le_iff_lt_succ` (lemma, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean#L90))

```lean
lemma Fin.le_iff_lt_succ (a b : Fin r) (h_b : b + 1 < r) : a ≤ b ↔ a < b + 1
```

`Fin.lt_succ'` (lemma, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean#L100))

```lean
lemma Fin.lt_succ' (a : Fin r) (h_a_add_1 : a + 1 < r) : a < a + 1
```

`Fin.le_succ` (lemma, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean#L105))

```lean
lemma Fin.le_succ (a : Fin r) (h_a_add_1 : a + 1 < r) : a ≤ a + 1
```

`Fin.succRecOnSameFinType` (definition, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean#L114))

> Recursion principle for `Fin r` that iterates upwards from `0`.
> This is useful when the type `Fin r` is fixed and we want to induct on the element.
> It's similar to `Fin.inductionOn`, but formulated with an explicit upper bound check.

```lean
def Fin.succRecOnSameFinType {motive : Fin r → Sort _}
    (zero : motive (⟨0, Nat.pos_of_neZero r⟩ : Fin r))
    (succ : ∀ i : Fin r, i + 1 < r → motive i → motive (i + 1)) : ∀ (i : Fin r), motive i
  | ⟨0, _⟩ => by exact zero
  | ⟨Nat.succ i_val, h⟩ => by -- ⊢ motive ⟨i_val.succ, h⟩
    simp only [Nat.succ_eq_add_one] at h
    set i : Fin r
```

`Fin.predRecOnSameFinType` (definition, [line 143](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean#L143))

> Recursion principle for `Fin r` that iterates downwards from `r - 1`.
> This is useful for definitions that process elements in reverse order, like `foldr`.

```lean
def Fin.predRecOnSameFinType {motive : Fin r → Sort _}
    (last : motive (⟨r - 1, by
      have h_r_ne_0: r ≠ 0 := by exact NeZero.ne r
      omega
    ⟩ : Fin r))
    (succ : ∀ i : Fin r, i.val > 0 → motive i → motive (⟨i.val - 1, by omega⟩ : Fin r))
    (i : Fin r): motive i
```

`Fin.sum_univ_split_even_add_odd` (theorem, [line 178](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean#L178))

> Splits a sum over `Fin (2 * r)` into a sum over even indices and a sum over odd indices.
> Useful for Fast Fourier Transform (FFT) type recursions.

```lean
theorem Fin.sum_univ_split_even_add_odd {r : ℕ} {M : Type*} [AddCommMonoid M]
    (f : Fin (2 * r) → M) :
    ∑ i : Fin (2 * r), f i
    = (∑ i : Fin r, f ⟨2 * i.val, by have := i.isLt; omega⟩)
    + (∑ i : Fin r, f ⟨2 * i.val + 1, by have := i.isLt; omega⟩)
```

`Fin.sum_univ_pow_two_even_add_odd` (theorem, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean#L227))

> Specialized form of `Fin.sum_univ_split_even_add_odd` for `r = 2 ^ n`.

```lean
theorem Fin.sum_univ_pow_two_even_add_odd {n : ℕ} {M : Type*} [AddCommMonoid M] (f : ℕ → M) :
    (∑ i : Fin (2 ^ n), f (2 * i)) + (∑ i : Fin (2 ^ n), f (2 * i + 1))
    = ∑ i : Fin (2 ^ (n + 1)), f i
```

`sum_Icc_split` (theorem, [line 237](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean#L237))

> Splits a sum over an interval `[a, c]` into two sums over `[a, b]` and `[b+1, c]`.
> Requires `a ≤ b ≤ c`.

```lean
theorem sum_Icc_split {α : Type*} [AddCommMonoid α] (f : ℕ → α) (a b c : ℕ)
    (h₁ : a ≤ b) (h₂ : b ≤ c):
    ∑ i ∈ Finset.Icc a c, f i = ∑ i ∈ Finset.Icc a b, f i + ∑ i ∈ Finset.Icc (b+1) c, f i
```

`equivFinFunSplitLast` (definition, [line 280](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean#L280))

```lean
def equivFinFunSplitLast {F : Type*} [Fintype F] [Nonempty F] {ϑ : ℕ} :
    (Fin (ϑ + 1) → F) ≃ (F × (Fin ϑ → F))
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Data/Fin/BigOperators.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Fin/BigOperators.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Fin.BigOperators.json)
