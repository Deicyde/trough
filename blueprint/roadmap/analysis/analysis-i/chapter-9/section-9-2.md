---
declaration: theorem
origin: cited
lean: Chapter9.add_func_eval, Chapter9.Exercise_9_2_1a, Chapter9.Exercise_9_2_1b, Chapter9.Exercise_9_2_1c, Chapter9.Exercise_9_2_1d
statement: formalized
---

# Section 9.2: The algebra of real-valued functions

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where
> the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Recalling basic pointwise operations on functions.

*Quoted from [Analysis/Section_9_2.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_2.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 5 labelled items, carried by 5 declarations: 1 proved here and 4 definitions (4 with a value left as `sorry`). It also has 9 declarations and 6 examples with no label, counted here but not shown.

## Definition 9.2.1

`Chapter9.add_func_eval` (theorem, [line 24](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_2.lean#L24)). Proved here.

> Definition 9.2.1 (Arithmetic operations on functions).

```lean
theorem add_func_eval (f g: ℝ → ℝ) (x: ℝ) : (f + g) x = f x + g x
```

## Exercise 9.2.1 (a)

`Chapter9.Exercise_9_2_1a` (def, [line 55](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_2.lean#L55)). A definition whose value is left as `sorry`.

> Exercise 9.2.1 (a)

```lean
def Exercise_9_2_1a : Decidable (∀ (f g h : ℝ → ℝ), (f+g) ∘ h = f ∘ h + g ∘ h)
```

## Exercise 9.2.1 (b)

`Chapter9.Exercise_9_2_1b` (def, [line 60](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_2.lean#L60)). A definition whose value is left as `sorry`.

> Exercise 9.2.1 (b)

```lean
def Exercise_9_2_1b : Decidable (∀ (f g h : ℝ → ℝ), f ∘ (g + h) = f ∘ g + f ∘ h)
```

## Exercise 9.2.1 (c)

`Chapter9.Exercise_9_2_1c` (def, [line 65](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_2.lean#L65)). A definition whose value is left as `sorry`.

> Exercise 9.2.1 (c)

```lean
def Exercise_9_2_1c : Decidable (∀ (f g h : ℝ → ℝ), (f+g) * h = f * h + g * h)
```

## Exercise 9.2.1 (d)

`Chapter9.Exercise_9_2_1d` (def, [line 70](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_2.lean#L70)). A definition whose value is left as `sorry`.

> Exercise 9.2.1 (d)

```lean
def Exercise_9_2_1d : Decidable (∀ (f g h : ℝ → ℝ), f * (g+h) = f * g + f * h)
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Section_9_2.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_2.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_9_2/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_9_2.html)
