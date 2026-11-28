---
catalog: module
lean: Cslib.Mech.LocalSig, Cslib.Mech.LocalSig.Var, Cslib.Mech.LocalSig.Var.Type, Cslib.Mech.LocalSig.Var.name_ne_of_type_ne, Cslib.Mech.Sig, Cslib.Mech.Sig.Var
statement: formalized
proof: formalized
---

# Signatures and variables for local computation

`Cslib.Languages.Mech.Common.Basic`, in [Cslib/Languages/Mech/Common/Basic.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Basic.lean), by Fabrizio Montesi.

> Choreographic programming and associated languages (like process calculi for modelling distributed
> protocol implementations) are typically defined abstracting from how processes locally compute and
> store values [Montesi2023].
>
> This module defines this interface. Local signatures (`LocalSig`) define the variables available to
> a process. Signatures of networks (`Sig`) assign a local signature to each process. Similarly, we
> define local stores (`LocalSig.Store`) mapping local variables to values, and global stores
> (`Sig.Store`) mapping processes to their local stores.
>
> ## Implementation notes
>
> Stores may assign different value types to different variables. Local computation uses plain Lean
> functions and relations (for modelling nondeterminism). Expressions are typed and keep a small
> syntax: values, variable reads, pairs, and calls of relations, so that the variables read by an
> expression can be computed (`LocalSig.Expr.vars`). A call `.call r e` may evaluate to any `b` such
> that `r a b`, where `a` is a value of `e`, which allows for nondeterministic local computations. A
> deterministic call of a Lean function `f` is the call of its graph, written `f <$> e` or with the
> braced notation `{f e}`.
>
> Processes have independent local signatures, so the same variable name may denote variables of
> different types in different processes. A variable of process `p` in a signature `S` has
> type `S.Var p α`.
>
> Local signatures include decidable equality of variable names, which is required by the write
> operation for stores.
>
> ## Limitations and future work
>
> The API currently requires going through Lean for any internal computation, and all computations
> are lifted as opaque nondeterministic computations. Future work will consider better support for:
> - Monadic computations in Lean (e.g., to capture probabilistic computations).
> - Second-stage compilation to other languages (e.g., C, Python, Rust).
> - Direct integration of other embedded languages (e.g., λ-calculus, which currently needs to go
> through encodings).
>
> ## References
>
> * [F. Montesi, *Introduction to Choreographies*][Montesi2023]

> ## Local signatures

`Cslib.Mech.LocalSig` (structure, [line 61](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Basic.lean#L61))

> A local signature, specifying variable names with their types.

```lean
structure LocalSig.{u, v} where
  /-- The type of variable names. -/
  VarName : Type u
  /-- Variable names have decidable equality. -/
  [decEq : DecidableEq VarName]
  /-- The type of the values stored in each variable. -/
  VarType : VarName → Type v
```

`Cslib.Mech.LocalSig.Var` (structure, [line 74](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Basic.lean#L74))

> A variable of type `α` under the local signature `L`.

```lean
structure Var (L : LocalSig.{u, v}) (α : Type v) : Type u where
  /-- The variable's name. -/
  name : L.VarName
  /-- Proof that the variable has type `α` in `L`. -/
  has_type : L.VarType name = α
```

`Cslib.Mech.LocalSig.Var.Type` (abbreviation, [line 81](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Basic.lean#L81))

> The type `α` of a variable `x : L.Var α`.

```lean
abbrev Var.Type {L : LocalSig} {α} (_ : L.Var α)
```

`Cslib.Mech.LocalSig.Var.name_ne_of_type_ne` (theorem, [line 84](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Basic.lean#L84))

> Variables of different types necessarily have different names.

```lean
theorem Var.name_ne_of_type_ne {L : LocalSig} {α β} (h : α ≠ β) (x : L.Var α) (y : L.Var β) :
    x.name ≠ y.name
```

> ## Signatures of networks

`Cslib.Mech.Sig` (abbreviation, [line 94](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Basic.lean#L94))

> The signature of a network, which assigns a local signature to each process.

```lean
abbrev Sig.{u,v,w} (Pid : Type u)
```

`Cslib.Mech.Sig.Var` (abbreviation, [line 99](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Basic.lean#L99))

> A variable of type `α` of process `p`.

```lean
abbrev Var {Pid} (S : Sig Pid) (p : Pid) (α : Type*)
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Languages/Mech/Common/Basic.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Basic.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Languages.Mech.Common.Basic.json)
