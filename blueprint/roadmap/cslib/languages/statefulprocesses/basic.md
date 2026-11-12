---
catalog: module
lean: Cslib.StatefulProcesses.Prefix, Cslib.StatefulProcesses.Process, Cslib.StatefulProcesses.Act, Cslib.StatefulProcesses.Act.isInternal, Cslib.StatefulProcesses.Prefix.toAct, Cslib.StatefulProcesses.Process.Tr, Cslib.StatefulProcesses.Process.lts
statement: formalized
proof: formalized
---

# Stateful Processes

`Cslib.Languages.StatefulProcesses.Basic`, in [Cslib/Languages/StatefulProcesses/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Basic.lean), by Fabrizio Montesi.

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
> For recursion, only the syntax is currently implemented. Its semantics will follow a similar
> approach to that for `CCS`.
>
> ## Implementation notes
>
> This development follows the presentation in [Montesi2023], with one difference: we adopt a modular
> approach to the definition of operational semantics, by first defining a symbolic semantics from
> which a concrete semantics is then derived by adding stores (process memory). This approach is
> described in [Acclavio2026].
>
> ## References
>
> * [M. Acclavio, G. Manara, F. Montesi, X. Qin, *Choreographic Programming: a Semantic Approach*][Acclavio2026]
> * [F. Montesi, *Introduction to Choreographies*][Montesi2023]

> ## Syntax of process terms

`Cslib.StatefulProcesses.Prefix` (inductive type, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Basic.lean#L54))

> Prefixes.

```lean
inductive Prefix (Pid Var Val FunId SelLabel : Type*) where
  /-- Assign to `x` the result of evaluating `e`. -/
  | assign (x : Var) (e : Expr Var Val FunId)
  /-- Send to `p` the result of evaluating `e`. -/
  | sendValue (p : Pid) (e : Expr Var Val FunId)
  /-- Receive a value from `p` and store it in `x`. -/
  | recvValue (p : Pid) (x : Var)
  /-- Send to `p` the label `l`. -/
  | sendLabel (p : Pid) (l : SelLabel)
```

`Cslib.StatefulProcesses.Process` (inductive type, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Basic.lean#L65))

> Processes.

```lean
inductive Process (Pid Var Val FunId SelLabel ProcName : Type*) where
  /-- The terminated process. -/
  | nil
  /-- Execute the prefix `prf` and proceed as the continuation `pr`. -/
  | pre (prf : Prefix Pid Var Val FunId SelLabel) (pr : Process Pid Var Val FunId SelLabel ProcName)
  /-- Branching process: receives a selection label and continues accordingly. -/
  | recvLabel (p : Pid) (branches : List (SelLabel × Process Pid Var Val FunId SelLabel ProcName))
  /-- Conditional: evaluate `e` to choose between `pr₁` and `pr₂`. -/
  | cond (e : Expr Var Val FunId) (pr₁ pr₂ : Process Pid Var Val FunId SelLabel ProcName)
  /-- Call the procedure `proc`. -/
  | call (proc : ProcName) (ps : List Pid)
```

> ## Semantics

`Cslib.StatefulProcesses.Act` (inductive type, [line 138](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Basic.lean#L138))

> Actions.

```lean
inductive Act (Pid Var Val FunId SelLabel : Type*) where
  /-- Assign to `x` the result of evaluating `e`. -/
  | assign (x : Var) (e : Expr Var Val FunId)
  /-- Send to `p` the result of evaluating `e`. -/
  | sendValue (p : Pid) (e : Expr Var Val FunId)
  /-- Receive a value from `p` and store it in variable `x`. -/
  | recvValue (p : Pid) (x : Var)
  /-- Send to `p` the selection label `l`. -/
  | sendLabel (p : Pid) (l : SelLabel)
  /-- Receive from `p` the selection label `l`. -/
  | recvLabel (p : Pid) (l : SelLabel)
  /-- Choose the then-branch of a conditional guarded by `e`. -/
  | condThen (e : Expr Var Val FunId)
  /-- Choose the else-branch of a conditional guarded by `e`. -/
  | condElse (e : Expr Var Val FunId)
```

`Cslib.StatefulProcesses.Act.isInternal` (definition, [line 155](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Basic.lean#L155))

> An action is internal if it is not meant to interact with another process.

```lean
def Act.isInternal : Act Pid Var Val FunId SelLabel → Bool
```

`Cslib.StatefulProcesses.Prefix.toAct` (abbreviation, [line 160](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Basic.lean#L160))

> Transforms a `Prefix` into an `Act`.

```lean
abbrev Prefix.toAct : Prefix Pid Var Val FunId SelLabel → Act Pid Var Val FunId SelLabel
```

`Cslib.StatefulProcesses.Process.Tr` (inductive type, [line 168](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Basic.lean#L168))

> Symbolic transition relation for processes.
> Do not use this directly, use `Process.lts` instead.

```lean
inductive Process.Tr :
    Process Pid Var Val FunId SelLabel ProcName → Act Pid Var Val FunId SelLabel →
    Process Pid Var Val FunId SelLabel ProcName → Prop
  | pre : Tr (pre prf pr) prf.toAct (pr)
  | condThen : Tr (cond e pr₁ pr₂) (.condThen e) pr₁
  | condElse : Tr (cond e pr₁ pr₂) (.condElse e) pr₂
  | recvLabel (h : (l, pr) ∈ branches): Tr (recvLabel p branches) (.recvLabel p l) pr
```

`Cslib.StatefulProcesses.Process.lts` (definition, [line 177](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Basic.lean#L177))

> Symbolic LTS of processes.

```lean
def Process.lts :
    LTS (Process Pid Var Val FunId SelLabel ProcName) (Act Pid Var Val FunId SelLabel)
```

## Depends on

- [Labelled Transition System (LTS)](../../foundations/semantics/lts/basic.md)
- [Local expressions, stores, and evaluation](../mech/localcomputation.md)

## Sources

- [Cslib/Languages/StatefulProcesses/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/StatefulProcesses/Basic.lean)
