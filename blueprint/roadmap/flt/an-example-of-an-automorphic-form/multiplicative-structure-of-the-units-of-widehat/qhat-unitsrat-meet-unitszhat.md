---
declaration: lemma
origin: cited
lean: QHat.unitsrat_meet_unitszHat
statement: formalized
proof: formalized
---

# Qhat.unitsrat_meet_unitszHat

The intersection of $\mathbb{Q}^\times$ and $\widehat{\mathbb{Z}}^\times$ in $\widehat{\mathbb{Q}}^\times$ is $\mathbb{Z}^\times$.

## Depends on

- [QHat](../widehat-q-and-tensor-products/qhat.md)
- [ZHat.commRing](../widehat-z/zhat-commring.md)

## Proof depends on

- [QHat.lowestTerms](../a-crash-course-in-tensor-products/qhat-lowestterms.md)
- [QHat.rat_meet_zHat](../additive-structure-of-widehat-q/qhat-rat-meet-zhat.md)

## Proof

Clearly the intersection is contained within $\mathbb{Q}\cap\widehat{\mathbb{Z}}=\mathbb{Z}$. If $n\in\mathbb{Z}$ is in $\widehat{\mathbb{Z}}^\times$ then $n\not=0$ and its inverse $1/n=\pm1/|n|$ is in lowest terms but also in $\widehat{\mathbb{Z}}$, and hence $|n|=1$ by uniqueness of lowest term representation.

## Lean

Formalized as [`QHat.unitsrat_meet_unitszHat`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/QHat.unitsrat_meet_unitszHat).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 488](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch05automorphicformexample.tex#L488)
