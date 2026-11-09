---
declaration: theorem
origin: cited
lean: OeisA384222.conjecture_1, OeisA384222.conjecture_formula
statement: formalized
---

# Lengths of the 2-dense sublists of divisors of $n$

> Write the divisors of $n$ in increasing order and split this list between consecutive divisors
> $d < d'$ with $d' > 2d$. The pieces are the 2-dense sublists of divisors of $n$. Row $n$ of the
> triangle lists their lengths. Row $n$ of A384225 lists the numbers of odd terms in them.
>
> *References:*
> - [A384222](https://oeis.org/A384222)
> - [A384225](https://oeis.org/A384225)

*Quoted from [FormalConjectures/OEIS/384222.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/384222.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 7 test statements, counted here but not shown.

## `OeisA384222.conjecture_1`

Solved: stated here; a Lean proof is at [https://github.com/otoi-lab/oeis-lean-proofs/blob/14f275b8b370bcf76213de10bb3f8fda84a6461e/OeisProofs/FC/A384222.lean#L26-L31](https://github.com/otoi-lab/oeis-lean-proofs/blob/14f275b8b370bcf76213de10bb3f8fda84a6461e/OeisProofs/FC/A384222.lean#L26-L31).

> "Conjecture 1: row n is a palindromic composition of A000005(n)."
>
> A composition of $A000005(n)$ is a list of positive integers with sum $A000005(n)$, the number
> of divisors of $n$.
>
> Solved by Claude (Anthropic) prompted by otoinobuo. The map $d \mapsto n/d$ reverses the list
> of divisors and preserves the ratio of consecutive divisors.

```lean
theorem conjecture_1 (n : ℕ) (hn : 0 < n) :
    (∀ k ∈ row n, 0 < k) ∧ (row n).sum = n.divisors.card ∧ (row n).reverse = row n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/384222.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/384222.lean#L82).

## `OeisA384222.conjecture_formula`

Solved: stated here; a Lean proof is at [https://github.com/otoi-lab/oeis-lean-proofs/blob/14f275b8b370bcf76213de10bb3f8fda84a6461e/OeisProofs/FC/A384222.lean#L33-L36](https://github.com/otoi-lab/oeis-lean-proofs/blob/14f275b8b370bcf76213de10bb3f8fda84a6461e/OeisProofs/FC/A384222.lean#L33-L36).

> "T(n,k) = A384225(n,k) * A001511(n) = A384225(n,k) * A000005(n) / A001227(n). (conjectured)."
> - Omar E. Pol, Apr 13 2026
>
> This formalizes the first equality. The ruler function is $A001511(n) = \nu_2(n) + 1$.
>
> Solved by Claude (Anthropic) prompted by otoinobuo. If $d$ and $2d$ divide $n$, then they lie
> in the same 2-dense sublist. So each sublist is a union of sets $\{o, 2o, \dots, 2^{\nu_2(n)} o\}$
> with $o$ odd.

```lean
theorem conjecture_formula (n : ℕ) (hn : 0 < n) :
    row n = (oddRow n).map ((padicValNat 2 n + 1) * ·)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/384222.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/384222.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/384222.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/384222.lean)
- [A384222](https://oeis.org/A384222)
