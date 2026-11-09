---
declaration: theorem
origin: cited
lean: Erdos388.erdos_388, Erdos388.erdos_388.variants.classification, Erdos388.erdos_388.variants.general
statement: formalized
---

# Erdős Problem 388

> *References:*
> - [erdosproblems.com/388](https://www.erdosproblems.com/388)
> - [Er76d] Erdős, P., *Problems and results on number theoretic properties of consecutive integers
>   and related questions*. Proceedings of the Fifth Manitoba Conference on Numerical Mathematics
>   (Univ. Manitoba, Winnipeg, Man., 1975) (1976), 25-44.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Er92e] Erdős, Pál, *Some Unsolved problems in Geometry, Number Theory and Combinatorics*.
>   Eureka (1992), 44-48.

*Quoted from [FormalConjectures/ErdosProblems/388.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/388.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/388](https://www.erdosproblems.com/388).

The file states 3 research or textbook statements: 3 open.

## `Erdos388.erdos_388`

Open: stated without proof.

> Are there only finitely many solutions of
> $$\prod_{1\leq i\leq k_1}(m_1+i)=\prod_{1\leq j\leq k_2}(m_2+j)$$
> with $k_1,k_2>3$ and $m_1+k_1\leq m_2$?
>
> Here $m_1, m_2 \geq 0$, so every factor is positive and the condition $m_1 + k_1 \leq m_2$ makes the
> two blocks disjoint. Negative $m_1$ would give trivial solutions such as
> $(-5)(-4)(-3)(-2) = 2 \cdot 3 \cdot 4 \cdot 5$. The source also asks to classify all solutions;
> see `Erdos388.erdos_388.variants.classification`.

```lean
theorem erdos_388 :
    {(m₁, k₁, m₂, k₂) : ℕ × ℕ × ℕ × ℕ | 3 < k₁ ∧ 3 < k₂ ∧ m₁ + k₁ ≤ m₂ ∧
      ∏ i ∈ Finset.Icc 1 k₁, (m₁ + i) = ∏ j ∈ Finset.Icc 1 k₂, (m₂ + j)}.Finite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/388.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/388.lean#L49).

## `Erdos388.erdos_388.variants.classification`

Open: stated without proof.

> Can one classify all solutions of
> $$\prod_{1\leq i\leq k_1}(m_1+i)=\prod_{1\leq j\leq k_2}(m_2+j)$$
> with $k_1,k_2>3$ and $m_1+k_1\leq m_2$?
>
> A solution must supply the set of all solutions $(m_1, k_1, m_2, k_2)$. Whether a description of
> this set is a satisfactory classification is up to human judgement.

```lean
theorem erdos_388.variants.classification :
    {(m₁, k₁, m₂, k₂) : ℕ × ℕ × ℕ × ℕ | 3 < k₁ ∧ 3 < k₂ ∧ m₁ + k₁ ≤ m₂ ∧
      ∏ i ∈ Finset.Icc 1 k₁, (m₁ + i) = ∏ j ∈ Finset.Icc 1 k₂,
        (m₂ + j)} = erdos_388.variants.classification.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/388.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/388.lean#L65).

## `Erdos388.erdos_388.variants.general`

Open: stated without proof.

> More generally, if $k_1>2$ then for fixed $a$ and $b$ the equation
> $$a\prod_{1\leq i\leq k_1}(m_1+i)=b\prod_{1\leq j\leq k_2}(m_2+j)$$
> should have only finitely many solutions.
>
> The source states no condition on $a$, $b$, $k_2$ or the position of the blocks, so this is our
> reading: $a$ and $b$ are positive integers, we keep the condition $m_1+k_1\leq m_2$ of the main
> problem (the $k_1$-block lies below the $k_2$-block), and we assume $k_2 > 2$ as well. Without
> these conditions there are infinite families of solutions:
> - for $k_2 = 1$ and $b = 1$, take $m_2 + 1 = a\prod_{1\leq i\leq k_1}(m_1+i)$;
> - for $k_2 = 2$, $a = 1$ and $b = 4$, the identity $(n+1)(n+2)(n+3)(n+4) = Y(Y+2)$ with
>   $Y = (n+1)(n+4)$ even gives a solution with $m_2 + 1 = Y/2$ for every $n \geq 2$;
> - overlapping blocks give $2\prod_{1\leq i\leq k}(k-1+i)=\prod_{1\leq j\leq k}(k+j)$ for every
>   $k \geq 2$.

```lean
theorem erdos_388.variants.general (a b : ℕ) (ha : 0 < a) (hb : 0 < b) :
    {(m₁, k₁, m₂, k₂) : ℕ × ℕ × ℕ × ℕ | 2 < k₁ ∧ 2 < k₂ ∧ m₁ + k₁ ≤ m₂ ∧
      a * ∏ i ∈ Finset.Icc 1 k₁, (m₁ + i) = b * ∏ j ∈ Finset.Icc 1 k₂, (m₂ + j)}.Finite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/388.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/388.lean#L87).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/388.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/388.lean)
- [erdosproblems.com/388](https://www.erdosproblems.com/388)
