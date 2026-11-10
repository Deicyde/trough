---
declaration: theorem
origin: cited
lean: Erdos22.erdos_22, Erdos22.erdos_22.variants.szemeredi_upper, Erdos22.erdos_22.variants.bollobas_erdos_lower, Erdos22.erdos_22.variants.fox_loh_zhao
statement: formalized
---

# Erdős Problem 22

> The central problem of Ramsey–Turán theory: writing $\mathrm{rt}(n; k, \ell)$ for the maximum
> number of edges of a $K_k$-free graph on $n$ vertices whose largest independent set has size
> less than $\ell$, is it true that for every $\epsilon > 0$ and all sufficiently large $n$
>
> $$\mathrm{rt}(n; 4, \epsilon n) \geq n^2/8?$$
>
> Conjectured by Bollobás and Erdős [BoEr76], who constructed such a graph with
> $(1/8 + o(1))n^2$ edges. Together with the matching upper bound
> $\mathrm{rt}(n; 4, \epsilon n) \leq (1/8 + o(1))n^2$ of Szemerédi [Sz72], this determines the
> Ramsey–Turán density of $K_4$ to be $1/8$. The conjecture as stated was proved by Fox, Loh,
> and Zhao [FLZ15].
>
> *References:*
> * [erdosproblems.com/22](https://www.erdosproblems.com/22)
> * [BoEr76] Bollobás, B. and Erdős, P., *On a Ramsey-Turán type problem*. J. Combin. Theory
>   Ser. B 21 (1976), 166--168.
> * [Sz72] Szemerédi, E., *On graphs containing no complete subgraph with 4 vertices*
>   (Hungarian). Mat. Lapok 23 (1972), 113--116.
> * [FLZ15] Fox, J., Loh, P.-S., and Zhao, Y., *The critical window for the classical
>   Ramsey-Turán problem*. Combinatorica 35 (2015), 435--476.

*Quoted from [FormalConjectures/ErdosProblems/22.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/22.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/22](https://www.erdosproblems.com/22).

The file states 4 research or textbook statements: 4 solved. It also has 1 test statement, counted here but not shown.

## `Erdos22.erdos_22`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos22.lean#L880](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos22.lean#L880).

> Let $\epsilon > 0$ and let $n$ be sufficiently large depending on $\epsilon$. Is there a graph
> on $n$ vertices with at least $n^2/8$ many edges which contains no $K_4$, such that the largest
> independent set has size at most $\epsilon n$?
>
> This is true, as proved by Fox, Loh, and Zhao [FLZ15].

```lean
theorem erdos_22 :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ (n : ℕ) in atTop,
      ∃ G : SimpleGraph (Fin n), G.CliqueFree 4 ∧
        (G.indepNum : ℝ) ≤ ε * n ∧ (n : ℝ) ^ 2 / 8 ≤ G.edgeFinset.card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/22.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/22.lean#L61).

## `Erdos22.erdos_22.variants.szemeredi_upper`

Solved: stated here without proof.

> The matching upper bound, due to Szemerédi [Sz72]: a $K_4$-free graph on $n$ vertices whose
> independence number is sublinear in $n$ has at most $(1/8 + o(1))n^2$ edges. That is, for every
> $\epsilon > 0$ there is a $\delta > 0$ such that for all sufficiently large $n$, every
> $K_4$-free graph $G$ on $n$ vertices with $\alpha(G) \leq \delta n$ has at most
> $(1/8 + \epsilon)n^2$ edges.

```lean
theorem erdos_22.variants.szemeredi_upper (ε : ℝ) (hε : 0 < ε) :
    ∃ δ : ℝ, 0 < δ ∧ ∀ᶠ (n : ℕ) in atTop,
      ∀ G : SimpleGraph (Fin n), G.CliqueFree 4 →
        (G.indepNum : ℝ) ≤ δ * n →
        (G.edgeFinset.card : ℝ) ≤ (1 / 8 + ε) * n ^ 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/22.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/22.lean#L76).

## `Erdos22.erdos_22.variants.bollobas_erdos_lower`

Solved: stated here without proof.

> The construction of Bollobás and Erdős [BoEr76]: for every $\epsilon > 0$ and $\delta > 0$,
> for all sufficiently large $n$ there is a $K_4$-free graph on $n$ vertices with independence
> number at most $\delta n$ and at least $(1/8 - \epsilon)n^2$ edges. Together with
> `erdos_22.variants.szemeredi_upper` this shows that the Ramsey–Turán density of $K_4$ is $1/8$.

```lean
theorem erdos_22.variants.bollobas_erdos_lower (ε δ : ℝ) (hε : 0 < ε) (hδ : 0 < δ) :
    ∀ᶠ (n : ℕ) in atTop,
      ∃ G : SimpleGraph (Fin n), G.CliqueFree 4 ∧
        (G.indepNum : ℝ) ≤ δ * n ∧ (1 / 8 - ε) * n ^ 2 ≤ G.edgeFinset.card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/22.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/22.lean#L91).

## `Erdos22.erdos_22.variants.fox_loh_zhao`

Solved: stated here without proof.

> The quantitative strengthening proved by Fox, Loh, and Zhao [FLZ15]: there is a constant
> $C > 0$ such that for all sufficiently large $n$ there exists a $K_4$-free graph on $n$
> vertices with at least $n^2/8$ edges whose largest independent set has size at most
>
> $$C \cdot \frac{(\log\log n)^{3/2}}{(\log n)^{1/2}} \cdot n.$$

```lean
theorem erdos_22.variants.fox_loh_zhao :
    ∃ C : ℝ, 0 < C ∧ ∀ᶠ (n : ℕ) in atTop,
      ∃ G : SimpleGraph (Fin n), G.CliqueFree 4 ∧
        (G.indepNum : ℝ) ≤
          C * (Real.log (Real.log n)) ^ (3 / 2 : ℝ) / (Real.log n) ^ (1 / 2 : ℝ) * n ∧
        (n : ℝ) ^ 2 / 8 ≤ G.edgeFinset.card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/22.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/22.lean#L105).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/22.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/22.lean)
- [erdosproblems.com/22](https://www.erdosproblems.com/22)
