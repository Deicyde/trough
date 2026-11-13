---
declaration: theorem
origin: cited
lean: OeisA208425.conjecture_1, OeisA208425.conjecture_2, OeisA208425.conjecture_3
statement: formalized
---

# Expansion of $\sum_{n \ge 0} \frac{(3n)!}{n!^3} \frac{x^{2n}}{(1-x)^{3n+1}}$

> The sequence $a(n)$ given by the expansion of
> $\sum_{n \ge 0} \frac{(3n)!}{n!^3} \frac{x^{2n}}{(1-x)^{3n+1}}$, which satisfies
>
> $$a(n) = \sum_{k=0}^n \binom{n}{k} \binom{n-k}{k} \binom{n+k}{k}.$$
>
> *References:*
> - [A208425](https://oeis.org/A208425)

*Quoted from [FormalConjectures/OEIS/208425.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/208425.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 5 test statements, counted here but not shown.

## `OeisA208425.conjecture_1`

Open: stated without proof.

> Conjecture (i): For any prime $p > 3$ and positive integer $n$, the number
> $(a(pn)-a(n))/(pn)^3$ is always a $p$-adic integer.
> - _Zhi-Wei Sun_, Nov 12 2016

```lean
theorem conjecture_1 (p : ℕ) (hp : p.Prime) (hpgt3 : 3 < p) (n : ℕ) (hn : 0 < n) :
    0 ≤ padicValRat p (((a (p * n) : ℚ) - (a n : ℚ)) / ((p * n : ℚ) ^ 3))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/208425.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/208425.lean#L61).

## `OeisA208425.conjecture_2`

Open: stated without proof.

> Conjecture (ii), part 1: For any prime $p \equiv 1 \pmod{3}$, we have
> $\sum_{k=0}^{p-1} a(k) \equiv \binom{2(p-1)/3}{(p-1)/3} \pmod{p^2}$.
> - _Zhi-Wei Sun_, Nov 12 2016

```lean
theorem conjecture_2 (p : ℕ) (hp : p.Prime) (hmod : p % 3 = 1) :
    (∑ k ∈ Finset.range p, a k) % (p ^ 2) =
      ((2 * (p - 1) / 3).choose ((p - 1) / 3)) % (p ^ 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/208425.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/208425.lean#L71).

## `OeisA208425.conjecture_3`

Open: stated without proof.

> Conjecture (ii), part 2: For any prime $p \equiv 2 \pmod{3}$, we have
> $\sum_{k=0}^{p-1} a(k) \equiv \frac{2p}{\binom{2(p+1)/3}{(p+1)/3}} \pmod{p^2}$.
> - _Zhi-Wei Sun_, Nov 12 2016

```lean
theorem conjecture_3 (p : ℕ) (hp : p.Prime) (hmod : p % 3 = 2) :
    ((∑ k ∈ Finset.range p, (a k : ℚ)) -
      (2 * p : ℚ) / ((2 * (p + 1) / 3).choose ((p + 1) / 3) : ℚ)).num % (p ^ 2 : ℤ) = 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/208425.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/208425.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/208425.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/208425.lean)
- [A208425](https://oeis.org/A208425)
