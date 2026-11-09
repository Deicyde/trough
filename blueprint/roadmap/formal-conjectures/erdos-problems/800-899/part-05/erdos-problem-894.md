---
declaration: theorem
origin: cited
lean: Erdos894.erdos_894
statement: formalized
---

# Erdős Problem 894

> *References:*
> - [erdosproblems.com/894](https://www.erdosproblems.com/894)
> - [Ka01] Katznelson, Y., *Chromatic numbers of Cayley graphs on $\mathbb{Z}$ and recurrence*.
>   Combinatorica (2001), 211--219.
> - [PeSc10] Peres, Yuval and Schlag, Wilhelm, *Two Erdős problems on lacunary sequences: chromatic
>   number and Diophantine approximation*. Bull. Lond. Math. Soc. (2010), 295--300.

*Quoted from [FormalConjectures/ErdosProblems/894.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/894.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/894](https://www.erdosproblems.com/894).

The file states 1 research or textbook statement: 1 solved.

## `Erdos894.erdos_894`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos894.lean#L310](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos894.lean#L310).

> Let $A=\{n_1\lt n_2\lt \cdots\}\subset \mathbb{N}$ be a lacunary sequence (so there exists some
> $\epsilon>0$ with $n_{k+1}\geq (1+\epsilon)n_k$ for all $k$). Is it true that there must exist a
> finite colouring of $\mathbb{N}$ with no monochromatic solutions to $a-b\in A$?
>
> Asked by Erdős in 1987, according to Katznelson [Ka01]. In other words, does the Cayley graph
> defined on $\mathbb{Z}$ by a lacunary sequence have a finite chromatic number?
>
> Katznelson observed that a positive solution to the problem follows from the answer to
> [464](https://www.erdosproblems.com/464), which yields an irrational $\theta$ and $\delta>0$
> such that $\inf_k \| \theta n_k\|>\delta$. In particular, the solution to
> [464](https://www.erdosproblems.com/464) implies the answer to this question is yes, with the
> best known quantitative bound, due to Peres and Schlag [PeSc10], being that there is a colouring
> with no solutions using at most $\ll \epsilon^{-1}\log(1/\epsilon)$ colours.

```lean
theorem erdos_894 :
    ∀ n : ℕ → ℕ, StrictMono n → (∀ k, 0 < n k) → IsLacunary n →
      ∃ (r : ℕ) (c : ℕ → Fin r), ∀ b k, c (b + n k) ≠ c b
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/894.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/894.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/894.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/894.lean)
- [erdosproblems.com/894](https://www.erdosproblems.com/894)
