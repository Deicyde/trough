---
declaration: theorem
origin: cited
lean: Erdos467.erdos_467
statement: formalized
---

# Erdős Problem 467

> *Reference:* [erdosproblems.com/467](https://www.erdosproblems.com/467)

*Quoted from [FormalConjectures/ErdosProblems/467.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/467.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/467](https://www.erdosproblems.com/467).

The file states 1 research or textbook statement: 1 open.

## `Erdos467.erdos_467`

Open: stated without proof.

> For every sufficiently large $x$, choose a congruence class $a_p\pmod p$ for each prime $p\leq x$.
> Can the primes be decomposed into two nonempty sets $A$ and $B$ such that every $n\lt x$ lies in a
> chosen class from $A$ and in a chosen class from $B$?
>
> This follows the interpretation on the Erdős Problems website, which notes that the original
> source omits some crucial quantifiers.

```lean
theorem erdos_467 :
    ∀ᶠ x in atTop, ∃ residue : ℕ → ℕ, ∃ A B : Finset ℕ,
      PrimePartitionUpTo x A B ∧ CongruenceCover x residue A B
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/467.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/467.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/467.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/467.lean)
- [erdosproblems.com/467](https://www.erdosproblems.com/467)
