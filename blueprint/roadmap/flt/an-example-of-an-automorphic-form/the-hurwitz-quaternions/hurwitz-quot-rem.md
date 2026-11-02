---
declaration: lemma
origin: cited
lean: Hurwitz.quot_rem
statement: formalized
proof: formalized
---

# Hurwitz.quot\_rem

Given two Hurwitz quaternions $a$ and $b$ with $b$ nonzero, there exists $q$ and $r$ such that $a=qb+r$ and $N(r)\lt N(b)$.

## Depends on

- [Hurwitz.norm](hurwitz-norm.md)
- [Hurwitz.exists\_near](hurwitz-exists-near.md)

## Proof

Let $q$ be the Hurwitz quaternion obtained by applying Lemma [Hurwitz.exists\_near](hurwitz-exists-near.md) to $a/b := ab^{-1}$; then $N(a/b-q)<1$ and now everything follows after multiplying up.

## Lean

Formalized as [`Hurwitz.quot_rem`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/Hurwitz.quot_rem).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 679](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch05automorphicformexample.tex#L679)
