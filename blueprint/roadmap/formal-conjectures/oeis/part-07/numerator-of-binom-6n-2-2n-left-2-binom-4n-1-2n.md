---
declaration: theorem
origin: cited
lean: OeisA109074.conjecture
statement: formalized
---

# Numerator of $\binom{6n-2}{2n} / \left(2 \binom{4n-1}{2n}\right)$

> The sequence $a(n)$ is the numerator of $\binom{6n-2}{2n} / \left(2 \binom{4n-1}{2n}\right)$.
> The OEIS entry records the conjecture that this ratio equals $\text{A005156}(n) / \text{A005156}(n-1)$,
> where $\text{A005156}(n)$ is the number of $(2n+1) \times (2n+1)$ vertically symmetric alternating
> sign matrices (VSASMs). This follows from Robbins's VSASM product formula, proved by Kuperberg
> (2002).
>
> *References:*
> - [A109074](https://oeis.org/A109074)
> - [A005156](https://oeis.org/A005156)
> - G. Kuperberg, "Symmetry classes of alternating-sign matrices under one roof,"
>   [arXiv:math/0008184](https://arxiv.org/abs/math/0008184), *Ann. of Math.* **156** (2002),
>   835–866.

*Quoted from [FormalConjectures/OEIS/109074.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109074.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 10 test statements, counted here but not shown.

## `OeisA109074.conjecture`

Solved: stated here without proof.

> "It is conjectured that $\binom{6n-2}{2n} / \left(2 \binom{4n-1}{2n}\right) =
> \text{A005156}(n+1)/\text{A005156}(n)$."
>
> The OEIS comment indexes A005156 from $1$; for the $0$-indexed sequence `b` this states
> `frac (n + 1) = b (n + 1) / b n`. This holds by the product formula
> $$\text{A005156}(n) = \frac{1}{2^n} \prod_{k=1}^{n} \frac{(6k-2)!\,(2k-1)!}{(4k-1)!\,(4k-2)!}$$
> conjectured by Robbins and proved by Kuperberg (2002).

```lean
theorem conjecture (n : ℕ) :
    frac (n + 1) = (b (n + 1) : ℚ) / (b n : ℚ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/109074.lean, line 153](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109074.lean#L153).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/109074.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109074.lean)
- [A109074](https://oeis.org/A109074)
