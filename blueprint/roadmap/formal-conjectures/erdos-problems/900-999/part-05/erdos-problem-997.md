---
declaration: theorem
origin: cited
lean: Erdos997.erdos_997, Erdos997.erdos_997.variants.lacunary, Erdos997.erdos_997.variants.irrational
statement: formalized
---

# Erdős Problem 997

> *References:*
> - [erdosproblems.com/997](https://www.erdosproblems.com/997)
> - [APSSV26] B. Alexeev, M. Putterman, M. Sawhney, M. Sellke, and G. Valiant,
>   [Short proofs in combinatorics and number theory](https://arxiv.org/abs/2603.29961).
>   arXiv:2603.29961 (2026).
> - [CLLW24] J. Champagne, T. Le, Y.-R. Liu, and T. D. Wooley, Well-distribution modulo one and the
>   primes. arXiv:2406.19491 (2024).
> - [Er64b] Erdős, P., Problems and results on diophantine approximations. Compositio Math. (1964),
>   52-65.
> - [Er85e] Erdős, P., Some problems and results in number theory. Number theory and combinatorics.
>   Japan 1984 (Tokyo, Okayama and Kyoto, 1984) (1985), 65-87.
> - [Hl55] Hlawka, Edmund, Zur formalen {T}heorie der {G}leichverteilung in kompakten {G}ruppen. Rend.
>   Circ. Mat. Palermo (2) (1955), 33--47.
> - [Mo26] P. Monticone, [Lean formalisation of Erdős problem 997](https://live.lean-lang.org/#project=mathlib-v4.28.0&url=https://gist.githubusercontent.com/pitmonticone/016f2ed66b4cd1c4c4b9998095170e60/raw/b7dfc05c525ae385b5835f89f1ada721443e4305/Erdos997.lean) (2026)

*Quoted from [FormalConjectures/ErdosProblems/997.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/997.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/997](https://www.erdosproblems.com/997).

The file states 3 research or textbook statements: 3 solved.

## `Erdos997.erdos_997`

Solved: stated here; a Lean proof is at [https://gist.githubusercontent.com/pitmonticone/016f2ed66b4cd1c4c4b9998095170e60/raw/b7dfc05c525ae385b5835f89f1ada721443e4305/Erdos997.lean](https://gist.githubusercontent.com/pitmonticone/016f2ed66b4cd1c4c4b9998095170e60/raw/b7dfc05c525ae385b5835f89f1ada721443e4305/Erdos997.lean).

> Is it true that, for every $\alpha$, the sequence $\{ \alpha p_n\}$ is not well-distributed,
> if $p_n$ is the sequence of primes?
>
> The answer is yes, by [APSSV26, Section 4]; a Lean formalisation is available in [Mo26].

```lean
theorem erdos_997 :
    ∀ α : ℝ, ¬ IsWellDistributed (fun n ↦ Int.fract (α * (n.nth Nat.Prime)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/997.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/997.lean#L68).

## `Erdos997.erdos_997.variants.lacunary`

Solved: stated here without proof.

> Erdős proved that, if $n_k$ is a lacunary sequence, then the sequence $\{ \alpha n_k\}$ is not
> well-distributed for almost all $\alpha$.

```lean
theorem erdos_997.variants.lacunary (n : ℕ → ℕ) (h : IsLacunary n) :
    ∀ᵐ α, ¬ IsWellDistributed (fun k ↦ Int.fract (α * (n k : ℝ)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/997.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/997.lean#L77).

## `Erdos997.erdos_997.variants.irrational`

Solved: stated here without proof.

> He also claimed in [Er64b] to have proved that there exists an irrational $\alpha$ for which
> $\{\alpha p_n\}$ is not well-distributed. He later retracted this claim in [Er85e], saying "The
> theorem is no doubt correct and perhaps will not be difficult to prove but I never was able to
> reconstruct my 'proof' which perhaps never existed."
>
> The existence of such an $\alpha$ was established by Champagne, Le, Liu, and Wooley [CLLW24].

```lean
theorem erdos_997.variants.irrational :
    ∃ α : ℝ, Irrational α ∧
      ¬ IsWellDistributed (fun n ↦ Int.fract (α * (n.nth Nat.Prime)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/997.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/997.lean#L90).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/997.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/997.lean)
- [erdosproblems.com/997](https://www.erdosproblems.com/997)
