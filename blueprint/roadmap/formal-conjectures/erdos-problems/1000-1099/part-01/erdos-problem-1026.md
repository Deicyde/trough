---
declaration: theorem
origin: cited
lean: Erdos1026.erdos_1026, Erdos1026.erdos_1026.variants.upper_bound, Erdos1026.erdos_1026.variants.lower_bound, Erdos1026.erdos_1026.variants.hanani, Erdos1026.erdos_1026.variants.weighted_erdos_szekeres
statement: formalized
---

# Erdős Problem 1026

> *References:*
> - [erdosproblems.com/1026](https://www.erdosproblems.com/1026)
> - [Er71] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
> - [Ha57] Hanani, Haim, *On the number of monotonic subsequences*. Bull. Res. Council Israel
>   Sect. F (1957/58), 11-13.
> - [St95] Steele, J. Michael, *Variations on the monotone subsequence theme of Erdős and
>   Szekeres*. (1995), 111-131.
> - [TWY16] Tidor, J. and Wang, V. and Yang, B., *$1$-color avoiding paths, special tournaments,
>   and incidence geometry*. arXiv:1608.04153 (2016).
> - [Wa17] Wagner, Adam Zsolt, *Large subgraphs in rainbow-triangle free colorings*. J. Graph
>   Theory (2017), 141-148.

*Quoted from [FormalConjectures/ErdosProblems/1026.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1026.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1026](https://www.erdosproblems.com/1026).

The file states 5 research or textbook statements: 5 solved.

## `Erdos1026.erdos_1026`

Solved: stated here without proof.

> Let $x_1,\ldots,x_n$ be a sequence of distinct real numbers. Determine
>
> $$
> \max\left(\sum x_{i_r}\right),
> $$
>
> where the maximum is taken over all monotonic subsequences.
>
> This is as Erdős posed the problem in [Er71], which is rather ambiguous. Discussion between
> several users in the comments section has led to the following precise possible question, as
> posed by van Doorn:
>
> What is the largest constant $c$ such that, for all sequences of $n$ real numbers
> $x_1,\ldots,x_n$,
>
> $$
> \max\left(\sum x_{i_r}\right) > (c-o(1))\frac{1}{\sqrt{n}}\sum x_i
> $$
>
> (where again the maximum is taken over all monotonic subsequences)?
>
> Cambie makes the stronger conjecture that if $x_1,\ldots,x_{k^2}$ are distinct positive real
> numbers with $\sum x_i=1$ then there is always a monotonic subsequence with sum at least $1/k$.
>
> This stronger conjecture appears to have been first proved by Tidor, Wang, and Yang [TWY16],
> and is also implicit in work of Wagner [Wa17]. A proof was given and formalised by Aristotle
> (see the comments), with an alternative proof provided by Chan. In particular, this shows that
> $c=1$.

```lean
theorem erdos_1026 : IsGreatest admissibleConstants 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1026.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1026.lean#L94).

## `Erdos1026.erdos_1026.variants.upper_bound`

Solved: stated here without proof.

> A construction of Cambie in the comments shows that $c\leq 1$.

```lean
theorem erdos_1026.variants.upper_bound : 1 ∈ upperBounds admissibleConstants
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1026.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1026.lean#L101).

## `Erdos1026.erdos_1026.variants.lower_bound`

Solved: stated here without proof.

> Hanani [Ha57] showed that every sequence is the disjoint union of at most
> $(\sqrt{2}+o(1))\sqrt{n}$ many monotonic subsequences, whence $c\geq 1/\sqrt{2}$.

```lean
theorem erdos_1026.variants.lower_bound : 1 / Real.sqrt 2 ∈ admissibleConstants
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1026.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1026.lean#L109).

## `Erdos1026.erdos_1026.variants.hanani`

Solved: stated here without proof.

> Hanani [Ha57] showed that every sequence is the disjoint union of at most
> $(\sqrt{2}+o(1))\sqrt{n}$ many monotonic subsequences.

```lean
theorem erdos_1026.variants.hanani (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ n : ℕ in atTop, ∀ x : Fin n → ℝ, Function.Injective x →
      ∃ (m : ℕ) (I : Fin m → Finset (Fin n)),
        (∀ j, MonotoneOn x ↑(I j) ∨ AntitoneOn x ↑(I j)) ∧
        (Pairwise fun j k => Disjoint (I j) (I k)) ∧
        (Finset.univ : Finset (Fin m)).biUnion I = Finset.univ ∧
        (m : ℝ) ≤ (Real.sqrt 2 + ε) * Real.sqrt (n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1026.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1026.lean#L117).

## `Erdos1026.erdos_1026.variants.weighted_erdos_szekeres`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1026.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1026.lean).

> Cambie makes the stronger conjecture that if $x_1,\ldots,x_{k^2}$ are distinct positive real
> numbers with $\sum x_i=1$ then there is always a monotonic subsequence with sum at least $1/k$.
> This is a weighted-form of the Erdős-Szekeres theorem, and is also mentioned (as an open
> question) in a survey on the latter by Steele [St95].
>
> This stronger conjecture appears to have been first proved by Tidor, Wang, and Yang [TWY16],
> and is also implicit in work of Wagner [Wa17]. A proof was given and formalised by Aristotle
> (see the comments), with an alternative proof provided by Chan.

```lean
theorem erdos_1026.variants.weighted_erdos_szekeres (k : ℕ) (hk : 0 < k) (x : Fin (k ^ 2) → ℝ)
    (hx : Function.Injective x) (hx' : ∀ i, 0 < x i) (hsum : (∑ i, x i) = 1) :
    ∃ S ∈ monotonicSubsequenceSums x, 1 / (k : ℝ) ≤ S
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1026.lean, line 138](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1026.lean#L138).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1026.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1026.lean)
- [erdosproblems.com/1026](https://www.erdosproblems.com/1026)
