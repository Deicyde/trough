---
declaration: theorem
origin: cited
lean: Erdos422.erdos_422, Erdos422.erdos_422.variants.surjective, Erdos422.erdos_422.variants.growth_rate, Erdos422.erdos_422.variants.eventually_const, Erdos422.erdos_422.variants.well_defined
statement: formalized
---

# Erdős Problem 422

> *References:*
> - [erdosproblems.com/422](https://www.erdosproblems.com/422)
> - [OEIS A005185](https://oeis.org/A005185)

*Quoted from [FormalConjectures/ErdosProblems/422.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/422.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/422](https://www.erdosproblems.com/422).

The file states 5 research or textbook statements: 4 open and 1 textbook result. It also has 2 test statements and 1 API statement, counted here but not shown.

## `Erdos422.erdos_422`

Open: stated without proof.

> Let $f(1) = f(2) = 1$ and for $n > 2$
>
> $$
> f(n) = f(n - f(n - 1)) + f(n - f(n - 2)).
> $$
>
> Does $f(n)$ miss infinitely many integers?

```lean
theorem erdos_422 :
    ∀ f : ℕ+ → ℕ+, IsHofstadterQ f → Set.Infinite {n | ∀ x, f x ≠ n}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/422.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/422.lean#L78).

## `Erdos422.erdos_422.variants.surjective`

Open: stated without proof.

> Is $f$ surjective?

```lean
theorem erdos_422.variants.surjective :
    ∀ f : ℕ+ → ℕ+, IsHofstadterQ f → f.Surjective
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/422.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/422.lean#L86).

## `Erdos422.erdos_422.variants.growth_rate`

Open: stated without proof.

> How does $f$ grow?

```lean
theorem erdos_422.variants.growth_rate :
    ∀ f : ℕ+ → ℕ+, IsHofstadterQ f →
    (fun n ↦ (f n : ℝ)) =O[atTop] erdos_422.variants.growth_rate.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/422.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/422.lean#L96).

## `Erdos422.erdos_422.variants.eventually_const`

Textbook result, proved here.

> Does $f$ become stationary at some point?
>
> No: see `IsHofstadterQ.not_eventuallyConst`. The statement is existential, so the answer does
> not depend on whether $f(n)$ is well-defined for all $n$.

```lean
theorem erdos_422.variants.eventually_const :
    ¬ ∃ f : ℕ+ → ℕ+, IsHofstadterQ f ∧ EventuallyConst f atTop
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/422.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/422.lean#L133).

## `Erdos422.erdos_422.variants.well_defined`

Open: stated without proof.

> Is $f(n)$ well-defined for all $n$?

```lean
theorem erdos_422.variants.well_defined : ∃ f : ℕ+ → ℕ+, IsHofstadterQ f
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/422.lean, line 141](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/422.lean#L141).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/422.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/422.lean)
- [erdosproblems.com/422](https://www.erdosproblems.com/422)
