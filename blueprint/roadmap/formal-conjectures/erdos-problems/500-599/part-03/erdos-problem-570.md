---
declaration: theorem
origin: cited
lean: Erdos570.erdos_570
statement: formalized
---

# Erdős Problem 570

> *References:*
> - [erdosproblems.com/570](https://www.erdosproblems.com/570)
> - [EFRS93] Erdős, P. and Faudree, R. J. and Rousseau, C. C. and Schelp, R. H., Ramsey size linear
>   graphs. Combin. Probab. Comput. (1993), 389-399.
> - [GoKl94] Goddard, W. and Kleitman, D. J., An upper bound for the Ramsey numbers $r(K_3,G)$.
>   Discrete Math. (1994), 177-182.
> - [Si91] Sidorenko, A. F., An upper bound on the Ramsey number $r(K_3,G)$ depending only on
>   the size of the graph $G$. J. Graph Theory (1991), 15-17.
> - [Ja99] Jayawardene, C. J., Ramsey numbers related to small cycles. University of Memphis (1999).
> - [CFMPP26] Cambie, S., Freschi, A., Morawski, P., Petrova, K. and Pokrovskiy, A.,
>   Ramsey number of a cycle versus a graph of a given size. arXiv:2601.10238 (2026).

*Quoted from [FormalConjectures/ErdosProblems/570.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/570.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/570](https://www.erdosproblems.com/570).

The file states 1 research or textbook statement: 1 solved.

## `Erdos570.erdos_570`

Solved: stated here without proof.

> Let $k\geq 3$. Is it true that, if $m$ is sufficiently large, for any graph $H$ on $m$ edges
> without isolated vertices,
>
> $$R(C_k,H) \leq 2m+\left\lfloor\frac{k-1}{2}\right\rfloor?$$
>
> This was proved for even $k$ by Erdős, Faudree, Rousseau, and Schelp [EFRS93]. This was proved
> for $k=3$ independently by Goddard and Kleitman [GoKl94] and Sidorenko [Si91]. This was proved
> for $k=5$ by Jayawardene [Ja99]. Finally it was proved for all odd $k\geq 7$ by Cambie, Freschi,
> Morawski, Petrova, and Pokrovskiy [CFMPP26].
>
> This problem is #35 in Ramsey Theory in the graphs problem collection.

```lean
theorem erdos_570 :
    ∀ (k : ℕ) (hk : 3 ≤ k),
      ∀ᶠ (m : ℕ) in atTop,
        ∀ (W : Type) [Fintype W] (H : SimpleGraph W) [DecidableRel H.Adj],
          (∀ v, 0 < H.degree v) →
          H.edgeSet.ncard = m →
          SimpleGraph.graphRamsey (SimpleGraph.cycleGraph k) H ≤ 2 * m + (k - 1) / 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/570.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/570.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/570.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/570.lean)
- [erdosproblems.com/570](https://www.erdosproblems.com/570)
