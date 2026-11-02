---
declaration: lemma
origin: cited
lean: ZHat.multiples
statement: formalized
proof: formalized
---

# ZHat.multiples

The multiples of $N$ in $\widehat{\mathbb{Z}}$ are precisely the compatible collections $(z_i)_i\in\widehat{\mathbb{Z}}$ with $z_N=0$.

## Depends on

- [ZHat.commRing](zhat-commring.md)

## Proof

Clearly $z_N=0$ is a necessary condition to be a multiple of $N$. To see it is sufficient, take a general $(z_i)\in\widehat{\mathbb{Z}}$ such that $z_N=0$, and now define a new element $(y_j)_j$ of $\widehat{\mathbb{Z}}$ by $y_j=z_{Nj}/N$. Just to clarify what this means: $z_{Nj}\in\mathbb{Z}/Nj\mathbb{Z}$ reduces mod $N$ to $z_N=0$ by the compatibility assumption, so it is in the subgroup $N\mathbb{Z}/Nj\mathbb{Z}$ of $\mathbb{Z}/Nj\mathbb{Z}$, which is isomorphic (via "division by $N$") to the group $\mathbb{Z}/j\mathbb{Z}$; this is how we construct $y_j$. It is easily checked that the $y_j$ are compatible and that $Ny=z$.

## Lean

Formalized as [`ZHat.multiples`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/ZHat.multiples).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 209](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch05automorphicformexample.tex#L209)
