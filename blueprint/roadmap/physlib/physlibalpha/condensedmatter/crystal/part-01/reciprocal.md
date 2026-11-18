---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.phase, CondensedMatter.Crystal.dualCharacter, CondensedMatter.Crystal.reciprocalLattice, CondensedMatter.Crystal.dualCharacter_apply, CondensedMatter.Crystal.phase_add, CondensedMatter.Crystal.dualCharacter_eq_one_iff, CondensedMatter.Crystal.dualCharacter_add_of_mem, CondensedMatter.Crystal.latticeBasis
statement: formalized
proof: formalized
---

# Reciprocal lattice

The module `PhyslibAlpha.CondensedMatter.Crystal.Reciprocal`, [PhyslibAlpha/CondensedMatter/Crystal/Reciprocal.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Reciprocal.lean): 11 declarations, 11 with a docstring.

## i. Overview

> A Bravais lattice with primitive translations `a₁, …, a_d` in Euclidean space acts on
> functions of position by translation. A plane wave `r ↦ exp(i k · r)` of wave vector `k`
> restricts to the lattice as the character `n ↦ exp(i Σ_j n_j ⟨a_j, k⟩)` of the translation
> group `ℤ^d`. Two wave vectors give the same character exactly when they differ by an element of
> the reciprocal lattice, the set of `k` with `⟨a_j, k⟩ ∈ 2π ℤ` for every `j`. The Brillouin zone
> is the quotient of wave-vector space by this lattice, and it is the Pontryagin dual of the
> translation group.
>
> `dualCharacter a k` is the character of `ℤ^d` determined by the wave vector `k`.
> `reciprocalLattice a` is its kernel in wave-vector space. For `d` independent vectors in
> `ℝ^d`, `reciprocalBasis` is the basis `b_i` with `⟨a_j, b_i⟩ = 2π δ_ij`, and
> `dualCharacter_surjective` states that every character of `ℤ^d` arises from a wave vector, so
> that wave-vector space modulo the reciprocal lattice is the full dual.

## ii. Key results

> - `dualCharacter` : the character of the translation group given by a wave vector.
> - `reciprocalLattice` : the wave vectors whose plane wave is trivial on the lattice.
> - `dualCharacter_eq_one_iff` : the kernel of `dualCharacter` is the reciprocal lattice.
> - `reciprocalBasis` : the basis `b_i` with `⟨a_j, b_i⟩ = 2π δ_ij`.
> - `dualCharacter_surjective` : every character of the translation group is a plane wave.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 5.

## A. Characters from wave vectors

**`CondensedMatter.Crystal.phase`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Reciprocal.lean#L65).

> The phase accumulated by a plane wave of wave vector `k` under the lattice translation
> `n`.

```lean
noncomputable def phase (k : EuclideanSpace ℝ (Fin D)) (n : Multiplicative (Fin d → ℤ)) : ℝ
```

**`CondensedMatter.Crystal.dualCharacter`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Reciprocal.lean#L69).

> The character of the translation group `ℤ^d` given by the plane wave of wave vector `k`.

```lean
noncomputable def dualCharacter (k : EuclideanSpace ℝ (Fin D)) :
    PontryaginDual (Multiplicative (Fin d → ℤ))
```

**`CondensedMatter.Crystal.reciprocalLattice`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Reciprocal.lean#L81).

> The reciprocal lattice: wave vectors whose plane wave is trivial on every lattice
> translation.

```lean
def reciprocalLattice : AddSubgroup (EuclideanSpace ℝ (Fin D))
```

**`CondensedMatter.Crystal.dualCharacter_apply`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Reciprocal.lean#L93).

> Evaluating the character of a wave vector gives the exponential of the phase.

```lean
lemma dualCharacter_apply (k : EuclideanSpace ℝ (Fin D)) (n : Multiplicative (Fin d → ℤ)) :
    dualCharacter a k n = Circle.exp (phase a k n)
```

**`CondensedMatter.Crystal.phase_add`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Reciprocal.lean#L97).

> The phase of a lattice translation is additive in the wave vector.

```lean
lemma phase_add (k l : EuclideanSpace ℝ (Fin D)) (n : Multiplicative (Fin d → ℤ)) :
    phase a (k + l) n = phase a k n + phase a l n
```

**`CondensedMatter.Crystal.dualCharacter_eq_one_iff`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Reciprocal.lean#L102).

> A wave vector gives the trivial character exactly when it lies in the reciprocal lattice.

```lean
lemma dualCharacter_eq_one_iff (k : EuclideanSpace ℝ (Fin D)) :
    dualCharacter a k = 1 ↔ k ∈ reciprocalLattice a
```

**`CondensedMatter.Crystal.dualCharacter_add_of_mem`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Reciprocal.lean#L124).

> Wave vectors differing by a reciprocal lattice vector give the same character.

```lean
lemma dualCharacter_add_of_mem {k l : EuclideanSpace ℝ (Fin D)}
    (hl : l ∈ reciprocalLattice a) : dualCharacter a (k + l) = dualCharacter a k
```

## B. The reciprocal basis

**`CondensedMatter.Crystal.latticeBasis`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Reciprocal.lean#L143).

> The basis of space formed by independent primitive translations.

```lean
noncomputable def latticeBasis (ha : LinearIndependent ℝ a) :
    Module.Basis (Fin d) ℝ (EuclideanSpace ℝ (Fin d))
```

**`CondensedMatter.Crystal.reciprocalBasis`**, a def, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Reciprocal.lean#L148).

> The reciprocal basis `b_i`, characterized by `⟨a_j, b_i⟩ = 2π δ_ij`.

```lean
noncomputable def reciprocalBasis (ha : LinearIndependent ℝ a) (i : Fin d) :
    EuclideanSpace ℝ (Fin d)
```

**`CondensedMatter.Crystal.inner_reciprocalBasis`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Reciprocal.lean#L154).

> The reciprocal basis is dual to the primitive translations up to the factor `2π`.

```lean
lemma inner_reciprocalBasis (ha : LinearIndependent ℝ a) (i j : Fin d) :
    ⟪a j, reciprocalBasis ha i⟫ = if i = j then 2 * Real.pi else 0
```

**`CondensedMatter.Crystal.dualCharacter_surjective`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Reciprocal.lean#L161).

> Every character of the translation group is the plane wave of some wave vector.

```lean
lemma dualCharacter_surjective (ha : LinearIndependent ℝ a) :
    Function.Surjective (dualCharacter a)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/Reciprocal.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Reciprocal.lean)
