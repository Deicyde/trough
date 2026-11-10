---
declaration: theorem
origin: cited
lean: Erdos508.HadwigerNelsonProblem, Erdos508.HadwigerNelsonAtLeastFive, Erdos508.HadwigerNelsonAtLeastSix, Erdos508.HadwigerNelsonAtLeast4, Erdos508.HadwigerNelsonAtMostSeven, Erdos508.HadwigerNelsonAtLeastThree
statement: formalized
---

# Erdős Problem 508

> *Reference:* [erdosproblems.com/508](https://www.erdosproblems.com/508)
>
> proven by considering the [Moser-Spindel graph]
> or the [Golomb graph]
> *At least 4 colors are required:* [Moser-Spindel graph](https://de.wikipedia.org/wiki/Moser-Spindel)
> *At least 4 colors are required:* [Golomb graph](https://en.wikipedia.org/wiki/Golomb_graph)
> *At least 5 colors are required:* [de Grey 2018](https://arxiv.org/abs/1804.02385)
> *At least 6 colors are required, and 7 colors suffice:* [OAI26]
>
> - [OAI26] OpenAI, *The Euclidean plane is not five-colorable*. OpenAI Math Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/paper.pdf

*Quoted from [FormalConjectures/ErdosProblems/508.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/508.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/508](https://www.erdosproblems.com/508).

The file states 6 research or textbook statements: 1 open, 3 solved and 2 textbook results.

## `Erdos508.HadwigerNelsonProblem`

Open: stated without proof.

> The Hadwiger–Nelson problem asks: How many colors are required to color the plane
> such that no two points at distance 1 from each other have the same color?
>
> It is known that $6 \leq \chi(\mathbb{R}^2) \leq 7$; see `HadwigerNelsonAtLeastSix` and
> `HadwigerNelsonAtMostSeven`.

```lean
theorem HadwigerNelsonProblem :
    χ(ℝ²) = HadwigerNelsonProblem.answer
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/508.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/508.lean#L55).

## `Erdos508.HadwigerNelsonAtLeastFive`

Solved: stated here without proof.

> Aubrey de Grey improved the lower bound for the chromatic number of the plane
> to 5 in 2018 using a graph that has >1000 nodes.
>
> "The chromatic number of the plane is at least 5" Aubrey D. N. J. de Grey, 2018
> (https://doi.org/10.48550/arXiv.1804.02385)

```lean
theorem HadwigerNelsonAtLeastFive :
    5 ≤ χ(ℝ²)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/508.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/508.lean#L67).

## `Erdos508.HadwigerNelsonAtLeastSix`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Geometry/PlaneColoring/Five.lean#L124](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Geometry/PlaneColoring/Five.lean#L124).

> The chromatic number of the plane is at least 6: there is no proper 5-colouring of the plane.
>
> This was proved by an internal OpenAI model in September 2026 [OAI26]; see the linked Lean proof.

```lean
theorem HadwigerNelsonAtLeastSix :
    6 ≤ χ(ℝ²)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/508.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/508.lean#L79).

## `Erdos508.HadwigerNelsonAtLeast4`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/394ec1c1ff92bdf2fa10f30d62ae9d0455d3ce20/Proofs/T_Erdos508_HadwigerNelsonAtLeast4.lean#L88](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/394ec1c1ff92bdf2fa10f30d62ae9d0455d3ce20/Proofs/T_Erdos508_HadwigerNelsonAtLeast4.lean#L88).

> The "chromatic number of the plane" is at least 4. This can be
> proven by considering the [Moser-Spindel graph](https://de.wikipedia.org/wiki/Moser-Spindel)
> or the [Golomb graph](https://en.wikipedia.org/wiki/Golomb_graph) graph.

```lean
theorem HadwigerNelsonAtLeast4 : 4 ≤ χ(ℝ²)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/508.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/508.lean#L90).

## `Erdos508.HadwigerNelsonAtMostSeven`

Textbook result, stated without proof. A Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Geometry/PlaneColoring/Seven.lean#L36](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Geometry/PlaneColoring/Seven.lean#L36).

> This upper bound for the chromatic number of the plane was
> observed by John R. Isbell. His approach was dividing the
> plane into hexagons of uniform size and coloring them with a repeating
> pattern. A proof can probably be found in:
>
> Soifer, Alexander (2008), The Mathematical Coloring Book: Mathematics of Coloring and the Colorful Life of its Creators, New York: Springer, ISBN 978-0-387-74640-1
>
> An alternative approach that uses square tiling was highlighted by László Székely.
>
> The linked Lean proof of this bound is part of the OpenAI release [OAI26].

```lean
theorem HadwigerNelsonAtMostSeven :
    χ(ℝ²) ≤ 7
```

Category `textbook`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/508.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/508.lean#L107).

## `Erdos508.HadwigerNelsonAtLeastThree`

Textbook result, proved here.

> The chromatic number of the plane is at least 3.
>
> This is proven by considering an equilateral triangle in the plane.

```lean
theorem HadwigerNelsonAtLeastThree : 3 ≤ χ(ℝ²)
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/508.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/508.lean#L115).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/508.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/508.lean)
- [erdosproblems.com/508](https://www.erdosproblems.com/508)
