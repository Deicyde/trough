---
declaration: theorem
origin: cited
lean: Erdos796.erdos_796
statement: formalized
---

# Erdős Problem 796

> *Reference:* [erdosproblems.com/796](https://www.erdosproblems.com/796)

*Quoted from [FormalConjectures/ErdosProblems/796.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/796.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/796](https://www.erdosproblems.com/796).

The file states 1 research or textbook statement: 1 solved.

## `Erdos796.erdos_796`

Solved: stated here; a Lean proof is at [https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-796/Research/CanonicalTail.lean](https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-796/Research/CanonicalTail.lean).

> Let $k\geq 2$ and let $g_k(n)$ be the largest possible size of
> $A\subseteq \{1,\ldots,n\}$ such that every $m$ has $\lt k$ solutions to
> $m=a_1a_2$ with $a_1\lt a_2\in A$. Is it true that
> $$g_3(n)=\frac{\log\log n}{\log n}n+(c+o(1))\frac{n}{\log n}$$
> for some constant $c$?
>
> The answer is yes: the rescaled error `normalizedError` converges.

```lean
theorem erdos_796 :
    ∃ c : ℝ, Tendsto normalizedError atTop (𝓝 c)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/796.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/796.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/796.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/796.lean)
- [erdosproblems.com/796](https://www.erdosproblems.com/796)
