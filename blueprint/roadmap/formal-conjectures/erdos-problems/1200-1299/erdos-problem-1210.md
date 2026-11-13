---
declaration: theorem
origin: cited
lean: Erdos1210.erdos_1210, Erdos1210.erdos_1210.variants.er80_correction
statement: formalized
---

# Erdős Problem 1210

> *References:*
> - [erdosproblems.com/1210](https://www.erdosproblems.com/1210)
> - [Er77c] Erdős, Paul, Problems and results on combinatorial number theory. III. Number theory day
>   (Proc. Conf., Rockefeller Univ., New York, 1976) (1977), 43-72.
> - [Er80] Erdős, Paul, A survey of problems in combinatorial number theory. Ann. Discrete Math.
>   (1980), 89-115.

*Quoted from [FormalConjectures/ErdosProblems/1210.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1210.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1210](https://www.erdosproblems.com/1210).

The file states 2 research or textbook statements: 2 open.

## `Erdos1210.erdos_1210`

Open: stated without proof.

> Let $A\subseteq [1,n)$ be a set of integers such that $(a,b)=1$ for all distinct $a,b\in A$.
> Is it true that $\sum_{a\in A}\frac{1}{n-a}\leq \sum_{p < n}\frac{1}{p}+O(1)$?

```lean
theorem erdos_1210 :
    ∃ C : ℝ, ∀ n : ℕ, ∀ A : Finset ℕ,
      (∀ a ∈ A, 1 ≤ a ∧ a < n) →
      (∀ a ∈ A, ∀ b ∈ A, a ≠ b → a.Coprime b) →
      ∑ a ∈ A, (1 / ((n : ℝ) - a)) ≤ (∑ p ∈ (range n).filter Prime, (1 / (p : ℝ))) + C
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1210.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1210.lean#L42).

## `Erdos1210.erdos_1210.variants.er80_correction`

Open: stated without proof.

> In [Er80] he claims he "did not state this quite correctly" in [Er77c]. The problem in [Er77c] which
> Erdős is presumably referring to states that if $n < q_1 < \cdots < q_k\leq m$ is the set of primes
> in $(n,m]$ then $\sum \frac{1}{q_i-n} < \sum_{p < m-n}\frac{1}{p}+O(1)$.

```lean
theorem erdos_1210.variants.er80_correction :
    ∃ C : ℝ, ∀ n m : ℕ, n < m →
      ∑ q ∈ (Ioc n m).filter Prime, (1 / ((q : ℝ) - n)) <
      (∑ p ∈ (range (m - n)).filter Prime, (1 / (p : ℝ))) + C
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1210.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1210.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1210.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1210.lean)
- [erdosproblems.com/1210](https://www.erdosproblems.com/1210)
