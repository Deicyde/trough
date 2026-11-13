---
declaration: theorem
origin: cited
lean: Erdos25.erdos_25
statement: formalized
---

# Erdős Problem 25: Logarithmic density of size-dependent congruences

> *Reference:* [erdosproblems.com/25](https://www.erdosproblems.com/25)

*Quoted from [FormalConjectures/ErdosProblems/25.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/25.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/25](https://www.erdosproblems.com/25).

The file states 1 research or textbook statement: 1 open.

## `Erdos25.erdos_25`

Open: stated without proof.

> Let $n_1 < n_2 < \dots$ be an arbitrary sequence of integers, each with an associated residue class
> $a_i \pmod{n_i}$. Let $A$ be the set of integers $n$ such that for every $i$ either $n < n_i$ or
> $n \not\equiv a_i \pmod{n_i}$. Must the logarithmic density of $A$ exist?

```lean
theorem erdos_25 :
    ∀ (seq_n : ℕ → ℕ) (seq_a : ℕ → ℤ), (∀ i, 0 < seq_n i) → StrictMono seq_n →
      ∃ d, Set.HasLogDensity
        { x : ℕ | ∀ i, (x : ℤ) < seq_n i ∨ ¬((x : ℤ) ≡ seq_a i [ZMOD seq_n i]) } d
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/25.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/25.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/25.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/25.lean)
- [erdosproblems.com/25](https://www.erdosproblems.com/25)
