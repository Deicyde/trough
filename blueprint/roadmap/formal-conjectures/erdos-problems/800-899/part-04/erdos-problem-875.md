---
declaration: theorem
origin: cited
lean: Erdos875.erdos_875, Erdos875.erdos_875.variants.erdos_nicolas_sarkozy, Erdos875.erdos_875.variants.polynomial_gaps, Erdos875.erdos_875.variants.deshouillers_freiman
statement: formalized
---

# Erdős Problem 875

> *References:*
> - [erdosproblems.com/875](https://www.erdosproblems.com/875)
> - [Er98] Erdős, P., *Some of my new and almost new problems and results in combinatorial number
>   theory*. Number theory (Eger, 1996) (1998), 169-180.
> - [Er62c] Erdős, P., *Some remarks on number theory. III* (in Hungarian). Mat. Lapok 13 (1962),
>   28-38. [PDF](https://www.renyi.hu/~p_erdos/1962-22.pdf)
> - [ENS91] Erdős, P., Nicolas, J.-L. and Sárközy, A., *Sommes de sous-ensembles*. J. Théor. Nombres
>   Bordeaux 3 (1991), 55-72. [Numdam](https://www.numdam.org/item/JTNB_1991__3_1_55_0/)
> - [DeFr99] Deshouillers, J.-M. and Freiman, G. A., *On an additive problem of Erdős and Straus,
>   2*. Astérisque 258 (1999), 141-148. [Numdam](https://www.numdam.org/item/AST_1999__258__141_0/)
>
> The finite version of this problem is [erdosproblems.com/874](https://www.erdosproblems.com/874).

*Quoted from [FormalConjectures/ErdosProblems/875.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/875.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/875](https://www.erdosproblems.com/875).

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 1 API statement, counted here but not shown.

## `Erdos875.erdos_875`

Open: stated without proof.

> Let $A=\{a_1\lt a_2\lt \cdots\}\subset \mathbb{N}$ be an infinite set such that the sets
> $$S_r = \{ a_1+\cdots +a_r : a_1\lt \cdots\lt a_r\in A\}$$
> are disjoint for distinct $r\geq 1$. How fast can such a sequence grow? How small can
> $a_{n+1}-a_n$ be? In particular, for which $c$ is it possible that $a_{n+1}-a_n\leq n^{c}$?
>
> A problem of Deshouillers and Erdős [Er98] (an infinite version of
> [874](https://www.erdosproblems.com/874)). Such sets are sometimes called admissible. We state the
> last question: the set of such $c$ is `erdos_875.answer`. The bound is required for all large $n$,
> since otherwise the first few $n$ would constrain the answer. The first two questions are not
> formalised separately. Erdős also writes that it is not completely trivial to find such a sequence
> with $a_{n+1}/a_n\to 1$ (not formalised).

```lean
theorem erdos_875 :
    {c : ℝ | ∃ A : Set ℕ, A.Infinite ∧ IsAdmissible A ∧
      ∀ᶠ n : ℕ in atTop, (gap A n : ℝ) ≤ (n : ℝ) ^ c} = erdos_875.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/875.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/875.lean#L93).

## `Erdos875.erdos_875.variants.erdos_nicolas_sarkozy`

Solved: stated here without proof.

> Erdős, Nicolas and Sárközy [ENS91, Theorem 2] constructed an infinite admissible set $A$ with
> $$A(x)=\lvert\{a\in A: a\leq x\}\rvert \gg x^{5-2\sqrt6}.$$
> The implied constant is positive and the inequality is required for all large $x$. This improves
> a result of Erdős [Er62c], who obtained $A(x)\gg x^{c}$ for some unspecified $c>0$.

```lean
theorem erdos_875.variants.erdos_nicolas_sarkozy :
    ∃ A : Set ℕ, A.Infinite ∧ IsAdmissible A ∧ ∃ c : ℝ, 0 < c ∧
      ∀ᶠ x : ℕ in atTop, c * (x : ℝ) ^ (5 - 2 * Real.sqrt 6) ≤ (countingFunction A x : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/875.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/875.lean#L105).

## `Erdos875.erdos_875.variants.polynomial_gaps`

Solved: stated here without proof.

> Since $5-2\sqrt6=(5+2\sqrt6)^{-1}$, the result of [ENS91, Theorem 2] gives
> $a_n\ll n^{5+2\sqrt6}$, hence $a_{n+1}-a_n\leq a_{n+1}\ll n^{5+2\sqrt6}$. So every
> $c>5+2\sqrt6$ is possible in the main question.

```lean
theorem erdos_875.variants.polynomial_gaps (c : ℝ) (hc : 5 + 2 * Real.sqrt 6 < c) :
    ∃ A : Set ℕ, A.Infinite ∧ IsAdmissible A ∧
      ∀ᶠ n : ℕ in atTop, (gap A n : ℝ) ≤ (n : ℝ) ^ c
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/875.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/875.lean#L116).

## `Erdos875.erdos_875.variants.deshouillers_freiman`

Solved: stated here without proof.

> Deshouillers and Freiman [DeFr99, Theorem 1] proved a conjecture of Erdős on the finite version
> ([874](https://www.erdosproblems.com/874)): for all sufficiently large $N$, every admissible set
> $A\subseteq\{1,\ldots,N\}$ satisfies
> $$\lvert A\rvert\leq 2\sqrt{N+\tfrac14}-1.$$
> This is sharp: by Straus, the set of $k$ consecutive integers ending at $N$ is admissible if and
> only if $k\leq 2\sqrt{N+\frac14}-1$.

```lean
theorem erdos_875.variants.deshouillers_freiman :
    ∃ N₀ : ℕ, ∀ N : ℕ, N₀ ≤ N → ∀ A : Finset ℕ, (A : Set ℕ) ⊆ Set.Icc 1 N →
      IsAdmissible (A : Set ℕ) → (A.card : ℝ) ≤ 2 * Real.sqrt ((N : ℝ) + 1 / 4) - 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/875.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/875.lean#L130).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/875.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/875.lean)
- [erdosproblems.com/875](https://www.erdosproblems.com/875)
