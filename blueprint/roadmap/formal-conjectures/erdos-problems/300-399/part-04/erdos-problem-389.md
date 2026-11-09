---
declaration: theorem
origin: cited
lean: Erdos389.erdos_389, Erdos389.erdos_389.variants.mehta_four
statement: formalized
---

# Erdős Problem 389

> *Reference:* [erdosproblems.com/389](https://www.erdosproblems.com/389)

*Quoted from [FormalConjectures/ErdosProblems/389.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/389.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/389](https://www.erdosproblems.com/389).

The file states 2 research or textbook statements: 1 open and 1 textbook result.

## `Erdos389.erdos_389`

Open: stated without proof.

> Is it true that for every $n \geq 1$ there is a $k$ such that
>
> $$
>   n(n + 1) \cdots (n + k - 1) \mid (n + k) \cdots (n + 2k - 1)?
> $$

```lean
theorem erdos_389 :
    ∀ n ≥ 1, ∃ k ≥ 1, ∏ i ∈ Finset.range k, (n + i) ∣ ∏ i ∈ Finset.range k, (n + k + i)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/389.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/389.lean#L37).

## `Erdos389.erdos_389.variants.mehta_four`

Textbook result, proved here.

> Bhavik Mehta has computed the minimal such $k$ for $1 \leq n \leq 18$.
> For example, the minimal $k$ for $n = 4$ is $207$.

```lean
theorem erdos_389.variants.mehta_four :
    IsLeast
      { k | 1 ≤ k ∧ ∏ i ∈ Finset.range k, (4 + i) ∣ ∏ i ∈ Finset.range k, (4 + k + i) }
      207
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/389.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/389.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/389.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/389.lean)
- [erdosproblems.com/389](https://www.erdosproblems.com/389)
