---
declaration: theorem
origin: cited
lean: Erdos20.erdos_20, Erdos20.erdos_20.variants.erdos_rado_bound
statement: formalized
---

# Erdős Problem 20

> *References:*
> * [erdosproblems.com/20](https://www.erdosproblems.com/20)
> * [Wikipedia](https://en.wikipedia.org/wiki/Sunflower_(mathematics))
> * [ErRa60] Erdős, Paul and Rado, Richard. Intersection theorems for systems of sets.
>   J. London Math. Soc. 35 (1960), 85--90.

*Quoted from [FormalConjectures/ErdosProblems/20.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/20.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/20](https://www.erdosproblems.com/20).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 test statement, counted here but not shown.

## `Erdos20.erdos_20`

Open: stated without proof.

> Is it true that $f(n,k) < c_k^n$ for some constant $c_k>0$ and for all $n > 0$?

```lean
theorem erdos_20 : ∃ (c : ℕ → ℕ), ∀ n k, n > 0 → f n k < (c k) ^ n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/20.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/20.lean#L54).

## `Erdos20.erdos_20.variants.erdos_rado_bound`

Solved: stated here; a Lean proof is at [https://github.com/HowieHwong/lean-erdos-proofs/blob/b8b641ba2d00dc4d1fe205a078a4159372672459/Erdos/P20.lean#L202](https://github.com/HowieHwong/lean-erdos-proofs/blob/b8b641ba2d00dc4d1fe205a078a4159372672459/Erdos/P20.lean#L202).

> Erdős and Rado [ErRa60] proved the factorial upper bound for the $k$-sunflower
> threshold: any family of $n$-uniform sets with more than $(k-1)^n \, n!$ members
> contains a $k$-sunflower, hence $f(n,k) \le (k-1)^n \, n! + 1$.

```lean
theorem erdos_20.variants.erdos_rado_bound :
    ∀ n k, n > 0 → 2 ≤ k → f n k ≤ (k - 1) ^ n * n.factorial + 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/20.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/20.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/20.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/20.lean)
- [erdosproblems.com/20](https://www.erdosproblems.com/20)
