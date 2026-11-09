---
declaration: theorem
origin: cited
lean: Erdos983.erdos_983.parts.i, Erdos983.erdos_983.parts.ii, Erdos983.erdos_983.variants.le_primeCounting, Erdos983.erdos_983.variants.upper_bound, Erdos983.erdos_983.variants.erdos_straus
statement: formalized
---

# Erdős Problem 983

> *References:*
> - [erdosproblems.com/983](https://www.erdosproblems.com/983)
> - [Er70b] Erdős, P., *Some applications of graph theory to number theory*. Proc. Second Chapel
>   Hill Conf. on Combinatorial Mathematics and its Applications (Univ. North Carolina, Chapel
>   Hill, N.C., 1970) (1970), 136-145. [PDF](https://www.renyi.hu/~p_erdos/1970-20.pdf)
> - [Po79] Pomerance, C., *The prime number graph*. Math. Comp. 33 (1979), 399-408.
>   [PDF](https://math.dartmouth.edu/~carlp/PDF/paper19.pdf)

*Quoted from [FormalConjectures/ErdosProblems/983.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/983.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/983](https://www.erdosproblems.com/983).

The file states 5 research or textbook statements: 1 open, 3 solved and 1 textbook result. It also has 1 API statement, counted here but not shown.

## `Erdos983.erdos_983.parts.i`

Solved: stated here without proof.

> Let $n\geq 2$ and $\pi(n)\lt k\leq n$. Let $f(k,n)$ be the smallest integer $r$ such that in any
> $A\subseteq \{1,\ldots,n\}$ of size $\lvert A\rvert=k$ there exist primes $p_1,\ldots,p_r$ such
> that $>r$ many $a\in A$ are only divisible by primes from $\{p_1,\ldots,p_r\}$.
>
> Is it true that
> $$2\pi(n^{1/2})-f(\pi(n)+1,n)\to \infty$$
> as $n\to \infty$?
>
> This is the first part. The primes may depend on $A$. Erdős and Straus conjectured this
> [Er70b, p. 138 and p. 140].
>
> The answer is no: Liam Price and GPT-5.5 Pro showed on the
> [forum](https://www.erdosproblems.com/forum/thread/983#post-6104) that
> $f(\pi(n)+1,n)=2\pi(n^{1/2})+1$ for infinitely many $n$; see the
> [explanation](https://www.erdosproblems.com/forum/thread/983#post-6525) by Nat Sothanaphan.
> Write $p_k$ for the $k$-th prime. By [Po79, Corollary after Theorem 2.2] there are infinitely
> many $N$ with $p_{N-i}p_{N+i}\lt p_N^2$ for $1\leq i\lt N$. Take $n=p_N^2-1$, so
> $\pi(n^{1/2})=N-1$. Let $A$ consist of the products of adjacent primes on the path
> $p_{2N-1},p_1,p_{2N-2},p_2,\ldots,p_{N+1},p_{N-1},p_N$, its two endpoint primes, and the
> other primes up to $n$. Then $\lvert A\rvert=\pi(n)+1$, and for any $r\leq 2N-2$ primes at
> most $r$ elements of $A$ are divisible only by those primes, so $f(\pi(n)+1,n)\geq 2N-1$.

```lean
theorem erdos_983.parts.i :
    ¬ Tendsto (fun n : ℕ ↦
      2 * (Nat.primeCounting (Nat.sqrt n) : ℤ) - (f (Nat.primeCounting n + 1) n : ℤ))
      atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/983.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/983.lean#L86).

## `Erdos983.erdos_983.parts.ii`

Open: stated without proof.

> Let $n\geq 2$ and $\pi(n)\lt k\leq n$. Let $f(k,n)$ be the smallest integer $r$ such that in any
> $A\subseteq \{1,\ldots,n\}$ of size $\lvert A\rvert=k$ there exist primes $p_1,\ldots,p_r$ such
> that $>r$ many $a\in A$ are only divisible by primes from $\{p_1,\ldots,p_r\}$.
>
> In general, estimate $f(k,n)$, particularly when $\pi(n)+1\lt k=o(n)$.
>
> This is the second part. We read "estimate" as an asymptotic formula `answer k n`, valid for
> every function $k=k(n)$ with $\pi(n)+1\lt k(n)=o(n)$.

```lean
theorem erdos_983.parts.ii :
    ∀ k : ℕ → ℕ, (∀ᶠ n : ℕ in atTop, Nat.primeCounting n + 1 < k n) →
      ((fun n : ℕ ↦ (k n : ℝ)) =o[atTop] (fun n : ℕ ↦ (n : ℝ))) →
      (fun n : ℕ ↦ (f (k n) n : ℝ)) ~[atTop]
        (fun n : ℕ ↦ erdos_983.parts.ii.answer (k n) n)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/983.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/983.lean#L105).

## `Erdos983.erdos_983.variants.le_primeCounting`

Textbook result, stated without proof.

> It is trivial that $f(k,n)\leq \pi(n)$ [Er70b, p. 138]. Here $\pi(n)\lt k$.

```lean
theorem erdos_983.variants.le_primeCounting {k n : ℕ} (hk : Nat.primeCounting n < k) :
    f k n ≤ Nat.primeCounting n
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/983.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/983.lean#L116).

## `Erdos983.erdos_983.variants.upper_bound`

Solved: stated here without proof.

> Erdős and Straus [Er70b, p. 139, (14)] proved
> $$f(\pi(n)+1,n)\leq 2\pi(n^{1/2})+1.$$

```lean
theorem erdos_983.variants.upper_bound (n : ℕ) :
    f (Nat.primeCounting n + 1) n ≤ 2 * Nat.primeCounting (Nat.sqrt n) + 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/983.lean, line 125](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/983.lean#L125).

## `Erdos983.erdos_983.variants.erdos_straus`

Solved: stated here without proof.

> Erdős and Straus proved [Er70b, pp. 138-140] that
> $$f(\pi(n)+1,n)=2\pi(n^{1/2})+o_A\left(\frac{n^{1/2}}{(\log n)^A}\right)$$
> for any $A>0$.

```lean
theorem erdos_983.variants.erdos_straus :
    ∀ A : ℝ, 0 < A →
      (fun n : ℕ ↦ (f (Nat.primeCounting n + 1) n : ℝ) -
          2 * (Nat.primeCounting (Nat.sqrt n) : ℝ)) =o[atTop]
        (fun n : ℕ ↦ Real.sqrt n / Real.log n ^ A)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/983.lean, line 135](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/983.lean#L135).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/983.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/983.lean)
- [erdosproblems.com/983](https://www.erdosproblems.com/983)
