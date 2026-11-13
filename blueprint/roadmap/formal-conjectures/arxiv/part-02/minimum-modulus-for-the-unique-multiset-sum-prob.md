---
declaration: theorem
origin: cited
lean: Arxiv.«2607.08366».min_modulus, Arxiv.«2607.08366».exists_isValidMod_minModulus
statement: formalized
---

# Minimum modulus for the unique multiset-sum problem

> *References:*
> - [arxiv/2607.08366](https://arxiv.org/abs/2607.08366)
>   **Minimum modulus for the unique multiset-sum problem**
>   by *José A. R. Fonollosa*
> - [jarfo/min-modulus](https://github.com/jarfo/min-modulus), the author's Lean development of
>   the paper's Main Theorem. Section 7 of the paper describes it.
>
> The paper's Main Theorem fixes the super-increasing set $\{2^k - 1\}$ and pins the least modulus
> at which *it* is valid. Conjecture 1 says no other set of $n$ residues does better, and is open.

*Quoted from [FormalConjectures/Arxiv/2607.08366/MinModulus.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2607.08366/MinModulus.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 5 API statements, counted here but not shown.

## `Arxiv.«2607.08366».min_modulus`

Open: stated without proof.

> **Conjecture 1 (Fonollosa, 2026).** For every $n \geq 2$ and every
> $N < 2^n - 2^{\lfloor \log_2 n\rfloor}$, no set of $n$ residues mod $N$ is valid.
>
> Equivalently the super-increasing set $\{2^k - 1 : 0 \leq k \leq n-1\}$ attains the least
> valid modulus, which is `minModulus n`.
>
> `0 < N` excludes `N = 0`, where `ZMod 0` is `ℤ` rather than a finite modulus and `{1, 2}` is
> valid, which would make the statement false for a reason unrelated to the question.

```lean
theorem min_modulus :
    ∀ n N : ℕ, 2 ≤ n → 0 < N → N < minModulus n →
      ∀ A : Finset (ZMod N), #A = n → ¬ IsValidMod A
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/2607.08366/MinModulus.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2607.08366/MinModulus.lean#L85).

## `Arxiv.«2607.08366».exists_isValidMod_minModulus`

Solved: stated here; a Lean proof is at [https://github.com/jarfo/min-modulus/blob/e7c78dd63955092b5f8d8a5fa826476337c0f4be/MinModulus/UniqueSums.lean#L837-L838](https://github.com/jarfo/min-modulus/blob/e7c78dd63955092b5f8d8a5fa826476337c0f4be/MinModulus/UniqueSums.lean#L837-L838).

> **Theorem A (Fonollosa, 2026).** `minModulus n` admits a valid set of `n` residues, the
> super-increasing set $\{2^k - 1 : 0 \leq k \leq n - 1\}$. This bounds the least valid modulus
> from above; that no smaller modulus works is the open half, stated in `min_modulus`.

```lean
theorem exists_isValidMod_minModulus (n : ℕ) (hn : 2 ≤ n) :
    ∃ A : Finset (ZMod (minModulus n)), #A = n ∧ IsValidMod A
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/2607.08366/MinModulus.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2607.08366/MinModulus.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2607.08366/MinModulus.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2607.08366/MinModulus.lean)
- [arxiv/2607.08366](https://arxiv.org/abs/2607.08366)
