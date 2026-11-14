---
declaration: theorem
origin: cited
lean: ProbabilityTheory.toReal_statInfo_eq_integral_max_of_le, ProbabilityTheory.toReal_statInfo_eq_integral_max_of_ge
statement: formalized
proof: formalized
---

# Integral form of the statistical information

For finite measures $\mu, \nu$ and $\xi \in \mathcal M(\{0,1\})$,

$$
\begin{aligned}
\mathcal I_\xi(\mu, \nu)
&= \nu\left[ x \mapsto \max \left\{0 , \xi_0\frac{d \mu}{d\nu}(x) - \xi_1 \right\} \right] + \xi_0 \mu_{\perp \nu}(\mathcal X) & \text{ if } \xi_0 \mu(\mathcal X) \le \xi_1 \nu(\mathcal X)
\: , \\
\mathcal I_\xi(\mu, \nu)
&= \nu\left[ x \mapsto \max \left\{0 , \xi_1 - \xi_0\frac{d \mu}{d\nu}(x) \right\} \right] & \text{ if } \xi_0 \mu(\mathcal X) \ge \xi_1 \nu(\mathcal X)
\: .
\end{aligned}
$$

## Depends on

- [statInfo](def-statinfo.md)

## Proof depends on

- [bayesBinaryRisk_eq](../../../testing-estimation-risk/simple-binary-hypothesis-testing/thm-bayesbinaryrisk-eq.md)

## Proof

By Theorem [bayesBinaryRisk_eq](../../../testing-estimation-risk/simple-binary-hypothesis-testing/thm-bayesbinaryrisk-eq.md),

$$
\begin{aligned}
\mathcal I_\xi(\mu, \nu)
&= \min\{\xi_0\mu(\mathcal X), \xi_1\nu(\mathcal X)\} - (P \circ \xi)\left[x \mapsto \min \left\{\xi_0\frac{d \mu}{d(P \circ \xi)}(x), \xi_1\frac{d \nu}{d(P \circ \xi)}(x)\right\}\right]
\: .
\end{aligned}
$$

Suppose that $\xi_0\mu(\mathcal X) \le \xi_1\nu(\mathcal X)$ . Then

$$
\begin{aligned}
\mathcal I_\xi(\mu, \nu)
&= \xi_0\mu(\mathcal X) - (P \circ \xi)\left[x \mapsto \xi_0\frac{d \mu}{d(P \circ \xi)}(x) + \min \left\{0 , \xi_1\frac{d \nu}{d(P \circ \xi)}(x) - \xi_0\frac{d \mu}{d(P \circ \xi)}(x)\right\}\right]
\\
&= - (P \circ \xi)\left[x \mapsto \min \left\{0 , \xi_1\frac{d \nu}{d(P \circ \xi)}(x) - \xi_0\frac{d \mu}{d(P \circ \xi)}(x) \right\}\right]
\\
&= (P \circ \xi)\left[x \mapsto \max \left\{0 , \xi_0\frac{d \mu}{d(P \circ \xi)}(x) - \xi_1\frac{d \nu}{d(P \circ \xi)}(x) \right\}\right]
\\
&= \nu\left[ x \mapsto \max \left\{0 , \xi_0\frac{d \mu}{d\nu}(x) - \xi_1 \right\} \right] + \xi_0 \mu_{\perp \nu}(\mathcal X)
\: .
\end{aligned}
$$

If on the other hand $\xi_0\mu(\mathcal X) \ge \xi_1\nu(\mathcal X)$ , with similar computations,

$$
\begin{aligned}
\mathcal I_\xi(\mu, \nu)
&= (P \circ \xi)\left[x \mapsto \max \left\{0 , \xi_1\frac{d \nu}{d(P \circ \xi)}(x) - \xi_0\frac{d \mu}{d(P \circ \xi)}(x) \right\}\right]
\\
&= \nu\left[ x \mapsto \max \left\{0 , \xi_1 - \xi_0\frac{d \mu}{d\nu}(x) \right\} \right]
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.toReal_statInfo_eq_integral_max_of_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.toReal_statInfo_eq_integral_max_of_le), [`ProbabilityTheory.toReal_statInfo_eq_integral_max_of_ge`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.toReal_statInfo_eq_integral_max_of_ge).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/stat_div.tex, line 157](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L157)
