---
declaration: theorem
origin: cited
lean: Erdos864.erdos_864, Erdos864.erdos_864.variants.lower_bound
statement: formalized
---

# Erdős Problem 864

> *References:*
> - [erdosproblems.com/864](https://www.erdosproblems.com/864)
> - [A389182](https://oeis.org/A389182)
> - [ErFr91] Erdős, P. and Freud, R., *On sums of a Sidon-sequence*. J. Number Theory 38 (1991),
>   196--205.
> - [Er92c] Erdős, P., *Some of my forgotten problems in number theory*. Hardy-Ramanujan J. 15
>   (1992), 34-50.

*Quoted from [FormalConjectures/ErdosProblems/864.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/864.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/864](https://www.erdosproblems.com/864).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 3 test statements, counted here but not shown.

## `Erdos864.erdos_864`

Open: stated without proof.

> Let $A\subseteq \{1,\ldots,N\}$ be a set such that there exists at most one $n$ with more than one
> solution to $n=a+b$ (with $a\leq b\in A$). Estimate the maximal possible size of $|A|$. In
> particular, is it true that
> $$|A| \leq (1+o(1))\frac{2}{\sqrt{3}} N^{1/2}?$$
>
> A problem of Erdős and Freud [ErFr91] [Er92c]. For the analogous question with $n=a-b$ they prove
> that $\lvert A\rvert\sim N^{1/2}$. This is a weaker form of Erdős Problem 840.
>
> The condition on $A$ is `HasAtMostOneRepeatedSum`. We state the question as follows: for every
> $\varepsilon > 0$ and all large $N$, every such set $A$ satisfies
> $|A| \leq (1+\varepsilon)\frac{2}{\sqrt{3}} N^{1/2}$.

```lean
theorem erdos_864 :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ N : ℕ in atTop, ∀ A ⊆ Finset.Icc 1 N,
      HasAtMostOneRepeatedSum A →
        (#A : ℝ) ≤ (1 + ε) * (2 / Real.sqrt 3) * Real.sqrt (N : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/864.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/864.lean#L65).

## `Erdos864.erdos_864.variants.lower_bound`

Solved: stated here without proof.

> Erdős and Freud [ErFr91] [Er92c] prove that
> $$\lvert A\rvert \geq (1+o(1))\frac{2}{\sqrt{3}}N^{1/2}.$$
> This is shown by taking a genuine Sidon set $B\subset [1,N/3]$ of size $\sim N^{1/2}/\sqrt{3}$
> and taking the union with $\{N-b : b\in B\}$.
>
> That is, for every $\varepsilon > 0$ and all large $N$ there is a set $A\subseteq \{1,\ldots,N\}$
> with the property of `Erdos864.erdos_864` and $|A| \geq (1-\varepsilon)\frac{2}{\sqrt{3}}N^{1/2}$.
> So the constant $2/\sqrt{3}$ there cannot be replaced by a smaller one.

```lean
theorem erdos_864.variants.lower_bound :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ N : ℕ in atTop, ∃ A ⊆ Finset.Icc 1 N,
      HasAtMostOneRepeatedSum A ∧
        (1 - ε) * (2 / Real.sqrt 3) * Real.sqrt (N : ℝ) ≤ #A
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/864.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/864.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/864.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/864.lean)
- [erdosproblems.com/864](https://www.erdosproblems.com/864)
