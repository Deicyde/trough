---
declaration: theorem
origin: cited
lean: Erdos840.erdos_840, Erdos840.erdos_840.variants.erdos_freud_lower, Erdos840.erdos_840.variants.erdos_freud_upper, Erdos840.erdos_840.variants.pikhurko
statement: formalized
---

# Erdős Problem 840

> *References:*
> - [erdosproblems.com/840](https://www.erdosproblems.com/840)
> - [Er81h] Erdős, P., *Some problems and results on additive and multiplicative number theory*.
>   Analytic number theory (Philadelphia, Pa., 1980), Lecture Notes in Math. 899 (1981), 171-182.
>   [PDF](https://www.renyi.hu/~p_erdos/1981-33.pdf)
> - [ErFr91] Erdős, P. and Freud, R., *On sums of a Sidon-sequence*. J. Number Theory 38 (1991),
>   196-205.
> - [Pi06] Pikhurko, O., *Dense edge-magic graphs and thin additive bases*. Discrete Math. 306
>   (2006), 2097-2107.

*Quoted from [FormalConjectures/ErdosProblems/840.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/840.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/840](https://www.erdosproblems.com/840).

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 1 test statement, counted here but not shown.

## `Erdos840.erdos_840`

Open: stated without proof.

> Let $f(N)$ be the size of the largest quasi-Sidon subset $A\subset\{1,\ldots,N\}$, where we say
> that $A$ is quasi-Sidon if
>
> $$\lvert A+A\rvert=(1+o(1))\binom{\lvert A\rvert}{2}.$$
>
> How does $f(N)$ grow?
>
> Following [Er81h, p. 175], we ask for the largest $c$ such that there are quasi-Sidon sets
> $A \subseteq \{1, \ldots, N\}$ with $\lvert A\rvert = (1+o(1))cN^{1/2}$.

```lean
theorem erdos_840 : IsLUB {c : ℝ | IsQuasiSidonConstant c} erdos_840.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/840.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/840.lean#L69).

## `Erdos840.erdos_840.variants.erdos_freud_lower`

Solved: stated here without proof.

> Erdős and Freud [ErFr91] proved
>
> $$\left(\frac{2}{\sqrt{3}}+o(1)\right)N^{1/2} \leq f(N) \leq \left(2+o(1)\right)N^{1/2}.$$
>
> (Although both bounds were already given by Erdős in [Er81h].)
>
> This is the lower bound. The lower bound is taking a genuine Sidon set $B\subset [1,N/3]$ of size
> $\sim N^{1/2}/\sqrt{3}$ and taking the union with $\{N-b : b\in B\}$.

```lean
theorem erdos_840.variants.erdos_freud_lower : IsQuasiSidonConstant (2 / Real.sqrt 3)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/840.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/840.lean#L81).

## `Erdos840.erdos_840.variants.erdos_freud_upper`

Proved here.

> Erdős and Freud [ErFr91] proved
>
> $$\left(\frac{2}{\sqrt{3}}+o(1)\right)N^{1/2} \leq f(N) \leq \left(2+o(1)\right)N^{1/2}.$$
>
> (Although both bounds were already given by Erdős in [Er81h].)
>
> This is the upper bound.

```lean
theorem erdos_840.variants.erdos_freud_upper (c : ℝ) (hc : IsQuasiSidonConstant c) : c ≤ 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/840.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/840.lean#L92).

## `Erdos840.erdos_840.variants.pikhurko`

Solved: stated here without proof.

> The upper bound was improved by Pikhurko [Pi06] to
>
> $$f(N) \leq \left(\left(\frac{1}{4}+\frac{1}{(\pi+2)^2}\right)^{-1/2}+o(1)\right)N^{1/2}$$
>
> (the constant here is $=1.863\cdots$).

```lean
theorem erdos_840.variants.pikhurko (c : ℝ) (hc : IsQuasiSidonConstant c) :
    c ≤ (1 / 4 + 1 / (Real.pi + 2) ^ 2) ^ (-(1 : ℝ) / 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/840.lean, line 141](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/840.lean#L141).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/840.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/840.lean)
- [erdosproblems.com/840](https://www.erdosproblems.com/840)
