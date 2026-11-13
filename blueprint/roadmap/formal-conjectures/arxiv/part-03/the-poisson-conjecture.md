---
declaration: theorem
origin: cited
lean: Arxiv.«math.0608009».poisson_conjecture, Arxiv.«math.0608009».poisson_conjecture.variants.dimension_one, Arxiv.«math.0608009».poisson_conjecture.variants.dimension_two, Arxiv.«math.0608009».poisson_conjecture.variants.dimension_three, Arxiv.«math.0608009».poisson_conjecture.variants.dimension_ge_two, Arxiv.«math.0608009».poisson_conjecture.variants.jacobian_implication
statement: formalized
---

# The Poisson Conjecture

> *References:*
> - [AvdE07] [arxiv/math.0608009](https://arxiv.org/abs/math/0608009)
>   **On the equivalence of the Jacobian, Dixmier and Poisson Conjectures in any characteristic**
>   by *Kossivi Adjamagbo, Arno van den Essen*. Published as *A proof of the equivalence of the
>   Dixmier, Jacobian and Poisson conjectures*, Acta Math. Vietnam. 32 (2007), 205–214.
> - [BCW82] [The Jacobian conjecture: reduction of degree and formal expansion of the inverse](https://doi.org/10.1090/S0273-0979-1982-15032-7)
>   by *Hyman Bass, Edwin H. Connell, David Wright*, Bull. Amer. Math. Soc. 7 (1982), 287–330.
> - [Alp26] [Counterexample to the Jacobian conjecture](https://x.com/__alpoge__/status/2079028340955197566)
>   by *Levent Alpöge* (2026), disproving the Jacobian conjecture in dimension $3$
> - [Lon26] [An Explicit Counterexample to the Rank-Two Poisson Conjecture](https://arxiv.org/abs/2608.23777)
>   by *Christopher D. Long* (2026), disproving $PC_2$
>
> The Poisson Conjecture $PC_n$ ([AvdE07], Notations 5) asserts that, over a field of
> characteristic zero, every endomorphism of the `n`-th canonical Poisson algebra
> $P_n(K)$ — the polynomial algebra $K[X_1, \dots, X_{2n}]$ equipped with the canonical
> Poisson bracket — is an automorphism.
>
> By [AvdE07], Theorem 7 (the "United Conjectures Theorem"), for every `n` there is a chain
> of implications
>
> $$JC_{2n} \Longrightarrow PC_n \Longrightarrow DC_n \Longrightarrow JC_n,$$
>
> where $JC_n$ is the Jacobian Conjecture in dimension `n` and $DC_n$ the Dixmier Conjecture
> for the `n`-th Weyl algebra (the implication $DC_n \Longrightarrow JC_n$ being classical [BCW82]).
> Since the Jacobian conjecture was disproved in dimension $3$ [Alp26] — and hence in every
> dimension $n ≥ 3$ by padding with identity coordinates — $PC_n$ is false for all $n ≥ 3$:
> composing the counterexample's failure of $JC_3$ through $PC_3 \Longrightarrow DC_3 \Longrightarrow JC_3$ refutes
> $PC_3$, and directly, the cotangent (symplectic) lift of the counterexample map
> ([AvdE07], Theorem 1 in reverse) is a non-invertible Poisson endomorphism of $P_3(K)$.
> $PC_2$ is false as well, by the explicit rank-two counterexample of [Lon26]. Only $n = 1$
> remains open.
>
> Indexing note: we index the $2n$ variables of $P_n(K)$ by `Fin n ⊕ Fin n`, with
> `Sum.inl i` playing the role of $X_i$ and `Sum.inr i` the role of $X_{i+n}$ of [AvdE07],
> so that the canonical bracket reads $\{X_i, X_{i+n}\} = 1$; see
> `MvPolynomial.poissonBracket`.

*Quoted from [FormalConjectures/Arxiv/math.0608009/PoissonConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/math.0608009/PoissonConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 1 open and 5 solved. It also has 3 test statements and 2 API statements, counted here but not shown.

## `Arxiv.«math.0608009».poisson_conjecture`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-01-000002](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-01-000002).

> The **Poisson Conjecture** ([AvdE07], the characteristic zero case): for every `n`, every
> endomorphism of the `n`-th canonical Poisson algebra over a field `K` of characteristic
> zero is an automorphism. This is **false**: the Jacobian conjecture fails in dimension $3$
> [Alp26], hence so does $PC_3$ (via [AvdE07], Theorem 7, or directly via the symplectic
> lift of the counterexample map).

```lean
theorem poisson_conjecture : ¬ ∀ n, PoissonConjectureFor K n
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [17 Nonassociative rings and algebras](../../by-subject/part-01/17-nonassociative-rings-and-algebras/README.md). Declared in [FormalConjectures/Arxiv/math.0608009/PoissonConjecture.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/math.0608009/PoissonConjecture.lean#L124).

## `Arxiv.«math.0608009».poisson_conjecture.variants.dimension_one`

Open: stated without proof.

> The Poisson Conjecture in dimension $1$ ($PC_1$) is open. By [AvdE07], Theorem 7, it is
> implied by the Jacobian conjecture in dimension $2$ (Keller's original problem, open) and
> implies the Dixmier conjecture for the first Weyl algebra (Problem 1 of Dixmier (1968),
> open).

```lean
theorem poisson_conjecture.variants.dimension_one : PoissonConjectureFor K 1
```

Category `research open`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [17 Nonassociative rings and algebras](../../by-subject/part-01/17-nonassociative-rings-and-algebras/README.md). Declared in [FormalConjectures/Arxiv/math.0608009/PoissonConjecture.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/math.0608009/PoissonConjecture.lean#L134).

## `Arxiv.«math.0608009».poisson_conjecture.variants.dimension_two`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-01-000002](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-01-000002).

> The Poisson Conjecture is false in dimension $2$ ($PC_2$). [Lon26] gives four explicit
> polynomials $R, T, D, S \in \mathbb{Q}[x, q, p, z]$ with
> $\{R, D\} = \{T, S\} = 1$ and $\{R, T\} = \{R, S\} = \{D, T\} = \{D, S\} = 0$, so that
> $X_1 \mapsto R$, $X_2 \mapsto T$, $X_3 \mapsto D$, $X_4 \mapsto S$ is a Poisson endomorphism of
> $P_2(K)$. It is not surjective: in the coordinates $(X_1, X_2, X_3, X_4)$ the two rational
> points $(0, 0, 1/24, -1/8)$ and $(1, 2/3, 247/96, -89/64)$ have the same image under
> $(R, T, D, S)$, so every polynomial in the image of the endomorphism takes equal values at
> them, while $X_1$ does not. The formulas have rational coefficients and the two points are
> rational, so the argument applies over every field of characteristic zero.
>
> This does not settle any conjecture further down the chain of [AvdE07], Theorem 7, which only
> propagates falsity upwards: $\lnot PC_2$ gives $\lnot JC_4$, already known from [Alp26].
> $DC_2$, $JC_2$ (Keller's problem), $PC_1$ and $DC_1$ all remain open.

```lean
theorem poisson_conjecture.variants.dimension_two : ¬ PoissonConjectureFor K 2
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [17 Nonassociative rings and algebras](../../by-subject/part-01/17-nonassociative-rings-and-algebras/README.md). Declared in [FormalConjectures/Arxiv/math.0608009/PoissonConjecture.lean, line 154](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/math.0608009/PoissonConjecture.lean#L154).

## `Arxiv.«math.0608009».poisson_conjecture.variants.dimension_three`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-01-000002](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-01-000002).

> The Poisson Conjecture is false in dimension $3$: the cotangent (symplectic) lift
> $\Phi(X_i) = F_i$, $\Phi(X_{i+3}) = \sum_j M_{ij} X_{j+3}$ with $M = (JF)^{-\top}$ of the
> degree-$6$ counterexample map $F$ of [Alp26] (whose Jacobian determinant is the constant
> $-2$, so $M$ is a polynomial matrix) is a Poisson endomorphism of $P_3(K)$ that is not
> injective on points — e.g. it identifies $(0, 6, -142, 0, 0, 0)$ and $(1, 0, 2, 0, 0, 0)$
> — and is therefore no automorphism. Alternatively, $PC_3$ fails by [AvdE07], Theorem 7,
> as it implies the Jacobian conjecture in dimension $3$, contradicting [Alp26].

```lean
theorem poisson_conjecture.variants.dimension_three : ¬ PoissonConjectureFor K 3
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [17 Nonassociative rings and algebras](../../by-subject/part-01/17-nonassociative-rings-and-algebras/README.md). Declared in [FormalConjectures/Arxiv/math.0608009/PoissonConjecture.lean, line 168](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/math.0608009/PoissonConjecture.lean#L168).

## `Arxiv.«math.0608009».poisson_conjecture.variants.dimension_ge_two`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-01-000002](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-01-000002).

> The Poisson Conjecture is false in every dimension $n ≥ 2$, by padding the dimension $2$
> counterexample of [Lon26] with identity canonical pairs.

```lean
theorem poisson_conjecture.variants.dimension_ge_two (n : ℕ) (hn : 2 ≤ n) :
    ¬ PoissonConjectureFor K n
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [17 Nonassociative rings and algebras](../../by-subject/part-01/17-nonassociative-rings-and-algebras/README.md). Declared in [FormalConjectures/Arxiv/math.0608009/PoissonConjecture.lean, line 177](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/math.0608009/PoissonConjecture.lean#L177).

## `Arxiv.«math.0608009».poisson_conjecture.variants.jacobian_implication`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-03-000028](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-03-000028).

> The Jacobian conjecture in dimension $2n$ implies the Poisson conjecture in dimension `n`
> ([AvdE07], Theorem 1 and Theorem 7).

```lean
theorem poisson_conjecture.variants.jacobian_implication (n : ℕ)
    (h : JacobianConjectureProp K (Fin (2 * n))) : PoissonConjectureFor K n
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [17 Nonassociative rings and algebras](../../by-subject/part-01/17-nonassociative-rings-and-algebras/README.md). Declared in [FormalConjectures/Arxiv/math.0608009/PoissonConjecture.lean, line 187](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/math.0608009/PoissonConjecture.lean#L187).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/math.0608009/PoissonConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/math.0608009/PoissonConjecture.lean)
- [arxiv/math.0608009](https://arxiv.org/abs/math/0608009)
