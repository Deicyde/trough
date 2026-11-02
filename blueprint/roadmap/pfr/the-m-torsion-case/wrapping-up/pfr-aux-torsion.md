---
declaration: lemma
origin: cited
lean: torsion_PFR_conjecture_aux
statement: formalized
proof: formalized
---

# pfr\_aux\_torsion

Suppose that $G$ is a finite abelian group of torsion $m$. If $A \subset G$ is non-empty and $|A+A| \leq K|A|$, then $A$ can be covered by at most $K ^ {128m^3+1}|A|^{1/2}/|H|^{1/2}$ translates of a subspace $H$ of $G$ with

$$
|H|/|A| \in [K^{-256m^3}, K^{256m^3}].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Entropy form of PFR](main-entropy.md)
- [Uniform distributions exist](../../shannon-entropy-inequalities/part-01/unif-exist.md)
- [Entropy of uniform random variable, II](../../shannon-entropy-inequalities/part-01/uniform-entropy-ii.md)
- [Jensen bound](../../shannon-entropy-inequalities/part-01/jensen-bound.md)
- [Ruzsa distance](../../entropic-ruzsa-calculus/part-01/ruz-dist-def.md)
- [Distance controls entropy difference](../../entropic-ruzsa-calculus/part-01/ruzsa-diff.md)
- [Bounded entropy implies concentration](../../shannon-entropy-inequalities/part-01/bound-conc.md)
- [Ruzsa covering lemma](../../proof-of-pfr/ruz-cov.md)

## Proof

Repeat the proof of [Lemma pfr\_aux](../../proof-of-pfr/pfr-aux.md), but with [Entropy form of PFR](main-entropy.md) in place of [Entropy version of PFR](../../entropy-version-of-pfr/conclusion/entropy-pfr.md). Because of the lack of $2$-torsion, one has to use the Ruzsa triangle inequality to bound $d[U,U]$ by $2d[U,-U]$, costing an additional factor of $2$ in the estimates.

## Lean

Formalized as [`torsion_PFR_conjecture_aux`](https://teorth.github.io/pfr/docs/find/#doc/torsion_PFR_conjecture_aux).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 880](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L880)
