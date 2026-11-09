---
declaration: theorem
origin: cited
lean: OeisA67857.conjecture
statement: formalized
---

# Sum of $a(k)/k!$ over divisors equals harmonic number

> The sequence $a(n)$ satisfies $\sum_{k \mid n} \frac{a(k)}{k!} = \sum_{j=1}^n \frac{1}{j} = H_n$,
> where the sum on the left is over positive divisors $k$ of $n$. By Möbius inversion,
> $$a(n) = n! \sum_{d \mid n} \mu(n/d) H_d$$
> where $H_d = \sum_{j=1}^d \frac{1}{j}$ is the $d$-th harmonic number.
>
> *References:*
> - [A067857](https://oeis.org/A067857)
> - [A001221](https://oeis.org/A001221)

*Quoted from [FormalConjectures/OEIS/67857.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/67857.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA67857.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/SamuelSchlesinger/a067857-counterexample/blob/44317ddb5bd735f7a1f6764c22db10c455e4b584/Counterexample.lean#L89-L92](https://github.com/SamuelSchlesinger/a067857-counterexample/blob/44317ddb5bd735f7a1f6764c22db10c455e4b584/Counterexample.lean#L89-L92).

> The terms are not all positive. The first negative one is
> $a(30) = -22690644647302814715858124800000$.
> Conjecture: $a(n) < 0$ if and only if A001221(n) is an odd number $\ge 3$.
>
> This conjecture is false. A counterexample is the product of all primes at most $1000$,
> which has $168$ distinct prime factors and a negative sequence value.
>
> The counterexample and formal proof were developed by Codex (GPT-6),
> prompted by Samuel Schlesinger.

```lean
theorem conjecture :
    ¬ ∀ n : ℕ, 0 < n →
      (a n < 0 ↔ Odd (cardDistinctFactors n) ∧ 3 ≤ cardDistinctFactors n)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/67857.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/67857.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/67857.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/67857.lean)
- [A067857](https://oeis.org/A067857)
