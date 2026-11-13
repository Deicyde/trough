---
declaration: theorem
origin: cited
lean: OeisA189409.conjecture_1, OeisA189409.conjecture_2
statement: formalized
---

# Primorial squared plus one

> The sequence $a(n)$ is defined by $a(n) = (p_n\#)^2 + 1$, where $p_n\# = \prod_{k=0}^{n-1} p_k$
> is the $n$-th primorial (A002110).
>
> *References:*
> - [A189409](https://oeis.org/A189409)

*Quoted from [FormalConjectures/OEIS/189409.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/189409.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA189409.conjecture_1`

Open: stated without proof.

> It is unknown whether or not numbers in this sequence are always squarefree.
> - _John M. Campbell_, Apr 21 2011

```lean
theorem conjecture_1 : ∀ n : ℕ, Squarefree (a n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/189409.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/189409.lean#L58).

## `OeisA189409.conjecture_2`

Open: stated without proof.

> It is unknown whether or not there exist infinitely many primes in this sequence.
> - _John M. Campbell_, Apr 21 2011

```lean
theorem conjecture_2 : Set.Infinite {n : ℕ | (a n).Prime}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/189409.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/189409.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/189409.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/189409.lean)
- [A189409](https://oeis.org/A189409)
