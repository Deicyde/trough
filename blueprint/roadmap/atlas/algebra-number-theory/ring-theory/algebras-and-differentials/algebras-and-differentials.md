---
declaration: section
origin: cited
lean: Algebra.isPushout_of_forall_existsUnique_algHom_comp_eq
statement: formalized
proof: formalized
---

# Étale algebras, norms and differentials: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/index.html).

Algebras over commutative rings: étale algebras and the trace form, norm and trace maps, Kähler differentials and derivations.

## Universal-property criterion for a pushout square of algebras

A square of algebras is a pushout when it satisfies the universal
property for algebra homomorphisms: for every `R'`-algebra `T` and every
`g : S →+* T` compatible with the maps from `R`, there is a unique
`R'`-algebra map `S' →ₐ[R'] T` extending `g`. The rings may lie in
independent universes; it suffices to quantify `T` in the maximum of the
universes of `S`, `R'`, and `S'`.

This is the hands-on criterion for recognizing pushouts (tensor products)
without computing the tensor product: it is used to identify fiber
products of schemes, base changes, and tensor-product decompositions from
their mapping properties.

Formalized by `Algebra.isPushout_of_forall_existsUnique_algHom_comp_eq`, a theorem declared in [MathlibExt/Algebra/Algebra/IsPushout.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Algebra/IsPushout.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/index.html#is-pushout-of-forall-exists-unique-alg-h).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Étale algebras, norms and differentials](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/algebras-and-differentials)
