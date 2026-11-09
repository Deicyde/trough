---
declaration: theorem
origin: cited
lean: Erdos670.erdos_670, Erdos670.erdos_670.variants.dim_one, Erdos670.erdos_670.variants.choose_two, Erdos670.erdos_670.variants.ho, Erdos670.erdos_670.variants.uniform_in_dim
statement: formalized
---

# Erdős Problem 670

> *References:*
> - [erdosproblems.com/670](https://www.erdosproblems.com/670)
> - [Er97f] Erdős, Paul, *Some unsolved problems*. Combinatorics, geometry and probability
>   (Cambridge, 1993) (1997), 1-10.
> - [Ho26] Ho, B. S., *Erdős's diameter conjecture for separated distances fails in high
>   dimensions*. [arXiv:2604.15305](https://arxiv.org/abs/2604.15305) (2026).

*Quoted from [FormalConjectures/ErdosProblems/670.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/670.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/670](https://www.erdosproblems.com/670).

The file states 5 research or textbook statements: 1 open, 3 solved and 1 textbook result.

## `Erdos670.erdos_670`

Open: stated without proof.

> Let $A\subseteq \mathbb{R}^d$ be a set of $n$ points such that all pairwise distances differ by
> at least $1$. Is the diameter of $A$ at least $(1+o(1))n^2$?
>
> The quantifiers in the source are ambiguous. Following the remarks on erdosproblems.com, this is
> the regime where $d$ is fixed and the $o(1)$ term tends to $0$ as $n \to \infty$, at a rate
> which may depend on $d$. The case $d = 1$ was proved by Erdős
> (`Erdos670.erdos_670.variants.dim_one`), so the question is open for $d \geq 2$.

```lean
theorem erdos_670 :
    ∀ d : ℕ, 1 ≤ d → ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      ∀ A : Finset (EuclideanSpace ℝ (Fin d)), A.card = n → HasSeparatedDistances A →
        (1 - ε) * (n : ℝ) ^ 2 ≤ Metric.diam (A : Set (EuclideanSpace ℝ (Fin d)))
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/670.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/670.lean#L54).

## `Erdos670.erdos_670.variants.dim_one`

Solved: stated here without proof.

> Erdős [Er97f] proved the claim when $d = 1$: if $A\subseteq \mathbb{R}$ is a set of $n$ points
> such that all pairwise distances differ by at least $1$, then the diameter of $A$ is at least
> $(1+o(1))n^2$.

```lean
theorem erdos_670.variants.dim_one :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      ∀ A : Finset (EuclideanSpace ℝ (Fin 1)), A.card = n → HasSeparatedDistances A →
        (1 - ε) * (n : ℝ) ^ 2 ≤ Metric.diam (A : Set (EuclideanSpace ℝ (Fin 1)))
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/670.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/670.lean#L66).

## `Erdos670.erdos_670.variants.choose_two`

Textbook result, stated without proof. A Lean proof is at [https://github.com/veljjanoski/formal-conjectures-proofs/blob/638a2315428e3a1c2f1a784bcaeffea6580d1cbd/FcProofs/Erdos670.lean#L65](https://github.com/veljjanoski/formal-conjectures-proofs/blob/638a2315428e3a1c2f1a784bcaeffea6580d1cbd/FcProofs/Erdos670.lean#L65).

> The trivial lower bound: if $A\subseteq \mathbb{R}^d$ is a set of $n \neq 2$ points such that all
> pairwise distances differ by at least $1$, then the diameter of $A$ is at least $\binom{n}{2}$.
>
> For $n \geq 3$, take a closest pair $a, b$ and a third point $c$. Then
> $1 \leq \lvert d(a, c) - d(b, c)\rvert \leq d(a, b)$, so every distance is at least $1$. The
> $\binom{n}{2}$ distances are at least $1$ apart, so the largest one is at least $\binom{n}{2}$.
> For $n = 2$ the hypothesis is vacuous, and two points at distance $1/2$ show that the bound fails.

```lean
theorem erdos_670.variants.choose_two (d : ℕ) (A : Finset (EuclideanSpace ℝ (Fin d)))
    (hA : HasSeparatedDistances A) (hn : A.card ≠ 2) :
    (A.card.choose 2 : ℝ) ≤ Metric.diam (A : Set (EuclideanSpace ℝ (Fin d)))
```

Category `textbook`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/670.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/670.lean#L83).

## `Erdos670.erdos_670.variants.ho`

Solved: stated here; a Lean proof is at [https://github.com/boonsuan/erdos670/blob/c053b2580e0cf7e74c8d905f96feb101061612a3/DiameterConstruction/MainTheorem.lean#L452](https://github.com/boonsuan/erdos670/blob/c053b2580e0cf7e74c8d905f96feb101061612a3/DiameterConstruction/MainTheorem.lean#L452).

> Ho [Ho26] showed that the claim fails if $n$ grows with $d$: there exist infinitely many $n$
> and, with $d = n^2 - n$, a set $A\subset \mathbb{R}^d$ of $n$ points such that all pairwise
> distances differ by at least $1$, with diameter at most
> $$
> \left(1-\frac{1}{\pi^2}+o(1)\right)n^2\approx 0.898n^2.
> $$
> Ho's construction uses $n = q + 1$ points in dimension $q^2 + q = n^2 - n$, for every prime power
> $q$.

```lean
theorem erdos_670.variants.ho :
    ∀ ε > (0 : ℝ), ∃ᶠ n : ℕ in atTop,
      ∃ A : Finset (EuclideanSpace ℝ (Fin (n ^ 2 - n))), A.card = n ∧
        HasSeparatedDistances A ∧
        Metric.diam (A : Set (EuclideanSpace ℝ (Fin (n ^ 2 - n)))) ≤
          (1 - 1 / Real.pi ^ 2 + ε) * (n : ℝ) ^ 2
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/670.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/670.lean#L101).

## `Erdos670.erdos_670.variants.uniform_in_dim`

Solved: stated here without proof.

> The version of the problem where the $o(1)$ term must be uniform in the dimension $d$ has a
> negative answer. This follows from `Erdos670.erdos_670.variants.ho` (Ho [Ho26]).

```lean
theorem erdos_670.variants.uniform_in_dim :
    ¬ ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∀ d : ℕ,
      ∀ A : Finset (EuclideanSpace ℝ (Fin d)), A.card = n → HasSeparatedDistances A →
        (1 - ε) * (n : ℝ) ^ 2 ≤ Metric.diam (A : Set (EuclideanSpace ℝ (Fin d)))
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/670.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/670.lean#L114).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/670.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/670.lean)
- [erdosproblems.com/670](https://www.erdosproblems.com/670)
