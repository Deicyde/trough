---
declaration: theorem
origin: cited
lean: Erdos571.erdos_571
statement: formalized
---

# Erdős Problem 571

> *References:*
> - [erdosproblems.com/571](https://www.erdosproblems.com/571)
> - [Formal Lean proof](https://github.com/Jayyhk/erdos-lean/blob/2f055a777231a73a305b379e993c37f00ed5a66b/problems/571/Erdos571.lean)
> - [BuCo18] Bukh, Boris and Conlon, David, *Rational exponents in extremal graph theory*. J. Eur.
>   Math. Soc. (JEMS) (2018), 1747-1757.
> - [CJL21] Conlon, David and Janzer, Oliver and Lee, Joonkyung, *More on the extremal number of
>   subdivisions*. Combinatorica (2021), 465-494.
> - [CoJa22] Conlon, David and Janzer, Oliver, *Rational exponents near two*. Adv. Comb. (2022), Paper
>   No. 9, 10.
> - [Er78] Erdős, Paul, *Problems and results in combinatorial analysis and combinatorial number
>   theory*. Proceedings of the Ninth Southeastern Conference on Combinatorics, Graph Theory, and
>   Computing (Florida Atlantic Univ., Boca Raton, Fla., 1978) (1978), 29-40.
> - [JJM20] Jiang, Tao and Jiang, Zilin and Ma, Jie, *Negligible obstructions and Turán exponents*.
>   arXiv:2007.02975 (2020).
> - [JMY22] Jiang, Tao and Ma, Jie and Yepremyan, Liana, *On Turán exponents of bipartite graphs*.
>   Combin. Probab. Comput. (2022), 333-344.
> - [JiQi20] Jiang, Tao and Qiu, Yu, *Turán numbers of bipartite subdivisions*. SIAM J. Discrete Math.
>   (2020), 556-570.
> - [JiQi23] Jiang, Tao and Qiu, Yu, *Many Turán exponents via subdivisions*. Combin. Probab. Comput.
>   (2023), 134-150.
> - [KKL21] Kang, Dong Yeap and Kim, Jaehoon and Liu, Hong, *On the rational Turán exponents
>   conjecture*. J. Combin. Theory Ser. B (2021), 149-172.

*Quoted from [FormalConjectures/ErdosProblems/571.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/571.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/571](https://www.erdosproblems.com/571).

The file states 1 research or textbook statement: 1 solved.

## `Erdos571.erdos_571`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/2f055a777231a73a305b379e993c37f00ed5a66b/problems/571/Erdos571.lean](https://github.com/Jayyhk/erdos-lean/blob/2f055a777231a73a305b379e993c37f00ed5a66b/problems/571/Erdos571.lean).

> Show that for any rational $\alpha \in [1,2)$ there exists a bipartite graph $G$ such that
>
> $$\mathrm{ex}(n;G)\asymp n^{\alpha}.$$
>
> The proof constructs balanced rooted models for all rational parameters. Its upper-bound closure replaces old edges by paths
> of arbitrary length, adds two color-class hubs, and commutes with positive rooted powers.

```lean
theorem erdos_571 :
    ∀ α : ℚ, 1 ≤ α → α < 2 →
      ∃ q : ℕ, ∃ G : SimpleGraph (Fin q), G.IsBipartite ∧
        Asymptotics.IsTheta atTop
          (fun n : ℕ => (extremalNumber n G : ℝ))
          (fun n : ℕ => (n : ℝ) ^ (α : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/571.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/571.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/571.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/571.lean)
- [erdosproblems.com/571](https://www.erdosproblems.com/571)
