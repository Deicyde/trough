---
declaration: theorem
origin: cited
lean: Erdos88.erdos_88, Erdos88.erdos_88.variants.erdos_mckay, Erdos88.erdos_88.variants.kwan_sah_sauermann_sawhney
statement: formalized
---

# Erdős Problem 88

> *References:*
> - [erdosproblems.com/88](https://www.erdosproblems.com/88)
> - [Er92b] Erdős, Paul, *Some of my favourite problems in various branches of combinatorics*.
>   Matematiche (Catania) (1992), 231-240.
> - [Er95] Erdős, Paul, *Some of my favourite problems in number theory, combinatorics, and
>   geometry*. Resenhas (1995), 165-186.
> - [Er97d] Erdős, Paul, *Some recent problems and results in graph theory*. Discrete Math. (1997),
>   81-85.
> - [KSSS22] Kwan, M. and Sah, A. and Sauermann, L. and Sawhney, M., *Anticoncentration in Ramsey
>   graphs and a proof of the Erdős-McKay conjecture*. Forum Math. Pi 11 (2023), e21.
>   [arXiv:2208.02874](https://arxiv.org/abs/2208.02874)

*Quoted from [FormalConjectures/ErdosProblems/88.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/88.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/88](https://www.erdosproblems.com/88).

The file states 3 research or textbook statements: 3 solved.

## `Erdos88.erdos_88`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos88.lean#L127](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos88.lean#L127).

> For any $\epsilon>0$ there exists $\delta=\delta(\epsilon)>0$ such that if $G$ is a graph on $n$
> vertices with no independent set or clique of size $\geq \epsilon\log n$ then $G$ contains an
> induced subgraph with $m$ edges for all $m\leq \delta n^2$.
>
> This was conjectured by Erdős and McKay and proved by Kwan, Sah, Sauermann, and Sawhney
> [KSSS22]. Erdős' original formulation also assumed that $G$ has $\gg n^2$ edges. By an old result
> of Erdős and Szemerédi this follows from the other condition, so it is omitted here.

```lean
theorem erdos_88 :
    ∀ ε > (0 : ℝ), ∃ δ > (0 : ℝ), ∀ n : ℕ, ∀ G : SimpleGraph (Fin n),
      (G.cliqueNum : ℝ) < ε * Real.log n → (G.indepNum : ℝ) < ε * Real.log n →
        ∀ m : ℕ, (m : ℝ) ≤ δ * n ^ 2 →
          ∃ S : Finset (Fin n), (G.induce (S : Set (Fin n))).edgeSet.ncard = m
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/88.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/88.lean#L54).

## `Erdos88.erdos_88.variants.erdos_mckay`

Solved: stated here without proof.

> Erdős and McKay proved the statement of `erdos_88` with $\delta n^2$ replaced by
> $\delta (\log n)^2$. Since $(\log n)^2 \leq n^2$, this weaker bound also follows from
> `erdos_88`.

```lean
theorem erdos_88.variants.erdos_mckay :
    ∀ ε > (0 : ℝ), ∃ δ > (0 : ℝ), ∀ n : ℕ, ∀ G : SimpleGraph (Fin n),
      (G.cliqueNum : ℝ) < ε * Real.log n → (G.indepNum : ℝ) < ε * Real.log n →
        ∀ m : ℕ, (m : ℝ) ≤ δ * Real.log n ^ 2 →
          ∃ S : Finset (Fin n), (G.induce (S : Set (Fin n))).edgeSet.ncard = m
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/88.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/88.lean#L67).

## `Erdos88.erdos_88.variants.kwan_sah_sauermann_sawhney`

Solved: stated here without proof.

> Kwan, Sah, Sauermann, and Sawhney [KSSS22, Theorem 1.1] proved the following stronger statement.
> Fix $C > 0$ and $\eta > 0$, and let $G$ be a graph on $n$ vertices with no independent set or
> clique of size $\geq C \log_2 n$, where $n$ is sufficiently large with respect to $C$ and $\eta$.
> Then for every integer $0 \leq m \leq (1 - \eta) e(G)$ there is an induced subgraph of $G$ with
> exactly $m$ edges.

```lean
theorem erdos_88.variants.kwan_sah_sauermann_sawhney :
    ∀ C > (0 : ℝ), ∀ η > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n),
      (G.cliqueNum : ℝ) < C * Real.logb 2 n → (G.indepNum : ℝ) < C * Real.logb 2 n →
        ∀ m : ℕ, (m : ℝ) ≤ (1 - η) * G.edgeSet.ncard →
          ∃ S : Finset (Fin n), (G.induce (S : Set (Fin n))).edgeSet.ncard = m
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/88.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/88.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/88.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/88.lean)
- [erdosproblems.com/88](https://www.erdosproblems.com/88)
