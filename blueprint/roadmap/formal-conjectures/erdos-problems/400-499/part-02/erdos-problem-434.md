---
declaration: theorem
origin: cited
lean: Erdos434.erdos_434.parts.i, Erdos434.erdos_434.parts.ii
statement: formalized
---

# Erdős Problem 434

> *References:*
> - [erdosproblems.com/434](https://www.erdosproblems.com/434)
> - [Ki02] Kiss, G., On the extremal Frobenius problem in a new aspect. Ann. Univ. Sci.
>   Budapest. Eötvös Sect. Math. (2002), 139–142.

*Quoted from [FormalConjectures/ErdosProblems/434.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/434.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/434](https://www.erdosproblems.com/434).

The file states 2 research or textbook statements: 2 solved.

## `Erdos434.erdos_434.parts.i`

Solved: stated here; a Lean proof is at [https://www.erdosproblems.com/forum/thread/434#post-4437](https://www.erdosproblems.com/forum/thread/434#post-4437).

> Let $k \le n$. What choice of $A\subseteq\{1, \dots, n\}$ (with $\text{gcd}(A) = 1$) of size $|A| = k$
> maximises the number of integers not representable as the sum of finitely
> many elements from $A$ (with repetitions allowed)?
> Is it $\{n, n - 1, \dots, n - k + 1\}$?
>
> The maximal choice is indeed $\{n, \dots, n - k + 1\}$, as proved by Kiss [Ki02].
>
> The Lean theorem assumes $2 \le k$. When $k = 1 < n$, the proposed singleton $\{n\}$ does not
> have gcd $1$; the gcd condition instead forces the unique admissible choice $A = \{1\}$.

```lean
theorem erdos_434.parts.i (n k : ℕ) (hn : 1 ≤ n) (hk : 2 ≤ k) (h : k ≤ n) :
    IsGreatest
      { Nat.NcardUnrepresentable S | (S : Finset ℕ) (_ : S ⊆ Finset.Icc 1 n)
        (_ : #S = k) (_ : S.gcd id = 1) }
      (Nat.NcardUnrepresentable <| erdos_434.parts.i.answer n k)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/434.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/434.lean#L65).

## `Erdos434.erdos_434.parts.ii`

Solved: stated here; a Lean proof is at [https://www.erdosproblems.com/forum/thread/434#post-4437](https://www.erdosproblems.com/forum/thread/434#post-4437).

> For $2 \le k \le n$, the interval $A = \{n, n - 1, \dots, n - k + 1\}$ maximises the number
> of integers not representable as the sum of finitely many elements from $A$ (with repetitions
> allowed), as proved by Kiss [Ki02].

```lean
theorem erdos_434.parts.ii : ∀ᵉ (n ≥ 1) (k ≥ 2), k ≤ n →
    IsGreatest
      { Nat.NcardUnrepresentable S | (S : Finset ℕ) (_ : S ⊆ Finset.Icc 1 n)
        (_ : #S = k) (_ : S.gcd id = 1)}
      (Nat.NcardUnrepresentable <| Set.Icc (n - k + 1 : ℕ) n)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/434.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/434.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/434.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/434.lean)
- [erdosproblems.com/434](https://www.erdosproblems.com/434)
