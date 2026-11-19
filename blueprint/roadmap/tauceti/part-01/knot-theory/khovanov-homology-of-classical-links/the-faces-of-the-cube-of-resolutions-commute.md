---
declaration: theorem
origin: cited
lean: TauCeti.PDCode.resolutionEdgeMap_comp_resolutionEdgeMap_comm
statement: formalized
proof: formalized
---

# The faces of the cube of resolutions commute

Let `s`, `t₁`, `t₂`, `u` be the states of a
face, where `t₁` changes `s` at `c`, `t₂` changes `s` at `c'`, and `u` changes both. If all four
edges are saddles, the composite of the edge maps through `t₁` equals the composite through
`t₂`.

```lean
TauCeti.PDCode.resolutionEdgeMap_comp_resolutionEdgeMap_comm.{u} {n : ℕ} (D : TauCeti.PDCode n)
  {s t₁ t₂ u : Fin n → Bool} {c c' : Fin n} (hst₁ : ∀ (j : Fin n), j ≠ c → s j = t₁ j)
  (hc₁ : s c ≠ t₁ c) (ht₁u : ∀ (j : Fin n), j ≠ c' → t₁ j = u j) (hc₁' : t₁ c' ≠ u c')
  (hst₂ : ∀ (j : Fin n), j ≠ c' → s j = t₂ j) (hc₂ : s c' ≠ t₂ c')
  (ht₂u : ∀ (j : Fin n), j ≠ c → t₂ j = u j) (hc₂' : t₂ c ≠ u c)
  (h₁ : (D.circlesAt s c).card = 2 ∨ (D.circlesAt t₁ c).card = 2)
  (h₁' : (D.circlesAt t₁ c').card = 2 ∨ (D.circlesAt u c').card = 2)
  (h₂ : (D.circlesAt s c').card = 2 ∨ (D.circlesAt t₂ c').card = 2)
  (h₂' : (D.circlesAt t₂ c).card = 2 ∨ (D.circlesAt u c).card = 2) (R : Type u) [CommSemiring R] :
  D.resolutionEdgeMap ht₁u hc₁' h₁' R ∘ₗ D.resolutionEdgeMap hst₁ hc₁ h₁ R =
    D.resolutionEdgeMap ht₂u hc₂' h₂' R ∘ₗ D.resolutionEdgeMap hst₂ hc₂ h₂ R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PDCode.resolutionEdgeMap_comp_resolutionEdgeMap_comm`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Resolution/Edge.html#TauCeti.PDCode.resolutionEdgeMap_comp_resolutionEdgeMap_comm).

## Sources

- [Tau Ceti documentation: `TauCeti.PDCode.resolutionEdgeMap_comp_resolutionEdgeMap_comm`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Resolution/Edge.html#TauCeti.PDCode.resolutionEdgeMap_comp_resolutionEdgeMap_comm)
- [Source of `TauCeti.PDCode.resolutionEdgeMap_comp_resolutionEdgeMap_comm` in TauCeti/KnotTheory/Khovanov/Resolution/Edge.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Khovanov/Resolution/Edge.lean#L139)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KhovanovHomology/STATUS.md)
