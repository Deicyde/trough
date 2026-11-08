---
declaration: theorem
origin: cited
lean: TauCeti.exists_linearEquiv_and_isCompl_biSup_ne
statement: formalized
proof: formalized
---

# Azumaya's exchange lemma

Let `M` be the internal direct sum of a finite family `Q` of
indecomposable submodules, and let `N` be a direct summand of `M` whose endomorphism ring is local
(so in particular `N` is nonzero). Then `N` is isomorphic to one of the `Q i₀`, and can be exchanged
for it: `N` and the remaining summands `⨆ j ≠ i₀, Q j` are complementary in `M`.

The locality of `Module.End A N` is what Fitting's lemma
`TauCeti.isLocalRing_end_of_isIndecomposable` supplies when `M` has finite length.

```lean
TauCeti.exists_linearEquiv_and_isCompl_biSup_ne.{u, v, w} {A : Type u} {M : Type v} [Ring A]
  [AddCommGroup M] [_root_.Module A M] {ι : Type w} [Finite ι] {Q : ι → Submodule A M}
  (hQi : iSupIndep Q) (hQt : ⨆ i, Q i = ⊤)
  (hQind : ∀ (i : ι), TauCeti.IsIndecomposableModule A ↥(Q i)) {N S : Submodule A M}
  [IsLocalRing (Module.End A ↥N)] (hNS : IsCompl N S) :
  ∃ i₀, Nonempty (↥N ≃ₗ[A] ↥(Q i₀)) ∧ IsCompl N (⨆ j, ⨆ (_ : j ≠ i₀), Q j)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_linearEquiv_and_isCompl_biSup_ne`](https://taucetiproject.org/docs/TauCeti/RingTheory/KrullSchmidt/Exchange.html#TauCeti.exists_linearEquiv_and_isCompl_biSup_ne).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_linearEquiv_and_isCompl_biSup_ne`](https://taucetiproject.org/docs/TauCeti/RingTheory/KrullSchmidt/Exchange.html#TauCeti.exists_linearEquiv_and_isCompl_biSup_ne)
- [Source of `TauCeti.exists_linearEquiv_and_isCompl_biSup_ne` in TauCeti/RingTheory/KrullSchmidt/Exchange.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/KrullSchmidt/Exchange.lean#L79)
