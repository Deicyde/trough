---
declaration: lemma
origin: cited
---

# nolean-compactopen-U1p

$U_v$ is a compact open subgroup of $GL_2(K_v)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Submonoid.units\_isOpen](../restricted-products/submonoid-units-isopen.md)
- [Submonoid.units\_isCompact](../restricted-products/submonoid-units-iscompact.md)

## Proof

$\Gamma_v$ is a group and hence its preimage $U_v$ is a subgroup of the monoid $M_2(K_v)$. It is compact and open as we just saw. Hence its units (also $U_v$) are a subgroup of $GL_2(K_v)$, which is compact and open, again by lemmas [Lemma Submonoid.units\_isOpen](../restricted-products/submonoid-units-isopen.md) and [Lemma Submonoid.units\_isCompact](../restricted-products/submonoid-units-iscompact.md).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HeckeOperatorProject.tex, line 420](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HeckeOperatorProject.tex#L420)
