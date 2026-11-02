---
declaration: lemma
origin: cited
lean: ZHat.torsionfree
statement: formalized
proof: formalized
---

# ZHat.torsionfree

If $0\lt N$ is an integer then multiplication by $N$ is injective on $\widehat{\mathbb{Z}}$.

## Depends on

- [ZHat.commRing](zhat-commring.md)
- [ZHat.charZero](zhat-charzero.md)

## Proof

Suppose that $(z_i)_i\in\widehat{\mathbb{Z}}$ and $Nz=0$. This means that $Nz_i=0\in\mathbb{Z}/i\mathbb{Z}$ for all $i$. Let us fix an arbitrary positive integer $j$; we need to prove that $z_j=0\in\mathbb{Z}/j\mathbb{Z}$. Consider the element $z_{Nj}\in\mathbb{Z}/Nj\mathbb{Z}$. By assumption, we have $Nz_{Nj}=0$, meaning that if we lift $z_{Nj}$ to an integer, we have $Nj\mid Nz_{Nj}$, and thus $j\mid z_{Nj}$. Thus by the compatibility assumption on the $z_i$ we have that $z_j\in\mathbb{Z}/j\mathbb{Z}$ is the mod $j$ reduction of $z_{Nj}$ and hence is zero.

## Lean

Formalized as [`ZHat.torsionfree`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/ZHat.torsionfree).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 189](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch05automorphicformexample.tex#L189)
