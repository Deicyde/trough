---
declaration: lemma
origin: cited
lean: Hurwitz.exists_near
statement: formalized
proof: formalized
---

# Hurwitz.exists_near

Given a “usual” quaternion $a=x+yi+zj+wk$ with $x,y,z,w\in\mathbb{R}$, there exists a Hurwitz quaternion $q$ such that $N(a-q)<1$.

## Depends on

- [Hurwitz.norm](hurwitz-norm.md)

## Proof

If $[r]$ denotes the nearest integer to the real number $r$, then $|r-[r]|\leq \frac{1}{2}$. Hence if $q=[x]+[y]i+[z]j+[w]k$ then $N(a-q)=|x-[x]|^2+\cdots \leq \frac{1}{4}+\frac{1}{4}+\frac{1}{4}+\frac{1}{4}\leq 1$, with strict inequality unless $|x-[x]|=|y-[y]|=|z-[z]|=|w-[w]|=\frac{1}{2}$, in which case $a\in\mathcal{O}$ because $a-\omega$ has integer coordinates.

## Lean

Formalized as [`Hurwitz.exists_near`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/Hurwitz.exists_near).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 662](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch05automorphicformexample.tex#L662)
