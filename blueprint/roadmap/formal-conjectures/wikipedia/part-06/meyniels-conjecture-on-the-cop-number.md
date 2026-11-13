---
declaration: theorem
origin: cited
lean: MeynielConjecture.meyniel_conjecture, MeynielConjecture.meyniel_conjecture.variants.soft, MeynielConjecture.meyniel_conjecture.variants.scott_sudakov, MeynielConjecture.meyniel_conjecture.variants.tree
statement: formalized
---

# Meyniel's conjecture on the cop number

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Cop_number)
> * [Fr87] Frankl, P. (1987). "Cops and robbers in graphs with large girth and Cayley graphs."
>   *Discrete Appl. Math.* 17, pp. 301--305.
> * [NW83] Nowakowski, R. and Winkler, P. (1983). "Vertex-to-vertex pursuit in a graph."
>   *Discrete Math.* 43, pp. 235--239.
> * [SS11] Scott, A. and Sudakov, B. (2011). "A bound for the cops and robbers problem."
>   *SIAM J. Discrete Math.* 25, pp. 1438--1442.
> * [BB12] Baird, W. and Bonato, A. (2012). "Meyniel's conjecture on the cop number: a survey."
>   *J. Comb.* 3, pp. 225--238.

*Quoted from [FormalConjectures/Wikipedia/MeynielConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MeynielConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open and 2 solved. It also has 2 test statements and 4 API statements, counted here but not shown.

## `MeynielConjecture.meyniel_conjecture`

Open: stated without proof.

> **Meyniel's conjecture (c. 1985).**
>
> There is a universal constant `C` such that every connected graph on `n` vertices has cop
> number at most `C √n`: a team of `O(√n)` cops can always catch the robber in the game of cops
> and robbers. The conjecture was communicated by Meyniel to Frankl and first appeared in
> [Fr87]; see [BB12] for a survey.

```lean
theorem meyniel_conjecture :
    ∃ C : ℝ, 0 < C ∧ ∀ (V : Type) [Fintype V] (G : SimpleGraph V), G.Connected →
      (copNumber G : ℝ) ≤ C * Real.sqrt (Fintype.card V)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [91 Game theory, economics, social and behavioral sciences](../../by-subject/part-03/91-game-theory-economics-social-and-behavioral-scie/README.md). Declared in [FormalConjectures/Wikipedia/MeynielConjecture.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MeynielConjecture.lean#L113).

## `MeynielConjecture.meyniel_conjecture.variants.soft`

Open: stated without proof.

> **The soft Meyniel conjecture.**
>
> There are constants `ε, C > 0` such that every connected graph on `n` vertices has cop number
> at most `C n^(1 - ε)`. Even this weakening of Meyniel's conjecture is open; no bound of the
> form `O(n^(1 - ε))` is known. See [BB12].

```lean
theorem meyniel_conjecture.variants.soft :
    ∃ ε C : ℝ, 0 < ε ∧ 0 < C ∧ ∀ (V : Type) [Fintype V] (G : SimpleGraph V), G.Connected →
      (copNumber G : ℝ) ≤ C * (Fintype.card V : ℝ) ^ ((1 : ℝ) - ε)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [91 Game theory, economics, social and behavioral sciences](../../by-subject/part-03/91-game-theory-economics-social-and-behavioral-scie/README.md). Declared in [FormalConjectures/Wikipedia/MeynielConjecture.lean, line 126](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MeynielConjecture.lean#L126).

## `MeynielConjecture.meyniel_conjecture.variants.scott_sudakov`

Solved: stated here without proof.

> **Scott–Sudakov (2011): the best known general bound.**
>
> Every connected graph on `n` vertices has cop number at most `n / 2^((1 - o(1)) √(log₂ n))`.
> This (together with the same bound obtained independently by Lu–Peng and by Frieze, Krivelevich
> and Loh) is the best known bound towards Meyniel's conjecture.
>
> *Reference:* [SS11].

```lean
theorem meyniel_conjecture.variants.scott_sudakov :
    ∃ f : ℕ → ℝ, Tendsto f atTop (nhds 0) ∧
      ∀ (V : Type) [Fintype V] (G : SimpleGraph V), G.Connected →
        (copNumber G : ℝ) ≤ (Fintype.card V : ℝ) /
          2 ^ ((1 - f (Fintype.card V)) * Real.sqrt (Real.logb 2 (Fintype.card V)))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [91 Game theory, economics, social and behavioral sciences](../../by-subject/part-03/91-game-theory-economics-social-and-behavioral-scie/README.md). Declared in [FormalConjectures/Wikipedia/MeynielConjecture.lean, line 141](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MeynielConjecture.lean#L141).

## `MeynielConjecture.meyniel_conjecture.variants.tree`

Solved: stated here without proof.

> **Trees are cop-win (Nowakowski–Winkler 1983).**
>
> Every nonempty tree has cop number `1`: a single cop, always moving towards the robber, catches
> the robber on any connected acyclic graph. More generally, the cop-win graphs are exactly the
> dismantlable graphs.
>
> *Reference:* [NW83].

```lean
theorem meyniel_conjecture.variants.tree {V : Type} [Fintype V] [Nonempty V]
    (G : SimpleGraph V) (hc : G.Connected) (ha : G.IsAcyclic) :
    copNumber G = 1
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [91 Game theory, economics, social and behavioral sciences](../../by-subject/part-03/91-game-theory-economics-social-and-behavioral-scie/README.md). Declared in [FormalConjectures/Wikipedia/MeynielConjecture.lean, line 158](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MeynielConjecture.lean#L158).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/MeynielConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MeynielConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Cop_number)
