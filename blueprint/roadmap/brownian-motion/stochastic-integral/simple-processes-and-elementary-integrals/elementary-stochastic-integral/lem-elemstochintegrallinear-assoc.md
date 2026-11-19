---
declaration: lemma
origin: cited
lean: ProbabilityTheory.SimpleProcess.integralEval_assoc
statement: formalized
proof: formalized
---

# elemStochIntegralLinear_assoc

For simple process $W$ with values in $L(E, F)$, simple process $V$ with values in $L(F, G)$, and stochastic process $X$ with values in $E$, we have

$$
\begin{aligned}
V \bullet_L (W \bullet_L X)
&= (V \circ W) \bullet_L X
\: ,
\end{aligned}
$$

in which $V \circ W$ is the simple process defined by $(V \circ W)_t = V_t \circ W_t$.

## Depends on

- [elemStochIntegralLinear](def-elemstochintegrallinear.md)

## Proof depends on

- [elemStochIntegralBilin_assoc](lem-elemstochintegralbilin-assoc.md)

## Proof

Use Lemma [elemStochIntegralBilin_assoc](lem-elemstochintegralbilin-assoc.md) with $B_1, B_2, B_4$ equal to the evaluation maps and $B_3$ the composition of continuous linear maps.

## Lean

Formalized as [`ProbabilityTheory.SimpleProcess.integralEval_assoc`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.SimpleProcess.integralEval_assoc).

## Sources

- [Brownian motion blueprint: chapters/elementary.tex, line 520](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/elementary.tex#L520)
