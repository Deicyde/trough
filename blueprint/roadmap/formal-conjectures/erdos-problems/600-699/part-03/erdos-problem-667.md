---
declaration: theorem
origin: cited
lean: Erdos667.erdos_667, Erdos667.erdos_667.variants.monotoneOn, Erdos667.erdos_667.variants.endpoint, Erdos667.erdos_667.variants.ramsey_bounds
statement: formalized
---

# Erdős Problem 667

> A problem of Erdős, Faudree, Rousseau, and Schelp on the growth exponent of the largest clique
> that is guaranteed inside a locally dense graph.
>
> *References:*
> * [erdosproblems.com/667](https://www.erdosproblems.com/667)
> * [Er97f] P. Erdős, _Some unsolved problems_. In: Combinatorics, Geometry and Probability
>   (Cambridge, 1993), Cambridge Univ. Press (1997), 1-10.
> * [EFRS94] P. Erdős, R. J. Faudree, C. C. Rousseau and R. H. Schelp,
>   _A local density condition for triangles_. Discrete Math. 127 (1994), 153-161.

*Quoted from [FormalConjectures/ErdosProblems/667.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/667.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/667](https://www.erdosproblems.com/667).

The file states 4 research or textbook statements: 1 open, 2 solved and 1 textbook result.

## `Erdos667.erdos_667`

Open: stated without proof.

> Let $p, q \geq 1$ be fixed integers. Define $H(n) = H(n; p, q)$ to be the largest $m$ such that any
> graph on $n$ vertices where every set of $p$ vertices spans at least $q$ edges must contain a
> complete graph on $m$ vertices. Is
>
> $$ c(p, q) = \liminf_{n \to \infty} \frac{\log H(n)}{\log n} $$
>
> a strictly increasing function of $q$ for $1 \leq q \leq \binom{p-1}{2} + 1$?
>
> A problem of Erdős, Faudree, Rousseau, and Schelp. When $q = 1$ this corresponds exactly to the
> classical Ramsey problem, and hence $\tfrac{1}{p-1} \leq c(p, 1) \leq \tfrac{2}{p+1}$ for
> $p \geq 3$. It is easy to see that if $q = \binom{p-1}{2} + 1$ then $c(p, q) = 1$.
>
> erdosproblems.com/667 also states that Erdős, Faudree, Rousseau and Schelp showed
> $c(p, \binom{p-1}{2}) \leq 1/2$. This cannot hold for all $p$: for $p = 6$, $q = 10$, the
> complement of a $(6, 10)$-locally dense graph is $C_6$-free, so Bondy–Simonovits together with
> $\alpha(F) \geq n^2 / (2e(F) + n)$ gives $c(6, 10) \geq 2/3$. That remark is therefore not
> formalised here.

```lean
theorem erdos_667 :
    ∀ p : ℕ, StrictMonoOn (c p) (Set.Icc 1 (Nat.choose (p - 1) 2 + 1))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/667.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/667.lean#L78).

## `Erdos667.erdos_667.variants.monotoneOn`

Textbook result, stated without proof. A Lean proof is at [https://github.com/linrock/math-proofs/blob/d16a9d73d85f1377e83798f5d9585ee4c4140979/erdos-667/Solution.lean#L41](https://github.com/linrock/math-proofs/blob/d16a9d73d85f1377e83798f5d9585ee4c4140979/erdos-667/Solution.lean#L41).

> That $c(p, q)$ is *nondecreasing* in $q$ for fixed $p$ is a straightforward consequence of the
> definitions: enlarging $q$ shrinks the family of $(p, q)$-locally dense graphs, which can only
> increase the guaranteed clique size $H(n)$, and hence the exponent.

```lean
theorem erdos_667.variants.monotoneOn (p : ℕ) :
    MonotoneOn (c p) (Set.Icc 1 (Nat.choose (p - 1) 2 + 1))
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/667.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/667.lean#L89).

## `Erdos667.erdos_667.variants.endpoint`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/d16a9d73d85f1377e83798f5d9585ee4c4140979/erdos-667/Solution.lean#L45](https://github.com/linrock/math-proofs/blob/d16a9d73d85f1377e83798f5d9585ee4c4140979/erdos-667/Solution.lean#L45).

> The right endpoint: when $q = \binom{p-1}{2} + 1$ one has $c(p, q) = 1$
> (stated as "easy to see" on erdosproblems.com/667).

```lean
theorem erdos_667.variants.endpoint (p : ℕ) (hp : 2 ≤ p) :
    c p (Nat.choose (p - 1) 2 + 1) = 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/667.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/667.lean#L100).

## `Erdos667.erdos_667.variants.ramsey_bounds`

Solved: stated here without proof.

> The case $q = 1$ is the classical Ramsey problem, giving the bounds
> $\tfrac{1}{p-1} \leq c(p, 1) \leq \tfrac{2}{p+1}$ for $p \geq 3$. (For $p = 2$ the condition
> forces $G$ to be complete, so $c(2, 1) = 1$ and the upper bound fails.)

```lean
theorem erdos_667.variants.ramsey_bounds (p : ℕ) (hp : 3 ≤ p) :
    1 / ((p : ℝ) - 1) ≤ c p 1 ∧ c p 1 ≤ 2 / ((p : ℝ) + 1)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/667.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/667.lean#L110).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/667.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/667.lean)
- [erdosproblems.com/667](https://www.erdosproblems.com/667)
