---
declaration: theorem
origin: cited
lean: Firoozbakht.firoozbakht_conjecture, Firoozbakht.firoozbakht_conjecture_consequence
statement: formalized
---

# Firoozbakht's conjecture

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Firoozbakht%27s_conjecture)
> - [primepuzzles](https://www.primepuzzles.net/conjectures/conj_030.htm)

*Quoted from [FormalConjectures/Wikipedia/Firoozbakht.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Firoozbakht.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Firoozbakht.firoozbakht_conjecture`

Open: stated without proof.

> **Firoozbakht's conjecture**
> The inequality $\sqrt[n+1]{p_{n+1}} < \sqrt[n]{p_n}$ holds for all prime numbers $p_n$.

```lean
theorem firoozbakht_conjecture (n : ℕ) :
    firoozbakhtSeq (n+1) < firoozbakhtSeq n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Firoozbakht.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Firoozbakht.lean#L45).

## `Firoozbakht.firoozbakht_conjecture_consequence`

Solved: stated here without proof.

> The inequality $p_{n+1}-p_n < (\log p_n)^2-\log p_n$ holds for all $n>4$.
> A consequence of Firuzbakht's conjecture.

```lean
theorem firoozbakht_conjecture_consequence (n : ℕ) (hn : 3 < n) (P : type_of% firoozbakht_conjecture) :
    (n+1).nth Prime - n.nth Prime < (log (n.nth Prime))^2 - log (n.nth Prime)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Firoozbakht.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Firoozbakht.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Firoozbakht.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Firoozbakht.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Firoozbakht%27s_conjecture)
