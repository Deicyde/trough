---
declaration: theorem
origin: cited
lean: LanderParkinSelfridge.lander_parkin_selfridge, LanderParkinSelfridge.lander_parkin_selfridge.variants.five_three
statement: formalized
---

# Lander, Parkin, and Selfridge Conjecture

> **Reference:** https://en.wikipedia.org/wiki/Lander,_Parkin,_and_Selfridge_conjecture

*Quoted from [FormalConjectures/Wikipedia/LanderParkinAndSelfridgeConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LanderParkinAndSelfridgeConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `LanderParkinSelfridge.lander_parkin_selfridge`

Open: stated without proof.

> The Lander–Parkin–Selfridge conjecture: if the sum of $n$ positive integer $k$-th powers
> equals the sum of $m$ positive integer $k$-th powers, with all values on the left distinct from
> all values on the right, then $n + m \geq k$.
>
> Formally, for positive integers $k, n, m \in \mathbb{N}$ and sequences
> $x : \{0, \ldots, n-1\} \to \mathbb{N}$ and $y : \{0, \ldots, m-1\} \to \mathbb{N}$
> with $x_i > 0$, $y_j > 0$, and $x_i \neq y_j$ for all $i, j$, if
>
> $$\sum_{i=0}^{n-1} x_i^k = \sum_{j=0}^{m-1} y_j^k,$$
>
> then $k \leq n + m$.

```lean
theorem lander_parkin_selfridge :
    ∀ (k n m : ℕ) (x : Fin n → ℕ) (y : Fin m → ℕ),
      0 < n → 0 < m →
      (∀ i, 0 < x i) → (∀ j, 0 < y j) →
      (∀ i j, x i ≠ y j) →
      ∑ i, x i ^ k = ∑ j, y j ^ k →
      k ≤ n + m
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/LanderParkinAndSelfridgeConjecture.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LanderParkinAndSelfridgeConjecture.lean#L40).

## `LanderParkinSelfridge.lander_parkin_selfridge.variants.five_three`

Open: stated without proof.

> Special case of the Lander–Parkin–Selfridge conjecture: there is no solution in positive
> integers to
>
> $$x_1^5 + x_2^5 + x_3^5 = y^5.$$
>
> That is, for all $x_1, x_2, x_3, y \in \mathbb{N}$ with $x_1, x_2, x_3, y > 0$,
>
> $$x_1^5 + x_2^5 + x_3^5 \neq y^5.$$
>
> This corresponds to the case $k = 5$, $n = 3$, $m = 1$ of the general conjecture,
> where $n + m = 4 < 5 = k$ would be required to yield a counterexample.

```lean
theorem lander_parkin_selfridge.variants.five_three :
    ∀ x₁ x₂ x₃ y : ℕ,
      0 < x₁ → 0 < x₂ → 0 < x₃ → 0 < y →
      x₁ ^ 5 + x₂ ^ 5 + x₃ ^ 5 ≠ y ^ 5
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/LanderParkinAndSelfridgeConjecture.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LanderParkinAndSelfridgeConjecture.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/LanderParkinAndSelfridgeConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LanderParkinAndSelfridgeConjecture.lean)
- [https://en.wikipedia.org/wiki/Lander,_Parkin,_and_Selfridge_conjecture](https://en.wikipedia.org/wiki/Lander,_Parkin,_and_Selfridge_conjecture)
