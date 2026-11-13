---
declaration: theorem
origin: cited
lean: Erdos872.erdos_872.parts.i, Erdos872.erdos_872.parts.ii, Erdos872.erdos_872.trivial_upper_bound, Erdos872.erdos_872.variants.prime_question
statement: formalized
---

# Erdős Problem 872

> This file states Erdős Problem 872 for the primitive-set saturation game on $\{2, \dots, n\}$.
> The game value `L n` is defined by a finite minimax recursion: Prolonger moves first and maximizes
> the final size of the claimed primitive set, while Shortener minimizes it.
>
> The problem statement does not fix the turn order. This file fixes Prolonger to move first,
> following the convention used in the forum discussion of the problem. The choice is not cosmetic:
> computational data suggests the Shortener-first value tracks $\pi(n)$ while the Prolonger-first
> value grows linearly, and the questions below concern the Prolonger-first quantity.
>
> *References:*
> - [erdosproblems.com/872](https://www.erdosproblems.com/872)
> - [erdosproblems.com/forum/thread/872](https://www.erdosproblems.com/forum/thread/872)

*Quoted from [FormalConjectures/ErdosProblems/872.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/872.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/872](https://www.erdosproblems.com/872).

The file states 4 research or textbook statements: 1 open, 2 solved and 1 textbook result. It also has 2 API statements, counted here but not shown.

## `Erdos872.erdos_872.parts.i`

Open: stated without proof.

> Erdős Problem 872, part (i) (weak form): there exists a constant $\epsilon > 0$ such that the
> game length is at least $\epsilon \cdot n$ for all sufficiently large $n$.

```lean
theorem erdos_872.parts.i :
    ∃ ε > (0 : ℝ), ∀ᶠ n in atTop, (L n : ℝ) ≥ ε * n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [91 Game theory, economics, social and behavioral sciences](../../../by-subject/part-03/91-game-theory-economics-social-and-behavioral-scie/README.md). Declared in [FormalConjectures/ErdosProblems/872.lean, line 161](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/872.lean#L161).

## `Erdos872.erdos_872.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/ilpauzner/formal-conjectures/blob/d9299da16287d2347e375d9eec253eec455bae75/FormalConjectures/ErdosProblems/872.lean#L1180](https://github.com/ilpauzner/formal-conjectures/blob/d9299da16287d2347e375d9eec253eec455bae75/FormalConjectures/ErdosProblems/872.lean#L1180).

> Erdős Problem 872, part (ii) (strong form): for every $\epsilon > 0$, the game length is at
> least $(1-\epsilon) \cdot n / 2$ for all sufficiently large $n$.
>
> The forum thread (April-May 2026) records Shortener strategies giving
> $L(n) \leq (23/48 + o(1)) \cdot n$ (described in the thread as accepted as correct, with a Lean
> formalization in progress) and a claimed $L(n) \leq 0.19 \cdot n$, either of which would answer this
> question negatively under the Prolonger-first convention.
>
> The $23/48$ upper bound for `C`-respecting plays (following old-bielefelder's strategy in the
> forum thread) was formalized in Lean 4 by Pommeret using Aristotle and Claude Opus 4.7, and
> completed to a proof for the full minimax game value `L n` by Ilia Pauzner using Gemini 4 Argon.

```lean
theorem erdos_872.parts.ii :
    ¬ ∀ ε > (0 : ℝ), ∀ᶠ n in atTop, (L n : ℝ) ≥ (1 - ε) * n / 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [91 Game theory, economics, social and behavioral sciences](../../../by-subject/part-03/91-game-theory-economics-social-and-behavioral-scie/README.md). Declared in [FormalConjectures/ErdosProblems/872.lean, line 178](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/872.lean#L178).

## `Erdos872.erdos_872.trivial_upper_bound`

Textbook result, proved here.

> A trivial upper bound: a play can claim at most the $n - 1$ elements of $\{2, \dots, n\}$, so
> $L(n) \leq n - 1$.

```lean
theorem erdos_872.trivial_upper_bound (n : ℕ) (hn : 2 ≤ n) :
    L n ≤ n - 1
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [91 Game theory, economics, social and behavioral sciences](../../../by-subject/part-03/91-game-theory-economics-social-and-behavioral-scie/README.md). Declared in [FormalConjectures/ErdosProblems/872.lean, line 185](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/872.lean#L185).

## `Erdos872.erdos_872.variants.prime_question`

Solved: stated here; a Lean proof is at [https://github.com/mnn31/erdos-lean/blob/5cb725981b3ad137103ef908eb6ecff9e7ed9bdf/ErdosLean/Erdos872.lean#L114](https://github.com/mnn31/erdos-lean/blob/5cb725981b3ad137103ef908eb6ecff9e7ed9bdf/ErdosLean/Erdos872.lean#L114).

> Forum-related variant: how small can a maximal primitive subset of $\{2, \dots, n\}$ be?
> The set of primes in $\{2, \dots, n\}$ is a maximal primitive subset of size $\pi(n)$, and the forum
> thread asks whether this is the smallest possible for all $n \geq 2$. Equivalently: must every
> completed play of the saturation game, by both players and regardless of strategy, claim at least
> $\pi(n)$ elements? (Terminal positions of the game are exactly the maximal primitive subsets.)
>
> The answer is yes. For each prime $q \le n$, let $q^k$ be the largest power of $q$ that is at most
> $n$. Maximality gives an element of $A$ comparable with $q^k$ under divisibility, and no element is
> comparable with two such prime powers, so $|A| \ge \pi(n)$. This argument was posted on the forum
> by old-bielefelder (May 2026); the statement also appears as Theorem 2.3(i) of
> [El23] S. Elsakhawy, *Independence and domination in divisor graph and mod-difference graphs*,
> J. Egyptian Math. Soc. 31 (2023).

```lean
theorem erdos_872.variants.prime_question :
    ∀ n ≥ 2, ∀ A : Finset ℕ, Maximal (IsPrimitive n) A →
      ((Finset.Icc 2 n).filter Nat.Prime).card ≤ A.card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [91 Game theory, economics, social and behavioral sciences](../../../by-subject/part-03/91-game-theory-economics-social-and-behavioral-scie/README.md). Declared in [FormalConjectures/ErdosProblems/872.lean, line 208](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/872.lean#L208).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/872.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/872.lean)
- [erdosproblems.com/872](https://www.erdosproblems.com/872)
