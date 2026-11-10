---
declaration: theorem
origin: cited
lean: Erdos344.erdos_344, Erdos344.erdos_344.variants.sqrt_two, Erdos344.erdos_344.variants.folkman
statement: formalized
---

# Erdős Problem 344

> *References:*
> - [erdosproblems.com/344](https://www.erdosproblems.com/344)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Er61b] Erdős, P., *On the representation of large integers as sums of distinct summands
>   taken from a fixed set*. Acta Arith. (1961/62), 345-354.
> - [Fo66] Folkman, J., *On the representation of integers as sums of distinct terms from a
>   fixed sequence*. Canadian J. Math. 18 (1966), 643-655.
> - [SzVu06] Szemerédi, E. and Vu, V., *Long arithmetic progressions in sumsets: thresholds and
>   bounds*. J. Amer. Math. Soc. 19 (2006), 119-169.
> - [SzVu06b] Szemerédi, E. and Vu, V., *Finite and infinite arithmetic progressions in sumsets*.
>   Ann. of Math. 163 (2006), 1-35.

*Quoted from [FormalConjectures/ErdosProblems/344.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/344.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/344](https://www.erdosproblems.com/344).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos344.erdos_344`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos344.lean#L8994](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos344.lean#L8994).

> If $A\subseteq \mathbb{N}$ is a set of integers such that
>
> $$\lvert A\cap \{1,\ldots,N\}\rvert\gg N^{1/2}$$
>
> for all $N$ then must $A$ be subcomplete? That is, must
>
> $$P(A) = \left\{\sum_{n\in B}n : B\subseteq A\textrm{ finite }\right\}$$
>
> contain an infinite arithmetic progression?
>
> This is true, and was proved by Szemerédi and Vu [SzVu06].
>
> The implied constant is absolute, as in [SzVu06b, Corollary 1.4].

```lean
theorem erdos_344 :
    ∃ C : ℝ, 0 < C ∧ ∀ A : Set ℕ,
      (∀ᶠ N : ℕ in atTop, C * Real.sqrt N ≤ A.countUpTo N) → IsSubcomplete A
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/344.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/344.lean#L57).

## `Erdos344.erdos_344.variants.sqrt_two`

Open: stated without proof.

> The stronger conjecture that this is true under
>
> $$\lvert A\cap \{1,\ldots,N\}\rvert\geq (2N)^{1/2}$$
>
> seems to be still open (this would be best possible as shown by [Er61b]).
>
> The bound is required for all sufficiently large $N$: at $N=1$, it is impossible since
> $\lvert A\cap\{1\}\rvert\leq 1\lt \sqrt{2}$.

```lean
theorem erdos_344.variants.sqrt_two :
    ∀ A : Set ℕ, (∀ᶠ N : ℕ in atTop, Real.sqrt (2 * N) ≤ A.countUpTo N) →
      IsSubcomplete A
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/344.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/344.lean#L71).

## `Erdos344.erdos_344.variants.folkman`

Proved here.

> Folkman proved this under the stronger assumption that
>
> $$\lvert A\cap \{1,\ldots,N\}\rvert\gg N^{1/2+\epsilon}$$
>
> for some $\epsilon>0$ [Fo66].

```lean
theorem erdos_344.variants.folkman :
    ∀ ε : ℝ, 0 < ε → ∀ c : ℝ, 0 < c → ∀ A : Set ℕ,
      (∀ᶠ N : ℕ in atTop, c * (N : ℝ) ^ ((1 : ℝ) / 2 + ε) ≤ A.countUpTo N) →
      IsSubcomplete A
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/344.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/344.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/344.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/344.lean)
- [erdosproblems.com/344](https://www.erdosproblems.com/344)
