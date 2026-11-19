---
declaration: theorem
origin: cited
lean: TauCeti.GraphOfGroups.normalForm_eq_normalForm_iff
statement: formalized
proof: formalized
---

# Normal form theorem

two `𝔸`-paths are homotopic exactly when they have the same normal
form.

```lean
TauCeti.GraphOfGroups.normalForm_eq_normalForm_iff.{u, v, w, x} {Γ : TauCeti.SerreGraph}
  {𝔸 : TauCeti.GraphOfGroups Γ} (d : 𝔸.Transversal) {a b : Γ.V}
  {p q : 𝔸.Path { as := a } { as := b }} :
  TauCeti.GraphOfGroups.normalForm d p = TauCeti.GraphOfGroups.normalForm d q ↔ p.Homotopic q
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GraphOfGroups.normalForm_eq_normalForm_iff`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GraphOfGroups/NormalForm.html#TauCeti.GraphOfGroups.normalForm_eq_normalForm_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.GraphOfGroups.normalForm_eq_normalForm_iff`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GraphOfGroups/NormalForm.html#TauCeti.GraphOfGroups.normalForm_eq_normalForm_iff)
- [Source of `TauCeti.GraphOfGroups.normalForm_eq_normalForm_iff` in TauCeti/GroupTheory/GraphOfGroups/NormalForm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/GraphOfGroups/NormalForm.lean#L907)
