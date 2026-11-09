---
declaration: theorem
origin: cited
lean: Erdos802.erdos_802, Erdos802.erdos_802.variants.aeks, Erdos802.erdos_802.variants.shearer, Erdos802.erdos_802.variants.r_eq_three, Erdos802.erdos_802.variants.alon
statement: formalized
---

# Erdős Problem 802

> *References:*
> - [erdosproblems.com/802](https://www.erdosproblems.com/802)
> - [AEKS81] Ajtai, M. and Erdős, P. and Komlós, J. and Szemerédi, E., *On Turán's theorem for
>   sparse graphs*. Combinatorica (1981), 313-317.
> - [AKS80] Ajtai, Miklós and Komlós, János and Szemerédi, Endre, *A note on Ramsey numbers*.
>   J. Combin. Theory Ser. A (1980), 354-360.
> - [Al96b] Alon, Noga, *Independence numbers of locally sparse graphs and a Ramsey type problem*.
>   Random Structures Algorithms (1996), 271-278.
> - [Sh95] Shearer, James B., *On the independence number of sparse graphs*. Random Structures
>   Algorithms (1995), 269-271.

*Quoted from [FormalConjectures/ErdosProblems/802.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/802.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/802](https://www.erdosproblems.com/802).

The file states 5 research or textbook statements: 1 open and 4 solved.

## `Erdos802.erdos_802`

Open: stated without proof.

> Is it true that any $K_r$-free graph on $n$ vertices with average degree $t$ contains an
> independent set on
> $$\gg_r \frac{\log t}{t}n$$
> many vertices?
>
> A conjecture of Ajtai, Erdős, Komlós, and Szemerédi [AEKS81].

```lean
theorem erdos_802 : ∀ r : ℕ, ∃ c > (0 : ℝ), ∀ n : ℕ, ∀ G : SimpleGraph (Fin n),
    G.CliqueFree r →
      c * (log G.averageDegree / G.averageDegree) * n ≤ G.indepNum
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/802.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/802.lean#L51).

## `Erdos802.erdos_802.variants.aeks`

Solved: stated here without proof.

> Ajtai, Erdős, Komlós, and Szemerédi [AEKS81] proved that any $K_r$-free graph on $n$ vertices
> with average degree $t$ contains an independent set on
> $$\gg_r \frac{\log\log(t+1)}{t}n$$
> many vertices.

```lean
theorem erdos_802.variants.aeks : ∀ r : ℕ, ∃ c > (0 : ℝ), ∀ n : ℕ, ∀ G : SimpleGraph (Fin n),
    G.CliqueFree r →
      c * (log (log (G.averageDegree + 1)) / G.averageDegree) * n ≤ G.indepNum
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/802.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/802.lean#L64).

## `Erdos802.erdos_802.variants.shearer`

Solved: stated here without proof.

> Shearer [Sh95] proved that any $K_r$-free graph on $n$ vertices with average degree $t$ contains
> an independent set on
> $$\gg_r \frac{\log t}{\log\log(t+1)t}n$$
> many vertices.
>
> We assume $t \geq 2$. For $t + 1$ slightly larger than $e$ the factor $\log\log(t+1)$ is close
> to $0$, so the bound blows up and the statement is false without such a restriction.

```lean
theorem erdos_802.variants.shearer : ∀ r : ℕ, ∃ c > (0 : ℝ), ∀ n : ℕ, ∀ G : SimpleGraph (Fin n),
    G.CliqueFree r → 2 ≤ G.averageDegree →
      c * (log G.averageDegree / (log (log (G.averageDegree + 1)) * G.averageDegree)) * n ≤
        G.indepNum
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/802.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/802.lean#L80).

## `Erdos802.erdos_802.variants.r_eq_three`

Solved: stated here without proof.

> Ajtai, Komlós, and Szemerédi [AKS80] proved the conjectured bound when $r = 3$: any
> triangle-free graph on $n$ vertices with average degree $t$ contains an independent set on
> $$\gg \frac{\log t}{t}n$$
> many vertices.

```lean
theorem erdos_802.variants.r_eq_three : ∃ c > (0 : ℝ), ∀ n : ℕ, ∀ G : SimpleGraph (Fin n),
    G.CliqueFree 3 →
      c * (log G.averageDegree / G.averageDegree) * n ≤ G.indepNum
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/802.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/802.lean#L94).

## `Erdos802.erdos_802.variants.alon`

Solved: stated here without proof.

> Alon [Al96b] proved the conjectured bound under the stronger assumption that the induced graph
> on every vertex neighbourhood has chromatic number $\leq r - 2$.

```lean
theorem erdos_802.variants.alon : ∀ r : ℕ, ∃ c > (0 : ℝ), ∀ n : ℕ, ∀ G : SimpleGraph (Fin n),
    (∀ v, (G.induce (G.neighborSet v)).Colorable (r - 2)) →
      c * (log G.averageDegree / G.averageDegree) * n ≤ G.indepNum
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/802.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/802.lean#L105).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/802.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/802.lean)
- [erdosproblems.com/802](https://www.erdosproblems.com/802)
