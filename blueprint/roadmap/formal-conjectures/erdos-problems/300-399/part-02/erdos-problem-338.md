---
declaration: theorem
origin: cited
lean: Erdos338.erdos_338, Erdos338.erdos_338.variants.bounded_by_order, Erdos338.erdos_338.variants.eq_order, Erdos338.erdos_338.variants.basis_after_finite_removal, Erdos338.erdos_338.variants.same_order_after_finite_removal, Erdos338.erdos_338.variants.bateman, Erdos338.erdos_338.variants.kelly, Erdos338.erdos_338.variants.kelly_lowerDensity, Erdos338.erdos_338.variants.kelly_conjecture, Erdos338.erdos_338.variants.squares, Erdos338.erdos_338.variants.triangular, Erdos338.erdos_338.variants.hegyvari_hennecart_plagne
statement: formalized
---

# Erdős Problem 338

> *References:*
> - [erdosproblems.com/338](https://www.erdosproblems.com/338)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [ErGr80b] Erdős, P. and Graham, R. L., *On bases with an exact order*. Acta Arith. (1980),
>   201-207.
> - [HHP07] Hegyvári, Norbert and Hennecart, François and Plagne, Alain, *Answer to a question by
>   Burr and Erdős on restricted addition, and related results*. Combin. Probab. Comput. (2007),
>   747--756.
> - [He05] Hennecart, François, *On the restricted order of asymptotic bases of order two*.
>   Ramanujan J. (2005), 123--130.
> - [Ke57] Kelly, John B., *Restricted bases*. Amer. J. Math. (1957), 258-264.
> - [Pa33] Pall, Gordon, *On Sums of Squares*. Amer. Math. Monthly (1933), 10-18.
> - [Sc54] Schinzel, A., *Sur la décomposition des nombres naturels en sommes de nombres
>   triangulaires distincts*. Bull. Acad. Polon. Sci. Cl. III. (1954), 409-410.

*Quoted from [FormalConjectures/ErdosProblems/338.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/338.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/338](https://www.erdosproblems.com/338).

The file states 12 research or textbook statements: 5 open and 7 solved.

## `Erdos338.erdos_338`

Open: stated without proof.

> The restricted order of a basis $A$ is the least integer $t$ (if it exists) such that every large
> integer is the sum of at most $t$ distinct summands from $A$. What are necessary and sufficient
> conditions that this exists?
>
> A solution must fill in `Erdos338.erdos_338.answer` with the condition and prove the
> equivalence. Whether a condition is a satisfactory answer is up to human judgement.

```lean
theorem erdos_338 :
    ∀ A : Set ℕ, (∃ h, HasOrder A h) → ((∃ t, HasRestrictedOrder A t) ↔ erdos_338.answer A)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/338.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/338.lean#L83).

## `Erdos338.erdos_338.variants.bounded_by_order`

Open: stated without proof.

> Can the restricted order of a basis be bounded (when it exists) in terms of the order of the
> basis?
>
> `HasOrder A h` only says that the order of $A$ is at most $h$. This gives the same question,
> since $f$ can be replaced by its running maximum. Kelly [Ke57] showed that $f(2) = 4$ works, and
> Hennecart [He05] showed that $4$ is optimal. Hegyvári, Hennecart and Plagne [HHP07] showed that
> any such $f$ has $f(k) \geq 2^{k-2}+k-1$ for $k \geq 3$.

```lean
theorem erdos_338.variants.bounded_by_order :
    ∃ f : ℕ → ℕ, ∀ (A : Set ℕ) (h : ℕ), HasOrder A h →
      (∃ t, HasRestrictedOrder A t) → HasRestrictedOrder A (f h)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/338.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/338.lean#L97).

## `Erdos338.erdos_338.variants.eq_order`

Open: stated without proof.

> What are necessary and sufficient conditions that the restricted order of a basis $A$ is equal to
> the order of $A$?
>
> For a basis, `basisOrder A` is finite, so the equality also says that the restricted order exists.
> The condition is `Erdos338.erdos_338.variants.eq_order.answer`, as in `Erdos338.erdos_338`.

```lean
theorem erdos_338.variants.eq_order :
    ∀ A : Set ℕ, (∃ h, HasOrder A h) →
      (restrictedOrder A = basisOrder A ↔ erdos_338.variants.eq_order.answer A)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/338.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/338.lean#L112).

## `Erdos338.erdos_338.variants.basis_after_finite_removal`

Open: stated without proof.

> Is it true that if $A \setminus F$ is a basis for all finite sets $F$ then $A$ must have a
> restricted order?

```lean
theorem erdos_338.variants.basis_after_finite_removal :
    ∀ A : Set ℕ, (∀ F : Set ℕ, F.Finite → ∃ h, HasOrder (A \ F) h) →
      ∃ t, HasRestrictedOrder A t
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/338.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/338.lean#L122).

## `Erdos338.erdos_338.variants.same_order_after_finite_removal`

Open: stated without proof.

> Is it true that if the sets $A \setminus F$, for all finite sets $F$, are bases of the same order,
> then $A$ must have a restricted order?
>
> We read "the same order" literally: every $A \setminus F$ has the same exact order $h$. This is
> equivalent to asking that the orders of the sets $A \setminus F$ are bounded. Removing elements can
> only raise the order, so if the orders are bounded, their maximum is attained at some $F_0$, and
> $A \setminus F_0 \subseteq A$ satisfies the literal hypothesis.

```lean
theorem erdos_338.variants.same_order_after_finite_removal :
    ∀ A : Set ℕ,
      (∃ h : ℕ, ∀ F : Set ℕ, F.Finite → basisOrder (A \ F) = (h : ℕ∞)) →
      ∃ t, HasRestrictedOrder A t
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/338.lean, line 137](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/338.lean#L137).

## `Erdos338.erdos_338.variants.bateman`

Solved: stated here without proof.

> Bateman observed that for $h \geq 3$ the set $A = \{1\} \cup \{x > 0 : h \mid x\}$ is a basis of
> order $h$ with no restricted order.

```lean
theorem erdos_338.variants.bateman (h : ℕ) (hh : 3 ≤ h) :
    basisOrder (insert 1 {x : ℕ | 0 < x ∧ h ∣ x}) = h ∧
      ¬ ∃ t, HasRestrictedOrder (insert 1 {x : ℕ | 0 < x ∧ h ∣ x}) t
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/338.lean, line 148](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/338.lean#L148).

## `Erdos338.erdos_338.variants.kelly`

Solved: stated here without proof.

> Kelly [Ke57] showed that any basis of order $2$ has restricted order at most $4$.

```lean
theorem erdos_338.variants.kelly (A : Set ℕ) (hA : HasOrder A 2) : HasRestrictedOrder A 4
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/338.lean, line 157](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/338.lean#L157).

## `Erdos338.erdos_338.variants.kelly_lowerDensity`

Solved: stated here without proof.

> Kelly [Ke57] showed that any basis of order $2$ with positive lower density has restricted order
> at most $3$.

```lean
theorem erdos_338.variants.kelly_lowerDensity (A : Set ℕ) (hA : HasOrder A 2)
    (hd : 0 < A.lowerDensity) : HasRestrictedOrder A 3
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/338.lean, line 165](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/338.lean#L165).

## `Erdos338.erdos_338.variants.kelly_conjecture`

Solved: stated here without proof.

> Kelly [Ke57] conjectured that any basis of order $2$ has restricted order at most $3$.
>
> This was disproved by Hennecart [He05], who constructed a basis of order $2$ with restricted
> order $4$.

```lean
theorem erdos_338.variants.kelly_conjecture :
    ¬ ∀ A : Set ℕ, HasOrder A 2 → HasRestrictedOrder A 3
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/338.lean, line 176](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/338.lean#L176).

## `Erdos338.erdos_338.variants.squares`

Solved: stated here without proof.

> The set of squares has order $4$ and restricted order $5$ (see [Pa33]).
>
> Here $0$ is a square. The order is $4$ by Lagrange's four-square theorem, and is not $3$ because
> no integer $\equiv 7 \pmod 8$ is a sum of three squares.

```lean
theorem erdos_338.variants.squares :
    basisOrder (Set.range fun k : ℕ ↦ k ^ 2) = 4 ∧
      restrictedOrder (Set.range fun k : ℕ ↦ k ^ 2) = 5
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/338.lean, line 187](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/338.lean#L187).

## `Erdos338.erdos_338.variants.triangular`

Solved: stated here without proof.

> The set of triangular numbers has order $3$ and restricted order $3$ (see [Sc54]).
>
> Here $0$ is a triangular number.

```lean
theorem erdos_338.variants.triangular :
    basisOrder (Set.range fun k : ℕ ↦ k * (k + 1) / 2) = 3 ∧
      restrictedOrder (Set.range fun k : ℕ ↦ k * (k + 1) / 2) = 3
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/338.lean, line 198](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/338.lean#L198).

## `Erdos338.erdos_338.variants.hegyvari_hennecart_plagne`

Solved: stated here without proof.

> Hegyvári, Hennecart and Plagne [HHP07] showed that for all $k \geq 2$ there exists a basis of
> order $k$ which has restricted order at least $2^{k-2}+k-1$.
>
> The basis built in the proof of Theorem 4 of [HHP07] (for $k \geq 3$) has order exactly $k$ and a
> finite restricted order, equal to $2^{k-2}+k-1$. The finiteness matters: without it, Bateman's
> example `Erdos338.erdos_338.variants.bateman` would already give the bound. For $k = 2$ the bound
> is $2$, and $A = \{1\} \cup \{x : 2 \mid x\}$ works.

```lean
theorem erdos_338.variants.hegyvari_hennecart_plagne :
    ∀ k : ℕ, 2 ≤ k → ∃ A : Set ℕ,
      basisOrder A = k ∧ restrictedOrder A = (2 ^ (k - 2) + k - 1 : ℕ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/338.lean, line 213](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/338.lean#L213).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/338.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/338.lean)
- [erdosproblems.com/338](https://www.erdosproblems.com/338)
