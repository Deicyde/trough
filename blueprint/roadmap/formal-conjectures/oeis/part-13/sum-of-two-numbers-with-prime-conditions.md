---
declaration: theorem
origin: cited
lean: OeisA231201.conjecture
statement: formalized
---

# Sum of two numbers with prime conditions

> Number of ways to write $n = x+y$, for $x,y > 0$ such that $2^x + y$ is prime.
>
> Zhi-Wei Sun has offered a \$1000 prize for the first proof.
>
> *References:*
> - [A231201](https://oeis.org/A231201)
> - Zhi-Wei Sun, "Table of n, a(n) for n = 1..10000",
>   "Write n = k + m with 2^k + m prime", a message to Number Theory List, Nov. 16, 2013,
>   "On a^n+ bn modulo m", arXiv:1312.1166 [math.NT], 2013-2014,
>   "Problems on combinatorial properties of primes", arXiv:1402.6641 [math.NT], 2014-2015.

*Quoted from [FormalConjectures/OEIS/231201.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/231201.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements, counted here but not shown.

## `OeisA231201.conjecture`

Open: stated without proof.

> The conjecture for sequence A231201: for any $n > 1$, there exist $x, y > 0$ such that $n = x + y$ and $2^x + y$ is prime.

```lean
theorem conjecture (n : ℕ) (hn : 1 < n) : A n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/231201.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/231201.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/231201.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/231201.lean)
- [A231201](https://oeis.org/A231201)
