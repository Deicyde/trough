---
declaration: theorem
origin: cited
lean: Erdos547.erdos_547, Erdos547.erdos_547.variants.sufficiently_large
statement: formalized
---

# Erdős Problem 547

> *References:*
> - [erdosproblems.com/547](https://www.erdosproblems.com/547)
> - [Bu74] Burr, S. A., Generalized Ramsey theory for graphs—a survey. Graphs and combinatorics
>   (Proc. Capital Conf., George Washington Univ., Washington, D.C., 1973) (1974), 52-75.
> - [Zh11] Zhao, Y., Proof of the $(n/2-n/2-n/2)$ conjecture for large $n$.
>   Electron. J. Combin. (2011), Paper 27, 61.

*Quoted from [FormalConjectures/ErdosProblems/547.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/547.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/547](https://www.erdosproblems.com/547).

The file states 2 research or textbook statements: 2 solved.

## `Erdos547.erdos_547`

Solved: stated here; a Lean proof is at [https://github.com/zhangjun725/erdos557/blob/c4e0ab13027f8bb50defade11cf8a53c7b8b0ba9/Erdos557/Erdos547.lean#L84](https://github.com/zhangjun725/erdos557/blob/c4e0ab13027f8bb50defade11cf8a53c7b8b0ba9/Erdos557/Erdos547.lean#L84).

> If $T$ is a tree on $n$ vertices then
>
> $$R(T) \leq 2n-2.$$
>
> This problem is #14 in Ramsey Theory in the graphs problem collection.
>
> Solved: the bound follows from the Erdős–Sós theorem (Erdős problem 548) by the pigeonhole
> principle, as noted on the problem page.

```lean
theorem erdos_547 :
    ∀ (n : ℕ) (hn : 2 ≤ n) (T : SimpleGraph (Fin n)),
      T.IsTree → SimpleGraph.diagonalGraphRamsey T ≤ 2 * n - 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/547.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/547.lean#L49).

## `Erdos547.erdos_547.variants.sufficiently_large`

Solved: stated here without proof.

> For sufficiently large $n$, every tree $T$ on $n$ vertices satisfies $R(T)\leq 2n-2$.
> Proved by Zhao [Zh11].

```lean
theorem erdos_547.variants.sufficiently_large :
    ∀ᶠ n : ℕ in atTop, ∀ T : SimpleGraph (Fin n),
      T.IsTree → SimpleGraph.diagonalGraphRamsey T ≤ 2 * n - 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/547.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/547.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/547.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/547.lean)
- [erdosproblems.com/547](https://www.erdosproblems.com/547)
