---
declaration: theorem
origin: cited
lean: LennonPittel.lennon_pittel_conjecture
statement: formalized
---

# Lennon–Pittel conjecture on random stable matchings

> *References:*
> - [On the Likely Number of Stable Marriages](https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1194991095&disposition=inline)
>   by *Craig Lennon*, PhD dissertation, The Ohio State University (2007).
> - [On the Likely Number of Solutions for the Stable Marriage Problem](https://doi.org/10.1017/S0963548308009607)
>   by *Craig Lennon and Boris Pittel*, *Combinatorics, Probability and Computing* 18 (2009),
>   371–421.
>
> Let $S_n$ be the number of stable matchings under uniformly random complete strict preferences.

*Quoted from [FormalConjectures/Paper/LennonPittelStableMatchings.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LennonPittelStableMatchings.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 1 test statement, counted here but not shown.

## `LennonPittel.lennon_pittel_conjecture`

Open: stated without proof.

> The [Lennon–Pittel conjecture](https://doi.org/10.1017/S0963548308009607) states that for every
> positive nonincreasing sequence $\varepsilon_n \to 0$, the probability that the number $S_n$ of
> stable matchings is at least $\varepsilon_n \mathbb{E}[S_n]$ tends to one.

```lean
theorem lennon_pittel_conjecture
    (ε : ℕ → ℝ) (hε_pos : ∀ n, 0 < ε n) (hε_antitone : Antitone ε)
    (hε_tendsto : Tendsto ε atTop (𝓝 0)) :
    Tendsto
      (fun n ↦
        (StableMarriage.uniformProfile n).toMeasure
          {p | (StableMarriage.numStableMatchings p : ℝ) ≥
            ε n * StableMarriage.expectedNumStableMatchings n})
      atTop (𝓝 1)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/Paper/LennonPittelStableMatchings.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LennonPittelStableMatchings.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/LennonPittelStableMatchings.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LennonPittelStableMatchings.lean)
- [On the Likely Number of Stable Marriages](https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1194991095&disposition=inline)
