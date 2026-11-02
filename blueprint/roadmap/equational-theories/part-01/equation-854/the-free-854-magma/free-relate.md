---
declaration: definition
origin: cited
---

# Relation on the free group

For $x,y \in M_X$, we have $x \to y$ if and only if one of the following holds:

- (i) $x = y_R$.
- (ii) $y = x_{RL}$ and $x_{RR} \to x_L$.
- (iii) $x = y_{RL}$, $y_{RR} \to y_L$, and $y_R \to y_{RL}$.
- (iv) $y = x_R$, and there exists $z \in \{ x_{LR}, x_{LRL}, x_{RR}, x_{RRL} \}$ such that $z \to x_L$ and $z \to x_R$.
- (v) $y = x_R$, and one of the claims $x_L = x_R$, $x_L = x_{RL}$, or $x_R = x_{LL}$ holds.

Here we adopt the convention that a claim can only hold if all terms in it are well-defined, for instance claim (ii) can only hold if $x_{RL}$ is well-defined.

## Depends on

Its statement uses no other node of the blueprint.

## Sources

- [Equational Theories blueprint: chapter/854.tex, line 291](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/854.tex#L291)
