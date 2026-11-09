---
declaration: theorem
origin: cited
lean: OeisA115366.conjecture
statement: formalized
---

# $a(n)$ = the number of values of $k <= 10^n$ such that $\sqrt{k(k+1)(k+2)(k+3)+1}$ is prime

> Since $\sqrt{k(k+1)(k+2)(k+3)+1} = k^2 + 3k + 1$,
> $a(n) = \#\{k \in \mathbb{N} \mid 1 \le k \le 10^n \land (k^2 + 3k + 1) \text{ is prime} \}.$
>
> *References:*
> - [A115366](https://oeis.org/A115366)

*Quoted from [FormalConjectures/OEIS/115366.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/115366.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA115366.conjecture`

Open: stated without proof.

> Conjecture: $a(n)/A006880(n) \rightarrow 1.77...$
> where A006880(n) is the number of primes $\le 10^n$.

```lean
theorem conjecture :
    ∃ L : ℝ,
      Tendsto (fun n : ℕ => (a n : ℝ) / (Nat.primeCounting' (10 ^ n) : ℝ)) atTop (nhds L) ∧
      1.77 ≤ L ∧ L ≤ 1.78
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/115366.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/115366.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/115366.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/115366.lean)
- [A115366](https://oeis.org/A115366)
