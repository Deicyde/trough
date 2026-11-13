---
declaration: theorem
origin: cited
lean: Erdos232.erdos_232, Erdos232.erdos_232.variants.acmvz_set, Erdos232.erdos_232.variants.acmvz, Erdos232.erdos_232.variants.hexagonal_lower_bound, Erdos232.erdos_232.variants.croft_lower_bound
statement: formalized
---

# Erdős Problem 232

> *References:*
> - [erdosproblems.com/232](https://www.erdosproblems.com/232)
> - [ACMVZ23] Ambrus, Gergely and Csiszárik, Adrián and Matolcsi, Máté and Varga, Dániel and
>   Zsámboki, Pál, *The density of planar sets avoiding unit distances*. Math. Program. (2023),
>   [arXiv:2207.14179](https://arxiv.org/abs/2207.14179).
> - [Cr67] Croft, H. T., *Incidence incidents*. Eureka (1967), 22-26.
> - [Er85] Erdős, Paul, *Problems and results in combinatorial geometry*. Discrete geometry and
>   convexity (New York, 1982), Ann. New York Acad. Sci. 440 (1985), 1-11.
>   [PDF](https://www.renyi.hu/~p_erdos/1985-23.pdf)
> - [Mo66] Moser, L., *Poorly formulated unsolved problems of combinatorial geometry*.
>   Mimeographed (1966).

*Quoted from [FormalConjectures/ErdosProblems/232.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/232.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/232](https://www.erdosproblems.com/232).

The file states 5 research or textbook statements: 5 solved.

## `Erdos232.erdos_232`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos232.lean#L125](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos232.lean#L125).

> For $A\subset \mathbb{R}^2$ we define the upper density as
>
> $$\overline{\delta}(A)=\limsup_{R\to \infty}\frac{\lambda(A \cap B_R)}{\lambda(B_R)},$$
>
> where $\lambda$ is the Lebesgue measure and $B_R$ is the ball of radius $R$.
>
> Estimate
>
> $$m_1=\sup \overline{\delta}(A),$$
>
> where $A$ ranges over all measurable subsets of $\mathbb{R}^2$ without two points distance $1$
> apart. In particular, is $m_1\leq 1/4$?
>
> A question of Moser [Mo66]; Erdős [Er85] conjectured $m_1<1/4$. The answer is yes: Ambrus,
> Csiszárik, Matolcsi, Varga, and Zsámboki [ACMVZ23] proved that $m_1\leq 0.247$.

```lean
theorem erdos_232 : m₁ ≤ 1 / 4
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/232.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/232.lean#L79).

## `Erdos232.erdos_232.variants.acmvz_set`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos232.lean#L90](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos232.lean#L90).

> Ambrus, Csiszárik, Matolcsi, Varga, and Zsámboki [ACMVZ23, Theorem 1]: any Lebesgue measurable,
> $1$-avoiding planar set has upper density at most $0.2470$.

```lean
theorem erdos_232.variants.acmvz_set (A : Set ℝ²) (hA : NullMeasurableSet A volume)
    (hfree : Erdos214.UnitDistanceAvoiding A) : upperDensity A ≤ 247 / 1000
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/232.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/232.lean#L89).

## `Erdos232.erdos_232.variants.acmvz`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos232.lean#L115](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos232.lean#L115).

> Ambrus, Csiszárik, Matolcsi, Varga, and Zsámboki [ACMVZ23] proved that $m_1\leq 0.247$.

```lean
theorem erdos_232.variants.acmvz : m₁ ≤ 247 / 1000
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/232.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/232.lean#L99).

## `Erdos232.erdos_232.variants.hexagonal_lower_bound`

Solved: stated here without proof.

> A lower bound of $m_1\geq \pi/(8\sqrt{3})\approx 0.2267$ is given by taking the union of open
> circular discs of radius $1/2$ at a regular hexagonal lattice suitably spaced apart
> (see [ACMVZ23, Section 1]).

```lean
theorem erdos_232.variants.hexagonal_lower_bound :
    Real.pi / (8 * Real.sqrt 3) ≤ m₁
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/232.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/232.lean#L108).

## `Erdos232.erdos_232.variants.croft_lower_bound`

Solved: stated here without proof.

> Croft [Cr67] gives a small improvement of $m_1\geq 0.22936$ (see [ACMVZ23, Section 1]).

```lean
theorem erdos_232.variants.croft_lower_bound : 0.22936 ≤ m₁
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/232.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/232.lean#L116).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/232.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/232.lean)
- [erdosproblems.com/232](https://www.erdosproblems.com/232)
