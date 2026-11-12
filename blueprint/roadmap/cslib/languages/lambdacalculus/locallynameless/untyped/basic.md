---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.openRec, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.openRec_bvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.openRec_fvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.openRec_app, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.openRec_abs, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.open', Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.closeRec, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.close, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.instHasSubstitutionTerm, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.fv, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.closeRec_bvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.closeRec_fvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.closeRec_app, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.closeRec_abs, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_bvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_fvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_app, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_abs, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_def
statement: formalized
proof: formalized
---

# λ-calculus (Basic)

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.Basic`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean), by Chris Henson.

> The untyped λ-calculus, with a locally nameless representation of syntax.
>
> ## References
>
> * [A. Chargueraud, *The Locally Nameless Representation*][Chargueraud2012]
> * See also <https://www.cis.upenn.edu/~plclub/popl08-tutorial/code/>, from which
>   this is partially adapted

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term` (inductive type, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L35))

> Syntax of locally nameless lambda terms, with free variables over `Var`.

```lean
inductive Term (Var : Type u)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.openRec` (definition, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L50))

> Variable opening of the ith bound variable.

```lean
def openRec (i : ℕ) (sub : Term Var) : Term Var → Term Var
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.openRec_bvar` (lemma, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L59))

```lean
lemma openRec_bvar : (bvar i')⟦i ↝ s⟧ = if i = i' then s else bvar i'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.openRec_fvar` (lemma, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L61))

```lean
lemma openRec_fvar : (fvar x)⟦i ↝ s⟧ = fvar x
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.openRec_app` (lemma, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L63))

```lean
lemma openRec_app : (app l r)⟦i ↝ s⟧ = app (l⟦i ↝ s⟧) (r⟦i ↝ s⟧)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.openRec_abs` (lemma, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L65))

```lean
lemma openRec_abs : M.abs⟦i ↝ s⟧ = M⟦i + 1 ↝ s⟧.abs
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.open'` (definition, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L69))

> Variable opening of the closest binding.

```lean
def open' {X} (e u)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.closeRec` (definition, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L76))

> Variable closing, replacing a free `fvar x` with `bvar k`

```lean
def closeRec (k : ℕ) (x : Var) : Term Var → Term Var
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.close` (definition, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L89))

> Variable closing of the closest binding.

```lean
def close {Var} [DecidableEq Var] (e u)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst` (definition, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L96))

> Substitution of a free variable to a term.

```lean
def subst (m : Term Var) (x : Var) (sub : Term Var) : Term Var
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.instHasSubstitutionTerm` (instance, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L104))

> `Term.subst` is a substitution for λ-terms. Gives access to the notation `m[x := n]`.

```lean
instance instHasSubstitutionTerm : HasSubstitution (Term Var) Var (Term Var)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.fv` (definition, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L109))

> Free variables of a term.

```lean
def fv : Term Var → Finset Var
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.closeRec_bvar` (lemma, [line 119](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L119))

```lean
lemma closeRec_bvar : (bvar i)⟦k ↜ x⟧ = bvar i
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.closeRec_fvar` (lemma, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L121))

```lean
lemma closeRec_fvar : (fvar x')⟦k ↜ x⟧ = if x = x' then bvar k else fvar x'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.closeRec_app` (lemma, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L123))

```lean
lemma closeRec_app : (app l r)⟦k ↜ x⟧ = app (l⟦k ↜ x⟧) (r⟦k ↜ x⟧)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.closeRec_abs` (lemma, [line 125](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L125))

```lean
lemma closeRec_abs : t.abs⟦k ↜ x⟧ = t⟦k + 1 ↜ x⟧.abs
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_bvar` (lemma, [line 129](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L129))

```lean
lemma subst_bvar : (bvar i : Term Var)[x := n] = bvar i
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_fvar` (lemma, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L131))

```lean
lemma subst_fvar : (fvar x')[x := n] = if x = x' then n else fvar x'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_app` (lemma, [line 133](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L133))

```lean
lemma subst_app {l r : Term Var} : (app l r)[x := n] = app (l[x := n]) (r[x := n])
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_abs` (lemma, [line 135](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L135))

```lean
lemma subst_abs {M : Term Var} : M.abs[x := n] = M[x := n].abs
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_def` (lemma, [line 137](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean#L137))

```lean
lemma subst_def (m : Term Var) (x : Var) (n : Term Var) : m.subst x n = m[x := n]
```

## Depends on

- [HasSubstitution](../../../../foundations/syntax/hassubstitution.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Basic.lean)
