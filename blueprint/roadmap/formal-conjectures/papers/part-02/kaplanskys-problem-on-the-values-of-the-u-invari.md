---
declaration: theorem
origin: cited
lean: KaplanskyUInvariant.u_invariant_values, KaplanskyUInvariant.u_invariant_values.variants.kaplansky_conjecture, KaplanskyUInvariant.u_invariant_values.variants.not_three, KaplanskyUInvariant.u_invariant_values.variants.not_five, KaplanskyUInvariant.u_invariant_values.variants.not_seven, KaplanskyUInvariant.u_invariant_values.variants.two_pow, KaplanskyUInvariant.u_invariant_values.variants.even, KaplanskyUInvariant.u_invariant_values.variants.nine, KaplanskyUInvariant.u_invariant_values.variants.two_pow_add_one, KaplanskyUInvariant.u_invariant_values.variants.karpenko, KaplanskyUInvariant.u_invariant_values.variants.eleven, KaplanskyUInvariant.u_invariant_values.variants.odd, KaplanskyUInvariant.u_invariant_values.variants.thirteen, KaplanskyUInvariant.u_invariant_values.variants.fifteen
statement: formalized
---

# Kaplansky's problem on the values of the $u$-invariant

> The $u$-invariant $u(F)$ of a field $F$ is the largest dimension of an anisotropic quadratic form
> over $F$, or $\infty$ if there is no largest one; that is, $u(F) = n$ exactly when
> `IsGreatest (QuadraticForm.anisotropicDims F) n`. Following [Kaplansky1953] and
> [MerkurjevParimala2025, §5.1], all fields are of characteristic not $2$.
>
> Kaplansky introduced the invariant (his $C(F)$) in [Kaplansky1953, p. 201], proved that $u(F) \ne 3$
> (his Theorem 2), observed that every power of $2$ occurs (his Theorem 3 gives
> $u(F((t))) = 2u(F)$), and conjectured that $u(F)$ is a power of $2$ whenever it is finite
> [Kaplansky1953, p. 202]. It is classical that $u(F) \notin \{3, 5, 7\}$
> [Lam2005, Proposition XI.6.8], [EKM2008, Corollary 36.4]. Merkurjev disproved Kaplansky's
> conjecture with a field of $u$-invariant $6$ [Merkurjev1989] and then showed that every positive
> even integer is a $u$-invariant [Merkurjev1991]. Izhboldin constructed a field of $u$-invariant
> $9$ [Izhboldin2001], and Vishik fields of $u$-invariant $2^r + 1$ for every $r \ge 3$
> [Vishik2009]. A 2026 preprint of Karpenko constructs fields of $u$-invariant $n$ for every $n$
> that is neither of the form $2^r - 1$ nor of the form $2^r - 3$ [Karpenko2026]; as of September
> 2026 it is not yet peer-reviewed.
>
> The problem (`u_invariant_values`) is to determine which integers are $u$-invariants of fields.
> The survey [MerkurjevParimala2025, §5.1] records the expectation that every odd integer $\ge 9$
> is a $u$-invariant (`u_invariant_values.variants.odd`). Given the results above, the problem is
> open exactly for the integers $2^r - 1$ and $2^r - 3$ with $r \ge 4$, the smallest of which are
> $13$ and $15$.
>
> *References:*
> - [Kaplansky1953] I. Kaplansky, *Quadratic forms*, J. Math. Soc. Japan 5 (1953), 200–207,
>   [doi:10.2969/jmsj/00520200](https://doi.org/10.2969/jmsj/00520200).
> - [Lam2005] T. Y. Lam, *Introduction to quadratic forms over fields*, Grad. Stud. Math. 67,
>   Amer. Math. Soc., 2005, [doi:10.1090/gsm/067](https://doi.org/10.1090/gsm/067).
> - [EKM2008] R. Elman, N. Karpenko, A. Merkurjev, *The algebraic and geometric theory of quadratic
>   forms*, Amer. Math. Soc. Colloq. Publ. 56, Amer. Math. Soc., 2008,
>   [doi:10.1090/coll/056](https://doi.org/10.1090/coll/056).
> - [Merkurjev1989] A. S. Merkurjev, *Kaplansky's conjecture in the theory of quadratic forms*
>   (Russian), Zap. Nauchn. Sem. LOMI 175 (1989), 75–89; English transl. J. Soviet Math. 57
>   (1991), no. 6, 3489–3497, [doi:10.1007/BF01100118](https://doi.org/10.1007/BF01100118).
> - [Merkurjev1991] A. S. Merkurjev, *Simple algebras and quadratic forms* (Russian), Izv. Akad.
>   Nauk SSSR Ser. Mat. 55 (1991), no. 1, 218–224; English transl. Math. USSR-Izv. 38 (1992),
>   no. 1, 215–221,
>   [doi:10.1070/IM1992v038n01ABEH002195](https://doi.org/10.1070/IM1992v038n01ABEH002195).
> - [Izhboldin2001] O. T. Izhboldin, *Fields of $u$-invariant $9$*, Ann. of Math. (2) 154 (2001),
>   no. 3, 529–587, [doi:10.2307/3062141](https://doi.org/10.2307/3062141).
> - [Vishik2009] A. Vishik, *Fields of $u$-invariant $2^r + 1$*, pp. 661–685 in Algebra,
>   arithmetic, and geometry: in honor of Yu. I. Manin, Vol. II, Progr. Math. 270, Birkhäuser,
>   2009, [doi:10.1007/978-0-8176-4747-6_22](https://doi.org/10.1007/978-0-8176-4747-6_22).
> - [Karpenko2026] N. A. Karpenko, *Fields of any $u$-invariant but a 2-power minus 1 or 3*,
>   preprint, 5 August 2026,
>   [author's web page](https://sites.ualberta.ca/~karpenko/publ/u1or3-02.pdf).
> - [MerkurjevParimala2025] A. Merkurjev, R. Parimala, *Quadratic forms beyond arithmetic*, Notices
>   Amer. Math. Soc. 72 (2025), no. 7, 711–718,
>   [doi:10.1090/noti3192](https://doi.org/10.1090/noti3192).

*Quoted from [FormalConjectures/Paper/KaplanskyUInvariant.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KaplanskyUInvariant.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 14 research or textbook statements: 4 open and 10 solved. It also has 2 test statements, counted here but not shown.

## `KaplanskyUInvariant.u_invariant_values`

Open: stated without proof.

> **The values of the $u$-invariant**, stated as in [MerkurjevParimala2025, §5.1]: which integers
> are $u$-invariants of fields (of characteristic not $2$)? The question goes back to
> [Kaplansky1953], who conjectured that only powers of $2$ occur
> (`u_invariant_values.variants.kaplansky_conjecture`). Every positive even integer is a
> $u$-invariant (`u_invariant_values.variants.even`), $3$, $5$ and $7$ are not
> (`u_invariant_values.variants.not_three`, `u_invariant_values.variants.not_five`,
> `u_invariant_values.variants.not_seven`), and it is expected that every odd integer $\ge 9$ is
> (`u_invariant_values.variants.odd`). Granting the preprint [Karpenko2026]
> (`u_invariant_values.variants.karpenko`), the answer is known for every $n$ except $n = 2^r - 1$
> and $n = 2^r - 3$ with $r \ge 4$.

```lean
theorem u_invariant_values :
    ∀ n, n ∈ u_invariant_values.answer ↔ IsUInvariant n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/KaplanskyUInvariant.lean, line 136](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KaplanskyUInvariant.lean#L136).

## `KaplanskyUInvariant.u_invariant_values.variants.kaplansky_conjecture`

Solved: stated here without proof.

> **Kaplansky's conjecture** [Kaplansky1953, p. 202]: the $u$-invariant of a field is a power of
> $2$ whenever it is finite. Disproved by Merkurjev, who constructed a field of $u$-invariant $6$
> [Merkurjev1989] (`u_invariant_values.variants.even`).

```lean
theorem u_invariant_values.variants.kaplansky_conjecture :
    ¬ ∀ n, IsUInvariant n → ∃ k, n = 2 ^ k
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/KaplanskyUInvariant.lean, line 146](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KaplanskyUInvariant.lean#L146).

## `KaplanskyUInvariant.u_invariant_values.variants.not_three`

Solved: stated here without proof.

> The $u$-invariant is never $3$ [Kaplansky1953, Theorem 2]; see also
> [Lam2005, Proposition XI.6.8] and [EKM2008, Corollary 36.4].

```lean
theorem u_invariant_values.variants.not_three : ¬ IsUInvariant 3
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/KaplanskyUInvariant.lean, line 153](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KaplanskyUInvariant.lean#L153).

## `KaplanskyUInvariant.u_invariant_values.variants.not_five`

Solved: stated here without proof.

> The $u$-invariant is never $5$ [Lam2005, Proposition XI.6.8], [EKM2008, Corollary 36.4].

```lean
theorem u_invariant_values.variants.not_five : ¬ IsUInvariant 5
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/KaplanskyUInvariant.lean, line 158](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KaplanskyUInvariant.lean#L158).

## `KaplanskyUInvariant.u_invariant_values.variants.not_seven`

Solved: stated here without proof.

> The $u$-invariant is never $7$ [Lam2005, Proposition XI.6.8], [EKM2008, Corollary 36.4].

```lean
theorem u_invariant_values.variants.not_seven : ¬ IsUInvariant 7
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/KaplanskyUInvariant.lean, line 163](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KaplanskyUInvariant.lean#L163).

## `KaplanskyUInvariant.u_invariant_values.variants.two_pow`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/47cc44ab944b6fd29b98a256ed4f92c8316f86bf/Proofs/T_KaplanskyUInvariant_u_invariant_values_variants_two_pow.lean#L563](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/47cc44ab944b6fd29b98a256ed4f92c8316f86bf/Proofs/T_KaplanskyUInvariant_u_invariant_values_variants_two_pow.lean#L563).

> Every power of $2$ is a $u$-invariant [Kaplansky1953, p. 202]: Theorem 3 of [Kaplansky1953]
> gives $u(F((t))) = 2u(F)$, so $u(\mathbb{C}((t_1)) \cdots ((t_k))) = 2^k$; see also
> [EKM2008, §38].

```lean
theorem u_invariant_values.variants.two_pow (k : ℕ) : IsUInvariant (2 ^ k)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/KaplanskyUInvariant.lean, line 173](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KaplanskyUInvariant.lean#L173).

## `KaplanskyUInvariant.u_invariant_values.variants.even`

Solved: stated here without proof.

> **Merkurjev's theorem** [Merkurjev1991], see also [EKM2008, Theorem 38.4]: every positive even
> integer is a $u$-invariant. The case $6$, the first counterexample to Kaplansky's conjecture, is
> [Merkurjev1989].

```lean
theorem u_invariant_values.variants.even (n : ℕ) (hn : Even n) (hn₀ : n ≠ 0) :
    IsUInvariant n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/KaplanskyUInvariant.lean, line 182](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KaplanskyUInvariant.lean#L182).

## `KaplanskyUInvariant.u_invariant_values.variants.nine`

Solved: stated here without proof.

> **Izhboldin's theorem** [Izhboldin2001]: there is a field of $u$-invariant $9$,
> the first example of an odd $u$-invariant greater than $1$.

```lean
theorem u_invariant_values.variants.nine : IsUInvariant 9
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/KaplanskyUInvariant.lean, line 189](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KaplanskyUInvariant.lean#L189).

## `KaplanskyUInvariant.u_invariant_values.variants.two_pow_add_one`

Solved: stated here without proof.

> **Vishik's theorem** [Vishik2009, Corollary 5.2]: for every $r \ge 3$ there is a field of
> $u$-invariant $2^r + 1$.

```lean
theorem u_invariant_values.variants.two_pow_add_one (r : ℕ) (hr : 3 ≤ r) :
    IsUInvariant (2 ^ r + 1)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/KaplanskyUInvariant.lean, line 195](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KaplanskyUInvariant.lean#L195).

## `KaplanskyUInvariant.u_invariant_values.variants.karpenko`

Solved: stated here without proof.

> **Karpenko's theorem** [Karpenko2026, Theorem 1.1]: if neither $n + 1$ nor $n + 3$ is a power
> of $2$, then there is a field of $u$-invariant $n$. This covers every positive integer except
> $1$, $3$, $5$, $7$ and the integers $2^r - 1$, $2^r - 3$ with $r \ge 4$. As of September 2026
> the result is a preprint and not yet peer-reviewed.

```lean
theorem u_invariant_values.variants.karpenko (n : ℕ) (h₁ : ∀ r, 2 ^ r ≠ n + 1)
    (h₃ : ∀ r, 2 ^ r ≠ n + 3) : IsUInvariant n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/KaplanskyUInvariant.lean, line 206](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KaplanskyUInvariant.lean#L206).

## `KaplanskyUInvariant.u_invariant_values.variants.eleven`

Proved here.

> The special case $n = 11$ of `u_invariant_values.variants.karpenko` (neither $12$ nor $14$ is a
> power of $2$), the first odd value not of the form $2^r + 1$ shown to be a $u$-invariant; it was
> announced in the preprint *Fields of $u$-invariant 11* (21 April 2026) that [Karpenko2026]
> absorbs.

```lean
theorem u_invariant_values.variants.eleven : IsUInvariant 11
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/KaplanskyUInvariant.lean, line 217](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KaplanskyUInvariant.lean#L217).

## `KaplanskyUInvariant.u_invariant_values.variants.odd`

Open: stated without proof.

> The expectation recorded in [MerkurjevParimala2025, §5.1]: every odd integer $\ge 9$ is a
> $u$-invariant. By `u_invariant_values.variants.karpenko` this is open exactly for the integers
> $2^r - 1$ and $2^r - 3$ with $r \ge 4$.

```lean
theorem u_invariant_values.variants.odd :
    ∀ n, Odd n → 9 ≤ n → IsUInvariant n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/KaplanskyUInvariant.lean, line 230](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KaplanskyUInvariant.lean#L230).

## `KaplanskyUInvariant.u_invariant_values.variants.thirteen`

Open: stated without proof.

> The smallest open case of the form $2^r - 3$: is there a field of $u$-invariant $13$?

```lean
theorem u_invariant_values.variants.thirteen : IsUInvariant 13
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/KaplanskyUInvariant.lean, line 236](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KaplanskyUInvariant.lean#L236).

## `KaplanskyUInvariant.u_invariant_values.variants.fifteen`

Open: stated without proof.

> The smallest open case of the form $2^r - 1$: is there a field of $u$-invariant $15$?

```lean
theorem u_invariant_values.variants.fifteen : IsUInvariant 15
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Paper/KaplanskyUInvariant.lean, line 241](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KaplanskyUInvariant.lean#L241).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/KaplanskyUInvariant.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/KaplanskyUInvariant.lean)
- [doi:10.2969/jmsj/00520200](https://doi.org/10.2969/jmsj/00520200)
