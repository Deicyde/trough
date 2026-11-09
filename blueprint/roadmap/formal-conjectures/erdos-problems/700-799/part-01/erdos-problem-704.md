---
declaration: theorem
origin: cited
lean: Erdos704.erdos_704.parts.i, Erdos704.erdos_704.parts.ii, Erdos704.erdos_704.variants.cube_colouring, Erdos704.erdos_704.variants.frankl_wilson, Erdos704.erdos_704.variants.raigorodskii, Erdos704.erdos_704.variants.davies_lower, Erdos704.erdos_704.variants.larman_rogers, Erdos704.erdos_704.variants.davies_upper, Erdos704.erdos_704.variants.larman_rogers_conjecture
statement: formalized
---

# Erdős Problem 704

> *References:*
> - [erdosproblems.com/704](https://www.erdosproblems.com/704)
> - [Da26] Davies, J., *Measurable obstructions for unmeasurable colourings*. Preprint (2026).
>   [arXiv:2610.12301](https://arxiv.org/abs/2610.12301)
> - [Er81] Erdős, P., *On the combinatorial problems which I would most like to see solved*.
>   Combinatorica (1981), 25-42.
> - [FrWi81] Frankl, P. and Wilson, R. M., *Intersection theorems with geometric consequences*.
>   Combinatorica (1981), 357-368.
> - [LaRo72] Larman, D. G. and Rogers, C. A., *The realization of distances within sets in
>   Euclidean space*. Mathematika (1972), 1-24.
> - [Pr20] Prosanov, R., *A new proof of the Larman-Rogers upper bound for the chromatic number of
>   the Euclidean space*. Discrete Appl. Math. (2020), 115-120.
> - [Ra00] Raigorodskii, A. M., *On the chromatic number of a space*. Uspekhi Mat. Nauk (2000),
>   147-148.

*Quoted from [FormalConjectures/ErdosProblems/704.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/704.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/704](https://www.erdosproblems.com/704).

The file states 9 research or textbook statements: 1 open, 7 solved and 1 textbook result.

## `Erdos704.erdos_704.parts.i`

Solved: stated here without proof.

> Does $\chi(G_n)$ grow exponentially in $n$?
>
> Yes: Frankl and Wilson [FrWi81] proved an exponential lower bound and Larman and Rogers
> [LaRo72] proved an exponential upper bound. Here exponential growth means that there are
> constants $1 < c \leq C$ such that $c^n \leq \chi(G_n) \leq C^n$ for all large $n$.

```lean
theorem erdos_704.parts.i :
    (∃ c > (1 : ℝ), ∀ᶠ n : ℕ in atTop,
      ∀ k : ℕ, (unitDistanceGraph n).Colorable k → c ^ n ≤ (k : ℝ)) ∧
    ∃ C : ℝ, ∀ᶠ n : ℕ in atTop,
      ∃ k : ℕ, (unitDistanceGraph n).Colorable k ∧ (k : ℝ) ≤ C ^ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/704.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/704.lean#L62).

## `Erdos704.erdos_704.parts.ii`

Open: stated without proof.

> Let $G_n$ be the unit distance graph in $\mathbb{R}^n$, with two vertices joined by an edge if
> and only if the distance between them is $1$. Does
> $$\lim_{n\to\infty}\chi(G_n)^{1/n}$$
> exist?
>
> This generalises the Hadwiger–Nelson problem (Erdős Problem 508), the case $n = 2$. The
> chromatic number is finite (see `Erdos704.erdos_704.variants.cube_colouring`).

```lean
theorem erdos_704.parts.ii :
    ∃ L : ℝ, Tendsto
      (fun n : ℕ ↦ ((unitDistanceGraph n).chromaticNumber.toNat : ℝ) ^ (1 / (n : ℝ)))
      atTop (𝓝 L)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/704.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/704.lean#L79).

## `Erdos704.erdos_704.variants.cube_colouring`

Textbook result, stated without proof.

> The trivial colouring (by tiling with cubes) gives
> $$\chi(G_n) \leq (2 + \sqrt{n})^n.$$
> In particular $\chi(G_n)$ is finite for every $n$.

```lean
theorem erdos_704.variants.cube_colouring :
    ∀ n : ℕ, ∃ k : ℕ, (unitDistanceGraph n).Colorable k ∧
      (k : ℝ) ≤ (2 + Real.sqrt n) ^ n
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/704.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/704.lean#L91).

## `Erdos704.erdos_704.variants.frankl_wilson`

Solved: stated here without proof.

> Frankl and Wilson [FrWi81] proved
> $$\chi(G_n) \geq (1 + o(1)) 1.2^n.$$

```lean
theorem erdos_704.variants.frankl_wilson :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      ∀ k : ℕ, (unitDistanceGraph n).Colorable k → (1 - ε) * 1.2 ^ n ≤ (k : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/704.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/704.lean#L101).

## `Erdos704.erdos_704.variants.raigorodskii`

Solved: stated here without proof.

> Raigorodskii [Ra00] proved
> $$\chi(G_n) \geq (1.239\cdots + o(1))^n.$$
> We state the weaker bound with the truncated constant $1.239$: for every $0 < c < 1.239$ we
> have $\chi(G_n) \geq c^n$ for all large $n$.

```lean
theorem erdos_704.variants.raigorodskii :
    ∀ c ∈ Set.Ioo (0 : ℝ) 1.239, ∀ᶠ n : ℕ in atTop,
      ∀ k : ℕ, (unitDistanceGraph n).Colorable k → c ^ n ≤ (k : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/704.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/704.lean#L113).

## `Erdos704.erdos_704.variants.davies_lower`

Solved: stated here without proof.

> Davies [Da26, Theorem 1.4] proved
> $$\chi(G_n) \geq (2 + o(1))^n,$$
> improving the bound of Raigorodskii (see `Erdos704.erdos_704.variants.raigorodskii`): for every
> $0 < c < 2$ we have $\chi(G_n) \geq c^n$ for all large $n$.

```lean
theorem erdos_704.variants.davies_lower :
    ∀ c ∈ Set.Ioo (0 : ℝ) 2, ∀ᶠ n : ℕ in atTop,
      ∀ k : ℕ, (unitDistanceGraph n).Colorable k → c ^ n ≤ (k : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/704.lean, line 125](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/704.lean#L125).

## `Erdos704.erdos_704.variants.larman_rogers`

Solved: stated here without proof.

> Larman and Rogers [LaRo72] proved
> $$\chi(G_n) \leq (3 + o(1))^n.$$
> Prosanov [Pr20] has given an alternative proof of this bound.

```lean
theorem erdos_704.variants.larman_rogers :
    ∀ C > (3 : ℝ), ∀ᶠ n : ℕ in atTop,
      ∃ k : ℕ, (unitDistanceGraph n).Colorable k ∧ (k : ℝ) ≤ C ^ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/704.lean, line 136](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/704.lean#L136).

## `Erdos704.erdos_704.variants.davies_upper`

Solved: stated here without proof.

> Davies [Da26, Theorem 1.5] proved
> $$\chi(G_n) \leq (3\sqrt{3}/2 + o(1))^n,$$
> improving the bound of Larman and Rogers (see `Erdos704.erdos_704.variants.larman_rogers`).
> (The abstract of [Da26] prints $3\sqrt{3}/4$; Theorem 1.5 has $3\sqrt{3}/2 \approx 2.598$.)

```lean
theorem erdos_704.variants.davies_upper :
    ∀ C > 3 * Real.sqrt 3 / 2, ∀ᶠ n : ℕ in atTop,
      ∃ k : ℕ, (unitDistanceGraph n).Colorable k ∧ (k : ℝ) ≤ C ^ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/704.lean, line 148](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/704.lean#L148).

## `Erdos704.erdos_704.variants.larman_rogers_conjecture`

Solved: stated here without proof.

> Larman and Rogers [LaRo72] conjecture that the truth may be
> $$\chi(G_n) = (2^{3/2} + o(1))^n,$$
> that is, $\chi(G_n)^{1/n} \to 2^{3/2}$.
>
> This is false: by `Erdos704.erdos_704.variants.davies_upper` [Da26] we have
> $\limsup \chi(G_n)^{1/n} \leq 3\sqrt{3}/2 < 2^{3/2}$. Whether the limit exists remains open
> (`Erdos704.erdos_704.parts.ii`).

```lean
theorem erdos_704.variants.larman_rogers_conjecture :
    ¬ Tendsto
      (fun n : ℕ ↦ ((unitDistanceGraph n).chromaticNumber.toNat : ℝ) ^ (1 / (n : ℝ)))
      atTop (𝓝 ((2 : ℝ) ^ ((3 : ℝ) / 2)))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/704.lean, line 163](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/704.lean#L163).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/704.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/704.lean)
- [erdosproblems.com/704](https://www.erdosproblems.com/704)
