---
declaration: theorem
origin: cited
lean: Erdos830.erdos_830.parts.i, Erdos830.erdos_830.parts.ii, Erdos830.erdos_830.variants.erdos, Erdos830.erdos_830.variants.pomerance, Erdos830.erdos_830.variants.pomerance_stronger
statement: formalized
---

# Erdős Problem 830

> *References:*
> - [erdosproblems.com/830](https://www.erdosproblems.com/830)
> - [Er55b] Erdős, P., *On amicable numbers*. Publ. Math. Debrecen (1955), 108-111.
> - [Gu04] Guy, Richard K., *Unsolved problems in number theory*. (2004), xviii+437.
> - [Po15] Pomerance, Carl, *On amicable numbers*. (2015), 321-327.
> - [Po81] Pomerance, Carl, *On the distribution of amicable numbers. II*. J. Reine Angew. Math.
>   (1981), 183-188.

*Quoted from [FormalConjectures/ErdosProblems/830.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/830.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/830](https://www.erdosproblems.com/830).

The file states 5 research or textbook statements: 2 open and 3 solved.

## `Erdos830.erdos_830.parts.i`

Open: stated without proof.

> **Erdos Problem 830, Part 1**
> We say that $a,b\in \mathbb{N}$ are an amicable pair if $\sigma(a)=\sigma(b)=a+b$. Are there
> infinitely many amicable pairs?

```lean
theorem erdos_830.parts.i : {(a, b) | IsAmicable a b}.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/830.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/830.lean#L51).

## `Erdos830.erdos_830.parts.ii`

Open: stated without proof.

> **Erdos Problem 830, Part 2**
> We say that $a,b\in \mathbb{N}$ are an amicable pair if $\sigma(a)=\sigma(b)=a+b$.
> If $A(x)$ counts the number of amicable $1\leq a\leq b\leq x$ then is it true that
> $$A(x) > x^{1-o(1)}?$$

```lean
theorem erdos_830.parts.ii : ∃ o : ℝ → ℝ, o =o[atTop] (1 : ℝ → ℝ) ∧ ∀ᶠ x in atTop,
    x ^ (1 - o x) < A x
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/830.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/830.lean#L60).

## `Erdos830.erdos_830.variants.erdos`

Solved: stated here without proof.

> We say that $a,b\in \mathbb{N}$ are an amicable pair if $\sigma(a)=\sigma(b)=a+b$.
> If $A(x)$ counts the number of amicable $1\leq a\leq b\leq x$ then one can show that $A(x) = o(x)$.

```lean
theorem erdos_830.variants.erdos : A =o[atTop] id
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/830.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/830.lean#L69).

## `Erdos830.erdos_830.variants.pomerance`

Solved: stated here without proof.

> We say that $a,b\in \mathbb{N}$ are an amicable pair if $\sigma(a)=\sigma(b)=a+b$.
> If $A(x)$ counts the number of amicable $1\leq a\leq b\leq x$ then one can show that
> $A(x) \leq x \exp(-(\log x)^{1/3})$.

```lean
theorem erdos_830.variants.pomerance : ∀ᶠ x in atTop, A x ≤ x * rexp (- Real.nthRoot 3 x.log)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/830.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/830.lean#L78).

## `Erdos830.erdos_830.variants.pomerance_stronger`

Solved: stated here without proof.

> We say that $a,b\in \mathbb{N}$ are an amicable pair if $\sigma(a)=\sigma(b)=a+b$.
> If $A(x)$ counts the number of amicable $1\leq a\leq b\leq x$ then one can show that
> $A(x) \leq x \exp(-(\tfrac{1}{2}+o(1))(\log x\log\log\log x)^{1/2})$.
> (erdosproblems.com has $\log\log x$; [Po15, Theorem 1.1] has $\log\log\log x$.)

```lean
theorem erdos_830.variants.pomerance_stronger :
    ∃ o : ℝ → ℝ, o =o[atTop] (1 : ℝ → ℝ) ∧
    ∀ᶠ x in atTop, A x ≤ x * rexp (- (1/ 2 + o x) * √(x.log * x.log.log.log))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/830.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/830.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/830.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/830.lean)
- [erdosproblems.com/830](https://www.erdosproblems.com/830)
