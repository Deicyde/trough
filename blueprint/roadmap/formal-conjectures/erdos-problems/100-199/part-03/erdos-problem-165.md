---
declaration: theorem
origin: cited
lean: Erdos165.erdos_165, Erdos165.erdos_165.variants.conjecture, Erdos165.erdos_165.variants.upper, Erdos165.erdos_165.variants.lower
statement: formalized
---

# Erdős Problem 165

> *References:*
> - [erdosproblems.com/165](https://www.erdosproblems.com/165)
> - [Er61] Erdős, P., *Graph theory and probability. II*. Canad. J. Math. (1961), 346-352.
> - [Er71] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
> - [Er90b] Erdős, Paul, *Problems and results on graphs and hypergraphs: similarities and
>   differences*. Mathematics of Ramsey theory (1990), 12-28.
> - [Er93] Erdős, Paul, *Some of my favorite solved and unsolved problems in graph theory*.
>   Quaestiones Math. (1993), 333-350.
> - [Er97c] Erdős, Paul, *Some of my favorite problems and results*. The mathematics of Paul Erdős,
>   I (1997), 47-67.
> - [Sh83] Shearer, J. B., *A note on the independence number of triangle-free graphs*. Discrete
>   Math. (1983), 83-87.
> - [Ki95] Kim, J. H., *The Ramsey number $R(3,t)$ has order of magnitude $t^2/\log t$*. Random
>   Structures Algorithms (1995), 173-207.
> - [CJMS25] Campos, M. and Jenssen, M. and Michelen, M. and Sahasrabudhe, J., *A new lower bound
>   for the Ramsey numbers $R(3,k)$*. arXiv:2505.13371 (2025).
> - [HHKP25] Hefty, Z. and Horn, P. and King, D. and Pfender, F., *Improving $R(3,k)$ in just two
>   bites*. arXiv:2510.19718 (2025).

*Quoted from [FormalConjectures/ErdosProblems/165.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/165.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/165](https://www.erdosproblems.com/165).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos165.erdos_165`

Open: stated without proof.

> Give an asymptotic formula for $R(3,k)$.

```lean
theorem erdos_165 :
    (fun k : ℕ ↦ (R(3, k) : ℝ)) ~[atTop] erdos_165.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/165.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/165.lean#L60).

## `Erdos165.erdos_165.variants.conjecture`

Open: stated without proof.

> Campos, Jenssen, Michelen and Sahasrabudhe [CJMS25] and Hefty, Horn, King and Pfender [HHKP25]
> conjecture that $R(3,k) \sim \frac{k^2}{2\log k}$.

```lean
theorem erdos_165.variants.conjecture :
    (fun k : ℕ ↦ (R(3, k) : ℝ)) ~[atTop] (fun k : ℕ ↦ (k : ℝ) ^ 2 / (2 * Real.log k))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/165.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/165.lean#L69).

## `Erdos165.erdos_165.variants.upper`

Solved: stated here without proof.

> Shearer [Sh83] proved $R(3,k) \leq (1+o(1))\frac{k^2}{\log k}$.

```lean
theorem erdos_165.variants.upper :
    ∀ ε > (0 : ℝ), ∀ᶠ k : ℕ in atTop,
      (R(3, k) : ℝ) ≤ (1 + ε) * (k : ℝ) ^ 2 / Real.log k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/165.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/165.lean#L77).

## `Erdos165.erdos_165.variants.lower`

Solved: stated here without proof.

> Hefty, Horn, King and Pfender [HHKP25] proved $R(3,k) \geq (1/2+o(1))\frac{k^2}{\log k}$,
> improving earlier bounds of Kim [Ki95] and Campos, Jenssen, Michelen and Sahasrabudhe [CJMS25].

```lean
theorem erdos_165.variants.lower :
    ∀ ε > (0 : ℝ), ∀ᶠ k : ℕ in atTop,
      (1 / 2 - ε) * (k : ℝ) ^ 2 / Real.log k ≤ (R(3, k) : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/165.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/165.lean#L87).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/165.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/165.lean)
- [erdosproblems.com/165](https://www.erdosproblems.com/165)
