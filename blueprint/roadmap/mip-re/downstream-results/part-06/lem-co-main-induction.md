---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Co.MainInductionStep.mainInduction
statement: formalized
proof: formalized
---

# The main induction, in a symmetric model

Consider an $(\varepsilon, \delta, \gamma)$-good symmetric strategy in $S$ for the low individual degree test in $m$ variables, as in Lemma [Commutativity of points, in a symmetric model](../part-05/lem-co-commutativity-points.md), with point measurements $A^u$ in $\mathcal{P}$. Let the bipartite reading of $S$ be a finite pair (Definition [Finite pairs](../part-04/def-finite-pair.md)) whose first player's operators contain no nonzero abelian projection, and let $d \geq 1$. Then for every integer $k \geq 400\, m d$ there is a measurement $G$ in $\mathcal{P}$ whose outcomes are the polynomials of individual degree at most $d$ with

$$
\mathop{\mathbb{E}}_u \mathrm{cons}\bigl(A^u, G^{[u]}\bigr) \leq m^2 \bigl(\nu + e^{-k / (80000 m^2)}\bigr),
\qquad \nu = 1000\, k^2 m^2 \Bigl(\varepsilon^{1/1024} + \delta^{1/1024} + \gamma^{1/1024} +
\Bigl(\frac{d}{q}\Bigr)^{1/1024}\Bigr),
$$

for a uniformly random point $u$.

## Depends on

- [Symmetric models](../part-05/def-sym-model.md)
- [Finite pairs](../part-04/def-finite-pair.md)
- [Self-improvement, in a symmetric model](lem-co-self-improvement.md)
- [Pasting, in a symmetric model](lem-co-ld-pasting.md)

## Proof

The proof is the vendored one, `MIPStarRE.LDT.MainInductionStep.mainInduction` in `MIPRE/Background/LIDT/MIPStarRE/LDT/MainInductionStep/Theorems/`, rewritten over the symmetric model (`planning/c6b-plan.md`, milestone M12): a strong induction on $m$, run on an answer-valued form of the statement that quantifies over every symmetric model whose bipartite reading is a finite pair without abelian projections. For $m = 1$ the axis-parallel line measurement read at the point is the measurement. For $m + 1$ variables the strategy restricted to each slice $x_{m+1} = x$ is good at parameters bounded by the restricted failure probabilities, whose averages are those of the whole strategy; the induction hypothesis gives each slice a polynomial measurement, which self-improvement (Lemma [Self-improvement, in a symmetric model](lem-co-self-improvement.md)) makes projective, complete, self-close and bounded, and pasting (Lemma [Pasting, in a symmetric model](lem-co-ld-pasting.md)) assembles the slices into one measurement in $m + 1$ variables; the vendored parameter bounds absorb the errors into the one of the statement. The restrictions keep the model, so the hypotheses on it, and $d$, pass to each slice unchanged. When the error is at least $1$, any measurement will do.

## Lean

Formalized as [`MIPRE.LIDT.Co.MainInductionStep.mainInduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.MainInductionStep.mainInduction).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 4106](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L4106)
