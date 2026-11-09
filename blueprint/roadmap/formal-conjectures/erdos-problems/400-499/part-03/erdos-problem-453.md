---
declaration: theorem
origin: cited
lean: Erdos453.erdos_453
statement: formalized
---

# Erdős Problem 453

> *References:*
> - [erdosproblems.com/453](https://www.erdosproblems.com/453)
> - [Er70b] Erdős, P., *Some applications of graph theory to number theory*. Proc. Second Chapel Hill
>   Conf. on Combinatorial Mathematics and its Applications (Univ. North Carolina, Chapel Hill, N.C.,
>   1970) (1970), 136-145.
> - [Er74b] Erdős, P., *Remarks on some problems in number theory*. Math. Balkanica (1974), 197-202.
> - [Er77c] Erdős, Paul, *Problems and results on combinatorial number theory. III*. Number theory day
>   (Proc. Conf., Rockefeller Univ., New York, 1976) (1977), 43-72.
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Gu04] Guy, Richard K., *Unsolved problems in number theory*. (2004), xviii+437.
> - [Po79] Pomerance, Carl, *The prime number graph*. Math. Comp. (1979), 399-408.

*Quoted from [FormalConjectures/ErdosProblems/453.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/453.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/453](https://www.erdosproblems.com/453).

The file states 1 research or textbook statement: 1 solved.

## `Erdos453.erdos_453`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos453.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos453.lean).

> Is it true that, for all sufficiently large $n$, there exists some $i\lt n$ such that
> $$
> p_n^2 < p_{n+i}p_{n-i},
> $$
> where $p_k$ is the $k$th prime?
>
> Pomerance proved that the answer is no.

```lean
theorem erdos_453 : ¬ EventuallyHasPrimeWitness
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/453.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/453.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/453.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/453.lean)
- [erdosproblems.com/453](https://www.erdosproblems.com/453)
