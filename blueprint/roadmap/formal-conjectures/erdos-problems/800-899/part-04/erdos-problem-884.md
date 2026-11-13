---
declaration: theorem
origin: cited
lean: Erdos884.erdos_884, Erdos884.erdos_884_false_of_hardy_littlewood
statement: formalized
---

# Erdős Problem 884

> *References:*
> - [erdosproblems.com/884](https://www.erdosproblems.com/884)
> - [Tao25](https://terrytao.wordpress.com/wp-content/uploads/2025/09/erdos-884.pdf)
> - [Larsen](https://github.com/Larsen-Daniel/Erdos-884/blob/main/884.pdf)

*Quoted from [FormalConjectures/ErdosProblems/884.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/884.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/884](https://www.erdosproblems.com/884).

The file states 2 research or textbook statements: 2 solved.

## `Erdos884.erdos_884`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/f8a51976fd2e66a52b4928c109fb9ae877a1a507/problems/884/Erdos884.lean](https://github.com/Jayyhk/erdos-lean/blob/f8a51976fd2e66a52b4928c109fb9ae877a1a507/problems/884/Erdos884.lean).

> For a natural number n, let $1 = d_1 < \dotsc < d_{\tau(n)} = n$ denote the divisors of $n$
> in increasing order.
> Does it hold that
> $\sum_{1 \le i < j \le \tau(n)} \frac{1}{d_j - d_i} \ll 1 + \sum_{1 \le i < \tau(n)}
>  \frac{1}{d_{i + 1} - d_i}$
> for $n \to \infty$, i.e.
> $\sum_{1 \le i < j \le \tau(n)} \frac{1}{d_j - d_i} \in O \left( 1 + \sum_{1 \le i < \tau(n)}
>  \frac{1}{d_{i + 1} - d_i} \right)$?
>
> This conjecture has been **disproved**:
> - In September 2025, Terence Tao gave a conditional _negative_ answer assuming the prime tuples
>   conjecture, see `erdos_884_false_of_hardy_littlewood` for this implication.
> - Daniel Larsen subsequently gave an
>   [unconditional disproof](https://github.com/Larsen-Daniel/Erdos-884/blob/main/884.pdf).
>
> *Reference:* [erdosproblems.com/884](https://www.erdosproblems.com/884)

```lean
theorem erdos_884 :
    ¬ Erdos884Prop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/884.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/884.lean#L87).

## `Erdos884.erdos_884_false_of_hardy_littlewood`

Solved: stated here without proof.

> In September 2025, Terence Tao gave a conditional _negative_ answer to Erdős problem 884,
> disproving it under the assumption of the *qualitative Hardy–Littlewood prime tuples
> conjecture*, see Conjecture 1.1 and Theorem 1.1 of
> [Tao25](https://terrytao.wordpress.com/wp-content/uploads/2025/09/erdos-884.pdf).
>
> The qualitative conjecture states that for every admissible tuple $(h_1, \dotsc, h_k)$ of
> integers, i.e. one which avoids at least one residue class modulo $p$ for every prime $p$,
> there are infinitely many natural numbers $n$ such that $n + h_1, \dotsc, n + h_k$ are all
> prime. Unlike the full Hardy–Littlewood conjecture, it does not give an asymptotic for the
> number of such $n$.

```lean
theorem erdos_884_false_of_hardy_littlewood
    (hHL : ∀ H : Finset ℤ, (∀ p : ℕ, p.Prime → ∃ a : ℤ, ∀ h ∈ H, ¬ (p : ℤ) ∣ a + h) →
      {n : ℕ | ∀ h ∈ H, Prime ((n : ℤ) + h)}.Infinite) :
    ¬Erdos884Prop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/884.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/884.lean#L104).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/884.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/884.lean)
- [erdosproblems.com/884](https://www.erdosproblems.com/884)
