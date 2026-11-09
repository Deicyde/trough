---
declaration: structure
origin: cited
lean: Chapter3.Function, Chapter3.Function.eval, Chapter3.P_3_3_3a, Chapter3.SetTheory.Set.P_3_3_5, Chapter3.Function.eq_iff, Chapter3.SetTheory.Set.f_3_3_10a, Chapter3.SetTheory.Set.f_3_3_11, Chapter3.Function.comp, Chapter3.SetTheory.Set.f_3_3_14, Chapter3.SetTheory.Set.comp_assoc, Chapter3.SetTheory.Set.f_3_3_18_one_to_one, Chapter3.SetTheory.Set.two_to_one, Chapter3.Function.onto, Chapter3.Function.bijective, Chapter3.f_3_3_24, Chapter3.Function.bijective_incorrect_def, Chapter3.Function.refl, Chapter3.Function.comp_of_inj, Chapter3.empty_function_one_to_one_iff, Chapter3.Function.comp_cancel_left, Chapter3.Function.comp_injective, Chapter3.Function.inverse_comp_self, Chapter3.Function.comp_bijective, Chapter3.Function.inclusion
statement: formalized
---

# Section 3.3: Functions

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - A notion of function `Function X Y` between two sets `X`, `Y` in the set theory of Section 3.1
> - Various relations with the Mathlib notion of a function `X → Y` between two types `X`, `Y`.
>   (Note from Section 3.1 that every `Set` `X` can also be viewed as a subtype
>   `` of `Object`.)
> - Basic function properties and operations, such as composition, one-to-one and onto functions,
>   and inverses.
>
> In the rest of the book we will deprecate the Chapter 3 version of a function, and work with the
> Mathlib notion of a function instead.  Even within this section, we will switch to the Mathlib
> formalism for some of the examples involving number systems such as `ℤ` or `ℝ` that have not been
> implemented in the Chapter 3 framework.
>
> We will work here with the version `Nat` of the natural numbers internal to the Chapter 3 set
> theory, though usually we will use coercions to then immediately translate to the Mathlib
> natural numbers `ℕ`.
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_3_3.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 26 labelled items, carried by 27 declarations: 9 proved here, 7 stated without proof (7 of them exercises) and 11 definitions. It also has 68 declarations and 13 examples with no label, counted here but not shown.

## Definition 3.3.1

`Chapter3.Function` (structure, [line 54](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L54)). A definition.

> Definition 3.3.1. `Function X Y` is the structure of functions from `X` to `Y`.
> Analogous to the Mathlib type `X → Y`.

```lean
structure Function (X Y: Set)
```

`Chapter3.Function.eval` (theorem, [line 78](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L78)). Proved here.

> Definition 3.3.1

```lean
theorem Function.eval {X Y: Set} (f: Function X Y) (x: X) (y: Y) : y = f x ↔ f.P x y
```

## Example 3.3.3

`Chapter3.P_3_3_3a` (abbrev, [line 87](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L87)). A definition.

> Example 3.3.3.

```lean
abbrev P_3_3_3a : Nat → Nat → Prop
```

## Example 3.3.4

An `example` ([line 162](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L162)). Proved here.

> Example 3.3.4 is a little tricky to replicate with the current formalism as the real numbers
> have not been constructed yet.  Instead, I offer some Mathlib counterparts, using the
> Mathlib API for `NNReal` and `ℝ`.

```lean
example : ¬ ∃ f: ℝ → ℝ, ∀ x y, y = f x ↔ y^2 = x
```

## Example 3.3.5

`Chapter3.SetTheory.Set.P_3_3_5` (abbrev, [line 184](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L184)). A definition.

> Example 3.3.5. The unused variable `_x` is underscored to avoid triggering a linter.

```lean
abbrev SetTheory.Set.P_3_3_5 : Nat → Nat → Prop
```

## Definition 3.3.8

`Chapter3.Function.eq_iff` (theorem, [line 195](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L195)). Proved here.

> Definition 3.3.8 (Equality of functions)

```lean
theorem Function.eq_iff {X Y: Set} (f g: Function X Y) : f = g ↔ ∀ x: X, f x = g x
```

## Example 3.3.10

`Chapter3.SetTheory.Set.f_3_3_10a` (abbrev, [line 206](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L206)). A definition.

> Example 3.3.10 (simplified).  The second part of the example is tricky to replicate in this
> formalism, so a Mathlib substitute is offered instead.

```lean
abbrev SetTheory.Set.f_3_3_10a : Function Nat Nat
```

## Example 3.3.11

`Chapter3.SetTheory.Set.f_3_3_11` (abbrev, [line 225](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L225)). A definition.

> Example 3.3.11

```lean
abbrev SetTheory.Set.f_3_3_11 (X:Set) : Function (∅:Set) X
```

## Definition 3.3.13

`Chapter3.Function.comp` (abbrev, [line 231](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L231)). A definition.

> Definition 3.3.13 (Composition)

```lean
noncomputable abbrev Function.comp {X Y Z: Set} (g: Function Y Z) (f: Function X Y) :
    Function X Z
```

## Example 3.3.14

`Chapter3.SetTheory.Set.f_3_3_14` (abbrev, [line 250](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L250)). A definition.

> Example 3.3.14

```lean
abbrev SetTheory.Set.f_3_3_14 : Function Nat Nat
```

## Lemma 3.3.15

`Chapter3.SetTheory.Set.comp_assoc` (theorem, [line 264](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L264)). Proved here.

> Lemma 3.3.15 (Composition is associative)

```lean
theorem SetTheory.Set.comp_assoc {W X Y Z: Set} (h: Function Y Z) (g: Function X Y)
  (f: Function W X) :
    h ○ (g ○ f) = (h ○ g) ○ f
```

## Example 3.3.18

`Chapter3.SetTheory.Set.f_3_3_18_one_to_one` (theorem, [line 287](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L287)). Proved here.

> Example 3.3.18.  One half of the example requires the integers, and so is expressed using
> Mathlib functions instead of Chapter 3 functions.

```lean
theorem SetTheory.Set.f_3_3_18_one_to_one :
    (Function.mk_fn (fun (n:Nat) ↦ ((n^2:ℕ):Nat))).one_to_one
```

## Remark 3.3.19

`Chapter3.SetTheory.Set.two_to_one` (theorem, [line 305](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L305)). Proved here.

> Remark 3.3.19

```lean
theorem SetTheory.Set.two_to_one {X Y: Set} {f: Function X Y} (h: ¬ f.one_to_one) :
    ∃ x x': X, x ≠ x' ∧ f x = f x'
```

## Definition 3.3.20

`Chapter3.Function.onto` (abbrev, [line 310](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L310)). A definition.

> Definition 3.3.20 (Onto functions)

```lean
abbrev Function.onto {X Y: Set} (f: Function X Y) : Prop
```

## Example 3.3.21

An `example` ([line 316](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L316)). Proved here.

> Example 3.3.21 (using Mathlib)

```lean
example : ¬ Function.Surjective (fun (n:ℤ) ↦ n^2)
```

## Definition 3.3.23

`Chapter3.Function.bijective` (abbrev, [line 328](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L328)). A definition.

> Definition 3.3.23 (Bijective functions)

```lean
abbrev Function.bijective {X Y: Set} (f: Function X Y) : Prop
```

## Example 3.3.24

`Chapter3.f_3_3_24` (abbrev, [line 336](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L336)). A definition.

> Example 3.3.24 (using Mathlib)

```lean
abbrev f_3_3_24 : Fin 3 → ({3,4}:_root_.Set ℕ)
```

## Example 3.3.25

An `example` ([line 362](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L362)). Proved here.

> Example 3.3.25 is formulated using Mathlib rather than the set theory framework here to avoid
> some tedious technical issues (cf. Exercise 3.3.2)

```lean
example : Function.Bijective (fun n ↦ ⟨ n+1, by omega⟩ : ℕ → { n:ℕ // n ≠ 0 })
```

## Remark 3.3.27

`Chapter3.Function.bijective_incorrect_def` (theorem, [line 376](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L376)). Proved here.

> Remark 3.3.27

```lean
theorem Function.bijective_incorrect_def :
    ∃ X Y: Set, ∃ f: Function X Y, (∀ x: X, ∃! y: Y, y = f x) ∧ ¬ f.bijective
```

## Exercise 3.3.1

`Chapter3.Function.refl` (theorem, [line 421](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L421)). An exercise, stated without proof.

> Exercise 3.3.1.  Although a proof operating directly on functions would be shorter,
> the spirit of the exercise is to show these using the `Function.eq_iff` definition.

```lean
theorem Function.refl {X Y:Set} (f: Function X Y) : f = f
```

## Exercise 3.3.2

`Chapter3.Function.comp_of_inj` (theorem, [line 431](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L431)). An exercise, stated without proof.

> Exercise 3.3.2

```lean
theorem Function.comp_of_inj {X Y Z:Set} {f: Function X Y} {g : Function Y Z} (hf: f.one_to_one)
  (hg: g.one_to_one) : (g ○ f).one_to_one
```

## Exercise 3.3.3

`Chapter3.empty_function_one_to_one_iff` (theorem, [line 440](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L440)). An exercise, stated without proof.

> Exercise 3.3.3 - fill in the sorrys in the statements in a reasonable fashion.

```lean
theorem empty_function_one_to_one_iff (X: Set) (f: Function ∅ X) : f.one_to_one ↔ sorry
```

## Exercise 3.3.4

`Chapter3.Function.comp_cancel_left` (theorem, [line 449](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L449)). An exercise, stated without proof.

> Exercise 3.3.4.

```lean
theorem Function.comp_cancel_left {X Y Z:Set} {f f': Function X Y} {g : Function Y Z}
  (heq : g ○ f = g ○ f') (hg: g.one_to_one) : f = f'
```

## Exercise 3.3.5

`Chapter3.Function.comp_injective` (theorem, [line 466](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L466)). An exercise, stated without proof.

> Exercise 3.3.5.

```lean
theorem Function.comp_injective {X Y Z:Set} {f: Function X Y} {g : Function Y Z} (hinj :
    (g ○ f).one_to_one) : f.one_to_one
```

## Exercise 3.3.6

`Chapter3.Function.inverse_comp_self` (theorem, [line 483](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L483)). An exercise, stated without proof.

> Exercise 3.3.6

```lean
theorem Function.inverse_comp_self {X Y: Set} {f: Function X Y} (h: f.bijective) (x: X) :
    (f.inverse h) (f x) = x
```

## Exercise 3.3.7

`Chapter3.Function.comp_bijective` (theorem, [line 496](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L496)). An exercise, stated without proof.

> Exercise 3.3.7

```lean
theorem Function.comp_bijective {X Y Z:Set} {f: Function X Y} {g : Function Y Z} (hf: f.bijective)
  (hg: g.bijective) : (g ○ f).bijective
```

## Exercise 3.3.8

`Chapter3.Function.inclusion` (abbrev, [line 504](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean#L504)). A definition.

> Exercise 3.3.8

```lean
abbrev Function.inclusion {X Y:Set} (h: X ⊆ Y) :
    Function X Y
```

## Depends on

- [Section 3.1: Fundamentals (of set theory)](section-3-1.md)

## Sources

- [Analysis/Section_3_3.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_3.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_3_3/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_3_3.html)
