---
declaration: lemma
origin: cited
lean: QHat.rat_meet_zHat
statement: formalized
proof: formalized
---

# QHat.rat_meet_zHat

The intersection of $\mathbb{Q}$ and $\widehat{\mathbb{Z}}$ in $\widehat{\mathbb{Q}}$ is $\mathbb{Z}$.

## Depends on

- [QHat](../widehat-q-and-tensor-products/qhat.md)
- [ZHat.commRing](../widehat-z/zhat-commring.md)

## Proof depends on

- [QHat.lowestTerms](../a-crash-course-in-tensor-products/qhat-lowestterms.md)

## Proof

Clearly $\mathbb{Z}\subseteq\mathbb{Q}\cap\widehat{\mathbb{Z}}$. Now suppose that $x\in\mathbb{Q}\cap\widehat{\mathbb{Z}}$. Because $x$ is rational we can write it as $\frac{A}{B}\otimes_t1$ for some fraction $A/B$ in lowest terms, and hence $x=A/B$ where now we regard $A\in\widehat{\mathbb{Z}}$ and note that $A/B$ is still in lowest terms. However $x\in\widehat{\mathbb{Z}}$ implies that $x=x/1$ is in lowest terms, so we deduce that $B=1$ and thus $x=A\in\mathbb{Z}$.

## Lean

Formalized as [`QHat.rat_meet_zHat`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/QHat.rat_meet_zHat).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 448](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch05automorphicformexample.tex#L448)
