---
declaration: theorem
origin: cited
lean: OeisA117545.conjecture
statement: formalized
---

# Least $k$ such that cyclotomic polynomial $\Phi_k(n)$ is prime

> $a(n) = \min \{k \in \mathbb{N} \mid 0 < k \wedge \text{Prime}(|\Phi_k(n)|) \}$,
> where $\Phi_k(n)$ is the $k$-th cyclotomic polynomial evaluated at $n$.
>
> *References:*
> - [A117545](https://oeis.org/A117545)

*Quoted from [FormalConjectures/OEIS/117545.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/117545.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA117545.conjecture`

Open: stated without proof.

> Is $a(n)$ defined for all $n \ge 1$?
> That is, for every $n \ge 1$, does there exist $k > 0$ such that $|\Phi_k(n)|$ is prime?

```lean
theorem conjecture (n : ℕ) (hn : 0 < n) :
    ∃ k > 0, ((Polynomial.cyclotomic k ℤ).eval (n : ℤ)).natAbs.Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/117545.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/117545.lean#L117).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/117545.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/117545.lean)
- [A117545](https://oeis.org/A117545)
