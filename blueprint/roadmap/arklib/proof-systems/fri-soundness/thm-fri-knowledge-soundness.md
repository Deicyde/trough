---
declaration: theorem
origin: cited
lean: Fri.Spec.knowledge_soundness_with, Fri.Spec.knowledge_soundness
statement: formalized
proof: formalized
---

# fri-knowledge-soundness

Suppose $M\leq N$, $\delta\geq0$, and $\min\{\theta,\delta\}\leq1-M/N$, including equality. For every input statement, every adaptive prover, and every query count $l$, the actual FRI reduction has straightline knowledge soundness with the named extractor and error

$$
\operatorname{soundnessError}
=\sum_i\varepsilon_i(\theta)
+\bigl(\max\{0,1-\min\{\theta,\delta\}\}\bigr)^l,
$$

where $\varepsilon_i(\theta)$ is the existing powers-MCA folding error. The failure event includes both extraction failure and a returned witness outside the original closed-ball input relation, when the accepted output witness is valid.

## Depends on

- [fri-folding-error](thm-fri-folding-error.md)
- [fri-extractor-recovery](thm-fri-extractor-recovery.md)

## Proof

Use fresh folding-failure events with the empty input language, so the adaptive accumulation covers all inputs. For $0\leq\min\{\theta,\delta\}$, conditional on a safe prefix, a failed extraction and a valid final polynomial imply that the accepting density is less than $1-\min\{\theta,\delta\}$, by Theorem [fri-extractor-recovery](thm-fri-extractor-recovery.md). The query-vector probability is bounded by the corresponding $l$th power. The logged-game bridge preserves private and shared oracle state and treats the optional extraction result as a value, counting failure rather than aborting it. If $\min\{\theta,\delta\}<0$, the query term is at least one and the bound is vacuous. If $l=0$, this term is one as well. Neither case needs an additional public assumption. Numerical estimates for the MCA terms retain their separate field-size, slack, and radius hypotheses.

## Lean

Formalized as [`Fri.Spec.knowledge_soundness_with`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.knowledge_soundness_with), [`Fri.Spec.knowledge_soundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.knowledge_soundness).

## Sources

- [ArkLib blueprint: proof_systems/fri.tex, line 176](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/fri.tex#L176)
