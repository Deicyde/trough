---
declaration: theorem
origin: cited
lean: PFR_conjecture
statement: formalized
proof: formalized
---

# PFR

If $A \subset {\bf F}_2^n$ is non-empty and $|A+A| \leq K|A|$, then $A$ can be covered by most $2K^{12}$ translates of a subspace $H$ of ${\bf F}_2^n$ with $|H| \leq |A|$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [pfr_aux](pfr-aux.md)

## Proof

Let $H$ be given by [Lemma pfr_aux](pfr-aux.md). If $|H| \leq |A|$ then we are already done thanks to [(1)](pfr-aux.md). If $|H| > |A|$ then we can cover $H$ by at most $2 |H|/|A|$ translates of a subspace $H'$ of $H$ with $|H'| \leq |A|$. We can thus cover $A$ by at most

$$
2K^{13/2} \frac{|H|^{1/2}}{|A|^{1/2}}
$$

translates of $H'$, and the claim again follows from [(1)](pfr-aux.md).

## Lean

Formalized as [`PFR_conjecture`](https://teorth.github.io/pfr/docs/find/#doc/PFR_conjecture).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/pfr.tex, line 50](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/pfr.tex#L50)
