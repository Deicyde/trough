---
catalog: module
lean: Nat.recAux_zero, Nat.recAux_succ, Nat.recAuxOn_zero, Nat.recAuxOn_succ, Nat.casesAuxOn_zero, Nat.casesAuxOn_succ, Nat.strongRec_eq, Nat.strongRecOn_eq, Nat.recDiagAux_zero_left, Nat.recDiagAux_zero_right, Nat.recDiagAux_succ_succ, Nat.recDiag_zero_zero, Nat.recDiag_zero_succ, Nat.recDiag_succ_zero, Nat.recDiag_succ_succ, Nat.recDiagOn_zero_zero, Nat.recDiagOn_zero_succ, Nat.recDiagOn_succ_zero, Nat.recDiagOn_succ_succ, Nat.casesDiagOn_zero_zero, Nat.casesDiagOn_zero_succ, Nat.casesDiagOn_succ_zero, Nat.casesDiagOn_succ_succ, Nat.lt_sum_ge, Nat.sum_trichotomy, Nat.div_le_div_of_lt, Nat.le_of_div_lt_div, Nat.mod_lt_mod_of_lt_of_div_eq, Nat.mod_le_mod_of_le_of_div_eq, Nat.lt_of_div_eq_of_mod_lt, Nat.le_of_div_eq_of_mod_le, Nat.lt_div_mod_iff, Nat.le_div_mod_iff, Nat.mkDivMod_def, Nat.div_mkDivMod, Nat.mod_mkDivMod, Nat.cast_mkDivMod, Nat.mkDivMod_div_add_mod, Nat.mkDivMod_div, Nat.mkDivMod_div_cast, Nat.mul_le_mkDivMod, Nat.mkDivMod_lt_mul_succ, Nat.mkDivMod_lt_mul_of_lt, Nat.mkDivMod_inj, Nat.mkDivMod_lt_mkDivMod_iff, Nat.mkDivMod_le_mkDivMod_iff, Nat.ofBits_zero, Nat.ofBits_succ, Nat.ofBits_lt_two_pow, Nat.testBit_ofBits_lt, Nat.testBit_ofBits_ge, Nat.testBit_ofBits, Nat.ofBits_testBit, Nat.toString_append_toString, Nat.mul_add_lt_mul_of_lt_of_lt, Nat.add_mul_lt_mul_of_lt_of_lt
statement: formalized
proof: formalized
---

# Basic lemmas about natural numbers

`Batteries.Data.Nat.Lemmas`, in [Batteries/Data/Nat/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean), by Leonardo de Moura, Jeremy Avigad, Mario Carneiro.

> The primary purpose of the lemmas in this file is to assist with reasoning
> about sizes of objects, array indices and such. For a more thorough development
> of the theory of natural numbers, we recommend using Mathlib.

> ### rec/cases

`Nat.recAux_zero` (theorem, [line 23](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L23))

```lean
theorem recAux_zero {motive : Nat → Sort _} (zero : motive 0)
    (succ : ∀ n, motive n → motive (n+1)) :
    Nat.recAux zero succ 0 = zero
```

`Nat.recAux_succ` (theorem, [line 27](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L27))

```lean
theorem recAux_succ {motive : Nat → Sort _} (zero : motive 0)
    (succ : ∀ n, motive n → motive (n+1)) (n) :
    Nat.recAux zero succ (n+1) = succ n (Nat.recAux zero succ n)
```

`Nat.recAuxOn_zero` (theorem, [line 31](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L31))

```lean
theorem recAuxOn_zero {motive : Nat → Sort _} (zero : motive 0)
    (succ : ∀ n, motive n → motive (n+1)) :
    Nat.recAuxOn 0 zero succ = zero
```

`Nat.recAuxOn_succ` (theorem, [line 35](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L35))

```lean
theorem recAuxOn_succ {motive : Nat → Sort _} (zero : motive 0)
    (succ : ∀ n, motive n → motive (n+1)) (n) :
    Nat.recAuxOn (n+1) zero succ = succ n (Nat.recAuxOn n zero succ)
```

`Nat.casesAuxOn_zero` (theorem, [line 39](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L39))

```lean
theorem casesAuxOn_zero {motive : Nat → Sort _} (zero : motive 0)
    (succ : ∀ n, motive (n+1)) :
    Nat.casesAuxOn 0 zero succ = zero
```

`Nat.casesAuxOn_succ` (theorem, [line 43](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L43))

```lean
theorem casesAuxOn_succ {motive : Nat → Sort _} (zero : motive 0)
    (succ : ∀ n, motive (n+1)) (n) :
    Nat.casesAuxOn (n+1) zero succ = succ n
```

`Nat.strongRec_eq` (theorem, [line 47](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L47))

```lean
theorem strongRec_eq {motive : Nat → Sort _} (ind : ∀ n, (∀ m, m < n → motive m) → motive n)
    (t : Nat) : Nat.strongRec ind t = ind t fun m _ => Nat.strongRec ind m
```

`Nat.strongRecOn_eq` (theorem, [line 51](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L51))

```lean
theorem strongRecOn_eq {motive : Nat → Sort _} (ind : ∀ n, (∀ m, m < n → motive m) → motive n)
    (t : Nat) : Nat.strongRecOn t ind = ind t fun m _ => Nat.strongRecOn m ind
```

`Nat.recDiagAux_zero_left` (theorem, [line 55](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L55))

```lean
theorem recDiagAux_zero_left {motive : Nat → Nat → Sort _}
    (zero_left : ∀ n, motive 0 n) (zero_right : ∀ m, motive m 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (n) :
    Nat.recDiagAux zero_left zero_right succ_succ 0 n = zero_left n
```

`Nat.recDiagAux_zero_right` (theorem, [line 60](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L60))

```lean
theorem recDiagAux_zero_right {motive : Nat → Nat → Sort _}
    (zero_left : ∀ n, motive 0 n) (zero_right : ∀ m, motive m 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (m)
    (h : zero_left 0 = zero_right 0 := by first | assumption | trivial) :
    Nat.recDiagAux zero_left zero_right succ_succ m 0 = zero_right m
```

`Nat.recDiagAux_succ_succ` (theorem, [line 66](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L66))

```lean
theorem recDiagAux_succ_succ {motive : Nat → Nat → Sort _}
    (zero_left : ∀ n, motive 0 n) (zero_right : ∀ m, motive m 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (m n) :
    Nat.recDiagAux zero_left zero_right succ_succ (m+1) (n+1)
      = succ_succ m n (Nat.recDiagAux zero_left zero_right succ_succ m n)
```

`Nat.recDiag_zero_zero` (theorem, [line 72](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L72))

```lean
theorem recDiag_zero_zero {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 n → motive 0 (n+1)) (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) :
    Nat.recDiag (motive:=motive) zero_zero zero_succ succ_zero succ_succ 0 0 = zero_zero
```

`Nat.recDiag_zero_succ` (theorem, [line 77](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L77))

```lean
theorem recDiag_zero_succ {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 n → motive 0 (n+1)) (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (n) :
    Nat.recDiag zero_zero zero_succ succ_zero succ_succ 0 (n+1)
      = zero_succ n (Nat.recDiag zero_zero zero_succ succ_zero succ_succ 0 n)
```

`Nat.recDiag_succ_zero` (theorem, [line 84](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L84))

```lean
theorem recDiag_succ_zero {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 n → motive 0 (n+1)) (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (m) :
    Nat.recDiag zero_zero zero_succ succ_zero succ_succ (m+1) 0
      = succ_zero m (Nat.recDiag zero_zero zero_succ succ_zero succ_succ m 0)
```

`Nat.recDiag_succ_succ` (theorem, [line 91](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L91))

```lean
theorem recDiag_succ_succ {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 n → motive 0 (n+1)) (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (m n) :
    Nat.recDiag zero_zero zero_succ succ_zero succ_succ (m+1) (n+1)
      = succ_succ m n (Nat.recDiag zero_zero zero_succ succ_zero succ_succ m n)
```

`Nat.recDiagOn_zero_zero` (theorem, [line 97](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L97))

```lean
theorem recDiagOn_zero_zero {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 n → motive 0 (n+1)) (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) :
    Nat.recDiagOn (motive:=motive) 0 0 zero_zero zero_succ succ_zero succ_succ = zero_zero
```

`Nat.recDiagOn_zero_succ` (theorem, [line 102](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L102))

```lean
theorem recDiagOn_zero_succ {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 n → motive 0 (n+1)) (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (n) :
    Nat.recDiagOn 0 (n+1) zero_zero zero_succ succ_zero succ_succ
      = zero_succ n (Nat.recDiagOn 0 n zero_zero zero_succ succ_zero succ_succ)
```

`Nat.recDiagOn_succ_zero` (theorem, [line 109](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L109))

```lean
theorem recDiagOn_succ_zero {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 n → motive 0 (n+1)) (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (m) :
    Nat.recDiagOn (m+1) 0 zero_zero zero_succ succ_zero succ_succ
      = succ_zero m (Nat.recDiagOn m 0 zero_zero zero_succ succ_zero succ_succ)
```

`Nat.recDiagOn_succ_succ` (theorem, [line 116](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L116))

```lean
theorem recDiagOn_succ_succ {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 n → motive 0 (n+1)) (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (m n) :
    Nat.recDiagOn (m+1) (n+1) zero_zero zero_succ succ_zero succ_succ
      = succ_succ m n (Nat.recDiagOn m n zero_zero zero_succ succ_zero succ_succ)
```

`Nat.casesDiagOn_zero_zero` (theorem, [line 122](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L122))

```lean
theorem casesDiagOn_zero_zero {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 (n+1)) (succ_zero : ∀ m, motive (m+1) 0)
    (succ_succ : ∀ m n, motive (m+1) (n+1)) :
    Nat.casesDiagOn 0 0 (motive:=motive) zero_zero zero_succ succ_zero succ_succ = zero_zero
```

`Nat.casesDiagOn_zero_succ` (theorem, [line 127](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L127))

```lean
theorem casesDiagOn_zero_succ {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 (n+1)) (succ_zero : ∀ m, motive (m+1) 0)
    (succ_succ : ∀ m n, motive (m+1) (n+1)) (n) :
    Nat.casesDiagOn 0 (n+1) zero_zero zero_succ succ_zero succ_succ = zero_succ n
```

`Nat.casesDiagOn_succ_zero` (theorem, [line 132](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L132))

```lean
theorem casesDiagOn_succ_zero {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 (n+1)) (succ_zero : ∀ m, motive (m+1) 0)
    (succ_succ : ∀ m n, motive (m+1) (n+1)) (m) :
    Nat.casesDiagOn (m+1) 0 zero_zero zero_succ succ_zero succ_succ = succ_zero m
```

`Nat.casesDiagOn_succ_succ` (theorem, [line 137](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L137))

```lean
theorem casesDiagOn_succ_succ {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 (n+1)) (succ_zero : ∀ m, motive (m+1) 0)
    (succ_succ : ∀ m n, motive (m+1) (n+1)) (m n) :
    Nat.casesDiagOn (m+1) (n+1) zero_zero zero_succ succ_zero succ_succ = succ_succ m n
```

> ## strong case

`Nat.lt_sum_ge` (definition, [line 145](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L145))

> Strong case analysis on `a < b ∨ b ≤ a`

```lean
protected def lt_sum_ge (a b : Nat) : a < b ⊕' b ≤ a
```

`Nat.sum_trichotomy` (definition, [line 149](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L149))

> Strong case analysis on `a < b ∨ a = b ∨ b < a`

```lean
protected def sum_trichotomy (a b : Nat) : a < b ⊕' a = b ⊕' b < a
```

> ### div/mod

`Nat.div_le_div_of_lt` (theorem, [line 161](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L161))

```lean
theorem div_le_div_of_lt {a b : Nat} (n : Nat) (h : a < b) : a / n ≤ b / n
```

`Nat.le_of_div_lt_div` (theorem, [line 164](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L164))

```lean
theorem le_of_div_lt_div {n a b : Nat} (h : a / n < b / n) : a ≤ b
```

`Nat.mod_lt_mod_of_lt_of_div_eq` (theorem, [line 167](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L167))

```lean
theorem mod_lt_mod_of_lt_of_div_eq {n a b : Nat} (h : a < b) (h0 : a / n = b / n) :
    a % n < b % n
```

`Nat.mod_le_mod_of_le_of_div_eq` (theorem, [line 170](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L170))

```lean
theorem mod_le_mod_of_le_of_div_eq {n a b : Nat} (h : a ≤ b) (h0 : a / n = b / n) :
    a % n ≤ b % n
```

`Nat.lt_of_div_eq_of_mod_lt` (theorem, [line 173](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L173))

```lean
theorem lt_of_div_eq_of_mod_lt {n a b : Nat} (h0 : a / n = b / n) (h1 : a % n < b % n) : a < b
```

`Nat.le_of_div_eq_of_mod_le` (theorem, [line 176](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L176))

```lean
theorem le_of_div_eq_of_mod_le {n a b : Nat} (h0 : a / n = b / n) (h1 : a % n ≤ b % n) : a ≤ b
```

`Nat.lt_div_mod_iff` (theorem, [line 179](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L179))

```lean
theorem lt_div_mod_iff (n a b : Nat) :
    a < b ↔ a / n < b / n ∨ a / n = b / n ∧ a % n < b % n
```

`Nat.le_div_mod_iff` (theorem, [line 185](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L185))

```lean
theorem le_div_mod_iff (n a b : Nat) :
    a ≤ b ↔ a / n < b / n ∨ a / n = b / n ∧ a % n ≤ b % n
```

> ### mkDivMod

`Nat.mkDivMod_def` (theorem, [line 193](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L193))

```lean
theorem mkDivMod_def (i : Nat) {n} (j : Fin n) : mkDivMod i j = n * i + j
```

`Nat.div_mkDivMod` (theorem, [line 195](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L195))

```lean
theorem div_mkDivMod (i : Nat) {n} (j : Fin n) :
    mkDivMod i j / n = i
```

`Nat.mod_mkDivMod` (theorem, [line 199](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L199))

```lean
theorem mod_mkDivMod (i : Nat) {n} (j : Fin n) :
    mkDivMod i j % n = j
```

`Nat.cast_mkDivMod` (theorem, [line 203](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L203))

```lean
theorem cast_mkDivMod (i : Nat) {n : Nat} (j : Fin n) :
    haveI : NeZero n := ⟨Nat.ne_zero_of_lt j.isLt⟩
    (mkDivMod i j : Fin n) = j
```

`Nat.mkDivMod_div_add_mod` (theorem, [line 207](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L207))

```lean
theorem mkDivMod_div_add_mod (k : Nat) {n} (j : Fin n) :
    mkDivMod (k / n) j + k % n = k + j
```

`Nat.mkDivMod_div` (theorem, [line 211](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L211))

```lean
theorem mkDivMod_div (k : Nat) {n} (j : Fin n) : mkDivMod (k / n) j = k + j - k % n
```

`Nat.mkDivMod_div_cast` (theorem, [line 215](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L215))

```lean
theorem mkDivMod_div_cast (k : Nat) {n : Nat} [NeZero n] :
    mkDivMod (k / n) (k : Fin n) = k
```

`Nat.mul_le_mkDivMod` (theorem, [line 218](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L218))

```lean
theorem mul_le_mkDivMod (i : Nat) {n} (j : Fin n) : n * i ≤ mkDivMod i j
```

`Nat.mkDivMod_lt_mul_succ` (theorem, [line 220](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L220))

```lean
theorem mkDivMod_lt_mul_succ (i : Nat) {n} (j : Fin n) : mkDivMod i j < n * (i + 1)
```

`Nat.mkDivMod_lt_mul_of_lt` (theorem, [line 223](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L223))

```lean
theorem mkDivMod_lt_mul_of_lt {i m : Nat} {n} (h : i < m) (j : Fin n) : mkDivMod i j < m * n
```

`Nat.mkDivMod_inj` (theorem, [line 226](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L226))

```lean
theorem mkDivMod_inj {i₁ i₂ : Nat} {n} {j₁ j₂ : Fin n} :
    mkDivMod i₁ j₁ = mkDivMod i₂ j₂ ↔ i₁ = i₂ ∧ j₁ = j₂
```

`Nat.mkDivMod_lt_mkDivMod_iff` (theorem, [line 230](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L230))

```lean
theorem mkDivMod_lt_mkDivMod_iff {i₁ i₂ : Nat} {n} {j₁ j₂ : Fin n} :
    mkDivMod i₁ j₁ < mkDivMod i₂ j₂ ↔ i₁ < i₂ ∨ i₁ = i₂ ∧ j₁ < j₂
```

`Nat.mkDivMod_le_mkDivMod_iff` (theorem, [line 234](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L234))

```lean
theorem mkDivMod_le_mkDivMod_iff {i₁ i₂ : Nat} {n} {j₁ j₂ : Fin n} :
    mkDivMod i₁ j₁ ≤ mkDivMod i₂ j₂ ↔ i₁ < i₂ ∨ i₁ = i₂ ∧ j₁ ≤ j₂
```

> ### ofBits

`Nat.ofBits_zero` (theorem, [line 240](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L240))

```lean
theorem ofBits_zero (f : Fin 0 → Bool) : ofBits f = 0
```

`Nat.ofBits_succ` (theorem, [line 242](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L242))

```lean
theorem ofBits_succ (f : Fin (n+1) → Bool) : ofBits f = 2 * ofBits (f ∘ Fin.succ) + (f 0).toNat
```

`Nat.ofBits_lt_two_pow` (theorem, [line 245](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L245))

```lean
theorem ofBits_lt_two_pow (f : Fin n → Bool) : ofBits f < 2 ^ n
```

`Nat.testBit_ofBits_lt` (theorem, [line 255](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L255))

```lean
theorem testBit_ofBits_lt (f : Fin n → Bool) (i : Nat) (h : i < n) :
    (ofBits f).testBit i = f ⟨i, h⟩
```

`Nat.testBit_ofBits_ge` (theorem, [line 267](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L267))

```lean
theorem testBit_ofBits_ge (f : Fin n → Bool) (i : Nat) (h : n ≤ i) :
    (ofBits f).testBit i = false
```

`Nat.testBit_ofBits` (theorem, [line 274](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L274))

```lean
theorem testBit_ofBits (f : Fin n → Bool) :
    (ofBits f).testBit i = if h : i < n then f ⟨i, h⟩ else false
```

`Nat.ofBits_testBit` (theorem, [line 280](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L280))

```lean
theorem ofBits_testBit (x n) : ofBits (fun i : Fin n => x.testBit i) = x % 2 ^ n
```

> ### toString

`Nat.toString_append_toString` (theorem, [line 301](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L301))

```lean
theorem toString_append_toString (a b : Nat) (ha : a ≠ 0) :
    toString a ++ toString b = toString (a * 10 ^ (toString b).length + b)
```

> ### Misc

`Nat.mul_add_lt_mul_of_lt_of_lt` (theorem, [line 308](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L308))

```lean
theorem mul_add_lt_mul_of_lt_of_lt {m n x y : Nat} (hx : x < m) (hy : y < n) :
    n * x + y < m * n
```

`Nat.add_mul_lt_mul_of_lt_of_lt` (theorem, [line 311](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean#L311))

```lean
theorem add_mul_lt_mul_of_lt_of_lt {m n x y : Nat} (hx : x < m) (hy : y < n) :
    x + m * y < m * n
```

## Depends on

- [Nat/Basic](basic.md)

## Sources

- [Batteries/Data/Nat/Lemmas.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Lemmas.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Nat.Lemmas.json)
