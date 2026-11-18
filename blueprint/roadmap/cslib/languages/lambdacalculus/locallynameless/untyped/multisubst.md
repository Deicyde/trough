---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Env, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiSubst, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Env.fv, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.envLC, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.envLC_cons, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiSubst_fvar_fresh, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiSubst_preserves_not_fvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiSubst_app, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiSubst_abs, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiSubst_open_var
statement: formalized
proof: formalized
---

# MultiSubst

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.MultiSubst`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiSubst.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiSubst.lean), by David Wegmann.

> Multiple substitution for untyped lambda calculus.

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Env` (abbreviation, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiSubst.lean#L32))

> An environment in context of multi substitution is a list of pairs of
> variable targets and terms to be substituted for that target

```lean
abbrev Env (Var : Type u)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiSubst` (definition, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiSubst.lean#L37))

> Multi-substitution substitutes all target variables
> in an environment by their corresponding terms

```lean
def multiSubst (E : Env Var) (M : Term Var) : Term Var
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Env.fv` (definition, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiSubst.lean#L45))

> The free variables of an environment are the union of
> the free variables of all terms in the environment.
> The target variables are not necessarily included

```lean
def Env.fv (E : Env Var) : Finset Var
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.envLC` (abbreviation, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiSubst.lean#L53))

> An environment is locally closed if all terms in the environment are locally closed

```lean
abbrev envLC (E : Env Var) : Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.envLC_cons` (lemma, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiSubst.lean#L56))

> Adding a locally closed term to an environment preserves local closure

```lean
lemma envLC_cons (lc_sub : LC sub) (lc_E : envLC E) : envLC (⟨ x, sub ⟩ :: E)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiSubst_fvar_fresh` (lemma, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiSubst.lean#L60))

> Multi-substitution of a fresh variable does nothing

```lean
lemma multiSubst_fvar_fresh (E : Env Var) : ∀ x ∉ E.dom, multiSubst E (fvar x) = fvar x
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiSubst_preserves_not_fvar` (lemma, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiSubst.lean#L65))

> If x is neither a free variable of an environment Ns or a term M, then
> x is also not a free variable of the multi-substitution of Ns into M

```lean
lemma multiSubst_preserves_not_fvar (M : Term Var) (E : Env Var) :
    (multiSubst E M).fv ⊆ M.fv ∪ E.fv
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiSubst_app` (lemma, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiSubst.lean#L70))

> Multi-substitution propagates recursively through an application

```lean
lemma multiSubst_app (M N : Term Var) (E : Env Var) :
    multiSubst E (app M N) = app (multiSubst E M) (multiSubst E N)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiSubst_abs` (lemma, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiSubst.lean#L75))

> Multi-substitution propagates recursively through an abstraction

```lean
lemma multiSubst_abs (M : Term Var) (E : Env Var) :
    multiSubst E (abs M) = abs (multiSubst E M)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiSubst_open_var` (lemma, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiSubst.lean#L82))

> Multi-substitution commutes with opening a term with a fresh variable,
> provided that the variable is not in the domain of the environment
> and the environment is locally closed

```lean
lemma multiSubst_open_var [HasFresh Var] (M : Term Var) (E : Env Var) (x : Var)
  (h_ndom : x ∉ E.dom) (h_lc : envLC E) :
    multiSubst E (M ^ fvar x) = multiSubst E M ^ fvar x
```

## Depends on

- [λ-calculus (Context)](../context.md)
- [LcAt](lcat.md)

## Proof depends on

- [Properties](properties.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiSubst.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiSubst.lean)
