---
declaration: theorem
origin: cited
lean: Bugeaud32.adamczewski_faverjon, Bugeaud32.problem_10_32.variants.strong, Bugeaud32.problem_10_32
statement: formalized
---

# Bugeaud Collection of Conjectures and Open Questions: Automatic Expansions in Two Bases

> Problem 10.32 asks whether some irrational real number has automatic expansions in two
> multiplicatively independent bases. The answer is no. Adamczewski and Faverjon [AF20] proved
> it with the multivariate Mahler method, in a form that is stronger than the question asked:
> the base-$b$ digit sequence may be $k$-automatic for an arbitrary $k \ge 2$, not only for
> $k = b$.
>
> The definitions used here are in `FormalConjecturesForMathlib`:
> `Nat.MultiplicativelyIndependent` and `Nat.MultiplicativelyIndependentFamily`,
> `AutomaticSequence.IsAutomatic`, `AutomaticSequence.IsAutomaticInBase` and
> `AutomaticSequence.IsBroadlyAutomaticInBase`.
>
> *References:*
>   - [AF20](https://arxiv.org/abs/2012.08283) Adamczewski, Boris, and Colin Faverjon.
>     "Mahler's method in several variables and finite automata." arXiv:2012.08283 (2020).
>     Appendix A, Conjectures A.2 and A.3, both proved there from Part (i) of Theorem 1.1.
>   - [AS03] Allouche, Jean-Paul, and Jeffrey Shallit. "Automatic Sequences: Theory,
>     Applications, Generalizations." Cambridge University Press, 2003. Chapter 13,
>     Open Problems 7, p. 403, is the problem that Problem 10.32 modifies.
>   - [Bug12] Bugeaud, Yann. "Distribution modulo one and Diophantine approximation."
>     Vol. 193. Cambridge University Press, 2012. Chapter 10.
>   - [Cob69] Cobham, Alan. "On the base-dependence of sets of numbers recognizable by finite
>     automata." Mathematical Systems Theory 3 (1969): 186-192.
>   - [LvdP82] Loxton, John H., and Alfred J. van der Poorten. "Arithmetic properties of the
>     solutions of a class of functional equations." Journal für die reine und angewandte
>     Mathematik 330 (1982): 159-172. Its transcendence method was the first attack on the
>     problem; Nishioka later reported a gap in its main proof.

*Quoted from [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_32.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_32.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved.

## `Bugeaud32.adamczewski_faverjon`

Solved: stated here without proof.

> **Adamczewski–Faverjon** [AF20, Conjecture A.3], proved there from Part (i) of Theorem 1.1.
> Let $b_1, \dots, b_r$ be multiplicatively independent positive integers, and for every $i$ let
> $\xi_i$ be a real number that is automatic in base $b_i$. Then $\xi_1, \dots, \xi_r$ are
> algebraically independent over $\mathbb{Q}$, unless one of them is rational.
>
> Two points of fidelity. The hypothesis is the *joint* multiplicative independence of
> $b_1, \dots, b_r$ that [AF20] defines on p. 3 (no nonzero integer tuple $(n_i)$ has
> $\prod_i b_i^{n_i} = 1$), not the weaker pairwise condition; it is what the proof feeds to
> Part (i) of Theorem 1.1, via the multiplicative independence of $1/b_1, \dots, 1/b_r$.
> Automaticity is the broad notion that the proof of Conjecture A.3 uses: the base-$b_i$ digits
> of $\xi_i$ are $k$-automatic for some $k \ge 2$, which need not be $b_i$.

```lean
theorem adamczewski_faverjon {r : ℕ} (b : Fin r → ℕ) (hb : ∀ i, 2 ≤ b i)
    (hind : Nat.MultiplicativelyIndependentFamily b)
    (ξ : Fin r → ℝ) (hauto : ∀ i, IsBroadlyAutomaticInBase (b i) (ξ i))
    (hirr : ∀ i, Irrational (ξ i)) :
    AlgebraicIndependent ℚ ξ
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_32.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_32.lean#L71).

## `Bugeaud32.problem_10_32.variants.strong`

Proved here.

> Problem 10.32, strong form. No irrational real number is automatic in two multiplicatively
> independent bases, in the broad sense that its digit sequence in each of the two bases is
> `k`-automatic for some `k`. This is [AF20, Conjecture A.2], with the broad notion of
> automaticity that its proof provides.

```lean
theorem problem_10_32.variants.strong (ξ : ℝ) (hξ : Irrational ξ) (b₁ b₂ : ℕ)
    (hb₁ : 2 ≤ b₁) (hb₂ : 2 ≤ b₂) (hind : Nat.MultiplicativelyIndependent b₁ b₂)
    (h₁ : IsBroadlyAutomaticInBase b₁ ξ) (h₂ : IsBroadlyAutomaticInBase b₂ ξ) : False
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_32.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_32.lean#L85).

## `Bugeaud32.problem_10_32`

Proved here.

> Problem 10.32. Is there an irrational real number whose expansions in two multiplicatively
> independent bases can both be generated by a finite automaton? The answer is no, by [AF20].

```lean
theorem problem_10_32 :
    ¬ ∃ ξ : ℝ, Irrational ξ ∧ ∃ b₁ b₂ : ℕ, 2 ≤ b₁ ∧ 2 ≤ b₂ ∧
      Nat.MultiplicativelyIndependent b₁ b₂ ∧
      IsAutomaticInBase b₁ ξ ∧ IsAutomaticInBase b₂ ξ
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_32.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_32.lean#L103).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_32.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_32.lean)
- [AF20](https://arxiv.org/abs/2012.08283)
