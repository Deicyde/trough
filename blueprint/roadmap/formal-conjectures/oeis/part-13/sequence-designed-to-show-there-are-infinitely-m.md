---
declaration: theorem
origin: cited
lean: OeisA231830.conjecture
statement: formalized
---

# Sequence designed to show there are infinitely many primes congruent to $1$ modulo $4$

> The sequence defined by $a(0) = 1$, $a(1) = 5$, and for $n > 1$,
> $a(n) = (a(n-1) - 1) \cdot a(n-1)^2 + 1 = 1 + 4 \prod_{i=1}^{n-1} a(i)^2$.
>
> *References:*
> - [A231830](https://oeis.org/A231830)

*Quoted from [FormalConjectures/OEIS/231830.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/231830.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA231830.conjecture`

Open: stated without proof.

> Similarly to Sylvester's sequence (A000058), it is unknown if all terms are squarefree.

```lean
theorem conjecture : ∀ n : ℕ, Squarefree (a n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/231830.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/231830.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/231830.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/231830.lean)
- [A231830](https://oeis.org/A231830)
