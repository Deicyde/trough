---
catalog: module
lean: Cslib.Mech.Expr, Cslib.Mech.LocalStore, Cslib.Mech.FunCallEval, Cslib.Mech.FunCallEval.EvalExpr, Cslib.Mech.GlobalStore, Cslib.Mech.AtPid, Cslib.Mech.AtPid.pid, Cslib.Mech.AtPid.elem
statement: formalized
proof: formalized
---

# Local expressions, stores, and evaluation

`Cslib.Languages.Mech.LocalComputation`, in [Cslib/Languages/Mech/LocalComputation.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/LocalComputation.lean), by Fabrizio Montesi.

> Choreographic programming and associated languages (like process calculi for modelling distributed
> protocol implementations) are typically defined abstracting from how processes locally compute and
> store values [Montesi2023]. This module defines this interface, as well as the derived concept of
> global store.
>
> ## Implementation notes
>
> The module is currently developed with minimality in mind. In the future, we plan on adding
> facilities for typing expressions and easy integration with Lean and other IRs/FFIs.
>
> ## References
>
> * [F. Montesi, *Introduction to Choreographies*][Montesi2023]

`Cslib.Mech.Expr` (inductive type, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/LocalComputation.lean#L34))

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

`Cslib.Mech.LocalStore` (abbreviation, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/LocalComputation.lean#L51))

> A local store represents the memory state of a process, mapping variables to values.

```lean
abbrev LocalStore Var Val
```

`Cslib.Mech.FunCallEval` (abbreviation, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/LocalComputation.lean#L55))

> Type of (potentially nondeterministic) evaluation relations for local function calls at
> processes.

```lean
abbrev FunCallEval FunId Val
```

`Cslib.Mech.FunCallEval.EvalExpr` (inductive type, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/LocalComputation.lean#L58))

> Evaluation relation for expressions.

```lean
inductive FunCallEval.EvalExpr (eval : FunCallEval FunId Val) :
    (σ : LocalStore Var Val) → (e : Expr Var Val FunId) → (v : Val) → Prop where
  /-- A value evaluates to itself. -/
  | val : eval.EvalExpr σ (.val v) v
  /-- A variable evaluates to its mapped value in the store. -/
  | var : eval.EvalExpr σ (.var x) (σ x)
  /-- A function call first recursively evaluates its expression arguments, and then
  invokes the parameter for function evaluation. -/
  | call
    (hArgs : List.Forall₂ (eval.EvalExpr σ) args vals)
    (hFun : eval f vals v) :
    eval.EvalExpr σ (.call f args) v
```

`Cslib.Mech.GlobalStore` (abbreviation, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/LocalComputation.lean#L73))

> A global store represents the memory state of an entire system, mapping each process to its
> local store.

```lean
abbrev GlobalStore Pid Var Val
```

`Cslib.Mech.AtPid` (abbreviation, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/LocalComputation.lean#L76))

> Type of an element of type `α` located at a process.

```lean
abbrev AtPid Pid α
```

`Cslib.Mech.AtPid.pid` (abbreviation, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/LocalComputation.lean#L79))

> The process name of a located element.

```lean
abbrev AtPid.pid (a : AtPid Pid α)
```

`Cslib.Mech.AtPid.elem` (abbreviation, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/LocalComputation.lean#L82))

> The element of a located element.

```lean
abbrev AtPid.elem (a : AtPid Pid α)
```

## Depends on

- [HasSubstitution](../../foundations/syntax/hassubstitution.md)

## Sources

- [Cslib/Languages/Mech/LocalComputation.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/Mech/LocalComputation.lean)
