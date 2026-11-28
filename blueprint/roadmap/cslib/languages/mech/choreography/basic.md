---
catalog: module
lean: Cslib.Languages.Mech.Prefix, Cslib.Languages.Mech.Choreography, Cslib.Languages.Mech.Prefix.pn, Cslib.Languages.Mech.Choreography.pn
statement: formalized
proof: formalized
---

# Choreography

`Cslib.Languages.Mech.Choreography.Basic`, in [Cslib/Languages/Mech/Choreography/Basic.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Choreography/Basic.lean), by Fabrizio Montesi.

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
> ## Implementation notes
>
> Choreographies are polymorphic in the types of participant, selection label, and procedure name
> types, and in the universes of the signature. As in Stateful
> Processes, the guard of a conditional may have any value type with a designated true value
> (`Cslib.HasTrue`), such as `Bool` or `Prop`.
>
> Local expressions in choreographies can use the notation for the syntactic category `mechExpr`; for
> example, a braced Lean computation, as in `p.{$x + 1} ⮕ q.y`.
>
> ## References
>
> * [F. Montesi, *Introduction to Choreographies*][Montesi2023]

> ## Syntax of choreographies

`Cslib.Languages.Mech.Prefix` (inductive type, [line 55](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Choreography/Basic.lean#L55))

> Choreographic prefix.

```lean
inductive Prefix (Pid : Type u) (S : Sig.{u, v, w} Pid) (SelLabel : Type*) where
  /-- `p` assigns `x` the value computed from `e`. -/
  | assign {α : Type w} (p : Pid) (x : S.Var p α) (e : S.Expr p α)
  /-- `p` communicates the evaluation of `e` to `q`, which stores it in its variable `x`. -/
  | com {α : Type w} (p : Pid) (e : S.Expr p α) (q : Pid) (x : S.Var q α)
  /-- `p` communicates the selection label (a static tag used to denote a choice) to `q`. -/
  | sel (p : Pid) (q : Pid) (l : SelLabel)
```

`Cslib.Languages.Mech.Choreography` (inductive type, [line 64](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Choreography/Basic.lean#L64))

> Choreographies.

```lean
inductive Choreography (Pid : Type u) (S : Sig.{u, v, w} Pid) (SelLabel ProcName : Type*) where
  /-- The terminated choreography. -/
  | nil
  /-- Do `prf` and continue as `c`. -/
  | pre (prf : Prefix Pid S SelLabel)
    (c : Choreography Pid S SelLabel ProcName)
  /-- Conditional: `p` evaluates the guard `e`, continuing as `c₁` if it evaluates to the true value
  of its guard type (see `HasTrue`) and as `c₂` otherwise. -/
  | cond {α : Type w} [inst : HasTrue α] (p : Pid) (e : S.Expr p α)
    (c₁ c₂ : Choreography Pid S SelLabel ProcName)
  /-- Call the procedure `proc`. -/
  | call (proc : ProcName) (ps : List Pid)
```

`Cslib.Languages.Mech.Prefix.pn` (definition, [line 126](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Choreography/Basic.lean#L126))

> Process names in a prefix.

```lean
def Prefix.pn : Prefix Pid S SelLabel → Finset Pid
```

`Cslib.Languages.Mech.Choreography.pn` (definition, [line 131](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Choreography/Basic.lean#L131))

> Process names in a choreography.

```lean
def Choreography.pn : Choreography Pid S SelLabel ProcName → Finset Pid
```

## Depends on

- [Types with a designated true value](../../../foundations/data/hastrue.md)
- [Local expressions](../common/expr/basic.md)

## Sources

- [Cslib/Languages/Mech/Choreography/Basic.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Choreography/Basic.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Languages.Mech.Choreography.Basic.json)
