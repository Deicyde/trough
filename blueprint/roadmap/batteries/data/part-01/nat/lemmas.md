---
catalog: module
lean: Nat.recAux_zero, Nat.recAux_succ, Nat.recAuxOn_zero, Nat.recAuxOn_succ, Nat.casesAuxOn_zero, Nat.casesAuxOn_succ, Nat.strongRec_eq, Nat.strongRecOn_eq, Nat.recDiagAux_zero_left, Nat.recDiagAux_zero_right, Nat.recDiagAux_succ_succ, Nat.recDiag_zero_zero, Nat.recDiag_zero_succ, Nat.recDiag_succ_zero, Nat.recDiag_succ_succ, Nat.recDiagOn_zero_zero, Nat.recDiagOn_zero_succ, Nat.recDiagOn_succ_zero, Nat.recDiagOn_succ_succ, Nat.casesDiagOn_zero_zero, Nat.casesDiagOn_zero_succ, Nat.casesDiagOn_succ_zero, Nat.casesDiagOn_succ_succ, Nat.lt_sum_ge, Nat.sum_trichotomy, Nat.ofBits_zero, Nat.ofBits_succ, Nat.ofBits_lt_two_pow, Nat.testBit_ofBits_lt, Nat.testBit_ofBits_ge, Nat.testBit_ofBits, Nat.ofBits_testBit, Nat.toString_append_toString, Nat.mul_add_lt_mul_of_lt_of_lt, Nat.add_mul_lt_mul_of_lt_of_lt
statement: formalized
proof: formalized
---

# Basic lemmas about natural numbers

`Batteries.Data.Nat.Lemmas`, in [Batteries/Data/Nat/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean), by Leonardo de Moura, Jeremy Avigad, Mario Carneiro.

> The primary purpose of the lemmas in this file is to assist with reasoning
> about sizes of objects, array indices and such. For a more thorough development
> of the theory of natural numbers, we recommend using Mathlib.

> ### rec/cases

`Nat.recAux_zero` (theorem, [line 23](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L23))

```lean
theorem recAux_zero {motive : Nat → Sort _} (zero : motive 0)
    (succ : ∀ n, motive n → motive (n+1)) :
    Nat.recAux zero succ 0 = zero
```

`Nat.recAux_succ` (theorem, [line 27](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L27))

```lean
theorem recAux_succ {motive : Nat → Sort _} (zero : motive 0)
    (succ : ∀ n, motive n → motive (n+1)) (n) :
    Nat.recAux zero succ (n+1) = succ n (Nat.recAux zero succ n)
```

`Nat.recAuxOn_zero` (theorem, [line 31](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L31))

```lean
theorem recAuxOn_zero {motive : Nat → Sort _} (zero : motive 0)
    (succ : ∀ n, motive n → motive (n+1)) :
    Nat.recAuxOn 0 zero succ = zero
```

`Nat.recAuxOn_succ` (theorem, [line 35](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L35))

```lean
theorem recAuxOn_succ {motive : Nat → Sort _} (zero : motive 0)
    (succ : ∀ n, motive n → motive (n+1)) (n) :
    Nat.recAuxOn (n+1) zero succ = succ n (Nat.recAuxOn n zero succ)
```

`Nat.casesAuxOn_zero` (theorem, [line 39](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L39))

```lean
theorem casesAuxOn_zero {motive : Nat → Sort _} (zero : motive 0)
    (succ : ∀ n, motive (n+1)) :
    Nat.casesAuxOn 0 zero succ = zero
```

`Nat.casesAuxOn_succ` (theorem, [line 43](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L43))

```lean
theorem casesAuxOn_succ {motive : Nat → Sort _} (zero : motive 0)
    (succ : ∀ n, motive (n+1)) (n) :
    Nat.casesAuxOn (n+1) zero succ = succ n
```

`Nat.strongRec_eq` (theorem, [line 47](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L47))

```lean
theorem strongRec_eq {motive : Nat → Sort _} (ind : ∀ n, (∀ m, m < n → motive m) → motive n)
    (t : Nat) : Nat.strongRec ind t = ind t fun m _ => Nat.strongRec ind m
```

`Nat.strongRecOn_eq` (theorem, [line 51](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L51))

```lean
theorem strongRecOn_eq {motive : Nat → Sort _} (ind : ∀ n, (∀ m, m < n → motive m) → motive n)
    (t : Nat) : Nat.strongRecOn t ind = ind t fun m _ => Nat.strongRecOn m ind
```

`Nat.recDiagAux_zero_left` (theorem, [line 55](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L55))

```lean
theorem recDiagAux_zero_left {motive : Nat → Nat → Sort _}
    (zero_left : ∀ n, motive 0 n) (zero_right : ∀ m, motive m 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (n) :
    Nat.recDiagAux zero_left zero_right succ_succ 0 n = zero_left n
```

`Nat.recDiagAux_zero_right` (theorem, [line 60](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L60))

```lean
theorem recDiagAux_zero_right {motive : Nat → Nat → Sort _}
    (zero_left : ∀ n, motive 0 n) (zero_right : ∀ m, motive m 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (m)
    (h : zero_left 0 = zero_right 0 := by first | assumption | trivial) :
    Nat.recDiagAux zero_left zero_right succ_succ m 0 = zero_right m
```

`Nat.recDiagAux_succ_succ` (theorem, [line 66](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L66))

```lean
theorem recDiagAux_succ_succ {motive : Nat → Nat → Sort _}
    (zero_left : ∀ n, motive 0 n) (zero_right : ∀ m, motive m 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (m n) :
    Nat.recDiagAux zero_left zero_right succ_succ (m+1) (n+1)
      = succ_succ m n (Nat.recDiagAux zero_left zero_right succ_succ m n)
```

`Nat.recDiag_zero_zero` (theorem, [line 72](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L72))

```lean
theorem recDiag_zero_zero {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 n → motive 0 (n+1)) (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) :
    Nat.recDiag (motive:=motive) zero_zero zero_succ succ_zero succ_succ 0 0 = zero_zero
```

`Nat.recDiag_zero_succ` (theorem, [line 77](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L77))

```lean
theorem recDiag_zero_succ {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 n → motive 0 (n+1)) (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (n) :
    Nat.recDiag zero_zero zero_succ succ_zero succ_succ 0 (n+1)
      = zero_succ n (Nat.recDiag zero_zero zero_succ succ_zero succ_succ 0 n)
```

`Nat.recDiag_succ_zero` (theorem, [line 84](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L84))

```lean
theorem recDiag_succ_zero {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 n → motive 0 (n+1)) (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (m) :
    Nat.recDiag zero_zero zero_succ succ_zero succ_succ (m+1) 0
      = succ_zero m (Nat.recDiag zero_zero zero_succ succ_zero succ_succ m 0)
```

`Nat.recDiag_succ_succ` (theorem, [line 91](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L91))

```lean
theorem recDiag_succ_succ {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 n → motive 0 (n+1)) (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (m n) :
    Nat.recDiag zero_zero zero_succ succ_zero succ_succ (m+1) (n+1)
      = succ_succ m n (Nat.recDiag zero_zero zero_succ succ_zero succ_succ m n)
```

`Nat.recDiagOn_zero_zero` (theorem, [line 97](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L97))

```lean
theorem recDiagOn_zero_zero {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 n → motive 0 (n+1)) (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) :
    Nat.recDiagOn (motive:=motive) 0 0 zero_zero zero_succ succ_zero succ_succ = zero_zero
```

`Nat.recDiagOn_zero_succ` (theorem, [line 102](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L102))

```lean
theorem recDiagOn_zero_succ {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 n → motive 0 (n+1)) (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (n) :
    Nat.recDiagOn 0 (n+1) zero_zero zero_succ succ_zero succ_succ
      = zero_succ n (Nat.recDiagOn 0 n zero_zero zero_succ succ_zero succ_succ)
```

`Nat.recDiagOn_succ_zero` (theorem, [line 109](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L109))

```lean
theorem recDiagOn_succ_zero {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 n → motive 0 (n+1)) (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (m) :
    Nat.recDiagOn (m+1) 0 zero_zero zero_succ succ_zero succ_succ
      = succ_zero m (Nat.recDiagOn m 0 zero_zero zero_succ succ_zero succ_succ)
```

`Nat.recDiagOn_succ_succ` (theorem, [line 116](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L116))

```lean
theorem recDiagOn_succ_succ {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 n → motive 0 (n+1)) (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
    (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) (m n) :
    Nat.recDiagOn (m+1) (n+1) zero_zero zero_succ succ_zero succ_succ
      = succ_succ m n (Nat.recDiagOn m n zero_zero zero_succ succ_zero succ_succ)
```

`Nat.casesDiagOn_zero_zero` (theorem, [line 122](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L122))

```lean
theorem casesDiagOn_zero_zero {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 (n+1)) (succ_zero : ∀ m, motive (m+1) 0)
    (succ_succ : ∀ m n, motive (m+1) (n+1)) :
    Nat.casesDiagOn 0 0 (motive:=motive) zero_zero zero_succ succ_zero succ_succ = zero_zero
```

`Nat.casesDiagOn_zero_succ` (theorem, [line 127](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L127))

```lean
theorem casesDiagOn_zero_succ {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 (n+1)) (succ_zero : ∀ m, motive (m+1) 0)
    (succ_succ : ∀ m n, motive (m+1) (n+1)) (n) :
    Nat.casesDiagOn 0 (n+1) zero_zero zero_succ succ_zero succ_succ = zero_succ n
```

`Nat.casesDiagOn_succ_zero` (theorem, [line 132](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L132))

```lean
theorem casesDiagOn_succ_zero {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 (n+1)) (succ_zero : ∀ m, motive (m+1) 0)
    (succ_succ : ∀ m n, motive (m+1) (n+1)) (m) :
    Nat.casesDiagOn (m+1) 0 zero_zero zero_succ succ_zero succ_succ = succ_zero m
```

`Nat.casesDiagOn_succ_succ` (theorem, [line 137](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L137))

```lean
theorem casesDiagOn_succ_succ {motive : Nat → Nat → Sort _} (zero_zero : motive 0 0)
    (zero_succ : ∀ n, motive 0 (n+1)) (succ_zero : ∀ m, motive (m+1) 0)
    (succ_succ : ∀ m n, motive (m+1) (n+1)) (m n) :
    Nat.casesDiagOn (m+1) (n+1) zero_zero zero_succ succ_zero succ_succ = succ_succ m n
```

> ## strong case

`Nat.lt_sum_ge` (definition, [line 145](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L145))

> Strong case analysis on `a < b ∨ b ≤ a`

```lean
protected def lt_sum_ge (a b : Nat) : a < b ⊕' b ≤ a
```

`Nat.sum_trichotomy` (definition, [line 149](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L149))

> Strong case analysis on `a < b ∨ a = b ∨ b < a`

```lean
protected def sum_trichotomy (a b : Nat) : a < b ⊕' a = b ⊕' b < a
```

> ### div/mod

> ### ofBits

`Nat.ofBits_zero` (theorem, [line 165](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L165))

```lean
theorem ofBits_zero (f : Fin 0 → Bool) : ofBits f = 0
```

`Nat.ofBits_succ` (theorem, [line 167](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L167))

```lean
theorem ofBits_succ (f : Fin (n+1) → Bool) : ofBits f = 2 * ofBits (f ∘ Fin.succ) + (f 0).toNat
```

`Nat.ofBits_lt_two_pow` (theorem, [line 170](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L170))

```lean
theorem ofBits_lt_two_pow (f : Fin n → Bool) : ofBits f < 2 ^ n
```

`Nat.testBit_ofBits_lt` (theorem, [line 180](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L180))

```lean
theorem testBit_ofBits_lt (f : Fin n → Bool) (i : Nat) (h : i < n) :
    (ofBits f).testBit i = f ⟨i, h⟩
```

`Nat.testBit_ofBits_ge` (theorem, [line 192](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L192))

```lean
theorem testBit_ofBits_ge (f : Fin n → Bool) (i : Nat) (h : n ≤ i) :
    (ofBits f).testBit i = false
```

`Nat.testBit_ofBits` (theorem, [line 199](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L199))

```lean
theorem testBit_ofBits (f : Fin n → Bool) :
    (ofBits f).testBit i = if h : i < n then f ⟨i, h⟩ else false
```

`Nat.ofBits_testBit` (theorem, [line 205](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L205))

```lean
theorem ofBits_testBit (x n) : ofBits (fun i : Fin n => x.testBit i) = x % 2 ^ n
```

> ### toString

`Nat.toString_append_toString` (theorem, [line 226](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L226))

```lean
theorem toString_append_toString (a b : Nat) (ha : a ≠ 0) :
    toString a ++ toString b = toString (a * 10 ^ (toString b).length + b)
```

> ### Misc

`Nat.mul_add_lt_mul_of_lt_of_lt` (theorem, [line 233](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L233))

```lean
theorem mul_add_lt_mul_of_lt_of_lt {m n x y : Nat} (hx : x < m) (hy : y < n) :
    n * x + y < m * n
```

`Nat.add_mul_lt_mul_of_lt_of_lt` (theorem, [line 240](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean#L240))

```lean
theorem add_mul_lt_mul_of_lt_of_lt {m n x y : Nat} (hx : x < m) (hy : y < n) :
    x + m * y < m * n
```

## Depends on

- [Nat/Basic](basic.md)

## Sources

- [Batteries/Data/Nat/Lemmas.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Lemmas.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Nat.Lemmas.json)
