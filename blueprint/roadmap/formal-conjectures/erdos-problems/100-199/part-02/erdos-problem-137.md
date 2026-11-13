---
declaration: theorem
origin: cited
lean: Erdos137.erdos_137, Erdos137.erdos_137.variants.perfect_power, Erdos137.erdos_137.variants.multiple_powerful_factors
statement: formalized
---

# Erdős Problem 137

> *References:*
> - [erdosproblems.com/137](https://www.erdosproblems.com/137)

*Quoted from [FormalConjectures/ErdosProblems/137.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/137.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/137](https://www.erdosproblems.com/137).

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Erdos137.erdos_137`

Open: stated without proof.

> We say that $N$ is powerful if whenever $p\mid N$ we also have $p^2\mid N$.
>
> Let $k\geq 3$. Can the product of any $k$ consecutive positive integers ever be powerful?

```lean
theorem erdos_137 : ∃ k ≥ 3, ∃ n, (∏ x ∈ Finset.Ioc n (n + k), x).Powerful
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/137.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/137.lean#L37).

## `Erdos137.erdos_137.variants.perfect_power`

Solved: stated here without proof.

> Let $k\geq 2$. Erdős and Selfridge [ES75] proved that the product of any $k$ consecutive
> integers $N$ cannot be a perfect power.
>
> [ES75] P. Erdös, J. L. Selfridge, "The product of consecutive integers is never a power",
>   Illinois J. Math. 19(2): 292-301, 1975

```lean
theorem erdos_137.variants.perfect_power (k : ℕ) (hk : k ≥ 2) (n : ℕ) (x l : ℕ) (hl : 2 ≤ l) :
    (∏ x ∈ Finset.Ioc n (n + k), x) ≠ x ^ l
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/137.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/137.lean#L48).

## `Erdos137.erdos_137.variants.multiple_powerful_factors`

Open: stated without proof.

> Erdős [Er82c] conjectures that, if $k$ is fixed, then for all $n$ sufficiently large and all
> positive integers $m$, there must be at least $k$ distinct primes $p$ such that
> $p\mid m(m+1)\cdots (m+n)$ and yet $p^2$ does not divide the right hand side.
>
> [Er82c] Erdős, Paul, "Miscellaneous problems in number theory". Congr. Numer. (1982), 25-45.,

```lean
theorem erdos_137.variants.multiple_powerful_factors (k : ℕ) : ∀ᶠ n in Filter.atTop,
    ∀ (m : ℕ) (hm : 0 < m),
    letI N := ∏ x ∈ Finset.Ioc m (m + n), x
    ∃ P : Finset ℕ, P.card = k ∧ ∀ p ∈ P, p.Prime ∧
    p ∣ N ∧ ¬ p ^ 2 ∣ N
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/137.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/137.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/137.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/137.lean)
- [erdosproblems.com/137](https://www.erdosproblems.com/137)
