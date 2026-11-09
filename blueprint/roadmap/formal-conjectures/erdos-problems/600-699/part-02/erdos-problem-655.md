---
declaration: theorem
origin: cited
lean: Erdos655.erdos_655, Erdos655.erdos_655.variants.general_position
statement: formalized
---

# Erdős Problem 655

> *Reference:* [erdosproblems.com/655](https://www.erdosproblems.com/655)

*Quoted from [FormalConjectures/ErdosProblems/655.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/655.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/655](https://www.erdosproblems.com/655).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos655.erdos_655`

Solved: stated here; a Lean proof is at [https://github.com/AlperTheKing/formal-conjectures/blob/4aaaf544b6ed0ef22580787a8d8a19e85dc49556/FormalConjectures/ErdosProblems/655.lean](https://github.com/AlperTheKing/formal-conjectures/blob/4aaaf544b6ed0ef22580787a8d8a19e85dc49556/FormalConjectures/ErdosProblems/655.lean).

> Let $x_1,\ldots,x_n\in \mathbb{R}^2$ be such that no circle whose centre is one
> of the $x_i$ contains three other points. Are there at least
>
> $$(1+c)\frac{n}{2}$$
>
> distinct distances determined between the $x_i$, for some constant $c>0$ and
> all $n$ sufficiently large?
>
> The answer is **no**: as Zach Hunter observed, the regular `n`-gon (`n` points equally spaced on a
> circle) is valid and determines only `⌊n/2⌋ < (1+c)n/2` distinct distances, for every `c > 0`.
> (In the spirit of related conjectures of Erdős and others, presumably some kind of assumption that
> the points are in general position was intended; see `erdos_655.variants.general_position`.)
>
> The disproof — the regular `n`-gon construction together with its supporting lemmas — is formalised
> at the linked commit.

```lean
theorem erdos_655 :
    ¬ ∃ c > (0 : ℝ), ∀ᶠ n in atTop, ∀ (X : Finset ℝ²), #X = n → IsValid X →
      (1 + c) * n / 2 ≤ distinctDistances X
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/655.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/655.lean#L53).

## `Erdos655.erdos_655.variants.general_position`

Open: stated without proof.

> Let $x_1,\ldots,x_n\in \mathbb{R}^2$ be such that no circle whose centre is one
> of the $x_i$ contains three other points. Are there at least
>
> $$(1+c)\frac{n}{2}$$
>
> distinct distances determined between the $x_i$, for some constant $c>0$ and
> all $n$ sufficiently large?
>
> In the spirit of related conjectures of Erdős and others, presumably
> some kind of assumption that the points are in general position
> (e.g. no three on a line and no four on a circle) was intended.

```lean
theorem erdos_655.variants.general_position :
    ∃ c > (0 : ℝ), ∀ᶠ n in atTop, ∀ (X : Finset ℝ²), #X = n → IsValid X →
      InGeneralPosition X → (1 + c) * n / 2 ≤ distinctDistances X
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/655.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/655.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/655.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/655.lean)
- [erdosproblems.com/655](https://www.erdosproblems.com/655)
