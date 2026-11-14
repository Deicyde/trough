---
declaration: lemma
origin: cited
lean: ProbabilityTheory.bayesBinaryRisk_le_min
statement: formalized
proof: formalized
---

# bayesBinaryRisk_le

For all measures $\mu, \nu$, $\mathcal B_\xi(\mu, \nu) \le \min\{\xi_0 \mu(\mathcal X), \xi_1 \nu(\mathcal X)\}$ .

## Depends on

- [bayesBinaryRisk](def-bayesbinaryrisk.md)

## Proof depends on

- [Data-processing inequality](thm-data-proc-bayesbinaryrisk.md)
- [bayesBinaryRisk_self](lem-bayesbinaryrisk-self.md)
- [bayesBinaryRisk_mul](lem-bayesbinaryrisk-mul.md)

## Proof

Let $d_{\mathcal X} : \mathcal X \rightsquigarrow *$ be the discard kernel and $\delta_*$ be the only probability measure over $*$, that is a Dirac delta. Then applying the DPI (Theorem [Data-processing inequality](thm-data-proc-bayesbinaryrisk.md)), followed by Lemma [bayesBinaryRisk_mul](lem-bayesbinaryrisk-mul.md) and Lemma [bayesBinaryRisk_self](lem-bayesbinaryrisk-self.md), we obtain:

$$
\begin{aligned}
\mathcal B_\xi(\mu, \nu)
&\le \mathcal B_\xi(d_{\mathcal X} \circ \mu, d_{\mathcal X} \circ \nu)
\\
&= \mathcal B_\xi(\mu(\mathcal X) \delta_*, \nu(\mathcal X) \delta_*)
\\
&= \mathcal B_{(\mu(\mathcal X) \xi_0, \nu(\mathcal X) \xi_1)}(\delta_*, \delta_*)
\\
&= \min\{\mu(\mathcal X) \xi_0, \nu(\mathcal X) \xi_1\} \delta_*(\mathcal X)
\\
&= \min\{\mu(\mathcal X) \xi_0, \nu(\mathcal X) \xi_1\}
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.bayesBinaryRisk_le_min`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.bayesBinaryRisk_le_min).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 655](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L655)
