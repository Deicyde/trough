---
declaration: theorem
origin: cited
lean: Erdos533.erdos_533, Erdos533.erdos_533.variants.ehsss_upper, Erdos533.erdos_533.variants.lrss_lower, Erdos533.erdos_533.variants.delta_four_eq_zero, Erdos533.erdos_533.variants.delta_seven_ge_quarter
statement: formalized
---

# Erdős Problem 533

> *References:*
> - [erdosproblems.com/533](https://www.erdosproblems.com/533)
> - [EHSSS94] P. Erdős, A. Hajnal, M. Simonovits, V. T. Sós and E. Szemerédi,
>   *Turán-Ramsey theorems and $K_p$-independence numbers*,
>   Combin. Probab. Comput. **3** (1994), 297–325.
> - [ErRo62] P. Erdős and C. A. Rogers, *The construction of certain graphs*,
>   Canad. J. Math. **14** (1962), 702–707.
> - [BaLe13] J. Balogh and J. Lenz, *On the Ramsey–Turán numbers of graphs and hypergraphs*,
>   Israel J. Math. **194** (2013), 45–68.
> - [LRSS21] H. Liu, C. Reiher, M. Sharifzadeh and K. Staden,
>   *Geometric constructions for Ramsey–Turán theory*,
>   [arXiv:2103.10423](https://arxiv.org/abs/2103.10423) (2021).

*Quoted from [FormalConjectures/ErdosProblems/533.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/533.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/533](https://www.erdosproblems.com/533).

The file states 5 research or textbook statements: 5 solved. It also has 1 test statement, counted here but not shown.

## `Erdos533.erdos_533`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos533.lean#L2922](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos533.lean#L2922).

> Let $\delta > 0$. If $n$ is sufficiently large and $G$ is a graph on $n$ vertices with no
> $K_5$ and at least $\delta n^2$ edges, must $G$ contain a set of $\gg_\delta n$ vertices
> spanning no triangle?
>
> Equivalently, writing $\mathrm{RT}_3(n, K_5, m)$ for the maximum number of edges of a
> $K_5$-free graph on $n$ vertices in which every triangle-free vertex set has fewer than $m$
> vertices (the *triangle Ramsey–Turán number*), is
> $$\delta_3(5) = \lim_{\epsilon \to 0} \lim_{n \to \infty}
>   \frac{\mathrm{RT}_3(n, K_5, \epsilon n)}{n^2} = 0?$$
>
> This is a problem of Erdős, Hajnal, Simonovits, Sós, and Szemerédi [EHSSS94], who proved
> $\delta_3(5) \leq 1/12$ and the analogous $\delta_3(4) = 0$, and observed $\delta_3(7) \geq 1/4$
> via a construction of Erdős and Rogers [ErRo62].
>
> The answer is **no**: Balogh and Lenz [BaLe13] disproved it by showing $\delta_3(5) > 0$, and
> the exact value $\delta_3(5) = 1/12$ was determined by the matching lower-bound construction of
> Liu, Reiher, Sharifzadeh, and Staden [LRSS21] (see `erdos_533.variants.lrss_lower`).

```lean
theorem erdos_533 :
    ¬ ∀ δ : ℝ, 0 < δ → ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop,
      ∀ G : SimpleGraph (Fin n), G.CliqueFree 5 →
        δ * (n : ℝ) ^ 2 ≤ G.edgeFinset.card →
          ∃ S : Finset (Fin n), c * n ≤ (S.card : ℝ) ∧
            G.CliqueFreeOn (S : Set (Fin n)) 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/533.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/533.lean#L66).

## `Erdos533.erdos_533.variants.ehsss_upper`

Solved: stated here without proof.

> The upper bound $\delta_3(5) \leq 1/12$ of Erdős, Hajnal, Simonovits, Sós, and Szemerédi
> [EHSSS94]: for every $\epsilon > 0$ there is a $\delta > 0$ such that for all sufficiently
> large $n$, every $K_5$-free graph $G$ on $n$ vertices in which every triangle-free vertex
> set has at most $\delta n$ vertices has at most $(1/12 + \epsilon)n^2$ edges.

```lean
theorem erdos_533.variants.ehsss_upper (ε : ℝ) (hε : 0 < ε) :
    ∃ δ : ℝ, 0 < δ ∧ ∀ᶠ n : ℕ in atTop,
      ∀ G : SimpleGraph (Fin n), G.CliqueFree 5 →
        (∀ S : Finset (Fin n),
            G.CliqueFreeOn (S : Set (Fin n)) 3 → (S.card : ℝ) ≤ δ * n) →
          (G.edgeFinset.card : ℝ) ≤ (1 / 12 + ε) * n ^ 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/533.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/533.lean#L82).

## `Erdos533.erdos_533.variants.lrss_lower`

Solved: stated here without proof.

> The matching lower bound $\delta_3(5) \geq 1/12$, from the construction of Liu, Reiher,
> Sharifzadeh, and Staden [LRSS21] (improving the earlier $\delta_3(5) > 0$ of Balogh and Lenz
> [BaLe13]): for every $\epsilon, \delta > 0$ and all sufficiently large $n$ there is a
> $K_5$-free graph $G$ on $n$ vertices in which every triangle-free vertex set has at most
> $\delta n$ vertices, yet which has at least $(1/12 - \epsilon)n^2$ edges. In particular this
> refutes `erdos_533`.

```lean
theorem erdos_533.variants.lrss_lower (ε δ : ℝ) (hε : 0 < ε) (hδ : 0 < δ) :
    ∀ᶠ n : ℕ in atTop,
      ∃ G : SimpleGraph (Fin n), G.CliqueFree 5 ∧
        (∀ S : Finset (Fin n),
            G.CliqueFreeOn (S : Set (Fin n)) 3 → (S.card : ℝ) ≤ δ * n) ∧
        (1 / 12 - ε) * (n : ℝ) ^ 2 ≤ G.edgeFinset.card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/533.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/533.lean#L100).

## `Erdos533.erdos_533.variants.delta_four_eq_zero`

Solved: stated here without proof.

> The contrasting positive result $\delta_3(4) = 0$ of Erdős, Hajnal, Simonovits, Sós, and
> Szemerédi [EHSSS94]: the $K_4$ analogue of `erdos_533` is **true**. For every $\delta > 0$
> there is a $c > 0$ such that for all sufficiently large $n$, every $K_4$-free graph $G$ on
> $n$ vertices with at least $\delta n^2$ edges contains a triangle-free vertex set of size at
> least $c n$.

```lean
theorem erdos_533.variants.delta_four_eq_zero :
    ∀ δ : ℝ, 0 < δ → ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop,
      ∀ G : SimpleGraph (Fin n), G.CliqueFree 4 →
        δ * (n : ℝ) ^ 2 ≤ G.edgeFinset.card →
          ∃ S : Finset (Fin n), c * n ≤ (S.card : ℝ) ∧
            G.CliqueFreeOn (S : Set (Fin n)) 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/533.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/533.lean#L117).

## `Erdos533.erdos_533.variants.delta_seven_ge_quarter`

Solved: stated here without proof.

> The observation $\delta_3(7) \geq 1/4$ of Erdős, Hajnal, Simonovits, Sós, and Szemerédi
> [EHSSS94], via a construction of Erdős and Rogers [ErRo62]: for every $\epsilon, \delta > 0$
> and all sufficiently large $n$ there is a $K_7$-free graph $G$ on $n$ vertices in which every
> triangle-free vertex set has at most $\delta n$ vertices, yet which has at least
> $(1/4 - \epsilon)n^2$ edges.

```lean
theorem erdos_533.variants.delta_seven_ge_quarter (ε δ : ℝ) (hε : 0 < ε) (hδ : 0 < δ) :
    ∀ᶠ n : ℕ in atTop,
      ∃ G : SimpleGraph (Fin n), G.CliqueFree 7 ∧
        (∀ S : Finset (Fin n),
            G.CliqueFreeOn (S : Set (Fin n)) 3 → (S.card : ℝ) ≤ δ * n) ∧
        (1 / 4 - ε) * (n : ℝ) ^ 2 ≤ G.edgeFinset.card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/533.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/533.lean#L134).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/533.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/533.lean)
- [erdosproblems.com/533](https://www.erdosproblems.com/533)
