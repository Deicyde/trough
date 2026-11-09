---
declaration: theorem
origin: cited
lean: Erdos34.erdos_34
statement: formalized
---

# Erdős Problem 34

> *References:*
> - [erdosproblems.com/34](https://www.erdosproblems.com/34)
> - [Er77c] Erdős, Paul, *Problems and results on combinatorial number theory. III*. Number theory day
>   (Proc. Conf., Rockefeller Univ., New York, 1976) (1977), 43-72.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [He86] Hegyvári, N., *On consecutive sums in sequences*. Acta Math. Hungar. (1986),
>   193--200.
> - [Ko15] Konieczny, J., *On consecutive sums in permutations*. arXiv:1504.07156 (2015).

*Quoted from [FormalConjectures/ErdosProblems/34.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/34.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/34](https://www.erdosproblems.com/34).

The file states 1 research or textbook statement: 1 solved.

## `Erdos34.erdos_34`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos34.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos34.lean).

> For any permutation $\pi\in S_n$ of $\{1,\ldots,n\}$ let $S(\pi)$ count the number of distinct consecutive sums, that is, sums of the shape $\sum_{u\leq i\leq v}\pi(i)$. Is it true that
>
> $$
> S(\pi) = o(n^2)
> $$
>
> for all $\pi\in S_n$?
>
> Hegyvári [He86] gave a counterexample.

```lean
theorem erdos_34 :
    ¬ ∀ c : ℝ, 0 < c → ∃ N : ℕ, ∀ n ≥ N, ∀ p : Equiv.Perm (Fin n),
      ((consecutiveSums n p).card : ℝ) < c * (n : ℝ) ^ 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/34.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/34.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/34.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/34.lean)
- [erdosproblems.com/34](https://www.erdosproblems.com/34)
