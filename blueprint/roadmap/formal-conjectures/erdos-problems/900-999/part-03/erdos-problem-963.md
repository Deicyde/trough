---
declaration: theorem
origin: cited
lean: Erdos963.erdos_963.parts.i, Erdos963.erdos_963.parts.ii, Erdos963.erdos_963.variants.greedy, Erdos963.erdos_963.variants.positive
statement: formalized
---

# Erdős Problem 963

> *References:*
> - [erdosproblems.com/963](https://www.erdosproblems.com/963)
> - [Er65] Erdős, P., *Extremal problems in number theory*. Proc. Sympos. Pure Math., Vol. VIII
>   (1965), 181-189. [PDF](https://www.renyi.hu/~p_erdos/1965-02.pdf)
>
> A set `B` of real numbers is dissociated if all sums over its finite subsets are distinct. This is
> `AddDissociated` in Mathlib.

*Quoted from [FormalConjectures/ErdosProblems/963.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/963.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/963](https://www.erdosproblems.com/963).

The file states 4 research or textbook statements: 3 open and 1 solved. It also has 2 API statements, counted here but not shown.

## `Erdos963.erdos_963.parts.i`

Open: stated without proof.

> Let $f(n)$ be the maximal $k$ such that in any set $A\subset \mathbb{R}$ of size $n$ there is a
> subset $B\subseteq A$ of size $\lvert B\rvert\geq k$ which is dissociated that is, the sums
> $\sum_{b\in S}b$ are distinct for all $S\subseteq B$. Estimate $f(n)$ - in particular, is it true
> that $f(n)\geq \lfloor \log_2 n\rfloor$?
>
> This is the first part, a problem of Erdős [Er65, p. 188]. We read "estimate" as an asymptotic
> equivalence $f(n)\sim$ `answer n`. The order of magnitude $\log n$ is easy (see
> `erdos_963.variants.greedy` and the example $a_i=i$ in [Er65, p. 188]), so the question is the
> constant.

```lean
theorem erdos_963.parts.i :
    (fun n : ℕ ↦ (f n : ℝ)) ~[atTop] erdos_963.parts.i.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/963.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/963.lean#L81).

## `Erdos963.erdos_963.parts.ii`

Open: stated without proof.

> Let $f(n)$ be the maximal $k$ such that in any set $A\subset \mathbb{R}$ of size $n$ there is a
> subset $B\subseteq A$ of size $\lvert B\rvert\geq k$ which is dissociated that is, the sums
> $\sum_{b\in S}b$ are distinct for all $S\subseteq B$. Estimate $f(n)$ - in particular, is it true
> that $f(n)\geq \lfloor \log_2 n\rfloor$?
>
> This is the second part. Erdős [Er65, p. 188] asks whether the bound $\lfloor\log_3 n\rfloor$ can
> be improved to $\lfloor\log_2 n\rfloor$. We state it for all $n\geq 1$, with
> $\lfloor\log_2 n\rfloor$ written as `Nat.log 2 n`.
>
> As on the problem page, $A$ is any set of reals. [Er65] speaks of "given numbers" and uses the
> example $a_i=i$. Allowing negative numbers makes the question harder. A dissociated set never
> contains both $x$ and $-x$, and changing signs keeps a set dissociated. So the largest dissociated
> subsets of $A$ and of $\{\lvert a\rvert : a\in A,\ a\neq 0\}$ have the same size, and the sets
> $\{\pm a : a\in S\}$ (with $0$ added for odd $n$) show that $f(2m)=f(2m+1)$ is the least size of a
> largest dissociated subset of a set of $m$ positive reals. Hence this statement asks for
> $\lfloor\log_2 m\rfloor+1$ for $m$ positive reals. The question for positive reals with
> $\lfloor\log_2\lvert A\rvert\rfloor$, one less, is `erdos_963.variants.positive`; it follows from
> this statement.

```lean
theorem erdos_963.parts.ii : ∀ n : ℕ, 1 ≤ n → Nat.log 2 n ≤ f n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/963.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/963.lean#L106).

## `Erdos963.erdos_963.variants.greedy`

Proved here.

> Erdős noted that the greedy algorithm showed $f(n)\geq \lfloor \log_3 n\rfloor$
> [Er65, p. 188].

```lean
theorem erdos_963.variants.greedy (n : ℕ) : Nat.log 3 n ≤ f n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/963.lean, line 154](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/963.lean#L154).

## `Erdos963.erdos_963.variants.positive`

Open: stated without proof.

> The second part for sets of positive reals, with $\lfloor\log_2\lvert A\rvert\rfloor$ as in
> [Er65, p. 188] and its example $a_i=i$: every set $A$ of positive reals has a dissociated subset
> with at least $\lfloor\log_2 \lvert A\rvert\rfloor$ elements.

```lean
theorem erdos_963.variants.positive :
    ∀ A : Finset ℝ, (∀ a ∈ A, 0 < a) →
      ∃ B ⊆ A, Nat.log 2 A.card ≤ B.card ∧ AddDissociated (B : Set ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/963.lean, line 190](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/963.lean#L190).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/963.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/963.lean)
- [erdosproblems.com/963](https://www.erdosproblems.com/963)
