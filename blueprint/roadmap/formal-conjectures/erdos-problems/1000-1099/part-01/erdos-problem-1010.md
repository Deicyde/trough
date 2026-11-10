---
declaration: theorem
origin: cited
lean: Erdos1010.erdos_1010, Erdos1010.erdos_1010.variants.rademacher, Erdos1010.erdos_1010.variants.erdos
statement: formalized
---

# Erdős Problem 1010

> *References:*
> - [erdosproblems.com/1010](https://www.erdosproblems.com/1010)
> - [Er62d] Erdős, P., *On a theorem of Rademacher-Turán*. Illinois J. Math. (1962), 122-127.
> - [LoSi76] Lovász, L. and Simonovits, Miklós, *On the number of complete subgraphs of a graph*.
>   (1976), 431-441.
> - [NiKh81] Nikiforov, V. S. and Khadzhiivanov, N. G., *Solution of the problem of P. Erdős on the
>   number of triangles in graphs with $n$ vertices and $[n^2/4]+l$ edges*. C. R. Acad. Bulgare
>   Sci. (1981), 969-970.

*Quoted from [FormalConjectures/ErdosProblems/1010.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1010.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1010](https://www.erdosproblems.com/1010).

The file states 3 research or textbook statements: 3 solved.

## `Erdos1010.erdos_1010`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1010.lean#L612](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1010.lean#L612).

> Let $t\lt \lfloor n/2\rfloor$. Does every graph on $n$ vertices with $\lfloor n^2/4\rfloor+t$ edges
> contain at least $t\lfloor n/2\rfloor$ triangles?
>
> Rademacher proved that every graph on $n$ vertices with $\lfloor n^2/4\rfloor+1$ edges contains at
> least $\lfloor n/2\rfloor$ triangles. Erdős [Er62d] proved that every graph on $n$ vertices with
> $\lfloor n^2/4\rfloor+t$ edges contains at least $t\lfloor n/2\rfloor$ triangles, for all $t\lt cn$,
> for some constant $c>0$.
>
> This is true, and was proved independently by Lovász and Simonovits [LoSi76] and Nikiforov and
> Khadzhiivanov [NiKh81].

```lean
theorem erdos_1010 : ∀ n t : ℕ, t < n / 2 → ∀ G : SimpleGraph (Fin n),
    G.edgeFinset.card = n ^ 2 / 4 + t → t * (n / 2) ≤ (G.cliqueFinset 3).card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1010.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1010.lean#L55).

## `Erdos1010.erdos_1010.variants.rademacher`

Solved: stated here without proof.

> Rademacher proved that every graph on $n$ vertices with $\lfloor n^2/4\rfloor+1$ edges contains at
> least $\lfloor n/2\rfloor$ triangles.

```lean
theorem erdos_1010.variants.rademacher : ∀ n : ℕ, ∀ G : SimpleGraph (Fin n),
    G.edgeFinset.card = n ^ 2 / 4 + 1 → n / 2 ≤ (G.cliqueFinset 3).card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1010.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1010.lean#L65).

## `Erdos1010.erdos_1010.variants.erdos`

Solved: stated here without proof.

> Erdős [Er62d] proved that every graph on $n$ vertices with $\lfloor n^2/4\rfloor+t$ edges contains
> at least $t\lfloor n/2\rfloor$ triangles, for all $t\lt cn$, for some constant $c>0$.

```lean
theorem erdos_1010.variants.erdos : ∃ c : ℝ, 0 < c ∧ ∀ n t : ℕ, t < c * n →
    ∀ G : SimpleGraph (Fin n), G.edgeFinset.card = n ^ 2 / 4 + t →
      t * (n / 2) ≤ (G.cliqueFinset 3).card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1010.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1010.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1010.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1010.lean)
- [erdosproblems.com/1010](https://www.erdosproblems.com/1010)
