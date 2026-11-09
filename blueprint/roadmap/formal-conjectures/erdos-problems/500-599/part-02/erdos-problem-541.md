---
declaration: theorem
origin: cited
lean: Erdos541.erdos_541, Erdos541.erdos_541.variants.general_moduli, Erdos541.erdos_541.variants.large_primes
statement: formalized
---

# Erdős Problem 541

> *References:*
> - [erdosproblems.com/541](https://www.erdosproblems.com/541)
> - [ErSz76] Erdős, E. and Szemerédi, E., On a problem of Graham. Publ. Math. Debrecen (1976),
>   123--127.
> - [GHW10] Gao, Weidong and Hamidoune, Yahya Ould and Wang, Guoqing, Distinct length modular zero-sum
>   subsequences: a proof of Graham's conjecture. J. Number Theory (2010), 1425--1431.

*Quoted from [FormalConjectures/ErdosProblems/541.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/541.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/541](https://www.erdosproblems.com/541).

The file states 3 research or textbook statements: 3 solved.

## `Erdos541.erdos_541`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos541.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos541.lean).

> Let $a_1, \dots, a_p$ be (not necessarily distinct) residues modulo a prime $p$, such that there
> exists some $r$ so that if $S \subseteq [p]$ is non-empty and
> $$\sum_{i \in S} a_i \equiv 0 \pmod{p}$$
> then $|S| = r$.
>
> Must there be at most two distinct residues amongst the $a_i$?
>
> This was formalized in Lean by Alexeev using Aristotle and ChatGPT.

```lean
theorem erdos_541 : (∀ p, Fact p.Prime → ∀ (a : Fin p → ZMod p),
    (∃ r, ∀ (S : Finset (Fin p)), S ≠ ∅ → ∑ i ∈ S, a i = 0 → S.card = r) →
      (Set.range a).ncard ≤ 2)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/541.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/541.lean#L49).

## `Erdos541.erdos_541.variants.general_moduli`

Solved: stated here without proof.

> Gao, Hamidoune, and Wang [GHW10] solved this for all moduli `p` (not necessarily prime).

```lean
theorem erdos_541.variants.general_moduli (p : ℕ) (a : Fin p → ZMod p)
    (ha₀ : ∃ r, ∀ (S : Finset (Fin p)), S ≠ ∅ → ∑ i ∈ S, a i = 0 → S.card = r) :
      (Set.range a).ncard ≤ 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/541.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/541.lean#L56).

## `Erdos541.erdos_541.variants.large_primes`

Solved: stated here without proof.

> This was proved by Erdős and Szemerédi [ErSz76] for p sufficiently large.

```lean
theorem erdos_541.variants.large_primes : ∀ᶠ p in atTop, p.Prime → ∀ a : Fin p → ZMod p,
    (∃ r, ∀ (S : Finset (Fin p)), S ≠ ∅ → ∑ i ∈ S, a i = 0 → S.card = r) →
      (Set.range a).ncard ≤ 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/541.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/541.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/541.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/541.lean)
- [erdosproblems.com/541](https://www.erdosproblems.com/541)
