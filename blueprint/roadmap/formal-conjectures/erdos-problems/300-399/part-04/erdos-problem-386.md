---
declaration: theorem
origin: cited
lean: Erdos386.erdos_386, Erdos386.erdos_386.variants.forall, Erdos386.erdos_386.variants.two
statement: formalized
---

# Erdős Problem 386

> *Reference:* [erdosproblems.com/386](https://www.erdosproblems.com/386)

*Quoted from [FormalConjectures/ErdosProblems/386.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/386.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/386](https://www.erdosproblems.com/386).

The file states 3 research or textbook statements: 3 open.

## `Erdos386.erdos_386`

Open: stated without proof.

> Let $2 \le k \le n - 2$. Can $\binom{n}{k}$ be the product of consecutive primes infinitely
> often? Here $k$ may vary with $n$: the question asks for infinitely many admissible binomial
> coefficients, not for a single $k$ that works infinitely often.

```lean
theorem erdos_386 :
    ∃ᶠ n in .atTop, ∃ k ≥ 2,
      k ≤ n - 2 ∧ ∃ p q : ℕ, n.choose k = ∏ i ∈ .Ico p q, nth Nat.Prime i
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/386.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/386.lean#L38).

## `Erdos386.erdos_386.variants.forall`

Open: stated without proof.

> For all $2 \le k \le n - 2$,
> can $\binom{n}{k}$ be the product of consecutive primes infinitely often?

```lean
theorem erdos_386.variants.forall :
    ∀ k ≥ 2, ∃ᶠ n in .atTop,
      k ≤ n - 2 ∧ ∃ p q : ℕ, n.choose k = ∏ i ∈ .Ico p q, nth Nat.Prime i
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/386.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/386.lean#L48).

## `Erdos386.erdos_386.variants.two`

Open: stated without proof.

> Can $\binom{n}{2}$ be the product of consecutive primes infinitely often?

```lean
theorem erdos_386.variants.two :
    ∃ᶠ n in .atTop,
      2 ≤ n - 2 ∧ ∃ p q : ℕ, n.choose 2 = ∏ i ∈ .Ico p q, nth Nat.Prime i
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/386.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/386.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/386.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/386.lean)
- [erdosproblems.com/386](https://www.erdosproblems.com/386)
