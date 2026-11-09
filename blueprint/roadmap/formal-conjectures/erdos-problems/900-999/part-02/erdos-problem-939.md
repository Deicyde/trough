---
declaration: theorem
origin: cited
lean: Erdos939.erdos_939, Erdos939.erdos_939.variants.finite, Erdos939.erdos_939.variants.infinite_of_six_le, Erdos939.erdos_939.variants.triples, Erdos939.erdos_939.variants.examples, Erdos939.erdos_939.variants.seven, Erdos939.erdos_939.variants.eight, Erdos939.erdos_939.variants.euler
statement: formalized
---

# Erdős Problem 939

> *References:*
> - [erdosproblems.com/939](https://www.erdosproblems.com/939)
> - [Ni95] Nitaj, A., _On a conjecture of Erdős on 3-powerful numbers_. Bull. London Math. Soc.
>   (1995), 317-318.
> - [Co98] Cohn, J. H. E., _A conjecture of Erdős on 3-powerful numbers_. Math. Comp. (1998),
>   439-440.
> - [Wa24] Walsh, P., _A question of Erdős on 3-powerful numbers and an elliptic curve analogue
>   of the Ankeny-Artin-Chowla conjecture_. arXiv:2404.03970 (2024).
> - [LaPa67] Lander, L. J. and Parkin, T. R., _A counterexample to Euler's sum of powers
>   conjecture_. Math. Comp. (1967), 101-103.

*Quoted from [FormalConjectures/ErdosProblems/939.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/939.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/939](https://www.erdosproblems.com/939).

The file states 8 research or textbook statements: 1 open and 7 solved.

## `Erdos939.erdos_939`

Open: stated without proof.

> If $r≥4$ then can the sum of $r-2$ coprime $r$-powerful numbers ever be itself $r$-powerful?

```lean
theorem erdos_939 : ∀ r ≥ 4, (Erdos939Sums r).Nonempty
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/939.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/939.lean#L61).

## `Erdos939.erdos_939.variants.finite`

Solved: stated here without proof.

> If $r≥4$, are there at most finitely many sums of $r-2$ coprime $r$-powerful numbers
> that are themselves $r$-powerful?
>
> The answer is no: for every $r \ge 6$ there are infinitely many such sums, see
> `erdos_939.variants.infinite_of_six_le`. (For $r = 4$ and $r = 5$ the question is open; for
> $r = 4$ no example is known at all, see `erdos_939`.)
> A construction in the site's comments, from GPT-5.5 Pro prompted by Price, gives infinitely
> many for every $r \ge 6$. This statement quantifies over every $r \ge 4$, so it stays open at
> $r = 4$ and $r = 5$. The category is unchanged because the construction is recorded in the
> comments and not in the literature.

```lean
theorem erdos_939.variants.finite : ¬ ∀ r ≥ 4, (Erdos939Sums r).Finite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/939.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/939.lean#L77).

## `Erdos939.erdos_939.variants.infinite_of_six_le`

Solved: stated here without proof.

> For every $r \ge 6$ there are infinitely many sums of $r - 2$ coprime $r$-powerful numbers that
> are themselves $r$-powerful.
>
> A construction, found by GPT-5.5 Pro prompted by Liam Price and recorded in the comments on
> [erdosproblems.com/939](https://www.erdosproblems.com/forum/thread/939), expands
> $(X+Y)^r = (X-Y)^r + \sum_{j \text{ odd}} 2\binom{r}{j} X^{r-j} Y^j$, splits the $j = 3$ term into
> $\lfloor r/2 \rfloor - 2$ distinct pieces to obtain exactly $r - 2$ summands, and takes
> $X = q^r$, $Y = B^r$ with $B$ divisible by all primes in the coefficients and $q > B$ a prime not
> dividing $B$; varying $q$ gives infinitely many solutions.

```lean
theorem erdos_939.variants.infinite_of_six_le : ∀ r ≥ 6, (Erdos939Sums r).Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/939.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/939.lean#L92).

## `Erdos939.erdos_939.variants.triples`

Solved: stated here without proof.

> Are there infinitely many triples of coprime $3$-powerful numbers $a, b, c$ such that $a + b = c$?
>
> The answer is yes. Nitaj [Ni95] proved it, with $2^3\cdot 3^5\cdot 73^3 + 271^3 = 919^3$ as an
> example. In Nitaj's construction at least two of $a, b, c$ are perfect cubes. Cohn [Co98]
> constructed infinitely many triples of which none is a perfect cube, and Walsh [Wa24] gave a
> further construction.

```lean
theorem erdos_939.variants.triples :
    {(a,b,c) | ({a, b, c} : Finset ℕ).Coprime ∧
      0 < a ∧ 0 < b ∧
      (3).Full a ∧ (3).Full b ∧ (3).Full c ∧
      a + b = c}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/939.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/939.lean#L104).

## `Erdos939.erdos_939.variants.examples`

Proved here.

> Cambie has found several examples of the sum of $r - 2$ coprime $r$-powerful numbers being itself
> $r$-powerful. For example when $r=5$ we have
> $$3^7\cdot 61^5 = 2^8\cdot3^{10}\cdot 5^7 + 2^{12}\cdot 23^6 + 11^5\cdot 13^5$$.

```lean
theorem erdos_939.variants.examples : (∃ r ≥ 4, (Erdos939Sums r).Nonempty)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/939.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/939.lean#L117).

## `Erdos939.erdos_939.variants.seven`

Solved: stated here without proof.

> Cambie has also found solutions when $r=7$.

```lean
theorem erdos_939.variants.seven : (Erdos939Sums 7).Nonempty
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/939.lean, line 132](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/939.lean#L132).

## `Erdos939.erdos_939.variants.eight`

Solved: stated here without proof.

> Cambie has also found solutions when $r=8$.
>
> The source adds that the $r=8$ solution works "even with the sum of $5$ $8$-powerful numbers".
> That is a stronger result than this statement, which asks for the $r - 2 = 6$ summands of
> `Erdos939Sums`.

```lean
theorem erdos_939.variants.eight : (Erdos939Sums 8).Nonempty
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/939.lean, line 143](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/939.lean#L143).

## `Erdos939.erdos_939.variants.euler`

Proved here.

> Euler had conjectured that the sum of $k - 1$ many $k$-th powers is never a
> $k$-th power, but this is false for $k=5$, as Lander and Parkin [LaPa67] found
> $$27^5+84^5+110^5+133^5=144^5$$.
>
> The summands must be positive. Without that condition a set containing `0` would count, so the
> negation would be satisfied by a sum of fewer than $k-1$ powers and would claim less than the
> refutation of Euler's conjecture that this theorem records.

```lean
theorem erdos_939.variants.euler : ¬ (∀ k ≥ 4, ∀ S : Finset ℕ, S.card = k - 1 →
    (∀ s ∈ S, 0 < s) → ¬ (∃ q, ∑ s ∈ S, s ^ k = q ^k))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/939.lean, line 156](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/939.lean#L156).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/939.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/939.lean)
- [erdosproblems.com/939](https://www.erdosproblems.com/939)
