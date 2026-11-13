---
declaration: section
origin: cited
lean: MathlibExt.Order.BooleanAlgebra.StoneRepresentation.stone_representation_theorem
statement: formalized
proof: formalized
---

# Lattices and Boolean algebras: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/lattices-boolean-algebras/index.html).

Lattices and Boolean algebras, their representation theorems, and Boolean functions viewed as maps between Boolean lattices.

## Stone representation theorem

Every Boolean algebra $B$ embeds in a power set algebra: there
are a set $X$ and an injective map $f$ from $B$ to the power set of $X$ such that
$f(a \sqcup b) = f(a) \cup f(b)$ and $f(a \sqcap b) = f(a) \cap f(b)$ for all $a, b \in B$,
$f(\top) = X$ and $f(\bot) = \emptyset$.

Such a map automatically preserves complements: $f(a^c) = X \setminus f(a)$ for all $a \in B$.

## Sources

- M. H. Stone, The Theory of Representation for Boolean Algebras, Trans. Amer. Math. Soc. 40 (1936), 37–111, DOI 10.2307/1989664.

Formalized by `MathlibExt.Order.BooleanAlgebra.StoneRepresentation.stone_representation_theorem`, a theorem declared in [MathlibExt/Order/BooleanAlgebra/StoneRepresentation.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Order/BooleanAlgebra/StoneRepresentation.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/lattices-boolean-algebras/index.html#stone-representation-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lattices and Boolean algebras](https://deicyde.github.io/atlas-lean/roadmap/Order/lattices-boolean-algebras/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Order/lattices-boolean-algebras)
