---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.countRedexes, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.appNoAbsL, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.appAbsL, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.appNoAbsR, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.appAbsR, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.countRedexes_openRec_fvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.countRedexes_open_fvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.countRedexes_app_le, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.countRedexes_app_abs, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.isAbs_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.cbn_not_isAbs, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.of_cbn_step, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.countRedexes_subst_fvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.isAbs_subst_fvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.to_step, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.le_countRedexes, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.rename, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.lc_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.abs_close
statement: formalized
proof: formalized
---

# Redex Positions

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.BetaAt`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean), by Maximiliano Onofre Martínez.

> This module defines β-reduction at a given redex position and proves its basic properties.
>
> ## Reference
>
> * [M. Copes, *A machine-checked proof of the Standardization Theorem in λ-calculus*][Copes2018]

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.countRedexes` (definition, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L35))

> The number of β-redexes occurring in a term.

```lean
def countRedexes : Term Var → Nat
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt` (inductive type, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L44))

> `BetaAt i M N` reduces the redex at position `i` of `M` to obtain `N`;
> positions are counted from left to right.

```lean
inductive BetaAt : Nat → Term Var → Term Var → Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.appNoAbsL` (lemma, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L59))

> Reducing a non-abstraction operator keeps the position.

```lean
lemma BetaAt.appNoAbsL (h : BetaAt i M M') (hna : ¬IsAbs M) :
    BetaAt i (app M N) (app M' N)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.appAbsL` (lemma, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L64))

> Reducing an abstraction operator advances the position by one.

```lean
lemma BetaAt.appAbsL (h : BetaAt i M M') (ha : IsAbs M) :
    BetaAt (i + 1) (app M N) (app M' N)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.appNoAbsR` (lemma, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L69))

> Reducing the operand adds the redex count of a non-abstraction operator.

```lean
lemma BetaAt.appNoAbsR (h : BetaAt i M M') (hna : ¬IsAbs N) :
    BetaAt (i + countRedexes N) (app N M) (app N M')
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.appAbsR` (lemma, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L74))

> Reducing the operand adds the redex count of an abstraction operator, plus one.

```lean
lemma BetaAt.appAbsR (h : BetaAt i M M') (ha : IsAbs N) :
    BetaAt (i + countRedexes N + 1) (app N M) (app N M')
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.countRedexes_openRec_fvar` (lemma, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L79))

> Opening with a free variable preserves the number of redexes.

```lean
lemma countRedexes_openRec_fvar (M : Term Var) (k : Nat) (x : Var) :
    countRedexes (M⟦k ↝ fvar x⟧) = countRedexes M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.countRedexes_open_fvar` (lemma, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L88))

> Opening the outermost binder with a free variable preserves the number of redexes.

```lean
lemma countRedexes_open_fvar (M : Term Var) (x : Var) :
    countRedexes (M ^ fvar x) = countRedexes M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.countRedexes_app_le` (lemma, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L93))

> An application has at least as many redexes as its operator and operand combined.

```lean
lemma countRedexes_app_le (M N : Term Var) :
    countRedexes M + countRedexes N ≤ countRedexes (app M N)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.countRedexes_app_abs` (lemma, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L98))

> An application with an abstraction operator has one more redex than its parts.

```lean
lemma countRedexes_app_abs {M : Term Var} (ha : IsAbs M) (N : Term Var) :
    countRedexes (app M N) = countRedexes M + countRedexes N + 1
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.isAbs_r` (lemma, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L103))

> Contracting a redex of an abstraction yields an abstraction.

```lean
lemma BetaAt.isAbs_r (h : BetaAt i M N) (ha : IsAbs M) : IsAbs N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.cbn_not_isAbs` (lemma, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L109))

> The source of a Call-by-Name step is never an abstraction.

```lean
lemma cbn_not_isAbs (h : M ⭢ₙ N) : ¬IsAbs M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.of_cbn_step` (lemma, [line 115](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L115))

> A single Call-by-Name step contracts the redex at position `0`.

```lean
lemma BetaAt.of_cbn_step (h : M ⭢ₙ N) : BetaAt 0 M N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.countRedexes_subst_fvar` (lemma, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L123))

> Renaming a free variable preserves the number of redexes.

```lean
lemma countRedexes_subst_fvar [DecidableEq Var] (M : Term Var) (x y : Var) :
    countRedexes (M[x := fvar y]) = countRedexes M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.isAbs_subst_fvar` (lemma, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L132))

> Renaming a free variable preserves being an abstraction.

```lean
lemma isAbs_subst_fvar [DecidableEq Var] {x y : Var} : IsAbs (M[x := fvar y]) ↔ IsAbs M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.to_step` (lemma, [line 136](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L136))

> A `BetaAt` step is a full β-step.

```lean
lemma BetaAt.to_step [DecidableEq Var] (h : BetaAt i M N) (lc : LC M) : M ⭢βᶠ N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.le_countRedexes` (lemma, [line 155](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L155))

> The position of a contracted redex is at most the redex count of the result.

```lean
lemma BetaAt.le_countRedexes (h : BetaAt i M N) : i ≤ countRedexes N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.rename` (lemma, [line 175](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L175))

> Renaming a free variable preserves the position of the contracted redex.

```lean
lemma BetaAt.rename (h : BetaAt i M M') (x y : Var) :
    BetaAt i (M[x := fvar y]) (M'[x := fvar y])
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.lc_r` (lemma, [line 195](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L195))

> Contracting a redex preserves local closure.

```lean
lemma BetaAt.lc_r (h : BetaAt i M M') (lc : LC M) : LC M'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.abs_close` (lemma, [line 212](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean#L212))

> Closing a variable and abstracting preserves the position of the contracted redex.

```lean
lemma BetaAt.abs_close {x : Var} (h : BetaAt i M M') (lc : LC M) :
    BetaAt i (M⟦0 ↜ x⟧.abs) (M'⟦0 ↜ x⟧.abs)
```

## Depends on

- [Call-by-Name Evaluation](callbyname.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/BetaAt.lean)
