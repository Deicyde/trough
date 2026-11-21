---
declaration: theorem
origin: cited
lean: OeisA109905.conjecture
statement: formalized
---

# Conjectures associated with A109905

> $a(n)$ is the greatest prime of the form $k(n-k)+1$, where $k$ can take values from
> $1$ to $\lfloor n/2 \rfloor$. $a(n)=0$ if no such prime exists.
>
> *References:*
> - [A109905](https://oeis.org/A109905)

*Quoted from [FormalConjectures/OEIS/109905.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/109905.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA109905.conjecture`

Open: stated without proof.

> $a(n) = 0$ for $n = 1$, $6$, $30$ and $54$. Are there any others?

```lean
theorem conjecture :
    ∃ n : ℕ, n > 0 ∧ a n = 0 ∧ n ∉ ({1, 6, 30, 54} : Finset ℕ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/109905.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/109905.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/109905.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/109905.lean)
- [A109905](https://oeis.org/A109905)
