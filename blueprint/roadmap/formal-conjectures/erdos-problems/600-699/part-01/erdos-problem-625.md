---
declaration: theorem
origin: cited
lean: Erdos625.erdos_625, Erdos625.erdos_625.variants.quantitative
statement: formalized
---

# Erdős Problem 625

> *References:*
> - [erdosproblems.com/625](https://www.erdosproblems.com/625)
> - [ErGi93] P. Erdős and J. Gimbel, *Some problems and results in cochromatic theory*.
>   Annals of Discrete Mathematics 55 (1993), 261–264.
> - [Gi16] J. Gimbel, *Some of my favorite coloring problems for graphs and digraphs*.
>   Graph Theory: Favorite Conjectures and Open Problems 1 (2016), 95–108.
> - [He24c] A. Heckel, *The difference between the chromatic and the cochromatic number of a
>   random graph* (2024), [arXiv:2409.17614](https://arxiv.org/abs/2409.17614).
> - [Pe26] S. Petkov, *A Full-Sequence Quantitative Gap Between the Chromatic and Cochromatic
>   Numbers of a Random Graph* (2026), [arXiv:2608.30604](https://arxiv.org/abs/2608.30604).

*Quoted from [FormalConjectures/ErdosProblems/625.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/625.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/625](https://www.erdosproblems.com/625).

The file states 2 research or textbook statements: 2 solved.

## `Erdos625.erdos_625`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-09-02-000006](https://palomar-registry.org/entry.html?id=PALOMAR-2026-09-02-000006).

> The cochromatic number of $G$, denoted by $\zeta(G)$, is the minimum number of colours needed
> to colour the vertices of $G$ such that each colour class induces either a complete graph or
> empty graph. Let $\chi(G)$ denote the chromatic number.
>
> If $G$ is a random graph with $n$ vertices and each edge included independently with
> probability $1/2$ then is it true that almost surely $\chi(G)-\zeta(G)\to\infty$ as
> $n\to\infty$?
>
> Here "almost surely $\chi(G)-\zeta(G)\to\infty$" is read in the usual random-graph sense: for
> every fixed real threshold $K$, the probability that $\chi(G)-\zeta(G)\ge K$ tends to one along
> the full sequence of natural numbers. The answer is yes. Heckel [He24c] proved this along a
> subsequence of density about $0.95$; Petkov [Pe26] proves it along all $n$, with the
> quantitative bound below.

```lean
theorem erdos_625 :
    ∀ K : ℝ, Tendsto
      (fun n : ℕ ↦ binomialRandom (Fin n) ⟨1 / 2, by norm_num⟩
        {G | K ≤ (G.chromaticNumber.toNat : ℝ) - G.cochromaticNumber.toNat})
      atTop (𝓝 1)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/625.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/625.lean#L59).

## `Erdos625.erdos_625.variants.quantitative`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-09-02-000006](https://palomar-registry.org/entry.html?id=PALOMAR-2026-09-02-000006).

> Petkov [Pe26] proves that, for $G\sim G(n,1/2)$, the probability that
>
> $$\chi(G)-\zeta(G)\geq
> \frac{(\log 2)^2}{4}\log\!\left(\frac{200}{153}\right)\frac{n}{(\log n)^3}$$
>
> tends to one as $n\to\infty$ along all natural numbers. All logarithms are natural.

```lean
theorem erdos_625.variants.quantitative :
    Tendsto
      (fun n : ℕ ↦ binomialRandom (Fin n) ⟨1 / 2, by norm_num⟩
        {G | ((Real.log 2) ^ 2 / 4 * Real.log (200 / 153 : ℝ)) *
            n / (Real.log n) ^ 3 ≤
          (G.chromaticNumber.toNat : ℝ) - G.cochromaticNumber.toNat})
      atTop (𝓝 1)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/625.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/625.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/625.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/625.lean)
- [erdosproblems.com/625](https://www.erdosproblems.com/625)
