---
declaration: abbrev
origin: cited
lean: Chapter6.Sequence.subseq, Chapter6.Sequence.subseq_self, Chapter6.Sequence.subseq_trans, Chapter6.Sequence.convergent_iff_subseq, Chapter6.Sequence.limit_point_iff_subseq, Chapter6.Sequence.convergent_of_subseq_of_bounded, Chapter6.Sequence.exist_subseq_of_subseq, Chapter6.Sequence.subseq_of_unbounded
statement: formalized
---

# Section 6.6: Subsequences

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Definition of a subsequence.

*Quoted from [Analysis/Section_6_6.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_6.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 8 labelled items, carried by 9 declarations: 1 proved here, 6 stated without proof (5 of them exercises) and 2 definitions (1 with a value left as `sorry`). It also has 3 examples with no label, counted here but not shown.

## Definition 6.6.1

`Chapter6.Sequence.subseq` (abbrev, [line 21](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_6.lean#L21)). A definition.

> Definition 6.6.1

```lean
abbrev Sequence.subseq (a b: ℕ → ℝ) : Prop
```

## Example 6.6.2

An `example` ([line 24](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_6.lean#L24)). Stated without proof.

> Example 6.6.2

```lean
example (a:ℕ → ℝ) : Sequence.subseq a (fun n ↦ a (2 * n))
```

## Lemma 6.6.4 / Exercise 6.6.1

`Chapter6.Sequence.subseq_self` (theorem, [line 39](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_6.lean#L39)). An exercise, stated without proof.

> Lemma 6.6.4 (reflexivity) / Exercise 6.6.1

```lean
theorem Sequence.subseq_self (a:ℕ → ℝ) : Sequence.subseq a a
```

`Chapter6.Sequence.subseq_trans` (theorem, [line 42](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_6.lean#L42)). An exercise, stated without proof.

> Lemma 6.6.4 (transitivity) / Exercise 6.6.1

```lean
theorem Sequence.subseq_trans {a b c:ℕ → ℝ} (hab: Sequence.subseq a b) (hbc: Sequence.subseq b c) :
    Sequence.subseq a c
```

## Proposition 6.6.5 / Exercise 6.6.4

`Chapter6.Sequence.convergent_iff_subseq` (theorem, [line 46](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_6.lean#L46)). An exercise, stated without proof.

> Proposition 6.6.5 / Exercise 6.6.4

```lean
theorem Sequence.convergent_iff_subseq (a:ℕ → ℝ) (L:ℝ) :
    (a:Sequence).TendsTo L ↔ ∀ b:ℕ → ℝ, Sequence.subseq a b → (b:Sequence).TendsTo L
```

## Proposition 6.6.6 / Exercise 6.6.5

`Chapter6.Sequence.limit_point_iff_subseq` (theorem, [line 51](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_6.lean#L51)). An exercise, stated without proof.

> Proposition 6.6.6 / Exercise 6.6.5

```lean
theorem Sequence.limit_point_iff_subseq (a:ℕ → ℝ) (L:ℝ) :
    (a:Sequence).LimitPoint L ↔ ∃ b:ℕ → ℝ, Sequence.subseq a b ∧ (b:Sequence).TendsTo L
```

## Theorem 6.6.8

`Chapter6.Sequence.convergent_of_subseq_of_bounded` (theorem, [line 56](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_6.lean#L56)). Proved here.

> Theorem 6.6.8 (Bolzano-Weierstrass theorem)

```lean
theorem Sequence.convergent_of_subseq_of_bounded {a:ℕ→ ℝ} (ha: (a:Sequence).IsBounded) :
    ∃ b:ℕ → ℝ, Sequence.subseq a b ∧ (b:Sequence).Convergent
```

## Exercise 6.6.2

`Chapter6.Sequence.exist_subseq_of_subseq` (def, [line 64](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_6.lean#L64)). A definition whose value is left as `sorry`.

> Exercise 6.6.2

```lean
def Sequence.exist_subseq_of_subseq :
  Decidable (∃ a b : ℕ → ℝ, a ≠ b ∧ Sequence.subseq a b ∧ Sequence.subseq b a)
```

## Exercise 6.6.3

`Chapter6.Sequence.subseq_of_unbounded` (theorem, [line 73](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_6.lean#L73)). An exercise, stated without proof.

> Exercise 6.6.3.  You may find the API around Mathlib's `Nat.find` to be useful
> (and `open Classical` to avoid any decidability issues)

```lean
theorem Sequence.subseq_of_unbounded {a:ℕ → ℝ} (ha: ¬ (a:Sequence).IsBounded) :
    ∃ b:ℕ → ℝ, Sequence.subseq a b ∧ (b:Sequence)⁻¹.TendsTo 0
```

## Depends on

- [Section 6.5: Some standard limits](section-6-5.md)

## Sources

- [Analysis/Section_6_6.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_6.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_6_6/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_6_6.html)
