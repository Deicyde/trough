---
declaration: theorem
origin: cited
lean: OeisA218585.conjecture_1, OeisA218585.conjecture_2, OeisA218585.conjecture_3, OeisA218585.conjecture_4
statement: formalized
---

# Partitions $n = x + y$ with $x^2 + xy + y^2$ prime

> For $n \ge 1$, $a(n)$ is the number of ways to write $n$ as $x + y$ with $0 < x \le y$ such that
> $x^2 + xy + y^2$ is prime.
>
> *References:*
> - [A218585](https://oeis.org/A218585)
> - E. Hecke, "Eine neue Art von Zetafunktionen und ihre Beziehungen zur Verteilung der Primzahlen.
>   Zweite Mitteilung", Math. Z. **6** (1920), 11–51.

*Quoted from [FormalConjectures/OEIS/218585.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/218585.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open and 2 solved. It also has 6 test statements, counted here but not shown.

## `OeisA218585.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 1$ with the only exception $n = 8$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 1 < n) (h8 : n ≠ 8) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/218585.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/218585.lean#L76).

## `OeisA218585.conjecture_2`

Open: stated without proof.

> Conjecture: The number of primes of the form $nx + (n - x)^2$
> with $0 < x < n / 3$ is positive for $n > 12$.
> - _Zak Seidov_, Sep 25 2013

```lean
theorem conjecture_2 (n : ℕ) (hn : 12 < n) :
    ∃ x : ℕ, 0 < x ∧ 3 * x < n ∧ Nat.Prime (n * x + (n - x) ^ 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/218585.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/218585.lean#L85).

## `OeisA218585.conjecture_3`

Solved: stated here without proof.

> $$\lim_{N \to \infty} \frac{\sum_{p < N, \, p \equiv 1 \pmod 3} x(p)}{\sum_{p < N, \, p \equiv 1 \pmod 3} y(p)} = 1 + \sqrt{3},$$
>
> where for a prime $p \equiv 1 \pmod 3$, $x(p) > y(p) > 0$ are the unique positive integers such
> that $p = x(p)^2 + x(p)y(p) + y(p)^2$.
> - _Zhi-Wei Sun_
>
> This follows from Hecke's (1920) equidistribution theorem for Hecke Grossencharacters of
> $\mathbb{Q}(\sqrt{-3})$ and partial summation with the prime number theorem.

```lean
theorem conjecture_3 :
    Filter.atTop.Tendsto
      (fun N : ℕ =>
        (∑ p ∈ (Finset.range N).filter (fun p => p.Prime ∧ p % 3 = 1), (xp p : ℝ)) /
        (∑ p ∈ (Finset.range N).filter (fun p => p.Prime ∧ p % 3 = 1), (yp p : ℝ)))
      (nhds (1 + Real.sqrt 3))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/218585.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/218585.lean#L99).

## `OeisA218585.conjecture_4`

Solved: stated here without proof.

> Conjecture:
>
> $$\lim_{N \to \infty} \frac{\sum_{p < N, \, p \equiv 1 \pmod 3} x(p)^2}{\sum_{p < N, \, p \equiv 1 \pmod 3} y(p)^2} = \frac{52}{9},$$
>
> where for a prime $p \equiv 1 \pmod 3$, $x(p) > y(p) > 0$ are the unique positive integers such
> that $p = x(p)^2 + x(p)y(p) + y(p)^2$.
> - _Zhi-Wei Sun_
>
> Disproved by Hecke's (1920) equidistribution theorem for Hecke Grossencharacters of
> $\mathbb{Q}(\sqrt{-3})$, which yields the true limit
>
> $$\frac{\int_0^{\pi/6} (\cos\theta - \frac{1}{\sqrt{3}}\sin\theta)^2\,d\theta}{\int_0^{\pi/6} \frac{4}{3}\sin^2\theta\,d\theta} = \frac{2\pi}{2\pi - 3\sqrt{3}} \approx 5.780124 \neq \frac{52}{9}.$$

```lean
theorem conjecture_4 :
    ¬ Filter.atTop.Tendsto
      (fun N : ℕ =>
        (∑ p ∈ (Finset.range N).filter (fun p => p.Prime ∧ p % 3 = 1), ((xp p : ℝ) ^ 2)) /
        (∑ p ∈ (Finset.range N).filter (fun p => p.Prime ∧ p % 3 = 1), ((yp p : ℝ) ^ 2)))
      (nhds (52 / 9 : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/218585.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/218585.lean#L119).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/218585.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/218585.lean)
- [A218585](https://oeis.org/A218585)
