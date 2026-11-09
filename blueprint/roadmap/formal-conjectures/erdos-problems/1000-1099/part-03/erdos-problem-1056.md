---
declaration: theorem
origin: cited
lean: Erdos1056.erdos_1056, Erdos1056.erdos_1056.variants.k2, Erdos1056.erdos_1056.variants.k3, Erdos1056.erdos_1056.variants.noll_simmons
statement: formalized
---

# Erdős Problem 1056

> *Reference:* [erdosproblems.com/1056](https://www.erdosproblems.com/1056)

*Quoted from [FormalConjectures/ErdosProblems/1056.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1056.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1056](https://www.erdosproblems.com/1056).

The file states 4 research or textbook statements: 2 open and 2 textbook results.

## `Erdos1056.erdos_1056`

Open: stated without proof.

> Let $k ≥ 2$. Does there exist a prime $p$ and consecutive intervals $I_0,\dots,I_k$
> such that $\prod\limits_{n{\in}I_i}n \equiv 1 \mod n$ for all $1 \le i \le k$?

```lean
theorem erdos_1056 :
    ∀ k ≥ 2, ∃ (p : ℕ) (_ : p.Prime) (boundaries : Fin (k + 1) → ℕ) (_ : StrictMono boundaries),
    AllModProdEqualsOne p boundaries
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1056.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1056.lean#L44).

## `Erdos1056.erdos_1056.variants.k2`

Textbook result, proved here.

> This is problem A15 in Guy's collection [Gu04], where he reports that in a letter in 1979
> Erdős observed that $3 * 4 \equiv 5 * 6 * 7 \equiv 1 \mod 11$.

```lean
theorem erdos_1056.variants.k2 :
    AllModProdEqualsOne 11 ![3, 5, 8]
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1056.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1056.lean#L54).

## `Erdos1056.erdos_1056.variants.k3`

Textbook result, proved here.

> Makowski [Ma83] found, for $k=3$:
> $2 * 3 * 4 * 5 \equiv 6 * 7 * 8 * 9 * 10 * 11 \equiv 12 * 13 * 14 * 15 \equiv 1 \mod 17$.

```lean
theorem erdos_1056.variants.k3 :
    AllModProdEqualsOne 17 ![2, 6, 12, 16]
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1056.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1056.lean#L64).

## `Erdos1056.erdos_1056.variants.noll_simmons`

Open: stated without proof.

> Noll and Simmons asked, more generally, whether there are solutions to
> $q_1! \equiv \dots \equiv q_k! \mod p$ for arbitrarily large $k$ (with $q_1 < \dots < q_k$).

```lean
theorem erdos_1056.variants.noll_simmons :
    ∀ᶠ k in Filter.atTop,
    ∃ (p : ℕ) (_ : p.Prime) (Q : Fin k → ℕ) (_ : StrictMono Q) (_ : ∀ i, Q i < p),
    ∀ i j : Fin k, (Q i)! ≡ (Q j)! [MOD p]
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1056.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1056.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1056.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1056.lean)
- [erdosproblems.com/1056](https://www.erdosproblems.com/1056)
