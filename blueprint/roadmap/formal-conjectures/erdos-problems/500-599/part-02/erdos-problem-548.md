---
declaration: theorem
origin: cited
lean: Erdos548.erdos_548
statement: formalized
---

# Erdős Problem 548

> *References:*
> - [erdosproblems.com/548](https://www.erdosproblems.com/548)
> - [BrDo96] Brandt, Stephan and Dobson, Edward, *The Erdős-Sós conjecture for graphs of girth {$5$}*.
>   Discrete Math. (1996), 411-414.
> - [Er78] Erdős, Paul, *Problems and results in combinatorial analysis and combinatorial number
>   theory*. Proceedings of the Ninth Southeastern Conference on Combinatorics, Graph Theory, and
>   Computing (Florida Atlantic Univ., Boca Raton, Fla., 1978) (1978), 29-40.
> - [ErGa59] Erdős, P. and Gallai, T., *On maximal paths and circuits of graphs*. Acta Math. Acad.
>   Sci. Hungar. (1959), 337-356 (unbound insert).
> - [SaWo97] Saclé, Jean-François and Woźniak, Mariusz, *The Erdős-Sós conjecture for graphs without
>   {$C_4$}*. J. Combin. Theory Ser. B (1997), 367-372.
> - [WLL00] Wang, Min and Li, Guo-jun and Liu, Ai-de, *A result of Erdős-Sós conjecture*. Ars Combin.
>   (2000), 123-127.
> - [YiLi04] Yin, Jian-hua and Li, Jiong-sheng, *The Erdős-Sós conjecture for graphs whose complements
>   contain no {$C_4$}*. Acta Math. Appl. Sin. Engl. Ser. (2004), 397-400.

*Quoted from [FormalConjectures/ErdosProblems/548.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/548.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/548](https://www.erdosproblems.com/548).

The file states 1 research or textbook statement: 1 solved.

## `Erdos548.erdos_548`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/4c355efbf8e90c2572aa8d0c8d6f3b4b43f011f4/problems/548/Erdos548.lean#L1182](https://github.com/Jayyhk/erdos-lean/blob/4c355efbf8e90c2572aa8d0c8d6f3b4b43f011f4/problems/548/Erdos548.lean#L1182).

> Let $n\geq k+1$. Every graph on $n$ vertices with at least $\frac{k-1}{2}n+1$ edges contains every tree on $k+1$ vertices.

```lean
theorem erdos_548 (n k : ℕ) (hk : k + 1 ≤ n) (G : SimpleGraph (Fin n))
    (H : ((k : ℚ) - 1) / 2 * n + 1 ≤ (G.edgeSet.ncard : ℚ))
    (T : SimpleGraph (Fin (k + 1))) (hT : T.IsTree) : T.IsContained G
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/548.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/548.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/548.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/548.lean)
- [erdosproblems.com/548](https://www.erdosproblems.com/548)
