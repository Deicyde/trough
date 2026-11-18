---
catalog: module
lean: Nat.recAuxOn, Nat.strongRec, Nat.strongRecMeasure, Nat.recDiagAux, Nat.recDiag, Nat.recDiagOn, Nat.casesDiagOn, Nat.ofBits
statement: formalized
proof: formalized
---

# Nat/Basic

`Batteries.Data.Nat.Basic`, in [Batteries/Data/Nat/Basic.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Basic.lean), by Leonardo de Moura, Jeremy Avigad, Mario Carneiro.

`Nat.recAuxOn` (definition, [line 16](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Basic.lean#L16))

> Recursor identical to `Nat.recOn` but uses notations `0` for `Nat.zero` and `·+1` for `Nat.succ`

```lean
protected def recAuxOn {motive : Nat → Sort _} (t : Nat) (zero : motive 0)
  (succ : ∀ n, motive n → motive (n+1)) : motive t
```

`Nat.strongRec` (definition, [line 23](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Basic.lean#L23))

> Strong recursor for `Nat`

```lean
protected def strongRec {motive : Nat → Sort _} (ind : ∀ n, (∀ m, m < n → motive m) → motive n)
  (t : Nat) : motive t
```

`Nat.strongRecMeasure` (definition, [line 30](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Basic.lean#L30))

> Strong recursor via a `Nat`-valued measure

```lean
def strongRecMeasure (f : α → Nat) {motive : α → Sort _}
    (ind : ∀ x, (∀ y, f y < f x → motive y) → motive x) (x : α) : motive x
```

`Nat.recDiagAux` (definition, [line 39](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Basic.lean#L39))

> Simple diagonal recursor for `Nat`

```lean
protected def recDiagAux {motive : Nat → Nat → Sort _}
  (zero_left : ∀ n, motive 0 n)
  (zero_right : ∀ m, motive m 0)
  (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) :
    (m n : Nat) → motive m n
```

`Nat.recDiag` (definition, [line 52](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Basic.lean#L52))

> Diagonal recursor for `Nat`

```lean
protected def recDiag {motive : Nat → Nat → Sort _}
  (zero_zero : motive 0 0)
  (zero_succ : ∀ n, motive 0 n → motive 0 (n+1))
  (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
  (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) :
    (m n : Nat) → motive m n
```

`Nat.recDiagOn` (definition, [line 72](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Basic.lean#L72))

> Diagonal recursor for `Nat`

```lean
protected def recDiagOn {motive : Nat → Nat → Sort _} (m n : Nat)
  (zero_zero : motive 0 0)
  (zero_succ : ∀ n, motive 0 n → motive 0 (n+1))
  (succ_zero : ∀ m, motive m 0 → motive (m+1) 0)
  (succ_succ : ∀ m n, motive m n → motive (m+1) (n+1)) :
    motive m n
```

`Nat.casesDiagOn` (definition, [line 83](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Basic.lean#L83))

> Diagonal recursor for `Nat`

```lean
protected def casesDiagOn {motive : Nat → Nat → Sort _} (m n : Nat)
  (zero_zero : motive 0 0)
  (zero_succ : ∀ n, motive 0 (n+1))
  (succ_zero : ∀ m, motive (m+1) 0)
  (succ_succ : ∀ m n, motive (m+1) (n+1)) :
    motive m n
```

`Nat.ofBits` (definition, [line 95](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Basic.lean#L95))

> Construct a natural number from a sequence of bits using little endian convention.

```lean
def ofBits (f : Fin n → Bool) : Nat
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/Nat/Basic.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Nat/Basic.lean)
