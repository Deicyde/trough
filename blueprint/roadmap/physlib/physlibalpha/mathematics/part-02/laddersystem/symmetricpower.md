---
declaration: module
origin: cited
lean: LadderSystem.vacuumSpanSymEquiv, LadderSystem.vacuumSpanSymEquiv_single
statement: formalized
proof: formalized
---

# The excitation sector is the symmetric power

The module `PhyslibAlpha.Mathematics.LadderSystem.SymmetricPower`, [PhyslibAlpha/Mathematics/LadderSystem/SymmetricPower.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/SymmetricPower.lean): 2 declarations, 2 with a docstring.

> The excitation-number sector `vacuumSpan L Ω n` is linearly isomorphic to `Sym^n(K^d)`.

## i. Overview

> `vacuumSpan L Ω n` is linearly isomorphic to the `n`-th symmetric power of `K^d` -- concretely, to
> the free `K`-vector space on `Sym (Fin d) n` (Mathlib's own type of size-`n` multisets on `Fin d`,
> the standard combinatorial model of `Sym^n(K^d)`'s natural basis once a basis `e_1,…,e_d` of `K^d`
> is fixed: a multiset `{i_1,…,i_n}` names the basis vector `e_{i_1} ⊙ ⋯ ⊙ e_{i_n}`). The
> isomorphism sends this basis to the occupation-number states, i.e. it is exactly
> `OccupationBasis.lean`'s `vacuumBasis` reindexed along `countFunEquivSym`.

## ii. Key results

> - `LadderSystem.vacuumSpanSymEquiv` : `(Sym (Fin d) n →₀ K) ≃ₗ[K] vacuumSpan L Ω n`.
> - `LadderSystem.vacuumSpanSymEquiv_single` : the basis vector of a multiset is sent to the
>   occupation-number state of its count function.

## iv. References

> * None.

## A. The isomorphism with the symmetric power

**`LadderSystem.vacuumSpanSymEquiv`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/SymmetricPower.lean#L58).

> `vacuumSpan L Ω n` is linearly isomorphic to `Sym^n(K^d)` (realized as the free `K`-module
> on `Sym (Fin d) n`), matching the natural monomial-type basis on one side to the occupation-number
> basis on the other.

```lean
noncomputable def vacuumSpanSymEquiv {Ω : V} (P : L.HasVacuum Ω) (n : ℕ) :
    (Sym (Fin d) n →₀ K) ≃ₗ[K] L.vacuumSpan Ω n
```

## B. The image of the basis vectors

**`LadderSystem.vacuumSpanSymEquiv_single`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/SymmetricPower.lean#L70).

> The isomorphism sends the basis vector for multiset `s` to the occupation-number state with
> that multiset's count function.

```lean
lemma vacuumSpanSymEquiv_single {Ω : V} (P : L.HasVacuum Ω) (n : ℕ) (s : Sym (Fin d) n) :
    (L.vacuumSpanSymEquiv P n (Finsupp.single s 1) : V)
      = L.word (countWord d ((countFunEquivSym d n).symm s).1) Ω
```

## Depends on

- [The occupation-number basis](occupationbasis.md)

## Sources

- [PhyslibAlpha/Mathematics/LadderSystem/SymmetricPower.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/SymmetricPower.lean)
