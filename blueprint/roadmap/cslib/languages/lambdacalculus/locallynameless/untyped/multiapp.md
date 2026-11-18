---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiApp, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.ListFullBeta, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiApp_tail, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiApp_lc, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.step_multiApp_l, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.steps_multiApp_l, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.step_multiApp_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.steps_multiApp_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.listFullBeta_cons_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.listFullBeta_cons_l, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.invert_abs_multiApp_st, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.invert_abs_multiApp_mst, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiApp_step_lc_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiApp_steps_lc
statement: formalized
proof: formalized
---

# MultiApp

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.MultiApp`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean), by David Wegmann.

> Multiple application for untyped lambda calculus.

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiApp` (definition, [line 29](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean#L29))

> multiApp f [x₁, x₂, ..., xₙ] applies the arguments x₁, x₂, ..., xₙ
> to f in left-associative order, i.e. as (((f x₁) x₂) ... xₙ).

```lean
def multiApp (f : Term Var) : List (Term Var) → Term Var
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.ListFullBeta` (inductive type, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean#L40))

> A list of arguments performs a single reduction step
>
> [x₁, ..., xᵢ ..., xₙ] ⭢βᶠ [x₁, ..., xᵢ', ..., xₙ]
>
> if one of the arguments performs a single step xᵢ ⭢βᶠ xᵢ'
> and the rest of the arguments are locally closed.

```lean
inductive ListFullBeta : List (Term Var) → List (Term Var) → Prop where
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiApp_tail` (lemma, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean#L48))

```lean
lemma multiApp_tail {N} : (M.multiApp (Ns ++ [N])) = (M.multiApp Ns).app  N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiApp_lc` (lemma, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean#L56))

> A term resulting from a multi-application is locally closed if
> and only if the leftmost term and all arguments applied to it are locally closed

```lean
lemma multiApp_lc : LC (M.multiApp Ns) ↔ LC M ∧ (∀ N ∈ Ns, LC N)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.step_multiApp_l` (lemma, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean#L62))

> Just like ordinary beta reduction, the left-hand side
> of a multi-application step is locally closed

```lean
lemma step_multiApp_l (steps : M ⭢βᶠ M') (lc_Ns : ∀ N ∈ Ns, LC N) :
    M.multiApp Ns ⭢βᶠ M'.multiApp Ns
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.steps_multiApp_l` (lemma, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean#L70))

> Congruence lemma for multi reduction of the left most term of a multi-application

```lean
lemma steps_multiApp_l (steps : M ↠βᶠ M') (lc_Ns : ∀ N ∈ Ns, LC N) :
    M.multiApp Ns ↠βᶠ M'.multiApp Ns
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.step_multiApp_r` (lemma, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean#L76))

> Congruence lemma for single reduction of one of the arguments of a multi-application

```lean
lemma step_multiApp_r (steps : Ns ⭢lβᶠ Ns') (lc_M : LC M) : M.multiApp Ns ⭢βᶠ M.multiApp Ns'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.steps_multiApp_r` (lemma, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean#L80))

> Congruence lemma for multiple reduction of one of the arguments of a multi-application

```lean
lemma steps_multiApp_r (steps : Ns ↠lβᶠ Ns') (lc_M : LC M) : M.multiApp Ns ↠βᶠ M.multiApp Ns'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.listFullBeta_cons_r` (lemma, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean#L83))

```lean
lemma listFullBeta_cons_r (h : Ns ⭢lβᶠ Ns') (h_lc : ∀ M ∈ l, LC M) : (l ++ Ns) ⭢lβᶠ (l ++ Ns')
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.listFullBeta_cons_l` (lemma, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean#L86))

```lean
lemma listFullBeta_cons_l (h : Ns ⭢lβᶠ Ns') (h_lc : ∀ M ∈ l, LC M) : (Ns ++ l) ⭢lβᶠ (Ns' ++ l)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.invert_abs_multiApp_st` (lemma, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean#L97))

> If a term (λ M) N P_1 ... P_n reduces in a single step to Q, then
> Q must be one of the following forms:
>
> Q = (λ M') N P₁ ... Pₙ where M ⭢βᶠ M' or
> Q = (λ M) N' P₁ ... Pₙ where N ⭢βᶠ N' or
> Q = (λ M) N P₁' ... Pₙ' where P_i ⭢βᶠ P_i' for some i or
> Q = (M ^ N) P₁ ... Pₙ

```lean
lemma invert_abs_multiApp_st {Ps} {M N Q : Term Var}
  (h_red : multiApp (M.abs.app N) Ps ⭢βᶠ Q) :
    (∃ M', M.abs ⭢βᶠ Term.abs M' ∧ Q = multiApp (M'.abs.app N) Ps) ∨
    (∃ N', N ⭢βᶠ N' ∧ Q = multiApp (M.abs.app N') Ps) ∨
    (∃ Ps', Ps ⭢lβᶠ Ps' ∧ Q = multiApp (M.abs.app N) Ps') ∨
    (Q = multiApp (M ^ N) Ps)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.invert_abs_multiApp_mst` (lemma, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean#L132))

> If a term (λ M) N P₁ ... Pₙ reduces in multiple steps to Q, then either Q if of the form
>
>    Q = (λ M') N' P'₁ ... P'ₙ
>
>    or
>
>  we first reach an intermediate term of this shape,
>
>    (λ M) N P₁ ... Pₙ ↠βᶠ (λ M') N' P'₁ ... P'ₙ
>
>    then perform a beta reduction and reduce further to Q
>
>    (λ M') N' P'₁ ... P'ₙ ↠βᶠ M' ^ N' P'_₁ ... P'_ₙ ↠βᶠ Q
>
> where M ↠βᶠ M' and N ↠βᶠ N' and P_i ↠βᶠ P_i' for all i

```lean
lemma invert_abs_multiApp_mst {Ps} {M N Q : Term Var}
  (h_red : multiApp (M.abs.app N) Ps ↠βᶠ Q) :
    ∃ M' N' Ns', M.abs ↠βᶠ M'.abs ∧ N ↠βᶠ N' ∧ Ps ↠lβᶠ Ns' ∧
                 (Q = multiApp (M'.abs.app N') Ns' ∨
     (multiApp (M.abs.app N) Ps ↠βᶠ multiApp (M' ^ N') Ns' ∧
                                     multiApp (M' ^ N') Ns' ↠βᶠ Q))
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiApp_step_lc_r` (lemma, [line 151](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean#L151))

> Just like ordinary beta reduction, the right-hand side
> of a multi-application step is locally closed

```lean
lemma multiApp_step_lc_r (step : Ns ⭢lβᶠ Ns') : ∀ N ∈ Ns', LC N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.multiApp_steps_lc` (lemma, [line 155](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean#L155))

> Just like ordinary beta reduction, multiple steps of a argument list preserves local closure

```lean
lemma multiApp_steps_lc (step : Ns ↠lβᶠ Ns') (H : ∀ N ∈ Ns, LC N) : ∀ N ∈ Ns', LC N
```

## Depends on

- [β-reduction for the λ-calculus](fullbeta.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/MultiApp.lean)
