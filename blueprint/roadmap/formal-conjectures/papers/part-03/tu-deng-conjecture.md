---
declaration: theorem
origin: cited
lean: TuDengConjecture.tu_deng_conjecture
statement: formalized
---

# Tu-Deng Conjecture

> *References:*
> * [Tu, Z., Deng, Y., *A conjecture about binary strings and its applications on constructing
>   Boolean functions with optimal algebraic immunity*, Des. Codes Cryptogr. **60** (2011),
>   1–14](https://doi.org/10.1007/s10623-010-9413-9)
> * [IACR ePrint 2009/272](https://eprint.iacr.org/2009/272)
> * [LLX26] [Liu, R., Luo, H., Xie, T., *A Complete Proof for Tu-Deng Conjecture*, arXiv:2608.05187v2
>   (2026)](https://arxiv.org/abs/2608.05187v2)
> * [Cu26] [Cusick, T. W., *Proof of the TuDeng Conjecture*, arXiv:2608.14821
>   (2026)](https://arxiv.org/abs/2608.14821)
> * [Lean26] [A Lean 4 proof of the count form of the conjecture](https://github.com/ifeelok92/tu-deng-conjecture-lean-formal-proof/blob/3c00561415deedcdc56b9e803042c1d0f15f5d5b/TuDengFormal/FirstExitNat.lean#L529-L535),
>   commit `3c005614`, theorem `TuDeng.FirstExit.tu_deng_conjecture_full`
>
> For an integer $k \ge 2$, identify the residues modulo $2^k - 1$ with the integers
> $0, 1, \dots, 2^k - 2$, and let $w(a)$ denote the binary weight of $a$ (the number of ones in
> its binary expansion). The Tu-Deng conjecture states that for every residue $t \ne 0$,
>
> $$\#\{(a, b) : a + b \equiv t \pmod{2^k - 1},\ w(a) + w(b) \le k - 1\} \le 2^{k-1}.$$
>
> Tu and Deng showed that this combinatorial statement implies that their constructions of
> Boolean functions (a bent class and a balanced class) achieve optimal algebraic immunity,
> which is the motivation for the conjecture. They verified the conjecture numerically for
> $k \le 29$ (Remark 3.1 of the ePrint version).
>
> The conjecture is no longer open: [LLX26] and, independently, [Cu26] give complete proofs.
> [Lean26] is a Lean 4 development of the same bound, stated for the count of natural-number
> representatives $x < 2^k - 1$ rather than for the set of residue pairs used below.

*Quoted from [FormalConjectures/Paper/TuDengConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/TuDengConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `TuDengConjecture.tu_deng_conjecture`

Solved: stated here without proof.

> **The Tu-Deng conjecture.** For $k \ge 2$ and a nonzero residue $t$ modulo $2^k - 1$, there
> are at most $2^{k-1}$ pairs of residues $(a, b)$ with $a + b = t$ whose binary weights
> (of their representatives in $0, \dots, 2^k - 2$) sum to at most $k - 1$.
>
> Proved in [LLX26] and independently in [Cu26]; see also the Lean development [Lean26].

```lean
theorem tu_deng_conjecture (k : ℕ) (hk : 2 ≤ k) (t : ZMod (2 ^ k - 1)) (ht : t ≠ 0) :
    {p : ZMod (2 ^ k - 1) × ZMod (2 ^ k - 1) |
        p.1 + p.2 = t ∧ binaryWeight p.1.val + binaryWeight p.2.val ≤ k - 1}.ncard
      ≤ 2 ^ (k - 1)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [94 Information and communication, circuits](../../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/Paper/TuDengConjecture.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/TuDengConjecture.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/TuDengConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/TuDengConjecture.lean)
- [Tu, Z., Deng, Y., *A conjecture about binary strings and its applications on constructing
  Boolean functions with optimal algebraic immunity*, Des. Codes Cryptogr. **60** (2011),
  1–14](https://doi.org/10.1007/s10623-010-9413-9)
