---
declaration: lemma
origin: cited
lean: rho_of_subgroup
statement: formalized
proof: formalized
---

# Rho of subgroup

If $H$ is a finite subgroup of $G$, and $\rho(U_H) \leq r$, then there exists $t$ such that $|A \cap (H+t)| \geq e^{-r} \sqrt{|A||H|}$, and $|H|/|A|\in[e^{-2r},e^{2r}]$.

## Depends on

- [Rho functional](rho-def.md)

## Proof depends on

- [Rho minus of subgroup](rhominus-subgroup.md)
- [Rho plus of subgroup](rhoplus-subgroup.md)

## Proof

The first claim is a direct corollary of [Rho minus of subgroup](rhominus-subgroup.md) and [Rho plus of subgroup](rhoplus-subgroup.md). To see the second claim, observe that [Rho minus non-negative](rhominus-nonneg.md) and [Rho plus of subgroup](rhoplus-subgroup.md) imply $\rho^-(U_H),\rho^+(U_H)\ge 0$. Therefore

$$
|H(U_A)-H(U_H)|=|\rho^+(U_H)-\rho^-(U_H)|\le \rho^-(U_H)+\rho^+(U_H)= 2\rho(U_H)\le 2r,
$$

which implies the second claim.

## Lean

Formalized as [`rho_of_subgroup`](https://teorth.github.io/pfr/docs/find/#doc/rho_of_subgroup).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 127](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L127)
