---
declaration: theorem
origin: cited
lean: OeisA108081.count_words_in_x_is_a_shifted
statement: formalized
---

# $a(n) = \sum_{i=0}^n \binom{2n-i}{n+i}$

> Alternatively the sequence `a` can be defined as
> $a(n) = \sum_{k=0}^n \binom{n+k-1}{k} F(n-k+1)$, where $F(m)$ is the $m$-th Fibonacci number.
> We formalize a conjecture about the number of words of length $n$ in a set $X$ being related
> to this sequence.
>
> *References:*
> - [A108081](https://oeis.org/A108081)

*Quoted from [FormalConjectures/OEIS/108081.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/108081.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA108081.count_words_in_x_is_a_shifted`

Solved: stated here; a Lean proof is at [https://github.com/niketp03/atlas-fc-verified/blob/15e4b3a7584e218cec531aeaf71cce72a8a9ecb1/AtlasFCSolutions/OeisA108081.lean#L3720](https://github.com/niketp03/atlas-fc-verified/blob/15e4b3a7584e218cec531aeaf71cce72a8a9ecb1/AtlasFCSolutions/OeisA108081.lean#L3720).

> "The number of words of length $n$ for $n \le 12$ is given by $a(n+1)$. Is this always true?"
>
> Formalized as $|X_n| = a(n-1)$ for $n \ge 1$, because the sequence values $a(0)=1, a(1)=2, a(2)=7$
> match the examples given for word lengths $n=1, 2, 3$ respectively.
>
> Solved: a Lean 4 proof, derived from the Atlas proofs in
> [facebookresearch/atlas-lean](https://github.com/facebookresearch/atlas-lean), is linked in
> `formal_proof`.

```lean
theorem count_words_in_x_is_a_shifted (n : ℕ) :
    n ≥ 1 → Set.ncard (xN n) = a (n - 1)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/OEIS/108081.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/108081.lean#L96).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/108081.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/108081.lean)
- [A108081](https://oeis.org/A108081)
