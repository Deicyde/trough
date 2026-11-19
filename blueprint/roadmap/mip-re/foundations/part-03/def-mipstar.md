---
declaration: definition
origin: cited
lean: MIPRE.MIPStar, MIPRE.PolyVerifier, MIPRE.PolyVerifier.Efficient, MIPRE.PolyVerifier.game
statement: formalized
---

# The class $\mathrm{MIP}^*_{1,1/2}(2,1)$

A language $L\subseteq\{0,1\}^*$ is in $\mathrm{MIP}^*_{1,1/2}(2,1)$, written $\mathrm{MIP}^*$ here, if there are two machines, a sampler $\mathcal{S}$ and a decider $\mathcal{D}$, and a polynomial $P$ such that for every string $z$, writing $B = P(\left\vert {z} \right\vert)$:

1. *Efficiency.* On input $z$ and a uniformly random seed $r\in\{0,1\}^B$, the sampler halts within time $P(\left\vert {z} \right\vert+\left\vert {r} \right\vert)$ with a pair $(x,y)$ of strings of length at most $B$; write $\mu_z$ for the distribution of $(x,y)$. On input $(z,x,y,a,b)$, the decider halts within time $P(\left\vert {z} \right\vert+\left\vert {x} \right\vert+\left\vert {y} \right\vert+\left\vert {a} \right\vert+\left\vert {b} \right\vert)$ with a bit $D_z(x,y,a,b)$, and this bit is $0$ whenever one of $x,y,a,b$ is longer than $B$. The game $\mathfrak{G}_z$ has the strings of length at most $B$ as its question and answer alphabets, question distribution $\mu_z$ and decision predicate $D_z$.
2. *Completeness.* If $z\in L$ then $\mathrm{val}^*(\mathfrak{G}_z)=1$.
3. *Soundness.* If $z\notin L$ then $\mathrm{val}^*(\mathfrak{G}_z)\leq\tfrac12$.

## Depends on

- [Quantum value](../part-01/def-q-value.md)
- [Normal form verifier in the ambient model](def-normal-verifier.md)

## Lean

Formalized as [`MIPRE.MIPStar`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MIPStar), [`MIPRE.PolyVerifier`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PolyVerifier), [`MIPRE.PolyVerifier.Efficient`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PolyVerifier.Efficient), [`MIPRE.PolyVerifier.game`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PolyVerifier.game).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 1599](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L1599)
