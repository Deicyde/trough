---
declaration: theorem
origin: cited
lean: Erdos883.erdos_883.parts.i, Erdos883.erdos_883.parts.ii
statement: formalized
---

# Erdős Problem 883

> *References:*
> - [erdosproblems.com/883](https://www.erdosproblems.com/883)
> - [ErSa97] Erdős, P. and Sárközy, G. N., On cycles in the coprime graph of integers.
>   Electron. J. Combin. (1997), Research Paper 8.
> - [Sa99] Sárközy, G. N., Complete tripartite subgraphs in the coprime graph of integers.
>   Discrete Math. (1999), 227-238.

*Quoted from [FormalConjectures/ErdosProblems/883.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/883.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/883](https://www.erdosproblems.com/883).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos883.erdos_883.parts.i`

Open: stated without proof.

> For $A\subseteq \{1,\ldots,n\}$ let $G(A)$ be the graph with vertex set $A$, where two
> integers are joined by an edge if they are coprime.
>
> Is it true that if
>
> $$|A| > \lfloor n/2 \rfloor + \lfloor n/3 \rfloor - \lfloor n/6 \rfloor$$
>
> then $G(A)$ contains all odd cycles of length $\leq n/3 + 1$?
>
> A problem of Erdős and Sárközy [ErSa97].

```lean
theorem erdos_883.parts.i :
    ∀ (n : ℕ) (A : Finset ℕ),
      A ⊆ Finset.Icc 1 n →
      n / 2 + n / 3 - n / 6 < A.card →
      ∀ l : ℕ, Odd l → 3 ≤ l → l ≤ n / 3 + 1 →
        l ∈ (coprimeGraph.induce (A : Set ℕ)).oddCycleLengths
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/883.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/883.lean#L54).

## `Erdos883.erdos_883.parts.ii`

Solved: stated here without proof.

> Is it true that, for every $\ell\geq 1$, if $n$ is sufficiently large and
>
> $$|A| > \lfloor n/2\rfloor + \lfloor n/3\rfloor - \lfloor n/6\rfloor$$
>
> then $G(A)$ must contain a complete $(1,\ell,\ell)$ tripartite graph on $2\ell+1$ vertices?
>
> The second question was solved by Sárközy [Sa99], who proved this with
> $\ell \gg \log n/\log\log n$.

```lean
theorem erdos_883.parts.ii :
    ∀ l : ℕ, 1 ≤ l → ∀ᶠ n : ℕ in atTop, ∀ A : Finset ℕ,
      A ⊆ Finset.Icc 1 n →
      n / 2 + n / 3 - n / 6 < A.card →
      (SimpleGraph.completeMultipartiteGraph (fun i : Fin 3 ↦ Fin (![1, l, l] i))).IsContained
        (coprimeGraph.induce (A : Set ℕ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/883.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/883.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/883.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/883.lean)
- [erdosproblems.com/883](https://www.erdosproblems.com/883)
