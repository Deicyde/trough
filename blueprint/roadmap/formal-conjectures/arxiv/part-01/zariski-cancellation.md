---
declaration: theorem
origin: cited
lean: Arxiv.«2208.14736».zariski_cancellation_problem, Arxiv.«2208.14736».zariski_cancellation_problem.variants.false_complex_four, Arxiv.«2208.14736».zariski_cancellation_problem.variants.dim_one, Arxiv.«2208.14736».zariski_cancellation_problem.variants.dim_two, Arxiv.«2208.14736».zariski_cancellation_problem.variants.false_pos_card
statement: formalized
---

# Zariski Cancellation

> *References:*
> - [arxiv/2208.14736](https://arxiv.org/abs/2208.14736)
>   **The Zariski Cancellation Problem and related problems in Affine Algebraic Geometry**
>   by *Neena Gupta*
> - [OAI26a] OpenAI, *An explicit failure of complex affine-space cancellation*.
>   OpenAI Math Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/paper.pdf

*Quoted from [FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 5 solved.

## `Arxiv.«2208.14736».zariski_cancellation_problem`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Algebra/AffineCancellation/Main.lean#L32](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Algebra/AffineCancellation/Main.lean#L32).

> The **Zariski Cancellation Problem**: is every polynomial ring over a field `k` of characteristic
> `0` cancellative?
>
> The answer is no: the polynomial ring in four variables over $\mathbb{C}$ is not cancellative.
> This was disproved by an internal OpenAI model in September 2026 [OAI26a]; see the linked Lean
> proof and `zariski_cancellation_problem.variants.false_complex_four`.

```lean
theorem zariski_cancellation_problem :
    ¬ ∀ {k : Type} [Field k] [CharZero k] {ι : Type} [Fintype ι],
      IsCancellative k (MvPolynomial ι k)
```

Category `research solved`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean#L58).

## `Arxiv.«2208.14736».zariski_cancellation_problem.variants.false_complex_four`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Algebra/AffineCancellation/Main.lean#L32](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Algebra/AffineCancellation/Main.lean#L32).

> The polynomial ring in four variables over $\mathbb{C}$ is not cancellative: there is a finitely
> generated $\mathbb{C}$-domain $A$ of Krull dimension $4$ with
> $A[w] \cong \mathbb{C}[x_1, \dots, x_5]$ but $A \not\cong \mathbb{C}[x_1, \dots, x_4]$.
> This was proved by an internal OpenAI model in September 2026 [OAI26a]; see the linked Lean proof.

```lean
theorem zariski_cancellation_problem.variants.false_complex_four :
    ¬ IsCancellative ℂ (MvPolynomial (Fin 4) ℂ)
```

Category `research solved`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean#L72).

## `Arxiv.«2208.14736».zariski_cancellation_problem.variants.dim_one`

Solved: stated here without proof.

> The single variable polynomial ring `k[X]` is cancellative in any characteristic

```lean
theorem zariski_cancellation_problem.variants.dim_one
    {k : Type*} [Field k] : IsCancellative k k[X]
```

Category `research solved`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean#L80).

## `Arxiv.«2208.14736».zariski_cancellation_problem.variants.dim_two`

Solved: stated here without proof.

> The two variable polynomial ring `k[X]` is cancellative in any characteristic

```lean
theorem zariski_cancellation_problem.variants.dim_two {k : Type*} [Field k] :
    IsCancellative k (MvPolynomial (Fin 2) k)
```

Category `research solved`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean#L88).

## `Arxiv.«2208.14736».zariski_cancellation_problem.variants.false_pos_card`

Solved: stated here without proof.

> The positive characteristic case of the Zariski Cancellation Problem is false in dimension `3`

```lean
theorem zariski_cancellation_problem.variants.false_pos_card
    (p : ℕ) [hp : Fact p.Prime] {ι : Type*} [Fintype ι] (hι : Fintype.card ι = 3) :
    ¬ IsCancellative (ZMod p) (MvPolynomial ι (ZMod p))
```

Category `research solved`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean#L96).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean)
- [arxiv/2208.14736](https://arxiv.org/abs/2208.14736)
