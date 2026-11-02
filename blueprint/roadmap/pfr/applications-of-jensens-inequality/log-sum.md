---
declaration: lemma
origin: cited
lean: Real.sum_mul_log_div_leq
statement: formalized
proof: formalized
---

# log sum inequality

If $S$ is a finite set, and $a_s,b_s$ are non-negative for $s\in S$, then

$$
\sum_{s\in S} a_s \log\frac{a_s}{b_s}\ge \left(\sum_{s\in S}a_s\right)\log\frac{\sum_{s\in S} a_s}{\sum_{s\in S} b_s},
$$

with the convention $0\log\frac{0}{b}=0$ for any $b\ge 0$ and $0\log\frac{a}{0}=\infty$ for any $a>0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $B:=\sum_{s\in S} b_s$. Apply Jensen and [Concavity](concave.md) to show that $\sum_{s\in S} \frac{b_s}{B} h(\frac{a_s}{b_s})\ge h(\frac{\sum_{s\in S} a_s}{B})$.

## Lean

Formalized as [`Real.sum_mul_log_div_leq`](https://teorth.github.io/pfr/docs/find/#doc/Real.sum_mul_log_div_leq).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/jensen.tex, line 14](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/jensen.tex#L14)
