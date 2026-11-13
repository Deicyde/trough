---
declaration: theorem
origin: cited
lean: Erdos171.erdos_171
statement: formalized
---

# Erdős Problem 171

> *References:*
> - [erdosproblems.com/171](https://www.erdosproblems.com/171)
> - [ErGr79] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory: van der Waerden's theorem and related topics*. Enseign. Math. (1979), 325-344.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [FuKa91] Furstenberg, H. and Katznelson, Y., *A density version of the Hales-Jewett Theorem*.
>   Journal d'Analyse Mathématique (1991), 64-119.
> - [Po12] Polymath, D. H. J., *A new proof of the density Hales–Jewett theorem*. Ann. Math.
>   (2012), 1283-1327.

*Quoted from [FormalConjectures/ErdosProblems/171.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/171.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/171](https://www.erdosproblems.com/171).

The file states 1 research or textbook statement: 1 solved.

## `Erdos171.erdos_171`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos171.lean#L42](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos171.lean#L42).

> Is it true that for every $\epsilon>0$ and integer $t\geq 1$, if $N$ is sufficiently large and
> $A$ is a subset of $[t]^N$ of size at least $\epsilon t^N$ then $A$ must contain a combinatorial
> line $P$ (a set $P=\{p_1,\ldots,p_t\}$ where for each coordinate $1\leq j\leq t$ the $j$th
> coordinate of $p_i$ is either $i$ or constant).
>
> The 'density Hales-Jewett' problem. This was proved by Furstenberg and Katznelson [FuKa91]. A
> new elementary proof, which gives quantitative bounds, was proved by the Polymath project
> [Po12].
>
> Combinatorial lines are Mathlib's `Combinatorics.Line (Fin t) (Fin N)` (which have at least one
> non-constant coordinate).

```lean
theorem erdos_171 : ∀ ε : ℝ, 0 < ε → ∀ t : ℕ, 1 ≤ t → ∀ᶠ N : ℕ in atTop,
    ∀ A : Finset (Fin N → Fin t), ε * t ^ N ≤ A.card →
      ∃ l : Combinatorics.Line (Fin t) (Fin N), ∀ i : Fin t, l i ∈ A
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/171.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/171.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/171.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/171.lean)
- [erdosproblems.com/171](https://www.erdosproblems.com/171)
