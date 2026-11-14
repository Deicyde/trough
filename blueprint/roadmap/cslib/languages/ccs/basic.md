---
catalog: module
lean: Cslib.CCS.Act, Cslib.CCS.Process, Cslib.CCS.Act.IsVisible, Cslib.CCS.Act.isVisible_neq_τ, Cslib.CCS.Act.Co, Cslib.CCS.Act.Co.symm, Cslib.CCS.Act.co_isVisible, Cslib.CCS.Act.isCo, Cslib.CCS.Act.isCo_iff, Cslib.CCS.Context, Cslib.CCS.Context.fill, Cslib.CCS.context_fill_def, Cslib.CCS.Context.complete
statement: formalized
proof: formalized
---

# Calculus of Communicating Systems (CCS)

`Cslib.Languages.CCS.Basic`, in [Cslib/Languages/CCS/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Basic.lean), by Fabrizio Montesi.

> CCS [Milner80], as presented in [Sangiorgi2011]. In the semantics (see `CCS.lts`), we adopt the
> option of constant definitions (K = P).
>
> ## Main definitions
> - `CCS.Process`: processes.
> - `CCS.Context`: contexts.
>
> ## Main results
> - `CCS.Context.complete`: any process is equal to some context filled an atomic process
> (nil or a constant).
>
> ## References
>
> * [R. Milner, *A Calculus of Communicating Systems*][Milner80]
> * [D. Sangiorgi, *Introduction to Bisimulation and Coinduction*][Sangiorgi2011]

`Cslib.CCS.Act` (inductive type, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Basic.lean#L39))

> Actions.

```lean
inductive Act (Name : Type u) : Type u where
  | name (a : Name)
  | coname (a : Name)
  | τ
deriving DecidableEq
```

`Cslib.CCS.Process` (inductive type, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Basic.lean#L46))

> Processes.

```lean
inductive Process (Name : Type u) (Constant : Type v) : Type (max u v) where
  /-- Terminated process. -/
  | nil
  /-- Do `μ` and proceed as `p`. -/
  | pre (μ : Act Name) (p : Process Name Constant)
  /-- `p` parallel `q`. -/
  | par (p q : Process Name Constant)
  /-- Do `p` or `q` (nondeterministically). -/
  | choice (p q : Process Name Constant)
  /-- Restriction. -/
  | res (a : Name) (p : Process Name Constant)
  /-- Constant. -/
  | const (c : Constant)
deriving DecidableEq
```

`Cslib.CCS.Act.IsVisible` (inductive type, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Basic.lean#L105))

> An action is visible if it a name or a coname.

```lean
inductive IsVisible : Act Name → Prop where
  | name : IsVisible (Act.name a)
  | coname : IsVisible (Act.coname a)
```

`Cslib.CCS.Act.isVisible_neq_τ` (theorem, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Basic.lean#L111))

> If an action is visible, it is not `τ`.

```lean
theorem isVisible_neq_τ {μ : Act Name} (h : μ.IsVisible) : μ ≠ Act.τ
```

`Cslib.CCS.Act.Co` (inductive type, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Basic.lean#L116))

> Checks that an action is the coaction of another.

```lean
inductive Co {Name : Type u} : Act Name → Act Name → Prop where
  | nc : Co (name a) (coname a)
  | cn : Co (coname a) (name a)
```

`Cslib.CCS.Act.Co.symm` (theorem, [line 122](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Basic.lean#L122))

> `Act.Co` is symmetric.

```lean
theorem Co.symm (h : Act.Co μ μ') : Act.Co μ' μ
```

`Cslib.CCS.Act.co_isVisible` (theorem, [line 126](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Basic.lean#L126))

> If two actions are one the coaction of the other, then they are both visible.

```lean
theorem co_isVisible (h : Act.Co μ μ') : μ.IsVisible ∧ μ'.IsVisible
```

`Cslib.CCS.Act.isCo` (definition, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Basic.lean#L130))

> Checks that an action is the coaction of another. This is the Boolean version of `Act.Co`.

```lean
def isCo [DecidableEq Name] (μ μ' : Act Name) : Bool
```

`Cslib.CCS.Act.isCo_iff` (theorem, [line 135](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Basic.lean#L135))

```lean
theorem isCo_iff [DecidableEq Name] {μ μ' : Act Name} : isCo μ μ' ↔ Co μ μ'
```

`Cslib.CCS.Context` (inductive type, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Basic.lean#L146))

> Contexts.

```lean
inductive Context (Name : Type u) (Constant : Type v) : Type (max u v) where
  | hole
  | pre (μ : Act Name) (c : Context Name Constant)
  | parL (c : Context Name Constant) (q : Process Name Constant)
  | parR (p : Process Name Constant) (c : Context Name Constant)
  | choiceL (c : Context Name Constant) (q : Process Name Constant)
  | choiceR (p : Process Name Constant) (c : Context Name Constant)
  | res (a : Name) (c : Context Name Constant)
deriving DecidableEq
```

`Cslib.CCS.Context.fill` (definition, [line 158](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Basic.lean#L158))

> Replaces the hole in a `Context` with a `Process`.

```lean
def Context.fill (c : Context Name Constant) (p : Process Name Constant) : Process Name Constant
```

`Cslib.CCS.context_fill_def` (theorem, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Basic.lean#L172))

> Definition of context filling.

```lean
theorem context_fill_def (c : Context Name Constant) (p : Process Name Constant) :
  c<[p] = c.fill p
```

`Cslib.CCS.Context.complete` (theorem, [line 177](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Basic.lean#L177))

> Any `Process` can be obtained by filling a `Context` with an atom. This proves that `Context`
> is a complete formalisation of syntactic contexts for CCS.

```lean
theorem Context.complete (p : Process Name Constant) :
    ∃ c : Context Name Constant, p = c<[(Process.nil : Process Name Constant)] ∨
    ∃ k : Constant, p = c<[(Process.const k : Process Name Constant)]
```

## Depends on

- [Context](../../foundations/syntax/context.md)

## Sources

- [Cslib/Languages/CCS/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Basic.lean)
