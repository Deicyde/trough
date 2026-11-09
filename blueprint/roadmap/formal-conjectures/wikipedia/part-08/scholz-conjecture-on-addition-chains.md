---
declaration: theorem
origin: cited
lean: ScholzConjecture.scholz_conjecture
statement: formalized
---

# Scholz conjecture on addition chains

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Scholz_conjecture)
> - [MathWorld](https://mathworld.wolfram.com/ScholzConjecture.html)
> - [Tall22](https://arxiv.org/abs/2210.13812) Amadou Tall. "The Scholz conjecture on addition
>   chain is true for infinitely many integers with $\ell(2n) = \ell(n)$." _arXiv:2210.13812_ (2022).
>   Also available as [ePrint 2023/020](https://eprint.iacr.org/2023/020).
> - [OEIS A003313](https://oeis.org/A003313)

*Quoted from [FormalConjectures/Wikipedia/ScholzConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ScholzConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 1 test statement, counted here but not shown.

## `ScholzConjecture.scholz_conjecture`

Open: stated without proof.

> The Scholz conjecture, also known as the Scholz-Brauer conjecture, asserts that
> for every positive integer $n$, the addition-chain length of $2^n - 1$ is at most
> $n - 1 + \ell(n)$.

```lean
theorem scholz_conjecture :
    ∀ (n : ℕ), 0 < n → ℓ(2 ^ n - 1) ≤ n - 1 + ℓ(n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Wikipedia/ScholzConjecture.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ScholzConjecture.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ScholzConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ScholzConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Scholz_conjecture)
