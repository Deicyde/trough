---
declaration: lemma
origin: cited
lean: QHat.rat_join_zHat
statement: formalized
proof: formalized
---

# QHat.rat\_join\_zHat

The sum of $\mathbb{Q}$ and $\widehat{\mathbb{Z}}$ in $\widehat{\mathbb{Q}}$ is $\widehat{\mathbb{Q}}$. More precisely, every element of $\widehat{\mathbb{Q}}$ can be written as $q+z$ with $q\in\mathbb{Q}$ and $z\in\widehat{\mathbb{Z}}$, or more precisely as $q\otimes_t 1+1\otimes_t z$.

## Depends on

- [QHat](../widehat-q-and-tensor-products/qhat.md)
- [ZHat.commRing](../widehat-z/zhat-commring.md)

## Proof depends on

- [QHat.canonicalForm](../a-crash-course-in-tensor-products/qhat-canonicalform.md)

## Proof

Write $x\in\widehat{\mathbb{Q}}$ as $x=z/N$ in lowest terms. Lift $z_N$ to an integer $t$ and observe that $(z-t)_N=0$, hence $z-t=Ny$ for some $y\in\widehat{\mathbb{Z}}$. Now $x=t/N+y\in\mathbb{Q}+\widehat{\mathbb{Z}}$.

## Lean

Formalized as [`QHat.rat_join_zHat`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/QHat.rat_join_zHat).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 465](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch05automorphicformexample.tex#L465)
