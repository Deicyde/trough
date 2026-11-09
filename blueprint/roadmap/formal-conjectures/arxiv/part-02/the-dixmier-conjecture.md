---
declaration: theorem
origin: cited
lean: Arxiv.«math.0608009».dixmier_conjecture, Arxiv.«math.0608009».dixmier_conjecture.variants.dimension_one, Arxiv.«math.0608009».dixmier_conjecture.variants.dimension_two, Arxiv.«math.0608009».dixmier_conjecture.variants.dimension_three, Arxiv.«math.0608009».dixmier_conjecture.variants.dimension_ge_three, Arxiv.«math.0608009».dixmier_conjecture.variants.jacobian_implication, Arxiv.«math.0608009».dixmier_conjecture.variants.poisson_implication
statement: formalized
---

# The Dixmier Conjecture

> *References:*
> - [Dix68] [Sur les algèbres de Weyl](http://www.numdam.org/item/BSMF_1968__96__209_0/)
>   by *Jacques Dixmier*, Bull. Soc. Math. France 96 (1968), 209–242. The conjecture is
>   Problem 1 (for the first Weyl algebra).
> - [BCW82] [The Jacobian conjecture: reduction of degree and formal expansion of the inverse](https://doi.org/10.1090/S0273-0979-1982-15032-7)
>   by *Hyman Bass, Edwin H. Connell, David Wright*, Bull. Amer. Math. Soc. 7 (1982),
>   287–330. Proves $DC_n \Longrightarrow JC_n$.
> - [AvdE07] [arxiv/math.0608009](https://arxiv.org/abs/math/0608009)
>   **On the equivalence of the Jacobian, Dixmier and Poisson Conjectures in any characteristic**
>   by *Kossivi Adjamagbo, Arno van den Essen*. Published as *A proof of the equivalence of
>   the Dixmier, Jacobian and Poisson conjectures*, Acta Math. Vietnam. 32 (2007), 205–214.
> - [Tsu05] [Endomorphisms of Weyl algebra and p-curvatures](https://doi.org/10.18910/7472)
>   by *Yoshifumi Tsuchimoto*, Osaka J. Math. 42 (2005), 435–452. Proves the stable
>   equivalence $JC \Longleftrightarrow DC$ independently.
> - [BKK07] [The Jacobian Conjecture is stably equivalent to the Dixmier Conjecture](https://doi.org/10.17323/1609-4514-2007-7-2-209-218)
>   by *Alexei Belov-Kanel, Maxim Kontsevich*, Moscow Math. J. 7 (2007), 209–218. Independent
>   proof of the stable equivalence.
> - [Bav20] [The Jacobian Conjecture implies the Dixmier Problem](https://arxiv.org/abs/math/0512250)
>   by *Vladimir Bavula*; published in Springer Proceedings in Mathematics & Statistics 317
>   (2020). A third proof.
> - [Alp26] [Counterexample to the Jacobian conjecture](https://x.com/__alpoge__/status/2079028340955197566)
>   by *Levent Alpöge* (2026), disproving the Jacobian conjecture in dimension $3$
> - [Lon26] [An Explicit Counterexample to the Rank-Two Poisson Conjecture](https://arxiv.org/abs/2608.23777)
>   by *Christopher D. Long* (2026), disproving $PC_2$
>
> The Dixmier Conjecture $DC_n$ asserts that, over a field `K` of characteristic zero, every
> endomorphism of the `n`-th Weyl algebra $A_n(K)$ is an automorphism. For $n = 1$ this is
> Problem 1 of [Dix68] and remains open.
>
> By [BCW82], $DC_n \Longrightarrow JC_n$ (the Jacobian conjecture in dimension `n`) over a
> fixed field `K`. By [AvdE07], Theorem 7, the chain
>
> $$JC_{2n} \Longrightarrow PC_n \Longrightarrow DC_n \Longrightarrow JC_n$$
>
> holds when each conjecture is quantified over all fields of characteristic zero
> ([AvdE07], Notations 5 and 7). Since the Jacobian conjecture fails in every dimension
> $n ≥ 3$ [Alp26], the contrapositive of [BCW82] gives that $DC_n$ is **false for all
> $n ≥ 3$**. $DC_1$ and $DC_2$ remain open. The chain only propagates falsity upwards, so the
> failure of $PC_2$ [Lon26] does not settle $DC_2$.
>
> The Weyl algebra $A_n(K)$ is `WeylAlgebra K (Fin n)`, with the $2n$ generators indexed by
> `Fin n ⊕ Fin n` as in `FormalConjecturesForMathlib/Algebra/WeylAlgebra.lean`; the Poisson
> side of the chain is stated in `PoissonConjecture.lean` in this directory.

*Quoted from [FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 7 research or textbook statements: 2 open and 5 solved. It also has 1 test statement, counted here but not shown.

## `Arxiv.«math.0608009».dixmier_conjecture`

Solved: stated here without proof.

> The **Dixmier Conjecture** (generalised to all dimensions; Problem 1 of [Dix68] for
> $n = 1$): for every `n`, every endomorphism of the `n`-th Weyl algebra over a field of
> characteristic zero is an automorphism. This is **false**: the Jacobian conjecture fails
> in dimension $3$ [Alp26], and $DC_n \Longrightarrow JC_n$ [BCW82], so $DC_3$ fails.

```lean
theorem dixmier_conjecture : ¬ ∀ n, DixmierConjectureFor K n
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean#L89).

## `Arxiv.«math.0608009».dixmier_conjecture.variants.dimension_one`

Open: stated without proof.

> The Dixmier Conjecture in dimension $1$ — Problem 1 of [Dix68] — is open. By [AvdE07],
> Theorem 7, it is implied by $PC_1$, and hence by $JC_2$ (Keller's problem).

```lean
theorem dixmier_conjecture.variants.dimension_one : DixmierConjectureFor K 1
```

Category `research open`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean#L97).

## `Arxiv.«math.0608009».dixmier_conjecture.variants.dimension_two`

Open: stated without proof.

> The Dixmier Conjecture in dimension $2$ ($DC_2$) is open. It implies Keller's
> two-variable Jacobian conjecture $JC_2$ [BCW82]. It is implied by $JC_4$ ([AvdE07],
> Theorem 7), but $JC_4$ and $PC_2$ are false ([Alp26], [Lon26]).

```lean
theorem dixmier_conjecture.variants.dimension_two : DixmierConjectureFor K 2
```

Category `research open`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean#L106).

## `Arxiv.«math.0608009».dixmier_conjecture.variants.dimension_three`

Solved: stated here without proof.

> The Dixmier Conjecture is false in dimension $3$: $DC_3$ implies the Jacobian conjecture in
> dimension $3$ [BCW82], which fails by the counterexample of [Alp26].

```lean
theorem dixmier_conjecture.variants.dimension_three : ¬ DixmierConjectureFor K 3
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean#L114).

## `Arxiv.«math.0608009».dixmier_conjecture.variants.dimension_ge_three`

Solved: stated here without proof.

> The Dixmier Conjecture is false in every dimension $n ≥ 3$, since the Jacobian conjecture
> is false in every dimension $n ≥ 3$ (padding the counterexample of [Alp26] with identity
> coordinates) and $DC_n \Longrightarrow JC_n$ [BCW82].

```lean
theorem dixmier_conjecture.variants.dimension_ge_three (n : ℕ) (hn : 3 ≤ n) :
    ¬ DixmierConjectureFor K n
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean#L123).

## `Arxiv.«math.0608009».dixmier_conjecture.variants.jacobian_implication`

Solved: stated here without proof.

> The Dixmier conjecture in dimension `n` implies the Jacobian conjecture in dimension `n`
> ([BCW82]; see also [AvdE07], Theorem 7).

```lean
theorem dixmier_conjecture.variants.jacobian_implication (n : ℕ)
    (h : DixmierConjectureFor K n) : JacobianConjectureProp K (Fin n)
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean, line 132](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean#L132).

## `Arxiv.«math.0608009».dixmier_conjecture.variants.poisson_implication`

Solved: stated here without proof.

> If the Poisson conjecture in dimension `n` holds over every field of characteristic zero,
> then so does the Dixmier conjecture in dimension `n`. This is $CPC(n, 0) \Longrightarrow
> CDC(n, 0)$ in [AvdE07], Theorem 7, where both statements quantify over all fields of
> characteristic zero (Notations 5 and 7). The proof reduces to prime characteristic and
> uses the Azumaya property of Weyl algebras in characteristic `p`.

```lean
theorem dixmier_conjecture.variants.poisson_implication (n : ℕ)
    (h : ∀ (L : Type) [Field L] [CharZero L], PoissonConjectureFor L n)
    (L : Type) [Field L] [CharZero L] : DixmierConjectureFor L n
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md), [17 Nonassociative rings and algebras](../../by-subject/part-01/17-nonassociative-rings-and-algebras/README.md). Declared in [FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean, line 144](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean#L144).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/math.0608009/DixmierConjecture.lean)
- [Sur les algèbres de Weyl](http://www.numdam.org/item/BSMF_1968__96__209_0/)
