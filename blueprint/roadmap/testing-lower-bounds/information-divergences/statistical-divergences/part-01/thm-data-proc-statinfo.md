---
declaration: theorem
origin: cited
lean: ProbabilityTheory.statInfo_comp_le
statement: formalized
proof: formalized
---

# Data-processing inequality

For $\mu, \nu \in \mathcal M(\mathcal X)$, $\xi \in \mathcal M(\{0,1\})$ and $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ a Markov kernel, $\mathcal I_\xi(\kappa \circ \mu, \kappa \circ \nu) \le \mathcal I_\xi(\mu, \nu)$ .

## Depends on

- [statInfo](def-statinfo.md)

## Proof depends on

- [Data-processing inequality](../../../testing-estimation-risk/simple-binary-hypothesis-testing/thm-data-proc-bayesbinaryrisk.md)
- [Data-processing inequality](../../../testing-estimation-risk/risk/lem-riskincrease-comp-del.md)

## Proof

Since $\kappa$ is a Markov kernel,

$$
\begin{aligned}
\mathcal I_\xi(\kappa \circ \mu, \kappa \circ \nu)
&= \min\{\xi_0(\kappa \circ \mu)(\mathcal X), \xi_1(\kappa \circ \nu)(\mathcal X)\} - \mathcal B_\xi(\kappa \circ \mu, \kappa \circ \nu)
\\
&= \min\{\xi_0 \mu(\mathcal X), \xi_1 \nu(\mathcal X)\} - \mathcal B_\xi(\kappa \circ \mu, \kappa \circ \nu)
\end{aligned}
$$

It suffices to prove $\mathcal B_\xi(\kappa \circ \mu, \kappa \circ \nu) \ge \mathcal B_\xi(\mu, \nu)$ since $\mathcal I_\xi(\mu, \nu) = \min\{\xi_0\mu(\mathcal X), \xi_1\nu(\mathcal X)\} - \mathcal B_\xi(\mu, \nu)$. The inequality was proved in Theorem [Data-processing inequality](../../../testing-estimation-risk/simple-binary-hypothesis-testing/thm-data-proc-bayesbinaryrisk.md).

Alternatively, we can use Lemma [Data-processing inequality](../../../testing-estimation-risk/risk/lem-riskincrease-comp-del.md).

## Lean

Formalized as [`ProbabilityTheory.statInfo_comp_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.statInfo_comp_le).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/stat_div.tex, line 76](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L76)
