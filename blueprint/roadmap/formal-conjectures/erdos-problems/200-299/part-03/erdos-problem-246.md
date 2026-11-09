---
declaration: theorem
origin: cited
lean: Erdos246.erdos_246
statement: formalized
---

# Erdős Problem 246

> *References:*
> - [erdosproblems.com/246](https://www.erdosproblems.com/246)
> - [Bi59] Birch, B. J., *Note on a problem of Erd\H{o}s*. Proc. Cambridge
>   Philos. Soc. (1959), 370-373.
> - [Ca60] Cassels, J. W. S., *On the representation of integers as the sums of
>   distinct summands taken from a fixed set*. Acta Sci. Math. (Szeged) (1960),
>   111-124.
> - [FaCh17] Fang, Jin-Hui and Chen, Yong-Gao, *A quantitative form of the
>   {E}rd\H{o}s-{B}irch theorem*. Acta Arith. (2017), 301--311.
> - [He00b] Hegyv\'{a}ri, N., *On the completeness of an exponential type
>   sequence*. Acta Math. Hungar. (2000), 127--135.
> - [Yu24] Yu, Wang-Xing, *On the representation of an exponential type sequence*.
>   Publ. Math. Debrecen (2024), 253--261.

*Quoted from [FormalConjectures/ErdosProblems/246.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/246.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/246](https://www.erdosproblems.com/246).

The file states 1 research or textbook statement: 1 solved.

## `Erdos246.erdos_246`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos246.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos246.lean).

> Let $(a,b)=1$. The set $\{a^kb^l: k,l\geq 0\}$ is complete - that is, every large integer is the sum of distinct integers of the form $a^kb^l$ with $k,l\geq 0$.
>
> We state the nontrivial case $a,b\geq 2$, proved by Birch [Bi59].

```lean
theorem erdos_246 (a b : ℕ) (ha : 2 ≤ a) (hb : 2 ≤ b) (hab : Nat.Coprime a b) :
    IsAddComplete (Gamma a b)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/246.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/246.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/246.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/246.lean)
- [erdosproblems.com/246](https://www.erdosproblems.com/246)
