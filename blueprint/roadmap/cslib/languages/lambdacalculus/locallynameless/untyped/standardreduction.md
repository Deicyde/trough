---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.lc_l, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.lc_refl, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.lc_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.of_cbn_step, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.cbn_step_trans, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.cbn_trans, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.of_cbn, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.isAbs_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.head_leftmost, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.cbn_head, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.app_r_abs, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.app_r_noAbs, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.app_r_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.le_countRedexes_of_ne, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.app_l_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.app_l_cong_of_ne, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.app_r_tail, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.app_r_trans, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.app_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.subst, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.of_beta_step, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.to_redex, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.abs_inv, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.abs_subst, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.trans_step, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.trans_redex, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.trans, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.standardization, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.iff_redex, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.lc_r, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.abs_close, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.abs_cong, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.to_redex, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.to_seq, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.to_standard, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.iff_seq
statement: formalized
proof: formalized
---

# Standard Reduction and the Standardization Theorem

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.StandardReduction`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean), by Maximiliano Onofre Martínez.

> ## References
>
> * [B. Calisto, *Formalization in Coq of the Standardization Theorem for λ-calculus*][Calisto2022]
> * [M. Copes, *A machine-checked proof of the Standardization Theorem in λ-calculus*][Copes2018]

> ## Main definitions

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq` (inductive type, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L36))

> A standard β-reduction sequence contracts redexes at non-decreasing positions. The index
> `n` is the last position contracted.

```lean
inductive StandardSeq : Nat → Term Var → Term Var → Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard` (inductive type, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L44))

> The Standard reduction relation.

```lean
inductive Standard : Term Var → Term Var → Prop
```

> ## Basic properties

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.lc_l` (lemma, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L60))

> The left side of a standard reduction is locally closed.

```lean
lemma Standard.lc_l (step : M ⭢ₛ N) : LC M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.lc_refl` (lemma, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L66))

> Standard reduction is reflexive for locally closed terms.

```lean
lemma Standard.lc_refl (M : Term Var) (lc : LC M) : M ⭢ₛ M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.lc_r` (lemma, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L71))

> The right side of a standard reduction is locally closed.

```lean
lemma Standard.lc_r (step : M ⭢ₛ N) : LC N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.of_cbn_step` (lemma, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L77))

> A single Call-by-Name step is a standard reduction.

```lean
lemma Standard.of_cbn_step (step : M ⭢ₙ N) (lc_N : LC N) : M ⭢ₛ N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.cbn_step_trans` (lemma, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L87))

> A Call-by-Name step followed by a standard reduction is a standard reduction.

```lean
lemma Standard.cbn_step_trans (step : M ⭢ₙ P) (std : P ⭢ₛ N) : M ⭢ₛ N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.cbn_trans` (lemma, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L98))

> A Call-by-Name reduction followed by a standard reduction is a standard reduction.

```lean
lemma Standard.cbn_trans (h1 : M ↠ₙ P) (h2 : P ⭢ₛ N) : M ⭢ₛ N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.of_cbn` (lemma, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L104))

> Call-by-Name reduction is contained in standard reduction.

```lean
lemma Standard.of_cbn (step : M ↠ₙ N) (lc_N : LC N) : M ⭢ₛ N
```

> ## Standard sequences

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.isAbs_r` (lemma, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L110))

> Standard sequences preserve being an abstraction.

```lean
lemma StandardSeq.isAbs_r (h : StandardSeq n M N) (ha : IsAbs M) : IsAbs N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.head_leftmost` (lemma, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L116))

> A standard sequence preceded by a step at position `0` remains standard.

```lean
lemma StandardSeq.head_leftmost (seq : StandardSeq n P N) :
    ∀ {M}, BetaAt 0 M P → ∃ k, k ≤ n ∧ StandardSeq k M N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.cbn_head` (lemma, [line 126](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L126))

> A standard sequence stays standard when preceded by a Call-by-Name reduction.

```lean
lemma StandardSeq.cbn_head (h : M ↠ₙ P) (hseq : StandardSeq n P N) :
    ∃ k, StandardSeq k M N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.app_r_abs` (lemma, [line 135](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L135))

> Right congruence for standard sequences when the operator is an abstraction.

```lean
lemma StandardSeq.app_r_abs (h : StandardSeq n M M') (ha : IsAbs L) :
    StandardSeq (n + countRedexes L + 1) (app L M) (app L M')
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.app_r_noAbs` (lemma, [line 142](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L142))

> Right congruence for standard sequences when the operator is a non-abstraction.

```lean
lemma StandardSeq.app_r_noAbs (h : StandardSeq n M M') (hna : ¬IsAbs L) :
    StandardSeq (n + countRedexes L) (app L M) (app L M')
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.app_r_cong` (lemma, [line 149](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L149))

> Right application congruence for standard sequences.

```lean
lemma StandardSeq.app_r_cong (h : StandardSeq n M M') :
    ∃ k, StandardSeq k (app L M) (app L M') ∧
      k ≤ n + countRedexes L + (if IsAbs L then 1 else 0)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.le_countRedexes_of_ne` (lemma, [line 162](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L162))

> The final position of a nonempty standard sequence is at most its target's redex count.

```lean
lemma StandardSeq.le_countRedexes_of_ne (h : StandardSeq n M N) (hne : M ≠ N) :
    n ≤ countRedexes N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.app_l_cong` (lemma, [line 171](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L171))

> Reducing the operator of an application yields a standard sequence, with the final position
> bounded.

```lean
lemma StandardSeq.app_l_cong (h : StandardSeq n L L') :
    ∃ k, StandardSeq k (app L M) (app L' M) ∧
      k ≤ n + (if IsAbs L' then 1 else 0)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.app_l_cong_of_ne` (lemma, [line 187](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L187))

> A nonempty operator reduction lifts to the application, bounded by the operator's redex
> count.

```lean
lemma StandardSeq.app_l_cong_of_ne (h : StandardSeq n L L') (hne : L ≠ L') :
    ∃ k, StandardSeq k (app L M) (app L' M) ∧
      k ≤ countRedexes L' + (if IsAbs L' then 1 else 0)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.app_r_tail` (lemma, [line 196](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L196))

> Append an operand step to a standard sequence of applications.

```lean
lemma StandardSeq.app_r_tail (h : StandardSeq n (app L M) (app L' N))
    (step : BetaAt i N N')
    (hle : n ≤ i + countRedexes L' + (if IsAbs L' then 1 else 0)) :
    StandardSeq (i + countRedexes L' + (if IsAbs L' then 1 else 0))
      (app L M) (app L' N')
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.app_r_trans` (lemma, [line 205](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L205))

> Compose an application sequence with a standard reduction of its operand.

```lean
lemma StandardSeq.app_r_trans (h : StandardSeq n M M')
    (happ : StandardSeq i (app L M) (app L' M))
    (hc : i ≤ countRedexes L' + (if IsAbs L' then 1 else 0)) :
    ∃ d, StandardSeq d (app L M) (app L' M') ∧
      d ≤ n + countRedexes L' + (if IsAbs L' then 1 else 0)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.app_cong` (lemma, [line 218](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L218))

> If operator and operand each reduce by a standard sequence, so does the application.

```lean
lemma StandardSeq.app_cong (hL : StandardSeq n L L') (hM : StandardSeq b M M') :
    ∃ k, StandardSeq k (app L M) (app L' M')
```

> ## Standardization

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.subst` (lemma, [line 233](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L233))

> Standard reduction is preserved by substitution.

```lean
lemma Standard.subst (hM : M ⭢ₛ M') (hN : N ⭢ₛ N') (x : Var) (lc_N : LC N) (lc_N' : LC N') :
    (M[x := N]) ⭢ₛ (M'[x := N'])
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.of_beta_step` (lemma, [line 252](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L252))

> A single full β-step is a standard reduction.

```lean
lemma Standard.of_beta_step (step : M ⭢βᶠ N) (lc_M : LC M) : M ⭢ₛ N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.to_redex` (lemma, [line 268](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L268))

> Standard reduction is contained in full β-reduction.

```lean
lemma Standard.to_redex (step : M ⭢ₛ N) : M ↠βᶠ N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.abs_inv` (lemma, [line 281](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L281))

> If a standard reduction reaches an abstraction, then its leading Call-by-Name
> reduction reaches an abstraction that standardly reduces to the same target.

```lean
lemma Standard.abs_inv (h : M ⭢ₛ N) (M' : Term Var) (eq : N = Term.abs M') :
    ∃ M'', M ↠ₙ Term.abs M'' ∧ Term.abs M'' ⭢ₛ Term.abs M'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.abs_subst` (lemma, [line 296](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L296))

> Standard reduction of abstractions is preserved by opening.

```lean
lemma Standard.abs_subst
    (h_abs : Term.abs M ⭢ₛ Term.abs M') (hN : N ⭢ₛ N') (lc_N : LC N) (lc_N' : LC N') :
    (M ^ N) ⭢ₛ (M' ^ N')
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.trans_step` (lemma, [line 306](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L306))

> A standard reduction followed by a full β-step is a standard reduction.

```lean
lemma Standard.trans_step (h1 : M ⭢ₛ P) (h2 : P ⭢βᶠ N) : M ⭢ₛ N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.trans_redex` (lemma, [line 328](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L328))

> A standard reduction followed by a full β-reduction is a standard reduction.

```lean
lemma Standard.trans_redex (h1 : M ⭢ₛ P) (h2 : P ↠βᶠ N) : M ⭢ₛ N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.trans` (lemma, [line 334](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L334))

> Standard reduction is transitive.

```lean
lemma Standard.trans (h1 : M ⭢ₛ P) (h2 : P ⭢ₛ N) : M ⭢ₛ N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.standardization` (theorem, [line 347](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L347))

> The standardization theorem: every full β-reduction is a standard reduction.

```lean
theorem Standard.standardization (lc_M : LC M) (step : M ↠βᶠ N) : M ⭢ₛ N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.iff_redex` (theorem, [line 353](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L353))

> Standard reduction coincides with full β-reduction on locally closed terms.

```lean
theorem Standard.iff_redex (lc_M : LC M) : M ⭢ₛ N ↔ M ↠βᶠ N
```

> ## Equivalence with standard sequences

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.lc_r` (lemma, [line 359](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L359))

> Standard sequences preserve local closure.

```lean
lemma StandardSeq.lc_r (h : StandardSeq n M N) (lc : LC M) : LC N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.abs_close` (lemma, [line 365](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L365))

> Closing a variable and abstracting preserves a standard sequence.

```lean
lemma StandardSeq.abs_close {x : Var} (h : StandardSeq n M M') (lc : LC M) :
    StandardSeq n (M⟦0 ↜ x⟧.abs) (M'⟦0 ↜ x⟧.abs)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.abs_cong` (lemma, [line 372](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L372))

> Abstraction congruence for standard sequences.

```lean
lemma StandardSeq.abs_cong (xs : Finset Var)
    (cofin : ∀ x ∉ xs, ∃ n, StandardSeq n (M ^ fvar x) (M' ^ fvar x))
    (lc : LC (abs M)) : ∃ n, StandardSeq n (abs M) (abs M')
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.to_redex` (lemma, [line 384](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L384))

> A standard sequence is a full β-reduction.

```lean
lemma StandardSeq.to_redex (h : StandardSeq n M N) (lc_M : LC M) : M ↠βᶠ N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.to_seq` (theorem, [line 390](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L390))

> A standard reduction gives a standard β-reduction sequence.

```lean
theorem Standard.to_seq (h : M ⭢ₛ N) : ∃ n, StandardSeq n M N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.StandardSeq.to_standard` (theorem, [line 405](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L405))

> A standard β-reduction sequence gives a standard reduction.

```lean
theorem StandardSeq.to_standard (h : StandardSeq n M N) (lc_M : LC M) : M ⭢ₛ N
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Standard.iff_seq` (theorem, [line 411](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean#L411))

> Standard reduction coincides with the existence of a standard β-reduction sequence.

```lean
theorem Standard.iff_seq (lc_M : LC M) : M ⭢ₛ N ↔ ∃ n, StandardSeq n M N
```

## Depends on

- [Redex Positions](betaat.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/StandardReduction.lean)
