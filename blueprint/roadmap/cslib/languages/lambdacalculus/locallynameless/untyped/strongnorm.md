---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_step, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_steps, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_fvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_app, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_app_left, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_app_right, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Neutral, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.neutral_step, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.neutral_steps, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_neutral, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_abs, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_abs_app_multiApp
statement: formalized
proof: formalized
---

# Untyped/StrongNorm

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.StrongNorm`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StrongNorm.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StrongNorm.lean), by David Wegmann.

> Strong normalization (termination) for full beta-reduction of untyped lambda calculus.

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_step` (lemma, [line 31](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StrongNorm.lean#L31))

> A single β-reduction step preserves strong normalization.

```lean
lemma sn_step (t_st_t' : t ⭢βᶠ t') (sn_t : SN FullBeta t) : SN FullBeta t'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_steps` (lemma, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StrongNorm.lean#L35))

> Multiple β-reduction steps also preserve strong normalization.

```lean
lemma sn_steps (t_st_t' : t ↠βᶠ t') (sn_t : SN FullBeta t) : SN FullBeta t'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_fvar` (lemma, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StrongNorm.lean#L40))

> Free variables are strongly normalizing.

```lean
lemma sn_fvar {x : Var} : SN FullBeta (fvar x)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_app` (lemma, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StrongNorm.lean#L46))

> An application is strongly normalizing if the left and right terms are strongly normalizing,
> as well as all possible future top level abstraction application beta reductions

```lean
lemma sn_app (t s : Term Var) (sn_t : SN FullBeta t) (sn_s : SN FullBeta s)
    (hβ : ∀ {t' s' : Term Var}, t ↠βᶠ t'.abs → s ↠βᶠ s' → SN FullBeta (t' ^ s')) :
    SN FullBeta (t.app s)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_app_left` (lemma, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StrongNorm.lean#L62))

> The left side of a strongly normalizing application is strongly normalizing.

```lean
lemma sn_app_left (M N : Term Var) (lc_N : Term.LC N) (sn_MN : SN FullBeta (M.app N)) :
    SN FullBeta M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_app_right` (lemma, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StrongNorm.lean#L68))

> The right side of a strongly normalizing application is strongly normalizing.

```lean
lemma sn_app_right (M N : Term Var) (lc_M : Term.LC M) (sn_MN : SN FullBeta (M.app N)) :
    SN FullBeta N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Neutral` (inductive type, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StrongNorm.lean#L76))

> A neutral term is a term of the form v t₁ … t_n where
> v is a variable and t₁ … t_n are strongly normalizing terms.

```lean
inductive Neutral : Term Var → Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.neutral_step` (lemma, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StrongNorm.lean#L87))

> Neutral terms only reduce to other neutral terms in a single step

```lean
lemma neutral_step (Hneut : Neutral t) (Hstep : t ⭢βᶠ t') : Neutral t'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.neutral_steps` (lemma, [line 91](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StrongNorm.lean#L91))

> Neutral terms only reduce to other neutral terms in multiple steps

```lean
lemma neutral_steps (Hneut : Neutral t) (Hsteps : t ↠βᶠ t') : Neutral t'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_neutral` (lemma, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StrongNorm.lean#L96))

> Neutral terms are strongly normalizing.

```lean
lemma sn_neutral (Hneut : Neutral t) : SN FullBeta t
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_abs` (lemma, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StrongNorm.lean#L104))

> A lambda abstraction is strongly normalizing if its body is strongly normalizing.

```lean
lemma sn_abs [DecidableEq Var] [HasFresh Var] {M N : Term Var} (sn_MN : SN FullBeta (M ^ N))
    (lc_N : LC N) : SN FullBeta (abs M)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.sn_abs_app_multiApp` (lemma, [line 120](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StrongNorm.lean#L120))

> A term of the form λ M N P_1 … P_n is strongly normalizing if
> 1. N is strongly normalizing,
> 1. M ^ N P₁ … Pₙ is strongly normalizing,
> 1. N is locally closed,
> 1. M ^ N P₁ … Pₙ is locally closed

```lean
lemma sn_abs_app_multiApp [DecidableEq Var] [HasFresh Var] {Ps} {M N : Term Var}
    (sn_N : SN FullBeta N) (sn_MNPs : SN FullBeta (multiApp (M ^ N) Ps))
    (lc_N : LC N) (lc_MNPs : LC (multiApp (M ^ N) Ps)) :
    SN FullBeta (multiApp (M.abs.app N) Ps)
```

## Depends on

- [Relations: Definitions](../../../../foundations/relation/defs.md)
- [MultiApp](multiapp.md)

## Proof depends on

- [Termination (well-foundedness) properties of relations](../../../../foundations/relation/termination.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StrongNorm.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StrongNorm.lean)
