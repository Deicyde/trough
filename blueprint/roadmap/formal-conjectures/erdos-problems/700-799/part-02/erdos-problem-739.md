---
declaration: theorem
origin: cited
lean: Erdos739.erdos_739, Erdos739.erdos_739.variants.aleph_zero, Erdos739.erdos_739.variants.induced, Erdos739.erdos_739.variants.gch
statement: formalized
---

# Erdős Problem 739

> *References:*
> - [erdosproblems.com/739](https://www.erdosproblems.com/739)
> - [dBE51] de Bruijn, N. G. and Erdős, P., *A colour problem for infinite graphs and a problem in
>   the theory of relations*. Indag. Math. (1951), 369-373.
> - [Ga73] Galvin, F., *Chromatic numbers of subgraphs*. Period. Math. Hungar. (1973), 117-119.
> - [Ko88b] Komjáth, Péter, *Consistency results on infinite graphs*. Israel J. Math. (1988),
>   285-294.
> - [Sh90] Shelah, Saharon, *Incompactness for chromatic numbers of graphs*. A tribute to Paul Erdős
>   (1990), 361-371.

*Quoted from [FormalConjectures/ErdosProblems/739.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/739.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/739](https://www.erdosproblems.com/739).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos739.erdos_739`

Open: stated without proof.

> Let $\mathfrak{m}$ be an infinite cardinal and $G$ be a graph with chromatic number $\mathfrak{m}$.
> Is it true that, for every infinite cardinal $\mathfrak{n}< \mathfrak{m}$, there exists a subgraph
> of $G$ with chromatic number $\mathfrak{n}$?
>
> A question of Galvin [Ga73]. Komjáth [Ko88b] proved it is consistent that
> $2^{\aleph_0}=2^{\aleph_1}=2^{\aleph_2}=\aleph_3$ and that there exist graphs which fail this
> property (with $\mathfrak{m}=\aleph_2$ and $\mathfrak{n}=\aleph_1$), so the statement below is
> not provable in ZFC (if ZFC is consistent). Shelah [Sh90] proved that, assuming the axiom of
> constructibility, the answer is yes with $\mathfrak{m}=\aleph_2$ and $\mathfrak{n}=\aleph_1$. It
> remains open whether the answer is yes assuming the Generalized Continuum Hypothesis (see
> `erdos_739.variants.gch`), so the statement is not known to be refutable either. Consistency
> results about models of ZFC are not directly formalizable inside Lean's fixed model, so only the
> question is recorded here.
>
> The subgraph need not be induced (see `erdos_739.variants.induced`). The hypothesis that
> $\mathfrak{m}$ is infinite follows from $\aleph_0 \le \mathfrak{n} < \mathfrak{m}$.

```lean
theorem erdos_739 :
    ∀ (V : Type u) (G : SimpleGraph V) (n : Cardinal.{u}),
      ℵ₀ ≤ n → n < G.chromaticCardinal →
        ∃ H : G.Subgraph, H.coe.chromaticCardinal = n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/739.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/739.lean#L61).

## `Erdos739.erdos_739.variants.aleph_zero`

Solved: stated here without proof.

> Every graph with chromatic number $\mathfrak{m}>\aleph_0$ has a subgraph with chromatic number
> $\aleph_0$. This is the case $\mathfrak{n}=\aleph_0$ of the question and follows from the
> de Bruijn–Erdős theorem [dBE51]. The source credits Galvin [Ga73] with the case
> $\mathfrak{m}=\aleph_0$, which has no infinite $\mathfrak{n}\lt \mathfrak{m}$; it is read here as
> $\mathfrak{n}=\aleph_0$.

```lean
theorem erdos_739.variants.aleph_zero :
    ∀ (V : Type u) (G : SimpleGraph V), ℵ₀ < G.chromaticCardinal →
      ∃ H : G.Subgraph, H.coe.chromaticCardinal = ℵ₀
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/739.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/739.lean#L75).

## `Erdos739.erdos_739.variants.induced`

Solved: stated here without proof.

> Galvin [Ga73] proved that the stronger version of `erdos_739`, in which the subgraph is induced,
> implies $2^{\mathfrak{k}}<2^{\mathfrak{n}}$ for all cardinals $\mathfrak{k}\lt \mathfrak{n}$.

```lean
theorem erdos_739.variants.induced :
    (∀ (V : Type u) (G : SimpleGraph V) (n : Cardinal.{u}),
      ℵ₀ ≤ n → n < G.chromaticCardinal →
        ∃ s : Set V, (G.induce s).chromaticCardinal = n) →
    ∀ κ μ : Cardinal.{u}, κ < μ → (2 : Cardinal.{u}) ^ κ < 2 ^ μ
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/739.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/739.lean#L85).

## `Erdos739.erdos_739.variants.gch`

Open: stated without proof.

> It remains open whether the answer to `erdos_739` is yes assuming the Generalized Continuum
> Hypothesis, stated as $2^{\mathfrak{c}} = \mathfrak{c}^+$ for every infinite cardinal
> $\mathfrak{c}$.

```lean
theorem erdos_739.variants.gch :
    (∀ c : Cardinal.{u}, ℵ₀ ≤ c → 2 ^ c = Order.succ c) →
    ∀ (V : Type u) (G : SimpleGraph V) (n : Cardinal.{u}),
      ℵ₀ ≤ n → n < G.chromaticCardinal →
        ∃ H : G.Subgraph, H.coe.chromaticCardinal = n
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/739.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/739.lean#L98).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/739.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/739.lean)
- [erdosproblems.com/739](https://www.erdosproblems.com/739)
