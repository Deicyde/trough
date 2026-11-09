---
declaration: theorem
origin: cited
lean: Erdos1191.erdos_1191.parts.i, Erdos1191.erdos_1191.parts.ii, Erdos1191.erdos_1191.variants.liminf_le
statement: formalized
---

# Erdős Problem 1191

> *References:*
> - [erdosproblems.com/1191](https://www.erdosproblems.com/1191)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115.
> - [HaRo66] Halberstam, H. and Roth, K. F., *Sequences. Vol. I*. (1966), xx+291.

*Quoted from [FormalConjectures/ErdosProblems/1191.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1191.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1191](https://www.erdosproblems.com/1191).

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Erdos1191.erdos_1191.parts.i`

Open: stated without proof.

> Let $A\subset\mathbb{N}$ be an infinite Sidon set. Is it true that
> $$\liminf_{x\to \infty} \frac{\lvert A\cap [1,x]\rvert}{x^{1/2}}(\log x)^{1/2}=0?$$
>
> Here $x$ runs over $\mathbb{N}$ and the $\liminf$ is taken in `ℝ≥0∞`, so that it is $\infty$
> rather than $0$ when the sequence tends to infinity.

```lean
theorem erdos_1191.parts.i : ∀ A : Set ℕ, A.Infinite → IsSidon A →
    liminf (fun x : ℕ ↦ ENNReal.ofReal
      ((A ∩ .Icc 1 x).ncard / (x : ℝ) ^ (1 / 2 : ℝ) * log x ^ (1 / 2 : ℝ))) atTop = 0
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1191.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1191.lean#L44).

## `Erdos1191.erdos_1191.parts.ii`

Open: stated without proof.

> Does there exist an infinite Sidon set $A$ such that
> $$\liminf_{x\to \infty} \frac{\lvert A\cap [1,x]\rvert}{x^{1/2}}(\log x)^c>0$$
> for some $c>0$?
>
> A positive answer would also give a positive answer to Erdős Problem 39.

```lean
theorem erdos_1191.parts.ii : ∃ A : Set ℕ, A.Infinite ∧ IsSidon A ∧
    ∃ c > (0 : ℝ), 0 < liminf (fun x : ℕ ↦ ENNReal.ofReal
      ((A ∩ .Icc 1 x).ncard / (x : ℝ) ^ (1 / 2 : ℝ) * log x ^ c)) atTop
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1191.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1191.lean#L57).

## `Erdos1191.erdos_1191.variants.liminf_le`

Solved: stated here without proof.

> Erdős proved (see for example [HaRo66]) that if $A$ is an infinite Sidon set then
> $$\liminf_{x\to \infty} \frac{\lvert A\cap [1,x]\rvert}{x^{1/2}}(\log x)^{1/2}\leq c$$
> for some constant $c>0$. See also `erdos_158.variants.isSidon'`.

```lean
theorem erdos_1191.variants.liminf_le {A : Set ℕ} (hAinf : A.Infinite) (hAsid : IsSidon A) :
    ∃ c > (0 : ℝ), liminf (fun x : ℕ ↦ ENNReal.ofReal
      ((A ∩ .Icc 1 x).ncard / (x : ℝ) ^ (1 / 2 : ℝ) * log x ^ (1 / 2 : ℝ))) atTop ≤
        ENNReal.ofReal c
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1191.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1191.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1191.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1191.lean)
- [erdosproblems.com/1191](https://www.erdosproblems.com/1191)
