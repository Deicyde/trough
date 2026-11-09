---
declaration: theorem
origin: cited
lean: EReal.def, EReal.neg_of_real, EReal.le_iff, EReal.lt_iff, EReal.refl, EReal.trichotomy, EReal.not_lt_and_eq, EReal.not_gt_and_eq, EReal.not_lt_and_gt, EReal.trans, EReal.neg_of_lt, EReal.sup_of_bounded_nonempty, EReal.sup_of_unbounded_nonempty, EReal.sup_of_empty, EReal.sup_of_infty_mem, EReal.sup_of_neg_infty_mem, Example_6_2_7, Example_6_2_8, Example_6_2_9, EReal.mem_le_sup, EReal.mem_ge_inf, EReal.sup_le_upper, EReal.inf_ge_lower
statement: formalized
---

# Section 6.2: The extended real number system

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Some API for Mathlib's extended reals `EReal`, particularly with regard to the supremum
>   operation `sSup` and infimum operation `sInf`.

*Quoted from [Analysis/Section_6_2.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 19 labelled items, carried by 27 declarations: 13 proved here, 11 stated without proof (11 of them exercises) and 3 definitions. It also has 11 declarations and 8 examples with no label, counted here but not shown.

## Definition 6.2.1

`EReal.def` (theorem, [line 24](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L24)). Proved here.

> Definition 6.2.1

```lean
theorem EReal.def (x:EReal) : (∃ (y:Real), y = x) ∨ x = ⊤ ∨ x = ⊥
```

## Definition 6.2.2

`EReal.neg_of_real` (theorem, [line 42](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L42)). Proved here.

> Definition 6.2.2 (Negation of extended reals)

```lean
theorem EReal.neg_of_real (x:Real) : -(x:EReal) = (-x:ℝ)
```

## Definition 6.2.3

`EReal.le_iff` (theorem, [line 48](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L48)). Proved here.

> Definition 6.2.3 (Ordering of extended reals)

```lean
theorem EReal.le_iff (x y:EReal) :
    x ≤ y ↔ (∃ (x' y':Real), x = x' ∧ y = y' ∧ x' ≤ y') ∨ y = ⊤ ∨ x = ⊥
```

`EReal.lt_iff` (theorem, [line 53](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L53)). Proved here.

> Definition 6.2.3 (Ordering of extended reals)

```lean
theorem EReal.lt_iff (x y:EReal) : x < y ↔ x ≤ y ∧ x ≠ y
```

## Examples 6.2.4

An `example` ([line 58](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L58)). Proved here.

> Examples 6.2.4

```lean
example : (3:EReal) ≤ (5:EReal)
```

An `example` ([line 62](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L62)). Proved here.

> Examples 6.2.4

```lean
example : (3:EReal) < ⊤
```

An `example` ([line 66](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L66)). Proved here.

> Examples 6.2.4

```lean
example : (⊥:EReal) < ⊤
```

An `example` ([line 70](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L70)). Proved here.

> Examples 6.2.4

```lean
example : ¬ (3:EReal) ≤ ⊥
```

## Proposition 6.2.5(a) / Exercise 6.2.1

`EReal.refl` (theorem, [line 78](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L78)). An exercise, stated without proof.

> Proposition 6.2.5(a) / Exercise 6.2.1

```lean
theorem EReal.refl (x:EReal) : x ≤ x
```

## Proposition 6.2.5(b) / Exercise 6.2.1

`EReal.trichotomy` (theorem, [line 81](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L81)). An exercise, stated without proof.

> Proposition 6.2.5(b) / Exercise 6.2.1

```lean
theorem EReal.trichotomy (x y:EReal) : x < y ∨ x = y ∨ x > y
```

## Proposition 6.2.5(b') / Exercise 6.2.1

`EReal.not_lt_and_eq` (theorem, [line 84](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L84)). An exercise, stated without proof.

> Proposition 6.2.5(b') / Exercise 6.2.1

```lean
theorem EReal.not_lt_and_eq (x y:EReal) : ¬ (x < y ∧ x = y)
```

## Proposition 6.2.5(b'') / Exercise 6.2.1

`EReal.not_gt_and_eq` (theorem, [line 87](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L87)). An exercise, stated without proof.

> Proposition 6.2.5(b'') / Exercise 6.2.1

```lean
theorem EReal.not_gt_and_eq (x y:EReal) : ¬ (x > y ∧ x = y)
```

## Proposition 6.2.5(b''') / Exercise 6.2.1

`EReal.not_lt_and_gt` (theorem, [line 90](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L90)). An exercise, stated without proof.

> Proposition 6.2.5(b''') / Exercise 6.2.1

```lean
theorem EReal.not_lt_and_gt (x y:EReal) : ¬ (x < y ∧ x > y)
```

## Proposition 6.2.5(c) / Exercise 6.2.1

`EReal.trans` (theorem, [line 93](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L93)). An exercise, stated without proof.

> Proposition 6.2.5(c) / Exercise 6.2.1

```lean
theorem EReal.trans {x y z:EReal} (hxy : x ≤ y) (hyz: y ≤ z) : x ≤ z
```

## Proposition 6.2.5(d) / Exercise 6.2.1

`EReal.neg_of_lt` (theorem, [line 96](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L96)). An exercise, stated without proof.

> Proposition 6.2.5(d) / Exercise 6.2.1

```lean
theorem EReal.neg_of_lt {x y:EReal} (hxy : x ≤ y): -y ≤ -x
```

## Definition 6.2.6

`EReal.sup_of_bounded_nonempty` (theorem, [line 99](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L99)). Proved here.

> Definition 6.2.6

```lean
theorem EReal.sup_of_bounded_nonempty {E: Set ℝ} (hbound: BddAbove E) (hnon: E.Nonempty) :
    sSup ((fun (x:ℝ) ↦ (x:EReal)) '' E) = sSup E
```

`EReal.sup_of_unbounded_nonempty` (theorem, [line 112](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L112)). Proved here.

> Definition 6.2.6

```lean
theorem EReal.sup_of_unbounded_nonempty {E: Set ℝ} (hunbound: ¬ BddAbove E) (hnon: E.Nonempty) :
    sSup ((fun (x:ℝ) ↦ (x:EReal)) '' E) = ⊤
```

`EReal.sup_of_empty` (theorem, [line 122](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L122)). Proved here.

> Definition 6.2.6

```lean
theorem EReal.sup_of_empty : sSup (∅:Set EReal) = ⊥
```

`EReal.sup_of_infty_mem` (theorem, [line 125](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L125)). Proved here.

> Definition 6.2.6

```lean
theorem EReal.sup_of_infty_mem {E: Set EReal} (hE: ⊤ ∈ E) : sSup E = ⊤
```

`EReal.sup_of_neg_infty_mem` (theorem, [line 128](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L128)). Proved here.

> Definition 6.2.6

```lean
theorem EReal.sup_of_neg_infty_mem {E: Set EReal} : sSup E = sSup (E \ {⊥})
```

## Example 6.2.7

`Example_6_2_7` (abbrev, [line 136](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L136)). A definition.

> Example 6.2.7

```lean
abbrev Example_6_2_7 : Set EReal
```

## Example 6.2.8

`Example_6_2_8` (abbrev, [line 147](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L147)). A definition.

> Example 6.2.8

```lean
abbrev Example_6_2_8 : Set EReal
```

## Example 6.2.9

`Example_6_2_9` (abbrev, [line 154](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L154)). A definition.

> Example 6.2.9

```lean
abbrev Example_6_2_9 : Set EReal
```

## Theorem 6.2.11 (a) / Exercise 6.2.2

`EReal.mem_le_sup` (theorem, [line 165](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L165)). An exercise, stated without proof.

> Theorem 6.2.11 (a) / Exercise 6.2.2

```lean
theorem EReal.mem_le_sup (E: Set EReal) {x:EReal} (hx: x ∈ E) : x ≤ sSup E
```

## Theorem 6.2.11 (a') / Exercise 6.2.2

`EReal.mem_ge_inf` (theorem, [line 168](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L168)). An exercise, stated without proof.

> Theorem 6.2.11 (a') / Exercise 6.2.2

```lean
theorem EReal.mem_ge_inf (E: Set EReal) {x:EReal} (hx: x ∈ E) : sInf E ≤ x
```

## Theorem 6.2.11 (b) / Exercise 6.2.2

`EReal.sup_le_upper` (theorem, [line 171](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L171)). An exercise, stated without proof.

> Theorem 6.2.11 (b) / Exercise 6.2.2

```lean
theorem EReal.sup_le_upper (E: Set EReal) {M:EReal} (hM: M ∈ upperBounds E) : sSup E ≤ M
```

## Theorem 6.2.11 (c) / Exercise 6.2.2

`EReal.inf_ge_lower` (theorem, [line 174](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean#L174)). An exercise, stated without proof.

> Theorem 6.2.11 (c) / Exercise 6.2.2

```lean
theorem EReal.inf_ge_lower (E: Set EReal) {M:EReal} (hM: M ∈ lowerBounds E) : sInf E ≥ M
```

## Depends on

- [Section 5.5: The least upper bound property](../chapter-5/section-5-5.md)
- [Chapter 5 epilogue: Isomorphism with the Mathlib real numbers](../chapter-5/section-5-epilogue.md)

## Sources

- [Analysis/Section_6_2.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_2.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_6_2/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_6_2.html)
