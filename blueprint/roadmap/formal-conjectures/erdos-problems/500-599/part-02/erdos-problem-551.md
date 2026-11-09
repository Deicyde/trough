---
declaration: theorem
origin: cited
lean: Erdos551.erdos_551, Erdos551.erdos_551.variants.sufficiently_large
statement: formalized
---

# Erdős Problem 551

> *References:*
> - [erdosproblems.com/551](https://www.erdosproblems.com/551)
> - [BoEr73] Bondy, J. A. and Erdős, P., Ramsey numbers for cycles in graphs. J. Combin. Theory
>   Ser. B (1973), 46-54.
> - [Ni05] Nikiforov, V., The cycle-complete graph Ramsey numbers. Combin. Probab. Comput. (2005),
>   349-370.
> - [KLS21] Keevash, P., Long, E. and Skokan, J., Cycle-complete Ramsey numbers.
>   Int. Math. Res. Not. IMRN (2021), 277-302.

*Quoted from [FormalConjectures/ErdosProblems/551.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/551.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/551](https://www.erdosproblems.com/551).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos551.erdos_551`

Open: stated without proof.

> Prove that
> $$R(C_k,K_n)=(k-1)(n-1)+1$$
> for $k\geq n\geq 3$ (except when $n=k=3$).
>
> Asked by Erdős, Faudree, Rousseau, and Schelp.
> This problem is #18 in Ramsey Theory in the graphs problem collection.

```lean
theorem erdos_551 :
    ∀ (k n : ℕ), 3 ≤ n → n ≤ k → ¬(n = 3 ∧ k = 3) →
      SimpleGraph.graphRamsey (SimpleGraph.cycleGraph k)
        (SimpleGraph.completeGraph (Fin n)) = (k - 1) * (n - 1) + 1
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/551.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/551.lean#L48).

## `Erdos551.erdos_551.variants.sufficiently_large`

Solved: stated here without proof.

> For sufficiently large $n$ and every $k\geq n$, $R(C_k,K_n)=(k-1)(n-1)+1$.
>
> Keevash, Long, and Skokan [KLS21] have proved this identity when
> $k\geq C\frac{\log n}{\log\log n}$ for some constant $C$, thus establishing the conjecture
> for sufficiently large $n$.

```lean
theorem erdos_551.variants.sufficiently_large :
    ∀ᶠ n : ℕ in atTop, ∀ k : ℕ, n ≤ k →
      SimpleGraph.graphRamsey (SimpleGraph.cycleGraph k)
        (SimpleGraph.completeGraph (Fin n)) = (k - 1) * (n - 1) + 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/551.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/551.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/551.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/551.lean)
- [erdosproblems.com/551](https://www.erdosproblems.com/551)
