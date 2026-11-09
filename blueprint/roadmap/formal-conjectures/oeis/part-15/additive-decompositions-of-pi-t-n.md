---
declaration: theorem
origin: cited
lean: OeisA262403.conjecture_1, OeisA262403.conjecture_2, OeisA262403.conjecture_3, OeisA262403.conjecture_4
statement: formalized
---

# Additive decompositions of $\pi(T(n))$

> Number of ways to write $\pi(T(n)) = \pi(T(k)) + \pi(T(m))$ with $1 < k < m < n$,
> where $T(x) = \frac{x(x+1)}{2}$ is the $x$-th triangular number and $\pi(x)$ is the number of
> primes not exceeding $x$.
>
> *References:*
> - [A262403](https://oeis.org/A262403)
> - [Problems on combinatorial properties of primes](https://arxiv.org/abs/1402.6641)
>   by *Zhi-Wei Sun*, arXiv:1402.6641 (2014)

*Quoted from [FormalConjectures/OEIS/262403.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/262403.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 open. It also has 6 test statements, counted here but not shown.

## `OeisA262403.conjecture_1`

Open: stated without proof.

> Conjecture (i): $a(n) > 0$ for all $n > 4$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 4 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262403.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/262403.lean#L76).

## `OeisA262403.conjecture_2`

Open: stated without proof.

> Conjecture (i): $a(n) = 1$ only for $n = 5, 6, 7, 10, 12, 32, 38, 445, 727$.

```lean
theorem conjecture_2 (n : ℕ) (hn : 4 < n) :
    a n = 1 ↔ n ∈ singletons
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262403.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/262403.lean#L83).

## `OeisA262403.conjecture_3`

Open: stated without proof.

> Conjecture (ii), first assertion: All numbers $\pi(T(n))$ ($n = 1, 2, 3, \dots$) are pairwise
> distinct.

```lean
theorem conjecture_3 (m n : ℕ) (hm : 0 < m) (hn : 0 < n)
    (h : primeCountTriangular m = primeCountTriangular n) : m = n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262403.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/262403.lean#L92).

## `OeisA262403.conjecture_4`

Open: stated without proof.

> Conjecture (ii), second assertion: If $\sum_{i=j}^{k} \frac{1}{\pi(T(i))}$ and
> $\sum_{r=s}^{t} \frac{1}{\pi(T(r))}$ with $1 < j \le k$ and $j \le s \le t$ have the same
> fractional part but $(j, k) \ne (s, t)$, then $j = 2$, $k = 5$, and $s = t = 4$.

```lean
theorem conjecture_4 (j k s t : ℕ) (hj : 1 < j) (hjk : j ≤ k) (hjs : j ≤ s)
    (hst : s ≤ t) (hne : (j, k) ≠ (s, t))
    (h : Int.fract (∑ i ∈ Finset.Icc j k, (primeCountTriangular i : ℚ)⁻¹) =
         Int.fract (∑ r ∈ Finset.Icc s t, (primeCountTriangular r : ℚ)⁻¹)) :
    j = 2 ∧ k = 5 ∧ s = 4 ∧ t = 4
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262403.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/262403.lean#L102).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/262403.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/262403.lean)
- [A262403](https://oeis.org/A262403)
