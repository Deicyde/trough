---
declaration: theorem
origin: cited
lean: Arxiv.«2607.05349».concentration_unique, Arxiv.«2607.05349».microscopic_weighting_iff_finite_concentration, Arxiv.«2607.05349».hasFiniteConcentration_of_hasMicroscopicWeighting, Arxiv.«2607.05349».hasMicroscopicWeighting_iff_of_isUnit
statement: formalized
---

# The microscopic weighting on a metric space

> *Reference:* [arxiv/2607.05349](https://arxiv.org/abs/2607.05349)
> **The microscopic weighting on a metric space**
> by *Emily Roff, Simon Willerton*

*Quoted from [FormalConjectures/Arxiv/2607.05349/MicroscopicWeighting.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.05349/MicroscopicWeighting.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 3 solved and 1 textbook result.

## `Arxiv.«2607.05349».concentration_unique`

Textbook result, proved here.

> All gaugings of a symmetric matrix share one concentration, so $\mathrm{con}$ is an
> attribute of the matrix. The source records this after Definition 2.3, as the calculation
> $c = c\mathbf{1}^T v' = (v^TA^T)v' = v^T(c'\mathbf{1}) = c'$, and Definition 2.4 rests on it.

```lean
theorem concentration_unique {M : Matrix X X ℝ} (hM : M.IsSymm) {g g' : X → ℝ} {c c' : ℝ}
    (h : IsGauging M g c) (h' : IsGauging M g' c') : c = c'
```

Category `textbook`; AMS [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/2607.05349/MicroscopicWeighting.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.05349/MicroscopicWeighting.lean#L70).

## `Arxiv.«2607.05349».microscopic_weighting_iff_finite_concentration`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/microscopic-weighting-counterexample/blob/eff8979/lean/MicroscopicWeightingCounterexampleFC.lean#L886-L894](https://github.com/KitaKen1/microscopic-weighting-counterexample/blob/eff8979/lean/MicroscopicWeightingCounterexampleFC.lean#L886-L894).

> **Conjecture 3.3 (Roff-Willerton, 2026).** A finite metric space admits a microscopic weighting
> if and only if its distance matrix has finite concentration.
>
> `Nonempty` is needed and not just tidiness. On the empty space every gauging condition fails,
> since `∑ i, g i` is `0` rather than `1`, while `X → ℝ` is a subsingleton so the weighting
> converges trivially. The equivalence would be false there for reasons that have nothing to do
> with the question.
>
> The answer is false as proved by Kenta Kitamura assisted by ChatGPT 5.6 sol.
>
> The proof proceeds by constructing an explicit counterexample: a finite metric space
> on 10 points that has finite concentration but does not admit a microscopic weighting.
> The metric space is defined by the following $10 \times 10$ distance matrix $A$:
> $$
> \begin{pmatrix}
> 0 & 116 & 236 & 231 & 260 & 124 & 64 & 290 & 266 & 64 \cr
> 116 & 0 & 312 & 268 & 296 & 112 & 64 & 280 & 296 & 64 \cr
> 236 & 312 & 0 & 68 & 40 & 236 & 288 & 68 & 36 & 288 \cr
> 231 & 268 & 68 & 0 & 34 & 237 & 288 & 72 & 40 & 288 \cr
> 260 & 296 & 40 & 34 & 0 & 264 & 320 & 40 & 68 & 320 \cr
> 124 & 112 & 236 & 237 & 264 & 0 & 64 & 280 & 264 & 64 \cr
> 64 & 64 & 288 & 288 & 320 & 64 & 0 & 312 & 320 & 120 \cr
> 290 & 280 & 68 & 72 & 40 & 280 & 312 & 0 & 40 & 312 \cr
> 266 & 296 & 36 & 40 & 68 & 264 & 320 & 40 & 0 & 320 \cr
> 64 & 64 & 288 & 288 & 320 & 64 & 120 & 312 & 320 & 0
> \end{pmatrix}
> $$
>
> The space has finite concentration, demonstrated by the explicit gauging $g$:
> $$
> g = \frac{1}{24842973905} \begin{pmatrix} 3672468740 \cr 6389133731 \cr 9124217512 \cr
> 5612262448 \cr -6875621136 \cr 2754831248 \cr 0 \cr 10758780188 \cr -6593098826 \cr 0
> \end{pmatrix}
> $$
> which gives $A g = \frac{4111107017312}{24842973905} \mathbf{1}$.
>
> To prove that it does not admit a microscopic weighting, we provide a vector $v \in \ker A$:
> $$
> v = \begin{pmatrix} -2 \cr -1 \cr 3 \cr 4 \cr -4 \cr -2 \cr 2 \cr 2 \cr -4 \cr 2 \end{pmatrix}
> $$
> along with a row-space certificate $q$ for the entrywise square matrix $B = A^{\circ 2}$ satisfying $q A = v^\top B$:
> $$
> q^\top = \frac{1}{128472094291} \begin{pmatrix} 43681853675722 \cr -53873248293642 \cr
> -66890627544007 \cr -81187181670120 \cr 24308499983196 \cr 40819375894674 \cr 0 \cr
> 54690260644468 \cr 35226831040652 \cr 0
> \end{pmatrix}
> $$
> This certificate shows that the obstruction $v^\top B$ annihilates $\ker A$, making it impossible to construct a convergent weighting.

```lean
theorem microscopic_weighting_iff_finite_concentration :
    ¬ ∀ (X : Type) [Fintype X] [DecidableEq X] [Nonempty X] [MetricSpace X],
      HasMicroscopicWeighting X ↔ HasFiniteConcentration (distanceMatrix X)
```

Category `research solved`; AMS [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Arxiv/2607.05349/MicroscopicWeighting.lean, line 146](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.05349/MicroscopicWeighting.lean#L146).

## `Arxiv.«2607.05349».hasFiniteConcentration_of_hasMicroscopicWeighting`

Solved: stated here without proof.

> One direction is known: a microscopic weighting implies finite concentration (Theorem 3.1(3)).
> Together with the conjecture above this leaves the converse, that finite concentration is enough.

```lean
theorem hasFiniteConcentration_of_hasMicroscopicWeighting
    (h : HasMicroscopicWeighting X) : HasFiniteConcentration (distanceMatrix X)
```

Category `research solved`; AMS [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Arxiv/2607.05349/MicroscopicWeighting.lean, line 156](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.05349/MicroscopicWeighting.lean#L156).

## `Arxiv.«2607.05349».hasMicroscopicWeighting_iff_of_isUnit`

Solved: stated here without proof.

> Theorem 3.8: the conjecture is known when the distance matrix is invertible, and the microscopic
> weighting is then the unique gauging.

```lean
theorem hasMicroscopicWeighting_iff_of_isUnit (h : IsUnit (distanceMatrix X).det) :
    HasMicroscopicWeighting X ↔ HasFiniteConcentration (distanceMatrix X)
```

Category `research solved`; AMS [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Arxiv/2607.05349/MicroscopicWeighting.lean, line 165](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.05349/MicroscopicWeighting.lean#L165).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2607.05349/MicroscopicWeighting.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.05349/MicroscopicWeighting.lean)
- [arxiv/2607.05349](https://arxiv.org/abs/2607.05349)
