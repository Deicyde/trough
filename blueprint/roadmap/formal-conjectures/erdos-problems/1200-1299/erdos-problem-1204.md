---
declaration: theorem
origin: cited
lean: Erdos1204.erdos_1204.parts.i, Erdos1204.erdos_1204.parts.ii, Erdos1204.erdos_1204.variants.A_lower, Erdos1204.erdos_1204.variants.A_upper, Erdos1204.erdos_1204.variants.B_upper
statement: formalized
---

# Erdős Problem 1204

> *References:*
> - [erdosproblems.com/1204](https://www.erdosproblems.com/1204)
> - [El65] Elliott, P. D. T. A., *On sequences of integers*. Quart. J. Math. Oxford Ser. (2) 16
>   (1965), 35-45.
> - [Er80] Erdős, P., *A survey of problems in combinatorial number theory*. Ann. Discrete Math. 6
>   (1980), 89-115.
> - [Po14c] Polymath, D. H. J., *Variants of the Selberg sieve, and bounded intervals containing
>   many primes*. Res. Math. Sci. 1 (2014), Art. 12.
>   [arXiv:1407.4897](https://arxiv.org/abs/1407.4897)

*Quoted from [FormalConjectures/ErdosProblems/1204.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1204.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1204](https://www.erdosproblems.com/1204).

The file states 5 research or textbook statements: 2 open and 3 solved. It also has 1 API statement, counted here but not shown.

## `Erdos1204.erdos_1204.parts.i`

Open: stated without proof.

> We call a sequence of integers $0\leq a_1\lt \cdots \lt a_k$ admissible if it is missing at least one
> congruence class modulo every prime $p$. Let $A(k)=\min a_k$. Estimate $A(k)$ - in particular, is
> it true that
>
> $$A(k)\sim k\log k?$$

```lean
theorem erdos_1204.parts.i :
    (fun k : ℕ ↦ (A k : ℝ)) ~[atTop] fun k : ℕ ↦ (k : ℝ) * Real.log k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1204.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1204.lean#L71).

## `Erdos1204.erdos_1204.parts.ii`

Open: stated without proof.

> We call a sequence of integers $0\leq a_1\lt \cdots \lt a_k$ admissible if it is missing at least one
> congruence class modulo every prime $p$. Estimate
>
> $$B(k)=\min \frac{a_1+\cdots+a_k}{k}.$$
>
> We read "estimate" as finding an asymptotic formula, since $B(k)\asymp k\log k$ already follows
> from the known bounds for $A(k)$ (as $a_j\geq A(j)$).

```lean
theorem erdos_1204.parts.ii : B ~[atTop] erdos_1204.parts.ii.answer
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1204.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1204.lean#L86).

## `Erdos1204.erdos_1204.variants.A_lower`

Solved: stated here without proof.

> It is known that $(1/2+o(1))k\log k \leq A(k)$. This lower bound is originally due to Elliott
> [El65], but was rediscovered by the Polymath project on bounded gaps between primes [Po14c].

```lean
theorem erdos_1204.variants.A_lower :
    ∀ ε > (0 : ℝ), ∀ᶠ k : ℕ in atTop, (1 / 2 - ε) * k * Real.log k ≤ (A k : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1204.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1204.lean#L94).

## `Erdos1204.erdos_1204.variants.A_upper`

Solved: stated here without proof.

> It is known that $A(k)\leq (1+o(1))k\log k$, by taking the $k$ smallest primes $>k$.

```lean
theorem erdos_1204.variants.A_upper :
    ∀ ε > (0 : ℝ), ∀ᶠ k : ℕ in atTop, (A k : ℝ) ≤ (1 + ε) * k * Real.log k
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1204.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1204.lean#L102).

## `Erdos1204.erdos_1204.variants.B_upper`

Solved: stated here without proof.

> Taking the first $k$ primes which are $>k$ implies $B(k)\leq (1/2+o(1))k\log k$.

```lean
theorem erdos_1204.variants.B_upper :
    ∀ ε > (0 : ℝ), ∀ᶠ k : ℕ in atTop, B k ≤ (1 / 2 + ε) * k * Real.log k
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1204.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1204.lean#L110).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1204.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1204.lean)
- [erdosproblems.com/1204](https://www.erdosproblems.com/1204)
