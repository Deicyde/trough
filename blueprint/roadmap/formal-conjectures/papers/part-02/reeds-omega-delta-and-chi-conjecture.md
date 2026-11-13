---
declaration: theorem
origin: cited
lean: ReedOmegaDeltaChi.reed_omega_delta_chi_conjecture, ReedOmegaDeltaChi.reed_omega_delta_chi_conjecture_for_finite_graphs, ReedOmegaDeltaChi.reed_conjecture_Δ_6_ω_2
statement: formalized
---

# Reed's omega, delta, and chi conjecture

> *References*:
> - [B. Reed,  ω Δ and χ, J. Graph Theory 27 (1998) 177-212.](https://onlinelibrary.wiley.com/doi/10.1002/(SICI)1097-0118(199804)27:4%3C177::AID-JGT1%3E3.0.CO;2-K)
> - [openproblemgarden](http://www.openproblemgarden.org/op/reeds_omega_delta_and_chi_conjecture)
> - [mathoverflow/37923](https://mathoverflow.net/questions/37923) asked by user [Andrew D. King](https://mathoverflow.net/users/4580/andrew-d-king)

*Quoted from [FormalConjectures/Paper/ReedOmegaDeltaChi.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/ReedOmegaDeltaChi.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open.

## `ReedOmegaDeltaChi.reed_omega_delta_chi_conjecture`

Open: stated without proof.

> For a graph $G$, we define $\Delta(G)$ to be the maximum degree, $\omega(G)$ to be the size of the
> largest clique subgraph, and $\chi(G)$ to be the chromatic number. Reed's omega, delta, and chi
> conjecture states that
>
> $$\chi(G) \leq \lceil \frac{1}{2}(\omega(G) + \Delta(G) + 1) \rceil.$$

```lean
theorem reed_omega_delta_chi_conjecture :
  ∀ {V : Type} (G : SimpleGraph V),
    let χ := G.chromaticNumber
    let ω := G.ecliqueNum
    let Δ := G.emaxDegree
    2 * χ ≤ ω + Δ + 2
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/ReedOmegaDeltaChi.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/ReedOmegaDeltaChi.lean#L41).

## `ReedOmegaDeltaChi.reed_omega_delta_chi_conjecture_for_finite_graphs`

Open: stated without proof.

> For a finite graph $G$, we define $\Delta(G)$ to be the maximum degree, $\omega(G)$ to be the
> size of the largest clique subgraph, and $\chi(G)$ to be the chromatic number. Reed's omega,
> delta, and chi conjecture states that
>
> $$\chi(G) \leq \lceil \frac{1}{2}(\omega(G) + \Delta(G) + 1) \rceil.$$

```lean
theorem reed_omega_delta_chi_conjecture_for_finite_graphs :
  ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
    let χ := G.chromaticNumber
    let ω := G.cliqueNum
    let Δ := G.maxDegree
    2 * χ ≤ ω + Δ + 2
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/ReedOmegaDeltaChi.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/ReedOmegaDeltaChi.lean#L55).

## `ReedOmegaDeltaChi.reed_conjecture_Δ_6_ω_2`

Open: stated without proof.

> The simplest open case is when $\Delta(G) = 6$ and $\omega(G) = 2$.

```lean
theorem reed_conjecture_Δ_6_ω_2 :
  ∀ {V : Type} (G : SimpleGraph V), G.emaxDegree = 6 ∧ G.cliqueNum = 2 → G.chromaticNumber ≤ 5
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/ReedOmegaDeltaChi.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/ReedOmegaDeltaChi.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/ReedOmegaDeltaChi.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/ReedOmegaDeltaChi.lean)
- [B. Reed,  ω Δ and χ, J. Graph Theory 27 (1998) 177-212.](https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291097-0118%28199804%2927:4%3C177::AID-JGT1%3E3.0.CO;2-K)
