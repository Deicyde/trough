---
declaration: theorem
origin: cited
lean: Mills.exists', Mills.exists_least, Mills.irrational, Mills.lower_bound_of_RH
statement: formalized
---

# Mills' Theorem

> There exists a real $A > 1$ such that
> $\lfloor A^{3^n}\rfloor$ is prime for every positive integer $n$, where $\lfloor\cdot\rfloor$
> denotes the floor function.
>
> The least such $A$ is known as *Mills' constant*. It is irrational, and assuming the
> Riemann hypothesis it is approximately $1.3063778838\ldots$.
>
> *References:*
> - [Wikipedia, Mills' constant](https://en.wikipedia.org/wiki/Mills%27_constant)
> - [A prime-representing function](https://www.ams.org/journals/bull/1947-53-06/S0002-9904-1947-08849-2/)
>   by *W. H. Mills*, Bull. Amer. Math. Soc. **53** (1947), 604.
> - [Mills' constant](https://mathworld.wolfram.com/MillsConstant.html) on Wolfram MathWorld.
> - [Mills' constant is irrational](https://doi.org/10.1112/mtk.70027) by *Kota Saito*,
>   Mathematika **71** (2025), no. 3, e70027, [arXiv:2404.19461](https://arxiv.org/abs/2404.19461).
> - [Determining Mills' Constant ..](https://cs.uwaterloo.ca/journals/JIS/VOL8/Caldwell/caldwell78.pdf)
>   by *Chris K. Caldwell and Yuanyou Cheng*, J. Integer Seq. **8** (2005), Article 05.4.1.
> - [OEIS A051021](https://oeis.org/A051021) (decimal expansion of Mills' constant)

*Quoted from [FormalConjectures/Wikipedia/Mills.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mills.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 solved.

## `Mills.exists'`

Solved: stated here without proof.

> **Mills' theorem** (Mills, 1947).
> There is a real number $A > 1$ such that $\lfloor A^{3^n}\rfloor$ is prime.

```lean
theorem exists' : ∃ A > 1, IsMills A
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mills.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mills.lean#L56).

## `Mills.exists_least`

Solved: stated here without proof.

> **Mills' constant.**
> There is a *least* Mills number.

```lean
theorem exists_least : ∃ A, IsMinMills A
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mills.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mills.lean#L69).

## `Mills.irrational`

Solved: stated here without proof.

> **Mills' constant is irrational** (Saito, 2024).

```lean
theorem irrational {A} (hA : IsMinMills A) :
    Irrational A
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mills.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mills.lean#L76).

## `Mills.lower_bound_of_RH`

Solved: stated here without proof.

> **Mills' constant lower bound** (Caldwell–Cheng, 2005): assuming the Riemann hypothesis,
> Mills' constant begins at $1.3063778838\ldots$.

```lean
theorem lower_bound_of_RH (hRH : RiemannHypothesis) {A} (hA : IsMinMills A) :
    A ∈ Set.Ioo (1.3063778838 : ℝ) 1.3063778839
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mills.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mills.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Mills.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mills.lean)
- [Wikipedia, Mills' constant](https://en.wikipedia.org/wiki/Mills%27_constant)
