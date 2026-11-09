---
declaration: theorem
origin: cited
lean: Erdos302.erdos_302.parts.i, Erdos302.erdos_302.parts.ii, Erdos302.erdos_302.variants.lower_half, Erdos302.erdos_302.variants.lower_five_eighths, Erdos302.erdos_302.variants.upper_nine_tenths, Erdos302.erdos_302.variants.upper_0_8461739827964010
statement: formalized
---

# Erdős Problem 302

> *References:*
> - [erdosproblems.com/302](https://www.erdosproblems.com/302)
> - [BrRo91] Brown, Tom C. and Rödl, Voijtech, Monochromatic solutions to equations with unit
>   fractions. Bull. Austral. Math. Soc. (1991), 387-392.
> - [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number
>   theory. Monographies de L'Enseignement Mathematique (1980).
> - [va25](https://github.com/Woett/Mathematical-shorts/blob/main/Two-colouring%20and%20density%20lead%20to%20solutions%20to%20an%20equation%20in%20unit%20fractions.pdf)

*Quoted from [FormalConjectures/ErdosProblems/302.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/302.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/302](https://www.erdosproblems.com/302).

The file states 6 research or textbook statements: 1 open and 5 solved.

## `Erdos302.erdos_302.parts.i`

Open: stated without proof.

> Let $f(N)$ be the size of the largest $A\subseteq \{1,\ldots,N\}$ such that there are no
> solutions to
>
> $$\frac{1}{a}= \frac{1}{b}+\frac{1}{c}$$
>
> with distinct $a,b,c\in A$? Estimate $f(N)$.
>
> The colouring version of this is [303], which was solved by Brown and Rödl [BrRo91].

```lean
theorem erdos_302.parts.i (f : ℕ → ℕ) (hf : ∀ N, IsMaxNoTripleCard N (f N)) :
    Tendsto (fun N : ℕ => (f N : ℝ) / N) atTop (𝓝 erdos_302.parts.i.answer)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/302.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/302.lean#L65).

## `Erdos302.erdos_302.parts.ii`

Solved: stated here without proof.

> In particular, is $f(N)=(\tfrac{1}{2}+o(1))N$?
>
> This is false: it is contradicted by Cambie's lower bound of $(5/8+o(1))N$ recorded below,
> since $5/8 > 1/2$.

```lean
theorem erdos_302.parts.ii (f : ℕ → ℕ) (hf : ∀ N, IsMaxNoTripleCard N (f N)) :
    ¬ Tendsto (fun N : ℕ => (f N : ℝ) / N) atTop (𝓝 ((1 : ℝ) / 2))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/302.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/302.lean#L76).

## `Erdos302.erdos_302.variants.lower_half`

Proved here.

> One can take either $A$ to be all odd integers in $[1,N]$ or all integers in $[N/2,N]$ to show
> $f(N)\geq (1/2+o(1))N$.

```lean
theorem erdos_302.variants.lower_half (f : ℕ → ℕ) (hf : ∀ N, IsMaxNoTripleCard N (f N))
    (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ N : ℕ in atTop, ((1 : ℝ) / 2 - ε) * N ≤ f N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/302.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/302.lean#L85).

## `Erdos302.erdos_302.variants.lower_five_eighths`

Solved: stated here without proof.

> Stijn Cambie has observed that
>
> $$f(N)\geq (5/8+o(1))N,$$
>
> taking $A$ to be all odd integers $\leq N/4$ and all integers in $[N/2,N]$.

```lean
theorem erdos_302.variants.lower_five_eighths (f : ℕ → ℕ) (hf : ∀ N, IsMaxNoTripleCard N (f N))
    (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ N : ℕ in atTop, ((5 : ℝ) / 8 - ε) * N ≤ f N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/302.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/302.lean#L127).

## `Erdos302.erdos_302.variants.upper_nine_tenths`

Solved: stated here without proof.

> Wouter van Doorn has proved [va25] that
>
> $$f(N) \leq (9/10+o(1))N.$$

```lean
theorem erdos_302.variants.upper_nine_tenths (f : ℕ → ℕ) (hf : ∀ N, IsMaxNoTripleCard N (f N))
    (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ N : ℕ in atTop, (f N : ℝ) ≤ ((9 : ℝ) / 10 + ε) * N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/302.lean, line 137](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/302.lean#L137).

## `Erdos302.erdos_302.variants.upper_0_8461739827964010`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-302-upper-bound/blob/9447ceb/lean/Erdos302ReflectiveUpperFC.lean#L92-L99](https://github.com/KitaKen1/erdos-302-upper-bound/blob/9447ceb/lean/Erdos302ReflectiveUpperFC.lean#L92-L99).

> Kenta Kitamura (KitaKen1 on GitHub) has given a Lean proof
> ([erdos-302-upper-bound](https://github.com/KitaKen1/erdos-302-upper-bound)) that
>
> $$f(N) \leq (0.8461739827964010+o(1))N.$$

```lean
theorem erdos_302.variants.upper_0_8461739827964010 (f : ℕ → ℕ)
    (hf : ∀ N, IsMaxNoTripleCard N (f N)) (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ N : ℕ in atTop, (f N : ℝ) ≤ ((8461739827964010 : ℝ) / 10000000000000000 + ε) * N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/302.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/302.lean#L151).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/302.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/302.lean)
- [erdosproblems.com/302](https://www.erdosproblems.com/302)
