---
declaration: theorem
origin: cited
lean: OeisA110566.conjecture
statement: formalized
---

# $a(n) = \operatorname{lcm}\{1,2,\dots,n\}/\operatorname{denom}(H(n))$

> *References:*
> - [A110566](https://oeis.org/A110566)

*Quoted from [FormalConjectures/OEIS/110566.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/110566.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements, counted here but not shown.

## `OeisA110566.conjecture`

Open: stated without proof.

> It is conjectured that every odd number occurs in this sequence.

```lean
theorem conjecture :
  ∀ m : ℕ, Odd m → ∃ n > 0, a n = m
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/110566.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/110566.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/110566.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/110566.lean)
- [A110566](https://oeis.org/A110566)
