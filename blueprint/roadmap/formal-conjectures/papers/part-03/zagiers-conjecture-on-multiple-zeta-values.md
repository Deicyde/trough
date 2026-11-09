---
declaration: theorem
origin: cited
lean: ZagierMZV.zagier_conjecture, ZagierMZV.zagier_upper_bound
statement: formalized
---

# Zagier's Conjecture on Multiple Zeta Values

> *References:*
> - [Za94] Zagier, Don. "Values of zeta functions and their applications."
>   First European Congress of Mathematics Paris, July 6–10, 1992: Vol. II: Invited Lectures (Part 2). Basel: Birkhäuser Basel, 1994.
> - [Co18] Combariza, Germán AG. "A few conjectures about the multiple zeta values."
>   ACM Communications in Computer Algebra 52.1 (2018): 11-20.
> - [Te02] T. Terasoma. Mixed Tate motives and multiple zeta values. Invent. Math., 149(2):339–369, 2002.
> - [DG05] P. Deligne and A. Goncharov. Groupes fondamentaux motiviques de Tate mixte. Ann. Sci.
>   Ecole Norm. Sup. (4), 38(1):1–56, 2005.
> - [OEIS A000931](https://oeis.org/A000931)

*Quoted from [FormalConjectures/Paper/ZagierMZV.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/ZagierMZV.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 7 test statements, counted here but not shown.

## `ZagierMZV.zagier_conjecture`

Open: stated without proof.

> **Zagier's conjecture**
>
> The $\mathbb{Q}$-dimension of the vector space spanned by all multiple zeta values
> of weight $n$ equals $d_n$, where $d_n$ is the Zagier dimension sequence
> satisfying $d_0 = 1$, $d_1 = 0$, $d_2 = 1$, and $d_n = d_{n-2} + d_{n-3}$ for $n \geq 3$.

```lean
theorem zagier_conjecture :
    ∀ n : ℕ, Module.finrank ℚ (mzvSpanOfWeight n) = zagierDim n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/ZagierMZV.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/ZagierMZV.lean#L97).

## `ZagierMZV.zagier_upper_bound`

Solved: stated here without proof.

> **Upper bound** [Te02, DG05]
>
> The dimension of the $\mathbb{Q}$-vector space of MZVs of weight $n$ is at most $d_n$.

```lean
theorem zagier_upper_bound :
    ∀ n : ℕ, Module.finrank ℚ (mzvSpanOfWeight n) ≤ zagierDim n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/ZagierMZV.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/ZagierMZV.lean#L107).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/ZagierMZV.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/ZagierMZV.lean)
- [OEIS A000931](https://oeis.org/A000931)
