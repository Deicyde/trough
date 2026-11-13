---
declaration: theorem
origin: cited
lean: Kourovka.«8.8».kourovka_8_8a, Kourovka.«8.8».kourovka_8_8b
statement: formalized
---

# Conjecture 8.8

> by R. I. Grigorchuk
>
> Both parts of the problem are due to D. V. Anosov.
>
> *Reference:* [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v46)

*Quoted from [FormalConjectures/Kourovka/8_8.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Kourovka/8_8.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Kourovka.«8.8».kourovka_8_8a`

Solved: stated here without proof.

> Does there exist a non-cyclic finitely-generated group $G$ containing an
> element $a$ such that every element of $G$ is conjugate to a power of $a$?
>
> Here a power of $a$ means $a^n$ for some $n \in \mathbb{Z}$.
>
> Answered affirmatively by V. S. Guba, Math. USSR-Izv. 29 (1986), 233–277.

```lean
theorem kourovka_8_8a :
    ∃ (G : Type) (_ : Group G), ¬ IsCyclic G ∧ Group.FG G ∧
      ∃ a : G, ∀ g : G, ∃ n : ℤ, IsConj g (a ^ n)
```

Category `research solved`; AMS [20 Group theory and generalizations](../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Kourovka/8_8.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Kourovka/8_8.lean#L44).

## `Kourovka.«8.8».kourovka_8_8b`

Open: stated without proof.

> Does there exist a non-cyclic finitely presented group $G$ which contains an
> element $a$ such that each element of $G$ is conjugate to some power of $a$?
>
> Here a power of $a$ means $a^n$ for some $n \in \mathbb{Z}$.

```lean
theorem kourovka_8_8b :
    ∃ (G : Type) (_ : Group G), ¬ IsCyclic G ∧ Group.IsFinitelyPresented G ∧
      ∃ a : G, ∀ g : G, ∃ n : ℤ, IsConj g (a ^ n)
```

Category `research open`; AMS [20 Group theory and generalizations](../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Kourovka/8_8.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Kourovka/8_8.lean#L56).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Kourovka/8_8.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Kourovka/8_8.lean)
- [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v46)
