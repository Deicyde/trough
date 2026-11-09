---
declaration: theorem
origin: cited
lean: Erdos403.erdos_403
statement: formalized
---

# Erdős Problem 403

> *References:*
> - [erdosproblems.com/403](https://www.erdosproblems.com/403)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial
>   number theory*. Monographies de L'Enseignement Mathématique (1980).
> - [Li76] Lin, S., *On two problems of Erdős concerning sums of distinct factorials*.
>   Bell Laboratories internal memorandum (1960).

*Quoted from [FormalConjectures/ErdosProblems/403.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/403.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/403](https://www.erdosproblems.com/403).

The file states 1 research or textbook statement: 1 solved.

## `Erdos403.erdos_403`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/f8a51976fd2e66a52b4928c109fb9ae877a1a507/problems/403/Erdos403.lean](https://github.com/Jayyhk/erdos-lean/blob/f8a51976fd2e66a52b4928c109fb9ae877a1a507/problems/403/Erdos403.lean).

> Does the equation
> $$2^m=a_1!+\cdots+a_k!$$
> with $a_1\lt a_2\lt \cdots \lt a_k$ have only finitely many solutions?
>
> Asked by Burr and Erdős. Frankl and Lin [Li76] independently showed that the answer is yes, and
> the largest solution is
> $$2^7=2!+3!+5!.$$
> In fact Lin showed that the largest power of $2$ which can divide a sum of distinct factorials
> containing $2$ is $2^{254}$, and that there are only 5 solutions to $3^m=a_1!+\cdots+a_k!$
> (when $m=0,1,2,3,6$).
>
> See also [404].
>
> A solution is encoded below as a pair $(m, s)$ where $s$ is the finite set
> $\{a_1 < a_2 < \cdots < a_k\}$ of positive integers, so the distinctness of the $a_i$ is
> given by set membership. The empty set contributes no solutions since $2^m \geq 1 > 0$.
>
> The linked proof gives more than finiteness: it classifies the solutions outright, as
> $(0,\{1\})$, $(1,\{2\})$, $(3,\{2,3\})$, $(5,\{2,3,4\})$ and $(7,\{2,3,5\})$, so the set below
> has exactly five elements.

```lean
theorem erdos_403 :
    {p : ℕ × Finset ℕ | (∀ a ∈ p.2, 0 < a) ∧
      2 ^ p.1 = ∑ a ∈ p.2, a.factorial}.Finite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/403.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/403.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/403.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/403.lean)
- [erdosproblems.com/403](https://www.erdosproblems.com/403)
