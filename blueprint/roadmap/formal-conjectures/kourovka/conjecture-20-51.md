---
declaration: theorem
origin: cited
lean: Kourovka.«20.51».kourovka_20_51
statement: formalized
---

# Conjecture 20.51

> by D. MacHale
>
> *Reference:* [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v50), Problem 20.51.

*Quoted from [FormalConjectures/Kourovka/20_51.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Kourovka/20_51.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Kourovka.«20.51».kourovka_20_51`

Open: stated without proof.

> Is it true that for every odd integer $t > 3$ there exists a finite non-abelian group $G$ of odd
> order with exactly $t$ conjugacy classes?

```lean
theorem kourovka_20_51 :
    ∀ t > 3, Odd t → ∃ (G : Type) (_ : Group G), Finite G ∧ (∃ a b : G, a * b ≠ b * a) ∧
      Odd (Nat.card G) ∧ Nat.card (ConjClasses G) = t
```

Category `research open`; AMS [20 Group theory and generalizations](../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Kourovka/20_51.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Kourovka/20_51.lean#L37).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Kourovka/20_51.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Kourovka/20_51.lean)
- [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v50)
