---
declaration: theorem
origin: cited
lean: Erdos582.erdos_582
statement: formalized
---

# Erdős Problem 582

> *References:*
> - [erdosproblems.com/582](https://www.erdosproblems.com/582)
> - [Er75b] Erdős, Paul, *Problems and results in combinatorial number theory*. Journées Arithmétiques
>   de Bordeaux (Conf., Univ. Bordeaux, Bordeaux, 1974) (1975), 295-310.
> - [Er69b] Erdős, P., *Problems and results in chromatic graph theory*. Proof Techniques in Graph
>   Theory (Proc. Second Ann Arbor Graph Theory Conf., Ann Arbor, Mich., 1968) (1969), 27-35.
> - [Er75d] Erdős, Paul, *Problems and results on finite and infinite graphs*. Recent advances in
>   graph theory (Proc. Second Czechoslovak Sympos., Prague, 1974) (1975), 183-192. (loose errata).
> - [FrRo86] Frankl, P. and Rödl, V., *Large triangle-free subgraphs in graphs without {$K_4$}*.
>   Graphs Combin. (1986), 135-144.
> - [Sp88] Spencer, Joel, *Three hundred million points suffice*. J. Combin. Theory Ser. A (1988),
>   210-217.
> - [Lu07] Lu, Linyuan, *Explicit construction of small Folkman graphs*. SIAM J. Discrete Math.
>   (2007), 1053-1060.
> - [DuRo08] Dudek, Andrzej and Rödl, Vojtěch, *On the Folkman number {$f(2,3,4)$}*. Experiment.
>   Math. (2008), 63-67.
> - [RaXu07] Radziszowski, Stanisław P. and Xu, Xiaodong, *On the most wanted Folkman graph*.
>   Geombinatorics (2007), 367-381.
> - [BiNe20] Bikov, Aleksandar and Nenov, Nedyalko, *On the independence number of
>   $(3,3)$-Ramsey graphs and the Folkman number $F_e(3,3;4)$*. Australas. J. Combin.
>   (2020), 35-50.
> - [ErHa67] Erdős, P. and Hajnal, A., *Research Problem 2.5*. J. Comb. Theory (1967).
> - [Fo70] Folkman, Jon, *Graphs with monochromatic complete subgraphs in every edge coloring*.
>   SIAM J. Appl. Math. (1970), 19-24.
> - [LRX14] Lange, Alexander R. and Radziszowski, Stanisław P. and Xu, Xiaodong, *Use of MAX-CUT
>   for Ramsey arrowing of triangles*. J. Combin. Math. Combin. Comput. (2014), 61-71.

*Quoted from [FormalConjectures/ErdosProblems/582.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/582.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/582](https://www.erdosproblems.com/582).

The file states 1 research or textbook statement: 1 solved.

## `Erdos582.erdos_582`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos582.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos582.lean).

> Does there exist a graph $G$ which contains no $K_4$, and yet any $2$-colouring of the edges
> produces a monochromatic $K_3$?
>
> Erdős and Hajnal [ErHa67] first asked for the existence of any such graph. Existence was proved
> by Folkman [Fo70], but with very poor quantitative bounds. (As a result these quantities are
> often called Folkman numbers.) The current best bounds on the minimal number of vertices $N$ of
> such a graph are $21 \leq N \leq 786$, where the lower bound is due to Bikov and Nenov [BiNe20]
> and the upper bound is due to Lange, Radziszowski, and Xu [LRX14].

```lean
theorem erdos_582 :
    ∃ (V : Type*) (_ : Fintype V) (G : SimpleGraph V),
      G.CliqueFree 4 ∧ EdgeRamseyTriangle G
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/582.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/582.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/582.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/582.lean)
- [erdosproblems.com/582](https://www.erdosproblems.com/582)
