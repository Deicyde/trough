---
declaration: theorem
origin: cited
lean: Erdos808.erdos_808, Erdos808.erdos_808.variants.positive, Erdos808.erdos_808.variants.ars_lower_bound
statement: formalized
---

# Erdős Problem 808

> *References:*
> - [erdosproblems.com/808](https://www.erdosproblems.com/808)
> - [ErSz83] Erdős, P. and Szemerédi, E., *On sums and products of integers*. Studies in pure
>   mathematics (1983), 213-218. [PDF](https://www.renyi.hu/~p_erdos/1983-18.pdf)
> - [ARS20] Alon, Noga and Ruzsa, Imre and Solymosi, József, *Sums, products and ratios along the
>   edges of a graph*. Publ. Mat. (2020), 143-155.
>   [arXiv:1802.06405](https://arxiv.org/abs/1802.06405)

*Quoted from [FormalConjectures/ErdosProblems/808.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/808.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/808](https://www.erdosproblems.com/808).

The file states 3 research or textbook statements: 3 solved. It also has 3 API statements, counted here but not shown.

## `Erdos808.erdos_808`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos808.lean#L1746](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos808.lean#L1746).

> Let $c,\epsilon>0$ and $n$ be sufficiently large. If $A\subset \mathbb{N}$ has $\lvert A\rvert=n$
> and $G$ is any graph on $A$ with at least $n^{1+c}$ edges then
>
> $$\max(\lvert A+_GA\rvert,\lvert A\cdot_G A\rvert) \geq \lvert A\rvert^{1+c-\epsilon},$$
>
> where
>
> $$A+_GA = \{ a+b : (a,b)\in G\}$$
>
> and similarly for $A\cdot_GA$.
>
> This strong conjecture of Erdős and Szemerédi [ErSz83] strengthens Erdős Problem 52
> (`Erdos52.erdos_52`, the case of the complete graph). It was disproved by Alon, Ruzsa, and
> Solymosi [ARS20, Theorem 3]: for arbitrarily large $m$ there are a set of integers $A$ with
> $\lvert A\rvert=m$ and a graph on $A$ with $\gg m^{5/3}/(\log m)^{1/3}$ edges such that
> $\lvert A+_GA\rvert+\lvert A\cdot_GA\rvert \ll (m\log m)^{4/3}$. The statement below is the
> negation of the conjecture.
>
> A set $A$ with a graph on it is given by a finite type `V`, a graph `G` on `V` and an injection
> `a : V ↪ ℕ` (so $A$ is the image of `a` and $n$ is `Fintype.card V`). Here `ℕ` contains $0$; see
> `erdos_808.variants.positive` for positive integers.

```lean
theorem erdos_808 :
    ¬ ∀ c : ℝ, 0 < c → ∀ ε : ℝ, 0 < ε →
      ∃ n₀ : ℕ, ∀ (V : Type) [Fintype V] (a : V ↪ ℕ) (G : SimpleGraph V) [DecidableRel G.Adj],
        n₀ ≤ Fintype.card V →
        (Fintype.card V : ℝ) ^ (1 + c) ≤ (G.edgeFinset.card : ℝ) →
        (Fintype.card V : ℝ) ^ (1 + c - ε) ≤
          max ((edgeSums a G).card : ℝ) ((edgeProducts a G).card : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/808.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/808.lean#L109).

## `Erdos808.erdos_808.variants.positive`

Solved: stated here without proof.

> The conjecture already fails for positive integers: the set of integers constructed in
> [ARS20, Theorem 3] consists of positive integers. This is `erdos_808` with the extra hypothesis
> `∀ v, 0 < a v`, so it implies `erdos_808`.

```lean
theorem erdos_808.variants.positive :
    ¬ ∀ c : ℝ, 0 < c → ∀ ε : ℝ, 0 < ε →
      ∃ n₀ : ℕ, ∀ (V : Type) [Fintype V] (a : V ↪ ℕ), (∀ v, 0 < a v) →
        ∀ (G : SimpleGraph V) [DecidableRel G.Adj],
          n₀ ≤ Fintype.card V →
          (Fintype.card V : ℝ) ^ (1 + c) ≤ (G.edgeFinset.card : ℝ) →
          (Fintype.card V : ℝ) ^ (1 + c - ε) ≤
            max ((edgeSums a G).card : ℝ) ((edgeProducts a G).card : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/808.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/808.lean#L124).

## `Erdos808.erdos_808.variants.ars_lower_bound`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos808.lean#L833](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos808.lean#L833).

> Alon, Ruzsa, and Solymosi do prove, however, that if $A$ has size $n$ and $G$ has $m$ edges then
>
> $$\max(\lvert A+_GA\rvert,\lvert A\cdot_G A\rvert) \gg m^{3/2}n^{-7/4}.$$
>
> This is [ARS20, Theorem 10]. It holds for any $n$-element set of real numbers, and [ARS20]
> state it for $\lvert A+_GA\rvert+\lvert A\cdot_GA\rvert$, which is within a factor $2$ of the
> maximum. It is written in multiplied-out form, so that $n=0$ needs no division.

```lean
theorem erdos_808.variants.ars_lower_bound :
    ∃ K : ℝ, 0 < K ∧
      ∀ (V : Type) [Fintype V] (a : V ↪ ℝ) (G : SimpleGraph V) [DecidableRel G.Adj],
        (G.edgeFinset.card : ℝ) ^ ((3 : ℝ) / 2) ≤
          K * (Fintype.card V : ℝ) ^ ((7 : ℝ) / 4) *
            max ((edgeSums a G).card : ℝ) ((edgeProducts a G).card : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/808.lean, line 145](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/808.lean#L145).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/808.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/808.lean)
- [erdosproblems.com/808](https://www.erdosproblems.com/808)
