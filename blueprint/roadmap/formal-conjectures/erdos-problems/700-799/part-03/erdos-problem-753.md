---
declaration: theorem
origin: cited
lean: Erdos753.erdos_753, Erdos753.erdos_753.variants.alon
statement: formalized
---

# Erdős Problem 753

> *References:*
> - [erdosproblems.com/753](https://www.erdosproblems.com/753)
> - [Al92] Alon, Noga, *Choice numbers of graphs: a probabilistic approach*. Combin. Probab.
>   Comput. (1992), 107-114.

*Quoted from [FormalConjectures/ErdosProblems/753.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/753.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/753](https://www.erdosproblems.com/753).

The file states 2 research or textbook statements: 2 solved.

## `Erdos753.erdos_753`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos753.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos753.lean).

> The list chromatic number $\chi_L(G)$ is defined to be the minimal $k$ such that for any
> assignment of a list of $k$ colours to each vertex of $G$ (perhaps different lists for different
> vertices) a colouring of each vertex by a colour on its list can be chosen such that adjacent
> vertices receive distinct colours.
>
> Does there exist some constant $c>0$ such that
>
> $$\chi_L(G)+\chi_L(G^c)> n^{1/2+c}$$
>
> for every graph $G$ on $n$ vertices (where $G^c$ is the complement of $G$)?
>
> A problem of Erdős, Rubin, and Taylor.
>
> The answer is no: Alon [Al92] proved that, for every $n$, there exists a graph $G$ on $n$ vertices
> such that
>
> $$\chi_L(G)+\chi_L(G^c)\ll (n\log n)^{1/2},$$
>
> where the implied constant is absolute.

```lean
theorem erdos_753 :
    ¬ ∃ c : ℝ, 0 < c ∧ ∀ n : ℕ, 0 < n → ∀ G : SimpleGraph (Fin n),
      (n : ℝ) ^ ((1 : ℝ) / 2 + c) <
        (listChromaticNumber G : ℝ) + (listChromaticNumber Gᶜ : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/753.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/753.lean#L54).

## `Erdos753.erdos_753.variants.alon`

Solved: stated here without proof.

> Alon [Al92] proved that, for every $n$, there exists a graph $G$ on $n$ vertices such that
>
> $$\chi_L(G)+\chi_L(G^c)\ll (n\log n)^{1/2},$$
>
> where the implied constant is absolute.

```lean
theorem erdos_753.variants.alon :
    ∃ C : ℝ, 0 < C ∧ ∀ n : ℕ, 2 ≤ n → ∃ G : SimpleGraph (Fin n),
      (listChromaticNumber G : ℝ) + (listChromaticNumber Gᶜ : ℝ) ≤
        C * ((n : ℝ) * Real.log (n : ℝ)) ^ ((1 : ℝ) / 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/753.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/753.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/753.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/753.lean)
- [erdosproblems.com/753](https://www.erdosproblems.com/753)
