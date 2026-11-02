---
declaration: theorem
origin: cited
---

# Hurwitz.surjective\_pnat\_quotient

If $N$ is a positive natural then the obvious map $\mathcal{O}\to\widehat{\mathcal{O}}/N\widehat{\mathcal{O}}$ is surjective.

## Depends on

- [Hurwitz](../the-hurwitz-quaternions/hurwitz.md)

## Proof

This is just four copies of the surjection $\mathbb{Z}\to\widehat{\mathbb{Z}}/N\widehat{\mathbb{Z}}$. Note that this latter map is surjective because $\mathbb{Z}\to\mathbb{Z}/N\mathbb{Z}$ is surjective, hence given $z\in\widehat{\mathbb{Z}}$ you can subtract an integer $w$ such that $(z-w)_N=0$, so $z-w$ is a multiple of $N$.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 716](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch05automorphicformexample.tex#L716)
