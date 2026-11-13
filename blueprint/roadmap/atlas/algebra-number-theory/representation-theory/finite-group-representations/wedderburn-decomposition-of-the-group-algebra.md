---
declaration: section
origin: cited
lean: CharacterTheory.wedderburnAlgHom, CharacterTheory.wedderburnIrrep, CharacterTheory.wedderburnIrrep_isIrreducible
statement: formalized
proof: formalized
---

# Wedderburn decomposition of the group algebra

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/wedderburn-decomposition-of-the-group-algebra/index.html).

## Algebra map of a Wedderburn block

Let $k$ be an algebraically closed field, $G$ a finite
group whose order is nonzero in $k$, and $e \colon k[G] \to \prod_{j < n} M_{d_j}(k)$ an
isomorphism of $k$-algebras from the group algebra onto a product of full matrix algebras. For
$i < n$, this is the $k$-algebra homomorphism $k[G] \to \operatorname{End}_k(k^{d_i})$ that sends
$a \in k[G]$ to the linear map $v \mapsto e(a)_i \, v$, where $e(a)_i$ is the $i$-th component of
$e(a)$.

Formalized by `CharacterTheory.wedderburnAlgHom`, a definition declared in [MathlibExt/RepresentationTheory/WedderburnIrrep.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/WedderburnIrrep.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/wedderburn-decomposition-of-the-group-algebra/index.html#wedderburn-alg-hom).

## Representation of a Wedderburn block

Let $k$ be an algebraically closed field, $G$ a
finite group whose order is nonzero in $k$, and $e \colon k[G] \to \prod_{j < n} M_{d_j}(k)$ an
isomorphism of $k$-algebras from the group algebra $k[G]$ onto a product of full matrix algebras
$M_{d_j}(k)$ of $d_j \times d_j$ matrices over $k$. For $i < n$, this is the representation of $G$
on $k^{d_i}$ in which $g \in G$ acts by $v \mapsto e(g)_i \, v$, where $g$ is viewed as an element
of $k[G]$ and $e(g)_i$ is the $i$-th component of $e(g)$.

Formalized by `CharacterTheory.wedderburnIrrep`, a definition declared in [MathlibExt/RepresentationTheory/WedderburnIrrep.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/WedderburnIrrep.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/wedderburn-decomposition-of-the-group-algebra/index.html#wedderburn-irrep).

## Wedderburn blocks are irreducible

Let $k$ be an algebraically closed field, $G$ a finite
group whose order is nonzero in $k$, and $e \colon k[G] \to \prod_{j < n} M_{d_j}(k)$ an
isomorphism of $k$-algebras from the group algebra $k[G]$ onto a product of full matrix algebras
$M_{d_j}(k)$ of $d_j \times d_j$ matrices over $k$. For every $i < n$ with $d_i \ne 0$, the
representation of $G$ on $k^{d_i}$ in which $g \in G$ acts by $v \mapsto e(g)_i \, v$, where $g$
is viewed as an element of $k[G]$ and $e(g)_i$ is the $i$-th component of $e(g)$, is
irreducible.

Formalized by `CharacterTheory.wedderburnIrrep_isIrreducible`, a theorem declared in [MathlibExt/RepresentationTheory/WedderburnIrrep.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/WedderburnIrrep.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/wedderburn-decomposition-of-the-group-algebra/index.html#wedderburn-irrep-is-irreducible).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wedderburn decomposition of the group algebra](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/wedderburn-decomposition-of-the-group-algebra/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RepresentationTheory/finite-group-representations/wedderburn-decomposition-of-the-group-algebra)
