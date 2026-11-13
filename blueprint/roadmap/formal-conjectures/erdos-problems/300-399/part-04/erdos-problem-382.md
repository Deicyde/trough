---
declaration: theorem
origin: cited
lean: Erdos382.lt_two_mul_of_largestPrimeRepeated, Erdos382.erdos_382.parts.i, Erdos382.erdos_382.parts.ii, Erdos382.erdos_382.variants.ramachandra
statement: formalized
---

# Erdős Problem 382

> *References:*
> - [erdosproblems.com/382](https://www.erdosproblems.com/382)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).

*Quoted from [FormalConjectures/ErdosProblems/382.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/382.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/382](https://www.erdosproblems.com/382).

The file states 4 research or textbook statements: 2 open, 1 solved and 1 textbook result. It also has 1 test statement, counted here but not shown.

## `Erdos382.lt_two_mul_of_largestPrimeRepeated`

Textbook result, proved here.

> If the condition holds, then $v < 2u$.
>
> Otherwise $2u \leq v$, and by Bertrand's postulate there is a prime $q$ with $v/2 < q \leq v$, so
> $u \leq q \leq v$. The largest prime $p$ of the product satisfies $p \geq q > v/2$. Hence $p$
> divides exactly one factor $m \in [u, v]$, namely $m = p$, and $p$ appears with exponent $1$.

```lean
theorem lt_two_mul_of_largestPrimeRepeated {u v : ℕ} (h : LargestPrimeRepeated u v) :
    v < 2 * u
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/382.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/382.lean#L59).

## `Erdos382.erdos_382.parts.i`

Open: stated without proof.

> Let $u \leq v$ be such that the largest prime dividing $\prod_{u \leq m \leq v} m$ appears with
> exponent at least $2$. Is it true that $v - u = v^{o(1)}$?
>
> We read this as: for every $\epsilon > 0$, every such pair with $v$ large enough satisfies
> $v - u \leq v^{\epsilon}$. Cambie observed that this question reduces to old conjectures on gaps
> between primes; for example, it follows from Cramér's conjecture. See also Erdős Problems 380 and
> 383.

```lean
theorem erdos_382.parts.i :
    ∀ ε > (0 : ℝ), ∀ᶠ v : ℕ in atTop, ∀ u : ℕ, LargestPrimeRepeated u v →
      ((v - u : ℕ) : ℝ) ≤ (v : ℝ) ^ ε
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/382.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/382.lean#L104).

## `Erdos382.erdos_382.parts.ii`

Open: stated without proof.

> Let $u \leq v$ be such that the largest prime dividing $\prod_{u \leq m \leq v} m$ appears with
> exponent at least $2$. Can $v - u$ be arbitrarily large?
>
> That is, for every $k$, is there such a pair with $v - u \geq k$? Cambie gives a heuristic that
> suggests the answer is yes.

```lean
theorem erdos_382.parts.ii :
    ∀ k : ℕ, ∃ u v : ℕ, LargestPrimeRepeated u v ∧ k ≤ v - u
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/382.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/382.lean#L117).

## `Erdos382.erdos_382.variants.ramachandra`

Solved: stated here without proof.

> Erdős and Graham [ErGr80] report that it follows from results of Ramachandra that
> $v - u \leq v^{1/2+o(1)}$ for every pair $u \leq v$ as in `Erdos382.erdos_382.parts.i`.
>
> That is, for every $\epsilon > 0$, every such pair with $v$ large enough satisfies
> $v - u \leq v^{1/2+\epsilon}$.

```lean
theorem erdos_382.variants.ramachandra :
    ∀ ε > (0 : ℝ), ∀ᶠ v : ℕ in atTop, ∀ u : ℕ, LargestPrimeRepeated u v →
      ((v - u : ℕ) : ℝ) ≤ (v : ℝ) ^ ((1 : ℝ) / 2 + ε)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/382.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/382.lean#L129).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/382.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/382.lean)
- [erdosproblems.com/382](https://www.erdosproblems.com/382)
