---
declaration: corollary
origin: cited
lean: rhoPlus_of_subgroup
statement: formalized
proof: formalized
---

# Rho plus of subgroup

If $H$ is a finite subgroup of $G$, then $\rho^+(U_H) = \log |H| - \log \max_t |A \cap (H+t)|$.

## Depends on

- [Rho plus](rhoplus-def.md)

## Proof depends on

- [Rho minus of subgroup](rhominus-subgroup.md)

## Proof

Straightforward by definition and [Rho minus of subgroup](rhominus-subgroup.md).

## Lean

Formalized as [`rhoPlus_of_subgroup`](https://teorth.github.io/pfr/docs/find/#doc/rhoPlus_of_subgroup).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 112](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/further_improvement.tex#L112)
