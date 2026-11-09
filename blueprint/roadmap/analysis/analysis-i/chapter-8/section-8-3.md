---
declaration: theorem
origin: cited
lean: Chapter8.EqualCard.power_set_false, Chapter8.Uncountable.power_set_nat, Chapter8.Uncountable.real, Chapter8.Schroder_Bernstein_lemma, Chapter8.Schroder_Bernstein
statement: formalized
---

# Section 8.3: Uncountable sets

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Uncountable sets.
>
> Some non-trivial API is provided beyond what is given in the textbook in order connect these
> notions with existing summation notions.

*Quoted from [Analysis/Section_8_3.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_3.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 8 labelled items, carried by 8 declarations: 3 proved here and 5 stated without proof (5 of them exercises). It also has 5 declarations and 1 example with no label, counted here but not shown.

## Theorem 8.3.1

`Chapter8.EqualCard.power_set_false` (theorem, [line 26](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_3.lean#L26)). Proved here.

> Theorem 8.3.1

```lean
theorem EqualCard.power_set_false (X:Type) : ¬ EqualCard X (Set X)
```

## Corollary 8.3.3

`Chapter8.Uncountable.power_set_nat` (theorem, [line 45](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_3.lean#L45)). Proved here.

> Corollary 8.3.3

```lean
theorem Uncountable.power_set_nat : Uncountable (Set ℕ)
```

## Corollary 8.3.4

`Chapter8.Uncountable.real` (theorem, [line 66](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_3.lean#L66)). Proved here.

> Corollary 8.3.4

```lean
theorem Uncountable.real : Uncountable ℝ
```

## Exercise 8.3.1

An `example` ([line 160](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_3.lean#L160)). An exercise, stated without proof.

> Exercise 8.3.1

```lean
example {X:Type} [Finite X] : Nat.card (Set X) = 2 ^ Nat.card X
```

## Exercise 8.3.2

`Chapter8.Schroder_Bernstein_lemma` (theorem, [line 165](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_3.lean#L165)). An exercise, stated without proof.

> Exercise 8.3.2.  Some subtle type changes due to how sets are implemented in Mathlib. Also we shift the sequence `D` by one so that we can work in `Set A` rather than `Set B`.

```lean
theorem Schroder_Bernstein_lemma {X: Type} {A B C: Set X} (hAB: A ⊆ B) (hBC: B ⊆ C) (f: C ↪ A) :
  let D : ℕ → Set A := Nat.rec ((f.image ∘ ((B.embeddingOfSubset _ hBC).image)) {x:B | ↑x ∉ A}) (fun _ ↦ (f.image ∘ ((B.embeddingOfSubset _ hBC).image) ∘ (A.embeddingOfSubset _ hAB).image))
  Set.univ.PairwiseDisjoint D ∧
  let g : A → B := fun x ↦ if h: x ∈ ⋃ n, D n ∧ ∃ y:B, f ⟨↑y, hBC y.property⟩ = x then h.2.choose else ⟨ ↑x, hAB x.property ⟩
  Function.Bijective g
```

## Exercise 8.3.3

`Chapter8.Schroder_Bernstein` (theorem, [line 176](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_3.lean#L176)). An exercise, stated without proof.

> Exercise 8.3.3

```lean
theorem Schroder_Bernstein {X Y:Type} (hXY : LeCard X Y) (hYX : LeCard Y X) : EqualCard X Y
```

## Exercise 8.3.4

An `example` ([line 182](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_3.lean#L182)). An exercise, stated without proof.

> Exercise 8.3.4

```lean
example {X:Type} : LtCard X (Set X)
```

## Exercise 8.3.5

An `example` ([line 200](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_3.lean#L200)). An exercise, stated without proof.

> Exercise 8.3.5

```lean
example (X:Type) : ¬ CountablyInfinite (Set X)
```

## Depends on

- [Section 8.1: Countability](section-8-1.md)
- [Section 8.2: Summation on infinite sets](section-8-2.md)

## Sources

- [Analysis/Section_8_3.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_3.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_8_3/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_8_3.html)
