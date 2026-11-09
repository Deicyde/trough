---
declaration: theorem
origin: cited
lean: Erdos517.erdos_517, Erdos517.erdos_517.variants.fejer
statement: formalized
---

# Erdős Problem 517

> *References:*
>  - [erdosproblems.com/517](https://www.erdosproblems.com/517)
>  - [Bi28] Biernacki, Miécislas, Sur les équations algébriques contenant des paramétres arbitraires.
>     (1928), 145.

*Quoted from [FormalConjectures/ErdosProblems/517.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/517.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/517](https://www.erdosproblems.com/517).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos517.erdos_517`

Open: stated without proof.

> If `f(z) = ∑ aₖzⁿₖ` is an entire function (with `aₖ ≠ 0` for all `k`) such that `nₖ / k → ∞`,
> is it true that `f` assumes every value infinitely often?

```lean
theorem erdos_517 : ∀ {f : ℂ → ℂ} {n : ℕ → ℕ} (hn : HasFabryGaps n)
    {a : ℕ → ℂ} (ha : ∀ k, a k ≠ 0) (hf : ∀ z, HasSum (fun k => a k * z ^ n k) (f z)) (z : ℂ),
    {x : ℂ | f x = z}.Infinite
```

Category `research open`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/517.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/517.lean#L38).

## `Erdos517.erdos_517.variants.fejer`

Solved: stated here without proof.

> If `f(z) = ∑ aₖzⁿₖ` is an entire function (with `aₖ ≠ 0` for all `k`) such that `∑ 1 / nₖ < ∞`,
> then `f` assumes every value infinitely often. This theorem is proved in [Bi28].

```lean
theorem erdos_517.variants.fejer {f : ℂ → ℂ} {n : ℕ → ℕ} (hn : HasFejerGaps n) {a : ℕ → ℂ}
    (ha : ∀ k, a k ≠ 0) (hf : ∀ z, HasSum (fun k => a k * z ^ n k) (f z)) (z : ℂ) :
    {x : ℂ | f x = z}.Infinite
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/517.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/517.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/517.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/517.lean)
- [erdosproblems.com/517](https://www.erdosproblems.com/517)
