---
declaration: theorem
origin: cited
lean: Erdos958.erdos_958
statement: formalized
---

# Erdős Problem 958

> *References:*
> - [erdosproblems.com/958](https://www.erdosproblems.com/958)
> - [CDL25] Clemen, F., Dumitrescu, A. and Liu, D., *On multiplicities of interpoint distances*.
>   arXiv:2505.04283 (2025).
> - [PALOMAR-2026-10-05-000004](https://palomar-registry.org/entry.html?id=PALOMAR-2026-10-05-000004&version=1)

*Quoted from [FormalConjectures/ErdosProblems/958.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/958.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/958](https://www.erdosproblems.com/958).

The file states 1 research or textbook statement: 1 solved.

## `Erdos958.erdos_958`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/08152671ab394392fd941b18654daba734c26518/erdos-958/Solution.lean#L60](https://github.com/linrock/math-proofs/blob/08152671ab394392fd941b18654daba734c26518/erdos-958/Solution.lean#L60).

> Let $A\subset \mathbb{R}^2$ be a finite set of size $n$, and let $\{d_1,\ldots,d_k\}$ be the set of
> distances determined by $A$. Let $f(d)$ be the multiplicity of $d$, that is, the number of
> unordered pairs from $A$ of distance $d$ apart.
>
> Is it true that $k=n-1$ and $\{f(d_i)\}=\{n-1,\ldots,1\}$ if and only if $A$ is a set of
> equidistant points on a line or a circle?
>
> Erdős conjectured that the answer is no, and other such configurations exist.
>
> This was proved by Clemen, Dumitrescu, and Liu [CDL25], who observed that equidistant points on a
> short circular arc on a circle of radius $1$, together with the centre, are also an example.
>
> The classification is asked for all sufficiently large $n$. Small exceptions such as
> $\{(0,0), (1,0), (0,1), (0,-1)\}$ exist, so the negative answer asserts
> counterexamples of arbitrarily large size, as in [CDL25].

```lean
theorem erdos_958 :
    ¬ ∃ N : ℕ, ∀ n ≥ N, ∀ A : Finset ℝ², #A = n →
      ((#(distanceSet A) = n - 1 ∧
            (distanceSet A).image (distanceMultiplicity A) = Finset.Icc 1 (n - 1)) →
        (IsEquidistantOnLine A ∨ IsEquidistantOnCircle A))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/958.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/958.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/958.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/958.lean)
- [erdosproblems.com/958](https://www.erdosproblems.com/958)
