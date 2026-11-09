---
declaration: theorem
origin: cited
lean: Erdos1134.erdos_1134, Erdos1134.erdos_1134.variants.sublinear, Erdos1134.erdos_1134.variants.klarner
statement: formalized
---

# Erdős Problem 1134

> *References:*
> - [erdosproblems.com/1134](https://www.erdosproblems.com/1134)
> - [La16] Lagarias, Jeffrey C., *Erdős, Klarner, and the $3x+1$ problem*. Amer. Math. Monthly
>   (2016), 753--776.
> - [KlRa74] Klarner, D. A. and Rado, R., *Arithmetic properties of certain recursively defined
>   sets*. Pacific J. Math. (1974), 445--463.
> - [Kl82] Klarner, David A., *A sufficient condition for certain semigroups to be free*. J. Algebra
>   (1982), 140--148.
> - [Gu83b] Guy, Richard K., *Unsolved Problems: Don't Try to Solve These Problems*. Amer. Math.
>   Monthly (1983), 35--38+39--41.
> - [Gu04] Guy, Richard K., *Unsolved problems in number theory*. (2004), xviii+437.

*Quoted from [FormalConjectures/ErdosProblems/1134.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1134.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1134](https://www.erdosproblems.com/1134).

The file states 3 research or textbook statements: 3 solved.

## `Erdos1134.erdos_1134`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1134.lean#L79](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1134.lean#L79).

> Let $A\subseteq \mathbb{N}$ be the smallest set which contains $1$ and is closed under the
> operations
> $$x\mapsto 2x+1,\quad x\mapsto 3x+1,\quad x\mapsto 6x+1.$$
> Does $A$ have positive lower density?
>
> Lagarias [La16] reports that Erdős asked this in 1972, offering £10 for a solution. (Although
> Hilton told Lagarias that this problem may have been formulated by Klarner, and that Erdős liked
> it and offered a prize for its solution.)
>
> Erdős had earlier proved (as reported in [KlRa74]) that if $A$ is the smallest set which contains
> $1$ and is closed under the operations $x\mapsto m_ix+b_i$ for some (possibly infinite) collection
> of $m_i\geq 1$ and $b_i\geq 0$ then, if $\sigma>0$ is such that $\sum \frac{1}{m_i^\sigma}=1$
> then, for all large $X$, $\lvert A\cap [1,X]\rvert \ll X^{\sigma+o(1)}$. This result does not
> help with the given problem since $\frac{1}{2}+\frac{1}{3}+\frac{1}{6}=1$.
>
> This was answered in the negative soon afterwards by Crampin and Hilton (as reported in [Kl82]),
> who proved that in fact, for all large $X$, $\lvert A\cap [1,X]\rvert \ll X^{\tau+o(1)}$ where
> $\tau\approx 0.900626$ is the unique positive root of
> $$6^{-\tau}+\sum_{k\geq 0}(3\cdot 2^k)^{-\tau}=1.$$
> Their proof is given in [La16]. This problem is repeated by Guy [Gu83b] in an article called
> 'Don't Try to Solve These Problems'. This is Problem E36 in Guy's collection [Gu04].

```lean
theorem erdos_1134 : ¬ 0 < A.lowerDensity
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1134.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1134.lean#L71).

## `Erdos1134.erdos_1134.variants.sublinear`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1134/Dirichlet.lean#L376](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1134/Dirichlet.lean#L376).

> The counting function of $A$ is sublinear: $\lvert A\cap [1,X]\rvert \ll X^{\tau+o(1)}$ with
> $\tau < 1$, so in particular $\lvert A \cap [1, X]\rvert \ll X^{19/20}$.

```lean
theorem erdos_1134.variants.sublinear :
    ∃ C : ℝ, 0 < C ∧ ∀ X : ℕ, ((A ∩ Set.Iic X).ncard : ℝ) ≤ C * (X : ℝ) ^ (19 / 20 : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1134.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1134.lean#L79).

## `Erdos1134.erdos_1134.variants.klarner`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-1134-lean/blob/57042c7e43ae71cd7008e461cf3b9d81b8d8a20f/lean/Erdos1134KlarnerFC.lean#L2110-L2113](https://github.com/KitaKen1/erdos-1134-lean/blob/57042c7e43ae71cd7008e461cf3b9d81b8d8a20f/lean/Erdos1134KlarnerFC.lean#L2110-L2113).

> Klarner has several (open) variants of this problem - see Section 8.9 of [La16]. For example, it
> is unknown if the smallest set $A$ which contains $0$ and is closed under
> $$x\mapsto 2x,\quad x\mapsto 3x+2,\quad x\mapsto 6x+3$$
> has positive density.
>
> The answer is negative: Kenta Kitamura (KitaKen1 on GitHub) has given a Lean proof
> ([erdos-1134-lean](https://github.com/KitaKen1/erdos-1134-lean)) that $A$ has natural density $0$.

```lean
theorem erdos_1134.variants.klarner :
    ¬ 0 < (⋂₀ {S : Set ℕ | 0 ∈ S ∧
      ∀ x ∈ S, 2 * x ∈ S ∧ 3 * x + 2 ∈ S ∧ 6 * x + 3 ∈ S}).lowerDensity
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1134.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1134.lean#L95).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1134.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1134.lean)
- [erdosproblems.com/1134](https://www.erdosproblems.com/1134)
