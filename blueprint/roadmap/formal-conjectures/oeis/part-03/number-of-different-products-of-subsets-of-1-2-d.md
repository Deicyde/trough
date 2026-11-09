---
declaration: theorem
origin: cited
lean: OeisA60957.counterexample, OeisA60957.conjecture
statement: formalized
---

# Number of different products of subsets of $\{1, 2, \dots, n\}$

> The number of distinct products (including the empty product 1) of any subset
> of $\{1, 2, \dots, n\}$.
>
> *References:*
> - [A060957](https://oeis.org/A060957)
> - [Li26] Wentao Li, [A counterexample to the A060957 interpolation conjecture](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/3be119e75ba5b31f034dc0c0b249975d17def711/proofs/new-proofs/A060957/PROOF.md), 2026.

*Quoted from [FormalConjectures/OEIS/60957.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/60957.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 6 test statements, counted here but not shown.

## `OeisA60957.counterexample`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/3be119e75ba5b31f034dc0c0b249975d17def711/LeanOeisProofs/NewProofs/A060957.lean#L1479](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/3be119e75ba5b31f034dc0c0b249975d17def711/LeanOeisProofs/NewProofs/A060957.lean#L1479).

> An explicit counterexample from [Li26]: both endpoint products occur, but the intermediate
> product with exponent $5$ does not. The definitions above specify every parameter, including
> `Counterexample.circuitM` as a finite product.

```lean
theorem counterexample :
    Counterexample.circuitPrime.Prime ∧ Counterexample.circuitPrime ≤ Counterexample.circuitN ∧
    Counterexample.circuitM ∈ productsOfSubsets Counterexample.circuitN ∧
    Counterexample.circuitPrime ^ 6 * Counterexample.circuitM ∈
      productsOfSubsets Counterexample.circuitN ∧
    0 < (5 : ℕ) ∧ 5 < (6 : ℕ) ∧
    Counterexample.circuitPrime ^ 5 * Counterexample.circuitM ∉
      productsOfSubsets Counterexample.circuitN
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/60957.lean, line 159](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/60957.lean#L159).

## `OeisA60957.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-oeis-proofs/blob/3be119e75ba5b31f034dc0c0b249975d17def711/LeanOeisProofs/NewProofs/A060957.lean#L1499](https://github.com/VictorLiwentao/lean-oeis-proofs/blob/3be119e75ba5b31f034dc0c0b249975d17def711/LeanOeisProofs/NewProofs/A060957.lean#L1499).

> Conjecture: let $p \le n$ be prime. If $m$ and $p^a m$ are two such products, then so is $p^k m$
> for all $0 < k < a$.
> - Yan Sheng Ang, Feb 13 2020
>
> This interpolation conjecture is false. Disproved by Wentao Li (2026), with AI assistance;
> see [Li26]. The counterexample has
> $p = 7 \cdot 2^{120} + 1$, $n = p \cdot 2^{189}$, $a = 6$, and $k = 5$.

```lean
theorem conjecture :
    ¬ ∀ (n p : ℕ), p.Prime → p ≤ n →
      ∀ (m a_exp : ℕ), m ∈ productsOfSubsets n → p ^ a_exp * m ∈ productsOfSubsets n →
        ∀ k : ℕ, 0 < k → k < a_exp → p ^ k * m ∈ productsOfSubsets n
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/60957.lean, line 181](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/60957.lean#L181).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/60957.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/60957.lean)
- [A060957](https://oeis.org/A060957)
