---
declaration: theorem
origin: cited
lean: Erdos627.erdos_627, Erdos627.erdos_627.variants.theta, Erdos627.erdos_627.variants.lower, Erdos627.erdos_627.variants.upper, Erdos627.erdos_627.variants.limit_bounds, Erdos627.erdos_627.variants.afm_upper, Erdos627.erdos_627.variants.conditional, Erdos627.erdos_627.variants.tutte_zykov, Erdos627.erdos_627.variants.erdos_1961
statement: formalized
---

# Erdős Problem 627

> *References:*
> - [erdosproblems.com/627](https://www.erdosproblems.com/627)
> - [AFM25] Araujo, I. and Filipe, R. and Miyazaki, R., *A note on the maximum ratio between
>   chromatic number and clique number*. arXiv:2512.16062 (2025).
> - [Er61d] Erdős, P., *Graph theory and probability. II*. Canadian J. Math. (1961), 346-352.
> - [Er67c] Erdős, P., *Some remarks on chromatic graphs*. Colloq. Math. (1967), 253-256.
> - [Er69b] Erdős, P., *Problems and results in chromatic graph theory*. Proof Techniques in Graph
>   Theory (Proc. Second Ann Arbor Graph Theory Conf., Ann Arbor, Mich., 1968) (1969), 27-35.
> - [My55] Mycielski, J., *Sur le coloriage des graphs*. Colloquium Mathematicum 3 (1955), 161–162.
>   [doi:10.4064/cm-3-2-161-162](https://doi.org/10.4064/cm-3-2-161-162)
> - [Zy52] Zykov, A. A., *On some properties of linear complexes*. Amer. Math. Soc. Translation
>   (1952), 33.

*Quoted from [FormalConjectures/ErdosProblems/627.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/627.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/627](https://www.erdosproblems.com/627).

The file states 9 research or textbook statements: 1 open and 8 solved.

## `Erdos627.erdos_627`

Open: stated without proof.

> Let $\omega(G)$ denote the clique number of $G$ and $\chi(G)$ the chromatic number. If $f(n)$ is
> the maximum value of $\chi(G)/\omega(G)$, as $G$ ranges over all graphs on $n$ vertices, then
> does
>
> $$\lim_{n\to\infty}\frac{f(n)}{n/(\log_2n)^2}$$
>
> exist?
>
> Since $f(n) \asymp n/(\log_2 n)^2$ (see `Erdos627.erdos_627.variants.theta`), the limit, if it
> exists, is a finite real number.

```lean
theorem erdos_627 :
    ∃ L : ℝ, Tendsto (fun n : ℕ ↦ maxChromaticCliqueRatio n / ((n : ℝ) / Real.logb 2 n ^ 2))
      atTop (𝓝 L)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/627.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/627.lean#L67).

## `Erdos627.erdos_627.variants.theta`

Solved: stated here without proof.

> Erdős [Er67c] proved that
>
> $$f(n) \asymp \frac{n}{(\log_2 n)^2}.$$

```lean
theorem erdos_627.variants.theta :
    (fun n : ℕ ↦ maxChromaticCliqueRatio n) =Θ[atTop]
      (fun n : ℕ ↦ (n : ℝ) / Real.logb 2 n ^ 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/627.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/627.lean#L77).

## `Erdos627.erdos_627.variants.lower`

Solved: stated here without proof.

> Erdős [Er67c] proved the lower bound
>
> $$f(n) \geq \left(\frac{1}{4} + o(1)\right) \frac{n}{(\log_2 n)^2}.$$

```lean
theorem erdos_627.variants.lower :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      (1 / 4 - ε) * ((n : ℝ) / Real.logb 2 n ^ 2) ≤ maxChromaticCliqueRatio n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/627.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/627.lean#L87).

## `Erdos627.erdos_627.variants.upper`

Solved: stated here without proof.

> The method of Erdős [Er67c] gives the upper bound
>
> $$f(n) \leq (4 + o(1)) \frac{n}{(\log_2 n)^2}.$$
>
> Erdős states the constant as $1$, but Araujo, Filipe, and Miyazaki [AFM25] note that his method
> gives $4$.

```lean
theorem erdos_627.variants.upper :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      maxChromaticCliqueRatio n ≤ (4 + ε) * ((n : ℝ) / Real.logb 2 n ^ 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/627.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/627.lean#L99).

## `Erdos627.erdos_627.variants.limit_bounds`

Solved: stated here without proof.

> Consequently, if the limit in `Erdos627.erdos_627` exists, it lies in $[1/4, 4]$ [Er67c]
> (with the correction of the upper constant from $1$ to $4$ noted in [AFM25]).

```lean
theorem erdos_627.variants.limit_bounds :
    ∀ L : ℝ, Tendsto (fun n : ℕ ↦ maxChromaticCliqueRatio n / ((n : ℝ) / Real.logb 2 n ^ 2))
      atTop (𝓝 L) → 1 / 4 ≤ L ∧ L ≤ 4
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/627.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/627.lean#L109).

## `Erdos627.erdos_627.variants.afm_upper`

Solved: stated here without proof.

> Araujo, Filipe, and Miyazaki [AFM25, Theorem 1.3] improved the upper bound to
>
> $$f(n) \leq (3.71943 + o(1)) \frac{n}{(\log_2 n)^2},$$
>
> using recent improvements in the asymptotics of Ramsey numbers. [AFM25] is an arXiv preprint.

```lean
theorem erdos_627.variants.afm_upper :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      maxChromaticCliqueRatio n ≤ (3.71943 + ε) * ((n : ℝ) / Real.logb 2 n ^ 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/627.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/627.lean#L120).

## `Erdos627.erdos_627.variants.conditional`

Solved: stated here without proof.

> Araujo, Filipe, and Miyazaki [AFM25, Theorem 1.2]: suppose that $R(s,t) \leq R(k)$ for all
> $s, t, k \in \mathbb{N}$ with $st \leq k^2$ (their Conjecture 1.1), and that
> $\lim_{k \to \infty} \frac{\log_2 R(k)}{k}$ exists and equals $\ell$. Then
>
> $$f(n) = (\ell^2 + o(1)) \frac{n}{(\log_2 n)^2},$$
>
> so the limit in `Erdos627.erdos_627` exists and equals $\ell^2$. Here $R(s,t)$ is the
> two-colour Ramsey number and $R(k) = R(k,k)$ (see [77]). [AFM25] is an arXiv preprint.

```lean
theorem erdos_627.variants.conditional (ℓ : ℝ)
    (hR : ∀ s t k : ℕ, s * t ≤ k ^ 2 → classicalRamsey s t ≤ diagonalRamsey k)
    (hlim : Tendsto (fun k : ℕ ↦ Real.logb 2 (diagonalRamsey k : ℝ) / (k : ℝ)) atTop (𝓝 ℓ)) :
    Tendsto (fun n : ℕ ↦ maxChromaticCliqueRatio n / ((n : ℝ) / Real.logb 2 n ^ 2))
      atTop (𝓝 (ℓ ^ 2))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/627.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/627.lean#L134).

## `Erdos627.erdos_627.variants.tutte_zykov`

Proved here.

> Tutte and Zykov [Zy52] independently proved that for every $k$ there is a graph with
> $\omega(G) = 2$ and $\chi(G) = k$.
>
> We require $k \geq 2$: a graph with $\omega(G) = 2$ has an edge, so $\chi(G) \geq 2$.
> The proof here uses Mycielski's construction [My55].

```lean
theorem erdos_627.variants.tutte_zykov :
    ∀ k : ℕ, 2 ≤ k → ∃ (n : ℕ) (G : SimpleGraph (Fin n)),
      G.cliqueNum = 2 ∧ G.chromaticNumber = (k : ℕ∞)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/627.lean, line 149](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/627.lean#L149).

## `Erdos627.erdos_627.variants.erdos_1961`

Solved: stated here without proof.

> Erdős [Er61d] proved that for every (large) $n$ there is a graph on $n$ vertices with
> $\omega(G) = 2$ and
>
> $$\chi(G) \gg \frac{n^{1/2}}{\log n},$$
>
> whence $f(n) \gg n^{1/2}/\log n$.

```lean
theorem erdos_627.variants.erdos_1961 :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∃ G : SimpleGraph (Fin n),
      G.cliqueNum = 2 ∧
        c * Real.sqrt (n : ℝ) / Real.log (n : ℝ) ≤ (G.chromaticNumber.toNat : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/627.lean, line 161](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/627.lean#L161).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/627.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/627.lean)
- [erdosproblems.com/627](https://www.erdosproblems.com/627)
