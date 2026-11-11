---
declaration: theorem
origin: cited
lean: Nat.exists_mem_Icc_eq_of_le_succ
statement: formalized
proof: formalized
---

# Discrete intermediate value theorem

If a sequence increases by at most one successor
at each step between `a` and `b`, then it attains every value between `f a` and `f b` at an index
in `[a, b]`. No restriction is imposed on downward jumps.

```lean
Nat.exists_mem_Icc_eq_of_le_succ.{u_1} {α : Type u_1} [LinearOrder α] [SuccOrder α] {f : ℕ → α}
  {a b : ℕ} {y : α} (hab : a ≤ b) (hstep : ∀ (i : ℕ), a ≤ i → i < b → f (i + 1) ≤ Order.succ (f i))
  (ha : f a ≤ y) (hb : y ≤ f b) : ∃ i ∈ Set.Icc a b, f i = y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Nat.exists_mem_Icc_eq_of_le_succ`](https://taucetiproject.org/docs/TauCeti/Order/SuccPred/IntermediateValue.html#Nat.exists_mem_Icc_eq_of_le_succ).

## Sources

- [Tau Ceti documentation: `Nat.exists_mem_Icc_eq_of_le_succ`](https://taucetiproject.org/docs/TauCeti/Order/SuccPred/IntermediateValue.html#Nat.exists_mem_Icc_eq_of_le_succ)
- [Source of `Nat.exists_mem_Icc_eq_of_le_succ` in TauCeti/Order/SuccPred/IntermediateValue.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Order/SuccPred/IntermediateValue.lean#L26)
