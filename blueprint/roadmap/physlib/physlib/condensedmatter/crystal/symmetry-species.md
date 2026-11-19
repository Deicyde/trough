---
declaration: module
origin: cited
lean: Physlib.CondensedMatter.Crystal.Symmetry.speciesGroup, Physlib.CondensedMatter.Crystal.Symmetry.mem_speciesGroup_iff, Physlib.CondensedMatter.Crystal.Symmetry.ofParts_mem_speciesGroup_iff, Physlib.CondensedMatter.Crystal.Symmetry.translations_le_speciesGroup, Physlib.CondensedMatter.Crystal.Symmetry.speciesGroup_const, Physlib.CondensedMatter.Crystal.Symmetry.speciesGroup_eq_ker_of_injective
statement: formalized
proof: formalized
---

# Species-preserving crystal symmetries

The module `Physlib.CondensedMatter.Crystal.Symmetry.Species`, [Physlib/CondensedMatter/Crystal/Symmetry/Species.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Species.lean): 7 declarations (1 instance with no name), 7 with a docstring.

> The symmetries of a crystal that keep every atom on a site of its own species.

## i. Overview

> A species assignment gives each label of the unit cell a species, for example a chemical
> element. Graphene and hexagonal boron nitride share the honeycomb lattice with two sites per
> cell. In graphene both sites carry carbon and the inversion through the centre of a bond
> exchanges them. In boron nitride one site carries boron and the other nitrogen. The same
> inversion would put boron where nitrogen was, so it is no longer a symmetry.
>
> A symmetry acts on species assignments by relabelling. The symmetries preserving an assignment
> `q` form its stabilizer. Only the permutation `σ` of the labels matters: a symmetry preserves `q`
> exactly when `q ∘ σ = q`. Lattice automorphisms and shifts are unrestricted. A single species
> allows every symmetry. Distinct species on all labels allow exactly the symmetries that fix
> every label.

## ii. Key results

> - `Crystal.Symmetry.speciesGroup` : the symmetries preserving a species assignment.
> - `Crystal.Symmetry.mem_speciesGroup_iff` : a symmetry preserves `q` exactly when `q ∘ σ = q`.
> - `Crystal.Symmetry.speciesGroup_eq_ker_of_injective` : distinct species allow exactly the
>   symmetries that fix every label.

## iv. References

> * None.

## A. The species group

**An instance with no name**, [line 60](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Species.lean#L60).

> A symmetry carries the species of each label to the image label: `(φ • q) (σ i) = q i`.

```lean
local instance : MulAction (Symmetry C) (Species C Q)
```

**`Physlib.CondensedMatter.Crystal.Symmetry.speciesGroup`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Species.lean#L63).

> The symmetries preserving the species assignment `q`.

```lean
def speciesGroup (q : Species C Q) : Subgroup (Symmetry C)
```

**`Physlib.CondensedMatter.Crystal.Symmetry.mem_speciesGroup_iff`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Species.lean#L67).

> A symmetry preserves `q` exactly when its label permutation `σ` satisfies `q ∘ σ = q`.

```lean
lemma mem_speciesGroup_iff {q : Species C Q} : φ ∈ speciesGroup q ↔ q ∘ φ.labelPerm = q
```

**`Physlib.CondensedMatter.Crystal.Symmetry.ofParts_mem_speciesGroup_iff`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Species.lean#L74).

> A symmetry built from `A`, `σ` and `s` preserves `q` exactly when `q ∘ σ = q`.

```lean
lemma ofParts_mem_speciesGroup_iff {q : Species C Q} (A : G ≃+ G) (σ : Equiv.Perm C.UnitCell)
    (s : C.UnitCell → G) : ofParts C A σ s ∈ speciesGroup q ↔ q ∘ σ = q
```

**`Physlib.CondensedMatter.Crystal.Symmetry.translations_le_speciesGroup`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Species.lean#L79).

> Every lattice translation preserves every species assignment.

```lean
lemma translations_le_speciesGroup (q : Species C Q) : translations C ≤ speciesGroup q
```

## B. Uniform and distinct species

**`Physlib.CondensedMatter.Crystal.Symmetry.speciesGroup_const`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Species.lean#L86).

> A single species allows every symmetry.

```lean
lemma speciesGroup_const (c : Q) : speciesGroup (C := C) (Function.const _ c) = ⊤
```

**`Physlib.CondensedMatter.Crystal.Symmetry.speciesGroup_eq_ker_of_injective`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Species.lean#L90).

> Distinct species on all labels allow exactly the symmetries that fix every label.

```lean
lemma speciesGroup_eq_ker_of_injective {q : Species C Q} (hq : Function.Injective q) :
    speciesGroup q = (MulAction.toPermHom (Symmetry C) C.UnitCell).ker
```

## Depends on

- [Decomposition of crystal symmetries](symmetry-decomposition.md)

## Sources

- [Physlib/CondensedMatter/Crystal/Symmetry/Species.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Species.lean)
