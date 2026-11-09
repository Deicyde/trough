---
declaration: theorem
origin: cited
lean: OeisA129365.conjecture1, OeisA129365.conjecture2, OeisA129365.conjecture3, OeisA129365.conjecture4
statement: formalized
---

# Ratio of product of GCDs to product of factorials of floor divisions

> $$a(n) = \frac{\prod_{j=1}^n \prod_{k=1}^n \gcd(j,k)}{\prod_{k=1}^n (\lfloor n/k \rfloor!)^k}$$
>
> *References:*
> - [A129365](https://oeis.org/A129365)

*Quoted from [FormalConjectures/OEIS/129365.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/129365.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 solved. It also has 5 test statements, counted here but not shown.

## `OeisA129365.conjecture1`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a129365-conjectures/blob/9c0201540c337733d6b8afb2aff209f5489c122a/lean/OeisA129365FC.lean#L234-L395](https://github.com/KitaKen1/oeis-a129365-conjectures/blob/9c0201540c337733d6b8afb2aff209f5489c122a/lean/OeisA129365FC.lean#L234-L395).

> Conjecture (1): $a(n)$ is always an integer (the denominator divides the numerator).
>
> Proof summary:
>
> Let $c(n) = \prod_{j=1}^n \prod_{k=1}^n (j,k)$ be the numerator.
> Observe that
> $$\textrm{ord}(c(n), p) = \left\lfloor \frac{n}{p} \right\rfloor^2 + \left\lfloor \frac{n}{p^2} \right\rfloor^2 + ...$$
> proven similar to Legendre's formula for $\textrm{ord}(n!, p)$.
>
> Next let $d(n) = \prod_{k=1}^n (\lfloor n/k \rfloor!)^k$ be the denominator.
> Observe that
> $$\textrm{ord}(d(n), p) = \sum_{k=1}^n k\,\textrm{ord}(\lfloor n/k \rfloor, p) = \sum_{k=1}^n \sum_{r \geq 1} k \left\lfloor \frac{\lfloor n/p^r \rfloor}{k} \right\rfloor.$$
>
> Combining the two gives:
> $$\textrm{ord}(a(n), p) = \sum_{r \geq 1} \sum_{k=1}^n \left(\left\lfloor \frac{n}{p^r} \right\rfloor \textrm{mod } k\right).$$
>
> Defining $b(m) = \sum_{k=1}^m m \textrm{ mod } k$, we obtain $\textrm{ord}(a(n), p) = \sum_{r \geq 1} b(\lfloor n/p^r \rfloor)$.
>
> As $b(m) \geq 0$, $\textrm{ord}(a(n), p)$ is non-negative for any $p$, so $a(n)$ is an integer.

```lean
theorem conjecture1 (n : ℕ) (hn : 0 < n) :
    ((Finset.Icc 1 n).prod fun k => (n / k).factorial ^ k) ∣
      ((Finset.Icc 1 n).prod fun j => (Finset.Icc 1 n).prod fun k => Nat.gcd j k)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/129365.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/129365.lean#L88).

## `OeisA129365.conjecture2`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a129365-conjectures/blob/9c0201540c337733d6b8afb2aff209f5489c122a/lean/OeisA129365FC.lean#L234-L395](https://github.com/KitaKen1/oeis-a129365-conjectures/blob/9c0201540c337733d6b8afb2aff209f5489c122a/lean/OeisA129365FC.lean#L234-L395).

> Conjecture (2): If $p$ is a prime, then $p \mid a(n)$ if and only if $p \le n/3$.
>
> Proof summary:
>
> We use the formula shown above:
> $\textrm{ord}(a(n), p) = \sum_{r \geq 1} b(\lfloor n/p^r \rfloor)$ where
> $b(m) = \sum_{k=1}^m m \textrm{ mod } k$.
>
> If $p ∣ a(n)$ then $b(\lfloor n/p^r \rfloor) ≥ 1$ for some $r ≥ 1$. Since b(m) = 0$ for $m \leq 2$,
> we must have $n / p^r \geq 3$. If the inequality holds for $r \geq 1$, it must be true for $r = 1$.
> Hence $n \geq 3p$, proving the conjecture.

```lean
theorem conjecture2 (n p : ℕ) (hn : 0 < n) (hp : p.Prime) :
    (∃ m : ℕ, a n = m ∧ p ∣ m) ↔ p ≤ n / 3
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/129365.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/129365.lean#L110).

## `OeisA129365.conjecture3`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a129365-conjectures/blob/9c0201540c337733d6b8afb2aff209f5489c122a/lean/OeisA129365FC.lean#L234-L395](https://github.com/KitaKen1/oeis-a129365-conjectures/blob/9c0201540c337733d6b8afb2aff209f5489c122a/lean/OeisA129365FC.lean#L234-L395).

> Conjecture (3): For each positive integer $n$, prime $p$, and $0 \le k < p$,
> $\mathrm{ord}_p(a(np)) = \mathrm{ord}_p(a(np + k))$.
>
> Proof summary:
>
> This follows from the formula shown above:
> $\textrm{ord}(a(n), p) = \sum_{r \geq 1} b(\lfloor n/p^r \rfloor)$ where
> $b(m) = \sum_{k=1}^m m \textrm{ mod } k$.
>
> Since $k < p$, we have $\lfloor (np + k)/p^r \rfloor = \lfloor np/p^r \rfloor$ for every $r \geq 1$,
> proving the claim.

```lean
theorem conjecture3 (n p k : ℕ) (hn : 0 < n) (hp : p.Prime) (hk : k < p) :
    padicValRat p (a (n * p)) = padicValRat p (a (n * p + k))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/129365.lean, line 131](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/129365.lean#L131).

## `OeisA129365.conjecture4`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a129365-conjectures/blob/9c0201540c337733d6b8afb2aff209f5489c122a/lean/OeisA129365FC.lean#L234-L395](https://github.com/KitaKen1/oeis-a129365-conjectures/blob/9c0201540c337733d6b8afb2aff209f5489c122a/lean/OeisA129365FC.lean#L234-L395).

> Conjecture (4): Let $b(n) = \mathrm{A004125}(n) = \sum_{k=1}^n (n \bmod k)$. Then
> $\mathrm{ord}_p(a(np)) = \sum_{i \ge 0} b(\lfloor n/p^i \rfloor)$.
>
> Proof summary:
>
> This follows directly from the formula shown at the beginning:
> $\textrm{ord}(a(n), p) = \sum_{r \geq 1} b(\lfloor n/p^r \rfloor)$ where
> $b(m) = \sum_{k=1}^m m \textrm{ mod } k$.

```lean
theorem conjecture4 (n p : ℕ) (hn : 0 < n) (hp : p.Prime) :
    padicValRat p (a (n * p)) = ∑' i : ℕ, (b (n / p ^ i) : ℤ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/129365.lean, line 149](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/129365.lean#L149).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/129365.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/129365.lean)
- [A129365](https://oeis.org/A129365)
