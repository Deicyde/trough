---
declaration: theorem
origin: cited
lean: OeisA114362.conjecture1, OeisA114362.conjecture2
statement: formalized
---

# Numerator of $\zeta(4n)/\zeta(2n)^2$ (with $a(0)=2$ instead of $-2$)

> The ratio $\zeta(4n)/\zeta(2n)^2$ for $n \ge 1$ is the rational number
>
> $$ Q_n = -2 \frac{B_{4n}}{B_{2n}^2 \binom{4n}{2n}} $$
>
> where $B_k$ is the $k$-th Bernoulli number. The sequence $a(n)$ is the numerator of $Q_n$,
> with $a(0)$ defined as $2$.
>
> *References:*
> - [A114362](https://oeis.org/A114362)

*Quoted from [FormalConjectures/OEIS/114362.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/114362.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 4 test statements, counted here but not shown.

## `OeisA114362.conjecture1`

Open: stated without proof.

> Conjecture: if an integer $n > 1$ is odd, then $\zeta(2n)/\zeta(n)^2$ is irrational.
> Cf. W. Kohnen (link) and my conjecture in A348829. - Thomas Ordowski, Jan 05 2022

```lean
theorem conjecture1 (n : ℕ) (hn_gt_one : 1 < n) (hn_odd : Odd n) :
    Irrational ((riemannZeta (2 * n : ℂ) / (riemannZeta (n : ℂ)) ^ 2).re)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/114362.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/114362.lean#L89).

## `OeisA114362.conjecture2`

Solved: stated here; a Lean proof is at [https://github.com/chy4pro/formal-conjectures/blob/872759d0b464254d868f107fe7f9cf762900f57d/FormalConjectures/OEIS/114362.lean#L646](https://github.com/chy4pro/formal-conjectures/blob/872759d0b464254d868f107fe7f9cf762900f57d/FormalConjectures/OEIS/114362.lean#L646).

> Conjecture:
> $\frac{1 - t(n)}{1 + t(n)} = \frac{1}{2^n} + \frac{1}{3^n} + \frac{1}{5^n} + \frac{1}{7^n} +
>   O(\frac{1}{11^n})$,
> where $t(n) = \zeta(2n)/\zeta(n)^2$. Cf. A348829. - Thomas Ordowski, Nov 13 2022

```lean
theorem conjecture2 :
    (fun n : ℕ => (1 - t n) / (1 + t n) -
      (1 / (2:ℝ)^n + 1 / (3:ℝ)^n + 1 / (5:ℝ)^n + 1 / (7:ℝ)^n))
      =O[atTop] (fun n : ℕ => 1 / (11:ℝ)^n)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/114362.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/114362.lean#L106).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/114362.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/114362.lean)
- [A114362](https://oeis.org/A114362)
