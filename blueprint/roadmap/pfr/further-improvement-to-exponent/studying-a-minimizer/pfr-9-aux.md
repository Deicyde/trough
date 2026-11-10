---
declaration: corollary
origin: cited
lean: better_PFR_conjecture_aux0
statement: formalized
proof: formalized
---

# pfr-9-aux

If $|A+A| \leq K|A|$, then there exists a subgroup $H$ and $t\in G$ such that $|A \cap (H+t)| \geq K^{-4} \sqrt{|A||H|}$, and $|H|/|A|\in[K^{-8},K^8]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [pfr-rho](pfr-rho.md)
- [Rho of subgroup](../rho-functionals/rho-subgroup.md)

## Proof

Apply [Proposition pfr-rho](pfr-rho.md) on $U_A,U_A$ to get a subspace such that $2\rho(U_H)\le 2\rho(U_A)+8d[U_A;U_A]$. Recall that $d[U_A;U_A]\le \log K$ as proved in [Lemma pfr_aux](../../proof-of-pfr/pfr-aux.md), and $\rho(U_A)=0$ by [Lemma rho_of_uniform](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/further_improvement.tex#L121). Therefore $\rho(U_H)\le 4\log(K)$. The claim then follows from [Rho of subgroup](../rho-functionals/rho-subgroup.md).

## Lean

Formalized as [`better_PFR_conjecture_aux0`](https://teorth.github.io/pfr/docs/find/#doc/better_PFR_conjecture_aux0).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 352](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/further_improvement.tex#L352)
