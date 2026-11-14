---
declaration: lemma
origin: cited
lean: ProbabilityTheory.isArgminEstimator_binaryGenBayesEstimator
statement: formalized
proof: formalized
---

# genBayesEstimator_bayesBinaryRisk

The generalized Bayes estimator for the Bayes binary risk with prior $\xi \in \mathcal M(\{0,1\})$ is $x \mapsto \text{if } \xi_1\frac{d \nu}{d(P \circ \xi)}(x) \le \xi_0\frac{d \mu}{d(P \circ \xi)}(x) \text{ then } 0 \text{ else } 1$, i.e. it is equal to $\mathbb{I}_E$ for $E = \{x \mid \xi_1\frac{d \nu}{d(P \circ \xi)}(x) > \xi_0\frac{d \mu}{d(P \circ \xi)}(x)\}$ .

## Depends on

- [Generalized Bayes estimator](../risk/def-genbayesestimator.md)
- [bayesBinaryRisk](def-bayesbinaryrisk.md)

## Proof depends on

- [bayesInv_binary](lem-bayesinv-binary.md)

## Proof

The generalized Bayes estimator is defined by

$$
\begin{aligned}
x \mapsto \arg\min_z P_\xi^\dagger(x)\left[\theta \mapsto \ell'(y(\theta), z)\right] \: .
\end{aligned}
$$

For the simple binary hypothesis testing problem,

$$
\begin{aligned}
P_\xi^\dagger(x)\left[\theta \mapsto \ell'(y(\theta), z)\right]
&= P_\xi^\dagger(x)(\theta \ne z)
\: .
\end{aligned}
$$

For $z = 0$, this is $P_\xi^\dagger(x)(\{1\})$ and for $z = 1$, this is $P_\xi^\dagger(x)(\{0\})$. The generalized Bayes estimator is $x \mapsto \text{if } P_\xi^\dagger(x)(\{1\}) \le P_\xi^\dagger(x)(\{0\}) \text{ then } 0 \text{ else } 1$.

The expression of the lemma statement is obtained by replacing $P_\xi^\dagger$ by its value (Lemma [bayesInv_binary](lem-bayesinv-binary.md)).

## Lean

Formalized as [`ProbabilityTheory.isArgminEstimator_binaryGenBayesEstimator`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.isArgminEstimator_binaryGenBayesEstimator).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 698](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L698)
