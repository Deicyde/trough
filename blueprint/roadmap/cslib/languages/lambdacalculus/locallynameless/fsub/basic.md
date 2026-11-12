---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term, Cslib.LambdaCalculus.LocallyNameless.Fsub.Binding, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.fv, Cslib.LambdaCalculus.LocallyNameless.Fsub.Binding.fv, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.fvTy, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.fvTm, Cslib.LambdaCalculus.LocallyNameless.Fsub.Env
statement: formalized
proof: formalized
---

# λ-calculus (Basic)

`Cslib.Languages.LambdaCalculus.LocallyNameless.Fsub.Basic`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Basic.lean), by Chris Henson.

> The λ-calculus with polymorphism and subtyping, with a locally nameless representation of syntax.
>
> ## References
>
> * [A. Chargueraud, *The Locally Nameless Representation*][Chargueraud2012]
> * See also <https://www.cis.upenn.edu/~plclub/popl08-tutorial/code/>, from which
>   this is adapted

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty` (inductive type, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Basic.lean#L33))

> Types of the polymorphic lambda calculus.

```lean
inductive Ty (Var : Type*)
  /-- The type ⊤, with a single inhabitant. -/
  | top : Ty Var
  /-- Bound variables that appear in a type, using a de-Bruijn index. -/
  | bvar : ℕ → Ty Var
  /-- Free type variables. -/
  | fvar : Var → Ty Var
  /-- A function type. -/
  | arrow : Ty Var → Ty Var → Ty Var
  /-- A universal quantification. -/
  | all : Ty Var → Ty Var → Ty Var
  /-- A sum type. -/
  | sum : Ty Var → Ty Var → Ty Var
  deriving Inhabited
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term` (inductive type, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Basic.lean#L49))

> Syntax of locally nameless lambda terms, with free variables over `Var`.

```lean
inductive Term (Var : Type*)
  /-- Bound term variables that appear under a lambda abstraction, using a de-Bruijn index. -/
  | bvar : ℕ → Term Var
  /-- Free term variables. -/
  | fvar : Var → Term Var
  /-- Lambda abstraction, introducing a new bound term variable. -/
  | abs : Ty Var → Term Var → Term Var
  /-- Function application. -/
  | app : Term Var → Term Var → Term Var
  /-- Type abstraction, introducing a new bound type variable. -/
  | tabs : Ty Var → Term Var → Term Var
  /-- Type application. -/
  | tapp : Term Var → Ty Var → Term Var
  /-- Binding of a term. -/
  | let' : Term Var → Term Var → Term Var
  /-- Left constructor of a sum. -/
  | inl : Term Var → Term Var
  /-- Right constructor of a sum. -/
  | inr : Term Var → Term Var
  /-- Case matching on a sum. -/
  | case : Term Var → Term Var → Term Var → Term Var
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Binding` (inductive type, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Basic.lean#L72))

> A context binding.

```lean
inductive Binding (Var : Type*)
  /-- Subtype binding. -/
  | sub : Ty Var → Binding Var
  /-- Type binding. -/
  | ty : Ty Var → Binding Var
  deriving Inhabited
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.fv` (definition, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Basic.lean#L81))

> Free variables of a type.

```lean
def Ty.fv : Ty Var → Finset Var
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Binding.fv` (definition, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Basic.lean#L88))

> Free variables of a binding.

```lean
def Binding.fv : Binding Var → Finset Var
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.fvTy` (definition, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Basic.lean#L93))

> Free type variables of a term.

```lean
def Term.fvTy : Term Var → Finset Var
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.fvTm` (definition, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Basic.lean#L102))

> Free term variables of a term.

```lean
def Term.fvTm : Term Var → Finset Var
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Env` (abbreviation, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Basic.lean#L110))

> A context of bindings.

```lean
abbrev Env (Var : Type*)
```

## Depends on

- [λ-calculus (Context)](../context.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Basic.lean)
