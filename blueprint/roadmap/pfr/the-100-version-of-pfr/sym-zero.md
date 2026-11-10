---
declaration: lemma
origin: cited
lean: isUniform_sub_const_of_rdist_eq_zero
statement: formalized
proof: formalized
---

# Translate is uniform on symmetry group

If $X$ is a $G$-valued random variable with $d[X ;X]=0$, and $x_0$ is a point with $P[X=x_0] > 0$, then $X-x_0$ is uniformly distributed on $\mathrm{Sym}[X]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Zero Ruzsa distance implies large symmetry group](zero-large.md)
- [Symmetry group](sym-group-def.md)
- [Uniform distribution](../shannon-entropy-inequalities/part-01/uniform-def.md)

## Proof

The law of $X-x_0$ is invariant under $\mathrm{Sym}[X]$, non-zero at the origin, and supported on $\mathrm{Sym}[X]$, giving the claim.

## Lean

Formalized as [`isUniform_sub_const_of_rdist_eq_zero`](https://teorth.github.io/pfr/docs/find/#doc/isUniform_sub_const_of_rdist_eq_zero).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/100_percent.tex, line 32](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/100_percent.tex#L32)
