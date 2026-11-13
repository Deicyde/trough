---
declaration: theorem
origin: cited
lean: Erdos24.erdos_24
statement: formalized
---

# Erdős Problem 24

> *References:*
> - [erdosproblems.com/24](https://www.erdosproblems.com/24)
> - [Er90] Erdős, Paul, *Some of my favourite unsolved problems*. A tribute to Paul Erdős (1990),
>   467-478.
> - [Er97b] Erdős, Paul, *Some old and new problems in various branches of combinatorics*. Discrete
>   Math. (1997), 227-231.
> - [Er92b] Erdős, Paul, *Some of my favourite problems in various branches of combinatorics*.
>   Matematiche (Catania) (1992), 231-240.
> - [Er97f] Erdős, Paul, *Some unsolved problems*. Combinatorics, geometry and probability
>   (Cambridge, 1993) (1997), 1-10.
> - [Gr12] Grzesik, Andrzej, *On the maximum number of five-cycles in a triangle-free graph*.
>   J. Combin. Theory Ser. B (2012), 1061-1066.
> - [HHKNR13] Hatami, Hamed and Hladký, Jan and Kráľ, Daniel and Norine, Serguei and Razborov,
>   Alexander, *On the number of pentagons in triangle-free graphs*. J. Combin. Theory Ser. A
>   (2013), 722-732.

*Quoted from [FormalConjectures/ErdosProblems/24.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/24.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/24](https://www.erdosproblems.com/24).

The file states 1 research or textbook statement: 1 solved.

## `Erdos24.erdos_24`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos24.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos24.lean).

> Does every triangle-free graph on $5n$ vertices contain at most $n^5$ copies of $C_5$?
>
> Győri proved this with $1.03n^5$, which has been improved by Füredi. The answer is yes, as proved
> independently by Grzesik [Gr12] and Hatami, Hladky, Král, Norine, and Razborov [HHKNR13].

```lean
theorem erdos_24 :
    ∀ (n : ℕ) (G : SimpleGraph (Fin (5 * n))), G.CliqueFree 3 →
      G.copyCount (cycleGraph 5) ≤ n ^ 5
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/24.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/24.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/24.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/24.lean)
- [erdosproblems.com/24](https://www.erdosproblems.com/24)
