---
declaration: lemma
origin: cited
lean: FreyPackage.of_not_FermatLastTheoremFor_p_ge_5
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/19
---

# FreyPackage.of_not_FermatLastTheorem_p_ge_5

If Fermat's Last Theorem is false for $p \ge 5$ and prime, then there exists a Frey package.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [FreyPackage](freypackage.md)

## Proof

Suppose we have a counterexample $a^p+b^p=c^p$ for the given $p$; we now build a Frey package from this data.

If the greatest common divisor of $a,b,c$ is $d$ then $a^p+b^p=c^p$ implies $(a/d)^p+(b/d)^p=(c/d)^p$. Dividing through, we can thus assume that no prime divides all of $a,b,c$. Under this assumption we must have that $a,b,c$ are pairwise coprime, as if some prime divides two of the integers $a,b,c$ then by $a^p+b^p=c^p$ and unique factorization it must divide all three of them. In particular we may assume that not all of $a,b,c$ are even, and now reducing modulo 2 shows that precisely one of them must be even.

Next we show that we can find a counterexample with $b$ even. If $a$ is the even one then we can just switch $a$ and $b$. If $c$ is the even one then we can replace $c$ by $-b$ and $b$ by $-c$ (using that $p$ is odd).

The last thing to ensure is that $a$ is 3 mod 4. Because $b$ is even, we know that $a$ is odd, so it is either 1 or 3 mod 4. If $a$ is 3 mod 4 then we are home; if however $a$ is 1 mod 4 we replace $a,b,c$ by their negatives and this is the Frey package we seek.

## Lean

Formalized as [`FreyPackage.of_not_FermatLastTheoremFor_p_ge_5`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/FreyPackage.of_not_FermatLastTheoremFor_p_ge_5).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch02reductions.tex, line 65](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch02reductions.tex#L65)
