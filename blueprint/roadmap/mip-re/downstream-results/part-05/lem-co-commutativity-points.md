---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Co.CommutativityPoints.commutativityPoints, MIPRE.LIDT.Co.CommutativityPoints.answerCommutativityPoints
statement: formalized
proof: formalized
---

# Commutativity of points, in a symmetric model

Let $S$ be a symmetric model over $\mathcal{P}$ (Definition [Symmetric models](def-sym-model.md)), with state $\Psi$ and first placement $L$, and consider a symmetric strategy in $S$ for the low individual degree test of Theorem [Quantum soundness of the seeded CL test](../../background-results/part-01/thm-lidt-cl-soundness.md), with parameters $q$, $m$ and $d$: projective measurements $A^u$ in $\mathcal{P}$ for the points $u \in \mathbb{F}_q^m$, and axis-parallel and diagonal-line measurements in $\mathcal{P}$, the diagonal-line measurement answering a polynomial of degree at most $d$ on the line or, in the answer-valued variant, an arbitrary function on the line. If the strategy is $(\varepsilon, \delta, \gamma)$-good — the axis-parallel, self-consistency and diagonal-line tests fail with probability at most $\varepsilon$, $\delta$ and $\gamma$ — then

$$
\mathop{\mathbb{E}}_{u, v} \sum_{a, b} \bigl\| L\bigl(A^u_a A^v_b - A^v_b A^u_a\bigr) \Psi \bigr\|^2 \leq 32\,
\gamma\, m,
$$

for independent uniformly random points $u$ and $v$.

## Depends on

- [Symmetric models](def-sym-model.md)

## Proof depends on

- [Bipartite model](../part-02/def-bipartite-model.md)

## Proof

The proof is the vendored one, `MIPStarRE.LDT.CommutativityPoints.commutativityPoints` in `MIPRE/Background/LIDT/MIPStarRE/LDT/CommutativityPoints/`, rewritten over the symmetric model declaration by declaration (`planning/c6b-plan.md`, milestone M1 and “Port conventions”). A uniformly random pair of points has the law of two points sampled on a random diagonal line, so it suffices to compare the two orders of the product for points $u$ and $v$ on a shared diagonal line $\ell$. By the diagonal-line test, the point measurement $A^u$ placed by $L$ is within $2 \gamma m$, in averaged squared state-dependent distance, of the line measurement of $\ell$ evaluated at $u$ and placed by $R$. Multiplying such an approximation by a family $C$ with $\sum_c C_c^* C_c \leq 1$ keeps its error, so four replacements carry $L(A^u_a A^v_b)$ to the product of the line measurement's two evaluations, placed by $R$, and from there to $L(A^v_b A^u_a)$; the two evaluations commute, being post-processings of one projective measurement. The triangle inequality for the squared distance loses a factor $2$, which gives $2 (2 \gamma m + 2 \gamma m) = 8 \gamma m$ for each half and $2 (8 \gamma m + 8 \gamma m) = 32 \gamma m$ in all. The Cauchy–Schwarz inequalities behind these steps are those of the vector state read as a state model (Definition [Bipartite model](../part-02/def-bipartite-model.md)). The flip of the model is never used. The answer-valued variant has the same proof; it is ported as a separate statement, as the vendored development states it and its consumers use it.

## Lean

Formalized as [`MIPRE.LIDT.Co.CommutativityPoints.commutativityPoints`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.CommutativityPoints.commutativityPoints), [`MIPRE.LIDT.Co.CommutativityPoints.answerCommutativityPoints`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.CommutativityPoints.answerCommutativityPoints).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3287](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3287)
