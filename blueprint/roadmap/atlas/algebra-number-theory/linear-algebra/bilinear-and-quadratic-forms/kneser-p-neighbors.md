---
declaration: section
origin: cited
lean: Submodule.ArePNeighbors, Submodule.arePNeighbors_comm, Submodule.not_arePNeighbors_one
statement: formalized
proof: formalized
---

# Kneser p-neighbors

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/kneser-p-neighbors/index.html).

## $p$-neighbors of submodules

Let $R$ be a commutative ring, $M$ an $R$-module and $p$ a
natural number. Two submodules $L_1$ and $L_2$ of $M$ are $p$-neighbors when $p$ is prime and the
intersection $L_1 \cap L_2$ has index $p$ in each of them, that is, the quotients
$L_1 / (L_1 \cap L_2)$ and $L_2 / (L_1 \cap L_2)$ both have exactly $p$ elements.

Formalized by `Submodule.ArePNeighbors`, a definition declared in [MathlibExt/LinearAlgebra/Submodule/PNeighbor.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Submodule/PNeighbor.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/kneser-p-neighbors/index.html#are-pneighbors).

## The $p$-neighbor relation is symmetric

For every natural number $p$ and all submodules
$L_1$, $L_2$ of a module $M$ over a commutative ring $R$, $L_1$ and $L_2$ are $p$-neighbors if
and only if $L_2$ and $L_1$ are $p$-neighbors.

Formalized by `Submodule.arePNeighbors_comm`, a theorem declared in [MathlibExt/LinearAlgebra/Submodule/PNeighbor.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Submodule/PNeighbor.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/kneser-p-neighbors/index.html#are-pneighbors-comm).

## No submodules are $1$-neighbors

For any submodules $L_1$ and $L_2$ of a module $M$
over a commutative ring $R$, $L_1$ and $L_2$ are not $1$-neighbors, since $1$ is not prime.

Formalized by `Submodule.not_arePNeighbors_one`, a theorem declared in [MathlibExt/LinearAlgebra/Submodule/PNeighbor.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Submodule/PNeighbor.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/kneser-p-neighbors/index.html#not-are-pneighbors-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kneser p-neighbors](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/kneser-p-neighbors/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/kneser-p-neighbors)
