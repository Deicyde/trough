---
declaration: theorem
origin: cited
lean: Erdos1079.erdos_1079, Erdos1079.erdos_1079.variants.bondy
statement: formalized
---

# Erdős Problem 1079

> *References:*
> - [erdosproblems.com/1079](https://www.erdosproblems.com/1079)
> - [Er75] Erdős, P., *Some recent progress on extremal problems in graph theory*. Congr. Numer.
>   (1975), 3-14.
> - [BoTh81] Bollobás, Béla and Thomason, Andrew, *Dense neighbourhoods and Turán's theorem*. J.
>   Combin. Theory Ser. B (1981), 111--114.
> - [Bo83b] Bondy, J. A., *Large dense neighbourhoods and Turán's theorem*. J. Combin. Theory Ser.
>   B (1983), 109--111.

*Quoted from [FormalConjectures/ErdosProblems/1079.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1079.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1079](https://www.erdosproblems.com/1079).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1079.erdos_1079`

Solved: stated here without proof.

> Let $r\geq 4$. If $G$ is a graph on $n$ vertices with at least $\mathrm{ex}(n;K_r)$ edges then
> must $G$ contain a vertex with degree $d\gg_r n$ whose neighbourhood contains at least
> $\mathrm{ex}(d;K_{r-1})$ edges?
>
> As Erdős [Er75] says 'if true this would be a nice generalisation of Turán's theorem'. This is
> true (unless $G$ it itself the Turán graph), and was proved by Bollobás and Thomason [BoTh81].
> Bondy [Bo83b] showed that if $G$ has $>\mathrm{ex}(n;K_r)$ edges then the corresponding vertex
> can be chosen to be of maximum degree in $G$.
>
> The number of edges in the neighbourhood of $v$ is the number of edges of $G$ both of whose
> endpoints are adjacent to $v$. Graphs on a single vertex are excluded, since there every degree
> is $0$.

```lean
theorem erdos_1079 : ∀ r : ℕ, 4 ≤ r → ∃ c : ℝ, 0 < c ∧ ∀ n : ℕ, 2 ≤ n →
    ∀ G : SimpleGraph (Fin n), extremalNumber n (completeGraph (Fin r)) ≤ G.edgeSet.ncard →
      ∃ v : Fin n, c * n ≤ G.degree v ∧
        extremalNumber (G.degree v) (completeGraph (Fin (r - 1))) ≤
          {e ∈ G.edgeSet | ∀ x ∈ e, G.Adj v x}.ncard
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1079.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1079.lean#L55).

## `Erdos1079.erdos_1079.variants.bondy`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1079.lean#L424](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1079.lean#L424).

> Bondy's strengthening [Bo83b]: if $G$ has more than $\mathrm{ex}(n;K_r)$ edges then some vertex
> $v$ of maximum degree has $d(v) \geq n/2$ and its neighbourhood contains more than
> $\mathrm{ex}(d(v);K_{r-1})$ edges.

```lean
theorem erdos_1079.variants.bondy (r n : ℕ) (hr : 4 ≤ r) (G : SimpleGraph (Fin n))
    [DecidableRel G.Adj]
    (hG : extremalNumber n (completeGraph (Fin r)) < G.edgeSet.ncard) :
    ∃ v : Fin n, G.degree v = G.maxDegree ∧ n ≤ 2 * G.degree v ∧
      extremalNumber (G.degree v) (completeGraph (Fin (r - 1))) <
        {e ∈ G.edgeSet | ∀ x ∈ e, G.Adj v x}.ncard
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1079.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1079.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1079.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1079.lean)
- [erdosproblems.com/1079](https://www.erdosproblems.com/1079)
