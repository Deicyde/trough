---
declaration: theorem
origin: cited
lean: Erdos1122.erdos_1122, Erdos1122.erdos_1122.variants.monotone, Erdos1122.erdos_1122.variants.sub_tendsto_zero
statement: formalized
---

# Erdős Problem 1122

> *References:*
> - [erdosproblems.com/1122](https://www.erdosproblems.com/1122)
> - [Er46] Erdős, P., *On the distribution function of additive functions*. Annals of Math. (1946),
>   1-20.
> - [Ma22] Mangerel, Alexander P., *Additive functions in short intervals, gaps and a conjecture of
>   Erdős*. Ramanujan J. (2022), 1023--1090.

*Quoted from [FormalConjectures/ErdosProblems/1122.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1122.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1122](https://www.erdosproblems.com/1122).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos1122.erdos_1122`

Open: stated without proof.

> Let $f:\mathbb{N}\to \mathbb{R}$ be an additive function (i.e. $f(ab)=f(a)+f(b)$ whenever
> $(a,b)=1$). Let
>
> $$A=\{ n \geq 1: f(n+1)< f(n)\}.$$
>
> If $\lvert A\cap [1,X]\rvert =o(X)$ then must $f(n)=c\log n$ for some $c\in \mathbb{R}$?
>
> The condition $\lvert A\cap [1,X]\rvert =o(X)$ says that $A$ has natural density $0$.
>
> Partial progress was made by Mangerel [Ma22], who proved that this is true for completely
> additive $f$ if
>
> $$\lvert A\cap [1,X]\rvert \ll \frac{X}{(\log X)^{2+c}}$$
>
> for some $c>0$, and if $f(p)$ does not have very large values (in a certain technical sense).
>
> See also `erdos_491`.

```lean
theorem erdos_1122 : ∀ f : ℕ → ℝ,
    (∀ᵉ (a > 0) (b > 0), a.Coprime b → f (a * b) = f a + f b) →
    {n | 1 ≤ n ∧ f (n + 1) < f n}.HasDensity 0 →
    ∃ c : ℝ, ∀ n > 0, f n = c * Real.log n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1122.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1122.lean#L55).

## `Erdos1122.erdos_1122.variants.monotone`

Solved: stated here without proof.

> Erdős [Er46] proved that $f(n)=c\log n$ for some $c\in\mathbb{R}$ if $A$ is empty, that is, if
> $f(n) \leq f(n+1)$ for all $n \geq 1$.

```lean
theorem erdos_1122.variants.monotone (f : ℕ → ℝ)
    (hf : ∀ᵉ (a > 0) (b > 0), a.Coprime b → f (a * b) = f a + f b)
    (hmono : ∀ n ≥ 1, f n ≤ f (n + 1)) :
    ∃ c : ℝ, ∀ n > 0, f n = c * Real.log n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1122.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1122.lean#L66).

## `Erdos1122.erdos_1122.variants.sub_tendsto_zero`

Solved: stated here without proof.

> Erdős [Er46] proved that $f(n)=c\log n$ for some $c\in\mathbb{R}$ if $f(n+1)-f(n)=o(1)$.

```lean
theorem erdos_1122.variants.sub_tendsto_zero (f : ℕ → ℝ)
    (hf : ∀ᵉ (a > 0) (b > 0), a.Coprime b → f (a * b) = f a + f b)
    (hdiff : Tendsto (fun n ↦ f (n + 1) - f n) atTop (𝓝 0)) :
    ∃ c : ℝ, ∀ n > 0, f n = c * Real.log n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1122.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1122.lean#L76).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1122.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1122.lean)
- [erdosproblems.com/1122](https://www.erdosproblems.com/1122)
