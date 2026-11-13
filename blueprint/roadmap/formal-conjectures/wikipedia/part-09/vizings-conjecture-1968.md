---
declaration: theorem
origin: cited
lean: VizingConjecture.vizing_conjecture, VizingConjecture.vizing_conjecture.variants.clark_suen, VizingConjecture.vizing_conjecture.variants.suen_tarr, VizingConjecture.vizing_conjecture.variants.dominationNumber_eq_one
statement: formalized
---

# Vizing's conjecture (1968)

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Vizing%27s_conjecture)
> * [Vi68] Vizing, V. G. (1968). "Some unsolved problems in graph theory."
>   *Uspekhi Mat. Nauk* 23, pp. 117--134.
> * [ClSu00] Clark, W. E. and Suen, S. (2000). "An inequality related to Vizing's conjecture."
>   *Electron. J. Combin.* 7, N4.
> * [SuTa12] Suen, S. and Tarr, J. (2012). "An improved inequality related to Vizing's conjecture."
>   *Electron. J. Combin.* 19, P8.
> * [BDGHHKR12] Brešar, B., Dorbec, P., Goddard, W., Hartnell, B. L., Henning, M. A., Klavžar, S.
>   and Rall, D. F. (2012). "Vizing's conjecture: a survey and recent results."
>   *J. Graph Theory* 69, pp. 46--76.

*Quoted from [FormalConjectures/Wikipedia/VizingConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/VizingConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 solved.

## `VizingConjecture.vizing_conjecture`

Open: stated without proof.

> **Vizing's conjecture (1968).**
>
> For all finite simple graphs $G$ and $H$, the domination number of the Cartesian (box)
> product satisfies $\gamma(G \,\square\, H) \ge \gamma(G)\,\gamma(H)$.

```lean
theorem vizing_conjecture :
    ∀ {α β : Type} [Fintype α] [Fintype β] [DecidableEq α] [DecidableEq β]
      (G : SimpleGraph α) (H : SimpleGraph β),
      G.dominationNumber * H.dominationNumber ≤ (G □ H).dominationNumber
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/VizingConjecture.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/VizingConjecture.lean#L49).

## `VizingConjecture.vizing_conjecture.variants.clark_suen`

Solved: stated here without proof.

> **The Clark–Suen inequality (2000).**
>
> For all finite simple graphs $G$ and $H$,
> $\gamma(G \,\square\, H) \ge \tfrac12\,\gamma(G)\,\gamma(H)$; that is, Vizing's conjecture holds
> up to a factor of $2$.
>
> *Reference:* [ClSu00].

```lean
theorem vizing_conjecture.variants.clark_suen
    {α β : Type} [Fintype α] [Fintype β] [DecidableEq α] [DecidableEq β]
    (G : SimpleGraph α) (H : SimpleGraph β) :
    G.dominationNumber * H.dominationNumber ≤ 2 * (G □ H).dominationNumber
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/VizingConjecture.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/VizingConjecture.lean#L65).

## `VizingConjecture.vizing_conjecture.variants.suen_tarr`

Solved: stated here without proof.

> **The Suen–Tarr inequality (2012).**
>
> For all finite simple graphs $G$ and $H$,
> $\gamma(G \,\square\, H) \ge \tfrac12\,\gamma(G)\,\gamma(H) +
> \tfrac12\min\{\gamma(G), \gamma(H)\}$, improving the Clark–Suen bound.
>
> *Reference:* [SuTa12].

```lean
theorem vizing_conjecture.variants.suen_tarr
    {α β : Type} [Fintype α] [Fintype β] [DecidableEq α] [DecidableEq β]
    (G : SimpleGraph α) (H : SimpleGraph β) :
    G.dominationNumber * H.dominationNumber + min G.dominationNumber H.dominationNumber ≤
      2 * (G □ H).dominationNumber
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/VizingConjecture.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/VizingConjecture.lean#L81).

## `VizingConjecture.vizing_conjecture.variants.dominationNumber_eq_one`

Proved here.

> **Vizing's conjecture when `γ(H) = 1`.**
>
> If `H` has a dominating vertex, so that $\gamma(H) = 1$, then Vizing's inequality reduces to
> $\gamma(G) \le \gamma(G \,\square\, H)$, which is the projection bound
> `dominationNumber_le_dominationNumber_boxProd`. This is the simplest of the known cases of the
> conjecture (see [BDGHHKR12]).

```lean
theorem vizing_conjecture.variants.dominationNumber_eq_one
    {α β : Type} [Fintype α] [Fintype β] [DecidableEq α] [DecidableEq β]
    (G : SimpleGraph α) (H : SimpleGraph β) (hH : H.dominationNumber = 1) :
    G.dominationNumber * H.dominationNumber ≤ (G □ H).dominationNumber
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/VizingConjecture.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/VizingConjecture.lean#L97).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/VizingConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/VizingConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Vizing%27s_conjecture)
