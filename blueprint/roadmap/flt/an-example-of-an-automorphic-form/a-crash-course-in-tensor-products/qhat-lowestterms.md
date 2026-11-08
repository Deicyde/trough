---
declaration: lemma
origin: cited
lean: QHat.lowestTerms
statement: formalized
---

# QHat.lowestTerms

Every element of $\widehat{\mathbb{Q}}$ can be uniquely written as $z/N$ with $z\in\widehat{\mathbb{Z}}$, $N\in\mathbb{N}^+$, and with $N$ and $z$ coprime.

## Depends on

- [QHat.IsCoprime](qhat-iscoprime.md)

## Proof

Existence: by the previous lemma, an arbitrary element can be written as $z/N$; let $D$ be the greatest common divisor of $N$ and $z_N$ (lifted to a natural). If $D=1$ then the fraction is by definition in lowest terms. However if $1\lt D\mid N$ then $z_D$ is the reduction of $z_N$ and is hence 0. By lemma [ZHat.multiples](../widehat-z/zhat-multiples.md) we deduce that $z=Dy$ is a multiple of $D$, and hence $z/N=\frac{1}{N}\otimes_tDy=\frac{1}{E}\otimes y$, where $E=N/D$. Now if a natural divided both $y_E$ and $E$ then this natural would divide both $z_N/D$ and $N/D$, contradicting the fact that $D$ is the greatest common divisor.

Uniqueness: if $z/N=w/M$, we deduce $1\otimes_t Mz=1\otimes_t Nw$, and by injectivity of $\widehat{\mathbb{Z}}\to\widehat{\mathbb{Q}}$ we deduce that $Mz=Nw=y$. In particular, if $L$ is the lowest common multiple of $M$ and $N$ then $y_L$ is a multiple of both $M$ and $N$ and is hence zero, so $y=Lx$ is a multiple of $L$ by [ZHat.multiples](../widehat-z/zhat-multiples.md), and we deduce from torsionfreeness that $z=(L/M)x$ and $w=(L/N)x$. If some prime divided $L/M$ then it would have to divide $N$ which means that $z$ is not in lowest terms; similarly if some prime divided $L/N$ then $w/M$ would not be in lowest terms. We deduce that $L=M=N$ and hence $z=w$ by torsionfreeness.

## Lean

Stated as [`QHat.lowestTerms`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/QHat.lowestTerms); the blueprint does not mark its proof formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 369](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch05automorphicformexample.tex#L369)
