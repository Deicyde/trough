---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN.lc_l, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN.step_to_redex, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN.to_redex, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN.steps_app_l_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN.lc_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN.steps_lc_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN.step_subst, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN.steps_subst
statement: formalized
proof: formalized
---

# Call-by-Name Evaluation

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.CallByName`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/CallByName.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/CallByName.lean), by Maximiliano Onofre Martínez.

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN` (inductive type, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/CallByName.lean#L28))

> A single step of Call-by-Name evaluation.

```lean
inductive CBN : Term Var → Term Var → Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN.lc_l` (lemma, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/CallByName.lean#L37))

> The left side of a Call-by-Name step is locally closed.

```lean
lemma CBN.lc_l (step : M ⭢ₙ N) : LC M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN.step_to_redex` (lemma, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/CallByName.lean#L41))

> A single Call-by-Name step is a full β-reduction.

```lean
lemma CBN.step_to_redex (step : M ⭢ₙ N) : M ↠βᶠ N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN.to_redex` (lemma, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/CallByName.lean#L47))

> Call-by-Name reduction is contained in full β-reduction.

```lean
lemma CBN.to_redex (step : M ↠ₙ N) : M ↠βᶠ N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN.steps_app_l_cong` (lemma, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/CallByName.lean#L53))

> Left congruence rule for application in Call-by-Name reduction.

```lean
lemma CBN.steps_app_l_cong (step : M ↠ₙ M') (lc_N : LC N) : Term.app M N ↠ₙ Term.app M' N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN.lc_r` (lemma, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/CallByName.lean#L61))

> The right side of a Call-by-Name step is locally closed.

```lean
lemma CBN.lc_r (step : M ⭢ₙ N) : LC N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN.steps_lc_r` (lemma, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/CallByName.lean#L65))

> The right side of a Call-by-Name reduction is locally closed.

```lean
lemma CBN.steps_lc_r (lc_M : LC M) (step : M ↠ₙ N) : LC N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN.step_subst` (lemma, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/CallByName.lean#L71))

> Substitution preserves a single Call-by-Name step.

```lean
lemma CBN.step_subst (x : Var) (h : M ⭢ₙ M') (lc_N : LC N) :
    M[x := N] ⭢ₙ M'[x := N]
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.CBN.steps_subst` (lemma, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/CallByName.lean#L78))

> Substitution preserves Call-by-Name reduction.

```lean
lemma CBN.steps_subst (x : Var) (step : M ↠ₙ M') (lc_N : LC N) :
    M[x := N] ↠ₙ M'[x := N]
```

## Depends on

- [β-reduction for the λ-calculus](fullbeta.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/CallByName.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/CallByName.lean)
