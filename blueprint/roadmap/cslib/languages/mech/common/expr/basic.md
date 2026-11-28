---
catalog: module
lean: Cslib.Mech.LocalSig.Expr, Cslib.Mech.LocalSig.Expr.map, Cslib.Mech.LocalSig.Expr.map₂, Cslib.Mech.LocalSig.Expr.varNames, Cslib.Mech.LocalSig.Expr.varNames_val, Cslib.Mech.LocalSig.Expr.varNames_var, Cslib.Mech.LocalSig.Expr.varNames_pair, Cslib.Mech.LocalSig.Expr.varNames_call, Cslib.Mech.LocalSig.Expr.varNames_map, Cslib.Mech.LocalSig.Expr.Eval, Cslib.Mech.LocalSig.Expr.Eval.var_iff, Cslib.Mech.LocalSig.Expr.Eval.call_iff, Cslib.Mech.LocalSig.Expr.Eval.map_iff, Cslib.Mech.LocalSig.Expr.Eval.of_agreeOn, Cslib.Mech.LocalSig.Expr.Eval.congr, Cslib.Mech.Sig.Expr
statement: formalized
proof: formalized
---

# Local expressions

`Cslib.Languages.Mech.Common.Expr.Basic`, in [Cslib/Languages/Mech/Common/Expr/Basic.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean), by Fabrizio Montesi.

`Cslib.Mech.LocalSig.Expr` (inductive type, [line 20](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean#L20))

> A local expression.

```lean
inductive Expr (L : LocalSig.{u, v}) : Type v → Type (max u (v + 1))
  /-- A value. -/
  | val {α} (v : α) : L.Expr α
  /-- Read a local variable. -/
  | var {α} (x : L.Var α) : L.Expr α
  /-- Evaluate two expressions as a pair. -/
  | pair {α β} (left : L.Expr α) (right : L.Expr β) : L.Expr (α × β)
  /-- Perform the computation `r` (modelled as a relation, in order to allow for nondeterminism) on
    the value of expression `arg`: the result may be any `b` with `r a b`, where `a` is the value of
    `arg`. -/
  | call {α β} (r : α → β → Prop) (arg : L.Expr α) : L.Expr β
```

`Cslib.Mech.LocalSig.Expr.map` (definition, [line 36](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean#L36))

> Apply a Lean function to an expression: the call of its graph.

```lean
def Expr.map {L : LocalSig} {α β} (f : α → β) (e : L.Expr α) : L.Expr β
```

`Cslib.Mech.LocalSig.Expr.map₂` (definition, [line 40](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean#L40))

> Apply a binary Lean function to two expressions.

```lean
def Expr.map₂ {L : LocalSig} {α β γ} (f : α → β → γ) (a : L.Expr α) (b : L.Expr β) : L.Expr γ
```

`Cslib.Mech.LocalSig.Expr.varNames` (definition, [line 50](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean#L50))

> The names of the variables read by an expression.

```lean
def Expr.varNames {L : LocalSig} {α} : L.Expr α → Finset L.VarName
```

`Cslib.Mech.LocalSig.Expr.varNames_val` (theorem, [line 57](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean#L57))

```lean
theorem Expr.varNames_val {L : LocalSig} {α} (v : α) : (Expr.val (L := L) v).varNames = ∅
```

`Cslib.Mech.LocalSig.Expr.varNames_var` (theorem, [line 60](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean#L60))

```lean
theorem Expr.varNames_var {L : LocalSig} {α} (x : L.Var α) : (Expr.var x).varNames = {x.name}
```

`Cslib.Mech.LocalSig.Expr.varNames_pair` (theorem, [line 64](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean#L64))

```lean
theorem Expr.varNames_pair {L : LocalSig} {α β} (left : L.Expr α) (right : L.Expr β) :
    (Expr.pair left right).varNames = left.varNames ∪ right.varNames
```

`Cslib.Mech.LocalSig.Expr.varNames_call` (theorem, [line 68](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean#L68))

```lean
theorem Expr.varNames_call {L : LocalSig} {α β} (r : α → β → Prop) (arg : L.Expr α) :
    (Expr.call r arg).varNames = arg.varNames
```

`Cslib.Mech.LocalSig.Expr.varNames_map` (theorem, [line 72](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean#L72))

```lean
theorem Expr.varNames_map {L : LocalSig} {α β} (f : α → β) (e : L.Expr α) :
    (e.map f).varNames = e.varNames
```

`Cslib.Mech.LocalSig.Expr.Eval` (inductive type, [line 77](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean#L77))

> Evaluation of expressions relative to a local store: `e.Eval σ v` states that `e` may evaluate
> to `v`.

```lean
inductive Expr.Eval.{u, v} {L : LocalSig.{u, v}} (σ : L.Store) : {α : Type v} → L.Expr α → α → Prop
  /-- A value evaluates to itself. -/
  | val {α} (v : α) : Eval σ (.val v) v
  /-- A variable evaluates to its value in the local store. -/
  | var {α} (x : L.Var α) : Eval σ (.var x) σ[x]
  /-- Two components of a pair evaluate independently. -/
  | pair {α β} {left : L.Expr α} {right : L.Expr β} {a : α} {b : β}
      (hl : Eval σ left a) (hr : Eval σ right b) : Eval σ (.pair left right) (a, b)
  /-- A call evaluates its argument and returns any result related to it. -/
  | call {α β} {r : α → β → Prop} {arg : L.Expr α} {a : α} {b : β}
      (harg : Eval σ arg a) (hr : r a b) : Eval σ (.call r arg) b
```

`Cslib.Mech.LocalSig.Expr.Eval.var_iff` (theorem, [line 91](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean#L91))

> A variable has the value stored at its name.

```lean
theorem Expr.Eval.var_iff {L : LocalSig} (σ : L.Store) {α} (x : L.Var α) (v : α) :
    Expr.Eval σ (.var x) v ↔ v = σ[x]
```

`Cslib.Mech.LocalSig.Expr.Eval.call_iff` (theorem, [line 98](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean#L98))

> A call evaluates exactly to the results related to a value of its argument.

```lean
theorem Expr.Eval.call_iff {L : LocalSig} (σ : L.Store) {α β} (r : α → β → Prop)
    (arg : L.Expr α) (b : β) : Expr.Eval σ (.call r arg) b ↔ ∃ a, arg.Eval σ a ∧ r a b
```

`Cslib.Mech.LocalSig.Expr.Eval.map_iff` (theorem, [line 109](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean#L109))

> Applying a Lean function evaluates to its value on a value of the argument.

```lean
theorem Expr.Eval.map_iff {L : LocalSig} (σ : L.Store) {α β} (f : α → β)
    (arg : L.Expr α) (b : β) : (arg.map f).Eval σ b ↔ ∃ a, arg.Eval σ a ∧ b = f a
```

`Cslib.Mech.LocalSig.Expr.Eval.of_agreeOn` (theorem, [line 114](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean#L114))

> The values of an expression depend only on the variables it reads.

```lean
theorem Expr.Eval.of_agreeOn {L : LocalSig} {σ₁ σ₂ : L.Store} {α} {e : L.Expr α} {v : α}
    (h : σ₁.AgreeOn σ₂ e.varNames) (he : e.Eval σ₁ v) : e.Eval σ₂ v
```

`Cslib.Mech.LocalSig.Expr.Eval.congr` (theorem, [line 124](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean#L124))

> Stores that agree on the variables read by an expression give it the same values.

```lean
theorem Expr.Eval.congr {L : LocalSig} {σ₁ σ₂ : L.Store} {α} {e : L.Expr α} {v : α}
    (h : σ₁.AgreeOn σ₂ e.varNames) : e.Eval σ₁ v ↔ e.Eval σ₂ v
```

`Cslib.Mech.Sig.Expr` (abbreviation, [line 133](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean#L133))

> A local expression of type `α` of process `p`.

```lean
abbrev Expr {Pid} (S : Sig Pid) (p : Pid) (α : Type*)
```

## Depends on

- [Local stores](../localstore.md)

## Sources

- [Cslib/Languages/Mech/Common/Expr/Basic.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Basic.lean)
- [Declaration ledger](../../../../../../sources/cslib/Cslib.Languages.Mech.Common.Expr.Basic.json)
