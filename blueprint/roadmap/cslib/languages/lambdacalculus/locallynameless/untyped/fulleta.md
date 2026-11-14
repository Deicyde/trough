---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Eta, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.step_lc_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.step_lc_l, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.redex_app_l_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.redex_app_r_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.invert_step_app_fvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.step_not_fv, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.steps_fv, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.step_subst_cong_l, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.steps_subst_cong_l, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.step_abs_close, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.redex_abs_close, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.redex_abs_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.step_subst_cong_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.steps_subst_cong_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.step_open_cong_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.steps_open_cong_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.close_eta_steps
statement: formalized
proof: formalized
---

# η-reduction for the λ-calculus

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.FullEta`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean), by Maximiliano Onofre Martínez.

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Eta` (inductive type, [line 29](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L29))

> A single η-reduction step.

```lean
inductive Eta : Term Var → Term Var → Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta` (abbreviation, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L35))

> Full η-reduction, defined as the congruence closure of the base η-rule.

```lean
abbrev FullEta : Term Var → Term Var → Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.step_lc_r` (lemma, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L43))

> The right side of an η-reduction is locally closed.

```lean
lemma step_lc_r (step : M ⭢ηᶠ M') : LC M'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.step_lc_l` (lemma, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L47))

> The left side of an η-reduction is locally closed.

```lean
lemma step_lc_l [HasFresh Var] (step : M ⭢ηᶠ M') : LC M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.redex_app_l_cong` (theorem, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L53))

> Left congruence rule for application in multiple reduction.

```lean
theorem redex_app_l_cong (redex : M ↠ηᶠ M') (lc_N : LC N) : app M N ↠ηᶠ app M' N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.redex_app_r_cong` (theorem, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L57))

> Right congruence rule for application in multiple reduction.

```lean
theorem redex_app_r_cong (redex : M ↠ηᶠ M') (lc_N : LC N) : app N M ↠ηᶠ app N M'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.invert_step_app_fvar` (lemma, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L63))

```lean
lemma invert_step_app_fvar (step : (app M (fvar x)) ⭢ηᶠ N) :
    ∃ M', N = app M' (fvar x) ∧ M ⭢ηᶠ M'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.step_not_fv` (lemma, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L72))

> An η-reduction step does not introduce new free variables.

```lean
lemma step_not_fv (step : M ⭢ηᶠ M') : M.fv = M'.fv
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.steps_fv` (lemma, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L80))

```lean
lemma steps_fv (steps : M ↠ηᶠ M') : M.fv = M'.fv
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.step_subst_cong_l` (lemma, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L84))

```lean
lemma step_subst_cong_l {x : Var} (s s' N : Term Var) (step : s ⭢ηᶠ s') (lc_N : LC N) :
    s[x := N] ⭢ηᶠ s'[x := N]
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.steps_subst_cong_l` (lemma, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L92))

```lean
lemma steps_subst_cong_l {x : Var} (s s' N : Term Var) (steps : s ↠ηᶠ s') (lc_N : LC N) :
    s[x := N] ↠ηᶠ s'[x := N]
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.step_abs_close` (lemma, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L99))

> Abstracting then closing preserves a single η-reduction step.

```lean
lemma step_abs_close {x} (step : M ⭢ηᶠ M') : (M ^* x).abs ⭢ηᶠ (M' ^* x).abs
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.redex_abs_close` (lemma, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L104))

> Abstracting then closing preserves multiple reductions.

```lean
lemma redex_abs_close {x} (steps : M ↠ηᶠ M') : (M ^* x).abs ↠ηᶠ (M' ^* x).abs
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.redex_abs_cong` (theorem, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L110))

> Multiple reduction of opening implies multiple reduction of abstraction.

```lean
theorem redex_abs_cong {M M' : Term Var} (xs : Finset Var)
    (cofin : ∀ x ∉ xs, (M ^ fvar x) ↠ηᶠ M' ^ fvar x) :
    M.abs ↠ηᶠ M'.abs
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.step_subst_cong_r` (lemma, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L118))

```lean
lemma step_subst_cong_r {x : Var} (s t t' : Term Var) (st : t ⭢ηᶠ t') (lc_s : LC s) :
    s[x := t] ↠ηᶠ s[x := t']
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.steps_subst_cong_r` (lemma, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L131))

```lean
lemma steps_subst_cong_r {x : Var} (s t t' : Term Var) (st : t ↠ηᶠ t') (lc_s : LC s) :
    s[x := t] ↠ηᶠ s[x := t']
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.step_open_cong_r` (lemma, [line 138](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L138))

```lean
lemma step_open_cong_r {s t t' : Term Var} (lc_s : LC s.abs) (step : t ⭢ηᶠ t') :
    (s ^ t) ↠ηᶠ s ^ t'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.steps_open_cong_r` (lemma, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L146))

```lean
lemma steps_open_cong_r {s t t' : Term Var} (lc_s : LC s.abs) (steps : t ↠ηᶠ t') :
    (s ^ t) ↠ηᶠ s ^ t'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullEta.close_eta_steps` (lemma, [line 154](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean#L154))

```lean
lemma close_eta_steps (hx_M : x ∉ M.fv) (st_M : ReflGen FullEta (M ^ fvar x) N) :
    ReflGen FullEta M.abs (N ^* x).abs
```

## Depends on

- [Congruence for the λ-calculus](congruence.md)

## Proof depends on

- [Properties](properties.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEta.lean)
