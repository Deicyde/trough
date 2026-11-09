---
declaration: theorem
origin: cited
lean: BrennanConjecture.brennan_universalSpectrum, BrennanConjecture.brennan_universalSpectrumBounded
statement: formalized
---

# Brennan's Conjecture

> *Reference:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Brennan_conjecture)
> - [arXiv:2409.15074](https://arxiv.org/abs/2409.15074)
> - [arXiv:2512.09330](https://arxiv.org/abs/2512.09330)
> - [OAI26a] OpenAI, *Brennan's conjecture and sharp inverse-square integral means*.
>   OpenAI Math Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/paper.pdf

*Quoted from [FormalConjectures/Wikipedia/Brennanconjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Brennanconjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 test statement and 3 API statements, counted here but not shown.

## `BrennanConjecture.brennan_universalSpectrum`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Analysis/IntegralMeans/Main.lean#L10](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Analysis/IntegralMeans/Main.lean#L10).

> Brennan's conjecture, part 1: $B(-2) = 1$.
>
> This was proved by an internal OpenAI model in September 2026 [OAI26a]; see the linked Lean
> proof.

```lean
theorem brennan_universalSpectrum :
    universalSpectrum (-2) = 1
```

Category `research solved`; AMS [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/Wikipedia/Brennanconjecture.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Brennanconjecture.lean#L88).

## `BrennanConjecture.brennan_universalSpectrumBounded`

Open: stated without proof.

> Brennan's conjecture, part 2: $B_b(-2) = 1$.

```lean
theorem brennan_universalSpectrumBounded :
    universalSpectrumBounded (-2) = 1
```

Category `research open`; AMS [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/Wikipedia/Brennanconjecture.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Brennanconjecture.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Brennanconjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Brennanconjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Brennan_conjecture)
