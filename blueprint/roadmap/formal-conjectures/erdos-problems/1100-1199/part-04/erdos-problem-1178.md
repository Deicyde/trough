---
declaration: theorem
origin: cited
lean: Erdos1178.erdos_1178
statement: formalized
---

# Erdős Problem 1178

> *References:*
> - [erdosproblems.com/1178](https://www.erdosproblems.com/1178)
> - [BES73] Brown, W. G. and Erdős, P. and S\'os, V. T., Some extremal problems on {$r$}-graphs.
>   (1973), 53--63.
> - [CGLS23] Conlon, David and Gishboliner, Lior and Levanzov, Yevgeny and Shapira, Asaf, A new bound
>   for the {B}rown-{E}rd\H os-S\'os problem. J. Combin. Theory Ser. B (2023), 1--35.
> - [EFR86] Erdős, P. and Frankl, P. and Rödl, V., The asymptotic number of graphs not containing a
>   fixed subgraph and a problem for hypergraphs having no exponent. Graphs Combin. (1986), 113-121.
> - [Er75b] Erdős, Paul, Problems and results in combinatorial number theory. Journ\'{e}es
>   Arithm\'{e}tiques de Bordeaux (Conf., Univ. Bordeaux, Bordeaux, 1974) (1975), 295-310.
> - [RuSz78] Ruzsa, I. Z. and Szemer\'{e}di, E., Triple systems with no six points carrying three
>   triangles. Combinatorics (Proc. Fifth Hungarian Colloq., Keszthely, 1976), Vol. II (1978), 939-945.
> - [SaSe05] Sárk\"ozy, Gábor N. and Selkow, Stanley, An extension of the {R}uzsa-Szemer\'edi theorem
>   . Combinatorica (2005), 77--84.
> - [SoSo17] Solymosi, David and Solymosi, Jozsef, Small cores in 3-uniform hypergraphs. J. Combin.
>   Theory Ser. B (2017), 897--910.

*Quoted from [FormalConjectures/ErdosProblems/1178.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1178.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1178](https://www.erdosproblems.com/1178).

The file states 1 research or textbook statement: 1 open.

## `Erdos1178.erdos_1178`

Open: stated without proof.

> For $r\geq 3$ let $d_r(e)$ be the minimal $d$ such that
>
> $$\mathrm{ex}_r(n,\mathcal{F})=o(n^2),$$
>
> where $\mathcal{F}$ is the family of $r$-uniform hypergraphs on $d$ vertices with $e$ edges. Prove
> that
>
> $$d_r(e)=(r-2)e+3$$
>
> for all $r,e\geq 3$.

```lean
theorem erdos_1178 :
    ∀ r e : ℕ, 3 ≤ r → 3 ≤ e →
    Hypergraph.sparseConfigurationThreshold r e = (((r - 2) * e + 3 : ℕ) : ℕ∞)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1178.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1178.lean#L56).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1178.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1178.lean)
- [erdosproblems.com/1178](https://www.erdosproblems.com/1178)
