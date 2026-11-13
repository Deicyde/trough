---
declaration: theorem
origin: cited
lean: Erdos190.erdos_190, Erdos190.erdos_190.variants.H
statement: formalized
---

# Erdős Problem 190

> *References:*
> - [erdosproblems.com/190](https://www.erdosproblems.com/190)
> - [ErGr79] P. Erdős and R. L. Graham, *Old and new problems and results in combinatorial
>   number theory: van der Waerden's theorem and related topics*, Enseign. Math. (2) 25 (1979),
>   325–344 (p. 333).
> - [ErGr80] P. Erdős and R. L. Graham, *Old and New Problems and Results in Combinatorial
>   Number Theory*, Monogr. Enseign. Math. 28 (1980), p. 17.
> - [Ba26] J. H. Bae, *A resolution of Erdős Problem #190 via Erdős–Lovász, BCT, and
>   Baker–Harman–Pintz*, arXiv:2604.20588 (22 April 2026).
> - [FoHu26] J. Fox and Z. Hunter, *Three-color van der Waerden numbers grow
>   super-exponentially*, arXiv:2606.02541 (1 June 2026).

*Quoted from [FormalConjectures/ErdosProblems/190.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/190.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/190](https://www.erdosproblems.com/190).

The file states 2 research or textbook statements: 2 solved. It also has 3 test statements, counted here but not shown.

## `Erdos190.erdos_190`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-09-15-000003](https://palomar-registry.org/entry.html?id=PALOMAR-2026-09-15-000003).

> Let $H(k)$ be the smallest $N$ such that in any finite colouring of $\{1,\ldots,N\}$ (into
> any number of colours) there is always either a monochromatic $k$-term arithmetic progression
> or a rainbow arithmetic progression (i.e. all elements are different colours). Estimate
> $H(k)$. Is it true that $H(k)^{1/k}/k\to\infty$ as $k\to\infty$?
>
> The question was answered affirmatively in [Ba26] (22 April 2026), which gave the first
> publicly available proof, with $H(k)\geq k^{(2-o(1))k}$.  The subsequent work [FoHu26]
> (1 June 2026) describes [Ba26] as independent work that also resolves the problem, and
> obtains $H(k)\geq k^{(1-o(1))k\log k}$.
>
> The statement is formalised without assuming the existence of $H(k)$: for every $C$, every
> canonical $N$ exceeds $(Ck)^k$ for all large $k$. Given the existence of $H(k)$ this is
> equivalent to $H(k)^{1/k}/k\to\infty$ (see `erdos_190.variants.H`).
>
> The formal proof (Lean 4 / Mathlib v4.33.0, following [Ba26]) is registered in
> the Palomar registry as PALOMAR-2026-09-15-000003.  A bridge deriving this exact statement
> (with the definitions above) from the registered proof is available at
> [jbaelaw/erdos190-fc-bridge](https://github.com/jbaelaw/erdos190-fc-bridge).

```lean
theorem erdos_190 :
    ∀ C : ℕ, ∀ᶠ k in atTop, ∀ N, IsCanonical N k → (C * k) ^ k < N
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/190.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/190.lean#L113).

## `Erdos190.erdos_190.variants.H`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-09-15-000003](https://palomar-registry.org/entry.html?id=PALOMAR-2026-09-15-000003).

> The same statement in terms of $H(k)$, assuming that a canonical `N` exists for every `k`
> (the Erdős–Graham theorem, via Szemerédi's theorem).

```lean
theorem erdos_190.variants.H :
    (∀ k, {N | IsCanonical N k}.Nonempty) →
      ∀ C : ℕ, ∀ᶠ k in atTop, (C * k) ^ k < H k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/190.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/190.lean#L121).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/190.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/190.lean)
- [erdosproblems.com/190](https://www.erdosproblems.com/190)
