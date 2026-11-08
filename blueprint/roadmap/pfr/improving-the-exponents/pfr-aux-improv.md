---
declaration: lemma
origin: cited
lean: PFR_conjecture_improv_aux
statement: formalized
proof: formalized
---

# pfr_aux-improv

If $A \subset {\bf F}_2^n$ is non-empty and $|A+A| \leq K|A|$, then $A$ can be covered by at most $K^6 |A|^{1/2}/|H|^{1/2}$ translates of a subspace $H$ of ${\bf F}_2^n$ with

$$
|H|/|A| \in [K^{-10}, K^{10}].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Improved entropy version of PFR](entropy-pfr-improv.md)
- [Uniform distributions exist](../shannon-entropy-inequalities/part-01/unif-exist.md)
- [Entropy of uniform random variable, II](../shannon-entropy-inequalities/part-01/uniform-entropy-ii.md)
- [Jensen bound](../shannon-entropy-inequalities/part-01/jensen-bound.md)
- [Ruzsa distance](../entropic-ruzsa-calculus/part-01/ruz-dist-def.md)
- [Distance controls entropy difference](../entropic-ruzsa-calculus/part-01/ruzsa-diff.md)
- [Bounded entropy implies concentration](../shannon-entropy-inequalities/part-01/bound-conc.md)
- [Ruzsa covering lemma](../proof-of-pfr/ruz-cov.md)

## Proof

By repeating the proof of [Lemma pfr_aux](../proof-of-pfr/pfr-aux.md) and using [Improved entropy version of PFR](entropy-pfr-improv.md) one can obtain the claim with $13/2$ replaced with $6$ and $11$ replaced by $10$.

## Lean

Formalized as [`PFR_conjecture_improv_aux`](https://teorth.github.io/pfr/docs/find/#doc/PFR_conjecture_improv_aux).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/improved_exponent.tex, line 214](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/improved_exponent.tex#L214)
