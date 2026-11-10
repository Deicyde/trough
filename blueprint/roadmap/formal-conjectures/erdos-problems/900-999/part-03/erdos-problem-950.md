---
declaration: theorem
origin: cited
lean: Erdos950.erdos_950.parts.i, Erdos950.erdos_950.parts.ii, Erdos950.erdos_950.parts.iii, Erdos950.erdos_950.variants.debruijn_erdos_turan, Erdos950.erdos_950.variants.weaker_pi, Erdos950.erdos_950.variants.weaker_pi_implies_f, Erdos950.erdos_950.variants.sum_primes
statement: formalized
---

# Erdős Problem 950

> *References:*
> - [erdosproblems.com/855](https://www.erdosproblems.com/855)
> - [erdosproblems.com/950](https://www.erdosproblems.com/950)
> - [Er77c] Erdős, Paul, Problems and results on combinatorial number theory. III. Number theory day
>   (Proc. Conf., Rockefeller Univ., New York, 1976) (1977), 43-72.
> - [mathoverflow/508491](https://mathoverflow.net/questions/508491)

*Quoted from [FormalConjectures/ErdosProblems/950.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/950.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/950](https://www.erdosproblems.com/950).

The file states 7 research or textbook statements: 5 open and 2 solved.

## `Erdos950.erdos_950.parts.i`

Open: stated without proof.

> Is it true that $\liminf f(n)=1$?

```lean
theorem erdos_950.parts.i :
    atTop.liminf (fun n : ℕ ↦ (f n : EReal)) = 1
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/950.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/950.lean#L48).

## `Erdos950.erdos_950.parts.ii`

Open: stated without proof.

> Is it true that $\limsup f(n)=\infty$?

```lean
theorem erdos_950.parts.ii :
    atTop.limsup (fun n : ℕ ↦ (f n : EReal)) = ⊤
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/950.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/950.lean#L56).

## `Erdos950.erdos_950.parts.iii`

Open: stated without proof.

> Is it true that $f(n)=o(\log\log n)$ for all $n$?

```lean
theorem erdos_950.parts.iii :
    f =o[atTop] (fun n : ℕ ↦ Real.log (Real.log n))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/950.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/950.lean#L64).

## `Erdos950.erdos_950.variants.debruijn_erdos_turan`

Solved: stated here without proof.

> This function was considered by de Bruijn, Erdős, and Turán, who showed that
> $\sum_{n\lt x}f(n)\sim \sum_{n\lt x}f(n)^2\sim x$. They gave no proofs, but a proof of the (harder) second
> claim is given by Gorodetsky here [mathoverflow/508491].

```lean
theorem erdos_950.variants.debruijn_erdos_turan :
    (fun x : ℕ ↦ ∑ n ∈ Finset.range x, f n) ~[atTop] (fun x : ℕ ↦ (x : ℝ)) ∧
    (fun x : ℕ ↦ ∑ n ∈ Finset.range x, (f n) ^ 2) ~[atTop] (fun x : ℕ ↦ (x : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/950.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/950.lean#L74).

## `Erdos950.erdos_950.variants.weaker_pi`

Open: stated without proof.

> Erdős writes that a 'weaker conjecture which is perhaps not quite inaccessible' is that,
> for every $\epsilon>0$, if $x$ is sufficiently large there exists $y\lt x$ such that
> $\pi(x)< \pi(y)+\epsilon \pi(x-y)$. Compare this to [855].

```lean
theorem erdos_950.variants.weaker_pi :
    ∀ ε > 0, ∀ᶠ x in atTop, ∃ y < x,
      (π x : ℝ) < (π y : ℝ) + ε * (π (x - y) : ℝ)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/950.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/950.lean#L85).

## `Erdos950.erdos_950.variants.weaker_pi_implies_f`

Solved: stated here without proof.

> He notes that if $\pi(x)< \pi(y)+O\left(\frac{x-y}{\log x}\right)$ for all $y\lt x-(\log x)^C$ for
> some constant $C>0$ then $f(n)\ll \log\log\log n$.

```lean
theorem erdos_950.variants.weaker_pi_implies_f
    (h : ∃ C > (0 : ℝ), ∃ K > (0 : ℝ), ∀ᶠ x : ℕ in atTop, ∀ y : ℕ,
      (y : ℝ) < x - (Real.log x) ^ C →
      (π x : ℝ) < (π y : ℝ) + K * ((x - y : ℝ) / Real.log x)) :
    f =O[atTop] fun n : ℕ ↦ Real.log (Real.log (Real.log n))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/950.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/950.lean#L95).

## `Erdos950.erdos_950.variants.sum_primes`

Open: stated without proof.

> The study of $f(p)$ is even harder, and Erdős could not prove that
> $\sum_{p\lt x}f(p)^2\sim \pi(x)$.

```lean
theorem erdos_950.variants.sum_primes :
    (fun x : ℕ ↦ ∑ p ∈ (Finset.range x).filter Prime, (f p) ^ 2) ~[atTop]
      fun x ↦ (π x : ℝ)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/950.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/950.lean#L107).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/950.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/950.lean)
- [erdosproblems.com/950](https://www.erdosproblems.com/950)
