---
declaration: theorem
origin: cited
lean: OeisA197630.conjecture
statement: formalized
---

# Lerch quotients of odd primes

> The Lerch quotient of an odd prime $p$ is given by
>
> $$L_p = \frac{\left(\sum_{k=1}^{p-1} q_p(k)\right) - w_p}{p}$$
>
> where $q_p(k) = (k^{p-1}-1)/p$ is the Fermat quotient and $w_p = ((p-1)!+1)/p$ is the Wilson
> quotient. For $n > 1$, $a(n)$ is the Lerch quotient of the $n$-th prime $p_n$.
>
> *References:*
> - [A197630](https://oeis.org/A197630)

*Quoted from [FormalConjectures/OEIS/197630.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/197630.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA197630.conjecture`

Open: stated without proof.

> "Is $13$ the only Lerch quotient that is itself prime?"

```lean
theorem conjecture : ∀ n : ℕ, 1 < n → (a n).Prime → a n = 13
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/197630.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/197630.lean#L87).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/197630.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/197630.lean)
- [A197630](https://oeis.org/A197630)
