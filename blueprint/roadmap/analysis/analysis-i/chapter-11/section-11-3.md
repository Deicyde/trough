---
declaration: abbrev
origin: cited
lean: Chapter11.MajorizesOn, Chapter11.upper_integral, Chapter11.le_lower_integral, Chapter11.integ, Chapter11.integ_of_piecewise_const, Chapter11.integ_on_subsingleton, Chapter11.upper_riemann_sum, Chapter11.upper_riemann_sum_le, Chapter11.upper_integ_le_upper_sum, Chapter11.MajorizesOn.trans, Chapter11.MajorizesOn.anti_symm, Chapter11.MajorizesOn.of_add
statement: formalized
---

# Section 11.3: Upper and lower Riemann integrals

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - The upper and lower Riemann integral; the Riemann integral.
> - Upper and lower Riemann sums.

*Quoted from [Analysis/Section_11_3.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_3.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 12 labelled items, carried by 12 declarations: 2 proved here, 5 stated without proof (5 of them exercises) and 5 definitions (1 with a value left as `sorry`). It also has 27 declarations with no label, counted here but not shown.

## Definition 11.3.1

`Chapter11.MajorizesOn` (abbrev, [line 24](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_3.lean#L24)). A definition.

> Definition 11.3.1 (Majorization of functions)

```lean
abbrev MajorizesOn (g f:ℝ → ℝ) (I: BoundedInterval) : Prop
```

## Definition 11.3.2

`Chapter11.upper_integral` (abbrev, [line 31](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_3.lean#L31)). A definition.

> Definition 11.3.2 (Upper and lower Riemann integrals ).

```lean
noncomputable abbrev upper_integral (f:ℝ → ℝ) (I: BoundedInterval) : ℝ
```

## Lemma 11.3.3

`Chapter11.le_lower_integral` (lemma, [line 82](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_3.lean#L82)). Proved here.

> Lemma 11.3.3.  The proof has been reorganized somewhat from the textbook.

```lean
lemma le_lower_integral {f:ℝ → ℝ} {I: BoundedInterval} {M:ℝ} (h: ∀ x ∈ (I:Set ℝ), |f x| ≤ M) :
  -M * |I|ₗ ≤ lower_integral f I
```

## Definition 11.3.4

`Chapter11.integ` (abbrev, [line 124](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_3.lean#L124)). A definition.

> Definition 11.3.4 (Riemann integral)
> As we permit junk values, the simplest definition for the Riemann integral is the upper integral.

```lean
noncomputable abbrev integ (f:ℝ → ℝ) (I: BoundedInterval) : ℝ
```

## Lemma 11.3.7 / Exercise 11.3.3

`Chapter11.integ_of_piecewise_const` (theorem, [line 133](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_3.lean#L133)). An exercise, stated without proof.

> Lemma 11.3.7 / Exercise 11.3.3

```lean
theorem integ_of_piecewise_const {f:ℝ → ℝ} {I: BoundedInterval} (hf: PiecewiseConstantOn f I) :
  IntegrableOn f I ∧ integ f I = hf.integ'
```

## Remark 11.3.8

`Chapter11.integ_on_subsingleton` (theorem, [line 138](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_3.lean#L138)). Proved here.

> Remark 11.3.8

```lean
theorem integ_on_subsingleton {f:ℝ → ℝ} {I: BoundedInterval} (hI: |I|ₗ = 0) :
  IntegrableOn f I ∧ integ f I = 0
```

## Definition 11.3.9

`Chapter11.upper_riemann_sum` (abbrev, [line 146](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_3.lean#L146)). A definition.

> Definition 11.3.9 (Riemann sums).  The restriction to positive length J is not needed thanks to various junk value conventions.

```lean
noncomputable abbrev upper_riemann_sum (f:ℝ → ℝ) {I: BoundedInterval} (P: Partition I) : ℝ
```

## Lemma 11.3.11 / Exercise 11.3.4

`Chapter11.upper_riemann_sum_le` (theorem, [line 153](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_3.lean#L153)). An exercise, stated without proof.

> Lemma 11.3.11 / Exercise 11.3.4

```lean
theorem upper_riemann_sum_le {f g: ℝ → ℝ} {I:BoundedInterval} (P: Partition I)
  (hgf: MajorizesOn g f I) (hg: PiecewiseConstantWith g P) :
  upper_riemann_sum f P ≤ integ g I
```

## Proposition 11.3.12 / Exercise 11.3.5

`Chapter11.upper_integ_le_upper_sum` (theorem, [line 164](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_3.lean#L164)). An exercise, stated without proof.

> Proposition 11.3.12 / Exercise 11.3.5

```lean
theorem upper_integ_le_upper_sum {f:ℝ → ℝ} {I:BoundedInterval} (hf: BddOn f I)
  (P: Partition I): upper_integral f I ≤ upper_riemann_sum f P
```

## Exercise 11.3.1 (i)

`Chapter11.MajorizesOn.trans` (theorem, [line 181](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_3.lean#L181)). An exercise, stated without proof.

> Exercise 11.3.1 (i)

```lean
theorem MajorizesOn.trans {f g h: ℝ → ℝ} {I: BoundedInterval}
  (hfg: MajorizesOn f g I) (hgh: MajorizesOn g h I) : MajorizesOn f h I
```

## Exercise 11.3.1 (ii)

`Chapter11.MajorizesOn.anti_symm` (theorem, [line 186](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_3.lean#L186)). An exercise, stated without proof.

> Exercise 11.3.1 (ii)

```lean
theorem MajorizesOn.anti_symm {f g: ℝ → ℝ} {I: BoundedInterval}:
  (∀ x ∈ (I:Set ℝ), f x = g x) ↔ MajorizesOn f g I ∧ MajorizesOn g f I
```

## Exercise 11.3.2

`Chapter11.MajorizesOn.of_add` (def, [line 191](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_3.lean#L191)). A definition whose value is left as `sorry`.

> Exercise 11.3.2

```lean
def MajorizesOn.of_add : Decidable ( ∀ (f g h:ℝ → ℝ) (I:BoundedInterval) (hfg: MajorizesOn f g I),
 MajorizesOn (f+h) (g+h) I)
```

## Depends on

- [Section 9.6: The maximum principle](../chapter-9/section-9-6.md)
- [Section 11.2: Piecewise constant functions](section-11-2.md)

## Sources

- [Analysis/Section_11_3.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_3.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_11_3/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_11_3.html)
