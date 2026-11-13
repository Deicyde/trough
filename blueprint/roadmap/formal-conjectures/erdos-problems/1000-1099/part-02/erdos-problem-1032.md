---
declaration: theorem
origin: cited
lean: Erdos1032.erdos_1032, Erdos1032.erdos_1032.variants.five, Erdos1032.erdos_1032.variants.dirac_six, Erdos1032.erdos_1032.variants.simonovits_toft
statement: formalized
---

# Erdős Problem 1032

> *References:*
> - [erdosproblems.com/1032](https://www.erdosproblems.com/1032)
> - [Er93] Erdős, P., *Some of my favorite solved and unsolved problems in graph theory*.
>   Quaestiones Math. 16 (1993), 333-350.
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference
>   "Paul Erdős and his mathematics", Budapest, July 1999 (1999).
> - [Di52] Dirac, G. A., *A property of $4$-chromatic graphs and some remarks on critical graphs*.
>   J. London Math. Soc. 27 (1952), 85-92.
> - [Si72] Simonovits, M., *On colour-critical graphs*. Studia Sci. Math. Hungar. 7 (1972), 67-81.
> - [To72] Toft, B., *Two theorems on critical $4$-chromatic graphs*. Studia Sci. Math. Hungar. 7
>   (1972), 83-89.
> - [Ma15] Markström, K. (ed.), *Problem collection from the IML programme: Graphs, Hypergraphs,
>   and Computing*. [arXiv:1511.00270](https://arxiv.org/abs/1511.00270) (2015). Problem 5.1
>   (M. Simonovits).
>
> See also [erdosproblems.com/917](https://www.erdosproblems.com/917) and
> [erdosproblems.com/944](https://www.erdosproblems.com/944).

*Quoted from [FormalConjectures/ErdosProblems/1032.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1032.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1032](https://www.erdosproblems.com/1032).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos1032.erdos_1032`

Open: stated without proof.

> We say that a graph is $4$-chromatic critical if it has chromatic number $4$, and removing any edge
> decreases the chromatic number to $3$.
>
> Is there, for arbitrarily large $n$, a $4$-chromatic critical graph on $n$ vertices with minimum
> degree $\gg n$?
>
> This is a question of Erdős [Er93, p. 341] (see also [Va99, 3.60]). We read $\gg n$ as
> $\geq cn$ for a fixed constant $c > 0$.

```lean
theorem erdos_1032 :
    ∃ c : ℝ, 0 < c ∧ ∃ᶠ n : ℕ in atTop,
      ∃ G : SimpleGraph (Fin n), IsKCritical G 4 ∧ c * (n : ℝ) ≤ (G.minDegree : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1032.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1032.lean#L71).

## `Erdos1032.erdos_1032.variants.five`

Open: stated without proof.

> Is there, for arbitrarily large $n$, a $5$-chromatic critical graph on $n$ vertices with minimum
> degree $\gg n$?
>
> This problem is also open for $5$-chromatic critical graphs.

```lean
theorem erdos_1032.variants.five :
    ∃ c : ℝ, 0 < c ∧ ∃ᶠ n : ℕ in atTop,
      ∃ G : SimpleGraph (Fin n), IsKCritical G 5 ∧ c * (n : ℝ) ≤ (G.minDegree : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1032.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1032.lean#L84).

## `Erdos1032.erdos_1032.variants.dirac_six`

Solved: stated here without proof.

> Dirac gave an example of a $6$-chromatic critical graph with minimum degree $>n/2$.
>
> Dirac's graphs join two disjoint odd cycles of length $n/2$ [Di52], [Ma15]. Here we state that
> there are such graphs for infinitely many $n$.

```lean
theorem erdos_1032.variants.dirac_six :
    ∃ᶠ n : ℕ in atTop,
      ∃ G : SimpleGraph (Fin n), IsKCritical G 6 ∧ (n : ℝ) / 2 < (G.minDegree : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1032.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1032.lean#L97).

## `Erdos1032.erdos_1032.variants.simonovits_toft`

Solved: stated here without proof.

> Simonovits [Si72] and Toft [To72] independently constructed $4$-chromatic critical graphs with
> minimum degree $\gg n^{1/3}$.
>
> We state this as in [Ma15, Problem 5.1]: there are $4$-critical graphs on $n$ vertices with minimum
> degree at least $c n^{1/3}$ for infinitely many $n$, for a fixed constant $c > 0$.

```lean
theorem erdos_1032.variants.simonovits_toft :
    ∃ c : ℝ, 0 < c ∧ ∃ᶠ n : ℕ in atTop,
      ∃ G : SimpleGraph (Fin n),
        IsKCritical G 4 ∧ c * (n : ℝ) ^ ((1 : ℝ) / 3) ≤ (G.minDegree : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1032.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1032.lean#L111).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1032.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1032.lean)
- [erdosproblems.com/1032](https://www.erdosproblems.com/1032)
