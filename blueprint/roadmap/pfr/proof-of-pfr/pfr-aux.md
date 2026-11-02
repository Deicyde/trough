---
declaration: lemma
origin: cited
lean: PFR_conjecture_aux
statement: formalized
proof: formalized
---

# pfr\_aux

If $A \subset {\bf F}_2^n$ is non-empty and $|A+A| \leq K|A|$, then $A$ can be covered by at most $K ^ {13/2}|A|^{1/2}/|H|^{1/2}$ translates of a subspace $H$ of ${\bf F}_2^n$ with

$$
|H|/|A| \in [K^{-11}, K^{11}].\qquad\text{(1)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Entropy version of PFR](../entropy-version-of-pfr/conclusion/entropy-pfr.md)
- [Uniform distributions exist](../shannon-entropy-inequalities/part-01/unif-exist.md)
- [Entropy of uniform random variable, II](../shannon-entropy-inequalities/part-01/uniform-entropy-ii.md)
- [Jensen bound](../shannon-entropy-inequalities/part-01/jensen-bound.md)
- [Ruzsa distance](../entropic-ruzsa-calculus/part-01/ruz-dist-def.md)
- [Distance controls entropy difference](../entropic-ruzsa-calculus/part-01/ruzsa-diff.md)
- [Bounded entropy implies concentration](../shannon-entropy-inequalities/part-01/bound-conc.md)
- [Ruzsa covering lemma](ruz-cov.md)

## Proof

Let $U_A$ be the uniform distribution on $A$ (which exists by [Uniform distributions exist](../shannon-entropy-inequalities/part-01/unif-exist.md)), thus $\mathbb{H}[U_A] = \log |A|$ by [Entropy of uniform random variable, II](../shannon-entropy-inequalities/part-01/uniform-entropy-ii.md). By [Jensen bound](../shannon-entropy-inequalities/part-01/jensen-bound.md) and the fact that $U_A + U_A$ is supported on $A + A$, $\mathbb{H}[U_A + U_A] \leq \log|A+A|$. By [Ruzsa distance](../entropic-ruzsa-calculus/part-01/ruz-dist-def.md), the doubling condition $|A+A| \leq K|A|$ therefore gives

$$
d[U_A;U_A] \leq \log K.
$$

By [Entropy version of PFR](../entropy-version-of-pfr/conclusion/entropy-pfr.md), we may thus find a subspace $H$ of $\mathbb{F}_2^n$ such that

$$
d[U_A;U_H] \leq \tfrac{1}{2} C' \log K\qquad\text{(2)}
$$

with $C' = 11$. By [Distance controls entropy difference](../entropic-ruzsa-calculus/part-01/ruzsa-diff.md) we conclude that

$$
|\log |H| - \log |A|| \leq C' \log K,
$$

proving (1). From [Ruzsa distance](../entropic-ruzsa-calculus/part-01/ruz-dist-def.md), (2) is equivalent to

$$
\mathbb{H}[U_A - U_H] \leq \log( |A|^{1/2} |H|^{1/2}) + \tfrac{1}{2} C' \log K.
$$

By [Bounded entropy implies concentration](../shannon-entropy-inequalities/part-01/bound-conc.md) we conclude the existence of a point $x_0 \in \mathbb{F}_p^n$ such that

$$
p_{U_A-U_H}(x_0) \geq |A|^{-1/2} |H|^{-1/2} K^{-C'/2},
$$

or equivalently

$$
|A \cap (H + x_0)| \geq K^{-C'/2} |A|^{1/2} |H|^{1/2}.
$$

Applying [Ruzsa covering lemma](ruz-cov.md), we may thus cover $A$ by at most

$$
\frac{|A + (A \cap (H+x_0))|}{|A \cap (H + x_0)|} \leq \frac{K|A|}{K^{-C'/2} |A|^{1/2} |H|^{1/2}} = K^{C'/2+1} \frac{|A|^{1/2}}{|H|^{1/2}}
$$

translates of

$$
\bigl(A \cap (H + x_0)\bigr) - \bigl(A \cap (H + x_0)\bigr) \subseteq H.
$$

This proves the claim.

## Lean

Formalized as [`PFR_conjecture_aux`](https://teorth.github.io/pfr/docs/find/#doc/PFR_conjecture_aux).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/pfr.tex, line 14](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/pfr.tex#L14)
