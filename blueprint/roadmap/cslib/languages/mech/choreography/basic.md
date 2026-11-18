---
catalog: module
lean: Cslib.Languages.Mech.Expr, Cslib.Languages.Mech.Prefix, Cslib.Languages.Mech.Choreography, Cslib.Languages.Mech.Prefix.pn, Cslib.Languages.Mech.Choreography.pn
statement: formalized
proof: formalized
---

# Choreography

`Cslib.Languages.Mech.Choreography.Basic`, in [Cslib/Languages/Mech/Choreography/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/Choreography/Basic.lean), by Fabrizio Montesi.

> A choreography defines the collective behaviour of a system of communicating participants
> (processes) [Montesi2023].
>
> ## Limitations
>
> Some notable features not yet included:
> - Recursion (only the syntax is implemented, but no semantics).
> - General recursion (the current syntax supports only tail recursion).
> - Choreographic choice (for barriers, first-come/first-served patterns, etc.).
> - Asynchronous communication.
>
> ## References
>
> * [F. Montesi, *Introduction to Choreographies*][Montesi2023]

> ## Syntax of choreographies

`Cslib.Languages.Mech.Expr` (inductive type, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/Choreography/Basic.lean#L40))

> Expressions for local computation.

```lean
inductive Expr (Var Val FunId : Type*) where
  /-- Read variable `x`. -/
  | var (x : Var)
  /-- Value `v`. -/
  | val (v : Val)
  /-- Call function `f` with arguments `args`. -/
  | call (f : FunId) (args : List (Expr Var Val FunId))
```

`Cslib.Languages.Mech.Prefix` (inductive type, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/Choreography/Basic.lean#L57))

> Choreographic prefix.

```lean
inductive Prefix (Pid Var Val FunId SelLabel : Type*) where
  /-- `p` assigns `x` the value computed from `e`. -/
  | assign (p : Pid) (x : Var) (e : Expr Var Val FunId)
  /-- `p` communicates the evaluation of `e` to `q`, which stores it in its variable `x`. -/
  | com (p : Pid) (e : Expr Var Val FunId) (q : Pid) (x : Var)
  /-- `p` communicates the selection label (a static tag used to denote a choice) to `q`. -/
  | sel (p : Pid) (q : Pid) (l : SelLabel)
```

`Cslib.Languages.Mech.Choreography` (inductive type, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/Choreography/Basic.lean#L66))

> Choreographies.

```lean
inductive Choreography (Pid Var Val FunId SelLabel ProcName : Type*) where
  /-- The terminated choreography. -/
  | nil
  /-- Do `prf` and continue as `c`. -/
  | pre (prf : Prefix Pid Var Val FunId SelLabel)
    (c : Choreography Pid Var Val FunId SelLabel ProcName)
  /-- Conditional: `p` evaluates `e` to choose between `c₁` and `c₂`. -/
  | cond (p : Pid) (e : Expr Var Val FunId)
    (c₁ c₂ : Choreography Pid Var Val FunId SelLabel ProcName)
  /-- Call the procedure `proc`. -/
  | call (proc : ProcName) (ps : List Pid)
```

`Cslib.Languages.Mech.Prefix.pn` (definition, [line 124](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/Choreography/Basic.lean#L124))

> Process names in a prefix.

```lean
def Prefix.pn : Prefix Pid Var Val FunId SelLabel → Finset Pid
```

`Cslib.Languages.Mech.Choreography.pn` (definition, [line 129](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/Choreography/Basic.lean#L129))

> Process names in a choreography.

```lean
def Choreography.pn : Choreography Pid Var Val FunId SelLabel ProcName → Finset Pid
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Languages/Mech/Choreography/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/Choreography/Basic.lean)
