---
declaration: theorem
origin: cited
lean: Erdos59.erdos_59, Erdos59.erdos_59.variants.erdos_frankl_rodl, Erdos59.erdos_59.variants.morris_saxton, Erdos59.erdos_59.variants.c4, Erdos59.erdos_59.variants.big_o
statement: formalized
---

# Erdős Problem 59

> *References:*
> - [erdosproblems.com/59](https://www.erdosproblems.com/59)
> - [EFR86] Erdős, P., Frankl, P. and Rödl, V., *The asymptotic number of graphs not containing a
>   fixed subgraph and a problem for hypergraphs having no exponent*. Graphs Combin. (1986),
>   113-121.
> - [MoSa16] Morris, R. and Saxton, D., *The number of $C_{2\ell}$-free graphs*. Adv. Math. (2016),
>   534-580. [arXiv:1309.2927](https://arxiv.org/abs/1309.2927)
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference "Paul
>   Erdős and his mathematics", Budapest, July 1999 (1999).

*Quoted from [FormalConjectures/ErdosProblems/59.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/59.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/59](https://www.erdosproblems.com/59).

The file states 5 research or textbook statements: 2 open and 3 solved. It also has 1 API statement, counted here but not shown.

## `Erdos59.erdos_59`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos59.lean#L46](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos59.lean#L46).

> Is it true that the number of graphs on $n$ vertices which do not contain $G$ is
> $$\leq 2^{(1+o(1))\mathrm{ex}(n;G)}?$$
>
> The answer is no, already for $G=C_6$ (see `erdos_59.variants.morris_saxton`). Graphs are
> labelled, and $G$ ranges over finite graphs containing a cycle, as in [MoSa16]; for some forests
> the answer is trivially no (for the path with two edges the free graphs include all matchings,
> about $2^{\Theta(n\log n)}$ of them).

```lean
theorem erdos_59 :
    ¬ ∀ (k : ℕ) (H : SimpleGraph (Fin k)), ¬ H.IsAcyclic →
      ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
        (numFree H n : ℝ) ≤ (2 : ℝ) ^ ((1 + ε) * (extremalNumber n H : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/59.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/59.lean#L64).

## `Erdos59.erdos_59.variants.erdos_frankl_rodl`

Solved: stated here without proof.

> If $G$ is not bipartite the answer is yes, proved by Erdős, Frankl, and Rödl [EFR86].

```lean
theorem erdos_59.variants.erdos_frankl_rodl {k : ℕ} (H : SimpleGraph (Fin k))
    (hH : ¬ H.IsBipartite) :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      (numFree H n : ℝ) ≤ (2 : ℝ) ^ ((1 + ε) * (extremalNumber n H : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/59.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/59.lean#L74).

## `Erdos59.erdos_59.variants.morris_saxton`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos59.lean#L46](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos59.lean#L46).

> The answer is no for $G=C_6$, the cycle on 6 vertices. Morris and Saxton [MoSa16, Proposition
> 1.4] have proved there are at least
> $$2^{(1+c)\mathrm{ex}(n;C_6)}$$
> such graphs for infinitely many $n$, for some constant $c>0$.

```lean
theorem erdos_59.variants.morris_saxton :
    ∃ c : ℝ, 0 < c ∧ ∃ᶠ n : ℕ in atTop,
      (2 : ℝ) ^ ((1 + c) * (extremalNumber n (cycleGraph 6) : ℝ)) ≤
        (numFree (cycleGraph 6) n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/59.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/59.lean#L89).

## `Erdos59.erdos_59.variants.c4`

Open: stated without proof.

> In [Va99] the specific case of $G=C_4$ is also asked.

```lean
theorem erdos_59.variants.c4 :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      (numFree (cycleGraph 4) n : ℝ) ≤
        (2 : ℝ) ^ ((1 + ε) * (extremalNumber n (cycleGraph 4) : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/59.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/59.lean#L99).

## `Erdos59.erdos_59.variants.big_o`

Open: stated without proof.

> It is still possible (and conjectured by Morris and Saxton) that the weaker bound of
> $$2^{O(\mathrm{ex}(n;G))}$$
> holds for all $G$ containing a cycle.

```lean
theorem erdos_59.variants.big_o :
    ∀ (k : ℕ) (H : SimpleGraph (Fin k)), ¬ H.IsAcyclic →
      ∃ C : ℝ, 0 < C ∧ ∀ᶠ n : ℕ in atTop,
        (numFree H n : ℝ) ≤ (2 : ℝ) ^ (C * (extremalNumber n H : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/59.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/59.lean#L111).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/59.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/59.lean)
- [erdosproblems.com/59](https://www.erdosproblems.com/59)
