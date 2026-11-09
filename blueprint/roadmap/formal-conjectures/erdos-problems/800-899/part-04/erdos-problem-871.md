---
declaration: theorem
origin: cited
lean: Erdos871.erdos_871
statement: formalized
---

# Erdős Problem 871

> *References:*
> - [erdosproblems.com/871](https://www.erdosproblems.com/871)
> - [ErNa88] Erdős, Paul and Nathanson, Melvyn B., *Partitions of bases into disjoint unions of bases*. J. Number Theory (1988), 1-9.
> - [ErNa89] Erdős, Paul and Nathanson, Melvyn B., *Additive bases with many representations*. Acta Arith. (1989), 399-406.

*Quoted from [FormalConjectures/ErdosProblems/871.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/871.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/871](https://www.erdosproblems.com/871).

The file states 1 research or textbook statement: 1 solved.

## `Erdos871.erdos_871`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos871.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos871.lean).

> Let $A$ be an additive basis of order $2$, and suppose $1_A\ast 1_A(n)\to \infty$ as $n\to \infty$. Can $A$ be partitioned into two disjoint additive bases of order $2$?
>
> A question of Erdős and Nathanson [ErNa88], who proved this is true if $1_A\ast 1_A(n) > c\log n$ (for all large $n$) for some constant $c>(\log\frac{4}{3})^{-1}$. Erdős and Nathanson [ErNa89] also proved that for every $t$ there exists a basis $A$ of order $2$ such that $1_A\ast 1_A(n)\geq t$ for all large $n$ and yet $A$ cannot be partitioned into two disjoint additive bases. This has been disproved by Larsen using Claude Opus 4.5 - in fact only a small modification of the argument of [ErNa89] is required.

```lean
theorem erdos_871 :
    ¬ ∀ (A : Set ℕ),
      (∀ᶠ n in Filter.atTop, ∃ a ∈ A, ∃ b ∈ A, a + b = n) ∧
      (∀ t, ∀ᶠ n in Filter.atTop, ∃ pairs : Finset (ℕ × ℕ),
        pairs.card ≥ t ∧
          ∀ p ∈ pairs, p.1 ∈ A ∧ p.2 ∈ A ∧ p.1 + p.2 = n ∧ p.1 ≤ p.2) →
      ∃ (B C : Set ℕ),
        (∀ x, x ∈ A ↔ x ∈ B ∨ x ∈ C) ∧
        Disjoint B C ∧
        (∀ᶠ n in Filter.atTop, ∃ a ∈ B, ∃ b ∈ B, a + b = n) ∧
        (∀ᶠ n in Filter.atTop, ∃ a ∈ C, ∃ b ∈ C, a + b = n)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/871.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/871.lean#L40).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/871.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/871.lean)
- [erdosproblems.com/871](https://www.erdosproblems.com/871)
