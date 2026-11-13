---
declaration: theorem
origin: cited
lean: Erdos270.erdos_270, Erdos270.erdos_270.variants.every_value, Erdos270.erdos_270.variants.monotone, Erdos270.erdos_270.variants.linear
statement: formalized
---

# Erdős Problem 270

> *References:*
> - [erdosproblems.com/270](https://www.erdosproblems.com/270)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Ha75] Hansen, E. R., *A Table of Series and Products*. Prentice-Hall (1975), 87.
> - [CrKo25] T. Crmarić and V. Kovač, *On the irrationality of certain super-polynomially decaying
>   series*. arXiv:2504.18712 (2025).
> - [Ko26] V. Kovač, [solution of the linear case](https://www.erdosproblems.com/forum/thread/270#post-7469)
>   (2026).

*Quoted from [FormalConjectures/ErdosProblems/270.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/270.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/270](https://www.erdosproblems.com/270).

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Erdos270.erdos_270`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos270.lean#L1027](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos270.lean#L1027).

> Let $f(n)\to \infty$ as $n\to \infty$. Is it true that
>
> $$\sum_{n\geq 1} \frac{1}{(n+1)\cdots (n+f(n))}$$
>
> is irrational?
>
> Erdős and Graham [ErGr80] write 'the answer is almost surely in the affirmative if $f(n)$ is
> assumed to be nondecreasing'. The case $f(n)=n$ was subsequently settled by Crmarić and Kovač
> [Ko26]. Hansen [Ha75] has
> shown that
>
> $$\sum_n \frac{1}{\binom{2n}{n}}=\sum_n \frac{n!}{(n+1)\cdots (n+n)}=\frac{1}{3}+\frac{2\pi}{3^{5/2}}$$
>
> is transcendental.
>
> Crmarić and Kovač [CrKo25] have shown that the answer to this question is no in a strong sense:
> for any $\alpha \in (0,\infty)$ there exists a function $f:\mathbb{N}\to\mathbb{N}$ such that
> $f(n)\to \infty$ as $n\to\infty$ and
>
> $$\sum_{n\geq 1} \frac{1}{(n+1)\cdots (n+f(n))}=\alpha.$$

```lean
theorem erdos_270 :
    ¬ ∀ f : ℕ → ℕ, Tendsto f atTop atTop → Irrational (series f)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/270.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/270.lean#L64).

## `Erdos270.erdos_270.variants.every_value`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos270.lean#L1009](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos270.lean#L1009).

> Crmarić and Kovač [CrKo25]: for any $\alpha \in (0,\infty)$ there exists a function
> $f:\mathbb{N}\to\mathbb{N}$ such that $f(n)\to \infty$ as $n\to\infty$ and
>
> $$\sum_{n\geq 1} \frac{1}{(n+1)\cdots (n+f(n))}=\alpha.$$

```lean
theorem erdos_270.variants.every_value (α : ℝ) (hα : 0 < α) :
    ∃ f : ℕ → ℕ, Tendsto f atTop atTop ∧
      HasSum (fun n : ℕ => (∏ i ∈ Finset.Icc (n + 2) (n + 1 + f (n + 1)), (i : ℝ))⁻¹) α
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/270.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/270.lean#L76).

## `Erdos270.erdos_270.variants.monotone`

Open: stated without proof.

> It is still possible that this sum is always irrational if $f$ is assumed to be non-decreasing;
> Crmarić and Kovač [CrKo25] show that the set of the possible values of such a sum has Lebesgue
> measure zero.

```lean
theorem erdos_270.variants.monotone :
    ∀ f : ℕ → ℕ, Monotone f → Tendsto f atTop atTop → Irrational (series f)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/270.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/270.lean#L87).

## `Erdos270.erdos_270.variants.linear`

Solved: stated here without proof.

> The case $f(n)=n$ has a positive answer, as observed by Crmarić and Kovač [Ko26]:
> $\sum_{n\geq 1} n!/(2n)!$ is irrational.

```lean
theorem erdos_270.variants.linear : Irrational (series id)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/270.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/270.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/270.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/270.lean)
- [erdosproblems.com/270](https://www.erdosproblems.com/270)
