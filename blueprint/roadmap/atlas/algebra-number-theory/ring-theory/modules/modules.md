---
declaration: section
origin: cited
lean: MathlibExt.Algebra.CommutativeAlgebra.EakinNagataWanted.eakin_nagata, IsLocalization.bijective_algebraMap_of_faithfullyFlat, Module.Invertible.of_projective_of_forall_finrank_eq_one, MathlibExt.Algebra.Module.KaplanskyProjectiveWanted.kaplansky_projective_local_free, MathlibExt.Algebra.Module.QuillenSuslinWanted.quillen_suslin
statement: formalized
proof: formalized
---

# Modules over commutative rings: its own results

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/modules/index.html).

Projective, free and finitely generated modules over commutative rings and module-finite extensions: Kaplansky's theorem, the Quillen–Suslin theorem, descent of Noetherianness (Eakin–Nagata) and the direct summand theorem.

## Eakin–Nagata theorem

Let $A$ and $B$ be commutative rings and let $B$ be an $A$-algebra
that is finitely generated as an $A$-module. If the structure map $A \to B$ is injective and $B$
is Noetherian, then $A$ is Noetherian.

## Sources

- P. M. Eakin Jr., 'The converse to a well known theorem on Noetherian rings', Mathematische Annalen 177 (1968), 278-282, DOI 10.1007/BF01350720.

Formalized by `MathlibExt.Algebra.CommutativeAlgebra.EakinNagataWanted.eakin_nagata`, a theorem declared in [MathlibExt/Algebra/CommutativeAlgebra/EakinNagata.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/CommutativeAlgebra/EakinNagata.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/modules/index.html#eakin-nagata).

## Faithfully flat algebras inside a localization equal the base ring

A faithfully flat `R`-algebra `S` which embeds compatibly in a localization
`K` of `R` has bijective structure map. No restriction on the denominators
or domain assumptions on the rings are required.

Formalized by `IsLocalization.bijective_algebraMap_of_faithfullyFlat`, a theorem declared in [MathlibExt/RingTheory/Flat/FaithfullyFlat/Localization.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Flat/FaithfullyFlat/Localization.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/modules/index.html#bijective-algebra-map-of-faithfully-flat).

## Finite projective modules of fiberwise rank one are invertible

A finite projective module whose base change to every field has rank
one is invertible.

This is the standard criterion for a module to define a line bundle: it
is used to show that projective modules of constant rank one are
invertible, to construct Picard group elements, and to recognize
invertible sheaves from their fibers.

Formalized by `Module.Invertible.of_projective_of_forall_finrank_eq_one`, a theorem declared in [MathlibExt/Algebra/Module/InvertibleRankOne.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Module/InvertibleRankOne.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/modules/index.html#of-projective-of-forall-finrank-eq-one).

## Kaplansky's theorem on projective modules over local rings

Every projective module over a
commutative local ring is free.

## Sources

- I. Kaplansky, Projective Modules, Ann. Math. 68 (1958), 372-377, DOI 10.2307/1970252.

Formalized by `MathlibExt.Algebra.Module.KaplanskyProjectiveWanted.kaplansky_projective_local_free`, a theorem declared in [MathlibExt/Algebra/Module/KaplanskyProjective.lean, line 850](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Module/KaplanskyProjective.lean#L850). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/modules/index.html#kaplansky-projective-local-free).

## Quillen–Suslin theorem

Let $k$ be a field and let $n$ be a natural number. Every finitely
generated projective module over the polynomial ring $k[x_1, \dots, x_n]$ in $n$ variables is
free.

Proof: The argument follows Quillen's induction and patching route, using Roberts'
idempotent-matrix proof of local Horrocks; see Quillen (1976), Lam, Lang, and Dicks.

## Sources

- Serre's conjecture proved by D. Quillen, Invent. Math. 36 (1976) and A. A. Suslin, Dokl. Akad. Nauk SSSR 229 (1976); Lam, Serre's Problem; Lean states field case over `MvPolynomial (Fin n) k` with PID generalization existing.

Formalized by `MathlibExt.Algebra.Module.QuillenSuslinWanted.quillen_suslin`, a theorem declared in [MathlibExt/Algebra/Module/QuillenSuslin.lean, line 2224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Module/QuillenSuslin.lean#L2224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/modules/index.html#quillen-suslin).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Modules over commutative rings](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/modules/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/modules)
