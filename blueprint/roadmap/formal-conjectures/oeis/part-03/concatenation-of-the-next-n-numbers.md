---
declaration: theorem
origin: cited
lean: OeisA53067.conjecture
statement: formalized
---

# Concatenation of the next $n$ numbers

> $a(n)$ is the concatenation of the next $n$ numbers: the integers from
> $\frac{(n-1)n}{2} + 1$ up to $\frac{n(n+1)}{2}$.
>
> *References:*
> - [A053067](https://oeis.org/A053067)

*Quoted from [FormalConjectures/OEIS/53067.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/53067.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA53067.conjecture`

Open: stated without proof.

> "The second term is a prime. When is the next prime, if there is another?
> - _N. J. A. Sloane_, Dec 16 2016"

```lean
theorem conjecture :
    conjecture.answer =
      if h : ∃ n, 2 < n ∧ (a n).Prime then
        some (sInf {n | 2 < n ∧ (a n).Prime})
      else
        none
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/53067.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/53067.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/53067.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/53067.lean)
- [A053067](https://oeis.org/A053067)
