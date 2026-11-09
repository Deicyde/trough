---
declaration: lemma
origin: cited
lean: Falconer.falconer_conjecture_two, Falconer.falconer_conjecture
statement: formalized
---

# Falconer's distance set conjecture

> If $d \ge 2$ and $E \subseteq \mathbb{R}^d$ is compact with $\dim_H E > \frac{d}{2}$, then the
> distance set
>
> $$\{ |x - y| \mid x, y \in E \}$$
>
> has positive Lebesgue measure. The restriction $d \ge 2$ is needed; see `falconer_conjecture`.
>
> ## References
>
> * [K. Falconer, *On the Hausdorff dimensions of distance sets*](https://doi.org/10.1112/S0025579300010998)
> * [Wikipedia, *Falconer's conjecture*](https://en.wikipedia.org/wiki/Falconer%27s_conjecture)
> * [OAI26a] OpenAI, *The Falconer distance conjecture in all dimensions*.
>   OpenAI Math Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/paper.pdf

*Quoted from [FormalConjectures/Wikipedia/Falconer.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Falconer.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved.

## `Falconer.falconer_conjecture_two`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/MeasureTheory/Falconer/Main.lean#L50](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/MeasureTheory/Falconer/Main.lean#L50).

> Falconer's distance set conjecture, $d = 2$ case.
>
> This was proved by an internal OpenAI model in September 2026 [OAI26a]; see the linked Lean
> proof.

```lean
lemma falconer_conjecture_two (E : Set <| ℝ²) (hc : IsCompact E) (hd : 2 < 2 * dimH E ) :
    0 < volume (image2 dist E E)
```

Category `research solved`; AMS [28 Measure and integration](../../by-subject/part-01/28-measure-and-integration/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/Wikipedia/Falconer.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Falconer.lean#L52).

## `Falconer.falconer_conjecture`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/MeasureTheory/Falconer/Campaign123PlanarFurstenbergProof.lean#L47](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/MeasureTheory/Falconer/Campaign123PlanarFurstenbergProof.lean#L47).

> Falconer's distance set conjecture in dimension $d \ge 2$.
>
> The hypothesis $2 \le d$ excludes a degenerate case: the conclusion is false for $d = 1$.
> The base-$7$ Cantor set $E = \{\sum_{n \ge 1} a_n 7^{-n} : a_n \in \{0, 1, 2\}\}$ is compact
> with $\dim_H E = \log 3 / \log 7 > 1/2$, but $E - E$ has digits in $\{-2, \dots, 2\}$, so
> after fixing $n$ digits it is covered by $5^n$ intervals of length $\frac{2}{3} 7^{-n}$ and is
> therefore null; its distance set is the image of $E - E$ under $|\cdot|$ and is null too.
>
> This was proved by an internal OpenAI model in September 2026 [OAI26a]; see the linked Lean
> proof.

```lean
lemma falconer_conjecture (d : ℕ) (h2d : 2 ≤ d) (E : Set <| ℝ^d) (hc : IsCompact E)
    (hd : d < 2 * dimH E) :
    0 < volume (image2 dist E E)
```

Category `research solved`; AMS [28 Measure and integration](../../by-subject/part-01/28-measure-and-integration/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/Wikipedia/Falconer.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Falconer.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Falconer.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Falconer.lean)
- [K. Falconer, *On the Hausdorff dimensions of distance sets*](https://doi.org/10.1112/S0025579300010998)
