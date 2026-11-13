---
declaration: theorem
origin: cited
lean: Rule30.centerColumn_not_eventually_periodic, Rule30.centerColumn_frequency_half
statement: formalized
---

# The Rule 30 Prize Problems

> **Rule 30** is the elementary cellular automaton with local update $c' = l \oplus (c \lor r)$,
> the Boolean rule numbered $30$ by Wolfram. Started from a single black cell on a bi-infinite row,
> its **center column** `t ↦ (state t) 0` looks random — it was long *Mathematica*'s default
> pseudorandom generator — yet nothing about that randomness is proven. In 2019 Wolfram offered
> the **Rule 30 Prizes** for three questions about it; we formalize the first two.
>
> * **Problem 1.** Is the center column non-periodic (never eventually periodic)?
> * **Problem 2.** Does each color occur on average equally often, i.e. does the running average
>   of the values converge to $1/2$?
>
> Problem 3 — whether computing the $n$-th cell requires at least $O(n)$ work — is omitted. It is
> model-relative and has no canonical model-independent phrasing. All three are open.
>
> *References:*
> - [Announcing the Rule 30 Prizes](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/),
>   Stephen Wolfram, 2019.
> - [Rule 30 Prizes](https://rule30prize.org/).
> - [Wikipedia: Rule 30](https://en.wikipedia.org/wiki/Rule_30).

*Quoted from [FormalConjectures/Other/Rule30.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/Rule30.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 1 test statement and 2 API statements, counted here but not shown.

## `Rule30.centerColumn_not_eventually_periodic`

Open: stated without proof.

> **Rule 30 Prize, Problem 1 (non-periodicity).** The center column of Rule 30 is not
> eventually periodic: there is no positive period $p$ and threshold $N$ past which the column
> repeats with period $p$.

```lean
theorem centerColumn_not_eventually_periodic :
    ¬ ∃ p : ℕ, 0 < p ∧ ∃ N : ℕ, ∀ t : ℕ, N ≤ t → centerColumn (t + p) = centerColumn t
```

Category `research open`; AMS [37 Dynamical systems and ergodic theory](../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md), [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Other/Rule30.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/Rule30.lean#L81).

## `Rule30.centerColumn_frequency_half`

Open: stated without proof.

> **Rule 30 Prize, Problem 2 (equal frequency).** Each color occurs on average equally often
> in the center column: the set of times at which it is black has natural density $1/2$. This is
> Wolfram's phrasing that the discrete limit of $\mathrm{Total}[c[t]]/t$ as $t \to \infty$ is
> $1/2$.

```lean
theorem centerColumn_frequency_half :
    {t : ℕ | centerColumn t}.HasDensity (1 / 2)
```

Category `research open`; AMS [37 Dynamical systems and ergodic theory](../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md), [68 Computer science](../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Other/Rule30.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/Rule30.lean#L90).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Other/Rule30.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/Rule30.lean)
- [Announcing the Rule 30 Prizes](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/)
