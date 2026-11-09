---
declaration: theorem
origin: cited
lean: Erdos643.erdos_643.parts.i, Erdos643.erdos_643.parts.ii, Erdos643.erdos_643.variants.exact_t_ge_four
statement: formalized
---

# Erdős Problem 643

> *References:*
> - [erdosproblems.com/643](https://www.erdosproblems.com/643)
> - [Fu84] F\"uredi, Z., Hypergraphs in which all disjoint pairs have distinct unions. Combinatorica
>   (1984), 161--168.
> - [PiVe09] Pikhurko, Oleg and Verstra\"{e}te, Jacques, The maximum size of hypergraphs without
>   generalized 4-cycles. J. Combin. Theory Ser. A (2009), 637--649.
> - [HMY26] Huang, Hao, Ma, Jie, and Yang, Tianchi, *Extremal hypergraphs without generalized
>   4-cycles*. [arXiv:2609.37744](https://arxiv.org/abs/2609.37744) (2026), Theorem 1.2.

*Quoted from [FormalConjectures/ErdosProblems/643.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/643.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/643](https://www.erdosproblems.com/643).

The file states 3 research or textbook statements: 2 open and 1 solved. It also has 1 test statement and 2 API statements, counted here but not shown.

## `Erdos643.erdos_643.parts.i`

Open: stated without proof.

> Let $f(n;t)$ be minimal such that if a $t$-uniform hypergraph on $n$ vertices contains at least
> $f(n;t)$ edges then there must be four edges $A,B,C,D$ such that
> $$A\cup B= C\cup D$$
> and
> $$A\cap B=C\cap D=\emptyset.$$
> Estimate $f(n;t)$ - in particular, is it true that for $t\geq 3$
> $$f(n;t)=(1+o(1))\binom{n}{t-1}?$$

```lean
theorem erdos_643.parts.i :
    ∀ t : ℕ, 1 ≤ t →
      (fun n ↦ (forcingThreshold n t : ℝ)) ~[atTop] erdos_643.parts.i.answer t
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/643.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/643.lean#L56).

## `Erdos643.erdos_643.parts.ii`

Open: stated without proof.

> Is it true that $f(n;t)=(1+o(1))\binom{n}{t-1}$ for $t\geq 3$?
>
> For $t\geq4$, Huang, Ma, and Yang [HMY26] prove the exact extremal formula below.
> The case $t=3$ remains open.

```lean
theorem erdos_643.parts.ii :
    ∀ t : ℕ, 3 ≤ t →
    (fun n ↦ (forcingThreshold n t : ℝ)) ~[atTop]
        (fun n ↦ (n.choose (t - 1) : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/643.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/643.lean#L68).

## `Erdos643.erdos_643.variants.exact_t_ge_four`

Solved: stated here without proof.

> Huang, Ma, and Yang [HMY26, Theorem 1.2] determine the maximum size of an avoiding family
> for each fixed $t\geq4$ and all sufficiently large $n$:
> $$\binom{n-1}{t-1}+\left\lfloor\frac{n-1}{t}\right\rfloor.$$
> The forcing threshold is one larger.

```lean
theorem erdos_643.variants.exact_t_ge_four :
    ∀ t : ℕ, 4 ≤ t → ∀ᶠ n : ℕ in atTop,
      Hypergraph.extremalNumber n t (fun H ↦ ¬ H.HasRepeatedDisjointUnion) =
        (n - 1).choose (t - 1) + (n - 1) / t
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/643.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/643.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/643.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/643.lean)
- [erdosproblems.com/643](https://www.erdosproblems.com/643)
