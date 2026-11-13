---
declaration: section
origin: cited
lean: AlgEquiv.isGalois_and_orderOf_eq_finrank_of_finrank_prime_of_ne_one, IsAbelianGalois.isModularLattice_intermediateField, Algebra.TensorProduct.algebraMap_norm_eq_prod_map_algEquiv, InfiniteGalois.topologicalClosure_eq_fixingSubgroup_fixedField
statement: formalized
proof: formalized
---

# Galois theory: its own results

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/index.html).

Galois theory relates a field extension to its group of automorphisms, covering the Galois correspondence, infinite Galois groups, Hilbert's theorem 90, solvability by radicals and essential dimension.

## Extensions of prime degree with a nontrivial automorphism are Galois

In an extension of prime degree, a nontrivial automorphism witnesses
that the extension is Galois, has order equal to the degree, and generates
the automorphism group.

Formalized by `AlgEquiv.isGalois_and_orderOf_eq_finrank_of_finrank_prime_of_ne_one`, a theorem declared in [MathlibExt/FieldTheory/Galois/PrimeDegree.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Galois/PrimeDegree.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/index.html#is-galois-and-order-of-eq-finrank-of-fin).

## Intermediate fields of an abelian extension form a modular lattice

If $L/K$ is a
finite-dimensional abelian Galois extension, then the lattice of intermediate fields of $L/K$
is modular.

The proof transports the modular lattice of subgroups of the commutative Galois group across
the Galois correspondence.

Formalized by `IsAbelianGalois.isModularLattice_intermediateField`, a theorem declared in [MathlibExt/FieldTheory/Galois/Abelian.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Galois/Abelian.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/index.html#is-modular-lattice-intermediate-field).

## Norm in a tensor product with a Galois extension

For a Galois extension `M / F` and any `F`-algebra `R`, the norm of an
element of `R ⊗[F] M` over `R` is the product of its Galois conjugates.

Formalized by `Algebra.TensorProduct.algebraMap_norm_eq_prod_map_algEquiv`, a theorem declared in [MathlibExt/Algebra/TensorProduct/Norm.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/TensorProduct/Norm.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/index.html#algebra-map-norm-eq-prod-map-alg-equiv).

## The closure of a Galois subgroup is the fixing group of its fixed field

Let $K/k$ be a
Galois extension, not necessarily finite, and give $\operatorname{Gal}(K/k)$ the Krull topology.
For every subgroup $H$ of $\operatorname{Gal}(K/k)$ with fixed field $K^H$, the closure of $H$
equals the subgroup of $\operatorname{Gal}(K/k)$ consisting of the automorphisms that fix $K^H$
pointwise.

Formalized by `InfiniteGalois.topologicalClosure_eq_fixingSubgroup_fixedField`, a theorem declared in [MathlibExt/FieldTheory/Galois/Infinite.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Galois/Infinite.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/index.html#topological-closure-eq-fixing-subgroup-f).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Galois theory](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/FieldTheory/galois-theory)
