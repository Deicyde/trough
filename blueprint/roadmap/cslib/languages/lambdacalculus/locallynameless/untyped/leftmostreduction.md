---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaNormal, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaNormal.app_inv, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaNormal.abs_open, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.steps_isAbs_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.steps_app_l_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.app_r_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.steps_app_r_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.steps_app_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.of_cbn, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.steps_lc_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.steps_abs_close, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.steps_abs_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.of_standard, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.normalization
statement: formalized
proof: formalized
---

# The Leftmost Reduction Theorem

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.LeftmostReduction`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean), by Maximiliano Onofre Martínez.

> ## Reference
>
> * [M. Copes, *A machine-checked proof of the Standardization Theorem in λ-calculus*][Copes2018]

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaNormal` (definition, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean#L33))

> A term is in normal form when it contains no β-redexes.

```lean
def BetaNormal (m : Term Var) : Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost` (abbreviation, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean#L37))

> Leftmost reduction: a β-reduction contracting the redex at position 0.

```lean
abbrev Leftmost : Term Var → Term Var → Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaNormal.app_inv` (lemma, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean#L43))

> In a normal-form application, both sides are normal and the operator is not an
> abstraction.

```lean
lemma BetaNormal.app_inv (h : BetaNormal (app L M)) :
    ¬IsAbs L ∧ BetaNormal L ∧ BetaNormal M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaNormal.abs_open` (lemma, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean#L48))

> The body of a normal-form abstraction opens to a normal form.

```lean
lemma BetaNormal.abs_open {x : Var} (h : BetaNormal (abs M)) : BetaNormal (M ^ fvar x)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.steps_isAbs_r` (lemma, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean#L53))

> Leftmost reduction preserves being an abstraction.

```lean
lemma Leftmost.steps_isAbs_r (h : M ↠ℓ N) (ha : IsAbs M) : IsAbs N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.steps_app_l_cong` (lemma, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean#L59))

> Left congruence for leftmost reduction, provided the target is not an abstraction.

```lean
lemma Leftmost.steps_app_l_cong (h : L ↠ℓ L') (hna : ¬IsAbs L') :
    app L M ↠ℓ app L' M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.BetaAt.app_r_cong` (lemma, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean#L68))

> Reducing the operand across a non-abstraction normal form keeps the position.

```lean
lemma BetaAt.app_r_cong (h : BetaAt i M M') (hL : BetaNormal L) (hna : ¬IsAbs L) :
    BetaAt i (app L M) (app L M')
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.steps_app_r_cong` (lemma, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean#L75))

> Right congruence for leftmost reduction, provided the operator is a non-abstraction
> normal form.

```lean
lemma Leftmost.steps_app_r_cong (h : M ↠ℓ M') (hL : BetaNormal L) (hna : ¬IsAbs L) :
    app L M ↠ℓ app L M'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.steps_app_cong` (lemma, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean#L83))

> Congruence for leftmost reduction on applications whose reduced operator is a
> non-abstraction normal form.

```lean
lemma Leftmost.steps_app_cong (hL : L ↠ℓ L') (hM : M ↠ℓ M')
    (hnf : BetaNormal L') (hna : ¬IsAbs L') : app L M ↠ℓ app L' M'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.of_cbn` (lemma, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean#L88))

> Call-by-Name reduction is contained in leftmost reduction.

```lean
lemma Leftmost.of_cbn (h : M ↠ₙ N) : M ↠ℓ N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.steps_lc_r` (lemma, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean#L96))

> Leftmost reduction preserves local closure.

```lean
lemma Leftmost.steps_lc_r (h : M ↠ℓ M') (lc : LC M) : LC M'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.steps_abs_close` (lemma, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean#L102))

> Leftmost reduction is preserved by closing a variable and abstracting.

```lean
lemma Leftmost.steps_abs_close {x : Var} (h : M ↠ℓ M') (lc : LC M) :
    (M⟦0 ↜ x⟧.abs) ↠ℓ (M'⟦0 ↜ x⟧.abs)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.steps_abs_cong` (lemma, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean#L109))

> Cofinite congruence rule for leftmost reduction under an abstraction.

```lean
lemma Leftmost.steps_abs_cong (xs : Finset Var)
    (cofin : ∀ x ∉ xs, (M ^ fvar x) ↠ℓ (M' ^ fvar x)) (lc : LC (abs M)) :
    abs M ↠ℓ abs M'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.of_standard` (theorem, [line 119](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean#L119))

> A standard reduction to a normal form is a leftmost reduction.

```lean
theorem Leftmost.of_standard (h : M ⭢ₛ N) (hn : BetaNormal N) : M ↠ℓ N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Leftmost.normalization` (theorem, [line 137](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean#L137))

> The leftmost reduction theorem: if a term β-reduces to a normal form, then leftmost
> reduction reaches it.

```lean
theorem Leftmost.normalization (lc : LC M) (h : M ↠βᶠ N) (hn : BetaNormal N) : M ↠ℓ N
```

## Depends on

- [Standard Reduction and the Standardization Theorem](standardreduction.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LeftmostReduction.lean)
