---
declaration: theorem
origin: cited
lean: OeisA262781.conjecture_1, OeisA262781.conjecture_2, OeisA262781.conjecture_3
statement: formalized
---

# Representations of $n$ as $x^2 + \phi(y^2) + \phi(z^2)$

> Number of ordered ways to write $n$ as $x^2 + \phi(y^2) + \phi(z^2)$ ($x \ge 0$ and $0 < y \le z$)
> with $y$ or $z$ prime, where $\phi(\cdot)$ is Euler's totient function.
>
> *References:*
> - [A262781](https://oeis.org/A262781)

*Quoted from [FormalConjectures/OEIS/262781.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262781.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 5 test statements, counted here but not shown.

## `OeisA262781.conjecture_1`

Open: stated without proof.

> Conjecture (i): $a(n) > 0$ for all $n > 6$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 6 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262781.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262781.lean#L69).

## `OeisA262781.conjecture_2`

Open: stated without proof.

> Conjecture (i): $a(n) = 1$ only for
> $n = 3, 5, 9, 10, 17, 20, 24, 25, 31, 36, 45, 73, 80, 101, 136, 145, 388, 649$.

```lean
theorem conjecture_2 (n : ℕ) :
    a n = 1 ↔ n ∈ singletons
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262781.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262781.lean#L77).

## `OeisA262781.conjecture_3`

Open: stated without proof.

> Conjecture (ii): For any integer $n > 4$, we can write $2n$ as $\phi(p^2) + \phi(x^2) + \phi(y^2)$
> with $p$ prime and $p \le x \le y$.

```lean
theorem conjecture_3 (n : ℕ) (hn : 4 < n) :
    ∃ p x y : ℕ, p.Prime ∧ p ≤ x ∧ x ≤ y ∧
      2 * n = Nat.totient (p ^ 2) + Nat.totient (x ^ 2) + Nat.totient (y ^ 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262781.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262781.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/262781.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262781.lean)
- [A262781](https://oeis.org/A262781)
