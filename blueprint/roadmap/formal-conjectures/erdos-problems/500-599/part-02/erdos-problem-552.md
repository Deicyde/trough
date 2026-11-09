---
declaration: theorem
origin: cited
lean: Erdos552.erdos_552.parts.i, Erdos552.erdos_552.parts.ii, Erdos552.erdos_552.variants.succ_le_add_two
statement: formalized
---

# Erdős Problem 552

> *References:*
> - [erdosproblems.com/552](https://www.erdosproblems.com/552)
> - [BEFRS89] Burr, S. and Erdős, P. and Faudree, R. J. and Rousseau, C. C. and Schelp, R. H., Some
>   complete bipartite graph-tree Ramsey numbers. Graph theory in memory of G. A. Dirac (Sandbjerg,
>   1985) (1989), 79-89.
> - [Ch97] Chen, G., *A result on $C_4$-star Ramsey numbers*. Discrete Mathematics **163** (1997),
>   243-246.

*Quoted from [FormalConjectures/ErdosProblems/552.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/552.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/552](https://www.erdosproblems.com/552).

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Erdos552.erdos_552.parts.i`

Open: stated without proof.

> Determine the Ramsey number
>
> $$R(C_4, S_n),$$
>
> where $S_n=K_{1,n}$ is the star on $n+1$ vertices.
>
> A problem of Burr, Erdős, Faudree, Rousseau, and Schelp [BEFRS89].
>
> This problem is #19 in Ramsey Theory in the graphs problem collection.

```lean
theorem erdos_552.parts.i :
    ∀ (n : ℕ),
      SimpleGraph.graphRamsey (SimpleGraph.cycleGraph 4)
        (completeBipartiteGraph (Fin 1) (Fin n)) =
        erdos_552.parts.i.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/552.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/552.lean#L48).

## `Erdos552.erdos_552.parts.ii`

Open: stated without proof.

> In particular, is it true that, for any $c > 0$, there are infinitely many $n$ such that
>
> $$R(C_4, S_n) \leq n + \sqrt{n} - c?$$

```lean
theorem erdos_552.parts.ii :
    ∀ (c : ℝ), 0 < c →
      Set.Infinite {n : ℕ |
        (SimpleGraph.graphRamsey (SimpleGraph.cycleGraph 4)
          (completeBipartiteGraph (Fin 1) (Fin n)) : ℝ) ≤ (n : ℝ) + Real.sqrt n - c}
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/552.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/552.lean#L60).

## `Erdos552.erdos_552.variants.succ_le_add_two`

Solved: stated here; a Lean proof is at [https://github.com/agnt-gg/erdos-lean/blob/8e5972f4e6787049b168e5350b1a2badc9eb8bcd/Erdos/Erdos552.lean#L292](https://github.com/agnt-gg/erdos-lean/blob/8e5972f4e6787049b168e5350b1a2badc9eb8bcd/Erdos/Erdos552.lean#L292).

> Burr, Erdős, Faudree, Rousseau and Schelp also asked whether $f(n + 1) \le f(n) + 2$ for all $n$,
> where $f(n) = R(C_4, S_n)$. Chen [Ch97] proved this for $n \ge 1$. It fails for $n = 0$, since
> $R(C_4, S_1) = 4$ and $R(C_4, S_0) = 1$.

```lean
theorem erdos_552.variants.succ_le_add_two (n : ℕ) (hn : 1 ≤ n) :
    SimpleGraph.graphRamsey (SimpleGraph.cycleGraph 4)
        (completeBipartiteGraph (Fin 1) (Fin (n + 1))) ≤
      SimpleGraph.graphRamsey (SimpleGraph.cycleGraph 4)
        (completeBipartiteGraph (Fin 1) (Fin n)) + 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/552.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/552.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/552.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/552.lean)
- [erdosproblems.com/552](https://www.erdosproblems.com/552)
