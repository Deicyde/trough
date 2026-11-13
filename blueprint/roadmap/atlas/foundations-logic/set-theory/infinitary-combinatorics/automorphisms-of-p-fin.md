---
declaration: section
origin: cited
lean: MetaMathlibExt.EqModFinite, MetaMathlibExt.IsPowModFiniteAutomorphism
statement: formalized
proof: formalized
---

# Automorphisms of P(ω)/fin

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/automorphisms-of-p-fin/index.html).

## Equality modulo finite sets

Subsets $A$ and $B$ of $\mathbb{N}$ are *equal modulo finite*,
written $A =^{\ast} B$, if their symmetric difference $A \mathbin{\triangle} B$ is finite.

Formalized by `MetaMathlibExt.EqModFinite`, a definition declared in [MathlibExt/SetTheory/Order/PowersetModFinite.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/SetTheory/Order/PowersetModFinite.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/automorphisms-of-p-fin/index.html#eq-mod-finite).

## Automorphisms of P(ω)/fin on representatives

For subsets $A$, $B$ of $\mathbb{N}$, write
$A =^{\ast} B$ when their symmetric difference is finite. A map $\Phi$ from subsets of
$\mathbb{N}$ to subsets of $\mathbb{N}$ presents an automorphism of $P(\omega)/\mathrm{fin}$ if for
all subsets $A$, $B$ of $\mathbb{N}$: it respects $=^{\ast}$ ($A =^{\ast} B$ implies
$\Phi(A) =^{\ast} \Phi(B)$), it preserves meets ($\Phi(A \cap B) =^{\ast} \Phi(A) \cap \Phi(B)$)
and complements ($\Phi(\mathbb{N} \setminus A) =^{\ast} \mathbb{N} \setminus \Phi(A)$), it is
one-to-one modulo finite ($\Phi(A) =^{\ast} \Phi(B)$ implies $A =^{\ast} B$), and it is onto
modulo finite (for every $B$ there is $A$ with $\Phi(A) =^{\ast} B$).

Formalized by `MetaMathlibExt.IsPowModFiniteAutomorphism`, a structure declared in [MathlibExt/SetTheory/Order/PowersetModFinite.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/SetTheory/Order/PowersetModFinite.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/automorphisms-of-p-fin/index.html#is-pow-mod-finite-automorphism).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Automorphisms of P(ω)/fin](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/automorphisms-of-p-fin/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/SetTheory/infinitary-combinatorics/automorphisms-of-p-fin)
