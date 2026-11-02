---
navigation: transparent
---

# Zeta0EqZeta to LogDerivZetaHolcLargeT9

- [Zeta0EqZeta](zeta0eqzeta.md)
- [ZetaBnd-aux2](zetabnd-aux2.md)
- [ZetaUpperBnd](zetaupperbnd.md)
- [DerivUpperBnd-aux7](derivupperbnd-aux7.md)
- [ZetaDerivUpperBnd](zetaderivupperbnd.md)
- [ZetaNear1BndFilter](zetanear1bndfilter.md)
- [ZetaNear1BndExact](zetanear1bndexact.md)
- [ZetaLowerBound3](zetalowerbound3.md)
- [ZetaInvBound1](zetainvbound1.md)
- [ZetaInvBound2](zetainvbound2.md)
- [Zeta-eq-int-derivZeta](zeta-eq-int-derivzeta.md)
- [Zeta-diff-Bnd](zeta-diff-bnd.md)
- [ZetaInvBnd](zetainvbnd.md)

Annoyingly, it is not immediate from this that $\zeta$ doesn't vanish there! That's because $1/0 = 0$ in Lean. So we give a second proof of the same fact (refactor this later), with a lower bound on $\zeta$ instead of upper bound on $1 / \zeta$.

- [ZetaLowerBnd](zetalowerbnd.md)

Now we get a zero free region.

- [ZetaZeroFree9](zetazerofree9.md)
- [LogDerivZetaBnd](logderivzetabnd.md)
- [ZetaNoZerosOn1Line](zetanozeroson1line.md)

Then, since $\zeta$ doesn't vanish on the 1-line, there is a $\sigma<1$ (depending on $T$), so that the box $[\sigma,1] \times_{ℂ} [-T,T]$ is free of zeros of $\zeta$.

- [ZetaNoZerosInBox](zetanozerosinbox.md)

We now prove that there's an absolute constant $\sigma_0$ so that $\zeta'/\zeta$ is holomorphic on a rectangle $[\sigma_2,2] \times_{ℂ} [-3,3] \setminus \{1\}$.

- [LogDerivZetaHolcSmallT](logderivzetaholcsmallt.md)
- [LogDerivZetaHolcLargeT9](logderivzetaholclarget9.md)
