---
declaration: theorem
origin: cited
lean: Erdos789.erdos_789, Erdos789.erdos_789.variants.sq, Erdos789.erdos_789.variants.isBigO_sq, Erdos789.erdos_789.variants.sq_isBigO, Erdos789.erdos_789.variants.sqrt_loglog_div_log_isBigO, Erdos789.erdos_789.variants.cube_root_linearithmic_isBigO, Erdos789.erdos_789.variants.isBigO_cube_root_linearithmic, Erdos789.erdos_789.variants.cube_root_linearithmic
statement: formalized
---

# Erdős Problem 789

> In this problem, a function $h : \mathbb{N} \to\mathbb{N}$ is defined maximally by
> some counting property.
>
> The problem asks to estimate $h(n)$. This has been interpreted here as asking for $\Theta(h(n))$.
> The principal version includes the unknown function `erdos_789.answer`.
>
> Straus [Str66] proved that $h(n) \ll \sqrt{n}$. Erdős [Er62c] and Choi [Ch74b] proved that
> $(n\log(n))^{1/3} \ll h(n)$. Korsky [Ko26] improved this to $h(n) \gg \sqrt{n\log\log n/\log n}$.
> The variants record these bounds and the open question whether $h(n) = \Theta(\sqrt{n})$. The file
> proves Korsky's bound, following [Ko26], and derives from it the Erdős–Choi bound and
> $h(n) \neq O((n\log(n))^{1/3})$.
>
> *References:*
> - [erdosproblems.com/789](https://www.erdosproblems.com/789)
> - [Str66] Straus, E. G., _On a problem in combinatorial number theory_. J. Math. Sci. (1966), 77--80.
> - [Er62c] Erdős, Pál, _Some remarks on number theory_. {III}. Mat. Lapok (1962), 28--38.
> - [Ch74b] Choi, S. L. G., _On an extremal problem in number theory_. J. Number Theory (1974), 105--111.
> - [Ko26] Korsky, S., _A near-square-root bound for an additive problem of Erdős and Straus_ (2026).
>   [Proof claim](https://www.erdosproblems.com/forum/thread/789/proof-claims).

*Quoted from [FormalConjectures/ErdosProblems/789.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/789.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/789](https://www.erdosproblems.com/789).

The file states 8 research or textbook statements: 3 open and 5 solved.

## `Erdos789.erdos_789`

Open: stated without proof.

> Let $h(n)$ be maximal such that if $A\subseteq \mathbb{Z}$ with $\lvert A\rvert=n$
> then there is $B\subseteq A$ with $\lvert B\rvert \geq h(n)$ such that if
> $a_1+\cdots+a_r=b_1+\cdots+b_s$ with $a_i,b_i\in B$ then $r=s$.
>
> Estimate $h(n)$.

```lean
theorem erdos_789 :
    (fun n ↦ (subsetSumThreshold n : ℝ)) =Θ[atTop] erdos_789.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/789.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/789.lean#L75).

## `Erdos789.erdos_789.variants.sq`

Open: stated without proof.

> Let $h(n)$ be maximal such that if $A\subseteq \mathbb{Z}$ with $\lvert A\rvert=n$
> then there is $B\subseteq A$ with $\lvert B\rvert \geq h(n)$ such that if
> $a_1+\cdots+a_r=b_1+\cdots+b_s$ with $a_i,b_i\in B$ then $r=s$.
>
> Is $h(n) = \Theta(\sqrt{n})$?

```lean
theorem erdos_789.variants.sq :
    (fun n ↦ (subsetSumThreshold n : ℝ)) =Θ[atTop] fun n ↦ √n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/789.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/789.lean#L87).

## `Erdos789.erdos_789.variants.isBigO_sq`

Solved: stated here without proof.

> Straus [Str66] proved that $h(n) \ll \sqrt{n}$.

```lean
theorem erdos_789.variants.isBigO_sq :
    (fun n ↦ (subsetSumThreshold n : ℝ)) =O[atTop] fun n ↦ √n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/789.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/789.lean#L93).

## `Erdos789.erdos_789.variants.sq_isBigO`

Open: stated without proof.

> By the solved variant `erdos_789.variants.isBigO_sq`, in order to prove
> `erdos_789.variants.sq` it suffices to show $\sqrt{n}=O(h(n))$.

```lean
theorem erdos_789.variants.sq_isBigO :
    (fun n : ℕ ↦ √n) =O[atTop] fun n ↦ (subsetSumThreshold n : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/789.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/789.lean#L100).

## `Erdos789.erdos_789.variants.sqrt_loglog_div_log_isBigO`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/57a0dc60e2cc245b69870647d122fb851f72d8e4/FormalConjectures/ErdosProblems/789.lean#L907](https://github.com/mo271/formal-conjectures/blob/57a0dc60e2cc245b69870647d122fb851f72d8e4/FormalConjectures/ErdosProblems/789.lean#L907).

> Korsky [Ko26] proved that $h(n) \gg \sqrt{n\log\log n/\log n}$.

```lean
theorem erdos_789.variants.sqrt_loglog_div_log_isBigO :
    (fun n : ℕ ↦ √(n * Real.log (Real.log n) / Real.log n)) =O[atTop]
      fun n ↦ (subsetSumThreshold n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/789.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/789.lean#L109).

## `Erdos789.erdos_789.variants.cube_root_linearithmic_isBigO`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/57a0dc60e2cc245b69870647d122fb851f72d8e4/FormalConjectures/ErdosProblems/789.lean#L973](https://github.com/mo271/formal-conjectures/blob/57a0dc60e2cc245b69870647d122fb851f72d8e4/FormalConjectures/ErdosProblems/789.lean#L973).

> Erdős [Er62c] and Choi [Ch74b] proved that $(n\log(n))^{1/3}\ll h(n)$. This also follows from
> `erdos_789.variants.sqrt_loglog_div_log_isBigO`.

```lean
theorem erdos_789.variants.cube_root_linearithmic_isBigO :
    (fun n : ℕ ↦ (n * Real.log n) ^ ((1 : ℝ) / 3)) =O[atTop]
      fun n ↦ (subsetSumThreshold n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/789.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/789.lean#L120).

## `Erdos789.erdos_789.variants.isBigO_cube_root_linearithmic`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/57a0dc60e2cc245b69870647d122fb851f72d8e4/FormalConjectures/ErdosProblems/789.lean#L981](https://github.com/mo271/formal-conjectures/blob/57a0dc60e2cc245b69870647d122fb851f72d8e4/FormalConjectures/ErdosProblems/789.lean#L981).

> It is not true that $h(n) = O((n\log(n))^{1/3})$. This follows from
> `erdos_789.variants.sqrt_loglog_div_log_isBigO` [Ko26].

```lean
theorem erdos_789.variants.isBigO_cube_root_linearithmic :
    ¬ (fun n ↦ (subsetSumThreshold n : ℝ)) =O[atTop]
      fun n ↦ (n * Real.log n) ^ ((1 : ℝ) / 3)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/789.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/789.lean#L130).

## `Erdos789.erdos_789.variants.cube_root_linearithmic`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/57a0dc60e2cc245b69870647d122fb851f72d8e4/FormalConjectures/ErdosProblems/789.lean#L994](https://github.com/mo271/formal-conjectures/blob/57a0dc60e2cc245b69870647d122fb851f72d8e4/FormalConjectures/ErdosProblems/789.lean#L994).

> It is not true that $h(n) = \Theta((n\log(n))^{1/3})$. This follows from
> `erdos_789.variants.isBigO_cube_root_linearithmic`.

```lean
theorem erdos_789.variants.cube_root_linearithmic :
    ¬ (fun n ↦ (subsetSumThreshold n : ℝ)) =Θ[atTop]
      fun n ↦ (n * Real.log n) ^ ((1 : ℝ) / 3)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/789.lean, line 140](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/789.lean#L140).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/789.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/789.lean)
- [erdosproblems.com/789](https://www.erdosproblems.com/789)
