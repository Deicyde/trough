---
declaration: theorem
origin: cited
lean: Erdos304.erdos_304.variants.upper_1950, Erdos304.erdos_304.variants.lower_1950, Erdos304.erdos_304.variants.upper_1985, Erdos304.upper_bound
statement: formalized
---

# Erdős Problem 304

> *Reference:* [erdosproblems.com/304](https://www.erdosproblems.com/304)
>
> [OAI26a] OpenAI, *Short Egyptian fractions*. OpenAI Math Release preprint (2026).
> https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Short-Egyptian-fractions-September-25-2026/Short-Egyptian-fractions-September-25-2026.pdf

*Quoted from [FormalConjectures/ErdosProblems/304.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/304.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/304](https://www.erdosproblems.com/304).

The file states 4 research or textbook statements: 4 solved. It also has 1 test statement and 11 API statements, counted here but not shown.

## `Erdos304.erdos_304.variants.upper_1950`

Solved: stated here without proof.

> In 1950, Erdős [Er50c] proved the upper bound $$N(b) \ll \log b / \log \log b$$.
> [Er50c] Erdős, P., Az ${1}/{x_1} + {1}/{x_2} + \ldots + {1}/{x_n} =A/B$ egyenlet eg\'{E}sz sz\'{A}m\'{u} megold\'{A}sairól. Mat. Lapok (1950), 192-210.

```lean
theorem erdos_304.variants.upper_1950 :
    (fun b => (smallestCollectionTo b : ℝ)) =O[atTop]
      (fun b => Real.log b / Real.log (Real.log b))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/304.lean, line 150](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/304.lean#L150).

## `Erdos304.erdos_304.variants.lower_1950`

Solved: stated here; a Lean proof is at [https://github.com/thepriceisright/publications/blob/8f055eb3fd1485477c92cbfbdfa4b3c56f192610/erdos/304/Lower1950.lean](https://github.com/thepriceisright/publications/blob/8f055eb3fd1485477c92cbfbdfa4b3c56f192610/erdos/304/Lower1950.lean).

> In 1950, Erdős [Er50c] proved the lower bound $$\log \log b \ll N(b)$$.
> [Er50c] Erdős, P., Az ${1}/{x_1} + {1}/{x_2} + \ldots + {1}/{x_n} =A/B$ egyenlet eg\'{E}sz sz\'{A}m\'{u} megold\'{A}sairól. Mat. Lapok (1950), 192-210.

```lean
theorem erdos_304.variants.lower_1950 :
    (fun b : ℕ => Real.log (Real.log b)) =O[atTop]
      (fun b => (smallestCollectionTo b : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/304.lean, line 161](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/304.lean#L161).

## `Erdos304.erdos_304.variants.upper_1985`

Solved: stated here without proof.

> In 1985 Vose [Vo85] proved the upper bound $$N(b) \ll \sqrt{\log b}$$.
> [Vo85] Vose, Michael D., Egyptian fractions. Bull. London Math. Soc. (1985), 21-24.

```lean
theorem erdos_304.variants.upper_1985 :
    (fun b => (smallestCollectionTo b : ℝ)) =O[atTop]
      (fun b => Real.sqrt (Real.log b))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/304.lean, line 171](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/304.lean#L171).

## `Erdos304.upper_bound`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/ShortEgyptian/Main.lean#L33](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/ShortEgyptian/Main.lean#L33).

> Is it true that $$N(b) \ll \log \log b$$?
>
> Yes. This was proved by an internal OpenAI model in September 2026 [OAI26a]; see the linked
> Lean proof.

```lean
theorem upper_bound :
    (fun b : ℕ => (smallestCollectionTo b : ℝ)) =O[atTop] (fun b : ℕ => Real.log (Real.log b))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/304.lean, line 185](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/304.lean#L185).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/304.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/304.lean)
- [erdosproblems.com/304](https://www.erdosproblems.com/304)
