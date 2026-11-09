---
declaration: theorem
origin: cited
lean: Irrational.algebraicIndependent_e_pi, Irrational.irrational_e_plus_pi, Irrational.irrational_e_times_pi, Irrational.irrational_e_to_e, Irrational.irrational_pi_to_e, Irrational.irrational_pi_to_pi, Irrational.irrational_ln_pi, Irrational.irrational_eulerMascheroniConstant, Irrational.irrational_catalanConstant
statement: formalized
---

# Open questions on irrationality of numbers

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Irrational_number#Open_questions)
> - [OAI26a] OpenAI, *Catalan's constant is irrational*. OpenAI Math Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf

*Quoted from [FormalConjectures/Wikipedia/Irrational.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Irrational.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 9 research or textbook statements: 8 open and 1 solved.

## `Irrational.algebraicIndependent_e_pi`

Open: stated without proof.

> Are $e$ and $\pi$ algebraically independent?

```lean
theorem algebraicIndependent_e_pi :
    AlgebraicIndependent ℚ ![e, π]
```

Category `research open`; AMS [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Irrational.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Irrational.lean#L42).

## `Irrational.irrational_e_plus_pi`

Open: stated without proof.

> Is $e + \pi$ irrational?

```lean
theorem irrational_e_plus_pi :
    Irrational (e + π)
```

Category `research open`; AMS [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Irrational.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Irrational.lean#L50).

## `Irrational.irrational_e_times_pi`

Open: stated without proof.

> Is $e \pi$ irrational?

```lean
theorem irrational_e_times_pi :
    Irrational (e * π)
```

Category `research open`; AMS [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Irrational.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Irrational.lean#L58).

## `Irrational.irrational_e_to_e`

Open: stated without proof.

> Is $e ^ e$ irrational?

```lean
theorem irrational_e_to_e :
    Irrational (e ^ e)
```

Category `research open`; AMS [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Irrational.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Irrational.lean#L66).

## `Irrational.irrational_pi_to_e`

Open: stated without proof.

> Is $\pi ^ e$ irrational?

```lean
theorem irrational_pi_to_e :
    Irrational (π ^ e)
```

Category `research open`; AMS [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Irrational.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Irrational.lean#L74).

## `Irrational.irrational_pi_to_pi`

Open: stated without proof.

> Is $\pi ^ \pi$ irrational?

```lean
theorem irrational_pi_to_pi :
    Irrational (π ^ π)
```

Category `research open`; AMS [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Irrational.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Irrational.lean#L82).

## `Irrational.irrational_ln_pi`

Open: stated without proof.

> Is $\ln(\pi)$ irrational?

```lean
theorem irrational_ln_pi :
    Irrational (log π)
```

Category `research open`; AMS [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Irrational.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Irrational.lean#L90).

## `Irrational.irrational_eulerMascheroniConstant`

Open: stated without proof.

> Is the Euler-Mascheroni constant $\gamma$ irrational?

```lean
theorem irrational_eulerMascheroniConstant :
    Irrational eulerMascheroniConstant
```

Category `research open`; AMS [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Irrational.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Irrational.lean#L98).

## `Irrational.irrational_catalanConstant`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/Catalan/Results/Conclusions.lean#L11](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/Catalan/Results/Conclusions.lean#L11).

> Is the Catalan constant $$G = \sum_{n=0}^∞ (-1)^n / (2n + 1)^2 \approx 0.91596$$ irrational?
>
> This was proved by an internal OpenAI model in September 2026 [OAI26a]; see the linked Lean proof.

```lean
theorem irrational_catalanConstant :
    Irrational catalanConstant
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Irrational.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Irrational.lean#L110).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Irrational.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Irrational.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Irrational_number#Open_questions)
