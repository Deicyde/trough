---
declaration: theorem
origin: cited
lean: Rat.between_int, Rat.exists_between_rat, Nat.no_infinite_descent, Int.infinite_descent, Rat.pos_infinite_descent, Rat.not_exist_sqrt_two, Rat.exist_approx_sqrt_two
statement: formalized
---

# Section 4.4: gaps in the rational numbers

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Irrationality of √2, and related facts about the rational numbers
>
> Many of the results here can be established more quickly by relying more heavily on the Mathlib
> API; one can set oneself the exercise of doing so.
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_4_4.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_4.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 8 labelled items, carried by 8 declarations: 3 proved here, 3 stated without proof (3 of them exercises) and 2 definitions (2 with a value left as `sorry`). It also has 3 declarations with no label, counted here but not shown.

## Proposition 4.4.1 / Exercise 4.4.1

`Rat.between_int` (theorem, [line 28](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_4.lean#L28)). An exercise, stated without proof.

> Proposition 4.4.1 (Interspersing of integers by rationals) / Exercise 4.4.1

```lean
theorem Rat.between_int (x:ℚ) : ∃! n:ℤ, n ≤ x ∧ x < n+1
```

## Proposition 4.4.3

`Rat.exists_between_rat` (theorem, [line 35](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_4.lean#L35)). Proved here.

> Proposition 4.4.3 (Interspersing of rationals)

```lean
theorem Rat.exists_between_rat {x y:ℚ} (h: x < y) : ∃ z:ℚ, x < z ∧ z < y
```

## Exercise 4.4.2 (a)

`Nat.no_infinite_descent` (theorem, [line 48](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_4.lean#L48)). An exercise, stated without proof.

> Exercise 4.4.2 (a)

```lean
theorem Nat.no_infinite_descent : ¬ ∃ a:ℕ → ℕ, ∀ n, a (n+1) < a n
```

## Exercise 4.4.2 (b)

`Int.infinite_descent` (def, [line 52](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_4.lean#L52)). A definition whose value is left as `sorry`.

> Exercise 4.4.2 (b)

```lean
def Int.infinite_descent : Decidable (∃ a:ℕ → ℤ, ∀ n, a (n+1) < a n)
```

## Exercise 4.4.2 (b')

`Rat.pos_infinite_descent` (def, [line 57](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_4.lean#L57)). A definition whose value is left as `sorry`.

> Exercise 4.4.2 (b')

```lean
def Rat.pos_infinite_descent : Decidable (∃ a:ℕ → {x: ℚ // 0 < x}, ∀ n, a (n+1) < a n)
```

## Proposition 4.4.4 / Exercise 4.4.3

`Rat.not_exist_sqrt_two` (theorem, [line 73](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_4.lean#L73)). An exercise, stated without proof.

> Proposition 4.4.4 / Exercise 4.4.3

```lean
theorem Rat.not_exist_sqrt_two : ¬ ∃ x:ℚ, x^2 = 2
```

## Proposition 4.4.5

`Rat.exist_approx_sqrt_two` (theorem, [line 123](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_4.lean#L123)). Proved here.

> Proposition 4.4.5

```lean
theorem Rat.exist_approx_sqrt_two {ε:ℚ} (hε:ε>0) : ∃ x ≥ (0:ℚ), x^2 < 2 ∧ 2 < (x+ε)^2
```

## Example 4.4.6

An `example` ([line 137](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_4.lean#L137)). Proved here.

> Example 4.4.6

```lean
example :
  let ε:ℚ := 1/1000
  let x:ℚ := 1414/1000
  x^2 < 2 ∧ 2 < (x+ε)^2
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Section_4_4.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_4.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_4_4/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_4_4.html)
