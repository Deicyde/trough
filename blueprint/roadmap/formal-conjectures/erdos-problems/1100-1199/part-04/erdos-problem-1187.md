---
declaration: theorem
origin: cited
lean: Erdos1187.erdos_1187.parts.i, Erdos1187.erdos_1187.parts.ii
statement: formalized
---

# Erdős Problem 1187

> *References:*
> - [erdosproblems.com/1187](https://www.erdosproblems.com/1187)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115.
> - [GrTa08] Green, Ben and Tao, Terence, *The primes contain arbitrarily long arithmetic
>   progressions*. Ann. of Math. (2) (2008), 481-547.

*Quoted from [FormalConjectures/ErdosProblems/1187.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1187.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1187](https://www.erdosproblems.com/1187).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1187.erdos_1187.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1187.lean#L246](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1187.lean#L246).

> Let $k\geq 3$. Is it true that, in any finite colouring of the integers, there are monochromatic
> arithmetic progressions of primes of length $k$?
>
> It follows from the theorem of Green and Tao [GrTa08] (that any set of primes with positive
> relative density contains arbitrarily long arithmetic progressions) that the answer to the first
> question is yes for any $k\geq 3$.
>
> See also [219](https://www.erdosproblems.com/219).

```lean
theorem erdos_1187.parts.i : ∀ k : ℕ, 3 ≤ k →
    ∀ (κ : Type) [Finite κ] (c : ℤ → κ), ∃ S : Set ℤ, S.IsAPOfLength k ∧
      (∀ n ∈ S, ∃ p : ℕ, p.Prime ∧ (p : ℤ) = n) ∧
        ∃ γ : κ, ∀ n ∈ S, c n = γ
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1187.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1187.lean#L48).

## `Erdos1187.erdos_1187.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1187.lean#L246](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1187.lean#L246).

> Let $k\geq 3$. In any finite colouring of the integers, are there monochromatic arithmetic
> progressions of length $k$ whose common difference is a prime?
>
> The answer to the second question is trivially no: colouring the integers by their residue modulo
> $4$ creates a colouring in which there is not even any monochromatic pair of integers whose
> difference is a prime. Alternatively, one can just use $2$ colours and avoid any $3$-term
> progressions whose difference is a prime by colouring $0,1\pmod{4}$ red and $2,3\pmod{4}$ blue.

```lean
theorem erdos_1187.parts.ii : ¬ ∀ k : ℕ, 3 ≤ k →
    ∀ (κ : Type) [Finite κ] (c : ℤ → κ), ∃ (a : ℤ) (p : ℕ) (S : Set ℤ), p.Prime ∧
      S.IsAPOfLengthWith k a p ∧ ∃ γ : κ, ∀ n ∈ S, c n = γ
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1187.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1187.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1187.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1187.lean)
- [erdosproblems.com/1187](https://www.erdosproblems.com/1187)
