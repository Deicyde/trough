---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Beta, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.step_lc_l, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.redex_app_l_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.redex_app_r_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.invert_step_app_fvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.step_lc_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.steps_lc_or_rfl, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.redex_subst_cong_lc, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.redex_subst_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.step_not_fv, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.step_abs_close, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.redex_abs_close, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.step_abs_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.redex_abs_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.step_open_cong_l, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.invert_steps_abs, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.steps_open_cong_l_abs, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.step_subst_cong_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.steps_subst_cong_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.steps_open_cong_abs
statement: formalized
proof: formalized
---

# β-reduction for the λ-calculus

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.FullBeta`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean), by Chris Henson.

> ## References
>
> * [A. Chargueraud, *The Locally Nameless Representation*] [Chargueraud2012]
> * See also https://www.cis.upenn.edu/~plclub/popl08-tutorial/code/, from which
>   this is partially adapted

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Beta` (inductive type, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L37))

> A single β-reduction step.

```lean
inductive Beta : Term Var → Term Var → Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta` (abbreviation, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L43))

> Full β-reduction.

```lean
abbrev FullBeta : Term Var → Term Var → Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.step_lc_l` (lemma, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L51))

> The left side of a reduction is locally closed.

```lean
lemma step_lc_l (step : M ⭢βᶠ M') : LC M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.redex_app_l_cong` (theorem, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L55))

> Left congruence rule for application in multiple reduction.

```lean
theorem redex_app_l_cong (redex : M ↠βᶠ M') (lc_N : LC N) : app M N ↠βᶠ app M' N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.redex_app_r_cong` (theorem, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L60))

> Right congruence rule for application in multiple reduction.

```lean
theorem redex_app_r_cong (redex : M ↠βᶠ M') (lc_N : LC N) : app N M ↠βᶠ app N M'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.invert_step_app_fvar` (lemma, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L66))

```lean
lemma invert_step_app_fvar (step : app M (fvar x) ⭢βᶠ N) :
    (∃ M', N = app M' (fvar x) ∧ M ⭢βᶠ M') ∨ (∃ M1, M = abs M1 ∧ N = M1 ^ fvar x)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.step_lc_r` (lemma, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L77))

> The right side of a reduction is locally closed.

```lean
lemma step_lc_r (step : M ⭢βᶠ M') : LC M'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.steps_lc_or_rfl` (lemma, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L79))

```lean
lemma steps_lc_or_rfl {M M' : Term Var} (redex : M ↠βᶠ M') : (LC M ∧ LC M') ∨ M = M'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.redex_subst_cong_lc` (lemma, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L83))

> Substitution of a locally closed term respects a single reduction step.

```lean
lemma redex_subst_cong_lc (s s' t : Term Var) (x : Var) (step : s ⭢βᶠ s') (h_lc : LC t) :
    s[x := t] ⭢βᶠ s'[x := t]
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.redex_subst_cong` (lemma, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L95))

> Substitution respects a single reduction step of a free variable.

```lean
lemma redex_subst_cong (s s' : Term Var) (x y : Var) (step : s ⭢βᶠ s') :
    s[x := fvar y] ⭢βᶠ s'[x := fvar y]
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.step_not_fv` (lemma, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L100))

> An β-reduction step does not introduce new free variables.

```lean
lemma step_not_fv (step : M ⭢βᶠ N) : N.fv ⊆ M.fv
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.step_abs_close` (lemma, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L110))

> Abstracting then closing preserves a single reduction.

```lean
lemma step_abs_close {x : Var} (step : M ⭢βᶠ M') : M⟦0 ↜ x⟧.abs ⭢βᶠ M'⟦0 ↜ x⟧.abs
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.redex_abs_close` (lemma, [line 114](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L114))

> Abstracting then closing preserves multiple reductions.

```lean
lemma redex_abs_close {x : Var} (step : M ↠βᶠ M') : (M⟦0 ↜ x⟧.abs ↠βᶠ M'⟦0 ↜ x⟧.abs)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.step_abs_cong` (theorem, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L121))

> Multiple reduction of opening implies multiple reduction of abstraction.

```lean
theorem step_abs_cong (xs : Finset Var) (cofin : ∀ x ∉ xs, (M ^ fvar x) ⭢βᶠ (M' ^ fvar x)) :
    M.abs ⭢βᶠ M'.abs
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.redex_abs_cong` (theorem, [line 128](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L128))

> Multiple reduction of opening implies multiple reduction of abstraction.

```lean
theorem redex_abs_cong (xs : Finset Var) (cofin : ∀ x ∉ xs, (M ^ fvar x) ↠βᶠ (M' ^ fvar x)) :
    M.abs ↠βᶠ M'.abs
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.step_open_cong_l` (lemma, [line 135](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L135))

```lean
lemma step_open_cong_l
  (s s' t) (L : Finset Var) (step : ∀ x ∉ L, (s ^ fvar x) ⭢βᶠ (s' ^ fvar x)) (h_lc : LC t) :
    (s ^ t) ⭢βᶠ (s' ^ t)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.invert_steps_abs` (lemma, [line 142](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L142))

```lean
lemma invert_steps_abs {s t : Term Var} (step : s.abs ↠βᶠ t) :
    ∃ (s' : Term Var), s.abs ↠βᶠ s'.abs ∧ t = s'.abs
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.steps_open_cong_l_abs` (lemma, [line 149](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L149))

```lean
lemma steps_open_cong_l_abs
  (s s' t : Term Var) (steps : s.abs ↠βᶠ s'.abs) (lc_t : LC t) :
    (s ^ t) ↠βᶠ (s' ^ t)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.step_subst_cong_r` (lemma, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L170))

```lean
lemma step_subst_cong_r {x : Var} (s t t' : Term Var) (step : t ⭢βᶠ t') (h_lc : LC s) :
    (s[x := t]) ↠βᶠ (s[x := t'])
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.steps_subst_cong_r` (lemma, [line 183](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L183))

```lean
lemma steps_subst_cong_r {x : Var} (s t t' : Term Var) (step : t ↠βᶠ t') (h_lc : LC s) :
    (s[x := t]) ↠βᶠ (s[x := t'])
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.steps_open_cong_abs` (lemma, [line 190](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean#L190))

```lean
lemma steps_open_cong_abs (s s' t t' : Term Var)
  (step1 : t ↠βᶠ t') (step2 : s.abs ↠βᶠ s'.abs) (lc_t : LC t) (lc_s : LC s.abs) :
    (s ^ t) ↠βᶠ (s' ^ t')
```

## Depends on

- [Congruence for the λ-calculus](congruence.md)

## Proof depends on

- [Properties](properties.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBeta.lean)
