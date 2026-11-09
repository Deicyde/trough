---
declaration: theorem
origin: cited
lean: SerreMultiplicityConjectures.supportDim_add_supportDim_le_ringKrullDim, SerreMultiplicityConjectures.intersectionMultiplicity_nonneg, SerreMultiplicityConjectures.intersectionMultiplicity_eq_zero_of_lt, SerreMultiplicityConjectures.intersectionMultiplicity_pos, SerreMultiplicityConjectures.intersectionMultiplicity_pos_quotient, SerreMultiplicityConjectures.intersectionMultiplicity_pos_of_equalCharacteristic, SerreMultiplicityConjectures.intersectionMultiplicity_pos_of_unramified
statement: formalized
---

# Serre's multiplicity conjectures

> Let $R$ be a regular local ring and let $M$, $N$ be finitely generated $R$-modules such that
> $M \otimes_R N$ has finite length. Serre defined the intersection multiplicity
> $$\chi(M, N) = \sum_{i \ge 0} (-1)^i \ell_R(\operatorname{Tor}_i^R(M, N)).$$
> He proved the dimension inequality $\dim M + \dim N \le \dim R$ for every regular local ring,
> and conjectured the following three properties:
>
> - **Non-negativity:** $\chi(M, N) \ge 0$.
> - **Vanishing:** if $\dim M + \dim N < \dim R$, then $\chi(M, N) = 0$.
> - **Positivity:** if $\dim M + \dim N = \dim R$, then $\chi(M, N) > 0$.
>
> Serre proved all three when $R$ is of equal characteristic, or of mixed characteristic and
> unramified. Vanishing was proved in general by Roberts and, independently, by Gillet and Soulé.
> Non-negativity was proved in general by Gabber. Positivity is open in general. For Serre's two
> special cases, this file states only positivity, since non-negativity and vanishing are now known
> in general.
>
> The intersection multiplicity is `Module.intersectionMultiplicity`, defined in
> `FormalConjecturesForMathlib.RingTheory.IntersectionMultiplicity`.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Serre%27s_multiplicity_conjectures)
> - [Se00] J.-P. Serre, *Local algebra*, Springer Monographs in Mathematics, Springer, 2000,
>   Chapter V, Part B.
> - [Ro85] P. Roberts, *The vanishing of intersection multiplicities of perfect complexes*,
>   Bull. Amer. Math. Soc. 13 (1985), 127–130.
> - [GS87] H. Gillet, C. Soulé, *Intersection theory using Adams operations*,
>   Invent. Math. 90 (1987), 243–277.
> - [Ro98] P. Roberts, *Recent developments on Serre's multiplicity conjectures: Gabber's proof of
>   the nonnegativity conjecture*, Enseign. Math. 44 (1998), 305–324.
> - [Sk19] C. Skalit, *Positivity of intersection multiplicity over a two-dimensional base*,
>   J. Pure Appl. Algebra 223 (2019), 1801–1816.
>   [arXiv:1510.05146](https://arxiv.org/abs/1510.05146)

*Quoted from [FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 7 research or textbook statements: 2 open and 5 solved.

## `SerreMultiplicityConjectures.supportDim_add_supportDim_le_ringKrullDim`

Solved: stated here without proof.

> **Dimension inequality.** Let $R$ be a regular local ring and let $M$, $N$ be finitely generated
> $R$-modules such that $M \otimes_R N$ has finite length. Then
> $\dim M + \dim N \le \dim R$. Proved by Serre for every regular local ring [Se00].

```lean
theorem supportDim_add_supportDim_le_ringKrullDim (h : IsFiniteLength R (M ⊗[R] N)) :
    Module.supportDim R M + Module.supportDim R N ≤ ringKrullDim R
```

Category `research solved`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean#L75).

## `SerreMultiplicityConjectures.intersectionMultiplicity_nonneg`

Solved: stated here without proof.

> **Non-negativity.** Let $R$ be a regular local ring and let $M$, $N$ be finitely generated
> $R$-modules such that $M \otimes_R N$ has finite length. Then $\chi(M, N) \ge 0$.
> Conjectured by Serre and proved by Gabber in 1995 [Ro98].

```lean
theorem intersectionMultiplicity_nonneg (h : IsFiniteLength R (M ⊗[R] N)) :
    0 ≤ intersectionMultiplicity R M N
```

Category `research solved`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean#L85).

## `SerreMultiplicityConjectures.intersectionMultiplicity_eq_zero_of_lt`

Solved: stated here without proof.

> **Vanishing.** Let $R$ be a regular local ring and let $M$, $N$ be finitely generated
> $R$-modules such that $M \otimes_R N$ has finite length. If $\dim M + \dim N < \dim R$, then
> $\chi(M, N) = 0$. Conjectured by Serre and proved by Roberts [Ro85] and, independently, by
> Gillet and Soulé [GS87].

```lean
theorem intersectionMultiplicity_eq_zero_of_lt (h : IsFiniteLength R (M ⊗[R] N))
    (hdim : Module.supportDim R M + Module.supportDim R N < ringKrullDim R) :
    intersectionMultiplicity R M N = 0
```

Category `research solved`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean#L96).

## `SerreMultiplicityConjectures.intersectionMultiplicity_pos`

Open: stated without proof.

> **Positivity conjecture.** Let $R$ be a regular local ring and let $M$, $N$ be finitely
> generated $R$-modules such that $M \otimes_R N$ has finite length. If
> $\dim M + \dim N = \dim R$, then $\chi(M, N) > 0$.
>
> The hypothesis on dimensions forces $M$ and $N$ to be nonzero, since the dimension of the zero
> module is $\bot$.

```lean
theorem intersectionMultiplicity_pos (h : IsFiniteLength R (M ⊗[R] N))
    (hdim : Module.supportDim R M + Module.supportDim R N = ringKrullDim R) :
    0 < intersectionMultiplicity R M N
```

Category `research open`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean#L110).

## `SerreMultiplicityConjectures.intersectionMultiplicity_pos_quotient`

Open: stated without proof.

> **Positivity conjecture**, in the form stated on Wikipedia. Let $R$ be a regular local ring and
> let $P$, $Q$ be prime ideals of $R$ such that $R/P \otimes_R R/Q$ has finite length. If
> $\dim R/P + \dim R/Q = \dim R$, then $\chi(R/P, R/Q) > 0$.

```lean
theorem intersectionMultiplicity_pos_quotient (P Q : Ideal R) [P.IsPrime] [Q.IsPrime]
    (h : IsFiniteLength R ((R ⧸ P) ⊗[R] (R ⧸ Q)))
    (hdim : ringKrullDim (R ⧸ P) + ringKrullDim (R ⧸ Q) = ringKrullDim R) :
    0 < intersectionMultiplicity R (R ⧸ P) (R ⧸ Q)
```

Category `research open`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean#L121).

## `SerreMultiplicityConjectures.intersectionMultiplicity_pos_of_equalCharacteristic`

Solved: stated here without proof.

> Serre proved the positivity conjecture when $R$ is of equal characteristic, that is, when $R$
> contains a field [Se00].

```lean
theorem intersectionMultiplicity_pos_of_equalCharacteristic (k : Type*) [Field k] [Algebra k R]
    (h : IsFiniteLength R (M ⊗[R] N))
    (hdim : Module.supportDim R M + Module.supportDim R N = ringKrullDim R) :
    0 < intersectionMultiplicity R M N
```

Category `research solved`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean, line 132](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean#L132).

## `SerreMultiplicityConjectures.intersectionMultiplicity_pos_of_unramified`

Solved: stated here without proof.

> Serre proved the positivity conjecture when $R$ is of mixed characteristic and unramified, that
> is, when the characteristic $p$ of the residue field is not in the square of the maximal ideal
> of $R$ [Se00]. The hypothesis $p \notin \mathfrak m^2$ excludes $p = 0$ and the equal
> characteristic case, where $p = 0$ in $R$.

```lean
theorem intersectionMultiplicity_pos_of_unramified (p : ℕ) [CharP (ResidueField R) p]
    (hp : (p : R) ∉ maximalIdeal R ^ 2) (h : IsFiniteLength R (M ⊗[R] N))
    (hdim : Module.supportDim R M + Module.supportDim R N = ringKrullDim R) :
    0 < intersectionMultiplicity R M N
```

Category `research solved`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean, line 145](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean#L145).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Serre%27s_multiplicity_conjectures)
