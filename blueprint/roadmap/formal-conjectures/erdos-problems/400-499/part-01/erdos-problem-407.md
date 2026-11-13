---
declaration: theorem
origin: cited
lean: Erdos407.erdos_407
statement: formalized
---

# Erdős Problem 407

> *References:*
> - [erdosproblems.com/407](https://www.erdosproblems.com/407)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [EGST88] Evertse, J.-H. and Győry, K. and Stewart, C. L. and Tijdeman, R., *$S$-unit equations
>   and their applications*. New advances in transcendence theory (Durham, 1986) (1988), 110-174.
> - [TiWa88] Tijdeman, R. and Wang, Lian Xiang, *Sums of products of powers of given prime
>   numbers*. Pacific J. Math. (1988), 177-193.
> - [BaBe24] Bajpai, Prajeet and Bennett, Michael A., *Effective $S$-unit equations beyond three
>   terms: Newman's conjecture*. Acta Arith. (2024), 421-458.

*Quoted from [FormalConjectures/ErdosProblems/407.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/407.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/407](https://www.erdosproblems.com/407).

The file states 1 research or textbook statement: 1 solved.

## `Erdos407.erdos_407`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos407.lean#L257](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos407.lean#L257).

> Let $w(n)$ count the number of solutions to
>
> $$n=2^a+3^b+2^c3^d$$
>
> with $a,b,c,d\geq 0$ integers. Is it true that $w(n)$ is bounded by some absolute constant?
>
> A conjecture originally due to Newman.
>
> This is true, and was proved by Evertse, Győry, Stewart, and Tijdeman [EGST88].
>
> Quantitative bounds were provided by Tijdeman and Wang [TiWa88], who proved that (if $w(n)$ only
> counts distinct solutions, where we call two solutions distinct if the sets
> $\{2^a,3^b,2^{c}3^d\}$ are distinct) then $w(n) \leq 4$ for all large $n$.
>
> This was made effective by Bajpai and Bennett [BaBe24], who proved that $w(n)\leq 4$ if
> $n\geq 131082$ and $w(n)\leq 9$ for all $n$. (The largest $n$ for which $w(n)=9$ is $299$.)

```lean
theorem erdos_407 : ∃ C : ℕ, ∀ n : ℕ, w n ≤ C
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/407.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/407.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/407.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/407.lean)
- [erdosproblems.com/407](https://www.erdosproblems.com/407)
