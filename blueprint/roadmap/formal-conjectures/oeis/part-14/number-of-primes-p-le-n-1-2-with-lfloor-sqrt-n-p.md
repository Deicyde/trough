---
declaration: theorem
origin: cited
lean: OeisA237720.conjecture_1, OeisA237720.conjecture_2, OeisA237720.conjecture_3
statement: formalized
---

# Number of primes $p \le (n+1)/2$ with $\lfloor\sqrt{n-p}\rfloor$ prime

> The sequence $a(n)$ counts the number of primes $p \le \lfloor (n+1)/2 \rfloor$ such that
> $\lfloor\sqrt{n-p}\rfloor$ is prime.
>
> *References:*
> - [A237720](https://oeis.org/A237720)

*Quoted from [FormalConjectures/OEIS/237720.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/237720.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 7 test statements, counted here but not shown.

## `OeisA237720.conjecture_1`

Open: stated without proof.

> Conjecture (i): $a(n) > 0$ for all $n > 5$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 5 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/237720.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/237720.lean#L65).

## `OeisA237720.conjecture_2`

Open: stated without proof.

> Conjecture: $a(n) = 1$ only for $n = 6, 23, 24, 111, 112, \ldots, 120$.

```lean
theorem conjecture_2 (n : ℕ) :
    a n = 1 ↔ n = 6 ∨ n = 23 ∨ n = 24 ∨ (111 ≤ n ∧ n ≤ 120)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/237720.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/237720.lean#L72).

## `OeisA237720.conjecture_3`

Open: stated without proof.

> Conjecture (ii): For any integer $n > 2$, there is a prime $p < n$
> with $\lfloor\sqrt{n+p}\rfloor$ prime.

```lean
theorem conjecture_3 (n : ℕ) (hn : 2 < n) :
    ∃ p : ℕ, p.Prime ∧ p < n ∧ (Nat.sqrt (n + p)).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/237720.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/237720.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/237720.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/237720.lean)
- [A237720](https://oeis.org/A237720)
