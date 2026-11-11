---
declaration: section
origin: cited
lean: PositiveLinearMap.exists_gns_cyclic_vector, MathlibExt.Analysis.CStarAlgebra.LandmarkWanted.cStarAlgebra_gns_cyclic_vector
statement: formalized
proof: formalized
---

# GNS construction

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/gns-construction/index.html).

## Positive Linear Map

## Existence of a unit cyclic vector in the GNS space

Let $A$ be a unital C*-algebra with
its standard order and let $f$ be a positive linear functional on $A$ with $f(1) = 1$. Let $H_f$
be the GNS Hilbert space of $f$ and $\pi_f : A \to B(H_f)$ its GNS representation. Then there is
a vector $\xi \in H_f$ with $\|\xi\| = 1$ such that $f(a) = \langle \xi, \pi_f(a) \xi \rangle$
for every $a \in A$, and the linear span of $\{\pi_f(a) \xi : a \in A\}$ is dense in $H_f$.

Formalized by `PositiveLinearMap.exists_gns_cyclic_vector`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/GNSCyclicVector.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/CStarAlgebra/GNSCyclicVector.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/gns-construction/index.html#exists-gns-cyclic-vector).

## GNS cyclic vector of a state

Let $A$ be a unital C*-algebra with its standard order and let
$f$ be a positive linear functional on $A$ with $f(1) = 1$. Let $H_f$ be the GNS Hilbert space of
$f$ and $\pi_f : A \to B(H_f)$ its GNS representation. Then there is a vector $\xi \in H_f$ with
$\|\xi\| = 1$ such that $f(a) = \langle \xi, \pi_f(a) \xi \rangle$ for every $a \in A$, and the
linear span of $\{\pi_f(a) \xi : a \in A\}$ is dense in $H_f$.

## Sources

- GNS construction, Gelfand–Naimark 1943 and I. E. Segal, Ann. of Math. 48 (1947); see Murphy, C*-Algebras; Lean is unital state f 1 = 1 unit cyclic vector with inner-product formula and dense span. It is `PositiveLinearMap.exists_gns_cyclic_vector`, kept under the source's name.

Formalized by `MathlibExt.Analysis.CStarAlgebra.LandmarkWanted.cStarAlgebra_gns_cyclic_vector`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/GNSCyclicVector.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/CStarAlgebra/GNSCyclicVector.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/gns-construction/index.html#c-star-algebra-gns-cyclic-vector).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: GNS construction](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/gns-construction/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-algebras/gns-construction)
