---
declaration: theorem
origin: cited
lean: Erdos756.erdos_756, Erdos756.erdos_756.variants.bhowmick, Erdos756.erdos_756.variants.bhowmick_general
statement: formalized
---

# Erdős Problem 756

> *References:*
> - [erdosproblems.com/756](https://www.erdosproblems.com/756)
> - [Bh24] Bhowmick, K., *A problem of Erdős about rich distances*. arXiv:2407.01174 (2024).
> - [CDL25] Clemen, F., Dumitrescu, A. and Liu, D., *On multiplicities of interpoint distances*.
>   arXiv:2505.04283 (2025).
> - [Er97b] Erdős, Paul, *Some old and new problems in various branches of combinatorics*.
>   Discrete Math. (1997), 227-231.
> - [ErPa90] Erdős, P. and Pach, J., *Variations on the theme of repeated distances*.
>   Combinatorica (1990), 261-269.
> - [HoPa34] Hopf, H. and Pannwitz, E., *Aufgabe 167*. Jber. Deutsch. Math. Verein. (1934), 114.

*Quoted from [FormalConjectures/ErdosProblems/756.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/756.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/756](https://www.erdosproblems.com/756).

The file states 3 research or textbook statements: 3 solved.

## `Erdos756.erdos_756`

Solved: stated here without proof.

> Let $A\subset \mathbb{R}^2$ be a set of $n$ points. Can there be $\gg n$ many distinct distances
> each of which occurs for more than $n$ many pairs from $A$?
>
> The answer is yes: Bhowmick [Bh24] constructs a set of $n$ points in $\mathbb{R}^2$ such that
> $\lfloor\frac{n}{4}\rfloor$ distances occur at least $n+1$ times.

```lean
theorem erdos_756 :
    (fun n : ℕ => (n : ℝ)) =O[atTop] (fun n : ℕ => (maxRichDistances n : ℝ))
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/756.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/756.lean#L59).

## `Erdos756.erdos_756.variants.bhowmick`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos756.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos756.lean).

> Bhowmick [Bh24] constructs a set of $n$ points in $\mathbb{R}^2$ such that
> $\lfloor\frac{n}{4}\rfloor$ distances occur at least $n+1$ times.

```lean
theorem erdos_756.variants.bhowmick (n : ℕ) :
    ∃ A : Finset ℝ², A.card = n ∧ n / 4 ≤ (richDistances A (n + 1)).card
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/756.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/756.lean#L69).

## `Erdos756.erdos_756.variants.bhowmick_general`

Solved: stated here without proof.

> More generally, they construct, for any positive integer $m$ and large $n$, a set of $n$ points
> such that
> $\lfloor \frac{n}{2(m+1)}\rfloor$ distances occur at least $n+m$ times.

```lean
theorem erdos_756.variants.bhowmick_general (m : ℕ) (hm : 1 ≤ m) :
    ∀ᶠ n : ℕ in atTop, ∃ A : Finset ℝ², A.card = n ∧
      n / (2 * (m + 1)) ≤ (richDistances A (n + m)).card
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/756.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/756.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/756.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/756.lean)
- [erdosproblems.com/756](https://www.erdosproblems.com/756)
