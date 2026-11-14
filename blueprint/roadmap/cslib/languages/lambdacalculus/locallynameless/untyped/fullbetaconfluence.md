---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Parallel, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.para_lc_l, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Parallel.lc_refl, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.para_lc_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.le_parallel, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Parallel.le_reflTransGen_fullBeta, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.reflTransGen_parallel_fullBeta, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.para_subst, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.para_open_close, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.para_open_out, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.parallel_diamond, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.confluent_parallel, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.confluent_fullBeta
statement: formalized
proof: formalized
---

# β-confluence for the λ-calculus

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.FullBetaConfluence`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean), by Chris Henson.

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Parallel` (inductive type, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean#L30))

> A parallel β-reduction step.

```lean
inductive Parallel : Term Var → Term Var → Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.para_lc_l` (lemma, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean#L53))

> The left side of a parallel reduction is locally closed.

```lean
lemma para_lc_l (step : M ⭢ₚ N) : LC M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Parallel.lc_refl` (lemma, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean#L61))

> Parallel reduction is reflexive for locally closed terms.

```lean
lemma Parallel.lc_refl (M : Term Var) (lc : LC M) : M ⭢ₚ M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.para_lc_r` (lemma, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean#L69))

> The right side of a parallel reduction is locally closed.

```lean
lemma para_lc_r (step : M ⭢ₚ N) : LC N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.FullBeta.le_parallel` (lemma, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean#L77))

> The inclusion `(· ⭢βᶠ ·) ≤ (· ⭢ₚ ·)`.

```lean
lemma FullBeta.le_parallel :
    ((· ⭢βᶠ ·) : Term Var → Term Var → Prop) ≤ (· ⭢ₚ ·)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Parallel.le_reflTransGen_fullBeta` (lemma, [line 90](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean#L90))

> The inclusion `(· ⭢ₚ ·) ≤ (· ↠βᶠ ·)`.

```lean
lemma Parallel.le_reflTransGen_fullBeta :
    ((· ⭢ₚ ·) : Term Var → Term Var → Prop) ≤ (· ↠βᶠ ·)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.reflTransGen_parallel_fullBeta` (theorem, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean#L113))

> Multiple parallel reduction is equal to multiple β-reduction.

```lean
theorem reflTransGen_parallel_fullBeta :
    ((· ↠ₚ ·) : Term Var → Term Var → Prop) = (· ↠βᶠ ·)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.para_subst` (lemma, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean#L121))

> Parallel reduction respects substitution.

```lean
lemma para_subst (x : Var) (pm : M ⭢ₚ M') (pn : N ⭢ₚ N') : M[x := N] ⭢ₚ M'[x := N']
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.para_open_close` (lemma, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean#L131))

> Parallel substitution respects closing and opening.

```lean
lemma para_open_close (x y z) (para : M ⭢ₚ M') : M⟦z ↜ x⟧⟦z ↝ fvar y⟧ ⭢ₚ M'⟦z ↜ x⟧⟦z ↝ fvar y⟧
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.para_open_out` (lemma, [line 135](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean#L135))

> Parallel substitution respects fresh opening.

```lean
lemma para_open_out (L : Finset Var) (mem : ∀ x, x ∉ L → (M ^ fvar x) ⭢ₚ N ^ fvar x)
    (para : M' ⭢ₚ N') : (M ^ M') ⭢ₚ (N ^ N')
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.parallel_diamond` (theorem, [line 144](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean#L144))

> Parallel reduction has the diamond property.

```lean
theorem parallel_diamond : Diamond ((· ⭢ₚ ·) : Term Var → Term Var → Prop)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.confluent_parallel` (theorem, [line 207](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean#L207))

> Parallel reduction is confluent.

```lean
theorem confluent_parallel : Confluent ((· ⭢ₚ ·) : Term Var → Term Var → Prop)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.confluent_fullBeta` (theorem, [line 212](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean#L212))

> β-reduction is confluent.

```lean
theorem confluent_fullBeta : Confluent ((· ⭢βᶠ ·) : Term Var → Term Var → Prop)
```

## Depends on

- [Relations: Definitions](../../../../foundations/relation/defs.md)
- [β-reduction for the λ-calculus](fullbeta.md)

## Proof depends on

- [Relations: Confluence](../../../../foundations/relation/confluence.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaConfluence.lean)
