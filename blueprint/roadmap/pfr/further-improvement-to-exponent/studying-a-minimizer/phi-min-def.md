---
declaration: definition
origin: cited
lean: phiMinimizes
statement: formalized
---

# phi-min-def

Given $G$-valued random variables $X,Y$, define

$$
\phi[X;Y] := d[X;Y] + \eta(\rho(X) + \rho(Y))
$$

and define a *$\phi$-minimizer* to be a pair of random variables $X,Y$ which minimizes $\phi[X;Y]$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`phiMinimizes`](https://teorth.github.io/pfr/docs/find/#doc/phiMinimizes).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 216](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L216)
