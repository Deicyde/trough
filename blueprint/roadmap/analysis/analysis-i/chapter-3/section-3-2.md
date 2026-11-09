---
declaration: abbrev
origin: cited
lean: Chapter3.axiom_of_universal_specification, Chapter3.SetTheory.Set.axiom_of_regularity, Chapter3.SetTheory.Set.emptyset_exists, Chapter3.SetTheory.Set.singleton_exists, Chapter3.SetTheory.Set.pair_exists, Chapter3.SetTheory.Set.union_exists, Chapter3.SetTheory.Set.specify_exists, Chapter3.SetTheory.Set.replace_exists, Chapter3.SetTheory.Set.not_mem_self, Chapter3.SetTheory.Set.not_mem_mem, Chapter3.SetTheory.Set.univ_iff, Chapter3.SetTheory.Set.no_univ
statement: formalized
---

# Section 3.2: Russell's paradox

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> This section is mostly optional, though it does make explicit the axiom of foundation which is
> used in a minor role in an exercise in Section 3.5.
>
> Main constructions and results of this section:
>
> - Russell's paradox (ruling out the axiom of universal specification).
> - The axiom of regularity (foundation) - an axiom designed to avoid Russell's paradox.
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_3_2.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_2.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 5 labelled items, carried by 12 declarations: 1 proved here, 10 stated without proof (10 of them exercises) and 1 definition. It also has 1 declaration with no label, counted here but not shown.

## Axiom 3.8

`Chapter3.axiom_of_universal_specification` (abbrev, [line 36](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_2.lean#L36)). A definition.

> Axiom 3.8 (Universal specification)

```lean
abbrev axiom_of_universal_specification : Prop
```

## Axiom 3.9

`Chapter3.SetTheory.Set.axiom_of_regularity` (theorem, [line 55](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_2.lean#L55)). Proved here.

> Axiom 3.9 (Regularity)

```lean
theorem SetTheory.Set.axiom_of_regularity {A:Set} (h: A ≠ ∅) :
    ∃ x:A, ∀ S:Set, x.val = S → Disjoint S A
```

## Exercise 3.2.1

`Chapter3.SetTheory.Set.emptyset_exists` (theorem, [line 68](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_2.lean#L68)). An exercise, stated without proof.

> Exercise 3.2.1.  The spirit of the exercise is to establish these results without using either
> Russell's paradox, or the empty set.

```lean
theorem SetTheory.Set.emptyset_exists (h: axiom_of_universal_specification):
    ∃ (X:Set), ∀ x, x ∉ X
```

`Chapter3.SetTheory.Set.singleton_exists` (theorem, [line 76](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_2.lean#L76)). An exercise, stated without proof.

> Exercise 3.2.1.  The spirit of the exercise is to establish these results without using either
> Russell's paradox, or the singleton set.

```lean
theorem SetTheory.Set.singleton_exists (h: axiom_of_universal_specification) (x:Object):
    ∃ (X:Set), ∀ y, y ∈ X ↔ y = x
```

`Chapter3.SetTheory.Set.pair_exists` (theorem, [line 84](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_2.lean#L84)). An exercise, stated without proof.

> Exercise 3.2.1.  The spirit of the exercise is to establish these results without using either
> Russell's paradox, or the pair set.

```lean
theorem SetTheory.Set.pair_exists (h: axiom_of_universal_specification) (x₁ x₂:Object):
    ∃ (X:Set), ∀ y, y ∈ X ↔ y = x₁ ∨ y = x₂
```

`Chapter3.SetTheory.Set.union_exists` (theorem, [line 92](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_2.lean#L92)). An exercise, stated without proof.

> Exercise 3.2.1. The spirit of the exercise is to establish these results without using either
> Russell's paradox, or the union operation.

```lean
theorem SetTheory.Set.union_exists (h: axiom_of_universal_specification) (A B:Set):
    ∃ (Z:Set), ∀ z, z ∈ Z ↔ z ∈ A ∨ z ∈ B
```

`Chapter3.SetTheory.Set.specify_exists` (theorem, [line 100](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_2.lean#L100)). An exercise, stated without proof.

> Exercise 3.2.1. The spirit of the exercise is to establish these results without using either
> Russell's paradox, or the specify operation.

```lean
theorem SetTheory.Set.specify_exists (h: axiom_of_universal_specification) (A:Set) (P: A → Prop):
    ∃ (Z:Set), ∀ z, z ∈ Z ↔ ∃ h : z ∈ A, P ⟨ z, h ⟩
```

`Chapter3.SetTheory.Set.replace_exists` (theorem, [line 108](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_2.lean#L108)). An exercise, stated without proof.

> Exercise 3.2.1. The spirit of the exercise is to establish these results without using either
> Russell's paradox, or the replace operation.

```lean
theorem SetTheory.Set.replace_exists (h: axiom_of_universal_specification) (A:Set)
  (P: A → Object → Prop) (hP: ∀ x y y', P x y ∧ P x y' → y = y') :
    ∃ (Z:Set), ∀ y, y ∈ Z ↔ ∃ a : A, P a y
```

## Exercise 3.2.2

`Chapter3.SetTheory.Set.not_mem_self` (theorem, [line 114](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_2.lean#L114)). An exercise, stated without proof.

> Exercise 3.2.2 (no set contains itself)

```lean
theorem SetTheory.Set.not_mem_self (A:Set) : (A:Object) ∉ A
```

`Chapter3.SetTheory.Set.not_mem_mem` (theorem, [line 117](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_2.lean#L117)). An exercise, stated without proof.

> Exercise 3.2.2 (no two sets contain each other)

```lean
theorem SetTheory.Set.not_mem_mem (A B:Set) : (A:Object) ∉ B ∨ (B:Object) ∉ A
```

## Exercise 3.2.3

`Chapter3.SetTheory.Set.univ_iff` (theorem, [line 120](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_2.lean#L120)). An exercise, stated without proof.

> Exercise 3.2.3 (universal specification)

```lean
theorem SetTheory.Set.univ_iff : axiom_of_universal_specification ↔
  ∃ (U:Set), ∀ x, x ∈ U
```

`Chapter3.SetTheory.Set.no_univ` (theorem, [line 124](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_2.lean#L124)). An exercise, stated without proof.

> Exercise 3.2.3 (there is no universal set)

```lean
theorem SetTheory.Set.no_univ : ¬ ∃ (U:Set), ∀ (x:Object), x ∈ U
```

## Depends on

- [Section 3.1: Fundamentals (of set theory)](section-3-1.md)

## Sources

- [Analysis/Section_3_2.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_2.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_3_2/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_3_2.html)
