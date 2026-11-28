---
catalog: module
lean: Cslib.StatefulProcesses.Prefix, Cslib.StatefulProcesses.Process, Cslib.StatefulProcesses.Act, Cslib.StatefulProcesses.Act.isInternal, Cslib.StatefulProcesses.Prefix.toAct, Cslib.StatefulProcesses.Process.Tr, Cslib.StatefulProcesses.Process.lts
statement: formalized
proof: formalized
---

# Stateful Processes

`Cslib.Languages.StatefulProcesses.Basic`, in [Cslib/Languages/StatefulProcesses/Basic.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Basic.lean), by Fabrizio Montesi.

> The language of Stateful Processes (SP for short), a process calculus
> where processes communicate via message passing [Montesi2023]. Stateful processes or similar
> languages are typically used to model implementations of choreographic programs (concurrent and/or
> distributed protocols), but they are also designed to be used as abstract representations that can
> be later compiled to executable mainstream languages.
>
> ## Limitations
>
> The current formalisation does not cover process polymorphism (procedures do not take process
> parameters) nor general recursion (this is the tail-recursive fragment of Stateful Processes).
> For recursion, only the syntax is currently implemented. …
>
> ## Implementation notes
>
> In process syntax, expressions can use the notation for the syntactic
> category `mechExpr`, see `Cslib.Languages.Mech.Common.Expr.Notation`): `{f $x $y}` applies a Lean
> function to participant-local variables `x` and `y`, `{term}` embeds a Lean term, and any term of
> type `L.Expr α` can be used directly.
>
> This development otherwise follows the presentation in [Montesi2023], with one difference: we
> adopt a modular approach to the definition of operational semantics, by first defining a symbolic
> semantics from which a concrete semantics is then derived by adding stores (process memory). This
> approach is described in [Acclavio2026].
>
> ## References
>
> * [M. Acclavio, G. Manara, F. Montesi, X. Qin,
>   *Choreographic Programming: a Semantic Approach*][Acclavio2026]
> * [F. Montesi, *Introduction to Choreographies*][Montesi2023]

> ## Syntax of process terms

`Cslib.StatefulProcesses.Prefix` (inductive type, [line 61](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Basic.lean#L61))

> A prefix of a stateful process.

```lean
inductive Prefix (Pid : Type u) (L : LocalSig.{v, w}) (SelLabel : Type*)
  /-- Assign a local variable. -/
  | assign {α : Type w} (x : L.Var α) (e : L.Expr α)
  /-- Send a value to a participant. -/
  | sendValue {α : Type w} (p : Pid) (e : L.Expr α)
  /-- Receive a value in a local variable. -/
  | recvValue {α : Type w} (p : Pid) (x : L.Var α)
  /-- Send a selection label. -/
  | sendLabel (p : Pid) (l : SelLabel)
```

`Cslib.StatefulProcesses.Process` (inductive type, [line 72](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Basic.lean#L72))

> Processes with typed local computations.

```lean
inductive Process (Pid : Type u) (L : LocalSig.{v, w}) (SelLabel ProcName : Type*)
  /-- Terminate. -/
  | nil
  /-- Execute a prefix and continue. -/
  | pre (prf : Prefix Pid L SelLabel) (pr : Process Pid L SelLabel ProcName)
  /-- Branch on a received label. -/
  | recvLabel (p : Pid) (branches : List (SelLabel × Process Pid L SelLabel ProcName))
  /-- Branch on a local computation `e`: continue as `pr₁` if `e` evaluates to the true value of its
  guard type (see `HasTrue`) and as `pr₂` otherwise. -/
  | cond {α : Type w} [inst : HasTrue α] (e : L.Expr α)
    (pr₁ pr₂ : Process Pid L SelLabel ProcName)
  /-- Call the procedure `proc`. -/
  | call (proc : ProcName) (ps : List Pid)
```

> ## Semantics

`Cslib.StatefulProcesses.Act` (inductive type, [line 152](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Basic.lean#L152))

> Symbolic actions.

```lean
inductive Act (Pid : Type u) (L : LocalSig.{v, w}) (SelLabel : Type*)
  | assign {α : Type w} (x : L.Var α) (e : L.Expr α)
  | sendValue {α : Type w} (p : Pid) (e : L.Expr α)
  | recvValue {α : Type w} (p : Pid) (x : L.Var α)
  | sendLabel (p : Pid) (l : SelLabel)
  | recvLabel (p : Pid) (l : SelLabel)
  | condThen {α : Type w} [inst : HasTrue α] (e : L.Expr α)
  | condElse {α : Type w} [inst : HasTrue α] (e : L.Expr α)
```

`Cslib.StatefulProcesses.Act.isInternal` (definition, [line 162](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Basic.lean#L162))

> An action is internal if it is not meant to interact with another process.

```lean
def Act.isInternal : Act Pid L SelLabel → Bool
```

`Cslib.StatefulProcesses.Prefix.toAct` (abbreviation, [line 167](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Basic.lean#L167))

> Transforms a `Prefix` into an `Act`.

```lean
abbrev Prefix.toAct : Prefix Pid L SelLabel → Act Pid L SelLabel
```

`Cslib.StatefulProcesses.Process.Tr` (inductive type, [line 175](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Basic.lean#L175))

> Symbolic transition relation for processes.
> Do not use this directly, use `Process.lts` instead.

```lean
inductive Process.Tr :
    Process Pid L SelLabel ProcName → Act Pid L SelLabel →
    Process Pid L SelLabel ProcName → Prop
  | pre : Tr (pre prf pr) prf.toAct (pr)
  | condThen {α} {_ : HasTrue α} {e : L.Expr α} : Tr (cond e pr₁ pr₂) (.condThen e) pr₁
  | condElse {α} {_ : HasTrue α} {e : L.Expr α} : Tr (cond e pr₁ pr₂) (.condElse e) pr₂
  | recvLabel (h : (l, pr) ∈ branches): Tr (recvLabel p branches) (.recvLabel p l) pr
```

`Cslib.StatefulProcesses.Process.lts` (definition, [line 184](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Basic.lean#L184))

> Symbolic LTS of processes.

```lean
def Process.lts :
    LTS (Process Pid L SelLabel ProcName) (Act Pid L SelLabel)
```

## Depends on

- [Types with a designated true value](../../foundations/data/hastrue.md)
- [Labelled Transition System (LTS)](../../foundations/semantics/lts/basic.md)
- [Local expressions](../mech/common/expr/basic.md)

## Sources

- [Cslib/Languages/StatefulProcesses/Basic.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/StatefulProcesses/Basic.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Languages.StatefulProcesses.Basic.json)
