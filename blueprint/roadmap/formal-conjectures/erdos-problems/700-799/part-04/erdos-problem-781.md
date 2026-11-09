---
declaration: theorem
origin: cited
lean: Erdos781.erdos_781.parts.i, Erdos781.erdos_781.parts.ii, Erdos781.erdos_781.variants.brown_erdos_freedman
statement: formalized
---

# Erdős Problem 781

> *References:*
> - [erdosproblems.com/781](https://www.erdosproblems.com/781)
> - [BEF90] Brown, T. C. and Erdős, P. and Freedman, A. R., _Quasi-progressions and descending
>   waves_. J. Combin. Theory Ser. A (1990), 81-95.
> - [AlSp89] Alon, N. and Spencer, Joel, _Ascending waves_. J. Combin. Theory Ser. A (1989),
>   275-287.

*Quoted from [FormalConjectures/ErdosProblems/781.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/781.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/781](https://www.erdosproblems.com/781).

The file states 3 research or textbook statements: 3 solved.

## `Erdos781.erdos_781.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos781.lean#L3202](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos781.lean#L3202).

> Let $f(k)$ be the minimal $n$ such that any $2$-colouring of $\{1,\ldots,n\}$ contains a
> monochromatic $k$-term descending wave: a sequence $x_1\lt \cdots \lt x_k$ such that, for $1\lt j\lt k$,
>
> $$x_j \geq \frac{x_{j+1}+x_{j-1}}{2}.$$
>
> Estimate $f(k)$.
>
> Brown, Erdős, and Freedman [BEF90] proved $k^2-k+1\leq f(k) \leq \frac{k^3-4k+9}{3}$. Resolved by
> Alon and Spencer [AlSp89] who proved that in fact $f(k) \gg k^3$, so that $f(k)\asymp k^3$.

```lean
theorem erdos_781.parts.i : (fun k ↦ (f k : ℝ)) =Θ[atTop] fun k ↦ (k : ℝ) ^ 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/781.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/781.lean#L61).

## `Erdos781.erdos_781.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos781.lean#L3202](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos781.lean#L3202).

> Is it true that $f(k)=k^2-k+1$ for all $k$?
>
> The answer is no, since $f(k)\gg k^3$ by Alon and Spencer [AlSp89].

```lean
theorem erdos_781.parts.ii : ¬ ∀ k ≥ 1, f k = k ^ 2 - k + 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/781.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/781.lean#L72).

## `Erdos781.erdos_781.variants.brown_erdos_freedman`

Solved: stated here without proof.

> Brown, Erdős, and Freedman [BEF90] proved $k^2-k+1\leq f(k) \leq \frac{k^3-4k+9}{3}$.

```lean
theorem erdos_781.variants.brown_erdos_freedman (k : ℕ) (hk : 1 ≤ k) :
    k ^ 2 - k + 1 ≤ f k ∧ (f k : ℚ) ≤ (k ^ 3 - 4 * k + 9) / 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/781.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/781.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/781.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/781.lean)
- [erdosproblems.com/781](https://www.erdosproblems.com/781)
